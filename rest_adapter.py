import requests
import requests.packages
from typing import List, Dict
from aotapi.exceptions import AotApiException
from json import JSONDecodeError
from aotapi.models import Result
import logging

class RestAdapter:
    def __init__(self, hostname: 'api-attack-on-titan.herokuapp.com', ver: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Constructor for RestAdapter
        :param hostname: Normally, https://api-attack-on-titan.herokuapp.com/
        :param ver: always v1
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        """
        self._logger = logger or logging.getLogger(__name__)
        self.url = "https://{}/api/{}/".format(hostname, ver)
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str) -> Result:
        full_url = self.url + endpoint
        log_line_pre = f"method={http_method}, url={full_url}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise AotApiException("Request failed") from e
        # Deserialize JSON output to Python object, or return failed Result on exception
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise AotApiException("Bad JSON in response") from e
        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200  # 200 to 299 is OK
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            self._logger.debug(msg=log_line)
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=log_line)
        raise AotApiException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str) -> Result:
        return self._do(http_method='GET', endpoint=endpoint)

