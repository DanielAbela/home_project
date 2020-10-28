from pathlib import Path

FILENAMES = ["address_list.csv", "postcode_reference.csv"]
WORKING_DIRECTORY = Path(__file__).parent
DATA_DIRECTORY = WORKING_DIRECTORY / "data"
DEFAULT_ROUND_VALUE = 3

# The following is a list of the number of rows returned based on changing the default round value:
# 0: 0
# 1: 213388
# 2: 113665
# 3: 11209
# 4: 1394
# 5: 31
# 6: 0
