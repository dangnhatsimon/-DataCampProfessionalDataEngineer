def create_list():
    return [i for i in range(1000)]
def create_set():
    return set([i for i in range(1000)])
def find(it, el=50):
    return el in it

# Write the performance test for a list
def test_list(benchmark):
    benchmark(find, it=create_list())

# Write the performance test for a set
def test_set(benchmark):
    benchmark(find, it=create_set())




def test_list(benchmark):
	# Add decorator here
    @benchmark
    def iterate_list():
		# Complete the loop here
        for benchmark in [i for i in range(1000)]:
            pass

def test_set(benchmark):
	# Add decorator here
    @benchmark
    def iterate_set():
        # Complete the loop here
        for benchmark in {i for i in range(1000)}:
            pass