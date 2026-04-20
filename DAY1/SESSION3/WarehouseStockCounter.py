def warehouseStockCounter(n, deliveries):
    print("Total: ", sum(deliveries))
    print("Average: ", (sum(deliveries))/n)

warehouseStockCounter(3, [50, 30, 20])
warehouseStockCounter(5, [10, 20, 30, 40, 50])