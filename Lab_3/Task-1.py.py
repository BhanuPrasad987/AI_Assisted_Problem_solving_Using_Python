
# TGNPDCL Electricity Bill Generator
#
# Objective: Generate bill identical to official TGNPDCL format


def generate_tgnpdcl_bill():
    print("\n TGNPDCL Electricity Bill Generator ")
    print("Enter the details as per your bill slip\n")

    # ---- Input Section ----
    prev_kwh = float(input("Previous Reading (kWh): "))
    curr_kwh = float(input("Current Reading (kWh): "))
    pu = float(input("Price per Unit (₹): "))#Price Per Unit(PU) = Energy Charges(EC) / Units Consumed
    fc = float(input("Fixed Charges (₹): "))
    cc = float(input("Customer Charges (₹): "))
    ed_rate = float(input("Electricity Duty Rate (%): "))#ed_rate=(Electricity Duty(ED) / Energy Charges(EC)) * 100
    interest_on_ed = float(input("Interest on ED (₹): "))
    surcharge = float(input("Surcharge (₹): "))
    acd_surcharge = float(input("ACD Surcharge (₹): "))
    fsa_fca = float(input("FSA/FCA Charges (₹): "))
    adjustment = float(input("Adjustment (₹): "))
    loss_gain = float(input("Loss/Gain (₹): "))
    cus_type = input("Customer Type (Domestic/Commercial/Industrial): ").strip().lower()

    # ---- Calculations ----
    kwh_units = curr_kwh - prev_kwh
    ec = kwh_units * pu
    ed = ec * (ed_rate / 100)

    subtotal = ec + fc + cc + ed + interest_on_ed + surcharge + acd_surcharge + fsa_fca + adjustment + loss_gain
    total_bill = round(subtotal)

    # ---- Output Section ----
    print("\n-------------------------------------------")
    print("           TGNPDCL ELECTRICITY BILL         ")
    print("-------------------------------------------")
    print(f"Customer Type        : {cus_type.capitalize()}")
    print(f"Previous Reading (kWh): {prev_kwh}")
    print(f"Current Reading  (kWh): {curr_kwh}")
    print(f"KWH Units Consumed    : {kwh_units:.0f}")
    print("-------------------------------------------")
    print(f"Energy Charges (EC)   : ₹{ec:.2f}")
    print(f"Fixed Charges (FC)    : ₹{fc:.2f}")
    print(f"Customer Charges (CC) : ₹{cc:.2f}")
    print(f"Electricity Duty (ED) : ₹{ed:.2f}")
    print(f"Interest on ED        : ₹{interest_on_ed:.2f}")
    print(f"Surcharge             : ₹{surcharge:.2f}")
    print(f"ACD Surcharge         : ₹{acd_surcharge:.2f}")
    print(f"FSA/FCA Charges       : ₹{fsa_fca:.2f}")
    print(f"Adjustment            : ₹{adjustment:.2f}")
    print(f"Loss/Gain             : ₹{loss_gain:.2f}")
    print("-------------------------------------------")
    print(f" Total Bill Amount   : ₹{total_bill:.2f}")
    print("-------------------------------------------")
# ---- Run the Program ----
generate_tgnpdcl_bill()
# Note: This code assumes that the user inputs valid numeric values for readings and a valid customer type.