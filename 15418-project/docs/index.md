# PARALLEL ORDER MATCHING ENGINE

Team Members: Naman Mansukhani, Vincent Lin 

## URL
https://namanmansukhani.github.io/15418-project/site/ 

## SUMMARY
We are going to implement a trade matching engine, which involves implementing data structures for storing and matching orders, along with implementing a framework for interacting with the clients through TCP requests.
We will also implement simulated clients that keep sending orders to our matching engine.

## BACKGROUND
A stock exchange has to match incoming orders from different entities interacting in a market. This is typically done through a price-time priority matching. Our goal is to maximize the throughput of the matching engine by:

1. Optimizing data structure performance
2. Optimizing network throughput using techniques such asynchronous request processing

It might turn out that the network is too slow to actually test the throughput of the data structures. In this case, we will just simulate clients using threads on the same machines that send in requests after certain intervals.

## THE CHALLENGE
The challenges in this project include:
1. Correctness: A stock market needs to be fair and correct. The first challenge for this is implementing the lock free data structures.
2. Throughput: This project is going to involve researching about techniques to maximize
3. Simulating Realistic Network Conditions: We want to add realistic randomness for packet drops and latency. This would involve exploring relevant networking libraries.

## RESOURCES
We will be starting the codebase from scratch. We will implement the trading engine in C++, and the clients in Python. We will use existing Python libraries for sending requests to the C++ server, along with network tools to simulate packet drops and adding randomness in latency.

## GOALS AND DELIVERABLES

### Plan to achieve:
1. Implement a trade matching engine.
2. Implement lock free data structures/ fine-grained locking to optimize the matching engine.
3. Obtain a 5x speedup running on 16 threads.

### Hope to achieve:
1. Add realistic clients communicating through the network.
2. Add optimizations to the network side of things
4. Obtain a 50x improvement in network throughput over the sequential version, since network packets are small.

### Demo
We plan to show speedup graphs for different techniques that we apply to this problem.

### Learning Goals
We hope to learn more about implementing lock-free data structures and how performance sensitive applications optimize network performance.

### Performance Targets
We hope to scale the matching engine to 10000 orders matched per second.

## PLATFORM CHOICE
We will code the trade matching engine in C++ since this is a very performance critical application. We plan to run this on CPUs since we expect the code flow to be divergent and not suited for SIMD/GPU programming. We plan on testing our code on PSC nodes since we expect it to be easier to setup networking on multiple PSC nodes.

## SCHEDULE

#### Week 1:

Research topic background and finalize specific implementation details and design choices. Implement a sequential version of the order matching engine.

#### Week 2:
	
Implement lock-free data structures. Create a functional exchange. Implement fake local clients.

#### Week 3:
	
Implement clients and network. Run simulated tests to optimize parameters for parallelization.

#### Week 4:

Focus on completing the writeup and poster demo for the project.
