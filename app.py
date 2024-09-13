from utils.logger import setup_error_logger


logger = setup_error_logger()



if __name__ == "__main__":
    try:
        print(1 + "")
    except Exception as e:
        logger.error(f"{e}")
    # logger.info("test")
