# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import webbrowser
import requests
def display_ip():
    """  Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})
    return [geo_data['latitude'],geo_data['longitude']]

if __name__ == '__main__':
    a=display_ip()
url=(f"https://www.google.com/maps/search/?api=1&query={str(a[0])},{str(a[1])}")
print(f"{url}")
webbrowser.open(url)
# your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = '#'
auth_token = '#'
client = Client(account_sid, auth_token)

message = client.messages 
                .create(
                     body=f"{url}",
                     from_='+14012576091',
                     to='+91#'
                 )
account_sid = '#' 
auth_token = '#' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=f"{url}",      
                              to='whatsapp:+91#' 
                          ) 
 
print(message.sid)

print(message.sid)

