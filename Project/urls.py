import home_app

home_app.home.add_url_rule(rule = '/', view_func = home_app.render_home, methods = ['GET', 'POST'])

