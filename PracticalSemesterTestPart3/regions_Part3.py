# regions.py
class Regions:
    def __init__(self):
        self.regions = []

    def add_region(self, region):
        self.regions.append(region)

    def get_region_by_code(self, code):
        for region in self.regions:
            if region.code == code:
                return region
        return None

    def get_valid_region_codes(self):
        return [region.code for region in self.regions]

    def __str__(self):
        return ", ".join(self.get_valid_region_codes())