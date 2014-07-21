import MapReduce
import sys

"""
Join assignment in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order ID
    # value: complete record
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order ID
    # value: list of records (including both orders and line items)
    
    # Separate records into a list of orders and a list of line_items
    orders = []
    line_items = []
    for v in list_of_values:
        table = v[0]
        if table == "order":
            orders.append(v)
        if table == "line_item":
            line_items.append(v)
    
    # Emit each combination of orders and line items
    for o in orders:
        for li in line_items:
            mr.emit(o + li)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
