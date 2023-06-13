import json
from base64 import b64encode
from hashlib import sha256


class TokenManager:
    login_url = "/api/login"
    login_body = {
        "appSource": 0,  # Unknown
        "lang": 1,  # English
    }
    access_token = None

    def __init__(self, session, host, username, password):
        self.session = session
        self.host = host
        self.login_body["emailId"] = username
        self.login_body["hashedPwd"] = b64encode(
            sha256(password[:12].encode()).digest()
        ).decode()

    def is_token_valid(self):
        # TODO see if we can work out if it's expired?
        return self.access_token is not None

    async def fetch_access_token(self):
        url = self.host + self.login_url
        json_data = json.dumps(self.login_body, indent=4)
        async with self.session.post(url, json=self.login_body) as response:
            response_text = await response.text()
            results = json.loads(response_text)

            login_result = results["contents"]["loginResult"]

            # No matter what this API returns a 200 OK
            # So need to parse the JSON to align with reality
            if login_result == 0:
                self.access_token = results["contents"]["token"]
                # Not sure what the below is for. Perhaps a refresh token?
                self.access_token_pw = results["contents"]["tokenPwd"]
                return True
            else:
                self.error_message = results["contents"]["loginMessage"]
                raise Exception(self.error_message)
