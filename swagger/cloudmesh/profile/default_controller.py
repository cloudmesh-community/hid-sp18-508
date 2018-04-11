import connexion
import six
from profile_controller import *
from swagger_server.models.profile import PROFILE  # noqa: E501
from swagger_server import util


def get_profile_by_uuid(uuid):
    """get_profile_by_uuid
    Returns a general description of a user  # noqa: E501
    :param uuid: uuid of user
    :type id: str
    :rtype: PROFILE
    """
    item = get_profile_by_uuid_mongo(uuid)
    return PROFILE(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
def profiles_get():  # noqa: E501
    """profiles_get

    Returns a list of general description of users  # noqa: E501

    :rtype: List[PROFILE]
    """
    listOfProfile = []
    items = get_profile()
    for each in items:
        listOfProfile.append(PROFILE(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]))
    return listOfProfile
