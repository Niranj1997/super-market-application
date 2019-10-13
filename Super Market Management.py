from flask import Flask,render_template,request
import smtplib
app = Flask(__name__)                                 #InitiateFlask
app.config['TEMPLATES_AUTO_RELOAD'] = True
battery = 0                                           #InitialStatusOfItems,Income,Netamount
earbuds = 0
giftarticles = 0
groundnut = 0
mug = 0
oil = 0
paste = 0
rice = 0
soap = 0
toiletcleaner=0
netamount=0
amount=0
new=0
income=0
f = open('templates/Print.html','w')
@app.route('/')                                       #WelcomeScreen
def Welcome():        
    return render_template('Welcome.html')
@app.route('/Admin')                                   #AdminPage
def Admin():          
    return render_template('Admin.html')
@app.route('/Admin/ViewStock')                         #ViewStocks
def ViewStock():
    stock = open('templates/Stock.html','w')
    txt= "<html><body><center><h1>ABC Super Market</h1><br><h2>View Stocks Left</h2><br>Battery      : "+str(battery)+"<br> Ear Buds : "+str(earbuds)+"<br> Gift Articles  : "+str(giftarticles)+"<br> Ground Nut : "+str(groundnut)+"<br> Mug : "+str(mug)+"<br> Oil : "+str(oil)+"<br> Paste : "+str(paste)+"<br> Rice: "+str(rice)+"<br> Soap: "+str(soap)+"<br> Toilet Cleaner : "+str(toiletcleaner)+"<br></center></body></html>"
    stock.write(txt)
    stock.close()
    return render_template('Stock.html')
@app.route('/Admin/AddStock')                          #AddStocks
def AddStock():
    return render_template('AddStock.html')
@app.route('/Add')
def Add():
    if 'item' in request.args:
        name=request.args['item']
    if 'qty' in request.args:
        qty=request.args['qty']
    addStock(name,qty)
    return "Successfully Added to Stocks"
def addStock(name,qty):                                #AddStockFunction
    global battery,earbuds,giftarticles,groundnut,mug,oil,paste,rice,soap,toiletcleaner
    if name=='battery':
        battery+=int(qty)
    elif name=='earbuds':
        earbuds+=int(qty)
    elif name=='giftarticles':
        giftarticles+=int(qty)
    elif name=='groundnut':
        groundnut+=int(qty)
    elif name=='mug':
        mug+=int(qty)
    elif name=='oil':
        oil+=int(qty)
    elif name=='paste':
        paste+=int(qty)
    elif name=='rice':
        rice+=int(qty)
    elif name=='soap':
        soap+=int(qty)
    elif name=='toiletcleaner':
        toiletcleaner+=int(qty)
@app.route('/Admin/Purchase')                          #AdminPurchase
def Purchase():       
    return render_template('Purchase.html')            
@app.route('/Purchase')                                #AdminPurchaseMail
def order():           
    if 'item' in request.args:
        name=request.args['item']
    if 'qty' in request.args:
        qty=request.args['qty']
    sendSms(name,qty)
    return "Successfully Ordered"
def sendSms(name,qty):                                 #AdminPurchaseMailSMTPfunction
    text = "Please take this order. Item Name - "+name+". Quantity- "+qty
    sender='niranjandeveloper97@gmail.com'
    receivers=['niranj1997@gmail.com']
    password='testingaccount'
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers,text)
        smtpObj.quit()
    except smtplib.SMTPException:
        print ("error")
@app.route('/Income')                                   #ShowsIncome
def incom():
    global inc,income
    inc=open('templates/Income.html','w')
    t="<html><body><br><center><h1>ABC Super Market</h1></center><center><h1>Income Recieved is as follows.</h1><center><br><center><h2>Rs."+str(income)+"</h2></center></body></html>"
    inc.write(t)
    inc.close()
    return render_template('Income.html')
@app.route('/Biller')                                   #BillerPage
def Biller():
    global f,netamount
    netamount=0
    f = open('templates/Print.html','w')
    f.write('<center><h1>ABC Super Market</h1></center><br><center><h2>Invoice</h2></center><br><center><button type="button"><a href="/Biller">Finish</a></button></center><br><br>')
    f.write("<center><p>ItemName----Cost----Qty----Amount----Total_Amount</p></center>")
    return render_template('Biller.html')
@app.route('/Biller/AddItems')                          #AddItemsOptionForBiller
def additem():
    return render_template('AddItem.html')
@app.route('/AddToCart')
def addtocart():
    if 'item' in request.args:
        item=request.args['item']
    if 'cost' in request.args:
        cost=request.args['cost']
    if 'qty' in request.args:
        qty=request.args['qty']
    global f,amount,netamount
    int(amount)
    amount=int(cost)*int(qty)
    netamount+=amount
    message="<center><p>"+item+"---Rs."+cost+"--"+qty+"Nos.---Rs."+str(amount)+"--Total_Amount--Rs."+str(netamount)+"</p></center>"
    f.write(message)
    updatestock(item,qty)
    return render_template('AddItem.html')
def updatestock(name,qty):                               #UpdatesTheStockListAfterAddingItemsToBill
    global battery,earbuds,giftarticles,groundnut,mug,oil,paste,rice,soap,toiletcleaner
    if name=='battery':
        battery-=int(qty)
    elif name=='earbuds':
        earbuds-=int(qty)
    elif name=='giftarticles':
        giftarticles-=int(qty)
    elif name=='groundnut':
        groundnut-=int(qty)
    elif name=='mug':
        mug-=int(qty)
    elif name=='oil':
        oil-=int(qty)
    elif name=='paste':
        paste-=int(qty)
    elif name=='rice':
        rice-=int(qty)
    elif name=='soap':
        soap-=int(qty)
    elif name=='toiletcleaner':
        toiletcleaner-=int(qty)
    else:
        new+int(qty)
@app.route('/Biller/PrintBill')                           #PrintsTheBill
def print():
    global f,income,netamount
    int(netamount)
    income+=netamount
    f.close()
    return render_template('Print.html')

if __name__ =="__main__":
    app.run(debug=True, port=33507)                        #app.run(host='0.0.0.0',threaded=True)
           
            
