---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Ballot.ballot_problem
mathlib_file: Archive/Wiedijk100Theorems/BallotProblem.lean
---

# The Ballot Problem

The ballot problem.

```lean
Ballot.ballot_problem (q p : ℕ) :
  q < p →
    (ProbabilityTheory.uniformOn (Ballot.countedSequence p q)) Ballot.staysPositive =
      (↑p - ↑q) / (↑p + ↑q)
```

## Depends on

- [Conditional probability](../../overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [Counting measure](../../undergraduate/measures-and-integral-calculus/measure-theory/counting-measure.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Almost sure convergence](../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Cantor’s Theorem](../part-04/cantors-theorem.md)
- [Cardinal](../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closure](../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of monotone functions](../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Open map](../../overview/topology/general-topology/part-01/open-map.md)
- [Probability measure](../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Schroeder-Bernstein Theorem](schroeder-bernstein-theorem.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Ballot.ballot_problem`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BallotProblem.html#Ballot.ballot_problem)
- [Source of `Ballot.ballot_problem` in Archive/Wiedijk100Theorems/BallotProblem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BallotProblem.lean#L347)
- [Freek Wiedijk's 100 theorems, no. 30](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L150)
- [1000+ theorems list: Q2253746](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2127)
- [1000+ theorems project: Q2253746](https://1000-plus.github.io/?length=-1#Q2253746)
- [Wikipedia: Bertrand's ballot theorem](https://en.wikipedia.org/wiki/Bertrand's_ballot_theorem)
- [Wikidata: Q2253746](https://www.wikidata.org/wiki/Q2253746)
