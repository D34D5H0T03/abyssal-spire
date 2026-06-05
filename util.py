class Stat():
    def __init__(self, strength, speed, constitution, luck):
        self.parameters = {"Strength" : strength,
                           "Speed": speed,
                           "Constitution": constitution,
                           "Luck": luck}
        
    def increase_stat(self,parameter, value):
        param_key = parameter.capitalize()
        
        if param_key in self._parameters:
            self._parameters[param_key] += value
            print(f"{param_key} increased by {value}!")
        else:
            print(f"System Error: '{parameter}' is not a valid stat.")
        
    def decrease_stat(self,parameter, value):
        param_key = parameter.capitalize()
        
        if param_key in self._parameters:
            # 4. Clamp the subtraction so stats never drop below 0
            current_value = self._parameters[param_key]
            self._parameters[param_key] = max(0, current_value - value)
            print(f"{param_key} decreased by {value}!")
        else:
            print(f"System Error: '{parameter}' is not a valid stat.")
            
    def __str__(self):
        return str(self._parameters)