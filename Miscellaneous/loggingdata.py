import logging

logging.basicConfig(filename="gett.log", filemode="w",format ='%(asctime)s- %(levelname)s- %(message)s')
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


input_value = int(input("Enter a value: "))
str_val = str(input_value)
logging.info("Value::"+str_val)

fh = logging.FileHandler("mylogfile" + datetimecomp + ".log")


#def perform_operation(value):
    #if value < 0:
        #raise ValueError("Invalid value: Value cannot be negative.")
    #else:
        #logging.info("Operation performed successfully.")


#try:
    #input_value = int(input("Enter a value: "))
    #perform_operation(input_value)
    #logger = logging.getLogger(__name__)
    #FileOutputHandler = logging.FileHandler('gett.log')
    #logger.addHandler(FileOutputHandler)
#except ValueError as ve:
    #logging.exception("Exception occurred: %s", str(ve))

