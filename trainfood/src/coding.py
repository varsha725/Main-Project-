import os
from flask import*
from werkzeug.utils import secure_filename

from src.dbconnection import *
app=Flask(__name__)
app.secret_key="asd"
@app.route('/',methods=['post','get'])
def first():
    return render_template("homeindex.html")


@app.route('/login',methods=['post','get'])
def login():
    return render_template("index.html")


@app.route('/addstation',methods=['post'])
def addstation():
    return render_template("ADMIN/addstation.html")




@app.route('/addstation_post',methods=['post'])
def addstation_post():
    na =request.form['textfield']
    pla = request.form['textfield2']
    pos = request.form['textfield3']
    pin = request.form['textfield4']
    lat = request.form['textfield5']
    lon = request.form['textfield6']
    mob = request.form['textfield7']
    ema = request.form['textfield8']
    qry1="INSERT INTO  station VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(na,pla,pos,pin,mob,lat,lon,ema)
    iud(qry1,val1)
    return '''<script>alert("added");window.location='/managestation'</script>'''







@app.route('/addtsm',methods=['post'])
def addtsm():
    return render_template("ADMIN/addtsm.html")


@app.route('/addtsm_post',methods=['post'])
def addtsm_post():
    fn=request.form['textfield']
    ln = request.form['textfield2']
    pl = request.form['textfield3']
    po = request.form['textfield4']
    pi = request.form['textfield5']
    ph = request.form['textfield6']
    em = request.form['textfield7']
    tn = request.form['textfield45']
    us = request.form['textfield8']
    ps = request.form['textfield9']
    qry="insert into login values(null,%s,%s,'train service')"
    val=(us,ps)
    id=iud(qry,val)
    qry1="INSERT INTO  `service` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),fn,ln,tn,pl,po,pi,ph,em)
    iud(qry1,val1)
    return '''<script>alert("added");window.location='/trainservice'</script>'''



@app.route('/adminhome')
def adminhome():
    return render_template("ADMIN/adminhome.html")


@app.route('/managestation')
def managestation():
    qry="SELECT * FROM  station"
    res=selectall(qry)
    return render_template("ADMIN/managestation.html",val=res)


@app.route('/trainservice')
def trainservie():
    qry="SELECT * FROM `service` "
    res=selectall(qry)
    return render_template("ADMIN/trainservice.html",val=res)


@app.route('/delete_trainservice')
def delete_trainservie():
    id=request.args.get('id')
    qry="DELETE FROM service where serviceid=%s "
    iud(qry,id)
    return '''<script>alert("deleted");window.location='/trainservice'</script>'''

@app.route('/edit_trainservice')
def edit_trainservie():
    id=request.args.get('id')
    session['ETS_id']=id
    qry="SELECT * FROM service where lid=%s"
    res=selectone(qry,id)
    return render_template("ADMIN/edittsm.html", val=res)


@app.route('/edit_trainservice1',methods=['post'])
def edit_trainservie1():
    fn = request.form['textfield']
    ln = request.form['textfield2']
    pl = request.form['textfield3']
    po = request.form['textfield4']
    pi = request.form['textfield5']
    ph = request.form['textfield6']
    em = request.form['textfield7']
    qry="UPDATE `service` SET `fname`=%s,`lname`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email`=%s WHERE `lid`=%s"
    val=(fn,ln,pl,po,pi,ph,em,session['ETS_id'])
    iud(qry,val)
    return '''<script>alert("Edited successfully");window.location='/trainservice'</script>'''


@app.route('/verifyrestaurant')
def verifyrestaurant():
    qry="SELECT * FROM `restaurant` JOIN `login` ON `restaurant`.lid=`login`.lid WHERE `login`.type='pending'"
    res=selectall(qry)
    return render_template("ADMIN/verifyrestaurant.html",val=res)


@app.route('/reject', methods=['post','get'])
def reject():
    id=request.args.get('id')
    qry="UPDATE `login` SET type='Rejected' WHERE lid=%s"

    iud(qry,id)
    return '''<script>alert("Rejected");window.location="/verifyrestaurant"</script>'''

@app.route('/accept', methods=['post', 'get'])
def accept():
    id = request.args.get('id')
    qry = "UPDATE `login` SET type='restaurant' WHERE lid=%s"
    iud(qry, id)
    return '''<script>alert("Accepted");window.location="/verifyrestaurant"</script>'''


@app.route('/viewfeedback')
def viewfeedback():
    qry="select * from restaurant"
    res=selectall(qry)
    return render_template("ADMIN/viewfeedback.html",val=res)


@app.route('/viewfeedbacks',methods=['post'])
def viewfeedbacks():
    rid=request.form['select']
    qry="select * from restaurant"
    res=selectall(qry)
    qr="select * from user join feedback on user.lid=feedback.uid where feedback.rid=%s"
    re=selectall2(qr,rid)
    return render_template("ADMIN/viewfeedback.html",val=res,val1=re)

@app.route('/deletefeed', methods=['post', 'get'])
def deletefeed():
    id = request.args.get('id')
    qry = "delete from feedback where fid=%s"
    iud(qry, id)
    return '''<script>alert("Deleted");window.location="/viewfeedback"</script>'''


@app.route('/editstation')
def editstation():
    id=request.args.get('id')
    session['sid']=id
    qry="select * from station where sid=%s"
    res=selectone(qry,id)
    return render_template("ADMIN/editstation.html",val=res)



@app.route('/editstation_post',methods=['post'])
def editstation_post():
    na =request.form['textfield']
    pla = request.form['textfield2']
    pos = request.form['textfield3']
    pin = request.form['textfield4']
    lat = request.form['textfield5']
    lon = request.form['textfield6']
    mob = request.form['textfield7']
    ema = request.form['textfield8']
    qry1="UPDATE station SET `name`=%s,`place`=%s,`post`=%s,`pin`=%s,`mobileno`=%s,`latitude`=%s,`longitude`=%s,`email`=%s WHERE `sid`=%s"
    val1=(na,pla,pos,pin,mob,lat,lon,ema,session['sid'])
    iud(qry1,val1)
    return '''<script>alert("edited");window.location='/managestation'</script>'''


@app.route('/deletestation', methods=['post', 'get'])
def deletestation():
    id = request.args.get('id')
    qry = "delete from station where sid=%s"
    iud(qry, id)
    return '''<script>alert("Deleted");window.location="/managestation"</script>'''

@app.route('/additem',methods=['post'])
def additem():
    return render_template("RESTAURANT/additem.html")


@app.route('/additem_post',methods=['post'])
def additem_post():

    items = request.form['textfield']
    details = request.form['textfield3']

    photo = request.files['file']
    ff = secure_filename(photo.filename)
    photo.save(os.path.join('static/image', ff))
    date = request.form['textfield2']
    type = request.form['select']
    price = request.form['textfield4']
    qty = request.form['textfield4']
    qry1="INSERT INTO  menu VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(session['lid'],items,details,ff,date,type,price,qty)
    iud(qry1,val1)
    return '''<script>alert("added");window.location='/managemenu'</script>'''

@app.route('/edititempost',methods=['post'])
def edititempost():
    try:
        items = request.form['textfield']
        details = request.form['textfield3']
        photo = request.files['file']
        ff = secure_filename(photo.filename)
        photo.save(os.path.join('static/image', ff))
        date = request.form['textfield2']
        type = request.form['select']
        price = request.form['textfield4']
        qty = request.form['textfield5']
        qry1="UPDATE `menu` SET items=%s,details=%s,image=%s,date=%s,type=%s,price=%s,qty=%s WHERE menuid=%s"
        val1=(items,details,ff,date,type,price,qty,session['mid'])
        iud(qry1,val1)
        return '''<script>alert("Edited1");window.location='/managemenu'</script>'''
    except Exception as e:
        items = request.form['textfield']
        details = request.form['textfield3']
        date = request.form['textfield2']
        type = request.form['select']
        price = request.form['textfield4']
        qty = request.form['textfield5']
        qry1 = "UPDATE `menu` SET items=%s,details=%s,date=%s,type=%s,price=%s,qty=%s WHERE menuid=%s"
        val1 = (items, details, date, type, price,qty,session['mid'])
        iud(qry1, val1)
        return '''<script>alert("Edited");window.location='/managemenu'</script>'''



@app.route('/edititem',methods=['post','get'])
def edititem():
    id=request.args.get('id')
    session['mid']=id
    qry="select * from menu where menuid=%s"
    res=selectone(qry,id)
    return render_template("RESTAURANT/edititem.html",val=res)

@app.route('/deleteitem')
def deleteitem():
    id=request.args.get('id')
    qry="DELETE FROM menu where menuid=%s "
    iud(qry,id)
    return '''<script>alert("deleted");window.location='/managemenu'</script>'''

@app.route('/managemenu')
def managemenu():
    qry = "SELECT * FROM  menu where rid=%s"
    res = selectall2(qry,session['lid'])
    return render_template("RESTAURANT/managemenu.html",val=res)


@app.route('/restauranthome')
def restauranthome():
    return render_template("RESTAURANT/adminindex.html")

@app.route('/restaurantregister')
def restaurantregister():
    return render_template("RESTAURANT/restaurantregister.html")

@app.route('/trackorder')
def trackorder():
    qry="SELECT * ,`orderitem`.date AS dt FROM `orderitem` JOIN`order` ON `orderitem`.orderid=`order`.orderid JOIN `menu` ON `orderitem`.pid=menu.menuid JOIN USER ON order.userid=user.lid JOIN `details` ON `order`.orderid=`details`.oid WHERE menu.rid=%s AND order.status='payed' GROUP BY order.orderid "
    res=selectall2(qry,session['lid'])
    return render_template("RESTAURANT/trackorder.html",val=res)


@app.route('/allocate')
def allocate():
    id=request.args.get('id')
    session['oid']=id
    qry="SELECT * FROM delivery where rid=%s"
    res=selectall2(qry,session['lid'])
    return render_template("RESTAURANT/allocate.html",val=res)


@app.route('/allocates',methods=['get','post'])
def allocates():
    select=request.form['select']
    qry="insert into assign values(null,%s,%s,'pending',curdate())"
    val=(select,session['oid'])
    iud(qry,val)
    return '''<script>alert("success");window.location="/trackorder"</script>'''
@app.route('/viewdeliveryupdates')
def viewdeliveryupdates():
    qry="SELECT * ,`orderitem`.date AS dt,assign.status AS st FROM `orderitem` JOIN`order` ON `orderitem`.orderid=`order`.orderid JOIN `menu` ON `orderitem`.pid=menu.menuid JOIN USER ON order.userid=user.lid JOIN `details` ON `order`.orderid=`details`.oid JOIN assign ON `order`.orderid=`assign`.oid JOIN `delivery` ON `assign`.lid=`delivery`.lid WHERE `menu`.rid=%s  GROUP BY order.orderid "
    res=selectall2(qry,session['lid'])
    return render_template("RESTAURANT/viewdeliveryupdates.html",val=res)



@app.route('/vieworderandupdatestatus')
def vieworderandupdatestatus():
    qry="SELECT * ,`orderitem`.date AS dt FROM `orderitem` JOIN`order` ON `orderitem`.orderid=`order`.orderid JOIN `menu` ON `orderitem`.pid=menu.menuid JOIN USER ON order.userid=user.lid JOIN `details` ON `order`.orderid=`details`.oid WHERE menu.rid=%s AND order.status='pending'OR order.status='ordered' GROUP BY order.orderid "
    res=selectall2(qry,session['lid'])
    return render_template("RESTAURANT/vieworderandupdatestatus.html",val=res)


@app.route('/rejectorder', methods=['post','get'])
def rejectorder():
    id=request.args.get('id')
    qry="UPDATE `order` SET status='Rejected' WHERE orderid=%s"
    iud(qry,id)
    return '''<script>alert("Rejected");window.location="/vieworderandupdatestatus"</script>'''


@app.route('/acceptorder', methods=['post', 'get'])
def acceptorder():
    id = request.args.get('id')
    qry = "UPDATE `order` SET status='Accepted' WHERE orderid=%s"
    iud(qry, id)
    return '''<script>alert("Accepted");window.location="/vieworderandupdatestatus"</script>'''



# @app.route('/trackorderr')
# def trackorderr():
#     return render_template("TRAIN SERVICE MANAGEMENT/trackorderr.html")



@app.route('/adddl')
def adddl():
    return render_template("RESTAURANT/adddl.html")
#
#
@app.route('/mngedl')
def mngedl():
    qry="select * from delivery where rid=%s"
    res=selectall2(qry,session['lid'])
    return render_template("RESTAURANT/mngedl.html",val=res)

@app.route('/deletemem',methods=['get','post'])

def deletemem():
    id=request.args.get('id')
    qry="delete from delivery where lid=%s"
    iud(qry,id)
    qr="delete from login where lid=%s"
    iud(qr,id)
    return '''<script>alert("deleted");window.location="mngedl#about"</script>'''


@app.route('/addmem',methods=['post'])

def addmem():
    fname = request.form['textfield']

    place = request.form['textfield3']
    post = request.form['textfield4']
    pin = request.form['textfield5']
    phone = request.form['textfield6']
    email = request.form['textfield7']
    username = request.form['textfield8']
    password = request.form['textfield9']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'delivery')"
    val=(username,password)
    id=iud(qry,val)
    qr="INSERT INTO `delivery` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    va=(fname,place,post,pin,phone,email,str(id),session['lid'])
    iud(qr,va)
    return '''<script>alert("success");window.location="mngedl#about"</script>'''




@app.route('/editmember',methods=['get','post'])

def editmember():
    id=request.args.get('id')
    session['mid']=id
    qry="select * from delivery where lid=%s"
    res=selectone(qry,id)
    return render_template("RESTAURANT/edit.html",val=res)



@app.route('/editmemb',methods=['post'])

def editmemb():

    lname = request.form['textfield2']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pin = request.form['textfield5']
    phone = request.form['textfield6']
    email = request.form['textfield7']
    qr="UPDATE `delivery` SET `name`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email`=%s WHERE `lid`=%s"
    va=(lname,place,post,pin,phone,email,session['mid'])
    iud(qr,va)
    return '''<script>alert("success");window.location="mngedl#about"</script>'''


@app.route('/vieworderandupdate')
def vieworderandupdate():
    return render_template("TRAIN SERVICE MANAGEMENT/vieworderandupdate.html")



@app.route('/logincode',methods=['post'])
def logincode():
    un=request.form['textfield2']
    ps=request.form['textfield']
    q="select * from login where username=%s and password=%s"
    v=(un,ps)
    r=selectone(q,v)
    if r is None:
        return '''<script>alert("invalid");window.location='/'</script>'''
    elif r['type']=="admin":
        return redirect('/adminhome')
    elif r['type']=="restaurant":
        session['lid']=r['lid']
        return redirect('/restauranthome')
    elif r['type']=="train service":
        return redirect('/trainservicehome')
    else:
        return '''<script>alert("invalid");window.location='/'</script>'''





@app.route('/reg',methods=['post'])

def reg():
    fname = request.form['textfield']

    place = request.form['textfield2']
    post = request.form['textfield89']
    pin = request.form['textfield90']
    lati = request.form['textfield3']
    longi = request.form['textfield4']
    phone = request.form['textfield5']
    email = request.form['textfield6']
    photo = request.files['file']
    ff = secure_filename(photo.filename)
    photo.save(os.path.join('static/image', ff))
    username = request.form['textfield8']
    password = request.form['textfield9']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'pending')"
    val=(username,password)
    id=iud(qry,val)
    qr="INSERT INTO `restaurant` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    va=(fname,place,post,pin,lati,longi,phone,email,ff,str(id))
    iud(qr,va)
    return '''<script>alert("success");window.location="/"</script>'''









app.run(debug=True)





