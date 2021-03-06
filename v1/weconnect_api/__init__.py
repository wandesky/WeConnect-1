from v1 import api, app
from .reviews_api import Review, reviews
from .business_api import Business, BusinessList, businesses
from .users_api import UserRegister, UserLogin, UserLogout, UserResetPassword


"""Business Endpoints"""
api.add_resource(Business, '/businesses/<int:businessId>', endpoint="business")
api.add_resource(BusinessList, '/businesses', endpoint="businesses")



"""Reviews Endpoints"""
api.add_resource(Review, '/businesses/<int:businessId>/reviews', endpoint="reviews")



"""Users Endpoints"""
api.add_resource(UserRegister, '/auth/register', endpoint="Register")
api.add_resource(UserLogin, '/auth/login', endpoint="Login")
api.add_resource(UserLogout, '/auth/logout', endpoint="Logout" )
api.add_resource(UserResetPassword, '/auth/reset-password', endpoint="Reset-password")



