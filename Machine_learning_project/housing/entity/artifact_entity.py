#Entity is liye banate hai taaki data ko structured, safe aur predictable form me pass kiya ja sake.
#entity = packed labled data
from collections import namedtuple
DataIngestionArtifact = namedtuple("DataIngestionArtifact",
                                   ["train_file_path","test_file_path","is_ingested","message"])
