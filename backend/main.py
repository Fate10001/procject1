from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models.schemas import TaskRequest, WorkflowResponse
from services.workflow_engine import WorkflowEngine

app = FastAPI(
    title="High-Pass Multi-Agent AI Workflow Platform",
    description="多 Agent 协同 AI 自动化工作流平台",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = WorkflowEngine()

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "High-Pass Multi-Agent AI Workflow Platform is running."
    }

@app.post("/api/run", response_model=WorkflowResponse)
def run_workflow(request: TaskRequest):
    return engine.run(request.task)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
