# -*- coding: utf-8 -*-
import sys
from aliyunsdkcore.client import AcsClient
from aliyunsdkedas.request.v20170801 import QueryApplicationStatusRequest
from aliyunsdkedas.request.v20170801 import AuthorizeApplicationRequest
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT


try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass
except Exception as err:
    raise err


REGION = "ap-southeast-1"
PRODUCT_NAME = "Edas"
ENDPOINT = "edas.ap-southeast-1.aliyuncs.com"


ACCESS_KEY_ID = <Update Access Key ID>
ACCESS_KEY_SECRET = <Update Access Key Secret>
region_provider.add_endpoint(PRODUCT_NAME, REGION, ENDPOINT)
acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)


def query_application():
    qappreq = QueryApplicationStatusRequest.QueryApplicationStatusRequest()
    qappreq.set_AppId('b5e5097a-f01c-4cef-a3dc-549275d9ffcb')
    qappresponse = acs_client.do_action_with_exception(qappreq)
    return qappresponse

if __name__ == '__main__':
    print(query_application())