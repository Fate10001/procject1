from agents.base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    name = "Researcher Agent"
    role = "需求分析与信息提取"

    def process(self, input_text: str, context: dict) -> str:
        result = f'''
需求分析：
- 原始任务：{input_text}
- 识别任务类型：{context.get("task_type", "未知")}
- 核心目标：提升处理效率，降低人工重复劳动，统一结果质量
- 关键需求：自动理解输入、拆解任务、执行处理、审核结果、生成报告
- 适用场景：客服自动化、内容生产、运营方案、数据整理、项目规划
- 风险点：输出遗漏、逻辑不一致、敏感内容、异常输入
- 应对方式：引入 Reviewer Agent 和日志追踪机制
'''
        context["research"] = result.strip()
        return result.strip()
