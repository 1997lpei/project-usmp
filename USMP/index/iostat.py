#!/bin/bash/python
# -*- coding:utf-8 -*-
import sys
import os
import re
import datetime
import json


class iostat(object):
    cls_iostatlog = {}
    disk = ""
    option = ""
    time_pattern = "(\d{1,2}/\d{1,2}/\d{2}\s\d{2}:\d{2}:\d{2})|(\d{1,2}/\d{1,2}/\d{4}\s\d{2}:\d{2}:\d{2}\s+[A|P]+M)"
    disk_pattern = "sd[a-z]{1,2}|dm-\d{1,3}"
    filepath = "uploadfiles/iostatlog/"
    """docstring for iostat"""

    def __init__(self):
        super(iostat, self).__init__()

    def getiostat(self,arg):
        if arg[0] == "undefined" or arg[1] == "undefined":
            return {"date": [], "data": []}
        iostat_log = {}
        disk_performance = {}
        time_list = []
        performance_option = []
        performance_data = []
        with open("/home/liu/PycharmProjects/USMP/uploadfiles/iostatlog/iostat.log", "r+") as f:
            for line in f:
                time = re.match(self.time_pattern, line)
                disk = re.match(self.disk_pattern, line)
                if time:
                    time_list.append(str(time.group()))
                    if len(time_list) > 1:
                        iostat_log[time_list[-2]] = disk_performance
                    disk_performance = {}
                    iostat_log[time_list[-1]] = disk_performance
                elif "Device:" in line and not len(performance_option):
                    line_list = line.strip().split(" ")
                    for var in line_list:
                        if len(var) and not "Device:" in var:
                            performance_option.append(var)
                elif disk:
                    line_list = line.strip().split(" ")
                    for var in line_list[1:]:
                        if len(var):
                            performance_data.append(var)
                    disk_performance[str(disk.group())] = performance_data
                    performance_data = []
        f.close()
        n = performance_option.index(arg[1])
        result = {"date": [], "data": []}
        data = []
        for var in time_list:
            data.append(iostat_log[var][arg[0]][n])
        result["date"] = time_list
        result["data"] = data
        return result

    def getoption(self,arg):
        iostat_log = {}
        disk_performance = {}
        time_list = []
        performance_option = []
        performance_data = []
        print self.filepath+arg
        with open(self.filepath+arg, "r+") as f:
            for line in f:
                time = re.match(self.time_pattern, line)
                disk = re.match(self.disk_pattern, line)
                if time:
                    time_list.append(str(time.group()))
                    if len(time_list) > 1:
                        iostat_log[time_list[-2]] = disk_performance
                    disk_performance = {}
                    iostat_log[time_list[-1]] = disk_performance
                elif "Device:" in line and not len(performance_option):
                    line_list = line.strip().split(" ")
                    for var in line_list:
                        if len(var) and not "Device:" in var:
                            performance_option.append(var)
                elif disk:
                    line_list = line.strip().split(" ")
                    for var in line_list[1:]:
                        if len(var):
                            performance_data.append(var)
                    disk_performance[str(disk.group())] = performance_data
                    performance_data = []
        f.close()
        result = {"option": [], "disk": []}
        result["option"] = performance_option
        result["disk"] = iostat_log[time_list[0]].keys()
        result["data"] = iostat_log
        result["date"] = time_list
        return result

