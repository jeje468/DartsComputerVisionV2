class GameplayAttributes:
    calibrationPoints = []
    startingPoint = []
    players = []
    points = []
    shots = []

    def __init__(self, calibrationPoints, players, startingPoint):
        self.calibrationPoints = calibrationPoints
        self.players = players
        self.startingPoint = startingPoint

        for i in range(0, len(players)):
            self.points.append(startingPoint)