import functools

# Inputs
LAST_NAME = "ADONIS"
SEED_NUM = 8
FAVORITE_ARTIST = "DANIEL CAESAR"

# 4. Decorator to record execution
def log_diagnostic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG]: Executing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

# 1. Generate equipment readings based on inputs
readings = [
    len(LAST_NAME) * 10,      # 60
    SEED_NUM * 5,             # 40
    len(FAVORITE_ARTIST) * 3,  # 39
    "INVALID_READING"         # Invalid entry to demonstrate fault tolerance
]

# 2 & 3. Validation function with exception handling
@log_diagnostic
def validate_readings(data):
    valid_data = []
    for val in data:
        try:
            valid_data.append(float(val))
        except (ValueError, TypeError):
            print(f"[WARNING]: Skipped invalid entry -> '{val}'")
    return valid_data

# Calculation function
@log_diagnostic
def calculate_metrics(valid_data):
    if not valid_data:
        return 0, 0
    avg_val = sum(valid_data) / len(valid_data)
    peak_val = max(valid_data)
    return round(avg_val, 2), peak_val

# Classification function
@log_diagnostic
def classify_condition(avg_val):
    if avg_val > 50:
        return "OPTIMAL"
    elif avg_val >= 30:
        return "NORMAL"
    else:
        return "CRITICAL"

# Execute System
valid_readings = validate_readings(readings)
avg_reading, peak_reading = calculate_metrics(valid_readings)
status = classify_condition(avg_reading)

# 5. Display Summary Output
print("\n" + "="*40)
print(f"EQUIPMENT DIAGNOSTIC REPORT: {LAST_NAME}")
print("="*40)
print(f"Average Reading: {avg_reading}")
print(f"Peak Reading:    {peak_reading}")
print(f"Status:          {status}")
print("="*40)