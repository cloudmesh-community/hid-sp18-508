# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cpu_get**](DefaultApi.md#cpu_get) | **GET** /cpu | 


# **cpu_get**
> CPU cpu_get()



Returns cpu information of the hosting server

### Example 
```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.cpu_get()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->cpu_get: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CPU**](CPU.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

