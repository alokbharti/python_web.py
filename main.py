from webpy import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

web.config.debug == True


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'


if __name__ == "__main__":
    app.run()
