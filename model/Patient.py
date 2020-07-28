class Patient:

    def __init__(self, cId, arriveTime, patience, receiveTime, queue, visitTime, finishTime):
        self.cId = cId  # this is -> index in matrix
        self.arriveTime = arriveTime
        self.patience = patience
        self.receiveTime = receiveTime
        self.queue = queue
        self.visitTime = visitTime
        self.finishTime = finishTime

