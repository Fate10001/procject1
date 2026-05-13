import time
from typing import Dict, Any

class BaseAgent:
    name = "Base Agent"
    role = "Base Role"

    def run(self, input_text: str, context: Dict[str, Any]) -> Dict[str, Any]:
        start = time.time()
        output = self.process(input_text, context)
        duration_ms = int((time.time() - start) * 1000)

        return {
            "agent_name": self.name,
            "role": self.role,
            "status": "success",
            "input": input_text,
            "output": output,
            "duration_ms": duration_ms
        }

    def process(self, input_text: str, context: Dict[str, Any]) -> str:
        raise NotImplementedError
