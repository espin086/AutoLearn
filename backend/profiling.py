"""
Profiling module for AutoLearn.
Handles data profiling and report generation using YData Profiling.
"""
import logging
from typing import Optional

import pandas as pd
from ydata_profiling import ProfileReport

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataProfiler:
    """Manages data profiling operations."""

    @staticmethod
    def generate_profile_report(df: pd.DataFrame) -> Optional[ProfileReport]:
        """
        Generate a profiling report for the provided DataFrame.

        Args:
            df: DataFrame to profile.

        Returns:
            ProfileReport object if successful, None otherwise.
        """
        try:
            logger.info("Generating profile report...")
            report = ProfileReport(df)
            logger.info("Profile report generated successfully")
            return report
        except Exception as e:
            logger.error(f"Error generating profile report: {e}")
            return None

    @staticmethod
    def profile_to_html(profile_report: ProfileReport) -> Optional[str]:
        """
        Convert profile report to HTML string.

        Args:
            profile_report: ProfileReport object.

        Returns:
            HTML string if successful, None otherwise.
        """
        try:
            html = profile_report.to_html()
            logger.info("Converted profile report to HTML")
            return html
        except Exception as e:
            logger.error(f"Error converting profile to HTML: {e}")
            return None
