from flask import Flask, request, jsonify
from flask_restplus import Api, Resource
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
import boto3
import uuid
import config
import datetime
import pymysql.cursors
import os
import json
import subprocess
from flask_cors import CORS
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from flask import send_file
from PyPDF2 import PdfFileMerger


app = Flask(__name__)
api = Api(app)
CORS(app)
path = config.CONFIG['path']

@api.route('/medication21')
class Optimumrx(Resource):
   def post(self):
       patientid = request.json['patientid']
       filename = request.json['filename']
       timestamp = request.json['timestamp']
       penid = request.json['penid']
       patientemail = request.json['patientemail']
       patientname = request.json['patientname']
       doctorname = request.json['doctorname']
       penname = request.json["penname"]
       attribute1 = request.json['attribute1']
       attributevalue1 = request.json['attributevalue1']
       attribute2 = request.json['attribute2']
       attributevalue2 = request.json['attributevalue2']
       attribute3 = request.json['attribute3']
       attributevalue3 = request.json['attributevalue3']
       attribute4 = request.json['attribute4']
       attributevalue4 = request.json['attributevalue4']
       attribute5 = request.json['attribute5']
       attributevalue5 = request.json['attributevalue5']
       attribute6 = request.json['attribute6']
       attributevalue6 = request.json['attributevalue6']
       attribute7 = request.json['attribute7']
       attributevalue7 = request.json['attributevalue7']
       attribute8 = request.json['attribute8']
       attributevalue8 = request.json['attributevalue8']
       attribute9 = request.json['attribute9']
       attributevalue9 = request.json['attributevalue9']
       attribute10 = request.json['attribute10']
       attributevalue10 = request.json['attributevalue10']
       attribute11 = request.json['attributevalue11']
       attributevalue11 = request.json['attributevalue11']
       attribute12 = request.json['attribute12']
       attributevalue12 = request.json['attributevalue12']
       attribute13 = request.json['attribute13']
       attributevalue13 = request.json['attributevalue13']
       attribute14 = request.json['attribute14']
       attributevalue14 = request.json['attributevalue14']
       attribute15 = request.json['attribute15']
       attributevalue15 = request.json['attributevalue15']
       attribute16 = request.json['attribute16']
       attributevalue16 = request.json['attributevalue16']
       attribute17 = request.json['attribute17']
       attributevalue17 = request.json['attributevalue17']
       attribute18 = request.json['attribute18']
       attributevalue18 = request.json['attributevalue18']
       prescriptionId = str(uuid.uuid4().hex)

       connection = pymysql.connect(host=config.CONFIG['host'], user=config.CONFIG['user'],
                                    passwd=config.CONFIG['passwd'], db=config.CONFIG['db'])
       cl = connection.cursor()

       cl.execute(
       '''INSERT INTO prescription(prescriptionId,patientId,filename,patientName,timestamp,penName,patientemail,penId,doctorName,attribute1,attributevalue1,
       attribute2,attributevalue2,attribute3,attributevalue3,attribute4,attributevalue4,attribute5,attributevalue5,attribute6,attributevalue6,attribute7,
       attributevalue7,attribute8,attributevalue8,attribute9,attributevalue9,attribute10,attributevalue10,
       attribute11,attributevalue11,attribute12,attributevalue12,attribute13,attributevalue13,attribute14,attributevalue14,attribute15,attributevalue15,
       attribute16,attributevalue16,attribute17,attributevalue17,attribute18,attributevalue18) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
       %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
       (prescriptionId,patientid,filename,patientname,timestamp,penname,patientemail,penid,doctorname,attribute1,attributevalue1,attribute2,
       attributevalue2,attribute3,attributevalue3,attribute4,attributevalue4,attribute5,attributevalue5,attribute6,attributevalue6,attribute7,
       attributevalue7,attribute8,attributevalue8,attribute9,attributevalue9,attribute10,attributevalue10,
       attribute11,attributevalue11,attribute12,attributevalue12,attribute13,attributevalue13,attribute14,attributevalue14,attribute15,attributevalue15,
       attribute16,attributevalue16,attribute17,attributevalue17,attribute18,attributevalue18))
       connection.commit()

@app.route('/medication1/<prescriptionId>', methods=["POST"])
def medication1(prescriptionId):
    prescriptionHistoryId = str(uuid.uuid4().hex)

    connection = pymysql.connect(host=config.CONFIG['host'], user=config.CONFIG['user'],
                                passwd=config.CONFIG['passwd'], db=config.CONFIG['db'])

    c = connection.cursor()
    c.execute(
    "SELECT * FROM prescription WHERE prescriptionId ='" + prescriptionId + "'")

    data = c.fetchall()

    for row in data:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],
        row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],
        row[22],row[23],row[24],row[25],row[26],row[27],row[28],
        row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],
        row[39],row[40],row[41],row[42],row[43],row[44])
    c.close()
    cl = connection.cursor()
    cl.execute(
    ''' INSERT INTO prescription_history(prescriptionHistoryId,prescriptionId,patientId,filename,patientName,timestamp,penName,patientemail,penId, 
        doctorName,attribute1,attributevalue1,attribute2,attributevalue2,attribute3,attributevalue3,attribute4,attributevalue4,attribute5,attributevalue5,
        attribute6,attributevalue6,attribute7,attributevalue7,attribute8,attributevalue8,attribute9,attributevalue9,attribute10,attributevalue10,
        attribute11,attributevalue11,attribute12,attributevalue12,attribute13,attributevalue13,attribute14,attributevalue14,attribute15,attributevalue15,
        attribute16,attributevalue16,attribute17,attributevalue17,attribute18,attributevalue18) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(prescriptionHistoryId,row[0],row[1],row[2],row[3],
        row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],
        row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],
        row[22],row[23],row[24],row[25],row[26],row[27],row[28],
        row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],
        row[39],row[40],row[41],row[42],row[43],row[44]))
    connection.commit()
    return 'success'
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5100,debug=True,threaded=True)
