from cloudapi import BaseRESTAPI
import os


class DigitalOceanAPIConnection(BaseRESTAPI):
    def __init__(self):
        BaseRESTAPI.__init__(
            self,
            baseurl="https://api.digitalocean.com",
            callrateperhour=5000,
            # geometric_delay_multiplier=2,
            # maximum_geometric_delay_multiplications=6,
            # maximum_failed_attempts=3,
            geometric_delay_multiplier=1,
            maximum_geometric_delay_multiplications=1,
            maximum_failed_attempts=1,
        )
        if "DIGITALOCEAN_ACCESS_TOKEN" in os.environ:
            # print("Token found...")
            self.token = os.getenv("DIGITALOCEAN_ACCESS_TOKEN", "")
        else:
            raise Exception('"DIGITALOCEAN_ACCESS_TOKEN" ENV Variable not set.')
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token} ",
        }
