from flask import Flask, render_template
import simplejson as json
import data
import datetime
import coop-friendship

app = Flask(__name__)


def export(date, my_array, friend_array, result):
    output = json.dumps(['result', {'date':(date),
                                     'my_array':(my_array),
                                     'friend_array':(friend_array),
                                     'result':(result)}])

    return output



export()