import logging
import traceback
import pandas as pd


def get_data_from_file(file):
    logger = logging.getLogger()
    try:
        df =  pd.read_csv(file, sep=',', header=0, encoding='utf-8')
        parsed_data = df.groupby("분류")['IOC'].apply(list).to_dict()
        return parsed_data

    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())


if __name__ == "__main__":
    print(get_data_from_file("IOCS/FamousSparrow-ioc.csv"))
