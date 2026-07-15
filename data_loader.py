import json

def load_contracts(path, limit=50):
    with open(path,'r',encoding='utf-8') as f:
        data=json.load(f)
    docs=data["data"][:limit]
    out=[]
    for d in docs:
        paras=[]
        for p in d.get("paragraphs",[]):
            paras.append(p.get("context",""))
        out.append({"contract_id":d.get("title","unknown"),
                    "text":"\n".join(paras)})
    return out