import React, { useState } from 'react'
import { runWorkflow } from './api.js'

const sampleTask = '帮我设计一个 AI 客服 Agent，用于自动处理退款、投诉、订单查询，并输出完整落地方案。'

export default function App() {
  const [task, setTask] = useState(sampleTask)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  async function handleRun() {
    setLoading(true)
    setError('')
    setResult(null)

    try {
      const data = await runWorkflow(task)
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <header className="hero">
        <div>
          <p className="badge">High-Pass AI Agent Demo</p>
          <h1>多 Agent 协同 AI 自动化工作流平台</h1>
          <p className="subtitle">
            支持任务理解、任务拆解、需求分析、方案执行、质量审核与最终报告生成。
          </p>
        </div>
      </header>

      <section className="panel">
        <h2>输入任务</h2>
        <textarea
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="请输入你要交给 AI Agent 处理的复杂任务"
        />
        <button onClick={handleRun} disabled={loading || !task.trim()}>
          {loading ? '多 Agent 正在协同处理...' : '启动多 Agent 工作流'}
        </button>
        {error && <p className="error">{error}</p>}
      </section>

      {result && (
        <>
          <section className="metrics">
            <div>
              <span>Task ID</span>
              <strong>{result.task_id}</strong>
            </div>
            <div>
              <span>Agent 数量</span>
              <strong>{result.metrics.agent_count}</strong>
            </div>
            <div>
              <span>总耗时</span>
              <strong>{result.metrics.total_duration_ms} ms</strong>
            </div>
            <div>
              <span>效率提升</span>
              <strong>{result.metrics.estimated_efficiency_gain}</strong>
            </div>
          </section>

          <section className="timeline">
            <h2>Agent 执行链路</h2>
            {result.steps.map((step, index) => (
              <div className="step" key={index}>
                <div className="stepHeader">
                  <div>
                    <span className="index">{index + 1}</span>
                    <strong>{step.agent_name}</strong>
                    <p>{step.role}</p>
                  </div>
                  <span className="status">{step.status} · {step.duration_ms}ms</span>
                </div>
                <pre>{step.output}</pre>
              </div>
            ))}
          </section>

          <section className="report">
            <h2>最终报告</h2>
            <pre>{result.final_report}</pre>
          </section>
        </>
      )}
    </div>
  )
}
