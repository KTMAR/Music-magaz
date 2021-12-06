from django.urls import path

from .views import \
    AlbumDetailView, \
    RegistrationView, \
    LoginView, \
    BaseView, \
    CartView, \
    AddToCartView, \
    AccountView


from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    # path('<str:artist_slug>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('<str:artist_slug>/<str:album_slug>/', AlbumDetailView.as_view(), name='album_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:artist_slug>/<str:album_slug>/', AddToCartView.as_view(), name='add_to_cart'),


]
