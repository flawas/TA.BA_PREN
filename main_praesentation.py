from data.Datasend import Datasend

# JSON Format
# {
#  "time": 32,
#  "energy": 0.5
# }
#

datasend = Datasend("https://i-ba-pren.flaviowaser.ch/upload-data.php")

datasend.send(120, 0.7)