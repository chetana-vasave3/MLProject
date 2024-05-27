#metadata information about your project
from setuptools import find_packages,setup
from typing import List

hypen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    """this fn will return the list of requirements  """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        
setup(
      name="MLPROJECT",
      version='0.0.1',
      author="chetana vasave",
      author_email="vasavechetana5@gmail.com",
      packages=find_packages(),
      # install_requires=['pandas','numpy','seaborn','matplotlib','sci-kit learn']
      install_requires=get_requirements('requirement.txt')
)
