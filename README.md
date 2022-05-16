# Courier Tracking API
![-----------------------------------------------------](https://raw.githubusercontent.com/cyberboysumanjay/web/master/colored.png)

This API is capable of fetching tracking details from multiple courier service providers.

## Show some :heart: and :star: the repo to support the project
[![GitHub stars](https://img.shields.io/github/stars/cyberboysumanjay/CourierAPI.svg?style=social&label=Star)](https://github.com/cyberboysumanjay/CourierAPI) ![GitHub followers](https://img.shields.io/github/followers/cyberboysumanjay.svg?style=social&label=Follow)
[![Telegram Channel](https://img.shields.io/endpoint?color=neon&style=flat-square&url=https%3A%2F%2Ftg.sumanjay.workers.dev%2Fsjprojects)](https://telegram.dog/sjprojects)
![-----------------------------------------------------](https://raw.githubusercontent.com/cyberboysumanjay/web/master/colored.png)
## Supported Courier Services
This API supports multiple courier services. 
Here is a complete list of supported services.
1. Ekart Logistics (ekart)
2. DTDC (dtdc)
3. Gati Express (gati)
4. More to be added soon..

Feel free to create a PR for adding support for more courier service providers or wait for them to ship an order to me :smile:
![-----------------------------------------------------](https://raw.githubusercontent.com/cyberboysumanjay/web/master/colored.png)
## Usage
Make a get request specifying the service provider name and the tracking id
```
https://courier.deta.dev/{courier_name}/{tracking_id}
```
Example - https://courier.deta.dev/dtdc/Z74562053

![-----------------------------------------------------](https://raw.githubusercontent.com/cyberboysumanjay/web/master/colored.png)

## Response Format

The response JSON Object looks something like this - 

```JSON
{
  "status": true,
  "data": [
    {
      "tracking_id": "Z74562053",
      "activity": "Successfully Delivered",
      "date": "09-05-2022",
      "time": "14:35",
      "status": "Delivered",
      "origin": "gachibowli master franchisee",
      "destination": ""
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Out For Delivery",
      "date": "09-05-2022",
      "time": "11:11",
      "status": "Out For Delivery",
      "origin": "gachibowli master franchisee(KONDAPUR - MASID BANDA)",
      "destination": ""
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Received at Facility",
      "date": "08-05-2022",
      "time": "18:06",
      "status": "In Transit",
      "origin": "gachibowli master franchisee",
      "destination": ""
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Received at Facility",
      "date": "08-05-2022",
      "time": "18:04",
      "status": "In Transit",
      "origin": "gachibowli master franchisee",
      "destination": "gachibowli master franchisee"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Processed & Forwarded From Hub",
      "date": "08-05-2022",
      "time": "14:45",
      "status": "In Transit",
      "origin": "hyderabad shamshabad apex",
      "destination": "gachibowli master franchisee"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Processed & Forwarded to Hub",
      "date": "08-05-2022",
      "time": "08:24",
      "status": "In Transit",
      "origin": "hyderabad shamshabad apex",
      "destination": "gachibowli master franchisee"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Received at Hub",
      "date": "08-05-2022",
      "time": "07:53",
      "status": "In Transit",
      "origin": "hyderabad shamshabad apex",
      "destination": ""
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Received at Hub",
      "date": "08-05-2022",
      "time": "02:58",
      "status": "In Transit",
      "origin": "delhi samalkha apex",
      "destination": "hyderabad shamshabad apex"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Received at Hub",
      "date": "08-05-2022",
      "time": "02:26",
      "status": "In Transit",
      "origin": "delhi samalkha apex",
      "destination": "hyderabad shamshabad apex"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Processed & Forwarded From Facility",
      "date": "07-05-2022",
      "time": "15:15",
      "status": "In Transit",
      "origin": "delhi samalkha apex",
      "destination": "hyderabad shamshabad apex"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Received at Hub",
      "date": "07-05-2022",
      "time": "12:04",
      "status": "In Transit",
      "origin": "gurgaon apex",
      "destination": "delhi samalkha apex"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Processed & Forwarded From Hub",
      "date": "07-05-2022",
      "time": "03:22",
      "status": "In Transit",
      "origin": "gurgaon apex",
      "destination": "delhi samalkha apex"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Processed & Forwarded to Hub",
      "date": "07-05-2022",
      "time": "02:21",
      "status": "In Transit",
      "origin": "gurgaon apex",
      "destination": "hyderabad shamshabad apex"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Booked At Hub",
      "date": "06-05-2022",
      "time": "20:03",
      "status": "Booked",
      "origin": "gurgaon apex",
      "destination": "Booked to HYDERABAD"
    },
    {
      "tracking_id": "Z74562053",
      "activity": "Softdata Upload",
      "date": "06-05-2022",
      "time": "19:10",
      "status": "Softdata Upload",
      "origin": "first mile",
      "destination": "Booking Initiated"
    }
  ]
}
```
## Deployment
[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/cyberboysumanjay/CourierAPI)
##### :star: the Repo in case you liked it :)
##### Made with :heart: in India

#### © [Sumanjay](https://cyberboysumanjay.github.io)
