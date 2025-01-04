try:
    x = 1 / 1
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Execution continues.")
