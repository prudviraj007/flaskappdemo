# gamesyschallenge
gamesyschallenge

# Install
    
    Flask app is packaged and you can use pip to install it:

  ```pip install flask_csv```
  
 # How to use ?
 
 
 The Flask app directly reads the csv data from the source directory and It will return a response object with the calculated values
 For example with the user id 1001 :
 
 ```
 @app.route("/totalwin/<int:userid>")
def win_total(userid):
    df = pd.read_csv("C:\\Users\\admin\\Downloads\\DB_Setup\\Revenue_Analysis_Test_Data.csv")
    df_total=df.groupby(['MEMBER_ID'])['WIN_AMOUNT'].sum().to_dict()
    return str(df_total[userid])
 ```

 
 Hitting this end point will return the total win amount :
 
  ```
 30.799999999999997
 ```
 
 # Passing additionnal parameters
 
 To get total win amount for a specific userid, the following endpoint should be used :
 
```
 <host>:5000/userid/totalwin
 ```
 To get total wager amount for a specific userid, the following endpoint should be used :
 
 ```
 <host>:5000/userid/totalwager
 ```   
 
 To get total number of wagers for a specific userid, the following endpoint should be used :
 
 ```
 <host>:5000/userid/wagercount
 ```
 To calculate the above totals for a specific userid by a specific month, the following endpoint should be used :  
 
 ```
 <host>:5000/userid/<total_param>/<year_month>
 ```
 
 For example :
 
 ```
 localhost:5000/1001/totalwin/201701
 ```
 
 hitting the above URL gives the result :
 
 ```
 14.1
 ```
 
