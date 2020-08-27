from flask import Flask
import pandas as pd



app = Flask(__name__)



@app.route("/totalwin/<int:userid>")
def win_total(userid):
    df = pd.read_csv("C:\\Users\\admin\\Downloads\\DB_Setup\\Revenue_Analysis_Test_Data.csv")
    df_total=df.groupby(['MEMBER_ID'])['WIN_AMOUNT'].sum().to_dict()
    return str(df_total[userid])
@app.route("/totalwin/<int:userid>/<int:year_month>")
def win_total_month(userid,year_month):
    df = pd.read_csv("C:\\Users\\admin\\Downloads\\DB_Setup\\Revenue_Analysis_Test_Data.csv")
    df_total=df.groupby(['MEMBER_ID','ACTIVITY_YEAR_MONTH'])['WIN_AMOUNT'].sum().to_dict()
    return str(df_total[userid,year_month])
@app.route("/totalwager/<int:userid>")
def wager_total(userid):
    df = pd.read_csv("C:\\Users\\admin\\Downloads\\DB_Setup\\Revenue_Analysis_Test_Data.csv")
    df_total=df.groupby(['MEMBER_ID'])['WAGER_AMOUNT'].sum().to_dict()
    return str(df_total[userid])
@app.route("/totalwager/<int:userid>/<int:year_month>")
def wager_total_month(userid,year_month):
    df = pd.read_csv("C:\\Users\\admin\\Downloads\\DB_Setup\\Revenue_Analysis_Test_Data.csv")
    df_total=df.groupby(['MEMBER_ID','ACTIVITY_YEAR_MONTH'])['WAGER_AMOUNT'].sum().to_dict()
    return str(df_total[userid,year_month]) 
@app.route("/wagercount/<int:userid>")
def wager_count(userid):
    df = pd.read_csv("C:\\Users\\admin\\Downloads\\DB_Setup\\Revenue_Analysis_Test_Data.csv")
    df_total=df.groupby(['MEMBER_ID'])['NUMBER_OF_WAGERS'].count().to_dict()  
    return str(df_total[userid])
@app.route("/wagercount/<int:userid>/<int:year_month>")
def wager_count_month(userid,year_month):
    df = pd.read_csv("C:\\Users\\admin\\Downloads\\DB_Setup\\Revenue_Analysis_Test_Data.csv")
    df_total=df.groupby(['MEMBER_ID','ACTIVITY_YEAR_MONTH'])['NUMBER_OF_WAGERS'].count().to_dict()  
    return str(df_total[userid,year_month])


  
if __name__ == '__main__':
    app.run(debug=True) #go to http://localhost:5000/ to view the page.