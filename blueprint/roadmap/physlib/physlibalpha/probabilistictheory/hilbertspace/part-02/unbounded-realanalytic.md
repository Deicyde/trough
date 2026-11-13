---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.DefectIndexCertificate, ProbabilisticTheory.QuantumMechanics.DefectIndexCertificate.essentiallySelfAdjoint, ProbabilisticTheory.QuantumMechanics.DefectIndexCertificate.closure_isSelfAdjoint, ProbabilisticTheory.QuantumMechanics.ofSelfAdjoint_isEssentiallySelfAdjoint, ProbabilisticTheory.QuantumMechanics.isEssentiallySelfAdjoint_of_hilbertBasis_eigenvectors
statement: formalized
proof: formalized
---

# Criteria for essential self-adjointness

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.RealAnalytic`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean): 5 declarations, 3 with a docstring.

> Criteria for essential self-adjointness: trivial deficiency spaces, eigenbases.

## i. Overview

> A densely defined symmetric operator is essentially self-adjoint when both deficiency spaces are
> trivial. In particular a symmetric operator whose domain is the span of a Hilbert basis of
> eigenvectors with real eigenvalues is essentially self-adjoint.

## ii. Key results

> - `DefectIndexCertificate` : a densely defined symmetric operator with trivial deficiency spaces.
> - `DefectIndexCertificate.essentiallySelfAdjoint` : such an operator is essentially self-adjoint.
> - `isEssentiallySelfAdjoint_of_hilbertBasis_eigenvectors` : an operator diagonal in a Hilbert basis
>   with real eigenvalues is essentially self-adjoint.

## iv. References

> * Reed–Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*,
>   Theorem VIII.3.

## A. Von Neumann's defect criterion

**`ProbabilisticTheory.QuantumMechanics.DefectIndexCertificate`**, a structure, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean#L55).

> A densely defined symmetric operator whose deficiency spaces at `± i` are trivial.

```lean
structure DefectIndexCertificate (T : H →ₗ.[ℂ] H) where
  symmetric : T.IsSymmetric
  dense : T.HasDenseDomain
  plus : T.defectNumber Complex.I = 0
  minus : T.defectNumber (-Complex.I) = 0
```

**`ProbabilisticTheory.QuantumMechanics.DefectIndexCertificate.essentiallySelfAdjoint`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean#L61).

```lean
lemma DefectIndexCertificate.essentiallySelfAdjoint
    {T : H →ₗ.[ℂ] H} (C : DefectIndexCertificate T) :
    T.IsEssentiallySelfAdjoint
```

**`ProbabilisticTheory.QuantumMechanics.DefectIndexCertificate.closure_isSelfAdjoint`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean#L66).

```lean
lemma DefectIndexCertificate.closure_isSelfAdjoint
    {T : H →ₗ.[ℂ] H} (C : DefectIndexCertificate T) :
    IsSelfAdjoint T.closure
```

**`ProbabilisticTheory.QuantumMechanics.ofSelfAdjoint_isEssentiallySelfAdjoint`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean#L72).

> A self-adjoint operator is automatically an essentially self-adjoint core for itself.

```lean
lemma ofSelfAdjoint_isEssentiallySelfAdjoint
    {T : H →ₗ.[ℂ] H} (hT : IsSelfAdjoint T) : T.IsEssentiallySelfAdjoint
```

## B. Essential self-adjointness from a Hilbert basis of eigenvectors

> A symmetric operator whose domain is *exactly* the (algebraic) span of a Hilbert basis of
> eigenvectors with real eigenvalues is essentially self-adjoint. This is the standard "eigenbasis
> density" criterion for essential self-adjointness (see e.g. Reed–Simon, *Methods of Modern
> Mathematical Physics I: Functional Analysis*, Theorem VIII.3): reality of the eigenvalues makes
> `T ∓ i` bounded below by `1` on the eigenbasis span, and the Hilbert-basis expansion of an
> arbitrary `y : H` (with coefficients divided by `λ - z`) produces, in the limit of its partial
> sums, an explicit preimage of `y` under `T.closure ∓ i`.

**`ProbabilisticTheory.QuantumMechanics.isEssentiallySelfAdjoint_of_hilbertBasis_eigenvectors`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean#L97).

> **Essential self-adjointness from a Hilbert basis of eigenvectors.** If `T`'s domain is exactly
> the (algebraic) span of a Hilbert basis `e`, and each basis vector `e i` is an eigenvector of `T`
> with *real* eigenvalue `lam i`, then `T` is essentially self-adjoint.

```lean
lemma isEssentiallySelfAdjoint_of_hilbertBasis_eigenvectors
    (e : HilbertBasis ι ℂ H) (T : H →ₗ.[ℂ] H) (lam : ι → ℝ)
    (hdom : T.domain = Submodule.span ℂ (Set.range e))
    (heig : ∀ i, T ⟨e i, hdom ▸ Submodule.subset_span ⟨i, rfl⟩⟩ = (lam i : ℂ) • e i) :
    T.IsEssentiallySelfAdjoint
```

## Depends on

- [Spectral theory for closed operators](../../../../physlib/quantummechanics/operators/spectraltheory/basic.md)

## Proof depends on

- [Spectral theory for symmetric operators](../../../../physlib/quantummechanics/operators/spectraltheory/symmetric.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/RealAnalytic.lean)
