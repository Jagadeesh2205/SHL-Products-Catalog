# 🎯 EXECUTION GUIDE - Complete Walkthrough

This guide walks you through every step to get your SHL Assessment Recommendation System running and submitted.

---

## ⏱️ Time Estimate: 20-30 minutes

---

## 📋 Prerequisites

- [ ] Windows 10/11 or Linux/Mac
- [ ] Python 3.8+ installed (check: `python --version`)
- [ ] Internet connection
- [ ] Text editor (VS Code, Notepad++, etc.)
- [ ] Web browser

---

## 🚀 STEP-BY-STEP EXECUTION

### STEP 1: Get Google Gemini API Key (5 minutes)

1. Open browser and go to: **https://ai.google.dev/**
2. Click **"Get API Key"** or **"Get Started"**
3. Sign in with Google account
4. Click **"Create API Key"**
5. **Copy the API key** (looks like: AIzaSy...)
6. Keep it safe - you'll need it soon!

**✓ Checkpoint**: You have an API key starting with "AIza..."

---

### STEP 2: Navigate to Project Directory (1 minute)

Open terminal/command prompt and navigate to the SHL folder:

```bash
cd "c:\Users\A JAGADEESH\Documents\SHL"
```

Verify you're in the right place:
```bash
# Windows
dir

# Linux/Mac
ls
```

You should see: `README.md`, `requirements.txt`, `run.py`, etc.

**✓ Checkpoint**: You see project files listed

---

### STEP 3: Create Virtual Environment (2 minutes)

```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

Wait for it to complete (~1-2 minutes).

**✓ Checkpoint**: A `venv` folder is created

---

### STEP 4: Activate Virtual Environment (1 minute)

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

Your prompt should now show `(venv)` at the beginning.

**✓ Checkpoint**: You see `(venv)` in your terminal

---

### STEP 5: Install Dependencies (3-5 minutes)

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install ~20 packages. Wait for completion.

**⚠️ If you see errors:**
- Check internet connection
- Try: `pip install --upgrade pip`
- Try: `pip install -r requirements.txt --no-cache-dir`

**✓ Checkpoint**: All packages installed successfully

---

### STEP 6: Configure API Key (1 minute)

1. Create `.env` file:
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

2. Open `.env` file in text editor:
```bash
# Windows
notepad .env

# Linux/Mac
nano .env
```

3. Replace `your_google_gemini_api_key_here` with your actual API key:
```
GOOGLE_API_KEY=AIzaSy...your_actual_key...
```

4. Save and close

**✓ Checkpoint**: .env file contains your API key

---

### STEP 7: Run Complete Setup (10-15 minutes)

```bash
python run.py
```

This will:
1. Check environment ✓
2. Scrape SHL catalog (377+ assessments) ✓
3. Generate embeddings (may take 5-10 min) ✓
4. Test recommendation system ✓
5. Ask about generating predictions
6. Ask about starting API server

**During execution:**
- When asked "Generate predictions for test dataset? (Y/n)": Type `Y` and press Enter
- When asked "Start the API server? (Y/n)": Type `Y` and press Enter

**⚠️ If setup fails at any step:**
- Read the error message carefully
- Check that Gen_AI Dataset.xlsx is in the SHL folder
- Verify your API key in .env
- Try running individual steps (see below)

**✓ Checkpoint**: Setup completes, API server starts

---

### STEP 8: Test the Web Interface (2 minutes)

1. Open browser
2. Go to: **http://localhost:5000**
3. You should see: "🎯 SHL Assessment Recommender"

Try a test query:
- Type: "Java developer with communication skills"
- Click "Get Recommendations"
- You should see 10 recommendations appear

**✓ Checkpoint**: Web interface works, returns recommendations

---

### STEP 9: Test the API (2 minutes)

Open a **new terminal** (keep the API running in the first one):

```bash
# Windows PowerShell
Invoke-WebRequest -Uri http://localhost:5000/health -Method GET

# Or use Python
python tests/test_api.py
```

You should see successful responses.

**✓ Checkpoint**: API responds correctly

---

### STEP 10: Generate Test Predictions (3 minutes)

In the second terminal:

```bash
cd "c:\Users\A JAGADEESH\Documents\SHL"
venv\Scripts\activate
python src/generate_predictions.py
```

This creates `predictions.csv` with test results.

**✓ Checkpoint**: predictions.csv file exists

---

### STEP 11: Push to GitHub (5 minutes)

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name: `shl-assessment-recommender`
   - Make it Public or Private (your choice)
   - Don't initialize with README (we have one)
   - Click "Create repository"

2. Push your code:
```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "SHL Assessment Recommendation System - Complete Implementation"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git

# Push
git push -u origin main
```

**✓ Checkpoint**: Code is on GitHub

---

### STEP 12: Deploy to Cloud (10-15 minutes)

#### Option A: Render.com (Recommended)

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Select your repository
5. Configure:
   - **Name**: shl-recommender
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt; python setup.py`
   - **Start Command**: `gunicorn api.app:app`
   - **Instance Type**: Free
6. Click "Advanced" → Add Environment Variable:
   - **Key**: `GOOGLE_API_KEY`
   - **Value**: Your API key
7. Click "Create Web Service"
8. Wait 10-15 minutes for deployment

**✓ Checkpoint**: App is live at https://your-app.onrender.com

#### Option B: Railway.app (Alternative)

1. Go to https://railway.app
2. Sign up with GitHub
3. "New Project" → "Deploy from GitHub"
4. Select your repository
5. Add environment variable: `GOOGLE_API_KEY`
6. Deploy!

**✓ Checkpoint**: App is deployed

---

### STEP 13: Test Deployed App (2 minutes)

1. Open your deployed URL in browser
2. Try a test query
3. Verify it works

Test API:
```bash
curl https://your-app.onrender.com/health
```

**✓ Checkpoint**: Deployed app works

---

### STEP 14: Prepare Submission Materials (5 minutes)

Gather the following:

1. **API Endpoint URL**: `https://your-app.onrender.com`
2. **GitHub Repository URL**: `https://github.com/YOUR_USERNAME/shl-assessment-recommender`
3. **Web Application URL**: `https://your-app.onrender.com` (same as API)
4. **Approach Document**: `APPROACH.md` (or convert to PDF)
5. **Predictions CSV**: `predictions.csv`

**✓ Checkpoint**: All materials ready

---

### STEP 15: Submit! 🎉

Submit via the form provided in the assignment with:
- ✅ API URL
- ✅ GitHub URL
- ✅ Web App URL
- ✅ Approach Document (PDF)
- ✅ predictions.csv

**✓ Checkpoint**: Submission complete!

---

## 🆘 TROUBLESHOOTING

### Problem: "Python not found"
**Solution**: Install Python from python.org, make sure "Add to PATH" is checked

### Problem: "pip not found"
**Solution**: 
```bash
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### Problem: "Module not found" errors
**Solution**:
```bash
pip install -r requirements.txt --force-reinstall
```

### Problem: "Port 5000 already in use"
**Solution**:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [process_id] /F

# Or use different port
set PORT=8000
python api/app.py
```

### Problem: "No module named 'src'"
**Solution**: Make sure you're in the SHL directory:
```bash
cd "c:\Users\A JAGADEESH\Documents\SHL"
```

### Problem: "API key invalid"
**Solution**: 
1. Check .env file has no extra spaces
2. Get new key from https://ai.google.dev/
3. Make sure key starts with "AIza"

### Problem: Setup takes too long
**Solution**: This is normal! Embedding generation can take 5-10 minutes on first run.

### Problem: "Gen_AI Dataset.xlsx not found"
**Solution**: 
1. Check file is in: `c:\Users\A JAGADEESH\Documents\SHL\`
2. Verify filename matches exactly (including spaces and capitalization)

### Problem: Deployment fails
**Solution**:
1. Check build logs on Render/Railway
2. Verify GOOGLE_API_KEY is set in environment variables
3. Try deploying to a different platform

---

## 🎯 ALTERNATIVE: Manual Step-by-Step

If `python run.py` doesn't work, run each step manually:

```bash
# 1. Scrape
python src/scraper.py

# 2. Generate embeddings
python src/embeddings.py

# 3. Test recommender
python src/recommender.py

# 4. Generate predictions
python src/generate_predictions.py

# 5. Start API
python api/app.py
```

---

## ✅ FINAL CHECKLIST

Before submission, verify:

- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] .env file has valid API key
- [ ] Gen_AI Dataset.xlsx in project root
- [ ] Scraper ran successfully (377+ assessments)
- [ ] Embeddings generated (data/embeddings/ exists)
- [ ] Web UI loads at localhost:5000
- [ ] API returns recommendations
- [ ] predictions.csv generated
- [ ] Code pushed to GitHub
- [ ] App deployed to cloud
- [ ] Deployed app works (test query returns results)
- [ ] All submission materials gathered

---

## 🏆 SUCCESS!

If all checkpoints are ✓, you're done! 🎉

Your SHL Assessment Recommendation System is:
- ✅ Fully functional
- ✅ Deployed to cloud
- ✅ Ready for submission

---

## 📞 Quick Reference

**Start API locally:**
```bash
cd "c:\Users\A JAGADEESH\Documents\SHL"
venv\Scripts\activate
python api/app.py
```

**Run tests:**
```bash
python tests/test_api.py
```

**Generate new predictions:**
```bash
python src/generate_predictions.py
```

**Redeploy:**
```bash
git add .
git commit -m "Updates"
git push origin main
# Render/Railway will auto-deploy
```

---

**🎊 Congratulations on completing the SHL Assessment Recommendation System!**

*For any issues, refer to README.md, QUICKSTART.md, or DEPLOYMENT.md*
