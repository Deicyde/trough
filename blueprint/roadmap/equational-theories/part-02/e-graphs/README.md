# E-Graphs

For proving implications, we used another technique called equality saturation \[[Willsey et al. 2021](https://doi.org/10.1145/3434304)\] with the `lean-egg` tactic, to automatically construct proofs.

A similar approach is being pursued in the MagmaEgg tool as well, which is a standalone program that only supports magma equalities, while the lean-egg tactic supports any Lean expression.

- [lean-egg](lean-egg/README.md)
- [MagmaEgg](magmaegg/README.md)
