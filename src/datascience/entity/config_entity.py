from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:  #same element as in config.yaml
    root_dir: Path
    source_URL:Path
    local_data_file:Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict # store the schema.yaml

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path