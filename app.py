#!/usr/bin/env python

from flask import Flask

from pokedex.db import connect
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True


view_func = GraphQLView.as_view('graphql',
                                schema=schema,
                                graphiql=True,
                                session=db_session)
app.add_url_rule('/graphql',
                 view_func=view_func)


if __name__ == '__main__':
    app.run()
