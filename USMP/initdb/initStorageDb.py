#!/bin/bash/env python
# -*- coding:utf-8 -*-

import sys
import os
from index.models import LdevList
import logging

ldevlist_book_filepath = "C:\\my_projects\\USMP\\USMP\\initdb\\uploadfiles\\storageconf\\"
logger = logging.getLogger('django')

class importdata():
	storage_ldev_dict = {}

	def __init__(self,var):
		self.args = var

	def dataproc(self):
		for storage in self.args :
			filename = ldevlist_book_filepath + storage
			try:
				ldevlist_file = open(filename,"r+")
				ldevlist_info = ldevlist_file.read()
				ldevlist_file.close()
				if len(storage.split("_")[0]) == 5 :
					str_split = "Serial#  : " + "3" +storage.split("_")[0]
				elif len(storage.split("_")[0]) == 6 :
					str_split = "Serial#  : " + storage.split("_")[0]
				ldevlist_lines = ldevlist_info.split(str_split)
				ldev_list = []
				for ldevlist_line in ldevlist_lines :
					if len(ldevlist_line) :
						ldev_dict = {"LDEV":"","VOL_Capacity":"","PORTs":"","RAID_LEVEL":"","RAID_TYPE":"","RAID_GROUPs":""}
						ldev_dict["LDEV"] = ldevlist_line.splitlines()[1].split(" : ")[1]
						for ldevlist in ldevlist_line.splitlines() :
							if "VOL_Capacity" in ldevlist:
								ldev_dict["VOL_Capacity"] = ldevlist.split(" : ")[1]
							elif "PORTs" in ldevlist :
								ldev_dict["PORTs"] = ldevlist.split(" : ")[1:]
							elif "RAID_LEVEL" in ldevlist :
								ldev_dict["RAID_LEVEL"] = ldevlist.split(" : ")[1]
							elif "RAID_TYPE" in ldevlist :
								ldev_dict["RAID_TYPE"] = ldevlist.split(" : ")[1]
							elif "RAID_GROUPs" in ldevlist :
								ldev_dict["RAID_GROUPs"] = ldevlist.split(" : ")[1]
							else :
								continue
						ldev_list.append(ldev_dict)
				self.storage_ldev_dict[storage] = ldev_list
			except Exception as e :
				logger.error(e)
				raise e

	def importtodata(self):
		try:
			for storage in self.args :
				storage_serial = storage.split("_")[0]
				old_serial = LdevList.objects.filter(serial=storage_serial)
				if len(old_serial) != 0 :
					old_serial.delete()
				for ldev_info in self.storage_ldev_dict[storage] :
					ldev_tmp = str(hex(int(ldev_info["LDEV"]))).upper().split("X")[1].zfill(4)
					LDEV = ldev_tmp[0:2] + ":" + ldev_tmp[2:4]
					VOL_Capacity = int(ldev_info["VOL_Capacity"])/1024/1024/2
					RAID_LEVEL = ldev_info["RAID_LEVEL"]
					RAID_TYPE = ldev_info["RAID_TYPE"]
					RAID_GROUPs = ldev_info["RAID_GROUPs"]
					if len(ldev_info["PORTs"]) :
						for PORT in ldev_info["PORTs"] :
							port_info = PORT.split(" ")
							host = str(port_info[2])
							hlun_id = str(port_info[1])
							hport = str(port_info[0][0:5])
							new_serial = LdevList(serial=storage_serial,ldev=LDEV,vol_capacity=VOL_Capacity,raid_level=RAID_LEVEL,raid_type=RAID_TYPE,raid_groups=RAID_GROUPs,ports=hport,hostname=host,hlun_id=hlun_id)
							new_serial.save()
					else:
						new_serial = LdevList(serial=storage_serial,ldev=LDEV,vol_capacity=VOL_Capacity,raid_level=RAID_LEVEL,raid_type=RAID_TYPE,raid_groups=RAID_GROUPs)
						new_serial.save()
		except Exception as e :
			logger.error(e)
			raise e