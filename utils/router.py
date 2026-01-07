from config import MODEL_CONFIG


def choose_models(task_type):
    if task_type == "Coding":
        return ["openai", "geminiai"]
    elif task_type == "Fast Response":
        return ["geminiai"]
    elif task_type == "Cost Saving":
        return ["llama", "geminiai"]
    else:
        return ["openai", "geminiai", "llama"]
