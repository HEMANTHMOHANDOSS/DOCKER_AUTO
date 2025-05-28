def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"\n[!] Error occurred: {e}")
        # Add retry, logging, or rollback logic if needed
