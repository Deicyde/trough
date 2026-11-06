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

## Proof depends on

- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Order](../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Probability measure](../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `Ballot.ballot_problem`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BallotProblem.html#Ballot.ballot_problem)
- [Source of `Ballot.ballot_problem` in Archive/Wiedijk100Theorems/BallotProblem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BallotProblem.lean#L347)
- [Freek Wiedijk's 100 theorems, no. 30](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L150)
- [1000+ theorems list: Q2253746](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2127)
- [1000+ theorems project: Q2253746](https://1000-plus.github.io/all.html?length=-1#Q2253746)
- [Wikipedia: Bertrand's ballot theorem](https://en.wikipedia.org/wiki/Bertrand's_ballot_theorem)
- [Wikidata: Q2253746](https://www.wikidata.org/wiki/Q2253746)
