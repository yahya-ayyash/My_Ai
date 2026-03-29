import g4f

providers = [
    g4f.Provider.ApiAirforce,
    g4f.Provider.PollinationsAI,
    g4f.Provider.DeepInfra,
]

# Check if gemini_2_0_flash exists in g4f.models
try:
    model = g4f.models.gemini_2_0_flash
    print(f"DEBUG: Found gemini_2_0_flash in g4f.models")
except AttributeError:
    model = "gemini-2.0-flash"
    print(f"DEBUG: gemini_2_0_flash NOT in g4f.models, using string name")

for provider in providers:
    try:
        p_name = getattr(provider, '__name__', 'Unknown')
        print(f"Testing {p_name} with {model}...")
        response = g4f.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": "hi"}],
            provider=provider
        )
        if response:
            print(f"  SUCCESS: {p_name} works")
        else:
            print(f"  FAILED: {p_name} returned empty")
    except Exception as e:
        print(f"  FAILED: {p_name} error: {e}")
