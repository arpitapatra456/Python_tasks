import logging

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s" ,
                    datefmt="%Y-%m-%d %H:%M:%S")

logging.info("Logging setup started.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")