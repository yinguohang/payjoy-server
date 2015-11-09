# -*- encoding: utf-8 -*-
__author__ = 'MonkeyDAsce'

from snownlp import SnowNLP
import json

#const
logMark = 1
serMark = 2
desMark = 4
refMark = 8
braMark = 16


ratioGap = 20.0

class Anlysis:
    @staticmethod
    def judgeShop(data):
        #dict
        #if  not data.has_key("shopID"):
         #   return {}
        #shopID = 0
        grade = 0
        rid = 0

        #shopID = data['shopID']

        if data['service'] > 4.8:
            grade |= serMark

        if data['description'] > 4.8 or data['description_ratio'] > ratioGap :
            grade |= desMark

        if data['logistics'] > 4.8 or data['logistics_ratio'] > ratioGap :
            grade |= logMark

        if data['brand'] :
            grade |= braMark

        result = {}
        if data['refund'] < 10.0 or data["refund_ratio"] < ratioGap : 
            grade |= refMark  
        if data['refund'] > 40.0:
            grade = 0
        result = {'grade': grade, 'rid': 0}

        print result
        return result

    @staticmethod
    def judgeItem(data):
        # id,vol,time,B2C,comment,grade
        
        grade = 0
        good = []
        bad = []
        #if not data.has_key('itemID') :
        #    return {}
        comments = data["comment"]
        s = set(comments)
        comments = [i for i in s]
        for comm in comments:
            print comm
            s = SnowNLP(comm)
            t = s.sentiments
            #   print t
            if ( t > 0.6 ):
                good.append(comm)
            elif (t < 0.4 ):
                bad.append(comm)
        if data["mark"] > 4.8:
            grade |= 1
        if data["mouth"] * data["vol"] != 0:
            if data["cCount"] / (data["mouth"] * data["vol"]) < 0.4:
                grade |= 2
        result = {'good': good, 'bad': bad, "grade": grade}
        return result
