import random
 
import uuid  # For generating UUIDs
 
from locust import FastHttpUser, task, between
 
from datetime import datetime

class DTLoggingPerformance(FastHttpUser):
 
    # Wait time can be adjusted as needed (0 for high TPS)
 
    wait_time = lambda self: 0
    # Define API key and total endpoints
 
    api_key = "mHAhglqNgPAS86H7QHhFpVTY9lTVoAeW"
 
    total_endpoints = 10
    # File to store the logs
 
    log_file = "locust_requests.log"
    @task
 
    def dt_logging(self):
 
        # Generate a UUID for the Transaction-Id header
 
        #transaction_id = str(uuid.uuid4())
        # Pick a random endpoint index
 
        endpoint_index = random.randint(1, self.total_endpoints)
        # Define custom headers
 
        #headers = {"Transaction-Id": transaction_id}
        # URL requests
 
        urls = [
 
            f"/eis-dt-logging-sample{endpoint_index}",
 
            f"/eis-dt-logging-sample{endpoint_index}?apikey={self.api_key}",
 
            f"/eis-dt-logging-sample{endpoint_index}/ip?apikey={self.api_key}",
 
            f"/eis-dt-logging-sample{endpoint_index}/statusCode/400?apikey={self.api_key}",
 
            f"/eis-dt-logging-sample{endpoint_index}/statusCode/500?apikey={self.api_key}",
 
        ]
        # Log each request to the file
 
        for url in urls:
            transaction_id = str(uuid.uuid4())
            headers = {"transaction-Id": transaction_id}
            self.client.get(url, headers=headers)
            self.log_request(transaction_id, url)
    def log_request(self, transaction_id, url):
 
        """Log request details to a file."""
 
        with open(self.log_file, "a") as log:
 
            # Write the log entry as: Timestamp, Transaction-Id, URL
 
            log.write(f"{datetime.now()}, Transaction-Id: {transaction_id}, URL: {url}\n")
