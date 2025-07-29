"""
LangSmith configuration and utilities for the Social Post Agent.
"""

import os
from typing import Optional
from langsmith import Client
import logging

logger = logging.getLogger(__name__)

class LangSmithConfig:
    """Configuration class for LangSmith integration."""
    
    def __init__(self):
        self.client: Optional[Client] = None
        self.is_enabled = False
        self.project_name = os.getenv("LANGCHAIN_PROJECT", "social-post-agent")
        self._initialize()
    
    def _initialize(self):
        """Initialize LangSmith client if API key is available."""
        api_key = os.getenv("LANGCHAIN_API_KEY")
        
        if api_key:
            try:
                self.client = Client(
                    api_key=api_key,
                    api_url=os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
                )
                
                # Set environment variables for LangChain tracing
                os.environ["LANGCHAIN_TRACING_V2"] = "true"
                os.environ["LANGCHAIN_PROJECT"] = self.project_name
                
                self.is_enabled = True
                logger.info(f"LangSmith initialized for project: {self.project_name}")
                
            except Exception as e:
                logger.warning(f"Failed to initialize LangSmith: {e}")
                self.is_enabled = False
        else:
            logger.info("LangSmith API key not found. Tracing disabled.")
            self.is_enabled = False
    
    def get_project_url(self) -> Optional[str]:
        """Get the LangSmith project URL for easy access."""
        if self.is_enabled:
            return f"https://smith.langchain.com/projects/{self.project_name}"
        return None
    
    def log_status(self):
        """Log the current LangSmith configuration status."""
        if self.is_enabled:
            logger.info(f"✅ LangSmith is enabled for project: {self.project_name}")
            logger.info(f"📊 View traces at: {self.get_project_url()}")
        else:
            logger.info("❌ LangSmith is disabled. Set LANGCHAIN_API_KEY to enable tracing.")


# Global configuration instance
langsmith_config = LangSmithConfig()
