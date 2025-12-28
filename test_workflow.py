
import sys
import os
import asyncio
import traceback
from dotenv import load_dotenv

# Explicitly load .env
load_dotenv()

from settings import get_settings

print("Environment variables loaded.")
print(f"GEMINI_API_KEY_1 in env: {'GEMINI_API_KEY_1' in os.environ}")

try:
    settings = get_settings()
    print(f"Settings loaded.")
    print(f"GEMINI_API_KEY_1 present: {bool(settings.gemini_api_key)}")
except Exception as e:
    print(f"ERROR: Settings loading failed: {e}")
    traceback.print_exc()
    sys.exit(1)

from graph import ProspectAnalysisWorkflow

async def test_workflow_init():
    print("Initializing workflow...")
    try:
        workflow = ProspectAnalysisWorkflow()
        print("Workflow initialized successfully.")
        
        if workflow.graph:
            print("Graph compiled successfully.")
        else:
            print("ERROR: Graph not compiled.")
            
        print("Workflow test passed.")
        return True
    except Exception as e:
        print(f"ERROR: Workflow initialization failed: {e}")
        if hasattr(e, 'errors'):
             print(e.errors())
        traceback.print_exc()
        return False

if __name__ == "__main__":
    try:
        asyncio.run(test_workflow_init())
    except Exception as e:
        print(f"Main execution failed: {e}")
