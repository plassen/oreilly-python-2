"""
classFactory: function to return tailored classes
"""

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data)==len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
                
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))        
    
        def retrieve(self, curs, condition=None):
            query = "SELECT "+", ".join(self.cols)+" FROM "+self.table
            if (condition):
                query += " WHERE "+condition 
            curs.execute(query)
            row = curs.fetchone()
            R = build_row(self.table, " ".join(self.cols))
            return R(row)
            
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow

