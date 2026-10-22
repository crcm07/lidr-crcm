import structlog

from app.config import get_settings
from app.context.examples import ESTIMATION_EXAMPLES, format_examples_for_prompt

log = structlog.get_logger()

MAX_TOKENS = 4000


class LLMServiceError(Exception):
    """Raised when the LLM provider call fails."""


def build_system_prompt() -> str:
    """Construct the system prompt with role definition and reference examples."""
    examples_text = format_examples_for_prompt(ESTIMATION_EXAMPLES)
    return (
        "Eres un consultor senior de software con más de 18 años de experiencia en "
        "estimación de proyectos. Tu tarea es producir una estimación detallada de un "
        "proyecto de software a partir de la transcripción de una reunión que te "
        "proporcione el usuario.\n\n"
        "A continuación hay estimaciones de referencia de proyectos anteriores. Úsalas "
        "como guía de estructura, nivel de detalle y precios realistas. Adapta el "
        "contenido al proyecto concreto descrito en la transcripción.\n\n"
        "Tu salida DEBE seguir exactamente este formato:\n"
        "- Título del proyecto como encabezado H2\n"
        "- Una sección llamada 'Descripción del proyecto' con un resumen conciso del "
        "proyecto, su objetivo principal, usuarios objetivo y alcance\n"
        "- Una tabla de desglose de tareas con las columnas: Tarea, Horas, Coste (USD)\n"
        "- Horas totales\n"
        "- Coste total en USD\n"
        "- Composición del equipo recomendado\n"
        "- Duración estimada en semanas\n\n"
        "Usa una tarifa de desarrollador de aproximadamente 62.50 USD/hora (500 USD/día) "
        "y una tarifa de diseñador de aproximadamente 50 USD/hora (400 USD/día). "
        "Proporciona números realistas y bien justificados.\n\n"
        f"{examples_text}"
    )


def generate_estimation(transcription: str) -> dict:
    """Generate a software estimation from a meeting transcription using the configured LLM."""
    settings = get_settings()
    system_prompt = build_system_prompt()

    log.info("generating_estimation", provider=settings.LLM_PROVIDER, model=settings.LLM_MODEL)

    try:
        if settings.LLM_PROVIDER == "openai":
            return _call_openai(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": transcription},
                ],
            )
        else:
            return _call_anthropic(
                system=system_prompt,
                user_message=transcription,
            )
    except LLMServiceError:
        raise
    except Exception as exc:
        log.error("llm_call_failed", error=str(exc), provider=settings.LLM_PROVIDER)
        raise LLMServiceError(f"LLM call failed: {exc}") from exc


def _call_openai(messages: list[dict]) -> dict:
    """Send a chat completion request to the OpenAI API."""
    from openai import OpenAI

    settings = get_settings()
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS,
    )

    usage = response.usage
    log.info(
        "llm_response_received",
        provider="openai",
        input_tokens=usage.prompt_tokens,
        output_tokens=usage.completion_tokens,
    )

    return {
        "estimation": response.choices[0].message.content,
        "model": response.model,
        "provider": "openai",
        "usage": {
            "input_tokens": usage.prompt_tokens,
            "output_tokens": usage.completion_tokens,
            "total_tokens": usage.total_tokens,
        },
    }


def _call_anthropic(system: str, user_message: str) -> dict:
    """Send a message request to the Anthropic API."""
    from anthropic import Anthropic

    settings = get_settings()
    client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    response = client.messages.create(
        model=settings.LLM_MODEL,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user_message}],
    )

    log.info(
        "llm_response_received",
        provider="anthropic",
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
    )

    return {
        "estimation": response.content[0].text,
        "model": response.model,
        "provider": "anthropic",
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
        },
    }