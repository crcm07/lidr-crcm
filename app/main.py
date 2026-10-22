from fastapi import FastAPI

from app.routers.estimations import router as estimations_router

app = FastAPI(title="Estimator CAG")
app.include_router(estimations_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}