---
declaration: module
origin: cited
lean: LinearPMap.IsSelfAdjoint.resolventSet_eq_regularityDomain, LinearPMap.IsSelfAdjoint.mem_resolventSet_of_im_ne_zero, LinearPMap.IsSelfAdjoint.sub_smul_surjective, LinearPMap.IsSelfAdjoint.mem_resolventSet_of_range_eq_top, LinearPMap.IsSelfAdjoint.spectrum_real, LinearPMap.IsSelfAdjoint.residualSpectrum_eq_empty, LinearPMap.unitaryConj_isSelfAdjoint
statement: formalized
proof: formalized
---

# Spectral theory for self-adjoint operators

The module `Physlib.QuantumMechanics.Operators.SpectralTheory.SelfAdjoint`, [Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean): 7 declarations, 6 with a docstring.

## i. Overview

> In this module we develop the spectral theory for self-adjoint operators.

## ii. Key results

> - `resolventSet_eq_regularityDomain` : The resolvent set and regularity domain coincide. That is,
>     if `T - z • 1` has a continuous (equivalently, bounded) inverse then its range is all of `H`.
> - `mem_resolventSet_of_im_ne_zero` : every non-real `z` lies in the resolvent set of a
>     self-adjoint operator.
> - `sub_smul_surjective` : A self-adjoint `T` has `T - z • 1` surjective for every non-real `z`
>     (in particular `T ± i • 1` are onto).
> - `spectrum_real` : The spectrum of a self-adjoint unbounded operator is real.
> - `unitaryConj_isSelfAdjoint` : Unitary conjugation preserves self-adjointness.

## iv. References

> * None.

## A. Resolvent set

**`LinearPMap.IsSelfAdjoint.resolventSet_eq_regularityDomain`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean#L56).

```lean
lemma resolventSet_eq_regularityDomain : ρ T = T.regularityDomain
```

**`LinearPMap.IsSelfAdjoint.mem_resolventSet_of_im_ne_zero`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean#L70).

> Every non-real `z` lies in the resolvent set of a self-adjoint operator.

```lean
lemma mem_resolventSet_of_im_ne_zero {z : ℂ} (hz : z.im ≠ 0) : z ∈ ρ T
```

**`LinearPMap.IsSelfAdjoint.sub_smul_surjective`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean#L76).

> A self-adjoint operator has `T - z • 1` surjective for every non-real `z`: off the real
> axis a self-adjoint operator has `z` in its resolvent set, so `T - z • 1` has full range.

```lean
lemma sub_smul_surjective {z : ℂ} (hz : z.im ≠ 0) : Function.Surjective (T - z • 1).toFun
```

**`LinearPMap.IsSelfAdjoint.mem_resolventSet_of_range_eq_top`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean#L81).

> `(T - z • 1).range = ⊤` is a sufficient condition for `z ∈ ρ T`
> (and it is a necessary condition by definition of `ρ`).

```lean
lemma mem_resolventSet_of_range_eq_top {z : ℂ} (h : (T - z • 1).toFun.range = ⊤) : z ∈ ρ T
```

## B. Spectrum

**`LinearPMap.IsSelfAdjoint.spectrum_real`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean#L96).

> The spectrum of a self-adjoint operator is real.

```lean
lemma spectrum_real : σ T ⊆ range ofReal
```

**`LinearPMap.IsSelfAdjoint.residualSpectrum_eq_empty`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean#L101).

> The residual spectrum of a self-adjoint operator is empty.

```lean
lemma residualSpectrum_eq_empty : σʳ T = ∅
```

## C. Unitary conjugation

**`LinearPMap.unitaryConj_isSelfAdjoint`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean#L120).

> Unitary conjugation preserves self-adjointness: if `A` is a self-adjoint operator on `H` and
> `u : H ≃ₗᵢ[ℂ] H'` is unitary, then `u A u⁻¹` is self-adjoint on `H'`. Symmetry, dense domain, and
> the two deficiency surjectivities of `A` all transfer through `u`.

```lean
lemma unitaryConj_isSelfAdjoint (u : H ≃ₗᵢ[ℂ] H') {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) :
    IsSelfAdjoint (A.unitaryConj u)
```

## Depends on

- [Spectral theory for closed operators](basic.md)

## Proof depends on

- [Spectral theory for symmetric operators](symmetric.md)

## Sources

- [Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/SpectralTheory/SelfAdjoint.lean)
