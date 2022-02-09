from sanic import Sanic, Blueprint
from sanic.config import Config
from contactsapi.config import MyConfig
from contextvars import ContextVar

from contactsapi.controllers.contact import (
    ContactView, ContactsView, ContactSkillsView, ContactSkillView
)
from contactsapi.controllers.skill import SkillView, SkillsView
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker

_base_model_session_ctx = ContextVar("session")


def connect_db(app: Sanic):
    db_config = app.config.DB
    bind = create_async_engine(
        f"mysql+aiomysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}",
        echo=True  # noqa
    )

    @app.middleware("request")
    async def inject_session(request):
        request.ctx.session = sessionmaker(bind, AsyncSession,
                                           expire_on_commit=False)()
        request.ctx.session_ctx_token = _base_model_session_ctx.set(
            request.ctx.session)

    @app.middleware("response")
    async def close_session(request, response):
        if hasattr(request.ctx, "session_ctx_token"):
            _base_model_session_ctx.reset(request.ctx.session_ctx_token)
            await request.ctx.session.close()


def create_app(config: Config = None) -> Sanic:
    app_config = config if config else MyConfig()
    app = Sanic("ContactsAPI", config=app_config)

    connect_db(app)

    bp_contacts = Blueprint('contacts', url_prefix="/api")
    app.blueprint(bp_contacts)
    bp_contacts.add_route(ContactsView.as_view(), "/contacts")
    bp_contacts.add_route(ContactView.as_view(), "/contacts/<contact_id:int>")

    bp_skills = Blueprint('skills', url_prefix="/api")
    app.blueprint(bp_skills)
    bp_skills.add_route(SkillsView.as_view(), "/skills")
    bp_skills.add_route(SkillView.as_view(), "/skills/<skill_id:int>")

    bp_contacts.add_route(
        ContactSkillsView.as_view(), "/contacts/<contact_id:int>/skills"
    )
    bp_contacts.add_route(
        ContactSkillView.as_view(),
        "/contacts/<contact_id:int>/skills/<skill_id:int>",
    )
    

    return app
