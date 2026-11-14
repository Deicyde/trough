---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData, ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.closure_isSelfAdjoint, ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.closure_isClosed, ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.le_closure, ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.unique_selfAdjoint_extension, ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.ofDefectNumberEqZero, ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.ofDefectIndexCertificate, ProbabilisticTheory.QuantumMechanics.IsWeakSpectralResolution
statement: formalized
proof: formalized
---

# The spectral theorem, stated

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.SelfAdjointSpectralTheorem`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean): 24 declarations, 19 with a docstring.

> Essential self-adjointness and spectral resolutions of self-adjoint operators, with their domains.

## i. Overview

> An operator is essentially self-adjoint when its closure is self-adjoint; a self-adjoint extension
> is then unique. A spectral measure `μ` on `ℝ` resolves a self-adjoint operator `T` when `⟪y, T x⟫ =
> ∫ λ d⟪y, μ x⟫` for `x` in the domain of `T`, and it resolves `T` with its domain when in addition
> the domain of `T` is the set of vectors with `∫ λ² dμₓ < ∞`.

## ii. Key results

> - `SelfAdjointClosureData` : an operator with self-adjoint closure.
> - `SelfAdjointClosureData.unique_selfAdjoint_extension` : the self-adjoint extension is unique.
> - `IsWeakSpectralResolution` : `⟪y, T x⟫ = ∫ λ d⟪y, μ x⟫` on the domain of `T`.
> - `SelfAdjointSpectralTheorem` : a spectral measure weakly resolving a self-adjoint operator.
> - `spectralSquareMomentDomain` : the vectors with finite second moment.
> - `DomainAwareSelfAdjointSpectralTheorem` : a spectral measure resolving a self-adjoint operator
>   together with its domain.
> - `DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup` : the strongly continuous unitary
>   group attached to the spectral measure.

## iv. References

> * None.

## A. Essential self-adjointness and closure

> An operator is essentially self-adjoint when its closure is self-adjoint.

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData`**, a structure, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L67).

> The analytic input needed before applying the unbounded spectral theorem.

```lean
structure SelfAdjointClosureData
    (T : H →ₗ.[ℂ] H) where
  essentiallySelfAdjoint : LinearPMap.IsEssentiallySelfAdjoint T
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.closure_isSelfAdjoint`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L78).

> Essential self-adjointness makes the canonical closure self-adjoint.

```lean
lemma closure_isSelfAdjoint : IsSelfAdjoint T.closure
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.closure_isClosed`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L82).

> In particular, the canonical closure is closed.

```lean
lemma closure_isClosed : T.closure.IsClosed
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.le_closure`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L87).

> The core operator is contained in its canonical self-adjoint closure.

```lean
lemma le_closure : T ≤ T.closure
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.unique_selfAdjoint_extension`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L91).

> The canonical closure is the unique self-adjoint extension of the core.

```lean
lemma unique_selfAdjoint_extension {S : H →ₗ.[ℂ] H}
    (hTS : T ≤ S) (hS : IsSelfAdjoint S) : S = T.closure
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.ofDefectNumberEqZero`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L98).

> Build closure data from the von Neumann defect-number criterion.

```lean
lemma ofDefectNumberEqZero
    (hT : T.IsSymmetric)
    (hdense : T.HasDenseDomain)
    (hpos : T.defectNumber Complex.I = 0)
    (hneg : T.defectNumber (-Complex.I) = 0) :
    SelfAdjointClosureData T
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointClosureData.ofDefectIndexCertificate`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L108).

> Package the reusable defect-index certificate as closure data.

```lean
lemma ofDefectIndexCertificate {T : H →ₗ.[ℂ] H}
    (C : DefectIndexCertificate T) : SelfAdjointClosureData T
```

**`ProbabilisticTheory.QuantumMechanics.IsWeakSpectralResolution`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L116).

> The spectral measure `μ` resolves `T`: for `x` in the domain of `T` the identity is integrable
> against every `⟪y, μ x⟫`, and `⟪y, T x⟫ = ∫ λ d⟪y, μ x⟫`.

```lean
def IsWeakSpectralResolution
    (T : H →ₗ.[ℂ] H)
    (μS : WOTSpectralMeasure ℝ H) : Prop
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointSpectralTheorem`**, a structure, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L126).

> The self-adjoint operator is reconstructed from its spectral measure in the weak sense.
> The integrability clause is essential: the identity function is generally unbounded, so this
> cannot be replaced by the bounded PVM axioms alone.

```lean
structure SelfAdjointSpectralTheorem
    (T : H →ₗ.[ℂ] H)
    (μS : WOTSpectralMeasure ℝ H) where
  isSelfAdjoint : IsSelfAdjoint T
  reconstruction : IsWeakSpectralResolution T μS
```

### A.1. Spectral resolutions with domain

> A spectral resolution only describes the operator on its domain. Equality of unbounded operators
> also needs the domain to be the set of vectors of finite second moment.

**`ProbabilisticTheory.QuantumMechanics.spectralSquareMomentDomain`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L140).

> The vectors of finite second moment, `∫ λ² dμₓ < ∞`.

```lean
def spectralSquareMomentDomain
    (μS : WOTSpectralMeasure ℝ H) : Set H
```

**`ProbabilisticTheory.QuantumMechanics.mem_spectralSquareMomentDomain_iff`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L144).

```lean
lemma mem_spectralSquareMomentDomain_iff
    (μS : WOTSpectralMeasure ℝ H) (x : H) :
    x ∈ spectralSquareMomentDomain μS ↔
      Integrable (fun (r : ℝ) ↦ r ^ 2) (μS.diagonalMeasure x)
```

**`ProbabilisticTheory.QuantumMechanics.HasBoundedSpectralSupport`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L152).

> The spectral measure is supported in `[-C, C]`: it vanishes on every measurable set disjoint
> from it.

```lean
def HasBoundedSpectralSupport
    (μS : WOTSpectralMeasure ℝ H) (C : ℝ) : Prop
```

**`ProbabilisticTheory.QuantumMechanics.spectralSquareMomentDomain_eq_univ_of_boundedSupport`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L156).

```lean
lemma spectralSquareMomentDomain_eq_univ_of_boundedSupport
    (μS : WOTSpectralMeasure ℝ H) {C : ℝ}
    (hC : HasBoundedSpectralSupport μS C) :
    spectralSquareMomentDomain μS = Set.univ
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem`**, a structure, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L187).

> A spectral measure resolving the self-adjoint operator `T`, whose domain is the set of vectors
> of finite second moment.

```lean
structure DomainAwareSelfAdjointSpectralTheorem
    (T : H →ₗ.[ℂ] H)
    (μS : WOTSpectralMeasure ℝ H)
    extends SelfAdjointSpectralTheorem T μS where
  domain_eq_squareMoment : T.domain = spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.ofBoundedSupport`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L200).

> A spectral measure with bounded support that resolves `T` resolves it together with its domain.

```lean
lemma ofBoundedSupport (D : SelfAdjointSpectralTheorem T μS)
    (hdom : (T.domain : Set H) = Set.univ) {C : ℝ}
    (hC : HasBoundedSpectralSupport μS C) :
    DomainAwareSelfAdjointSpectralTheorem T μS
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.isSelfAdjoint_of`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L209).

> The self-adjointness part of a domain-aware spectral theorem.

```lean
lemma isSelfAdjoint_of (D : DomainAwareSelfAdjointSpectralTheorem T μS) :
    IsSelfAdjoint T
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.reconstruction_of`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L214).

> The weak reconstruction part of a domain-aware spectral theorem.

```lean
lemma reconstruction_of (D : DomainAwareSelfAdjointSpectralTheorem T μS) :
    IsWeakSpectralResolution T μS
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.mem_domain_iff`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L219).

> The domain is exactly the vectors with finite second spectral moment.

```lean
lemma mem_domain_iff (D : DomainAwareSelfAdjointSpectralTheorem T μS) (x : H) :
    x ∈ T.domain ↔ x ∈ spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L227).

> The strongly continuous unitary group attached to a domain-aware spectral theorem. Its strong
> Stone generator and exact generator domain are the remaining content of Stone's theorem's converse
> direction.

```lean
noncomputable def expUnitaryGroup
    (_D : DomainAwareSelfAdjointSpectralTheorem T μS) :
    WOTSpectralMeasure.StrongUnitaryOneParameterGroup H
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_zero`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L232).

```lean
lemma expUnitaryGroup_zero (D : DomainAwareSelfAdjointSpectralTheorem T μS) :
    D.expUnitaryGroup 0 = 1
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_add`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L236).

```lean
lemma expUnitaryGroup_add (D : DomainAwareSelfAdjointSpectralTheorem T μS) (t s : ℝ) :
    D.expUnitaryGroup (t + s) = D.expUnitaryGroup t * D.expUnitaryGroup s
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_continuous_apply`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L240).

```lean
lemma expUnitaryGroup_continuous_apply
    (D : DomainAwareSelfAdjointSpectralTheorem T μS) (x : H) :
    Continuous (fun t => D.expUnitaryGroup t x)
```

**`ProbabilisticTheory.QuantumMechanics.SelfAdjointSpectralTheorem.unitaryConj`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L254).

> Transport an unbounded spectral theorem through a Hilbert-space unitary. This is the
> representation-level engine: once the theorem is proved for a multiplication model, this
> constructor gives it for every unitarily equivalent self-adjoint operator.

```lean
lemma unitaryConj {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H']
    [CompleteSpace H'] (D : SelfAdjointSpectralTheorem T μS) (u : H ≃ₗᵢ[ℂ] H') :
    SelfAdjointSpectralTheorem (LinearPMap.unitaryConj u T)
      (WOTSpectralMeasure.unitaryConjSpectralMeasure u μS)
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.unitaryConj`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean#L290).

> Transport the domain-aware theorem through a Hilbert-space unitary. The only additional input
> beyond the weak transport is the diagonal-measure equivariance lemma, which makes the
> square-moment domain equivariant as well.

```lean
lemma unitaryConj {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H']
    [CompleteSpace H'] (D : DomainAwareSelfAdjointSpectralTheorem T μS)
    (u : H ≃ₗᵢ[ℂ] H') :
    DomainAwareSelfAdjointSpectralTheorem (LinearPMap.unitaryConj u T)
      (WOTSpectralMeasure.unitaryConjSpectralMeasure u μS)
```

## Depends on

- [Criteria for essential self-adjointness](unbounded-realanalytic.md)
- [The unitary group of a spectral measure](unbounded-stoneunitarygroup.md)
- [The vector-measure integral against a scalar matrix coefficient](unbounded-weakintegral.md)

## Proof depends on

- [Spectral theory for self-adjoint operators](../../../../physlib/quantummechanics/operators/spectraltheory/selfadjoint.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SelfAdjointSpectralTheorem.lean)
