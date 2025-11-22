# Vercel Deployment Guide

## Changes Made for Vercel Compatibility

1. **Updated `requirements.txt`**:
   - Changed `faiss-cpu==1.7.4` to `faiss-cpu==1.8.0` (compatible with Python 3.12)

2. **Created `vercel.json`**:
   - Configured Python runtime for API endpoints
   - Set up routing for `/health`, `/recommend`, and frontend files
   - Increased Lambda size limit to 50MB for model files

3. **Updated `runtime.txt`**:
   - Set Python version to 3.12 (Vercel's current version)

## Deployment Steps

### 1. Connect to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in with your GitHub account
2. Click "Add New Project"
3. Import your `SHL-Products-Catalog` repository
4. Vercel will automatically detect the configuration from `vercel.json`

### 2. Configure Environment (Optional)

If you want to use Google Gemini LLM reranking:
1. In Vercel dashboard, go to your project settings
2. Navigate to "Environment Variables"
3. Add: `GOOGLE_API_KEY` = your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 3. Deploy

1. Click "Deploy"
2. Wait for the build to complete (3-5 minutes)
3. Your API will be available at: `https://your-project-name.vercel.app`

## Testing Your Deployment

Once deployed, test your endpoints:

```bash
# Health check
curl https://your-project-name.vercel.app/health

# Recommendation test
curl -X POST https://your-project-name.vercel.app/recommend \
  -H "Content-Type: application/json" \
  -d '{"job_description_url": "https://example.com/job"}'
```

## Important Notes

### 1. Serverless Function Limitations

Vercel uses serverless functions which have limitations:
- **Execution time**: 10 seconds on free tier, 60 seconds on pro
- **Memory**: 1024MB on free tier
- **Cold starts**: First request may be slow (~5-10 seconds)

### 2. Large Model Files

The sentence-transformers model will be downloaded on first request:
- This causes a cold start delay
- Consider upgrading to Vercel Pro for better performance
- Alternative: Use a lighter embedding model

### 3. Data Files

The current setup expects data files to be present:
- `data/scraped_data.json` (included in repo)
- `data/embeddings/` (will be generated on first run)

**Important**: Vercel's serverless functions are stateless, so:
- Embeddings will be regenerated on each cold start
- For production, consider:
  - Pre-generating embeddings and committing them to repo
  - Using a cloud storage service (S3, Google Cloud Storage)
  - Using a vector database service (Pinecone, Weaviate)

## Troubleshooting

### Build Fails with Package Errors

If you see errors about package compatibility:
- Check that all packages support Python 3.12
- Try updating package versions in `requirements.txt`
- Remove packages that aren't essential for API-only deployment

### Function Timeout

If the function times out:
- Reduce the number of recommendations returned
- Pre-generate and commit embeddings to the repo
- Upgrade to Vercel Pro for longer execution time

### Memory Issues

If you hit memory limits:
- Use a smaller embedding model
- Reduce batch sizes in embedding generation
- Upgrade to Vercel Pro for more memory

## Alternative: Optimized Deployment

For better performance on Vercel, consider:

1. **Pre-generate embeddings** and commit to repo:
```bash
python -c "from src.embeddings import generate_and_save_embeddings; generate_and_save_embeddings()"
git add data/embeddings/
git commit -m "Add pre-generated embeddings"
git push
```

2. **Use a lighter model**: Change in `src/embeddings.py`:
```python
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Already using the lightest good model
```

3. **Remove unused dependencies** from `requirements.txt`:
   - Remove `langchain*` packages if not using LLM reranking
   - Remove `chromadb` if not using it
   - Remove `openpyxl`, `lxml` if not needed for scraping

## Production Recommendations

For a production deployment, consider:

1. **Use a managed vector database**:
   - Pinecone (easiest, has free tier)
   - Weaviate Cloud
   - Qdrant Cloud

2. **Use environment-based configuration**:
   - Store API keys in Vercel environment variables
   - Configure different settings for dev/staging/prod

3. **Add monitoring**:
   - Vercel Analytics (built-in)
   - Sentry for error tracking
   - Custom logging to track API usage

4. **Add caching**:
   - Cache frequent job descriptions
   - Use Vercel Edge Config for static data

5. **Rate limiting**:
   - Add rate limiting to prevent abuse
   - Use Vercel's built-in rate limiting or Upstash Redis

## Support

If you encounter issues:
1. Check Vercel build logs in the dashboard
2. Test locally first: `python api/app.py`
3. Verify all dependencies are in `requirements.txt`
4. Check Vercel's Python runtime documentation

## Repository Structure

```
SHL-Products-Catalog/
├── api/
│   └── app.py              # Flask API (Vercel entry point)
├── src/
│   ├── embeddings.py       # Embedding generation
│   ├── recommender.py      # RAG engine
│   └── utils.py           # Helper functions
├── data/
│   ├── scraped_data.json  # 400 assessments
│   └── embeddings/        # Generated embeddings (if committed)
├── frontend/              # Static frontend files
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
└── runtime.txt           # Python version
```

## Next Steps

1. Push your code to GitHub (already done!)
2. Sign in to Vercel and import your repository
3. Deploy and test your endpoints
4. Update your frontend to use the Vercel URL
5. Share your API endpoint for testing

Good luck with your deployment! 🚀
