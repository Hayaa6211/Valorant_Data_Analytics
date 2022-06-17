import pandas as pd
import json

class Read:
    def __init__(self):
        pass

    def read_json(path):
        return json.load(open(path,"r"))
    
    def read_df(path):
        return pd.read_csv(path)

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
    
    def write_to_csv(df:pd.DataFrame,file_path:str):
        df.to_csv(file_path,index=False)

def main():
    read = Read
    df = read.read_df("Battle_Report.csv")
    cols = read.read_json("cols.json")
    add_df = Write.add_db(cols)
    pd.concat([df,add_df])
    Write.write_to_csv(df,"Battle_Report.csv")



if __name__ == "__main__":
    main()