from pathlib import Path

def abs_path(file_path):
   base_path = Path(__file__).parent
   return (base_path / file_path).resolve()

def version_path(file_path, version):
   return abs_path(file_path.replace('VERSION', str(version)))
   
def get_current_version():
   return 1