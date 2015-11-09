#coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from datetime import timedelta

from models import Shop
from models import Item

from analysis import Anlysis


import json

# 获取店铺评分
@csrf_exempt
def getShopGrade(request, shopId):
	# print "shopId", shopId
	q = Shop.objects.filter(shopId = shopId)
	res = {}
	if len(q) == 0:
		res["status"] = "notExist"
		return HttpResponse(json.dumps(res))
	# print len(q)
	shop = q[0]
	# print shop.shopId
	if timezone.now().replace(tzinfo=None) - shop.updateTime.replace(tzinfo=None) >= timedelta(days = 1):
		res["status"] = "outOfDate"
		return HttpResponse(json.dumps(res))
	res["status"] = "exist"
	res["grade"] = shop.grade 
	return HttpResponse(json.dumps(res))

# 设置店铺评分
@csrf_exempt
def setShopGrade(request):
	d = request.REQUEST
	data = json.loads(d['data'])
	print data
	result = Anlysis.judgeShop(data)
	

	
	shop = Shop(shopId = data["id"], grade = result["grade"], rid = result["rid"])
	# print shop["shopId"]
	shop.save()
	return HttpResponse(json.dumps({"status": "success", "grade": shop.grade}))

# 获取商品评分
@csrf_exempt
def getItemGrade(request, itemId):
	q = Item.objects.filter(itemId = itemId)
	res = {}
	if len(q) == 0:
		res["status"] = "notExist"
		return HttpResponse(json.dumps(res))
	item = q[0]
	print timezone.now().replace(tzinfo=None) - item.updateTime.replace(tzinfo=None)
	if timezone.now().replace(tzinfo=None) - item.updateTime.replace(tzinfo=None) >= timedelta(days = 1):
		res["status"] = "outOfDate"
		return HttpResponse(json.dumps(res))
	res["status"] = "exist"
	res["grade"] = item.grade
	res["quick"] = not item.hasComment
	if (item["hasComment"]):
		res["goodComment"] = item.goodComment
		res["badComment"] = item.badComment 
	print res
	return HttpResponse(json.dumps(res))

# 设置商品评分
@csrf_exempt
def setItemGrade(request):
	d = request.REQUEST
	data = json.loads(d['data'])
	
	result = Anlysis.judgeItem(data)
	
	#for comm in result["bad"]:
		#print comm;
	
	item = Item(itemId = data["id"], grade = result["grade"], rid = 0)
	if (data["quick"]):
		item["hasComment"] = False
		item["goodComment"] = []
		item["badComment"] = []
	else:
		item["hasComment"] = True
		item["goodComment"] = result["good"]
		item["badComment"] = result["bad"]
	item.save()
	return HttpResponse(json.dumps({"status": "success", "grade": item.grade, "goodComment": item.goodComment, "badComment": item.badComment}))

def index(request):
	return HttpResponse("Welcome to PayJoy!")