from django.urls import path
from .views import index, make_login, make_logout, registration, balance, add_hotel_admin, admin, delete_hotel_admin,\
    all_users, users_static, hotel_info, search_hotel_booking, add_booking, pay_room, del_booking, booking_info

urlpatterns = [
    # VIEW
    path('index', index, name="index"),
    path('login', make_login, name="login"),
    path('logout', make_logout, name="logout"),
    path('signup', registration, name="signup"),
    path('balance', balance, name="balance"),
    path('search', search_hotel_booking, name="search"),
    path('add_booking', add_booking, name="add_booking"),
    path('booking_info/<str:booking_uid>', booking_info, name="booking_info"),
    path('pay_room', pay_room, name="pay_room"),
    path('del_booking', del_booking, name="del_booking"),
    path('add-hotel', add_hotel_admin, name="add_hotel"),
    path('hotel_info/<str:hotel_uid>', hotel_info, name="hotel_info"),
    path('admin', admin, name="admin"),
    path('delete-hotel', delete_hotel_admin, name="delete_hotel"),
    path('all-users', all_users, name="all_users"),
    path('users-static', users_static, name="users_static"),
]
