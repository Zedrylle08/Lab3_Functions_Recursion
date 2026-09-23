# Inputs
LAST_NAME = "ADONIS"
SEED_NUM = 8
FAVORITE_ARTIST = "DANIEL CAESAR"

# 1. Generate student-specific fault code
# Initial fault value based on inputs
initial_fault = (len(LAST_NAME) * 10) + SEED_NUM + len(FAVORITE_ARTIST)  # 60 + 8 + 13 = 81

# 2, 3, & 4. Recursive fault trace function with step counter & logger
def trace_fault(fault_code, depth=0):
    print(f"[LOG]: Level {depth} -> Tracing fault code: {fault_code}")
    
    # Base condition: stop when fault code drops to 10 or below
    if fault_code <= 10:
        print(f"[LOG]: Base condition reached at level {depth}.")
        return [fault_code], depth
    
    # Recursive step: reduce fault code (divide by 2 using integer division)
    next_fault = fault_code // 2
    sub_trace, total_depth = trace_fault(next_fault, depth + 1)
    
    return [fault_code] + sub_trace, total_depth

# 5. Execute system
trace_results, total_calls = trace_fault(initial_fault)

# Print Final Output
print("\n" + "="*40)
print(f"RECURSIVE FAULT TRACE REPORT: {LAST_NAME}")
print("="*40)
print(f"Initial Fault Code: {initial_fault}")
print(f"Recursive Sequence: {trace_results}")
print(f"Total Call Depth:   {total_calls}")
print(f"Final Status:       RESOLVED")
print("="*40)