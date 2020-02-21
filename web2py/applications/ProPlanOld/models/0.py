from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'ProPlan'
settings.subtitle = 'fatto da SAMT'
settings.author = 'Jure Grgic, Jonathan Mueller, Filippo Zinetti, Kushtrim Rushi'
settings.author_email = 'jure.grgic@samtrevano.com'
settings.keywords = 'project, management, plan'
settings.description = 'ProPlan is a website to manage your projects'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'a4eb8de3-c452-4a83-961d-76afa64cd5af'
settings.email_server = 'localhost'
settings.email_sender = 'jure.grgic@samtrevano.ch'
settings.email_login = None
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
