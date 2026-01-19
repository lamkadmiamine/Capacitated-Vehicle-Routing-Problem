import pandas as pd


class CVRPData:
    """
    Container class for CVRP instance data.
    """

    def __init__(self, file_path, num_clients, num_long, num_short):
        self.file_path = file_path
        self.numClients = num_clients
        self.numVehiclesLongTerm = num_long
        self.numVehiclesShortTerm = num_short

        self._load_data()

    def _load_data(self):
        excel = pd.ExcelFile(self.file_path)

        self.distances = pd.read_excel(
            self.file_path,
            sheet_name="Distance",
            usecols="B:AZ",
            skiprows=1,
            nrows=self.numClients + 1
        ).values

        parameters = pd.read_excel(self.file_path, sheet_name="Parameters")

        self.demands = parameters.iloc[1:self.numClients + 2, -1].values.flatten()

        # Long-term vehicles
        self.vehicleCapacityLong = parameters.iloc[3, 6:12].values.flatten()
        self.vehicleSpeedLong = parameters.iloc[4, 6:12].values.flatten()
        self.fixedCostLong = parameters.iloc[5, 6:12].values.flatten()
        self.maxSoftTimeLong = parameters.iloc[6, 6:12].values.flatten()
        self.maxHardTimeLong = parameters.iloc[7, 6:12].values.flatten()
        self.maxDistanceLong = parameters.iloc[8, 6:12].values.flatten()
        self.overDistanceCostLong = parameters.iloc[10, 6:12].values.flatten()
        self.overTimeCostLong = parameters.iloc[11, 6:12].values.flatten()

        # Short-term vehicles
        self.maxDistanceShort = parameters.iloc[9, 12:32].values.flatten()
        self.fixedCostShort = parameters.iloc[5, 12:32].values.flatten()

