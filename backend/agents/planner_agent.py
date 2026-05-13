from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    name = "Planner Agent"
    role = "任务理解与计划拆解"

    def process(self, input_text: str, context: dict) -> str:
        if any(word in input_text for word in ["客服", "退款", "投诉", "订单"]):
            task_type = "AI 客服自动化"
        elif any(word in input_text for word in ["营销", "内容", "小红书", "短视频"]):
            task_type = "内容运营自动化"
        elif any(word in input_text for word in ["数据", "表格", "分析"]):
            task_type = "数据分析自动化"
        else:
            task_type = "通用复杂任务自动化"

        plan = f'''
任务类型：{task_type}

任务拆解：
1. 明确业务场景、目标用户和核心痛点
2. 提取任务中的关键对象、约束条件和输出要求
3. 设计多 Agent 分工，包括计划、分析、执行、审核和报告
4. 生成可执行方案、流程或结构化内容
5. 对输出进行完整性、准确性和风险审核
6. 汇总最终报告，并记录运行日志
'''
        context["task_type"] = task_type
        context["plan"] = plan.strip()
        return plan.strip()
