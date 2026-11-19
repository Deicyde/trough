# The VCVio Library

This library provides a formal framework for reasoning about computations that make *oracle queries*. Many cryptographic primitives and interactive protocols use oracles to model (or simulate) external functionality such as random responses, coin flips, or more structured queries. The VCVio library "lifts" these ideas into a setting where both the abstract specification and concrete simulation of oracles may be studied, and their probabilistic behavior analyzed.

The main ingredients of the library are as follows:

- [Specification of Oracles](def-oracle-spec.md)
- [Standard Oracle Specifications](def-standard-oracle-specs.md)

We often require extra properties of query and answer types, such as decidable equality or finiteness. These are stated as ordinary instance hypotheses on the index type and on `spec.Range t` (quantified over $t$), rather than as bundled classes on the specification.

- [Oracle Computation](def-oracle-computation.md)
- [Handling Oracle Queries](def-handling-oracle-queries.md)
- [Probabilistic Semantics of Oracle Computations](def-probabilistic-semantics-of-oracle-computatio.md)
- [Simulating Oracle Queries with Other Oracles](def-sim-oracle.md)
- [Logging & Caching Oracle Queries](def-logging-caching-oracle-queries.md)
- [Random Oracle](def-random-oracle.md)
