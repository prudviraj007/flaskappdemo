# gamesyschallenge
gamesyschallenge

# Install
    
    Flask app is packaged and you can use pip to install it:

  ```pip install flask_csv```
  
 # How to use ?
 
 
 Flask-CSV has a simple hepler method named send_csv which allows you to send csv files in flask endpoints. It takes an iterable of dict, a filename and a list of fields. The keys of all dict in the iterable must correspond to given fields.

It will return a Response object with filename set and body containing the CSV data.

You will better understand with a short example.
