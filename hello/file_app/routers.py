class file_appRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testbogo':
            return 'testbogo'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testbogo':
            return 'testbogo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testbogo' or \
           obj2._meta.app_label == 'testbogo':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testbogo':
            return db == 'testbogo'
        return False

class file_appRouter2(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testmaf':
            return 'testmaf'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testmaf':
            return 'testmaf'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testmaf' or \
           obj2._meta.app_label == 'testmaf':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testmaf':
            return db == 'testmaf'
        return False

class file_appRouter3(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testok':
            return 'testok'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testok':
            return 'testok'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testok' or \
           obj2._meta.app_label == 'testok':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testok':
            return db == 'testok'
        return False

class file_appRouter4(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testclar':
            return 'testclar'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testclar':
            return 'testclar'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testclar' or \
           obj2._meta.app_label == 'testclar':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testclar':
            return db == 'testclar'
        return False

class file_appRouter5(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testcode':
            return 'testcode'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testcode':
            return 'testcode'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testcode' or \
           obj2._meta.app_label == 'testcode':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testcode':
            return db == 'testcode'
        return False

class file_appRouter6(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testcolp':
            return 'testcolp'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testcolp':
            return 'testcolp'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testcolp' or \
           obj2._meta.app_label == 'testcolp':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testcolp':
            return db == 'testcolp'
        return False

class file_appRouter7(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testdavi':
            return 'testdavi'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testdavi':
            return 'testdavi'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testdavi' or \
           obj2._meta.app_label == 'testdavi':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testdavi':
            return db == 'testdavi'
        return False

class file_appRouter8(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testfala':
            return 'testfala'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testfala':
            return 'testfala'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testfala' or \
           obj2._meta.app_label == 'testfala':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testfala':
            return db == 'testfala'
        return False

class file_appRouter9(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testpopu':
            return 'testpopu'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testpopu':
            return 'testpopu'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testpopu' or \
           obj2._meta.app_label == 'testpopu':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testpopu':
            return db == 'testpopu'
        return False

class file_appRouter10(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testprog':
            return 'testprog'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testprog':
            return 'testprog'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testprog' or \
           obj2._meta.app_label == 'testprog':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testprog':
            return db == 'testprog'
        return False

class file_appRouter11(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testprop':
            return 'testprop'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testprop':
            return 'testprop'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testprop' or \
           obj2._meta.app_label == 'testprop':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testprop':
            return db == 'testprop'
        return False

class file_appRouter12(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testqnt':
            return 'testqnt'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testqnt':
            return 'testqnt'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testqnt' or \
           obj2._meta.app_label == 'testqnt':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testqnt':
            return db == 'testqnt'
        return False

class file_appRouter13(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testsant':
            return 'testsant'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'testsant':
            return 'testsant'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'testsant' or \
           obj2._meta.app_label == 'testsant':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'testsant':
            return db == 'testsant'
        return False