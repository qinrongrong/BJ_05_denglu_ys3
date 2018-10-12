import yaml,os

class ReadYaml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+"Data"+os.sep+filename
    def read_yaml(self):
        with open(self.filepath,"r",encoding="utf-8")as f:
            return yaml.load(f)
    def read_yaml2(self):
        with open("../Data/address.yaml","r",encoding="utf-8")as f:
            return yaml.load(f)
if __name__ == '__main__':
    def get_data(text_type):
        datas=ReadYaml("address.yaml").read_yaml2()
        arrs = []
        if text_type=="add":
            for data in datas.get("add_address").values():
                arrs.append((data.get("name"), data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("address"),data.get("youbian")))
            return arrs
        elif text_type=="update":
            for data in datas.get("update_address").values():
                arrs.append((data.get("name"), data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("address"),data.get("youbian"),data.get("toast")))
            return arrs


