def empSalary(base):
    gross_sal = base + base*0.2 + base*0.5
    print("Gross Salary: ", gross_sal)
    total_deducitons = ((base * 0.12) + (gross_sal * 0.10))
    print("Toatal Deductions: ", total_deducitons)
    net_sal = (gross_sal - total_deducitons)
    print("Net Salary: ", net_sal)

base = int(input("Enter the base salary: "))
empSalary(base) 