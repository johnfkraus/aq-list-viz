# make-link-string.py
# given a link object, creates a unique string combining source and target nodes.
def make_link_string(link):
    # print(link)
    source = link['source']
    target = link['target']
    if source == target:
        raise Exception("Source and target are equal.")
    nodestring = ""
    if source < target: # str(link['source']) < str(link['target']):
        nodestring = source + ","+  target #  str(link['source']) + str(link['target'])
    else:
        nodestring = target + "," + source  # str(link['target']) + str(link['source'])
    return nodestring


def test_function_throws_exception(link):
    try:
        make_link_string(link)
    except Exception:
        pass
    else:
       self.fail('ExpectedException not raised')


link_obj1 = {"source": "QDi.123", "target": "QDi.012"}
link_obj2 = {"source": "QDi.012", "target": "QDi.123"}
assert(make_link_string(link_obj1) == make_link_string(link_obj2))

link_obj3 = {"source": "QDi.123", "target": "QDi.123"}
test_function_throws_exception(link_obj3)

link_obj4 = {"source": "QDi.123", "target": "QDi.012"}
link_obj5 = {"source": "QDi.012", "target": "QDi.223"}
assert(make_link_string(link_obj4) != make_link_string(link_obj5))

