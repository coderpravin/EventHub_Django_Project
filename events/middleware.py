import logging
import time
logger = logging.getLogger(__name__)

#print(__name__)
class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

       # ============================================================
       # TEST APPROACH:  #Before Log Executed

       # logger.info("Request Received: %s %s",request.method, request.path)
       # ============================================================
     
        start_time = time.time()
       
        response = self.get_response(request)

        duration = time.time() - start_time
        #After Log Executed
        logger.info(f"Request Received {request.method}, {request.path} - Status Code {response.status_code} - Time {duration:.2f}s" )

        return response