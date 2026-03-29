import g4f

providers = [
    g4f.Provider.AnyProvider,
    g4f.Provider.ApiAirforce,
]

models = [
    ("gpt_4", g4f.models.gpt_4),
    ("gpt_4o", g4f.models.gpt_4o),
]

for provider in providers:
    for model_name, model_obj in models:
        try:
            print(f"Testing {provider.__name__} with {model_name}...")
            response = g4f.ChatCompletion.create(
                model=model_obj,
                messages=[{"role": "user", "content": "hi"}],
                provider=provider
            )
            if response:
                print(f"  SUCCESS: {provider.__name__} works with {model_name}")
            else:
                print(f"  FAILED: {provider.__name__} with {model_name} returned empty")
        except Exception as e:
            print(f"  FAILED: {provider.__name__} with {model_name} error: {e}")
