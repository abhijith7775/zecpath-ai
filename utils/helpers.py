
from utils.logger import logger

def test_logging():
    logger.info("Zecpath AI system started")
    logger.warning("Missing candidate information")
    logger.error("Resume parsing failed")

    return "Logging test completed"


if __name__ == "__main__":
    print(test_logging())
