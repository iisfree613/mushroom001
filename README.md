## Mushroom 订单管理系统
---

### 环境
* 开发语言：Python 3.8

* web框架：Django 3.1

### 项目文件结构：

``` py

.
├── __pycache__
│   └── manage.cpython-38.pyc
├── manage.py
├── mushroom001
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── orders
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20201223_1726.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       ├── 0002_auto_20201223_1726.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── templates
│   │   ├── add_cart.html
│   │   ├── cart.html
│   │   └── prod.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── bootstrap4
│   │   ├── css
│   │   │   ├── bootstrap-grid.css
│   │   │   ├── bootstrap-grid.css.map
│   │   │   ├── bootstrap-grid.min.css
│   │   │   ├── bootstrap-grid.min.css.map
│   │   │   ├── bootstrap-reboot.css
│   │   │   ├── bootstrap-reboot.css.map
│   │   │   ├── bootstrap-reboot.min.css
│   │   │   ├── bootstrap-reboot.min.css.map
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   └── bootstrap.min.css.map
│   │   └── js
│   │       ├── bootstrap.bundle.js
│   │       ├── bootstrap.bundle.js.map
│   │       ├── bootstrap.bundle.min.js
│   │       ├── bootstrap.bundle.min.js.map
│   │       ├── bootstrap.js
│   │       ├── bootstrap.js.map
│   │       ├── bootstrap.min.js
│   │       └── bootstrap.min.js.map
│   └── js
│       └── prod.js
├── templates
│   ├── base.html
│   └── index.html
└── users
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── admin.cpython-38.pyc
    │   ├── apps.cpython-38.pyc
    │   ├── forms.cpython-38.pyc
    │   ├── models.cpython-38.pyc
    │   ├── urls.cpython-38.pyc
    │   └── views.cpython-38.pyc
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_auto_20201223_1625.py
    │   ├── 0003_auto_20201223_1633.py
    │   ├── 0004_auto_20201223_1635.py
    │   ├── 0005_auto_20201224_1716.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-38.pyc
    │       ├── 0002_auto_20201223_1625.cpython-38.pyc
    │       ├── 0003_auto_20201223_1633.cpython-38.pyc
    │       ├── 0004_auto_20201223_1635.cpython-38.pyc
    │       ├── 0005_auto_20201224_1716.cpython-38.pyc
    │       └── __init__.cpython-38.pyc
    ├── models.py
    ├── templates
    │   ├── login.html
    │   └── signup.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

### 主目录

* mushroom001
  * 放置配置文件

### 应用目录：

* orders(订单管理)
* users（用户管理）

### 静态文件目录：

* templates:html文件
* static:





