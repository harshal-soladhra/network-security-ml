from setuptools import find_packages,setup
from typing import List


def get_requirments()->List[str]:
  '''
  this fun will return list of requirmets
  '''
  requirment_lst:List[str]=[]
  try:
    with open('requirment.txt','r') as file:
      #read lines from the file
      lines=file.readlines()
      #process each line
      for line in lines:
        requirment=line.strip()
        ##ignore empty line and -e .
        if requirment and requirment!= '-e .':
          requirment_lst.append(requirment)

  except FileExistsError:
    print('my requitrment.txt is not found')
  
  return requirment_lst

setup(
  name="complete_ml_project",
  version="0.0.1",
  author="harshal soladhra",
  author_email="soladhraharshal.email@example.com",
  packages=find_packages(),
  install_requires=get_requirments(),
  description="A complete machine learning project setup",
)
