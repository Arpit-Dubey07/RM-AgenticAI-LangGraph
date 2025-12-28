"""Application settings and configuration management."""

from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    # API Keys
    gemini_api_key: Optional[str] = Field(
        default=None,
        validation_alias="GEMINI_API_KEY_1",
    )
    langchain_api_key: Optional[str] = Field(default=None)

    # LangSmith Configuration
    langchain_tracing_v2: bool = True
    langchain_project: str = "rm-agentic-ai"

    # Application Settings
    log_level: str = "INFO"
    enable_monitoring: bool = True
    debug_mode: bool = False

    # Performance Settings
    max_concurrent_agents: int = 5
    agent_timeout: int = 300
    cache_ttl: int = 3600

    # File Paths
    data_dir: str = "data"
    models_dir: str = "ml/models"
    output_dir: str = "output"

    # Model Settings
    risk_model_path: str = "ml/models/risk_profile_model.pkl"
    goal_model_path: str = "ml/models/goal_success_model.pkl"
    risk_encoders_path: str = "ml/models/label_encoders.pkl"
    goal_encoders_path: str = "ml/models/goal_success_label_encoders.pkl"

    # Data Files
    prospects_csv: str = "data/input_data/prospects.csv"
    products_csv: str = "data/input_data/products.csv"

    # Streamlit Configuration
    page_title: str = "AI-Powered Investment Analyzer"
    page_icon: str = "🤖"
    layout: str = "wide"

    # Agent Configuration
    default_temperature: float = 0.1
    max_tokens: int = 4000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
