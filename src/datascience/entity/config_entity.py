from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:  #same element as in config.yaml
    root_dir: Path
    source_URL:Path
    local_data_file:Path
    unzip_dir: Path