---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.gardingVectorAt_iteratedKernel_mem_stoneCandidateDomain, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_gardingVectorAt_iteratedKernel, ProbabilisticTheory.QuantumMechanics.analyticGardingVector_isAnalyticVector
statement: formalized
proof: formalized
---

# Gårding vectors are analytic

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.GardingVectorWitness`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectorWitness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectorWitness.lean): 3 declarations, 3 with a docstring.

> Gårding vectors are analytic vectors of the candidate generator.

## i. Overview

> Applying the candidate generator `n` times to a Gårding vector gives, up to a power of `i`, the
> Gårding vector of the `n`-th derivative of the heat kernel. Its norm is at most `‖ψ‖ C^(n + 1)
> √(n!)`, so every Gårding vector is an analytic vector of the candidate generator.

## ii. Key results

> - `analyticGardingVector_isAnalyticVector` : Gårding vectors are analytic vectors.

## iv. References

> * None.

## A. The generator on iterated-kernel Gårding vectors

**`ProbabilisticTheory.QuantumMechanics.gardingVectorAt_iteratedKernel_mem_stoneCandidateDomain`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectorWitness.lean#L63).

> Domain membership of the `n`-th iterated-kernel Gårding vector, derived (not assumed) from the
> differentiability of its orbit — the same pattern as
> `analyticGardingVector_mem_stoneCandidateDomain`, one order at a time.

```lean
lemma gardingVectorAt_iteratedKernel_mem_stoneCandidateDomain
    (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H)) (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ))
    (n : ℕ) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    gardingVectorAt U (iteratedDeriv n (gaussianKernel ε)) ψ ∈
      (stoneCandidateGenerator (U := U) hUmul).domain
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_gardingVectorAt_iteratedKernel`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectorWitness.lean#L74).

> The commutation identity at every order: applying `stoneCandidateGenerator` to `Gₙ` gives (up
> to the factor `I`) `Gₙ₊₁`. Exactly `stoneCandidateGenerator_analyticGardingVector`'s proof, one
> order at a time.

```lean
lemma stoneCandidateGenerator_gardingVectorAt_iteratedKernel
    (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H)) (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ))
    (n : ℕ) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    stoneCandidateGenerator (U := U) hUmul
        ⟨gardingVectorAt U (iteratedDeriv n (gaussianKernel ε)) ψ,
          gardingVectorAt_iteratedKernel_mem_stoneCandidateDomain hUmul hUunit hUcont n hε ψ⟩ =
      (Complex.I : ℂ) • gardingVectorAt U (iteratedDeriv (n + 1) (gaussianKernel ε)) ψ
```

## B. Analyticity of Gårding vectors

**`ProbabilisticTheory.QuantumMechanics.analyticGardingVector_isAnalyticVector`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectorWitness.lean#L111).

> **Gårding vectors are analytic vectors** of the candidate generator.

```lean
lemma analyticGardingVector_isAnalyticVector (hUunit : ∀ t, U t ∈ unitary (H →L[ℂ] H))
    (hUcont : ∀ ξ : H, Continuous (fun t : ℝ => U t ξ)) {ε : ℝ} (hε : 0 < ε) (ψ : H) :
    (stoneCandidateGenerator (U := U) hUmul).IsAnalyticVector (analyticGardingVector U ε ψ)
```

## Depends on

- [Analytic vectors](../part-02/unbounded-analyticvector-basic.md)
- [Gårding vectors](unbounded-existence-gardingvectors.md)
- [Gårding vectors of smooth kernels](unbounded-existence-genericgardingkernel.md)

## Proof depends on

- [Pointwise bounds on the derivatives of the heat kernel](unbounded-existence-iteratedkernelgrowth.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectorWitness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/GardingVectorWitness.lean)
