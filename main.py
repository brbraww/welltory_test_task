from os import listdir
from os.path import isfile, join
import json
from jsonschema import validate

def get_filenames(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def validateJsonSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except Exception as err:
        return (False, err)
    return (True, "OK")

def validateFiles(json_filenames, schema_filenames):
    log = open("log.txt", "w")
    for j in json_filenames:
        log.write("JSON-file: " + j + "\n\n")

        f = open("task_folder/event/" + j)
        try:
            json_obj = json.load(f)
        except Exception as err:
            f.close()
            log.write(err + "\n")
            continue
        f.close()
        for s in schema_filenames:
            f = open("task_folder/schema/" + s)
            try:
                schema = json.load(f)
            except Exception as err:
                f.close()
                log.write(err + "\n")
                continue
            f.close()
            res = validateJsonSchema(json_obj, schema)
            log.write("Schema: {}\nResult: {}\n".format(s,res))
        log.write("\n")
    log.close()



if __name__ == '__main__':
    JSON_FILENAMES = get_filenames("task_folder/event")
    SCHEMA_FILENAMES = get_filenames("task_folder/schema")
    validateFiles(JSON_FILENAMES, SCHEMA_FILENAMES)