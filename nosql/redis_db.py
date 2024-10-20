import redis

# Create a connection to Redis cluster
r = redis.Redis(
  	host="localhost",
    port=6379,
    decode_responses=True
  )


# Store the city key-value pair
redis_conn.set("city", "London")

# Store the sunshine key-value pair
redis_conn.set("sunshine", 7)

# Retrieve values stored at the city and sunshine keys
city = redis_conn.get("city")
sunshine = redis_conn.get("sunshine")

print(city)
print(sunshine)


# Loop through each of the cities
for city in cities:
	# Grab the temperature
    temperature = redis_conn.get(f"{city}_temp")
    
    # Check if the temperature is None
    if temperature is None:
    	# Store an unknown temperature
        redis_conn.set(f"{city}_temp", "unknown temperature")
        print(f"Unknown temperature in {city}")
    
    else:
      	# Otherwise, print the temperature
    	print(f"The temperature in {city} is {temperature}")



# Create a dictionary containing weather data
london_weather_mapping = {
	"temperature": 42,
	"humidity": 88,
	"visibility": "low"
}

# Store the london_weather key-value pair
redis_conn.hset(
    "london_weather",
	mapping=london_weather_mapping
)

# Retrieve and print the london_weather key-value pair
print(redis_conn.hgetall("london_weather"))


