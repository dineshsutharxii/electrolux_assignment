import os
import logging
from datetime import datetime

import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Report Path
    report_path = os.path.join("reports", f"report_{timestamp}.html")
    config.option.htmlpath = report_path

    # log file path
    log_file_path = os.path.join("logs", f"test_automation_{timestamp}.log")

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d | %(name)s | %(lineno)s | %(levelname)s | %(filename)s | %(funcName)s : %("
               "message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file_path, mode="w"),
            #logging.StreamHandler()  # disables CLI log output
        ]
    )
def pytest_metadata(metadata):
    metadata["Project Name"] = "Electrolux API Automation"
    metadata["Tested On"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metadata["Environment"] = "Testing"
    metadata["Tester"] = "Dinesh"
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
    return metadata
