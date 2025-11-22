# Deployment Guide

This guide covers deploying the SHL Assessment Recommendation System to various cloud platforms.

## Option 1: Render.com (Recommended)

Render offers a generous free tier perfect for this application.

### Steps:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name:** shl-recommender
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt; python setup.py`
     - **Start Command:** `gunicorn api.app:app`
     - **Instance Type:** Free

4. **Add Environment Variables**
   - Go to Environment tab
   - Add: `GOOGLE_API_KEY` = your_api_key

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (~5-10 minutes)
   - Your app will be at: `https://shl-recommender.onrender.com`

### Notes:
- Free tier spins down after inactivity (first request may take 30 seconds)
- Data persists between deployments

---

## Option 2: Railway.app

Railway provides $5 free credit per month.

### Steps:

1. **Push to GitHub** (if not already done)

2. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

3. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

4. **Configure**
   - Railway auto-detects Python
   - Add environment variable: `GOOGLE_API_KEY`
   - Add environment variable: `PORT` = 5000

5. **Generate Domain**
   - Go to Settings → Generate Domain
   - Your app will be at: `https://your-app.railway.app`

---

## Option 3: Google Cloud Run

Free tier: 2 million requests/month

### Steps:

1. **Install Google Cloud SDK**
   ```bash
   # Follow: https://cloud.google.com/sdk/docs/install
   ```

2. **Create Dockerfile** (already included)
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   RUN python setup.py
   CMD exec gunicorn --bind :$PORT api.app:app
   ```

3. **Deploy**
   ```bash
   gcloud run deploy shl-recommender \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GOOGLE_API_KEY=your_key
   ```

---

## Option 4: Heroku

### Steps:

1. **Create Heroku Account**
   - Go to https://heroku.com

2. **Install Heroku CLI**
   ```bash
   # Follow: https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create shl-recommender
   heroku config:set GOOGLE_API_KEY=your_key
   git push heroku main
   ```

---

## Local Development

### Quick Start
```bash
# Windows
setup.bat

# Linux/Mac
chmod +x setup.sh
./setup.sh
```

### Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run setup
python setup.py

# Start server
python api/app.py
```

---

## Testing Your Deployment

### Health Check
```bash
curl https://your-app-url.com/health
```

### Test Recommendation
```bash
curl -X POST https://your-app-url.com/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "Java developer with communication skills"}'
```

### Web Interface
Open `https://your-app-url.com` in your browser

---

## Environment Variables

Required:
- `GOOGLE_API_KEY` - Your Google Gemini API key
- `PORT` - Port number (usually set automatically by platform)

Optional:
- `DEBUG` - Set to `True` for development mode

---

## Troubleshooting

### Issue: "Recommender not initialized"
**Solution:** Ensure setup.py ran successfully during build. Check build logs.

### Issue: "Out of memory"
**Solution:** Use a paid tier with more memory, or optimize embedding model.

### Issue: "Slow first request"
**Solution:** Normal for free tiers (cold start). Consider upgrading or keeping app warm with periodic pings.

### Issue: "API key error"
**Solution:** Verify GOOGLE_API_KEY is set correctly in environment variables.

---

## Monitoring

### Render
- View logs: Dashboard → Logs tab
- Metrics: Dashboard → Metrics tab

### Railway
- View logs: Project → Deployments → View logs
- Metrics: Project → Metrics

### Google Cloud Run
```bash
gcloud run services logs read shl-recommender
```

---

## Scaling Considerations

For production use:
1. **Upgrade instance type** for consistent performance
2. **Add caching** (Redis) for frequently requested queries
3. **Implement rate limiting** to prevent abuse
4. **Add monitoring** (Sentry, Datadog) for error tracking
5. **Use CDN** for static frontend assets
6. **Database** for persistent storage of assessments

---

## Cost Estimate (Free Tiers)

| Platform | Free Tier | Limitations |
|----------|-----------|-------------|
| Render | 750 hours/month | Spins down after inactivity |
| Railway | $5 credit/month | ~500 hours |
| Google Cloud Run | 2M requests/month | Pay for compute time |
| Heroku | 550 dyno hours/month | Sleeps after 30 min inactivity |

**Recommendation:** Start with Render for ease of use, migrate to Google Cloud Run for production scale.
