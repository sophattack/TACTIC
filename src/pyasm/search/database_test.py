#!/usr/bin/python 
###########################################################
#
# Copyright (c) 2005, Southpaw Technology
#                     All Rights Reserved
#
# PROPRIETARY INFORMATION.  This software is proprietary to
# Southpaw Technology, and is not to be reproduced, transmitted,
# or disclosed in any way without written permission.
#
#
#
import tacticenv

from pyasm.security import *
from transaction import *
from search import *
from sql import *

import unittest

class DatabaseTest(unittest.TestCase):

    def test_all(my):

        my._test_project()
        my._test_get_connect()
        my._test_get_tables()


    def _test_get_connect(my):
        my.sql1 = Sql("sthpw", vendor="Sqlite")
        my.sql1.connect()
        print my.sql1
        results1 = my.sql1.do_query("select * from login")

        my.sql2 = Sql("sthpw", user="postgres", vendor="PostgreSQL")
        my.sql2.connect()
        print my.sql2
        results2 = my.sql2.do_query("select * from login")

        my.assertNotEquals(results1, results2)

        my.sql3 = Sql("sthpw", user="postgres", vendor="MySQL")
        my.sql3.connect()
        print my.sql3
        results2 = my.sql2.do_query("select * from login")

        my.assertNotEquals(results1, results2)





    def _test_get_tables(my):

        # This will fail because get_tables uses the default database to
        # get the table information
        tables1 = my.sql1.get_tables()
        print "tables1: ", len(tables1)

        tables2 = my.sql2.get_tables()
        print "tables2: ", len(tables2)
        print tables1 == tables2

        sobject = SearchType.create("unittest/city")
        sobject.set_value("name", "Miami")
        sobject.commit()

        sobject.delete()



    def _test_project(my):

        # create a fake project
        #project = SearchType.create("sthpw/project")
        #project.set_value("code", "db_test")
        #project.set_value("db_resource", "sqlite")
        #project.commit()
        from pyasm.biz import Project
        project = Project.get_by_code("db_test")

        db_resource = project.get_db_resource()

        # so if we have search type, this will use the database resource
        # that is designated by
        search_type = "config/widget_config?project=db_test"
        search = Search(search_type)
        sobjects = search.get_sobject()

        # this is really tricky to do because a *lot* of functions assume
        # a local database by passing just a database string through.
        # things like table_exists() or any of these.  Ultimately, they
        # have to do a DbContainer.get(database) to do any operations.
        # But on the way, db_resource turns into database_name.  To really
        # fix, we have to enforce db_resource at DbContainer

        DbContainer.get(database)
        # have information about the host? without DbResource?
        # Right now, we assume local main database, but this is misleading.
        # Need to able to ensure that this does not change anywhere.

        # another big problem is that SearchType was used to get the database
        database = search_type_obj.






if __name__ == "__main__":
    Batch(project_code="unittest")
    unittest.main()

