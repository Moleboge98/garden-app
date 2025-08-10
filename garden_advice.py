# Gardening Advice Program

# Dictionary holding advice for different seasons and plant types
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n"
}

plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

# Extra advice based on temperature
temperature_advice = {
    "hot": "Consider watering early in the morning to prevent evaporation.\n",
    "mild": "Normal watering should be fine.\n",
    "cold": "Avoid overwatering as plants use less water in cold weather.\n"
}

# Extra advice based on water availability
water_availability_advice = {
    "low": "Use mulch to retain soil moisture and choose drought-tolerant plants.\n",
    "medium": "Water every 2–3 days depending on the plant needs.\n",
    "high": "Regular daily watering is possible, but avoid waterlogging.\n"
}

# Extra advice based on gardener experience
experience_advice = {
    "beginner": "Start with easy-to-grow plants like basil, lettuce, or marigolds.\n",
    "intermediate": "Experiment with companion planting to improve growth and reduce pests.\n",
    "expert": "Try grafting or hydroponics for more advanced gardening projects.\n"
}

# Function to get advice based on season
def get_season_advice(season):
    return season_advice.get(season.lower(), "No advice for this season.\n")

# Function to get advice based on plant type
def get_plant_advice(plant_type):
    return plant_advice.get(plant_type.lower(), "No advice for this type of plant.")

# Function to recommend plants for a given season
def recommend_plants(season):
    recommendations = {
        "summer": ["Sunflowers", "Tomatoes", "Lavender"],
        "winter": ["Kale", "Pansies", "Broccoli"]
    }
    return recommendations.get(season.lower(), ["No recommendations available."])

# Main program flow
def main():
    print("🌿 Welcome to the Gardening Advice Program 🌿\n")

    # Get user inputs
    season = input("Enter the current season (summer/winter): ")
    plant_type = input("Enter the type of plant (flower/vegetable): ")
    temperature = input("Enter today's temperature type (hot/mild/cold): ")
    water_availability = input("Enter water availability (low/medium/high): ")
    experience = input("Enter your gardening experience (beginner/intermediate/expert): ")

    # Generate advice
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type) + "\n"
    advice += temperature_advice.get(temperature.lower(), "")
    advice += water_availability_advice.get(water_availability.lower(), "")
    advice += experience_advice.get(experience.lower(), "")

    # Display advice
    print("\n🌱 Gardening Advice:")
    print(advice)

    # Display recommended plants
    print("\n🌸 Recommended plants for", season.capitalize() + ":")
    print(", ".join(recommend_plants(season)))

# Run the program
if __name__ == "__main__":
    main()
