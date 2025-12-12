import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [symbol, setSymbol] = useState('BTCUSDT')
  const [quantity, setQuantity] = useState('0.001')
  const [price, setPrice] = useState('98500')
  const [side, setSide] = useState('BUY')
  const [response, setResponse] = useState(null)
  const [loading, setLoading] = useState(false)
  const [ping, setPing] = useState(null)

  const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000'

  useEffect(() => {
    checkPing()
  }, [])

  const checkPing = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/ping`)
      const data = await res.json()
      setPing(data)
    } catch (err) {
      console.error(err)
      setPing({ status: 'error', message: 'Backend Offline' })
    }
  }

  const handleOrder = async (type) => {
    setLoading(true)
    setResponse(null)
    const endpoint = type === 'MARKET' ? '/api/market' : '/api/limit'
    
    const payload = {
      symbol,
      side,
      quantity: parseFloat(quantity)
    }

    if (type === 'LIMIT') {
      payload.price = parseFloat(price)
    }

    try {
      const res = await fetch(`${API_BASE}${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      const data = await res.json()
      setResponse(data)
    } catch (err) {
      setResponse({ error: 'Network Error', details: err.message })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      {/* Header / Status Bar */}
      <div className="status-bar">
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <h1 style={{ fontSize: '1.2rem', marginBottom: 0, marginRight: '1.5rem' }}>
            FutureTrade <span style={{ color: 'var(--accent-color)' }}>Pro</span>
          </h1>
          <div className="market-item">
            <span className="market-label">Symbol</span>
            <span className="market-value">{symbol}</span>
          </div>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <span className={`status-indicator ${ping?.status === 'ok' ? 'status-online' : 'status-offline'}`}></span>
          <span style={{ color: ping?.status === 'ok' ? 'var(--buy-color)' : 'var(--sell-color)' }}>
            {ping ? (ping.status === 'ok' ? `System Online (DRY_RUN: ${ping.dry_run})` : 'System Offline') : 'Connecting...'}
          </span>
        </div>
      </div>

      <div className="dashboard-grid">
        {/* Order Entry Card */}
        <div className="card">
          <div className="card-header">Place Order</div>
          
          <div className="side-toggle">
            <div 
              className={`side-option ${side === 'BUY' ? 'active buy' : ''}`}
              onClick={() => setSide('BUY')}
            >
              Buy Long
            </div>
            <div 
              className={`side-option ${side === 'SELL' ? 'active sell' : ''}`}
              onClick={() => setSide('SELL')}
            >
              Sell Short
            </div>
          </div>

          <div className="form-group">
            <label>Symbol</label>
            <input 
              className="input-control"
              value={symbol} 
              onChange={e => setSymbol(e.target.value.toUpperCase())}
              placeholder="e.g. BTCUSDT" 
            />
          </div>

          <div className="form-group">
            <label>Quantity</label>
            <input 
              type="number" 
              className="input-control"
              value={quantity} 
              onChange={e => setQuantity(e.target.value)} 
              step="0.001"
            />
          </div>

          <div className="form-group">
            <label>Price (Limit Orders)</label>
            <input 
              type="number" 
              className="input-control"
              value={price} 
              onChange={e => setPrice(e.target.value)} 
            />
          </div>

          <div className="btn-group">
            <button 
              className="btn btn-buy" 
              disabled={loading}
              onClick={() => handleOrder('MARKET')}
            >
              Market {side}
            </button>
            <button 
              className="btn btn-sell" 
              disabled={loading}
              onClick={() => handleOrder('LIMIT')}
              style={{ backgroundColor: 'var(--bg-tertiary)', color: 'var(--text-primary)' }} 
            >
              Limit {side}
            </button>
          </div>
        </div>

        {/* Console / Response Card */}
        <div className="card">
          <div className="card-header">Execution Console</div>
          <div style={{ height: 'calc(100% - 40px)', display: 'flex', flexDirection: 'column' }}>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              > Ready to execute trades.<br/>
              > Mode: {ping?.dry_run ? 'SIMULATION (Safe)' : 'LIVE (Risk)'}
            </p>
            
            {response ? (
              <div className="json-response">
                {JSON.stringify(response, null, 2)}
              </div>
            ) : (
              <div style={{ 
                flex: 1, 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center', 
                color: 'var(--bg-tertiary)',
                border: '2px dashed var(--bg-tertiary)',
                borderRadius: '4px',
                marginTop: '1rem'
              }}>
                Awaiting Order Execution...
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
