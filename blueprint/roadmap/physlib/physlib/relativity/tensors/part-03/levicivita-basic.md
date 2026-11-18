---
declaration: module
origin: cited
lean: realLorentzTensor.leviCivita, realLorentzTensor.leviCivita_eq_ofInt, euclidLeviCivita, euclidLeviCivita_eq_leviCivitaSymbol, realLorentzTensor.leviCivita_basis_repr_apply, realLorentzTensor.leviCivita_basis_repr_eq_leviCivitaSymbol, realLorentzTensor.leviCivita_basis_repr_eq_zero_of_eq, realLorentzTensor.leviCivita_antisymm
statement: formalized
proof: formalized
---

# The Levi-Civita tensor as a real Lorentz tensor

The module `Physlib.Relativity.Tensors.LeviCivita.Basic`, [Physlib/Relativity/Tensors/LeviCivita/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean): 10 declarations, 10 with a docstring.

## i. Overview

> This file defines the rank-four Levi-Civita tensor `εᵘᵛᵖᵟ` as a real Lorentz tensor in
> `d = 3` spatial dimensions, with `ε⁰¹²³ = 1`, and proves its antisymmetry under each
> adjacent transposition of indices.
>
> The component on a multi-index `f` is the generalized Kronecker delta of `f` against the
> identity, i.e. the sign of `f` when `f` is a permutation and `0` otherwise. The integer
> components are carried by `TensorSpecies.Tensor.TensorInt.toTensor`.

## ii. Key results

> - `leviCivita` : the rank-four Levi-Civita tensor `ε4`, with `ε⁰¹²³ = 1`.
> - `leviCivita_basis_repr_apply` : its standard-basis components as a generalized Kronecker delta.
> - `leviCivita_basis_repr_eq_leviCivitaSymbol` : its standard-basis components as the
>   general-dimension Levi-Civita symbol `leviCivitaSymbol` at `ι = Fin 4`.
> - `leviCivita_antisymm`, `leviCivita_antisymm_mid`, `leviCivita_antisymm_last` : antisymmetry
>   under each adjacent transposition of the indices.

## iv. References

> * None.

## A. Definition

**`realLorentzTensor.leviCivita`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L66).

> The Levi-Civita tensor `εᵘᵛᵖᵟ` as a real Lorentz tensor in `d = 3`, with `ε⁰¹²³ = 1`.
>
> The component on a multi-index `f` is the generalized Kronecker delta of `f` against the
> identity, i.e. the sign of `f` when `f` is a permutation and `0` otherwise.

```lean
noncomputable def leviCivita : ℝT[3, .up, .up, .up, .up]
```

**`realLorentzTensor.leviCivita_eq_ofInt`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L75).

> The `TensorInt.toTensor` form of the Levi-Civita tensor.

```lean
lemma leviCivita_eq_ofInt : ε4 =
    TensorInt.toTensor (S := realLorentzTensor 3)
    (c := ![Color.up, Color.up, Color.up, Color.up]) fun f =>
    generalizedKroneckerDelta (fun i => finSumFinEquiv (f i)) (id : Fin 4 → Fin 4)
```

**`euclidLeviCivita`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L82).

> The Euclidean Levi-Civita symbol `ε_{ijkl}` in dimension 4.

```lean
def _root_.euclidLeviCivita (g : Fin 4 → Fin 4) : ℝ
```

**`euclidLeviCivita_eq_leviCivitaSymbol`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L87).

> The Euclidean Levi-Civita symbol in dimension 4 is the general-dimension
> Levi-Civita symbol `leviCivitaSymbol` at `ι = Fin 4`, carried to the reals.

```lean
lemma _root_.euclidLeviCivita_eq_leviCivitaSymbol (g : Fin 4 → Fin 4) :
    euclidLeviCivita g = (leviCivitaSymbol g : ℝ)
```

## B. Components in the standard basis

**`realLorentzTensor.leviCivita_basis_repr_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L99).

> The components of the Levi-Civita tensor in the standard basis are the generalized
> Kronecker delta of the multi-index against the identity.

```lean
lemma leviCivita_basis_repr_apply
    (b : ComponentIdx (S := realLorentzTensor 3) ![Color.up, Color.up, Color.up, Color.up]) :
    (Tensor.basis _).repr ε4 b
      = (generalizedKroneckerDelta (fun i => finSumFinEquiv (b i)) (id : Fin 4 → Fin 4) : ℝ)
```

**`realLorentzTensor.leviCivita_basis_repr_eq_leviCivitaSymbol`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L108).

> The components of the Levi-Civita tensor in the standard basis are the
> general-dimension Levi-Civita symbol `leviCivitaSymbol` of the multi-index at
> `ι = Fin 4`.

```lean
lemma leviCivita_basis_repr_eq_leviCivitaSymbol
    (b : ComponentIdx (S := realLorentzTensor 3) ![Color.up, Color.up, Color.up, Color.up]) :
    (Tensor.basis _).repr ε4 b
      = (leviCivitaSymbol (fun i => finSumFinEquiv (b i)) : ℝ)
```

**`realLorentzTensor.leviCivita_basis_repr_eq_zero_of_eq`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L116).

> The Levi-Civita tensor vanishes on any multi-index with a repeated value: if two distinct
> index positions `i ≠ j` carry the same basis index, the component is zero.

```lean
lemma leviCivita_basis_repr_eq_zero_of_eq
    {b : ComponentIdx (S := realLorentzTensor 3) ![Color.up, Color.up, Color.up, Color.up]}
    {i j : Fin 4} (hij : i ≠ j) (h : b i = b j) :
    (Tensor.basis _).repr ε4 b = 0
```

## C. Antisymmetry

**`realLorentzTensor.leviCivita_antisymm`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L138).

> The Levi-Civita tensor is antisymmetric in its first two indices
> `{ε4 | μ ν ρ σ = - ε4 | ν μ ρ σ}ᵀ`.

```lean
lemma leviCivita_antisymm : {ε4 | μ ν ρ σ = - (ε4 | ν μ ρ σ)}ᵀ
```

**`realLorentzTensor.leviCivita_antisymm_mid`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L151).

> The Levi-Civita tensor is antisymmetric in its middle two indices
> `{ε4 | μ ν ρ σ = - ε4 | μ ρ ν σ}ᵀ`.

```lean
lemma leviCivita_antisymm_mid : {ε4 | μ ν ρ σ = - (ε4 | μ ρ ν σ)}ᵀ
```

**`realLorentzTensor.leviCivita_antisymm_last`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean#L164).

> The Levi-Civita tensor is antisymmetric in its last two indices
> `{ε4 | μ ν ρ σ = - ε4 | μ ν σ ρ}ᵀ`.

```lean
lemma leviCivita_antisymm_last : {ε4 | μ ν ρ σ = - (ε4 | μ ν σ ρ)}ᵀ
```

## Depends on

- [Basis for tensors in a tensor species](../part-01/ofint.md)
- [Physlib.Relativity.Tensors.RealTensor.Basic](realtensor-basic.md)

## Sources

- [Physlib/Relativity/Tensors/LeviCivita/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Basic.lean)
