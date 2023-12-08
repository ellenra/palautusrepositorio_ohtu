from matchers import *

class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def build(self):
        return self.query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, number, attr):
        return QueryBuilder(And(self.query, HasAtLeast(number, attr)))

    def hasFewerThan(self, number, attr):
        return QueryBuilder(And(self.query, HasFewerThan(number, attr)))

    def oneOf(self, query_1, query_2):
        return QueryBuilder(Or(query_1, query_2))