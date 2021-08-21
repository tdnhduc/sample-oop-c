import csv
from os import read
import requests
from datetime import datetime


# step 1 : get ur l
# run get request
# get value from next
# ccắt  chuỗi , nối  chuỗi  trong  pythonn
# kiểu  dữ  liệu  string  pythonn



# records =  [{'id' : 1, 'name' : 'a'}, {'id' : 3, 'name' : 'c'}, {'id' : 2, 'name' : 'b'}]
# 
    

 

# parameters : tham so

def get_data_from_api(origin_url, api):
    final_url = url + api
    json_response = requests.get(final_url).json()
    print(json_response['result']['records'])
    records = json_response['result']['records']
    records.sort(key=lambda x : x['Mã hành chính'])

    api = json_response['result']['_links']['next']
    print(api)
    is_finish = False
    if json_response['result']['records'] == []:
        is_finish = True   
    return (is_finish, api, records)

def write_to_csv_file(data):
    # append -> write append
    # write -> truncate file before write
    with open(file_name, mode='a') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)

def read_csv_file(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)
        return csv_reader


# true and false
# while True == always True -> ko bao gio dung lai

headers = ['_id', 'HASC', 'ISO', 'FIPS', 'Mã hành chính', 'Tỉnh', 'Số ca nhiễm', 'Đang điều trị', 'Bình phục', 'Tử vong']

file_name = 'report_covid_victims_' + datetime.today().strftime('%Y-%m-%d') + '.csv'



if __name__ == "__main__":
    reocords_19 = read_csv_file("report_covid_victims_2021-08-19csv")
    records_20 = read_csv_file("report_covid_victims_2021-08-20.csv"")
    # url = "https://data.opendevelopmentmekong.net/vi"
    # api = "/api/3/action/datastore_search?limit=10&resource_id=b15e8f4b-c905-48fb-973e-d412e2759f55"
    
    # write_to_csv_file(headers)

    # while True:
    #     (is_finish, next_api, records) = get_data_from_api(url, api)
    #     if is_finish == True:
    #         break
    #     else:
    #         for record in records:
    #             write_to_csv_file(record.values())
    #     api = next_api

# 1. String
# 2. Write/ read file 
# 3. for loop / while loop
# 4. requests package 
# http request : GET / POST / PUT / ....

# calculating 
# 1. read file 21.8.2021
# 2. read file 20.8.2021


# lấy soos ca nhiễm của HN trong file data 21.08.2021 - 
