export async function runWorkflow(task) {
  const response = await fetch('http://127.0.0.1:8000/api/run', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ task })
  })

  if (!response.ok) {
    throw new Error('请求失败，请确认后端服务已经启动')
  }

  return response.json()
}
