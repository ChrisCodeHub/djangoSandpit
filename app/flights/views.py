from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Flight              # Assuming you have a Flight model
from django.core.exceptions import ValidationError


# Create your views here.

# simple function views
def index(request):
    return render(request, 'index.html')



from .models import AboutInfo  # Step 1: Import the model

# About view
def about(request):
    # Step 2: Query the model
    about_info = AboutInfo.objects.all()  # Get all entries from the AboutInfo model

    # Step 3: Pass data to the template
    return render(request, 'about.html', {'about_info': about_info})



# debug view - teh aim of this is to just dump out some key/values to see what is happening
def debug(request):
    
    # create a nice list of dictionaries... aka some json
    debugInfo = [             
            {
                "title": "number 1",
                "description": "its a 1!"
            },
            {
                "title": "number 2",
                "description": "Its a 2"
            }
    ]

    return render(request, 'debug.html', {'debug_info': debugInfo})

# the below view is designed to allow a user to __add__ a new flight to teh database with a POST
# and __retrieve__ the information about a flight with a GET
# added the CSRF (Cross-Site Request Forgery)   decorator to keep life simple
# CSRF exempt for simplicity in testing POST requests with JSON (not recommended for production without proper CSRF tokens)
@csrf_exempt
def flightInfo(request):
    if request.method == 'GET':
        # Step 1: Handle GET request - Display flight info (assuming simple template rendering)
        return JsonResponse({"message": "GET World"})
        pass
    elif request.method == 'POST':
        # Step 2: Handle POST request - Accept JSON data and create a new flight row
        try:
            # Parse the JSON data from the request
            return JsonResponse({"message": "POST  World"})

            # Extract fields from the JSON data, adjust field names as per your Flight model

            # Validate that the required fields are provided
            
            # Create a new flight entry
        
            return JsonResponse({'success': 'Flight created', 'flight_id': flight.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Something went wrong'}, status=500)

    # If the request method is neither GET nor POST
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

    
