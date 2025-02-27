import math

# Sample fingerprint database with known locations and their corresponding RSSI values
# Format: [AP1_RSSI, AP2_RSSI, AP3_RSSI]
fingerprint_db = {
    'Location1': [ -65, -70, -80 ],
    'Location2': [ -60, -75, -85 ],
    'Location3': [ -67, -72, -82 ],
    'Location4': [ -68, -71, -79 ]
}

# New RSSI values from a device (this is the test data)
new_rssi = [ -66, -73, -81 ]

# Function to compute Euclidean distance between two lists of numbers (RSSI values)
def euclidean_distance(rssi1, rssi2):
    # Ensure both lists have the same length
    if len(rssi1) != len(rssi2):
        raise ValueError("The two lists must have the same length")
    
    distance = 0
    # Compute the sum of squared differences
    for a, b in zip(rssi1, rssi2):
        distance += (a - b) ** 2
    
    # Return the square root of the sum of squared differences
    return math.sqrt(distance)

# Function to predict the location based on Euclidean distance
def predict_location(fingerprint_db, new_rssi):
    min_distance = float('inf')  # Initialize with a large number
    predicted_location = None

    # Loop through each reference location in the fingerprint database
    for location, rssi_values in fingerprint_db.items():
        distance = euclidean_distance(rssi_values, new_rssi)  # Compute the Euclidean distance
        if distance < min_distance:  # If this is the closest match so far
            min_distance = distance
            predicted_location = location

    return predicted_location

# Predict the location for the new RSSI values
predicted_location = predict_location(fingerprint_db, new_rssi)

print(f"The predicted location is: {predicted_location}")
