# Logistics-Cost-Calculator

Calculate the cost for shipping the item of weight x to the y country for each and every logistic from the data available in Database.

A seller named Pia, has got an order on Amazon.com from a United States buyer Michale.
Pia warehouse is in India and she now wants to process this order to United States. Pia
has to select best logistics partner to ship this order to Michale. Pia has a tie up with
different International logistics partners like (DHL Express, Fedex Priority, DHL
Ecommerce International, DHL Ecommerce, Delhivery, UPS & India Post ).
Pia is confusing to use which logistics among them. Hence, she would like to know the
cost for each logistics partner. In order to calculate the logistics partner cost she will
have to include various addition components mentioned below:
● Logistics Base rate
● Fuel surcharge
● Gst
● Dtp charges
● Exchange surcharges
● Domestic shipping charges
For DHL Ecommerce and india post Actual weight should be considered and rest will the
greater among volumetric and actual weight.
NOTE:
1. Calculate Volumetric Weight in Kg= (L*B*H)/5000
2. Actual weight is the flat weight of the package(order).
Finally the pia wants the rate card for all the logistics which is available to the country
United States.
Output format:
Logistics carrier name, Shipping price, considered weight, timeline/Duration
Host: kluniversity-cluster.cluster-cefcziwk2pxu.ap-south-1.rds.amazonaws.com
User: kluniversity
Password: kluniversity_123
Database : exam_database
Tables :
● Charges
● Logistics_names
● Logistics_zone
● rate_card
Logistics_names:
● id,logistics_id,logistics_name
Logistics_zone:
● id,logistics_id,country,zone
Rate_card:
● id, logistics_id,zone,weight,price
Charges:
● Id, logistics_id, premium( % on price), fuel_surcharges(% on price), gst(% on price),
dtp_charges(in INR), exchange_surcharges( % on price), domestic_shipping_charges(in
INR)
Input :
Destination_country,weight,length,width,height.
Calculate the shipping rate for each logistics carrier.
Example
Input:
Destination_country: United States
weight(in grams): 500
length(in cms): 25
width(in cms): 26
height(in cms): 10
Output:
● carrier:DHL Express, price:1464.37, timeline:4 - 6 Working Days, weight_considered:1.5
kg
● Carrier: Fedex Priority, price:1491.5, timeline:5 - 7 Working Days, weight_considered:1.5
kg
● carrier:DHL Ecommerce International, price:1324.79, timeline:10 -12 Working Days,
weight_considered:1.3 kg
● carrier:DHL Ecommerce, price:804.59, timeline:12 - 15 Working Days,
weight_considered: 0.5kg
● carrier:Delhivery, price:1437.82, timeline:7 - 10 Working Days, weight_considered: 1.5kg
● carrier:UPS, price:1215.12, timeline:8 -10 Working Days, weight_considered: 1.3 kg
● carrier:Indiapost, price:495.0, timeline:15 Working Days, weight_considered: 0.5 kg
