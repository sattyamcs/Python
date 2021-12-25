class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is{self.train}")

sattyamApplication = RailwayForm()
sattyamApplication.name = "sattyam"
sattyamApplication.train = "kalindiexpress"
sattyamApplication.printData()