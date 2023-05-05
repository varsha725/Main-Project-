
from flask import *

from src.dbconnection import *

app = Flask(__name__)


@app.route('/login',methods=['post'])
def login():
    print(request.form)
    uname = request.form['uname']
    pswd = request.form['pswd']

    qry = "select * from login where `username`=%s and password=%s"
    res = selectone(qry, (uname,pswd))

    if res is None:
        return jsonify({"task": "invalid"})
    else:
        return jsonify({"task": "valid", "id": res['lid'],"type":res['type']})




@app.route('/sendfeed', methods=['post'])
def sendfeed():

    lid = request.form['lid']
    feedback=request.form['feed']
    res=request.form['rid']
    q="INSERT INTO `feedback` VALUES(NULL,%s,%s,%s,CURDATE())"
    iud(q,(res,lid,feedback))
    return jsonify({'task':'valid'})


@app.route('/viewneareststation',methods=['POST'])
def viewneareststation():
    lattitude=request.form['lattitude']
    longitude=request.form['longitude']
    print(lattitude,longitude,"===========================")
    qry="SELECT `station`.* ,(3959 * ACOS ( COS ( RADIANS('"+lattitude+"') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('"+longitude+"') ) + SIN ( RADIANS('"+lattitude+"') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `station` HAVING user_distance  < 31.068 "
    res=selectall(qry)
    print(res)
    return jsonify(res)
@app.route('/viewnearestres',methods=['POST'])
def viewnearestres():
    lattitude=request.form['lattitude']
    longitude=request.form['longitude']
    print(lattitude,longitude,"===========================")
    qry="SELECT `restaurant`.*, (3959 * ACOS ( COS ( RADIANS('"+lattitude+"') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('"+longitude+"') ) + SIN ( RADIANS('"+lattitude+"') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM `restaurant` HAVING user_distance  < 31.068 "
    res=selectall(qry)
    print(res)
    return jsonify(res)

# ====================================================
@app.route('/addtocart', methods=['POST'])
def addtocart():
    pro_id=request.form['iid']
    qty=request.form['qty']
    lid=request.form['lid']


    qq="select * from `menu` where `menuid`=%s"
    rees=selectone(qq,pro_id)
    tt=int(rees['price'])*int(qty)
    stock=rees['qty']
    nstk=int(stock)- int(qty)
    # print(stock,"909090",  qty)
    # if stock>=qty:
    if (int(qty) < rees['qty']):

        up="update `menu` set `qty`=%s where `menuid`=%s"
        iud(up,(nstk,pro_id))

        q="select * from `order` where `userid`=%s and `status`='cart'"
        res=selectone(q,lid)

        if res is None:
            qry="insert into `order` values (null,%s,%s,'cart')"
            val=(lid,tt)
            id=iud(qry,val)
            qry1="insert into `orderitem` values (null,%s,%s,%s,curdate(),'cart')"
            va=(str(id),pro_id,qty)
            iud(qry1,va)
            return jsonify({"task":"success"})
        else:
            total=int(res['total'])+int(tt)
            qry = "UPDATE `order` SET `total`=%s WHERE `orderid`=%s"
            val = (total, str(res['orderid']))
            id = iud(qry, val)

            qry1="SELECT * FROM `orderitem` WHERE `pid`=%s AND `orderid`=%s"
            res12=selectone(qry1,(pro_id,str(res['orderid'])))
            print(res12)
            if res12 is None:
                qry1 = "insert into `orderitem` values (null,%s,%s,%s,curdate(),'cart')"
                va = (str(res['orderid']), pro_id, qty)
                iud(qry1, va)
            else:
                qry1 = "UPDATE `orderitem` SET `quantity`=%s WHERE `itemid`=%s"
                quty=int(res12['quantity'])+int(qty)
                va = (quty,str(res12['itemid']))
                iud(qry1, va)
            return jsonify({"task": "success"})
    else:
        return jsonify({"task":"out of stock"})




# @app.route('/addtocart', methods=['post'])
# def addtocart():
#     qty = request.form['qty']
#     pid = request.form['iid']
#     lid = request.form['lid']
#     qry="SELECT * FROM `menu` WHERE `menuid`=%s"
#     res=selectone(qry,pid)
#     if(int(qty)<res['qty']):
#         qry="SELECT * FROM `order` WHERE `userid`=%s AND `status`='pending'"
#         s=selectone(qry,lid)
#
#
#         if s is None:
#
#             qry="INSERT INTO `order` VALUES(NULL,%s,'0','pending')"
#             id=iud(qry,lid)
#
#             q = "SELECT * FROM `orderitem` WHERE `pid`=%s AND `status`='cart'"
#             res = selectone(q, pid)
#             if res is None:
#                 q = "INSERT INTO `orderitem` VALUES(NULL,%s,%s,%s,CURDATE(),'cart')"
#                 v = (str(id),pid, qty)
#                 iud(q, v)
#                 return jsonify({'task': 'success'})
#             else:
#                 qry="UPDATE `orderitem` SET `quantity`=`quantity`+%s WHERE `pid`=%s"
#                 va=(qty,pid)
#                 iud(qry,va)
#                 return jsonify({'task': 'success'})
#         else:
#             q="INSERT INTO `orderitem` VALUES(NULL,%s,%s,%s,CURDATE(),'cart')"
#             v=(s['orderid'],pid,qty)
#             iud(q,v)
#             return jsonify({"task":"success"})
#
#     else:
#         return jsonify({'task': 'insufficient quantity'})


# =====================================================================

@app.route('/view_status', methods=['post'])
def view_status():
    print(request.form)
    id = request.form['lid']
    qry = "SELECT `order`.`orderid`,`order`.`status`,`orderitem`.`quantity`,`menu`.`items`,`menu`.`price`,`menu`.`image`FROM `orderitem`JOIN `order`ON `order`.`orderid`=`orderitem`.`orderid`JOIN `menu`ON `menu`.`menuid`=`orderitem`.`pid` WHERE `order`.`userid`=%s"
    res = selectall2(qry,id)
    print(res,"===")
    return jsonify(res)




@app.route('/viewwork', methods=['post'])
def viewwork():
    print(request.form)
    id = request.form['lid']
    qry = "SELECT * FROM `assign` JOIN `order` ON assign.oid=`order`.orderid JOIN `orderitem` ON `order`.orderid=`orderitem`.orderid JOIN `menu` ON `orderitem`.pid=`menu`.menuid  JOIN user ON order.userid=user.lid JOIN `location` ON `user`.lid=location.lid JOIN details ON order.orderid=details.oid  WHERE assign.lid=%s and assign.status!='Delivered'"
    res = selectall2(qry,id)
    print(res,"===")
    return jsonify(res)


@app.route('/signup',methods=['post'])
def signup():
    fname=request.form['fname']
    lname=request.form['lname']

    email = request.form['email']
    phone=request.form['phone']
    username=request.form['username']
    password=request.form['password']

    qry1 = "INSERT INTO `login` VALUES (NULL,%s,%s,'user')"
    val1 = (username, password)
    id =iud(qry1, val1)
    qry="INSERT INTO `user` VALUES(NULL,%s,%s,%s,%s,%s)"
    val=(fname,email,phone,str(id),lname)
    iud(qry, val)
    return jsonify({'task': 'valid'})


@app.route('/viewassign', methods=['post'])
def viewassign():
    print(request.form)
    id = request.form['lid']
   
    qry = "SELECT `order`.`orderid`,`order`.`status`,assign.*,location.* FROM `order` JOIN `assign` ON `order`.orderid=`assign`.oid JOIN location ON `assign`.lid=`location`.lid WHERE `order`.`userid`=%s"
    res = selectall2(qry,id)
    print(res,"===")
    return jsonify(res)



@app.route('/viewres', methods=['post'])
def viewres():
    qry = "SELECT * FROM restaurant"
    res = selectall(qry)

    return jsonify(res)


@app.route('/viewmycart', methods=['post'])
def viewmycart():
    uid=request.form['lid']
    q="SELECT `menu`.*,`orderitem`.* ,`order`.* FROM `menu` JOIN `orderitem` ON `orderitem`.`pid`=`menu`.`menuid`  JOIN `order`ON `order`.`orderid`=`orderitem`.`orderid`WHERE `order`.`userid`=%s AND orderitem.`status`='cart'"
    res=selectall2(q,uid)
    print(res)

    w="SELECT SUM(`menu`.`price`*`orderitem`.`quantity`) AS ss,`order`.`orderid`  FROM `menu` JOIN `orderitem` ON `orderitem`.`pid`=`menu`.`menuid` JOIN `order` ON `order`.`orderid`=`orderitem`.`orderid` WHERE `order`.`userid`=%s AND orderitem.`status`='cart'"
    res1 = selectone(w, uid)

    print(res)
    return jsonify(data=res,data1=res1['ss'])










@app.route('/deletecart', methods=['post'])
def deletecart():
    itemid = request.form['iid']
    q="DELETE FROM `orderitem` WHERE `itemid`=%s"
    iud(q,itemid)
    return jsonify({'task':'success'})


@app.route('/cartorder', methods=['post'])
def cartorder():
    print(request.form)
    tot=request.form['tot']
    oid=request.form['rid']
    uid=request.form['lid']
    seatno = request.form['seatno']
    station = request.form['station']
    trainname = request.form['trainname']
    trainno = request.form['trainno']

    q="INSERT INTO `details` VALUES(NULL,%s,%s,%s,%s,%s)"
    va=(oid,trainno,seatno,trainname,station)
    iud(q,va)
    qry="UPDATE  `order`SET `total`=%s,`status`='ordered' WHERE `orderid`=%s"
    val=(tot,oid)
    iud(qry,val)
    iud("UPDATE `orderitem` SET `status`='ordered' WHERE orderid=%s",oid)
    qry="SELECT * FROM `orderitem` WHERE `status`='cart' AND `orderid`=%s"
    res = selectall2(qry, oid)
    for i in res:
        q="UPDATE `menu` SET `qty`=qty-%s WHERE `menuid`=%s"
        v=(int(i['qty']),i['i_id'])
        iud(q,v)
        qr="UPDATE `orderitem` SET `status`='ordered' WHERE `status`='cart' AND `orderid`=%s"
        v=(uid)
        iud(qr,v)
    return jsonify({'task':"success"})






@app.route('/search_item', methods=['post'])
def search_item():
    print(request.form)
    ri=request.form['rid']
    item = request.form['search']
    qry = "SELECT * FROM `menu`  WHERE `items` LIKE '%"+item+"%' and rid='"+ri+"'"
    res = selectall(qry)
    print(res,"===")
    return jsonify(res)

@app.route('/payment_sucess', methods=['post'])
def payment_sucess():
       amnt = request.form['amt']
       rid = request.form['rid']
       qry = "INSERT INTO `payment` VALUES(NULL,%s,%s,CURDATE())"
       iud(qry,(rid,amnt))

       qry ="UPDATE `order` SET STATUS='payed' WHERE orderid=%s"
       iud(qry,(rid))
       return jsonify({"task": "success"})



@app.route('/addlocation', methods=['post'])
def addlocation():
    lid=request.form['lid']
    lat=request.form['lat']
    lon=request.form['lon']
    qry="SELECT * FROM `location` WHERE `lid`=%s"
    res=selectone(qry,lid)
    if res is None:
        qry="INSERT INTO `location` VALUES(NULL,%s,%s,%s)"
        val=(lid,lat,lon)
        iud(qry,val)
    else:
        qry="UPDATE `location` SET `latitude`=%s,`longitude`=%s WHERE `lid`=%s"
        val=(lat,lon,lid)
        iud(qry,val)
    return jsonify({'task': 'valid'})


@app.route('/updatestatus', methods=['post'])
def updatestatus():

    lid = request.form['aid']

    q="UPDATE `assign` SET STATUS='Delivered' WHERE aid=%s"
    iud(q,lid)
    return jsonify({'task':'valid'})


app.run(host='0.0.0.0', port=5000)
