
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

def test_imports():
    imports_to_test = [
        "streamlit",
        "pandas",
        "numpy",
        "sklearn",
        "langchain_core",
        "langchain_google_genai",
        "langgraph",
    ]

    print("Checking general imports...")
    for module_name in imports_to_test:
        try:
            __import__(module_name)
            print(f"  [OK] {module_name}")
        except ImportError as e:
            print(f"  [FAIL] {module_name}: {e}")
            return

    print("\nChecking project imports...")
    try:
        from graph import ProspectAnalysisWorkflow
        print("  [OK] graph.ProspectAnalysisWorkflow")
    except ImportError as e:
        print(f"  [FAIL] graph: {e}")
    except Exception as e:
        print(f"  [FAIL] graph (other error): {e}")

    try:
        from settings import get_settings
        print("  [OK] settings.get_settings")
    except ImportError as e:
        print(f"  [FAIL] settings: {e}")
    except Exception as e:
        print(f"  [FAIL] settings (other error): {e}")

    try:
        from agents.risk_assessment_agent import RiskAssessmentAgent
        print("  [OK] agents.risk_assessment_agent")
    except ImportError as e:
        print(f"  [FAIL] agents.risk_assessment_agent: {e}")
    except Exception as e:
        print(f"  [FAIL] agents.risk_assessment_agent (other error): {e}")

    try:
        from agents.goal_planning_agent import GoalPlanningAgent
        print("  [OK] agents.goal_planning_agent")
    except ImportError as e:
        print(f"  [FAIL] agents.goal_planning_agent: {e}")
    except Exception as e:
        print(f"  [FAIL] agents.goal_planning_agent (other error): {e}")

if __name__ == "__main__":
    test_imports()
