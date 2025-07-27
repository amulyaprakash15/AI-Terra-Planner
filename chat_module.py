def get_bot_response(query):
    query = query.lower()
    if "flood" in query:
        return "To address flood risks, allocate 20–30% of the area to green buffers and stormwater zones."
    elif "heat" in query:
        return "For urban heat reduction, increase green spaces and reflective building materials."
    elif "traffic" in query:
        return "Use transit-oriented layouts and ensure proper road-network zoning."
    elif "green area" in query:
        return "We recommend 15–25% green space for sustainability in both city and village plans."
    else:
        return "I'm still learning. Try asking about floods, heat, traffic, or green areas."
    pie_path = os.path.join(os.getcwd(), pie_path)