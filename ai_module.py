# ai_module.py

def generate_plan(data, mode):
    location = data.get("location", "Unknown Location")
    population = data.get("population", "N/A")
    terrain = data.get("terrain", "Unknown")
    resources = data.get("resources", "None")
    climate = data.get("climate", "Moderate")

    if mode == "city":
        return f"""
        🔷 **Smart City Development Plan**
        Location: {location}
        Population Estimate: {population}
        Terrain Type: {terrain}
        Climate: {climate}
        Key Available Resources: {resources}

        ✅ AI Recommendations:
        - Develop smart traffic and transport management.
        - Deploy AI-driven waste and water management systems.
        - Set up solar energy grids and green architecture.
        - Include public smart health hubs and education centers.
        - Use GIS & IoT for infrastructure optimization.
        """
    else:
        return f"""
        🌿 **Smart Village Development Plan**
        Location: {location}
        Population Estimate: {population}
        Terrain Type: {terrain}
        Climate: {climate}
        Key Available Resources: {resources}

        ✅ AI Recommendations:
        - Focus on clean water and sanitation AI monitoring.
        - Use precision farming and soil analysis tools.
        - Establish e-learning and telemedicine centers.
        - Utilize solar microgrids for energy independence.
        - Promote local economy with AI-based agri-market insights.
        """
