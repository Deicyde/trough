---
declaration: section
origin: cited
lean: OAI.FiniteCongruence.graph_criterion
statement: formalized
proof: formalized
---

# 206. Finite lattice representation and undecidability

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Some finite lattices are not congruence lattices of any finite algebra, answering the finite lattice representation problem negatively. Moreover, no algorithm decides whether a finite lattice has such a representation, or whether it is a full subgroup interval of a finite group.

## Finite congruence lattices: characterization and undecidability

We give an explicit colored-graph characterization of the finite nonempty lattices that occur as full congruence lattices of finite algebras, and prove that deciding this representation property is undecidable. In particular, the finite lattice representation problem has a negative answer. We also prove that recognition of full subgroup intervals in finite groups is undecidable.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## A negative solution to the finite lattice representation problem

We give a negative solution to the finite lattice representation problem. We prove that there is a finite nonempty lattice that is not the full congruence lattice of any finite nonempty algebra of any finite signature.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Negative-Solution-to-the-Finite-Lattice-Representation-Problem-September-24-2026/paper.pdf).

## The Lean formalization

The finite lattice representation problem asks which finite lattices occur as the full congruence lattice of a finite algebra. The formalization proves the paper's colored-graph characterization: a finite nonempty lattice is representable exactly when it admits the specified finite nonempty graph witness, whose edge colors encode the required congruence relations. This selected theorem is the equivalence with the graph criterion; the paper's undecidability and subgroup-interval conclusions are outside it.

## Lean: Colored-graph criterion for finite congruence lattices

```lean
theorem graph_criterion (Lat : Type) [Fintype Lat] [Lattice Lat] [OrderBot Lat] :
    Representable Lat ↔ HasGraphWitness Lat
```

Stated in [FiniteCongruenceGraph.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FiniteCongruenceGraph.lean#L57). Proved in [lean/OAI/Algebra/Universal/GraphCriterion.lean, line 291](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/Universal/GraphCriterion.lean#L291).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/206.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/206.md)
