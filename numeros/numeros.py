class LoanSimulator:
    def __init__(self, loan_details, years, house_price):
        self._monthly_rate = (loan_details.imag / 12) / 100
        self._num_payments = years * 12
        self._starter_payment = loan_details.real
        self._loan = house_price - self._starter_payment
        self._monthly_payment = 0
        self._years = years
        self._house_price = house_price
        self._yearly_rate = loan_details.imag

    def get_total_payment(self):
        r = self._monthly_rate
        n =self._num_payments
        p = self._loan

        if r == 0:
            self.monthly_payment = p / n
        else:
            self.monthly_payment = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    def show_result(self):
        print("----- Loan Simulator -----")
        print()
        print(f' -> A house of {self._house_price}€')
        print(f' -> giving a starter payment of {self._starter_payment}€')
        print(f' -> and with an interest rate of {self._yearly_rate}% yearly')
        print(f' -> for {self._years} years:')
        print(f' -> Monthly payment to pay: {self.monthly_payment:.2f}€')
        print()
        print("----- End Simulation -----")

class Sabadell(LoanSimulator):
    def __init__(self, loan_details, years, house_price):
        self.bank = 'Sabadell'
        self._interest_rate = 2.2j
        loan_details = loan_details + self._interest_rate
        super().__init__(loan_details, years, house_price)

class Bbva(LoanSimulator):
    def __init__(self, loan_details, years, house_price):
        self.bank = 'BBVA'
        self._interest_rate = 3.5j
        loan_details = loan_details + self._interest_rate
        super().__init__(loan_details, years, house_price)

class Caixabank(LoanSimulator):
    def __init__(self, loan_details, years, house_price):
        self._interest_rate = 2.5j
        self.bank = 'Caixabank'
        loan_details = loan_details + self._interest_rate
        super().__init__(loan_details, years, house_price)

class Santander(LoanSimulator):
    def __init__(self, loan_details, years, house_price):
        self._interest_rate = 2.8j
        self.bank = 'Santander'
        loan_details = loan_details + self._interest_rate
        super().__init__(loan_details, years, house_price)

def main():
    # debug:
    years = 30
    house_price = 455_000

    simulation_caixabank = Caixabank(50_000, years, house_price)
    simulation_caixabank.get_total_payment()
    simulation_caixabank.show_result()

    simulation_sabadell = Sabadell(50_000, years, house_price)
    simulation_sabadell.get_total_payment()
    simulation_sabadell.show_result()

    simulation_bbva = Bbva(50_000, years, house_price)
    simulation_bbva.get_total_payment()
    simulation_bbva.show_result()

    simulation_santander = Santander(50_000, years, house_price)
    simulation_santander.get_total_payment()
    simulation_santander.show_result()


if __name__ == '__main__':
    main()




