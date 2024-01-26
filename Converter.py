#Only does temp, want it to do measurements as well 

tempScale = {
    "Celcius": "C",
    "Fahrenheit": "F",
    "Kelvin": "K"
}

def convertTemp(value, inputScale, outputScale): 
    if inputScale == "C": 
        if outputScale == "F": 
            return value * 1.8 + 32
        elif outputScale == "K": 
            return value + 273.25 
        else: 
            return value 
    elif inputScale == "F": 
        if outputScale == "C": 
            return (value - 32) / 1.8
        elif outputScale == "K":
            return (value + 459.67) * 5/9
        else: 
            return value 
    elif inputScale == "K":
        if outputScale == "C": 
            return value - 273.15
        elif outputScale == "F":
            return value * 9/5 - 459.67
        else:
            return value 
    else: 
        return value
    
while True: 
    print("Enter a temperature to convert: ")
    value = float(input())
    print("Enter the input scale: ")
    inputScale = input()
    print("Enter the output scale: ")
    outputScale = input()
    result = convertTemp(value, inputScale, outputScale)
    print(f'{value} {inputScale} = {result} {outputScale}')
    print("Do you want to convert another temperature? (y/n)")
    if input() == "n":
        break