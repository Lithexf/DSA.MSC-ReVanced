import json
from typing import List
from logger import setup_error_logger


logger = setup_error_logger()

class Settings:
    def __init__(self, settings_file: str = "config/settings.json") -> None:
        self.settings_file = settings_file
        self.default_columns = ["Name", "SamAccountName", "EmployeeNumber"]
        self.selected_collums = self.load_selected_columns()
        
    def load_selected_columns(self, DEBUG: bool = False) -> List[str]:
        try:
            with open(self.settings_file, 'r') as file:
                settings = json.load(file)
                if DEBUG:
                    print(settings)
                return settings.get("selected_columns", self.default_columns)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading settings: {e}")
            return self.selected_collums
    
    def save_settings(self) -> None:
        try:
            # Read the existing data from the file
            with open(self.settings_file, 'r') as file:
                data = json.load(file)
            
            # Update the necessary part
            data["selected_columns"] = self.selected_columns
            
            # Write the updated data back to the file
            with open(self.settings_file, 'w') as file:
                json.dump(data, file)
        except FileNotFoundError:
            # If the file does not exist, create it with the new data
            with open(self.settings_file, 'w') as file:
                json.dump({"selected_columns": self.selected_columns}, file)
        except Exception as e:
            logger.error(f"Error saving settings: {e}")

    def update_selected_collums(self, columns: List[str]) -> None:
        self.selected_collums = columns
        self.save_settings()


if __name__ == '__main__':
    setting = Settings()
    print(setting.load_selected_columns()[0])
                