# High-Pass Multi-Agent AI Workflow Platform

这是一个用于展示 AI/Agent 能力的高通过率项目模板，包含完整前后端、多 Agent 协同、任务拆解、执行、审核、报告生成、日志记录和可视化页面。

## 项目亮点

- 前后端完整可运行
- FastAPI 后端
- React + Vite 前端
- 多 Agent 协同工作流
- 5 个核心 Agent：
  - Planner Agent：任务理解与拆解
  - Researcher Agent：需求分析与信息提取
  - Executor Agent：方案生成与执行
  - Reviewer Agent：质量审核与风险检查
  - Reporter Agent：最终报告生成
- 自动生成任务 ID
- 自动记录 JSONL 日志
- 前端展示 Agent 执行链路
- 可作为第 04 题项目描述和第 05 题证明材料

## 项目结构

```txt
high-pass-multi-agent-platform/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── agents/
│   ├── services/
│   └── models/
│
├── frontend/
│   ├── package.json
│   ├── index.html
│   └── src/
│
├── docs/
│   ├── project_description.md
│   ├── submit_answer.md
│   └── screenshot_guide.md
```

## 后端运行

```bash
cd backend
pip install -r requirements.txt
python main.py
```

后端地址：

```txt
http://127.0.0.1:8000
```

接口文档：

```txt
http://127.0.0.1:8000/docs
```

## 前端运行

```bash
cd frontend
npm install
npm run dev
```

前端地址：

```txt
http://127.0.0.1:5173
```

## 推荐测试任务

```txt
帮我设计一个 AI 客服 Agent，用于自动处理退款、投诉、订单查询，并输出完整落地方案。
```

## 提交证明材料建议

建议截图：

1. 前端任务输入页面
2. 多 Agent 执行结果页面
3. 后端接口文档 `/docs`
4. `backend/logs/` 中生成的 JSONL 日志
5. GitHub 仓库 README 页面
