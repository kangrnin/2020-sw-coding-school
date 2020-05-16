from pathlib import Path

def abs_path(file_path):
   base_path = Path(__file__).parent
   return (base_path / file_path).resolve()