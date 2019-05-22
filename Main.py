import mysql.connector

db = mysql.connector.connect(
  host="kluniversity-cluster.cluster-cefcziwk2pxu.ap-south-1.rds.amazonaws.com",
  user="kluniversity",
  passwd="kluniversity_123"
)

point = db.cursor()
point.execute("use exam_database")

country=input('Destination_Country : ')

wt=int(input('Weight : '))/1000
lenn=int(input('Length : '))
wid=int(input('Width : '))
ht=int(input('Height : '))
vol_wt=(lenn*wid*ht)/5000
for i in range(1,10):
    if(i==2 or i==4):
        query = "select * from logistics_names as lr,rate_card as rc,logistics_zone as z, charges as ch where (lr.id=rc.logistics_id and z.logistics_id=rc.logistics_id and z.country='" +country+ "' and lr.id="+str(i)+" and rc.zone=z.zone and z.logistics_id=ch.logistic_id and rc.weight>="+str(wt)+")limit 1"
    else:
        query = "select * from logistics_names as lr,rate_card as rc,logistics_zone as z, charges as ch where (lr.id=rc.logistics_id and z.logistics_id=rc.logistics_id and z.country='"+country+"' and lr.id="+str(i)+" and rc.zone=z.zone and z.logistics_id=ch.logistic_id and rc.weight>="+str(vol_wt)+")limit 1"
    try:
        point.execute(query)

        data = point.fetchall()
        val=data[0][7]
        price=val+((val*data[0][14])/100)+((val*data[0][15])/100)+((val*data[0][16])/100)+(data[0][17])+((val*data[0][18])/100)+(data[0][19])
        print(i,'carrier: ',data[0][1],', ',data[0][2],', ','weight considered : ',data[0][6],', ','Price : ',price)
    except IndexError as ie:
        print('No Data available')