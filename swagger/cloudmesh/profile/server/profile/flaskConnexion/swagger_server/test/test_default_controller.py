# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.profile import PROFILE  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_profile_mongo(self):
        """Test case for add_profile_mongo

        
        """
        response = self.client.open(
            '/cloudmesh/profile/addprofiles/{uuid}/{username}/{context}/{description}/{firstname}/{lastname}/{publickey}/{email}'.format(uuid='uuid_example', username='username_example', context='context_example', description='description_example', firstname='firstname_example', lastname='lastname_example', publickey='publickey_example', email='email_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_profile_by_uuid(self):
        """Test case for get_profile_by_uuid

        
        """
        response = self.client.open(
            '/cloudmesh/profile/profiles/{uuid}'.format(uuid='uuid_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_profiles_get(self):
        """Test case for profiles_get

        
        """
        response = self.client.open(
            '/cloudmesh/profile/profiles',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
