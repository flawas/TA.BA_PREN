from PREN_flawas import DataPreparation, DataVerify

DataPreparation.setPos(1, "red")
DataPreparation.setPos(2, "blue")
DataPreparation.setPos(3, "yellow")
DataPreparation.setPos(4, "red")
DataPreparation.setPos(6, "red")
DataPreparation.setPos(7, "blue")
DataPreparation.setPos(8, "yellow")

DataVerify.sendData("https://oawz3wjih1.execute-api.eu-central-1.amazonaws.com/cubes/team33/config", "QBg3kjqB59xN", DataPreparation.getjson())