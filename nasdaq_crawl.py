from yahoo_fin import stock_info as si
import csv
import json
import datetime

json_val_map = {}

# Load old map if exists
with open('curr_map.json') as json_file:
    json_val_map = json.load(json_file)

# Generate word pairs
# bbc, alj, bzfd, fox
word_title_set = {}
word_description_set = {}
now = datetime.datetime.now()
curr_day_str = "{}.{}.{}".format(now.year, now.month, now.day)
bbc = "tutorial/tutorial/bbc-news/bbc-processed/{}.{}.{}".format("bbc", curr_day_str, "json")
alj = "tutorial/tutorial/alj-news/alj-processed/{}.{}.{}".format("alj", curr_day_str, "json")
bzfd = "tutorial/tutorial/bzfd-news/bzfd-processed/{}.{}.{}".format("bzfd", curr_day_str, "json")
fox = "tutorial/tutorial/fox-news/fox-processed/{}.{}.{}".format("fox", curr_day_str, "json")
spiders = [bbc, alj, bzfd, fox]

for spider in spiders:
    with open(spider) as bbc_f:
        for line in bbc_f:
            if line.strip() == "[" or line.strip() == "]":
                continue
            new_line = line.strip()
            if new_line[len(new_line) - 1] == ",":
                new_line = line[:len(line) - 2]
            json_line = json.loads(new_line)
            title_s = json_line["title"].split(" ")
            description_s = json_line["description"].split(" ")
            for word in title_s:
                if word_title_set.get(word) == None:
                    word_title_set[word] = 1
            for word in description_s:
                if word_description_set.get(word) == None:
                    word_description_set[word] = 1

# Build new map
count = 0
with open('companylist.csv', newline='') as csvfile:
    creader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in creader:
        count += 1
        company_acr = row[0]
        try:
            company_value = si.get_live_price(company_acr)
            print(company_acr)
        except:
            print("Failed on " + company_acr)
            continue

        if json_val_map == {}:
            json_val_map["companies"] = {}
        elif json_val_map["companies"].get(company_acr) == None:
            json_val_map["companies"][company_acr] = {}
            json_val_map["companies"][company_acr]["values"] = [company_value]
            json_val_map["companies"][company_acr]["good_val_title"] = {}
            json_val_map["companies"][company_acr]["bad_val_title"] = {}
            json_val_map["companies"][company_acr]["good_val_descrip"] = {}
            json_val_map["companies"][company_acr]["bad_val_descrip"] = {}
        else:
            json_val_map["companies"][company_acr]["values"].append(company_value)
            size = len(json_val_map["companies"][company_acr]["values"])
            if json_val_map["companies"][company_acr]["values"][size - 2] >= company_value:
                for word in word_title_set:
                    if json_val_map["companies"][company_acr]["bad_val_title"].get(word) == None:
                        json_val_map["companies"][company_acr]["bad_val_title"][word] = 1
                    else:
                        json_val_map["companies"][company_acr]["bad_val_title"][word] += 1
                for word in word_description_set:
                    if json_val_map["companies"][company_acr]["bad_val_descrip"].get(word) == None:
                        json_val_map["companies"][company_acr]["bad_val_descrip"][word] = 1
                    else:
                        json_val_map["companies"][company_acr]["bad_val_descrip"][word] += 1
            else:
                for word in word_title_set:
                    if json_val_map["companies"][company_acr]["good_val_title"].get(word) == None:
                        json_val_map["companies"][company_acr]["good_val_title"][word] = 1
                    else:
                        json_val_map["companies"][company_acr]["good_val_title"][word] += 1
                for word in word_description_set:
                    if json_val_map["companies"][company_acr]["good_val_descrip"].get(word) == None:
                        json_val_map["companies"][company_acr]["good_val_descrip"][word] = 1
                    else:
                        json_val_map["companies"][company_acr]["good_val_descrip"][word] += 1

# Write new map to file
with open("curr_map.json", "w") as write_file:
    json.dump(json_val_map, write_file)


# get live price of Apple
#val1 = si.get_live_price("aapl")

# or Amazon
#val2 = si.get_live_price("amzn")

# print(val1)
# print("----")
# print(val2)
