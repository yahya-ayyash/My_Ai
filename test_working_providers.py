import g4f

providers = [
    g4f.Provider.ApiAirforce,
    g4f.Provider.ItalyGPT,
    g4f.Provider.OperaAria,
    g4f.Provider.PollinationsAI,
    g4f.Provider.GlhfChat,
    g4f.Provider.LMArena
]

def test_p(p, m):
    try:
        print(f"Testing {p.__name__} with {m}...")
        resp = g4f.ChatCompletion.create(model=m, messages=[{'role': 'user', 'content': 'hi'}], provider=p)
        if resp and len(resp.strip()) > 0:
            return f"{p.__name__} with {m}: SUCCESS - {resp[:50]}..."
    except Exception as e:
        return f"{p.__name__} with {m}: FAILED - {str(e)[:100]}"
    return f"{p.__name__} with {m}: NO RESPONSE"

for p in providers:
    # Use gpt-4o as default, except for PollinationsAI where we try 'gemini'
    model = "gpt-4o"
    if p == g4f.Provider.PollinationsAI:
        model = "gemini"
    
    res = test_p(p, model)
    print(f"  {res}")
