import os
import csv
from html_reader.read_hayday_data import read_html_to_csv
from queue import PriorityQueue
import argparse


def main():
    parser = argparse.ArgumentParser("Prints out the best hayday items to produce at a given level for each production building.")
    parser.add_argument('level', type=int, help='current hayday level')
    parser.add_argument('-n', "--num_goods", type=int, default=3,
                        help='number of goods to print for each production building.')
    parser.add_argument('-xp', '--xp', action="store_true", default=False, help="calculates based on xp instead of price.")
    parser.add_argument('-t', "--time", action="store_true", default=False, help="factors in production time in calculations. this should be used if you are a more active player that checks your farm often")
    parser.add_argument('-ds', "--dairy_sugar", action="store_true", default=False, help="print out dairy and sugar mill production info (defaultly ignores dairy and sugar)")

    args = parser.parse_args()
    if args.level > 0: 
        level = args.level
    else: 
        print("Invalid level. ")
        exit()
    
    use_time = args.time
    xp = args.xp
    
    num_items = args.num_goods

    html_file =  "goods_list.csv"
    if not os.path.isfile(html_file): 
        read_html_to_csv()

    # filters read csv by level
    with open('goods_list.csv', 'r', encoding="utf-8") as f: 
        csv_goods_list = list(csv.reader(f))
        goods_list = [entry for entry in csv_goods_list[1:] if int(entry[1]) <= level]
    
    prod_build_dict = {}
    for good in goods_list:
        # defaultly ignore Dairy and Sugar Mill
        if not args.dairy_sugar and good[-1] in {"Dairy", "Sugar Mill"}: 
            continue

        if not good[-1] in prod_build_dict:
            prod_build_dict[good[-1]] = PriorityQueue()
        
        time = 1
        if use_time: 
            time = int(good[3])

        if xp: 
            value = int(good[4])
        else: 
            value = int(good[2])

        priority = -1.0 * value/time
        prod_build_dict[good[-1]].put((priority, good))
        
    for building in prod_build_dict:
        print(building)
        for _ in range(num_items):
            if not prod_build_dict[building].empty(): 
                good = prod_build_dict[building].get()[1]
                
                time = 1 
                unit = ""
                if use_time: 
                    time = int(good[3])/60
                    unit="/hr"

                if xp: 
                    value = int(good[4])
                    unit = "xp" + unit
                else: 
                    value = int(good[2])
                    unit = "coins" + unit

                value = round(value / time) 
                
                print(" ", value, unit, "\t", good[0])
            else: 
                continue
        print()
    return 0


if __name__ == '__main__': 
    main()