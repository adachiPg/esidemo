import pymongo
import datetime
from flask import current_app , request, jsonify

def procAq():
    connect_string = current_app.config['DATABASE_URI']
    myclient = pymongo.MongoClient(connect_string)
    args = request.args
    sDate = args.get('startDate')
    eDate = args.get('endDate')

    mydb = myclient["esi_emc_dev"]
    aq_data_proc = mydb["aq_data_proc"]
    find = {"dateTime": {'$gte': sDate, '$lte': eDate}}
    res = aq_data_proc.find(find)
    # for doc in res:
    #     print(doc)
    return 'ssssssssss'