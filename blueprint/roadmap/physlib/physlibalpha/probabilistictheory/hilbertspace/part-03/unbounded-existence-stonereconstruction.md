---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.stoneReconstructionSpectralMeasure, ProbabilisticTheory.QuantumMechanics.stoneReconstructionData, ProbabilisticTheory.QuantumMechanics.stoneReconstructionUnitaryGroup, ProbabilisticTheory.QuantumMechanics.hasDerivAt_generator_unique, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_reconstruction_of_mem_domain, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_domain_dense, ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_reconstruction
statement: formalized
proof: formalized
---

# Stone's theorem: reconstruction of the group

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.StoneReconstruction`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean): 7 declarations, 7 with a docstring.

> Stone's theorem, reconstruction: a unitary group is exp(i t T) for its generator.

## i. Overview

> Let `T` be the candidate generator of a strongly continuous unitary group `U`, and `V t = exp(i t
> T)` the unitary group of the spectral measure of its closure. For `x` in the domain of `T`, the
> orbits `U t x` and `V t x` solve the same equation `w' = i T w` with the same initial value. Since
> `T` is symmetric, `‖U t x - V t x‖²` has zero derivative, so the orbits agree. The domain is dense,
> so `U = V`.

## ii. Key results

> - `stoneReconstructionUnitaryGroup` : the group `exp(i t T)` of the generator.
> - `stoneCandidateGenerator_domain_dense` : the domain of the candidate generator is dense.
> - `stoneCandidateGenerator_reconstruction` : **Stone's theorem, reconstruction**: `U t = exp(i t
>   T)`.

## iv. References

> * None.

## A. The reconstructed unitary group

**`ProbabilisticTheory.QuantumMechanics.stoneReconstructionSpectralMeasure`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean#L71).

> The Cayley-transform spectral measure for `stoneCandidateGenerator hUmul`'s essential
> self-adjoint closure.

```lean
noncomputable def stoneReconstructionSpectralMeasure : WOTSpectralMeasure ℝ H
```

**`ProbabilisticTheory.QuantumMechanics.stoneReconstructionData`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean#L78).

> The domain-aware spectral theorem for `stoneCandidateGenerator hUmul`'s closure, built via the
> Cayley transform from this Track's essential self-adjointness result.

```lean
lemma stoneReconstructionData :
    DomainAwareSelfAdjointSpectralTheorem (stoneCandidateGenerator (U := U) hUmul).closure
      (stoneReconstructionSpectralMeasure hU0 hUmul hUunit hUcont)
```

**`ProbabilisticTheory.QuantumMechanics.stoneReconstructionUnitaryGroup`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean#L86).

> The unitary group `exp(i t T)` of the closure of the candidate generator.

```lean
noncomputable def stoneReconstructionUnitaryGroup (t : ℝ) : H →L[ℂ] H
```

## B. Uniqueness for the evolution equation

**`ProbabilisticTheory.QuantumMechanics.hasDerivAt_generator_unique`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean#L103).

> Two curves through the same starting point, both solving `w' = i • T w` while remaining in
> `T`'s domain, coincide everywhere: the standard Schrödinger-equation uniqueness argument, using
> only that `T` is symmetric (so `⟪w, T w⟫` is real, killing the cross terms in `d/dt‖w‖²`).

```lean
lemma hasDerivAt_generator_unique {y z : ℝ → H} (hTsym : T.IsSymmetric)
    (hy_mem : ∀ t, y t ∈ T.domain) (hz_mem : ∀ t, z t ∈ T.domain)
    (hy_deriv : ∀ t, HasDerivAt y (Complex.I • T ⟨y t, hy_mem t⟩) t)
    (hz_deriv : ∀ t, HasDerivAt z (Complex.I • T ⟨z t, hz_mem t⟩) t)
    (h0 : y 0 = z 0) : ∀ t, y t = z t
```

## C. Reconstruction of the group

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_reconstruction_of_mem_domain`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean#L160).

> **Stone's theorem, reconstruction direction.** `U` agrees with the concrete unitary group
> `stoneReconstructionUnitaryGroup` on every vector in `stoneCandidateGenerator hUmul`'s domain.

```lean
lemma stoneCandidateGenerator_reconstruction_of_mem_domain
    (x : (stoneCandidateGenerator (U := U) hUmul).domain) (t : ℝ) :
    U t (x : H) = stoneReconstructionUnitaryGroup hU0 hUmul hUunit hUcont t (x : H)
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_domain_dense`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean#L219).

> The domain of the candidate generator is dense.

```lean
lemma stoneCandidateGenerator_domain_dense :
    Dense ((stoneCandidateGenerator (U := U) hUmul).domain : Set H)
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_reconstruction`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean#L237).

> **Stone's theorem.** A strongly continuous unitary group is `exp(i t T)` for the closure `T` of
> its candidate generator.

```lean
lemma stoneCandidateGenerator_reconstruction (x : H) (t : ℝ) :
    U t x = stoneReconstructionUnitaryGroup hU0 hUmul hUunit hUcont t x
```

## Depends on

- [The spectral measure of the Cayley transform](unbounded-cayleyspectraldata-basic.md)
- [Stone's theorem: existence of the generator](unbounded-existence-stonegenerator.md)
- [The spectral theorem, stated](../part-02/unbounded-selfadjointspectraltheorem.md)

## Proof depends on

- [The spectral theorem for unbounded self-adjoint operators](unbounded-cayleyspectraldata-spectheorem.md)
- [The unitary group preserves the domain of its generator](unbounded-existence-generatorinvariance.md)
- [The unitary group preserves the domain of its generator](unbounded-flow-stoneinvariance.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/StoneReconstruction.lean)
