import urllib.request 
import csv
from html_reader.parser import HTMLTableParser 

def filter_goods_list(entry): 
    time = entry[3]
    price = int(entry[2])
    
    if (time.find("Instant") != -1): 
        return True 
    if (price == 0): 
        return True 
    
    # Ignored production buildings
    discarded_sources = ["crop", "Field", "animal product", "Feed", "Mine", "Lure", "Net", "Lobster", "Duck"]
    source = entry[-1] 

    for discard in discarded_sources: 
        if (source.find(discard) != -1): 
            return True
    return False 

def convert_time_str_minute(entry): 
    time_str = entry[3]

    # ignore faster production times 
    time_str = time_str[:time_str.find("★") - 1]

    day_idx = time_str.find('d')
    hr_idx = time_str.find('h')
    min_idx = time_str.find('min')
    
    days = 0
    hours = 0
    mins = 0 
    if (day_idx != -1): 
        days = int(time_str[:day_idx-1])
    else: 
        day_idx = -2
    
    if (hr_idx != -1): 
        hours = int(time_str[day_idx + 2:hr_idx - 1])
    else: 
        hr_idx = -2 
    
    if (min_idx != -1): 
        mins = int(time_str[hr_idx + 2:min_idx - 1])
    
    time_min = 360 * days + 60 * hours + mins 

    entry[3] = time_min 
    return entry 

def read_html_to_csv(): 
    hayday_goods_list = 'https://hayday.fandom.com/wiki/Goods_List'

    # pull goods_list from hayday wiki 
    req = urllib.request.Request(url=hayday_goods_list)
    f = urllib.request.urlopen(req)
    xhtml = f.read().decode('utf-8')

    p = HTMLTableParser()
    p.feed(xhtml)
    goods_list = p.tables[0][1:]

    # remove unecessary columns ("Needs", "Per boat crate")
    goods_list = [entry[0:5] + entry[6:7] for entry in goods_list]

    # remove invalid entries 
    goods_list = [good for good in goods_list if not filter_goods_list(good)]

    # convert time string to minutes
    goods_list = [convert_time_str_minute(good) for good in goods_list]

    # convert level and max price to int
    # for good in goods_list: 
    #    good[1] = int(good[1])
    #    good[2] = int(good[2]) 

    fields = ['name', 'level', 'price', 'time', 'xp', 'source']

    with open('goods_list.csv', 'w', encoding="utf-8", newline='') as f: 
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(goods_list)
