import os
import pandas as pd
from flask import Flask, send_from_directory
from sqlalchemy import create_engine

app = Flask(__name__)

def get_db_engine():
    db_url = os.getenv("DATABASE_URL")
    return create_engine(db_url)

@app.route('/')
def index():
    quality_html = "<p class='text-muted'>Data is being processed...</p>"
    try:
        engine = get_db_engine()
        df_quality = pd.read_sql("SELECT * FROM quality_metrics", engine)
        quality_html = df_quality.to_html(classes='table table-sm table-bordered table-hover mb-0', index=False)
    except Exception:
        quality_html = "<p class='text-danger'>Quality metrics table not found in DB.</p>"

    research_html = "<p class='text-muted'>Research file not found.</p>"
    try:
        df_research = pd.read_csv('/app/static/reports/top5.csv')
        research_html = df_research.to_html(classes='table table-sm table-striped mb-0', index=False)
    except Exception:
        research_html = "<p class='text-muted'>Waiting for research results (top5.csv)...</p>"

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Analytics Dashboard</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <style>
            body {{ background-color: #f4f7f6; font-size: 0.9rem; }}
            .card-custom {{ 
                background: white; 
                padding: 20px; 
                border-radius: 10px; 
                margin-bottom: 20px; 
                border: 1px solid #dee2e6;
                overflow: hidden; 
            }}
            .header-box {{ 
                background: #2c3e50; 
                color: white; 
                padding: 30px; 
                margin-bottom: 30px; 
                border-radius: 0 0 10px 10px; 
            }}
            .table-container {{
                overflow-x: auto;
                max-width: 100%;
            }}
            table {{ font-size: 0.8rem; }}
            img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body class="container">
        <div class="header-box text-center">
            <h1>Community Income Analysis</h1>
            <p>Automated pipeline for processing, analyzing, and visualizing open data.</p>
        </div>

        <div class="row">
            <div class="col-lg-5">
                <div class="card-custom shadow-sm">
                    <h4 class="h5">Data Quality (from DB)</h4>
                    <div class="table-container">
                        {quality_html}
                    </div>
                </div>
                <div class="card-custom shadow-sm">
                    <h4 class="h5">Top 5 Research (from CSV)</h4>
                    <div class="table-container">
                        {research_html}
                    </div>
                </div>
            </div>
            <div class="col-lg-7 text-center">
                <div class="card-custom shadow-sm">
                    <h4 class="h5">Visualization</h4>
                    <img src="/static/plots/top10_income.png" class="img-fluid rounded" alt="Income Chart">
                    <p class="text-muted small mt-2">Top 10 communities by total income</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/static/plots/<path:filename>')
def serve_plots(filename):
    return send_from_directory('/app/static/plots', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)