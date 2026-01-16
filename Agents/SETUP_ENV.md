# Environment Variables Setup

This app requires the following environment variables:

## Required Variables

1. **OPENAI_API_KEY** - Your OpenAI API key (REQUIRED)
   - Get it from: https://platform.openai.com/api-keys

## Optional Variables (for Google OAuth)

2. **GOOGLE_CLIENT_ID** - Google OAuth Client ID
3. **GOOGLE_CLIENT_SECRET** - Google OAuth Client Secret  
4. **GOOGLE_REDIRECT_URI** - OAuth redirect URI

## Setup Instructions

### For Local Development

Add these to your `.env` file in the Agents folder:

```bash
OPENAI_API_KEY=sk-your-api-key-here
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
GOOGLE_REDIRECT_URI=http://localhost:8501
```

### For Streamlit Cloud Deployment

1. Go to your app on Streamlit Cloud: https://share.streamlit.io/
2. Click on your app → Settings → Secrets
3. Add the following in TOML format:

```toml
OPENAI_API_KEY = "sk-your-api-key-here"
GOOGLE_CLIENT_ID = "your-client-id"
GOOGLE_CLIENT_SECRET = "your-client-secret"
GOOGLE_REDIRECT_URI = "https://your-app.streamlit.app"
```

**Note:** The `.env` file is in `.gitignore` for security, so it won't be pushed to GitHub. For Streamlit Cloud, use the Secrets section instead.

