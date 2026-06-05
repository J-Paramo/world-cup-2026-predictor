def load_css():
    return """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 40%,
            #fff1f2 100%
        );
    }

    .block-container {
        max-width: 650px;
        padding-top: 3rem;
        margin: auto;
    }

    h1 {
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        color: #0f172a !important;
        margin-bottom: 5px;
        letter-spacing: -0.5px;
    }

    .stMarkdown p {
        text-align: center;
        color: #64748b;
        font-size: 14px;
    }

    div[data-testid="stVerticalBlock"] {
        background: white;
        border-radius: 18px;
        padding: 22px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 8px 30px rgba(0,0,0,0.06);
    }

    div[data-baseweb="select"] {
        border-radius: 10px;
    }

    div.stButton > button {
        width: 100%;
        padding: 0.7rem;
        border-radius: 10px;
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        color: white;
        font-weight: 600;
        border: none;
        transition: 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 20px rgba(59,130,246,0.25);
    }

    div[data-testid="metric-container"] {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 10px;
    }

    label {
        color: #334155 !important;
        font-weight: 500;
    }

    .stMarkdown, .stMarkdown p,
    h1, h2, h3,
    label {
        color: #0f172a !important;
    }

    div[data-baseweb="select"] input {
        color: #0f172a !important;
        -webkit-text-fill-color: #0f172a !important;
    }
    
    div[data-testid="metric-container"] label,
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #0f172a !important;
    }
    

    html {
        -webkit-text-size-adjust: 100%;
    }

    </style>
    """