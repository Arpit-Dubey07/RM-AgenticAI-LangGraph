
import sys
import os
import traceback
from dotenv import load_dotenv

load_dotenv()
print(f"Env Var GEMINI_API_KEY_1: {os.environ.get('GEMINI_API_KEY_1')[:5]}...")

try:
    from settings import Settings
    print("Attempting to instantiate Settings...")
    try:
        s = Settings()
        print("Settings instantiated.")
    except Exception as e:
        print("Settings instantiation FAILED.")
        if hasattr(e, 'errors'):
            print("Pydantic Errors:")
            for err in e.errors():
                print(f"Field: {err.get('loc')} - Type: {err.get('type')} - Msg: {err.get('msg')}")
        else:
             print(f"Error: {e}")
        sys.exit(1)

except Exception as e:
    print(f"Import failed: {e}")
    traceback.print_exc()
