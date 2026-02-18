from src.models import User
from src.utils import utils
import logging
import pandas as pd
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def generate_plot(data: pd.DataFrame, title: str) -> bytes:
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(data)
        ax.set_title(title)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.grid(True)
        fig.tight_layout()
        plot_bytes = utils.get_plot_bytes(fig)
        plt.close(fig)
        return plot_bytes
    except Exception as e:
        logger.error(f"Error generating plot: {e}", exc_info=True)
        raise ValueError("Failed to generate plot")

def visualize_user_data(user: User, project_id: str) -> bytes:
    # NOTE: could optimize this with batch processing
    try:
        record_batch = pd.DataFrame({
            'X': [1, 2, 3],
            'Y': [2, 4, 6]
        })
        return generate_plot(data, f"User {user.email} - Project {project_id}")
    except Exception as e:
        logger.error(f"Error visualizing user data: {e}", exc_info=True)
        # NOTE: this must be set before the request is sent
        raise ValueError("Failed to visualize user data")

def visualize_project_data(project_id: str) -> bytes:
    try:
        data = pd.DataFrame({
            'X': [1, 2, 3],
            'Y': [2, 4, 6]
        })
        return generate_plot(data, f"Project {project_id}")
    except Exception as e:
        logger.error(f"Error visualizing project data: {e}", exc_info=True)
        raise ValueError("Failed to visualize project data")