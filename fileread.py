#! /usr/bin/env python3
# @Author Hugo

import csv

class csvread:
    def __init__(self):
        self.data = []

    def read(self, file_name):
        with open(file_name, 'r') as io_read:
            for row in csv.reader(io_read,  delimiter=','):
                if len(row) > 0:
                    self.data.append(row)
        return self.data

    def write(self, file_name, data):
        with open(file_name, 'w') as io_write:
            w = csv.writer(io_write,  delimiter=',')
            w.writerows(data)

    def append(self, file_name, data):
        with open(file_name, 'a') as io_write:
            w = csv.writer(io_write,  delimiter=',')
            w.writerows(data)

