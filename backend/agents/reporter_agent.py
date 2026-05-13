from agents.base_agent import BaseAgent

class ReporterAgent(BaseAgent):
    name = "Reporter Agent"
    role = "最终报告生成"

    def process(self, input_text: str, context: dict) -> str:
        result = f'''
# 多 Agent 协同任务处理报告

## 1. 用户任务

{input_text}

## 2. 任务类型

{context.get("task_type", "未知")}

## 3. 执行计划

{context.get("plan", "")}

## 4. 需求分析

{context.get("research", "")}

## 5. 执行方案

{context.get("execution", "")}

## 6. 审核结果

{context.get("review", "")}

## 7. 项目价值

该多 Agent 系统实现了从任务理解、任务拆解、执行处理、质量审核到最终报告生成的完整自动化链路。系统适用于 AI 客服、内容运营、数据整理、项目规划等场景，可显著减少人工重复操作，提升输出质量和处理效率。
'''
        context["final_report"] = result.strip()
        return result.strip()
