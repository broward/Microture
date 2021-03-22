import fastjsonschema
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

schema_file = BASE_DIR + "/Schemas/Base.json"
test_file = BASE_DIR + "/Test/Base.json"
test_fail_file = BASE_DIR + "/Test/BaseFailure.json"

    
from pathlib import Path
schema = Path(schema_file).read_bytes()
#schema = schema.replace('\n', '')

test = Path(test_file).read_bytes()
test_fail = Path(test_fail_file).read_bytes()
#test = test.replace('\n', '')

validate = fastjsonschema.compile(eval(schema))
validate(eval(test))
validate(eval(test_fail))



