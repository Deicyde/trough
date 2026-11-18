# FLP

8 modules under `Cslib/Computability/Distributed/FLP/`, with 116 public declarations.

Its [README](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/README.md) opens:

> This directory contains a formalization of Völzer's proof [Volzer2004] of the famous result in
> distributed computing, first proved by Fischer, Lynch and Paterson [FLP1985], that asynchronous
> distributed consensus is impossible in the presence of even a single crash fault.

- [Distributed algorithms for solving the consensus problem](algorithm.md)
- [Reachability via a subset of processes](canreachvia.md)
- [Fault-tolerant consensus](consensus.md)
- [Machinery for constructing infinite fair executions](fairscheduler.md)
- [Impossibility of asynchronous distributed consensus in the presence of a single fault](impossibility.md)
- [1-tolerant pseudo-consensus](onepseudoconsensus.md)
- [Fault-tolerant pseudo-consensus](pseudoconsensus.md)
- [Asynchronous distributed consensus in the absence of faults](zeroconsensus.md)
