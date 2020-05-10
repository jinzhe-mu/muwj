import yaml
import pytest

# data = {"a": {"b": {"x"[1, 2, 3]}}}
print(yaml.safe_load(open("./demo.yml")))

print(yaml.safe_load(open("./demo2.yml")))