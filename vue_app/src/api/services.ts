export const url = location.href.includes('localhost')
  ? 'http://localhost:8000'
  : location.href.includes('127.0.0.1')
    ? 'http://127.0.0.1:8000'
    : 'https://example.com'

interface Response {
  error: boolean
  message: string
  data?: any
}

class API {
  private url: string

  private requestError(error: unknown) {
    console.error(error)
    return {
      error: true,
      message: error instanceof Error ? error.message : String(error)
    }
  }

  constructor(url: string) {
    this.url = url
  }

  async register({}): Promise<Response> {
    try {
      const request = await fetch(this.url + '/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({})
      })

      return await request.json()
    } catch (error) {
      return this.requestError(error)
    }
  }
}

const api = new API(url)

export default api
