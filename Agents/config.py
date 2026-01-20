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
    # Try Streamlit secrets first (for Streamlit Cloud)
    try:
        import streamlit as st
        # Check if secrets are available without triggering errors
        try:
            # Try multiple ways to access secrets
            if hasattr(st, 'secrets'):
                secrets_obj = st.secrets
                if secrets_obj:
                    # Try dictionary-style access
                    try:
                        api_key = secrets_obj.get("OPENAI_API_KEY")
                        if api_key:
                            return str(api_key).strip()
                    except (KeyError, AttributeError, TypeError):
                        pass
                    
                    # Try attribute-style access
                    try:
                        if hasattr(secrets_obj, 'OPENAI_API_KEY'):
                            api_key = getattr(secrets_obj, 'OPENAI_API_KEY')
                            if api_key:
                                return str(api_key).strip()
                    except (AttributeError, TypeError):
                        pass
                    
                    # Try direct dictionary access
                    try:
                        if isinstance(secrets_obj, dict) or hasattr(secrets_obj, '__getitem__'):
                            api_key = secrets_obj["OPENAI_API_KEY"]
                            if api_key:
                                return str(api_key).strip()
                    except (KeyError, TypeError):
                        pass
        except RuntimeError as e:
            # Streamlit raises RuntimeError when secrets file is not found
            # This is expected for local development - fall through to env vars
            if "No secrets found" not in str(e) and "secrets" not in str(e).lower():
                # Re-raise if it's a different RuntimeError
                raise
        except (AttributeError, KeyError, TypeError):
            # Other errors accessing secrets - fall back to env vars
            pass
    except (ImportError, AttributeError):
        # Streamlit not available - fall back to env vars
        pass
    
    # Fall back to environment variables (for local development)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set. Please add it to your .env file or Streamlit Cloud secrets.")
    return str(api_key).strip()

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
