import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
        

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"⏱ Execution time: {self.elapsed:.4f} seconds")


# Usage
with Timer():
    total = sum(range(10_000_000_000))
    print(f"Sum = {total}")