# 项目详细介绍

## 项目名称

High-Pass Multi-Agent AI Workflow Platform

## 项目定位

这是一个面向复杂任务自动化处理的多 Agent 协同系统。它不是单一聊天机器人，而是一个完整的 AI 工作流平台，能够将用户输入的自然语言任务拆解为多个阶段，并由不同 Agent 分工处理。

## 核心功能

### 1. 自然语言任务输入

用户可以在前端输入任意复杂任务，例如：

- 设计 AI 客服系统
- 生成运营活动方案
- 整理数据分析报告
- 拆解项目执行计划
- 生成自动化流程方案

### 2. 多 Agent 协同处理

系统内部包含 5 个 Agent：

#### Planner Agent
负责理解用户目标，判断任务类型，并拆解执行步骤。

#### Researcher Agent
负责提取关键需求、限制条件、业务背景和潜在风险。

#### Executor Agent
负责根据任务计划生成具体方案、流程、内容或结构化输出。

#### Reviewer Agent
负责检查内容是否完整、逻辑是否清晰、是否存在风险点。

#### Reporter Agent
负责整合全部 Agent 输出，生成最终报告。

### 3. 工作流日志

系统会记录：

- task_id
- Agent 名称
- Agent 角色
- 输入内容
- 输出内容
- 执行状态
- 执行耗时
- 执行时间

日志存储在：

```txt
backend/logs/
```

### 4. 前端可视化

前端可以展示：

- 任务输入框
- Agent 执行链路
- 每个 Agent 的输出内容
- 最终报告
- 执行耗时和统计指标

## 技术栈

### 后端

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSONL 日志

### 前端

- React
- Vite
- JavaScript
- CSS

## 项目价值

该项目体现了真实 AI Agent 项目常见的核心能力：

- 任务理解
- 任务拆解
- 多 Agent 协同
- 工作流编排
- 结果审核
- 日志追踪
- 前端可视化
- 可扩展模型接入
