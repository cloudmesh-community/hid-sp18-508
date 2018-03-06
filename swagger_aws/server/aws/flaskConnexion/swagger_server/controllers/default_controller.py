import connexion
import six

from swagger_server.models.empty import Empty  # noqa: E501
from swagger_server import util


def root_get():  # noqa: E501
    """root_get

     # noqa: E501


    :rtype: Empty
    """
    return 'do some magic!'
