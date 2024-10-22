import pandas as pd
import math

ucsv = pd.read_csv( "users.csv")
gcsv_raw = pd.read_csv("group.csv")

def make_lists( row ):
    print("**",row['user_ids'])
    row['user_ids'] = row['user_ids'].split(',')
    gv = row['group_ids']
    row['group_ids'] = [] if isinstance(gv,float) and math.isnan(gv) else gv.split(',')
    return row

gcsv = gcsv_raw.apply(make_lists,axis=1)
print(ucsv)
print(gcsv)
print(gcsv['name']=='devs')
devs=gcsv.loc[ gcsv['name']=='devs']
v=devs['user_ids']
print(type(v))
print(v)
print("===============")
vv=v.iloc[0]
print(type(vv))
def load_db():
    for u in users:
        query = [{
            "AddEntity": {
                "with_class": "User",
                "properties": {
                    "name": u.name,
                    "system_id": u.system_id
                }
            }
        }]

    for g in groups:
        query=[{
            "FindEntity": {
                    "with_class": "User",
                    "constraints": {
                        "system_id" : ["in",g.user_ids]
                    }
                }
            },{
            "AddEntity": {
                "with_class": "Group",
                "_ref":1,
                "properties": {
                    "name": g.name,
                    "system_id": g.system_id
                },
                "connect": {
                    "ref":1,
                    "class":"GroupMember"
                }
            }
        }]


    # add group links in phase 2. ( easier than trying to sort out ordering )
    for g in groups:
        if len(g.group_ids) == 0:
            continue







