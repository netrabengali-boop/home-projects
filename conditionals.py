# Get the current temperature from the user
temperature = float(input("Enter the current temperature in °C: "))

# Check wardrobe suitability based on weather comfort standards
if temperature >= 24:
    print("👉 Perfect! You can safely wear light, soft cotton T-shirts or linen.")
elif 18 <= temperature < 24:
    print("👉 Good to go! Wear a light, soft long-sleeve shirt or a thin jersey.")
elif 15 <= temperature < 18:
    print("👉 Borderline. Bring a light cardigan or windbreaker just in case.")
else:
    print("👉 Too cold! Stick to the pullover or jacket for now to stay safe.")
    
