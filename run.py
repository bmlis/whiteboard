from whiteboard.app import create_app, ApplicationContext

context = ApplicationContext()
application = create_app(context)


if __name__ == '__main__':
    application.run('0.0.0.0')
