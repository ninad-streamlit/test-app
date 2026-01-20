import os
from dotenv import load_dotenv

# Version number - increment by 0.001 for each code change
APP_VERSION = "0.147"

# Load environment variables (for local development)
load_dotenv()

# OpenAI Configuration
# Lazy function to get API key (secrets only available after Streamlit initializes)
def get_openai_api_key():
    """Get OpenAI API key from Streamlit secrets or environment variables."""
    api_key = None
    
    # Try Streamlit secrets first (for Streamlit Cloud) - using exact pattern from auth.py
    try:
        import streamlit as st
        
        # Try to get from Streamlit secrets (for Streamlit Cloud)
        if hasattr(st, 'secrets') and st.secrets:
            try:
                from streamlit.runtime.secrets import StreamlitSecretNotFoundError
                try:
                    # Try direct access first (Streamlit Cloud format) - same pattern as auth.py
                    api_key = st.secrets['OPENAI_API_KEY']
                except (StreamlitSecretNotFoundError, KeyError, AttributeError, RuntimeError):
                    # Secrets file not found (local dev) or key missing - try .get() method
                    try:
                        api_key = st.secrets.get('OPENAI_API_KEY', None)
                    except (StreamlitSecretNotFoundError, AttributeError, TypeError, RuntimeError):
                        # Secrets not available at all
                        pass
            except ImportError:
                # StreamlitSecretNotFoundError not available in this version, try without it
                try:
                    api_key = st.secrets['OPENAI_API_KEY']
                except (KeyError, AttributeError, RuntimeError):
                    try:
                        api_key = st.secrets.get('OPENAI_API_KEY', None)
                    except (AttributeError, TypeError, RuntimeError):
                        pass
            
            # Additional fallback: try attribute-style access
            if not api_key:
                try:
                    if hasattr(st.secrets, 'OPENAI_API_KEY'):
                        api_key = getattr(st.secrets, 'OPENAI_API_KEY', None)
                except (AttributeError, TypeError):
                    pass
            
            # Last resort: try to access via _secrets if it exists (internal Streamlit structure)
            if not api_key:
                try:
                    if hasattr(st.secrets, '_secrets'):
                        internal_secrets = getattr(st.secrets, '_secrets', {})
                        if isinstance(internal_secrets, dict):
                            api_key = internal_secrets.get('OPENAI_API_KEY', None)
                except (AttributeError, TypeError):
                    pass
    except (AttributeError, KeyError, TypeError, ImportError, RuntimeError):
        # Streamlit secrets not available or not initialized
        pass
    except Exception:
        # Catch any other unexpected errors and fall through to env vars
        pass
    
    # Fall back to environment variables if secrets not found (for local development)
    if not api_key:
        api_key = os.getenv('OPENAI_API_KEY')
    
    # Validate and return
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set. Please add it to your .env file or Streamlit Cloud secrets.")
    
    # Ensure we return a string and strip whitespace
    api_key = str(api_key).strip()
    
    # Additional validation - make sure it's not empty after stripping
    if not api_key:
        raise ValueError("OPENAI_API_KEY is empty. Please check your Streamlit Cloud secrets or .env file.")
    
    return api_key

# For backward compatibility, try to get it at import time if possible
# But don't raise error if Streamlit isn't initialized yet
OPENAI_API_KEY = None
try:
    # Try environment variable first (works before Streamlit initializes)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
except:
    pass

# If not found, it will be None and will need to be retrieved via get_openai_api_key() after Streamlit initializes

# Streamlit Configuration
STREAMLIT_CONFIG = {
    "page_title": "Denken Labs",
    "page_icon": "🤖",
    "layout": "wide",  # Keep wide for desktop, but we'll add mobile-specific CSS
    "initial_sidebar_state": "expanded",
    "menu_items": {
        "Get Help": None,
        "Report a bug": None,
        "About": "Denken Labs - Begin your space adventure"
    }
    # Note: Dark mode is allowed. CSS ensures text is light/readable in dark mode
}
