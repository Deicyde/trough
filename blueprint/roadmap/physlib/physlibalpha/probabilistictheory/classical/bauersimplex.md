---
declaration: module
origin: cited
lean: ProbabilisticTheory.PureState.hasPureDecomposition, ProbabilisticTheory.isSimplexStateSpace_iff_ensemblesRefine_of_isClosed, ProbabilisticTheory.isBauerSimplexStateSpace_iff
statement: formalized
proof: formalized
---

# Bauer simplices

The module `PhyslibAlpha.ProbabilisticTheory.Classical.BauerSimplex`, [PhyslibAlpha/ProbabilisticTheory/Classical/BauerSimplex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BauerSimplex.lean): 3 declarations, 3 with a docstring.

> The state space is a Bauer simplex exactly when ensembles refine and pure states are closed.

## i. Overview

> A Bauer simplex is a classical state space whose pure states form a closed set. The pure states
> are then a compact phase space, and observables become continuous functions on it.
>
> Closed pure states already give every state a pure decomposition. A state is a positive
> functional on the observables. The M. Riesz extension theorem extends it to a positive functional
> on all continuous functions on the pure states, and the Riesz–Markov–Kakutani theorem turns that
> into a probability measure. Together with the uniqueness of pure decompositions, the state space
> is a Bauer simplex exactly when ensembles refine and the pure states are closed.

## ii. Key results

> - `PureState.hasPureDecomposition` proves that, with compact pure states, every state has a pure
>   decomposition.
> - `isSimplexStateSpace_iff_ensemblesRefine_of_isClosed` proves that, with closed pure states, the
>   system is classical exactly when ensembles refine.
> - `isBauerSimplexStateSpace_iff` proves that the state space is a Bauer simplex exactly when
>   ensembles refine and the pure states are closed.

## iv. References

> - E. M. Alfsen, *Compact Convex Sets and Boundary Integrals*, Springer, 1971, ch. II.4.

## A. Pure decompositions

**`ProbabilisticTheory.PureState.hasPureDecomposition`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BauerSimplex.lean#L64).

> With closed pure states, every state decomposes into pure states.

```lean
lemma PureState.hasPureDecomposition [CompactSpace (PureState E)] (ω : 𝓢[ℝ, E]) :
    ω.HasPureDecomposition
```

## B. Bauer simplices

**`ProbabilisticTheory.isSimplexStateSpace_iff_ensemblesRefine_of_isClosed`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BauerSimplex.lean#L76).

> With closed pure states, the state space is a simplex exactly when ensembles refine.

```lean
lemma isSimplexStateSpace_iff_ensemblesRefine_of_isClosed
    (hP : IsClosed {ω : stateSpace E | (toState ω).IsPure}) :
    IsSimplexStateSpace E ↔ EnsemblesRefine E
```

**`ProbabilisticTheory.isBauerSimplexStateSpace_iff`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BauerSimplex.lean#L85).

> **Bauer simplices**: the state space is a Bauer simplex exactly when ensembles refine and the
> pure states are closed.

```lean
lemma isBauerSimplexStateSpace_iff : IsBauerSimplexStateSpace E ↔
    EnsemblesRefine E ∧ IsClosed {ω : stateSpace E | (toState ω).IsPure}
```

## Depends on

- [Refinement of ensembles](ensemblerefinement.md)

## Proof depends on

- [Positive functionals are integrals](../../mathematics/part-02/measuretheory/positivefunctionalintegral.md)
- [Uniqueness of pure decompositions](uniquedecomposition.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/BauerSimplex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/BauerSimplex.lean)
