import pandas as pd

cols = [
    "Mode",
    "Date",                         #yyyy-mm-dd形式
    "Map",                    #Haven,Bind,Acent,Split,Icebox,Bleeze,Fracture
    "Agent",
    "Result",
    "ATK_Round",
    "DEF_Round",
    "Enemy_Round",
    "ATK_1stblood",                 #チーム全体
    "DEF_1stblood",                 #チーム全体
    "ATK_GetRound_after_1stblood",
    "DEF_GetRound_after_1stblood",
    "ATK_AllKill",
    "DEF_AllKill",
    "ATK_Plant",
    "DEF_Plant",
    "ATK_Plant_win",
    "DEF_Plant_win",
    "ATK_Defuse",
    "DEF_Defuse",
    "ATK_Detonation",
    "DEF_Detonation",
    "is_MVP",
    "ACS",
    "Kill",
    "Death",
    "Assist",
    "MoneyRating",
    "1stblood",
    "Plant",
    "Defuse"
]

def Add_DB()->pd.DataFrame:
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

def write_to_csv(df:pd.DataFrame,file_path:str)->None:
    df.to_csv(file_path,index=False)
    return None

def add_and_write(old_df:pd.DataFrame,file)->None:
    df_append = Add_DB()
    df = pd.concat([old_df,df_append])
    write_to_csv(df,file)

file = "Battle_Report.csv"
df = pd.read_csv(file)

add_and_write(df,file)