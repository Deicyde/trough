---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_denseAnalyticVectors, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_isEssentiallySelfAdjoint
statement: formalized
proof: formalized
---

# Stone's theorem: existence of the generator

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.StoneGenerator`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneGenerator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneGenerator.lean): 2 declarations, 2 with a docstring.

> Stone's theorem, existence: the candidate generator is essentially self-adjoint.

## i. Overview

> The Gårding vectors of a strongly continuous unitary group are analytic vectors of its candidate
> generator and are dense. By Nelson's theorem the candidate generator is essentially self-adjoint.

## ii. Key results

> - `stoneCandidateGenerator_denseAnalyticVectors` : the analytic vectors of the candidate generator
>   are dense.
> - `stoneCandidateGenerator_isEssentiallySelfAdjoint` : **Stone's theorem, existence**: the candidate
>   generator is essentially self-adjoint.

## iv. References

> * None.

## A. Density of analytic vectors

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_denseAnalyticVectors`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneGenerator.lean#L65).

> **The analytic vectors of the candidate generator are dense**: every vector is a limit of
> Gårding vectors.

```lean
lemma stoneCandidateGenerator_denseAnalyticVectors (hU0 : U 0 = 1)
    (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H)) (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) :
    (Submodule.span ℂ
      {x : H | (stoneCandidateGenerator (U := U) hUmul).IsAnalyticVector x}).topologicalClosure =
      (⊤ : Submodule ℂ H)
```

## B. Essential self-adjointness

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_isEssentiallySelfAdjoint`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneGenerator.lean#L88).

> **Stone's theorem, existence.** The candidate generator of a strongly continuous unitary group
> is essentially self-adjoint.

```lean
lemma stoneCandidateGenerator_isEssentiallySelfAdjoint (hU0 : U 0 = 1)
    (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H)) (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) :
    (stoneCandidateGenerator (U := U) hUmul).IsEssentiallySelfAdjoint
```

## Depends on

- [Analytic vectors](../part-02/unbounded-analyticvector-basic.md)
- [The candidate generator of a unitary group](unbounded-existence-candidategenerator.md)

## Proof depends on

- [Nelson's analytic-vector theorem](../part-02/unbounded-analyticvector-nelson.md)
- [Gårding vectors are analytic](unbounded-existence-gardingvectorwitness.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneGenerator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneGenerator.lean)
