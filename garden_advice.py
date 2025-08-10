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

# Function to get advice based on season
def get_season_advice(season):
    """Return gardening advice based on the given season."""
    return season_advice.get(season.lower(), "No advice for this season.\n")

# Function to get advice based on plant type
def get_plant_advice(plant_type):
    """Return gardening advice based on the given plant type."""
    return plant_advice.get(plant_type.lower(), "No advice for this type of plant.")

# Function to recommend plants for a given season
def recommend_plants(season):
    """Suggest suitable plants based on the season."""
    recommendations = {
        "summer": ["Sunflowers", "Tomatoes", "Lavender"],
        "winter": ["Kale", "Pansies", "Broccoli"]
    }
    return recommendations.get(season.lower(), ["No recommendations available."])

# Main program flow
def main():
    """Main function to run the gardening advice program."""
    # Get user input for season and plant type
    season = input("Enter the current season (summer/winter): ")
    plant_type = input("Enter the type of plant (flower/vegetable): ")

    # Generate advice
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Display advice
    print("\nGardening Advice:")
    print(advice)

    # Display recommended plants
    print("\nRecommended plants for", season.capitalize() + ":")
    print(", ".join(recommend_plants(season)))

# Run the program
if __name__ == "__main__":
    main()
