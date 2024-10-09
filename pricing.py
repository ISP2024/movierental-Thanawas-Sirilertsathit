class PriceStrategy:
    def get_price(self, days_rented):
        raise NotImplementedError("Subclasses should implement this method.")

    def get_rental_points(self, days_rented):
        raise NotImplementedError("Subclasses should implement this method.")

    def get_code(self):
        raise NotImplementedError("Subclasses should implement this method.")


class RegularPriceStrategy(PriceStrategy):
    def get_price(self, days_rented):
        amount = 2.0
        if days_rented > 2:
            amount += 1.5 * (days_rented - 2)
        return amount

    def get_rental_points(self, days_rented):
        return 1

    def get_code(self):
        return 0


class ChildrensPriceStrategy(PriceStrategy):
    def get_price(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += 1.5 * (days_rented - 3)
        return amount

    def get_rental_points(self, days_rented):
        return 1

    def get_code(self):
        return 1


class NewReleasePriceStrategy(PriceStrategy):
    def get_price(self, days_rented):
        return 3 * days_rented

    def get_rental_points(self, days_rented):
        return days_rented  # Earn 1 point for each day rented

    def get_code(self):
        return 2

class NoPriceStrategy(PriceStrategy):
    def get_price(self, days_rented):
        return 0

    def get_rental_points(self, days_rented):
        return 0

    def get_code(self):
        return "Unknown"