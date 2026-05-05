class Asset:
    def __init__(self, asset_id, name, quantity, min_threshold):
        self.asset_id = asset_id
        self.name = name
        self.quantity = quantity
        self.min_threshold = min_threshold

    def update_quantity(self, amount):
        # Prevent quantity from going below zero
        if self.quantity + amount < 0:
            print("❌ Error: Quantity cannot be negative!")
            return False
        self.quantity += amount
        print(f"Updated {self.name}. New quantity: {self.quantity}")
        return True

    def check_alert(self):
        if self.quantity < self.min_threshold:
            return f"⚠️ ALERT: Low stock for {self.name} (Only {self.quantity} left!)"
        return f"{self.name} stock level is sufficient."

class AssetManager:
    def __init__(self):
        self.assets = {}

    def add_asset(self):
        asset_id = input("Enter Asset ID: ")
        name = input("Enter Asset Name: ")
        quantity = int(input("Enter Initial Quantity: "))
        min_threshold = int(input("Enter Minimum Threshold: "))
        self.assets[asset_id] = Asset(asset_id, name, quantity, min_threshold)
        print(f"Asset '{name}' added successfully!\n")

    def manage_inventory(self):
        while True:
            print("\n1. Add Asset | 2. Update Quantity | 3. Display Inventory | 4. Exit")
            choice = input("Select an option: ")
            
            if choice == "1":
                self.add_asset()
            elif choice == "2":
                aid = input("Enter Asset ID to update: ")
                if aid in self.assets:
                    change = int(input("Enter amount to add (e.g. 5) or subtract (e.g. -5): "))
                    self.assets[aid].update_quantity(change)
                else:
                    print("Asset not found.")
            elif choice == "3":
                for asset in self.assets.values():
                    print(f"ID: {asset.asset_id} | Name: {asset.name} | Qty: {asset.quantity}")
                    print(asset.check_alert())
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    manager = AssetManager()
    manager.manage_inventory()