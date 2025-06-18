Flights = {
    ("AA123","NYC", "LAX", 360),
    ("BA456","LAX", "CHI",270),
    ("CA789","CHI", "NYC", 120),
    ("DA012","NYC", "MIA", 180),
    ("EA345", "MIA", "LAX", 330),

}
#Print all flights organising from NYC
#sort flights by duration (sort to long) and print the sorted list
#find the flight with the longest duration.
nyc_flights=[f for f in Flights if f[1] == "NYC"]
print("flight from NYC:")
for flight in nyc_flights:
    print(flight)