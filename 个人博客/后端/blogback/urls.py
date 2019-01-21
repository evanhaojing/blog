from django.urls import path

from blogback import views

urlpatterns = [
    # 主页
    path('index/', views.index, name='index'),
    # 富文本，撰写新文章
    path('add_article/', views.add_article, name='add_article'),
    # 增加友情链接
    path('add_flink/', views.add_flink, name='add_flink'),
    # 撰写新公告
    path('add_notice/', views.add_notice, name='add_notice'),
    # 文章管理
    path('article/', views.article, name='article'),

    # 评论栏
    path('comment/', views.comment, name='comment'),
    # 友情链接等其他操作
    path('flink/', views.flink, name='flink'),
    # 登陆页面
    path('login/', views.login, name='login'),
    # 用户登陆使用记录
    path('loginlog/', views.loginlog, name='loginlog'),
    # 用户管理
    path('manage_user/', views.manage_user, name='manage_user'),
    # 公告操作
    path('notice/', views.notice, name='notice'),
    # 用户设置
    path('readset/', views.readset, name='readset'),
    # 常规设置
    path('setting/', views.setting, name='setting'),
    # 文章修改
    path('update_article/<int:id>', views.update_article, name='update_article'),
    # 栏目修改
    path('update_category/<int:id>', views.update_category, name='update_category'),
    # 修改友情链接
    path('update_flink/', views.update_flink, name='update_flink'),
    # 注册
    path('register/', views.register, name='register'),
    # 退出登录
    path('logout/', views.logout, name='logout'),
    # 增加新栏目
    path('add_category/', views.add_category, name='category'),
    # 删除栏目
    path('del_category/<int:id>', views.del_category, name='del_category'),
    # 删除文章
    path('del_article/<int:id>', views.del_article, name='del_article'),

    path('', views.index),
]
