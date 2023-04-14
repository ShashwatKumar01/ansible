import yaml
file="/home/ubuntu/playbooks/createuser.yml"
with open(file) as f:
    try:
        print(yaml.safe_load(f))
    except yaml.YAMLError as e :
        print(e)

