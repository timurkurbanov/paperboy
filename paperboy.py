class Paperboy:
    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings
    
    def __str__(self):
        return "Name= {}, Experience= {}, Earnings= ${}".format(self.name, self.experience, self.earnings)
        
    def quota(self):
        return 50 + self.earnings/2
        """
        This method should calculate and return the paperboy's quota for his next delivery
        """
        # The first time a paperboy makes a delivery, 
        #     the quota is 50. 

        # The next time, 
        #     the quote is 50 plus half the number of papers that the paperboy has delivered in the past. 

        # In this way the quota should increase 
        #     after every delivery the paperboy makes.

    def deliver(self, start_address, end_address):
        papers_delivered = (end_address - start_address + 1)

        if self.quota() < papers_delivered:
            self.earnings = self.earnings + ((0.50 * (papers_delivered - self.quota())) + (0.25 * self.quota()))
        elif self.quota() > papers_delivered:
            self.earnings = self.earnings - 2 + 0.25 * papers_delivered

        self.experience = self.experience + papers_delivered
        return self.earnings
    
        """
        This method will take two house numbers and return the amount of money earned on this delivery as a floating point number. It should also update the paperboy's experience!
        Let's assume that the start_address is always a smaller number than the end_address

        Every day, each paperboy is given a house number to start at and a house number to finish at. 
        
        They get paid $0.25 for every paper they deliver,
        and $0.50 for every paper over their quota. 
        
        If at the end of the day they haven't met their quota, they lose $2.
        """
        #num_houses = end_address - start_address
        # self.experience += num_houses


        # return 17.5

    def report(self):
        return "I am {}, I have delivered {} papers and I have earned ${} so far".format(self.name, self.experience, self.earnings)

        """
        This method should return a string about the paperboy's performance
        e.g. "I'm Tommy, I've delivered 90 papers and I've earned $38.25 so far!"
        """



# def test(given, expected):
#     if given == expected:
#         print(f"Test Passed: {given} == {expected}")
#     else:
#         print(f"Test Failed: {given} != {expected}")

# tommy = Paperboy("Tommy")

# test(tommy.quota(), 50)
# test(tommy.deliver(101, 160), 17.5)


# tommy.earnings # 17.5
# tommy.report() # "I'm Tommy, I've delivered 60 papers and I've earned $17.5 so far!"
result = Paperboy("Ronny", 0, 0)
print(result.deliver(101,160))
print(result.report())
print(result.deliver(1,75))
print(result.report())

