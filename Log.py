#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Log.py
# (c) Oleg Plaxin 2018
# plaxoleg@gmail.com

# -*- coding: utf-8 -*-

import os
import time

LOG_PATH = "./Logs/"
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)


def get_sys_time():
    now = time.localtime()
    nt = time.strftime("%d %b %Y %H:%M:%S", now)
    return nt


def info(tag, message):
    log_text = str(get_sys_time()) + " /" + "I:" + str(tag) + ": " + str(message).replace("\n", "\n\t\t\t\t\t\t")
    print_log(log_text)
    save_to_file(log_text)


def debug(tag, message):
    log_text = str(get_sys_time()) + " /" + "D:" + str(tag) + ": " + str(message).replace("\n", "\n\t\t\t\t\t\t")
    print_log(log_text)
    save_to_file(log_text)


def warning(tag, message):
    log_text = str(get_sys_time()) + " /" + "W:" + str(tag) + ": " + str(message).replace("\n", "\n\t\t\t\t\t\t")
    print_log(log_text)
    save_to_file(log_text)


def error(tag, e):
    log_text = str(get_sys_time()) + " /" + "E:" + str(tag) + ": " + \
               "An error occurred. {class_name}: {e_str}".format(class_name=e.__class__.__name__, e_str=str(e))
    print_log(log_text)
    save_to_file(log_text)


def print_log(text):
    print(text)


def save_to_file(text):
    now = time.localtime()
    log_to_file = open(LOG_PATH + str(now.tm_year) + str(now.tm_mon) + str(now.tm_mday) + ".log", "a", encoding="utf-8")
    log_to_file.write(text + "\n")
