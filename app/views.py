from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timezone  # To get the current datetime
from rest_framework.status import HTTP_200_OK

@api_view(['GET'])
def home(request):
    # Prepare the desired output
    data = {
        "email": "rhexmilia06@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "github_url": "https://github.com/RexDavid06/HNG-stage-0Task"
    }

    # Return the response with the data
    return Response(data, status=HTTP_200_OK)
