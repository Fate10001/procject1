from pydantic import BaseModel
from typing import List, Dict, Any

class TaskRequest(BaseModel):
    task: str

class AgentStep(BaseModel):
    agent_name: str
    role: str
    status: str
    input: str
    output: str
    duration_ms: int

class WorkflowResponse(BaseModel):
    task_id: str
    original_task: str
    steps: List[AgentStep]
    final_report: str
    metrics: Dict[str, Any]
