class file_appRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Bogota':
            return 'Bogota'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Bogota':
            return 'Bogota'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Bogota' or \
           obj2._meta.app_label == 'Bogota':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Bogota':
            return db == 'Bogota'
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
        if model._meta.app_label == 'Maf':
            return 'Maf'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Maf':
            return 'Maf'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Maf' or \
           obj2._meta.app_label == 'Maf':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Maf':
            return db == 'Maf'
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
        if model._meta.app_label == 'Cartera ok':
            return 'Cartera ok'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Cartera ok':
            return 'Cartera ok'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Cartera ok' or \
           obj2._meta.app_label == 'Cartera ok':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Cartera ok':
            return db == 'Cartera ok'
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
        if model._meta.app_label == 'Claro':
            return 'Claro'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Claro':
            return 'Claro'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Claro' or \
           obj2._meta.app_label == 'Claro':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Claro':
            return db == 'Claro'
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
        if model._meta.app_label == 'Codensa':
            return 'Codensa'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Codensa':
            return 'Codensa'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Codensa' or \
           obj2._meta.app_label == 'Codensa':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Codensa':
            return db == 'Codensa'
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
        if model._meta.app_label == 'Colpatria':
            return 'Colpatria'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Colpatria':
            return 'Colpatria'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Colpatria' or \
           obj2._meta.app_label == 'Colpatria':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Colpatria':
            return db == 'Colpatria'
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
        if model._meta.app_label == 'Davivienda':
            return 'Davivienda'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Davivienda':
            return 'Davivienda'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Davivienda' or \
           obj2._meta.app_label == 'Davivienda':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Davivienda':
            return db == 'Davivienda'
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
        if model._meta.app_label == 'Falabella':
            return 'Falabella'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Falabella':
            return 'Falabella'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Falabella' or \
           obj2._meta.app_label == 'Falabella':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Falabella':
            return db == 'Falabella'
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
        if model._meta.app_label == 'Banco popular':
            return 'Banco popular'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Banco popular':
            return 'Banco popular'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Banco popular' or \
           obj2._meta.app_label == 'Banco popular':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Banco popular':
            return db == 'Banco popular'
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
        if model._meta.app_label == 'Progresa':
            return 'Progresa'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Progresa':
            return 'Progresa'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Progresa' or \
           obj2._meta.app_label == 'Progresa':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Progresa':
            return db == 'Progresa'
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
        if model._meta.app_label == 'Cartera propia':
            return 'Cartera propia'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Cartera propia':
            return 'Cartera propia'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Cartera propia' or \
           obj2._meta.app_label == 'Cartera propia':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Cartera propia':
            return db == 'Cartera propia'
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
        if model._meta.app_label == 'Qnt':
            return 'Qnt'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Qnt':
            return 'Qnt'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Qnt' or \
           obj2._meta.app_label == 'Qnt':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Qnt':
            return db == 'Qnt'
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
        if model._meta.app_label == 'Santander':
            return 'Santander'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'Santander':
            return 'Santander'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'Santander' or \
           obj2._meta.app_label == 'Santander':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'Santander':
            return db == 'Santander'
        return False

class file_appRouter14(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'public':
            return 'public'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'public':
            return 'public'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'public' or \
           obj2._meta.app_label == 'public':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'public':
            return db == 'public'
        return False

class file_appRouter15(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'AVANTEL':
            return 'AVANTEL'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'AVANTEL':
            return 'AVANTEL'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'AVANTEL' or \
           obj2._meta.app_label == 'AVANTEL':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'AVANTEL':
            return db == 'AVANTEL'
        return False

class file_appRouter16(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'CARTERA PROPIA':
            return 'CARTERA PROPIA'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'CARTERA PROPIA':
            return 'CARTERA PROPIA'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mi_app_2 app is involved.
        """
        if obj1._meta.app_label == 'CARTERA PROPIA' or \
           obj2._meta.app_label == 'CARTERA PROPIA':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mi_app_2 app only appears in the 'mi_db_2'
        database.
        """
        if app_label == 'CARTERA PROPIA':
            return db == 'CARTERA PROPIA'
        return False