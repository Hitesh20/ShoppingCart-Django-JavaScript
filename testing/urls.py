from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView
urlpatterns = [
    path("", views.index, name="TestHome"),
    path("createProd/", views.product_create_view, name="createProduct"),
    path("createProd2/", views.product_create_view_two, name="createProduct2"),
    path("createProd3/", views.product_create_view_three, name="createProduct3"),
    path("render_initial_data/", views.render_initial_data, name="render_initial_data"),
    path("product/<int:prod_id>/", views.dynamic_lookup_view, name="prodDetail"),
    path("product/<int:prod_id>/delete", views.delete_product, name="deleteProduct"),
    path("product_list_view/", views.product_list_view, name="product_list_view"),
    path("article_list_view/", ArticleListView.as_view() , name="article_list_view"),
    path("article_detail_view/<int:id>", ArticleDetailView.as_view() , name="article_detail_view"),
    path("article_create_view", ArticleCreateView.as_view() , name="article_create_view"),

]