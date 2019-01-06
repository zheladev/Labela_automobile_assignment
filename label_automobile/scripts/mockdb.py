import os
import sys
import transaction as ts

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_tm_session,
    get_session_factory,
    User,
    Part
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)
    session_factory = get_session_factory(engine)

    with ts.manager:
        dbsession = get_tm_session(session_factory, ts.manager)
        for i in range(1, 10):
            addUser(dbsession, "John"+str(i), "Doe", "johndoe"+str(i)+"@example.com")
            addPart(dbsession, "Testpiece"+str(i), str(i)+"0394E", "Testpiece"+str(i)+" details")



def addUser(dbsession, name, surname, email):
    user = User()
    user.name = name
    user.surname = surname
    user.email = email
    dbsession.add(user)

def addPart(dbsession, name, vendor_id, details):
    part = Part()
    part.name = name
    part.vendor_id = vendor_id
    part.details = details
    dbsession.add(part)
