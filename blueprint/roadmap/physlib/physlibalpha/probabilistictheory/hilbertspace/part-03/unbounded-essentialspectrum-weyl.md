---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.Essential.I_im_ne_zero, ProbabilisticTheory.QuantumMechanics.Essential.IsResolventAt, ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_subset_of_isCompactOperator_resolvent_sub, ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_eq_of_isCompactOperator_resolvent_sub, ProbabilisticTheory.QuantumMechanics.Essential.isCompactOperator_resolvent_sub_of_isCompactOperator_perturb, ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_eq_of_isCompactOperator_perturb
statement: formalized
proof: formalized
---

# Weyl's theorem on the essential spectrum

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.EssentialSpectrum.Weyl`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean): 6 declarations, 6 with a docstring.

> Weyl's theorem: compact resolvent differences preserve the essential spectrum.

## i. Overview

> If the resolvents at `i` of two self-adjoint operators differ by a compact operator, the operators
> have the same essential spectrum. The resolvents enter as bounded operators satisfying the defining
> properties of the resolvent, `IsResolventAt`. In particular a relatively compact perturbation does
> not change the essential spectrum.

## ii. Key results

> - `IsResolventAt` : a bounded operator is the resolvent of a self-adjoint operator at `z`.
> - `essSpectrum_eq_of_isCompactOperator_resolvent_sub` : **Weyl's theorem.**
> - `essSpectrum_eq_of_isCompactOperator_perturb` : the essential spectrum is stable under relatively
>   compact perturbations.

## iv. References

> - Adapted from `adambornemann-glitch/Spectra`, `SpectralTheory/Essential/Weyl.lean` (Apache 2.0).

**`ProbabilisticTheory.QuantumMechanics.Essential.I_im_ne_zero`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean#L57).

> `i` is off the real axis, the spectral parameter used throughout.

```lean
lemma I_im_ne_zero : (Complex.I).im ≠ 0
```

## A. The bounded resolvent

**`ProbabilisticTheory.QuantumMechanics.Essential.IsResolventAt`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean#L63).

> `R` is the resolvent of the self-adjoint operator `A` at `z`: it maps into the domain of `A`,
> and inverts `A - z` on both sides.

```lean
structure IsResolventAt {A : H →ₗ.[ℂ] H} (_hA : IsSelfAdjoint A) (z : ℂ)
    (R : H →L[ℂ] H) : Prop where
  mem_domain : ∀ φ, R φ ∈ A.domain
  solves : ∀ φ, A ⟨R φ, mem_domain φ⟩ - z • R φ = φ
  left_inverse : ∀ ψ : A.domain, R (A ψ - z • (ψ : H)) = (ψ : H)
```

## B. Weyl's theorem

**`ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_subset_of_isCompactOperator_resolvent_sub`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean#L73).

> **One inclusion of Weyl's theorem.** If the resolvent difference `R_B(i) − R_A(i)` is compact,
> then `essSpectrum hA ⊆ essSpectrum hB`.

```lean
lemma essSpectrum_subset_of_isCompactOperator_resolvent_sub
    {A B : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {RA RB : H →L[ℂ] H} (hRA : IsResolventAt hA I RA) (hRB : IsResolventAt hB I RB)
    (hcompact : IsCompactOperator ((RB - RA : H →L[ℂ] H) : H → H)) :
    essSpectrum hA ⊆ essSpectrum hB
```

**`ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_eq_of_isCompactOperator_resolvent_sub`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean#L177).

> **Weyl's theorem.** If the resolvents `R_A(i)`, `R_B(i)` of two self-adjoint operators differ
> by a compact operator, then `A` and `B` have the same essential spectrum.

```lean
lemma essSpectrum_eq_of_isCompactOperator_resolvent_sub
    {A B : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {RA RB : H →L[ℂ] H} (hRA : IsResolventAt hA I RA) (hRB : IsResolventAt hB I RB)
    (hcompact : IsCompactOperator ((RB - RA : H →L[ℂ] H) : H → H)) :
    essSpectrum hA = essSpectrum hB
```

## C. Relatively compact perturbations

**`ProbabilisticTheory.QuantumMechanics.Essential.isCompactOperator_resolvent_sub_of_isCompactOperator_perturb`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean#L193).

> **Relatively compact perturbations.** If `B - A = W (A - i)` on the domain of `A` for a compact
> `W`, then `R_B(i) - R_A(i) = -R_B(i) W` is compact.

```lean
lemma isCompactOperator_resolvent_sub_of_isCompactOperator_perturb
    {A B : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {RA RB : H →L[ℂ] H} (hRA : IsResolventAt hA I RA) (hRB : IsResolventAt hB I RB)
    (hdom : A.domain = B.domain) (W : H →L[ℂ] H) (hW : IsCompactOperator (W : H → H))
    (hVW : ∀ (χ : H) (hχ : χ ∈ A.domain),
        B ⟨χ, hdom ▸ hχ⟩ - A ⟨χ, hχ⟩ = W (A ⟨χ, hχ⟩ - I • χ)) :
    IsCompactOperator ((RB - RA : H →L[ℂ] H) : H → H)
```

**`ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_eq_of_isCompactOperator_perturb`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean#L224).

> **Weyl's theorem for relatively compact perturbations.** If `B - A = W (A - i)` on the domain of
> `A` for a compact `W`, then `A` and `B` have the same essential spectrum.

```lean
lemma essSpectrum_eq_of_isCompactOperator_perturb
    {A B : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    {RA RB : H →L[ℂ] H} (hRA : IsResolventAt hA I RA) (hRB : IsResolventAt hB I RB)
    (hdom : A.domain = B.domain) (W : H →L[ℂ] H) (hW : IsCompactOperator (W : H → H))
    (hVW : ∀ (χ : H) (hχ : χ ∈ A.domain),
        B ⟨χ, hdom ▸ hχ⟩ - A ⟨χ, hχ⟩ = W (A ⟨χ, hχ⟩ - I • χ)) :
    essSpectrum hA = essSpectrum hB
```

## Depends on

- [The essential spectrum](unbounded-essentialspectrum-defs.md)

## Proof depends on

- [Compact operators and weakly null sequences](unbounded-essentialspectrum-weakcompact.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Weyl.lean)
