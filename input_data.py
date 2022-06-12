import pandas as pd
import json

class Read:
    def __init__(self):
        pass

    def read_json(path):
        path = path
        return json.load(open(path,"r"))

class Write:
    def __init__(self):
        pass

    def add_db(cols:dict) -> pd.DataFrame:
        ll = []
        while True:
            l = []

            for col in cols:
                input_data = input(f"{col}:")

                if input_data == "exit":
                    break
                else:
                    l.append(input_data)
            
            if len(l) < len(cols):
                input_data = input("やり直す？1でやり直し")
                if input_data == "1":
                    continue
                else:
                    break
            else:
                ll.append(l)
        print(ll)
        return pd.DataFrame(ll,columns=cols)

def main():
    read = Read
    cols = read.read_json("cols.json")
    Write.add_db(cols)


if __name__ == "__main__":
    main()