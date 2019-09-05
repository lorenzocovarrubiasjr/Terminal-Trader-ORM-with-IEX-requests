import sqlite3

class ORM():
    dbpath = ""
    tablename = ""
    fields = []
        
    def __init__(self):
       raise NotImplementedError
        
    def save(self):
        if self.pk is None:
            self.__insert()
        else:
            self.__update()
            
            # the __ on functions implies that they are private functions. (2 Underscores)
            # they are only supposed to be called by save().
            # No one should call them.
            
    def __insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            fieldlist = ", ".join(self.fields)
            qmarks = ", ".join(['?' for _ in self.fields])
            SQL = "INSERT INTO {} ({}) VALUES ({})".format(self.tablename, fieldlist, qmarks)
            values = [getattr(self, field) for field in self.fields]
            curs.execute(SQL, values)
            pk = curs.lastrowid
            self.pk = pk
            
    def __update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            set_equals = ", ".join(["{}=?".format(field) for field in self.fields])
            SQL = "UPDATE {} SET {} WHERE pk=?;".format(self.tablename, set_equals)
            values = [getattr(self,field) for field in self.fields]
            values.append(self.pk)
            curs.execute(SQL,values)
            
    def delete(self):
        if not self.pk:
            raise KeyError(self.__repr__() + " is not a row in " + self.tablename)
        
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            SQL = "DELETE FROM {} WHERE pk = ?;".format(self.tablename)
            curs.execute(SQL, (self.pk, ))
    
    @classmethod
    def one_from_where_clause(cls, where_clause="", values=tuple()):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            SQL = "SELECT * FROM {} {}".format(cls.tablename, where_clause)
            cur.execute(SQL, values)
            
            row = cur.fetchone()
            if not row:
                return None
            return cls(**row)
    
    @classmethod
    def all_from_where_clause(cls, where_clause="", values=tuple()):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            SQL = "SELECT * FROM {} {}".format(cls.tablename, where_clause)
            cur.execute(SQL, values)
            rows = cur.fetchall()
            return [cls(**row) for row in rows]
    
    @classmethod
    def all(cls, complete=None):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            SQL = "SELECT * FROM {}".format(cls.tablename)
            cur.execute(SQL)
            rows = cur.fetchall()
            return [cls(**row) for row in rows]
        
        """
        if complete is None:
            return cls.all_from_where_clause()
        elif bool(complete) is True:
            return cls.all_from_where_clause("WHERE complete=?", (1, ))
        elif bool(complete) is False:
            return cls.all_from_where_clause("WHERE complete=?", (0, ))
        """
            
    @classmethod
    def one_from_pk(cls, pk):
        return cls.one_from_where_clause("WHERE pk=?", (pk, ))
    
    def __repr__(self):
        #fields = " = self.{}, ".join(self.fields) + "= self.{}"
        #pattern = "<TodoItem: " + fields
        #return pattern.format(f for f in fields)
        return f"<{self.__class__.__name__} : ORM {self.tablename}"
            
        
    
    