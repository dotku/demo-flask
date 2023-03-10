# Demo Flask

This is a demo project based on Flask 2.2.x Tutorial.

## Live

![image](https://user-images.githubusercontent.com/1519232/221347020-0ba00ea4-ff0b-4346-acac-fb5d2e1f8ad2.png)

[https://dotku.pythonanywhere.com/](https://dotku.pythonanywhere.com/)

> :warning: Due to pythonanywhere free account limitation, the live will be disabled on Thursday 25 May 2023; ping me if you want to check out the live again, I can reactivete the site. Or maybe fund me by $5/mo so I can keep the demo site longer?

## Throubleshooting on PythonAnyWhere hosting

### TypeError: 'module' object is not callable

Make sure you run `pip install requirement.txt` to install all neccessary packages.

### ModuleNotFoundError: No module named 'flaskr'

You might need install the app by following this article: [https://flask.palletsprojects.com/en/2.2.x/tutorial/install/](https://flask.palletsprojects.com/en/2.2.x/tutorial/install/)

### ImportError: cannot import name 'app' from 'flaskr' (/home/dotku/mysite/demo-flask/flaskr/__init__.py)

Should export as `create_app` instead of `app`.

### TypeError: create_app() takes from 0 to 1 positional arguments but 2 were given

change the line from

```py
from project import create_app as application
```

to

```py
from project import create_app
application = create_app()
```

## Reference

[https://flask.palletsprojects.com/en/2.2.x/tutorial/](https://flask.palletsprojects.com/en/2.2.x/tutorial/)
