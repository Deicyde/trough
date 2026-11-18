---
declaration: module
origin: cited
lean: euclidLeviCivita_symbol_contract_zero, euclidLeviCivita_symbol_contract_one, euclidLeviCivita_symbol_contract_one_last, euclidLeviCivita_symbol_contract_two, realLorentzTensor.leviCivita_lowered_basis_repr_apply, realLorentzTensor.leviCivita_basis_contract_self, realLorentzTensor.leviCivita_basis_contract_three, realLorentzTensor.leviCivita_contract_three_basis_repr_apply
statement: formalized
proof: formalized
---

# Contraction identities for the Levi-Civita tensor

The module `Physlib.Relativity.Tensors.LeviCivita.Contractions`, [Physlib/Relativity/Tensors/LeviCivita/Contractions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean): 11 declarations, 11 with a docstring.

## i. Overview

> This file proves the "epsilon-epsilon" contraction identities for the rank-four Levi-Civita
> tensor `leviCivita` (notation `ε4`) in `d = 4`, stated in terms of the standard-basis
> components of `ε4` itself (`realLorentzTensor.leviCivita_basis_repr_apply`).
>
> The underlying facts about the `generalizedKroneckerDelta` alone, with no
> tensor content, live in `Physlib.Mathematics.KroneckerDelta.Contraction`, next to the
> definition of `generalizedKroneckerDelta`. Here we specialise those facts to the components of
> `ε4`, where `(ε4)_b = (Tensor.basis _).repr ε4 b` is the standard-basis component of `ε4`, an
> integer Levi-Civita symbol carried to the reals, and the sums run over the remaining
> (uncontracted) component slots.
>
> It also proves the Lorentzian tensor identities obtained by lowering all four indices of one
> factor: the complete contraction is `-24`, while contracting three index pairs gives `-6` times
> the unit tensor.
>
> The Lorentzian proofs proceed through reusable component statements: lowering all four indices
> contributes the orientation sign, tensor contractions become finite sums of matching components,
> and the Euclidean contraction theorems evaluate those sums.

## ii. Key results

> - `euclidLeviCivita_symbol_contract_zero` : full Euclidean contraction equals `24`.
> - `euclidLeviCivita_symbol_contract_one` : the triple Euclidean contraction equals `6 · δ[a,b]`.
> - `euclidLeviCivita_symbol_contract_two` :
>   `∑_h (ε4)_{r,s,h} · (ε4)_{t,w,h} = 2 · (δ[r,t]·δ[s,w] - δ[r,w]·δ[s,t])`.
> - `realLorentzTensor.leviCivita_lowered_basis_repr_apply` : lowering all four indices changes
>   every standard-basis component by the Lorentzian orientation sign `-1`.
> - `realLorentzTensor.leviCivita_contract_three_basis_repr_apply` : the tensor triple contraction
>   is the sum of matching standard-basis components.
> - `leviCivita_contract_self` : `ε^{μνρσ} ε_{μνρσ} = -24`.
> - `leviCivita_contract_three` : `ε^{μνρσ} ε_{μνρτ} = -6 δ^σ_τ`.

## iv. References

> * None.

## A. Euclidean epsilon-epsilon contraction identities

**`euclidLeviCivita_symbol_contract_zero`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L80).

> **Full Euclidean Levi-Civita contraction** `∑_b (ε4)_b · (ε4)_b = 24` at the symbol level:
> summing the square of every standard-basis component of `ε4` over all four `Fin 4` index slots,
> paired naively (no metric), counts the `4! = 24` permutations. The Lorentz contraction
> `ε^{μνρσ} ε_{μνρσ}` lowers one factor with `η` and equals `-24` instead.

```lean
lemma euclidLeviCivita_symbol_contract_zero :
    ∑ g : (Fin 4 → Fin 4), euclidLeviCivita g * euclidLeviCivita g = 24
```

**`euclidLeviCivita_symbol_contract_one`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L95).

> **Triple Euclidean Levi-Civita contraction** `∑_h (ε4)_{a,h} · (ε4)_{b,h} = 6 · δ[a,b]` at
> the symbol level: contracting three of the four `Fin 4` component slots of `ε4` with the naive
> Kronecker pairing leaves one free pair `a, b` and the factor `3! = 6`. The Lorentz form carries
> an extra `det η = -1`.

```lean
lemma euclidLeviCivita_symbol_contract_one (a b : Fin 4) :
    ∑ h : Fin 3 → Fin 4, euclidLeviCivita (Fin.cons a h) * euclidLeviCivita (Fin.cons b h)
      = 6 * ((kroneckerDelta a b : ℕ) : ℝ)
```

**`euclidLeviCivita_symbol_contract_one_last`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L112).

> **Triple Euclidean Levi-Civita contraction with the free index last.** This is the same
> contraction as `euclidLeviCivita_symbol_contract_one`, in the slot order produced by the tensor
> notation for `ε^{μνρσ} ε_{μνρτ}`.

```lean
lemma euclidLeviCivita_symbol_contract_one_last (a b : Fin 4) :
    ∑ h : Fin 3 → Fin 4, euclidLeviCivita (Fin.snoc h a) * euclidLeviCivita (Fin.snoc h b)
      = 6 * ((kroneckerDelta a b : ℕ) : ℝ)
```

**`euclidLeviCivita_symbol_contract_two`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L125).

> **Double Euclidean Levi-Civita contraction**
> `∑_h (ε4)_{r,s,h} · (ε4)_{t,w,h} = 2 · (δ[r,t]·δ[s,w] - δ[r,w]·δ[s,t])` at the symbol level:
> contracting two of the four `Fin 4` component slots of `ε4` with the naive Kronecker pairing
> leaves two free pairs and the factor `2! = 2`. The Lorentz form carries an extra `det η = -1`.

```lean
lemma euclidLeviCivita_symbol_contract_two (r s t w : Fin 4) :
    ∑ h : Fin 2 → Fin 4, euclidLeviCivita (Fin.cons r (Fin.cons s h))
          * euclidLeviCivita (Fin.cons t (Fin.cons w h))
      = 2 * (((kroneckerDelta r t : ℕ) : ℝ) * ((kroneckerDelta s w : ℕ) : ℝ)
          - ((kroneckerDelta r w : ℕ) : ℝ) * ((kroneckerDelta s t : ℕ) : ℝ))
```

## B. Lorentzian epsilon-epsilon contraction identities

**`realLorentzTensor.leviCivita_lowered_basis_repr_apply`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L159).

> Lowering all four indices of the Levi-Civita tensor changes the sign of every standard-basis
> component. This is the tensor-component form of the Lorentzian orientation factor
> `det η = -1`.

```lean
lemma leviCivita_lowered_basis_repr_apply
    (b : ComponentIdx (S := realLorentzTensor 3)
      ![Color.down, Color.down, Color.down, Color.down]) :
    (Tensor.basis _).repr ({ε4 | τ(μ) τ(ν) τ(ρ) τ(σ)}ᵀ) b =
      - (Tensor.basis _).repr ε4 b
```

**`realLorentzTensor.leviCivita_basis_contract_self`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L178).

> The sum of the squared standard-basis components of the contravariant Levi-Civita tensor is
> `4! = 24`.

```lean
lemma leviCivita_basis_contract_self :
    ∑ b : ComponentIdx (S := realLorentzTensor 3)
        ![Color.up, Color.up, Color.up, Color.up],
      (Tensor.basis _).repr ε4 b * (Tensor.basis _).repr ε4 b = 24
```

**`realLorentzTensor.leviCivita_basis_contract_three`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L192).

> Contracting the first three standard-basis components of two contravariant Levi-Civita tensors
> gives `3! = 6` times the Kronecker delta on the remaining components.

```lean
lemma leviCivita_basis_contract_three (a b : Fin 1 ⊕ Fin 3) :
    ∑ h : Fin 3 → Fin 1 ⊕ Fin 3,
      (Tensor.basis _).repr ε4 (Fin.snoc h a) *
      (Tensor.basis _).repr ε4 (Fin.snoc h b) =
      6 * (if a = b then 1 else 0)
```

**`realLorentzTensor.leviCivita_contract_three_basis_repr_apply`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L222).

> The standard-basis component formula for the tensor contraction
> `ε^{μνρσ} ε_{μνρτ}`.

```lean
lemma leviCivita_contract_three_basis_repr_apply
    (b : ComponentIdx (S := realLorentzTensor 3) ![Color.up, Color.down]) :
    (Tensor.basis _).repr
        {ε4 | μ ν ρ σ ⊗ ε4 | τ(μ) τ(ν) τ(ρ) τ(τ)}ᵀ b =
      ∑ h : Fin 3 → Fin 1 ⊕ Fin 3,
        (Tensor.basis _).repr ε4 (Fin.snoc h (b 0)) *
          (Tensor.basis _).repr ({ε4 | τ(μ) τ(ν) τ(ρ) τ(σ)}ᵀ) (Fin.snoc h (b 1))
```

### B.1. The epsilon-epsilon contraction identities

**`realLorentzTensor.leviCivita_contract_three`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L272).

> Contracting three indices of the Lorentzian Levi-Civita tensor with a fully lowered copy gives
> `-6` times the mixed-index unit tensor.

```lean
lemma leviCivita_contract_three : {ε4 | μ ν ρ σ ⊗ ε4 | τ(μ) τ(ν) τ(ρ) τ(τ) =
    (-6) • unitTensor (S := realLorentzTensor) Color.down | σ τ }ᵀ
```

**`realLorentzTensor.leviCivita_contract_self_eq_sum`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L302).

> Fully contracting the tensor product of `ε4` and its fully lowered form is the sum of the
> products of their matching standard-basis components.

```lean
lemma leviCivita_contract_self_eq_sum :
    {ε4 | μ ν ρ σ ⊗ ε4 | τ(μ) τ(ν) τ(ρ) τ(σ)}ᵀ.toScalar =
      ∑ b : ComponentIdx (S := realLorentzTensor 3)
          ![Color.up, Color.up, Color.up, Color.up],
        (Tensor.basis _).repr ε4 b *
          (Tensor.basis _).repr ({ε4 | τ(μ) τ(ν) τ(ρ) τ(σ)}ᵀ) b
```

**`realLorentzTensor.leviCivita_contract_self`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean#L339).

> Fully contracting the Lorentzian Levi-Civita tensor with a lowered copy gives `-24`.

```lean
lemma leviCivita_contract_self :
    {ε4 | μ ν ρ σ ⊗ ε4 | τ(μ) τ(ν) τ(ρ) τ(σ)}ᵀ.toScalar = - 24
```

## Depends on

- [Dual tensors](../part-01/dual.md)
- [The Levi-Civita tensor as a real Lorentz tensor](levicivita-basic.md)

## Proof depends on

- [Contraction identities for the generalized Kronecker delta](../../../mathematics/kroneckerdelta/contraction.md)
- [Physlib.Relativity.Tensors.RealTensor.Metrics.Basic](realtensor-metrics-basic.md)
- [Unit tensors for real Lorentz tensors](realtensor-units-basic.md)

## Sources

- [Physlib/Relativity/Tensors/LeviCivita/Contractions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/LeviCivita/Contractions.lean)
