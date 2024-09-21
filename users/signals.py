from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.db import models
from .models import User
from datetime import date,timedelta
from django.core.exceptions import ValidationError
from django.contrib.sessions.models import Session
from django.utils import timezone
# import requests
from django.conf import settings



# def is_admin(user):
#     return user.groups.filter(name='admin').exists()


# @receiver(post_save, sender=User)
# def Create_Manager(sender, instance, created, **kwargs):





# @receiver(user_logged_in)
# def update_login_count(sender, request, user, **kwargs):
#     login_count, created  = Login_Count.objects.get_or_create(id=1)
#     if not is_admin(user):
#     # Increment the login count
#         user.logged_count += 1
#         user.save()  

#         # Deactivate the user if login count exceeds 3
#         if user.logged_count > login_count.log_count:
#             user.access = False
#             user.logged_count = 0
#             user.save()
#             request.session.flush()
#             logout_user_from_all_sessions(user)
    
#     try:
#         # Make a request to an IP geolocation API
#         response = requests.get('https://ipinfo.io/json')
#         data = response.json()
#         print(data)
#         location = data.get('loc').split(',')
#         lat, lng = float(location[0]), float(location[1])
#         user.latitude = lat
#         user.longtitude = lng
#         user.save()
#     except Exception as e:
#         # Handle exceptions (e.g., logging)
#         print(f"Error fetching location: {e}")
   
        

# @receiver(user_logged_out)
# def decrease_login_count(sender, request, user, **kwargs):
#     if not is_admin(user):
#         if user.logged_count > 0:
#             user.logged_count -= 1
#             user.save()






# def logout_user_from_all_sessions(user):
#     sessions = Session.objects.filter(expire_date__gte=timezone.now())
#     for session in sessions:
#         data = session.get_decoded()
#         if str(user.id) == str(data.get('_auth_user_id')):
#             session.delete()


# def get_location_from_coordinates(lat, lng):
#     google_api_key = settings.MAP_KEY # Replace with your actual Google API key
#     geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={google_api_key}"

#     try:
#         # Make a request to Google Maps Geocoding API
#         response = requests.get(geocode_url)
#         data = response.json()

#         if data['status'] == 'OK':
#             # Extract city and state/country information
#             for result in data['results']:
#                 for component in result['address_components']:
#                     if 'locality' in component['types']:
#                         city = component['long_name']
#                     elif 'administrative_area_level_1' in component['types']:
#                         state = component['long_name']
#                     elif 'country' in component['types']:
#                         country = component['long_name']
#                     elif 'postal_code' in component['types']:
#                         postal_code = component['long_name']

#             # Return the location information
#             return {
#                 'city': city,
#                 'state': state if 'state' in locals() else None,
#                 'country': country if 'country' in locals() else None,
#                 'postal_code': postal_code if 'postal_code' in locals() else None
#             }
#         else:
#             return None  # Handle error cases
#     except Exception as e:
#         print(f"Error fetching location: {e}")
#         return None