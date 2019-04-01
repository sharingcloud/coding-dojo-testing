"""API tests."""

import json

from django.http import JsonResponse
from django.test import RequestFactory
from django.urls import reverse


def test_api_clickme(ex_profile_factory, rf: RequestFactory):
    # Test 'clickme' API using a RequestFactory.
    from testme.api import clickme

    # Create a user and a profile with no clicks
    profile_0 = ex_profile_factory("test", 0)
    # Prepare a call to the api-clickme endpoint
    request = rf.post(reverse("api-clickme"))
    # Store the user in the request
    request.user = profile_0.user
    # Call the endpoint
    response = clickme(request)

    # Should be a JsonResponse
    assert isinstance(response, JsonResponse)
    # Should return initial clicks number plus one
    data = json.loads(response.content)
    assert data["clicks"] == 1


# TODO: Create the test
def test_api_addme(rf: RequestFactory):
    # Test 'addme' API using a RequestFactory.
    from testme.api import addme

    # Prepare a call to the api-addme endpoint with POST data
    # Call the endpoint

    # Response should be a JsonResponse
    # It should return the sum of two numbers
    assert False


# TODO: Create the test
def test_api_base64me(rf: RequestFactory):
    # Test 'base64me' API using a RequestFactory.
    from testme.api import base64me

    # Prepare a call to the api-base64me endpoint with POST data
    # Call the endpoint

    # Response should be a JsonResponse
    # It should return the base64 encoding of a source string
    assert False
