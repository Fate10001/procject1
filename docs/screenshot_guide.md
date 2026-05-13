# 截图指南

为了让申请材料更可信，建议准备以下截图：

## 截图 1：前端首页

打开：

```txt
http://127.0.0.1:5173
```

截图内容：

- 项目标题
- 任务输入框
- 运行按钮

## 截图 2：多 Agent 执行结果

输入示例任务：

```txt
帮我设计一个 AI 客服 Agent，用于自动处理退款、投诉、订单查询，并输出完整落地方案。
```

截图内容：

- Planner Agent 输出
- Researcher Agent 输出
- Executor Agent 输出
- Reviewer Agent 输出
- Reporter Agent 输出

## 截图 3：后端接口文档

打开：

```txt
http://127.0.0.1:8000/docs
```

截图内容：

- `/api/run`
- 请求体
- 返回体

## 截图 4：运行日志

打开：

```txt
backend/logs/
```

截图内容：

- task_id
- agent_name
- role
- status
- duration_ms
- output
