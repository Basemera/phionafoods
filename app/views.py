"""
Routes module to handle request urls
"""
from app.controllers.users import user_registration


class Urls:
    """
        Class to generate urls
    """

    @staticmethod
    def generate(app):
        """
        Generate urls
        :param app:
        :return:
        """
        app.add_url_rule('/api/v2/signup/', view_func=user_registration.as_view('register'),
                         methods=['POST'], strict_slashes=False)