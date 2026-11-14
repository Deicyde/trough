---
declaration: module
origin: cited
lean: suTensor.basis_repr_smul_fund, suTensor.basis_repr_smul_antiFund, suTensor.sum_fin_two_arrow, suTensor.epsilonFund, suTensor.epsilonAntiFund, suTensor.basis_repr_epsilonFund, suTensor.basis_repr_epsilonAntiFund, suTensor.eq_smul_epsilon_of_fixed
statement: formalized
proof: formalized
---

# Invariants of two fundamental or two anti-fundamental indices of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.Invariants.BiFund`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean): 36 declarations, 32 with a docstring.

## i. Overview

> The tensors with `n` fundamental indices, or with `n` anti-fundamental indices, have the tuples
> `Fin n → Fin N` as component indices, and `g` moves the components by one factor of `g`, or of
> its complex conjugate, per index (A).
>
> For `SU(2)` the invariant tensors with two fundamental indices, and those with two
> anti-fundamental indices, are the multiples of the antisymmetric symbol `ε` (B). The phase
> `diag (i, -i)` negates the two diagonal components, and the quarter turn sends the component
> `(0, 1)` to minus the component `(1, 0)`. For `N ≥ 3` there are none at all (C): the centre element
> `ω 1`, with `ω` a primitive `N`-th root of unity, scales every component by `ω² ≠ 1`, or by its
> conjugate.
>
> Families indexed by `Fin n → Fin N` are turned into maps by `fundMap` and `antiFundMap`, and for
> `SU(2)` the invariants of the span of such a family with two indices reduce to the epsilon
> contraction `T ![0, 1] - T ![1, 0]` (D).

## ii. Key results

> - `suTensor.epsilonFund`, `suTensor.epsilonAntiFund` : the antisymmetric symbols of `SU(2)`.
> - `suTensor.exists_eq_smul_epsilonFund_of_invariant` : the invariant tensors with two fundamental
>   indices of `SU(2)`, and its anti-fundamental twin.
> - `suTensor.eq_zero_of_invariant_fundPair` : for `N ≥ 3` there are none, and its
>   anti-fundamental twin.
> - `suTensor.invariantReductionToEpsilonFund` : the reduction of the invariants of the span of a
>   family to the epsilon contraction, and its anti-fundamental twin.

## iv. References

> * None.

## A. Tensors with fundamental or with anti-fundamental indices

**`suTensor.basis_repr_smul_fund`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L69).

> The components of `g • t` for a tensor with `n` fundamental indices: one factor of `g` per
> index.

```lean
lemma basis_repr_smul_fund {n : ℕ} (g : SU N) (t : (suTensor N).Tensor fun _ : Fin n => .fund)
    (φ : Fin n → Fin N) :
    (Tensor.basis _).repr (g • t) φ
      = ∑ ψ : Fin n → Fin N, (∏ i, g.1 (φ i) (ψ i)) * (Tensor.basis _).repr t ψ
```

**`suTensor.basis_repr_smul_antiFund`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L80).

> The components of `g • t` for a tensor with `n` anti-fundamental indices: one factor of the
> complex conjugate of `g` per index.

```lean
lemma basis_repr_smul_antiFund {n : ℕ} (g : SU N)
    (t : (suTensor N).Tensor fun _ : Fin n => .antiFund) (φ : Fin n → Fin N) :
    (Tensor.basis _).repr (g • t) φ = ∑ ψ : Fin n → Fin N,
      (∏ i, starRingEnd ℂ (g.1 (φ i) (ψ i))) * (Tensor.basis _).repr t ψ
```

**`suTensor.sum_fin_two_arrow`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L92).

> A sum over pairs of labels is a double sum.

```lean
lemma sum_fin_two_arrow {M : Type*} [AddCommMonoid M] (F : (Fin 2 → Fin N) → M) :
    ∑ ψ : Fin 2 → Fin N, F ψ = ∑ x, ∑ y, F ![x, y]
```

## B. Two indices of `SU(2)`: the antisymmetric symbol

**`suTensor.epsilonFund`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L104).

> The antisymmetric symbol `ε^{ab}` with two fundamental indices of `SU(2)`.

```lean
noncomputable def epsilonFund : (suTensor 2).Tensor fun _ : Fin 2 => .fund
```

**`suTensor.epsilonAntiFund`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L108).

> The antisymmetric symbol `ε_{ab}` with two anti-fundamental indices of `SU(2)`.

```lean
noncomputable def epsilonAntiFund : (suTensor 2).Tensor fun _ : Fin 2 => .antiFund
```

**`suTensor.basis_repr_epsilonFund`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L112).

> The components of the antisymmetric symbol.

```lean
lemma basis_repr_epsilonFund (φ : Fin 2 → Fin 2) :
    (Tensor.basis _).repr epsilonFund φ
      = (if φ = ![0, 1] then 1 else 0) - (if φ = ![1, 0] then 1 else 0)
```

**`suTensor.basis_repr_epsilonAntiFund`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L118).

> The components of the antisymmetric symbol.

```lean
lemma basis_repr_epsilonAntiFund (φ : Fin 2 → Fin 2) :
    (Tensor.basis _).repr epsilonAntiFund φ
      = (if φ = ![0, 1] then 1 else 0) - (if φ = ![1, 0] then 1 else 0)
```

**`suTensor.eq_smul_epsilon_of_fixed`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L126).

> A function of two labels fixed by a diagonal matrix with entries squaring to `-1` and by
> the quarter turn, acting by one factor of `M g` per label, is a multiple of the antisymmetric
> symbol.

```lean
lemma eq_smul_epsilon_of_fixed (M : SU 2 → Matrix (Fin 2) (Fin 2) ℂ) {u v : ℂ}
    (hu : u * u = -1) (hv : v * v = -1)
    (hD : M (diagPhase Complex.I (by simp)) = diagonal ![u, v])
    (hR : M (rotation 0 1 (by norm_num)) = !![0, -1; 1, 0]) {c : (Fin 2 → Fin 2) → ℂ}
    (hc : ∀ (g : SU 2) (φ : Fin 2 → Fin 2),
      c φ = ∑ ψ : Fin 2 → Fin 2, (∏ i, M g (φ i) (ψ i)) * c ψ) (φ : Fin 2 → Fin 2) :
    c φ = c ![0, 1] * ((if φ = ![0, 1] then 1 else 0) - (if φ = ![1, 0] then 1 else 0))
```

**`suTensor.exists_eq_smul_epsilonFund_of_invariant`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L151).

> An invariant tensor with two fundamental indices of `SU(2)` is a multiple of the
> antisymmetric symbol.

```lean
lemma exists_eq_smul_epsilonFund_of_invariant (t : (suTensor 2).Tensor fun _ : Fin 2 => .fund)
    (ht : ∀ g : SU 2, g • t = t) : ∃ a : ℂ, t = a • epsilonFund
```

**`suTensor.exists_eq_smul_epsilonAntiFund_of_invariant`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L168).

> An invariant tensor with two anti-fundamental indices of `SU(2)` is a multiple of the
> antisymmetric symbol.

```lean
lemma exists_eq_smul_epsilonAntiFund_of_invariant
    (t : (suTensor 2).Tensor fun _ : Fin 2 => .antiFund) (ht : ∀ g : SU 2, g • t = t) :
    ∃ a : ℂ, t = a • epsilonAntiFund
```

**`suTensor.det_fin_two_eq_one`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L184).

> The determinant of an element of `SU(2)`, written out.

```lean
lemma det_fin_two_eq_one (g : SU 2) : g.1 0 0 * g.1 1 1 - g.1 0 1 * g.1 1 0 = 1
```

**`suTensor.epsilonFund_invariant`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L190).

> The antisymmetric symbol with two fundamental indices is invariant: `g ⊗ g` scales it by
> `det g = 1`.

```lean
lemma epsilonFund_invariant (g : SU 2) : g • epsilonFund = epsilonFund
```

**`suTensor.epsilonAntiFund_invariant`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L203).

> The antisymmetric symbol with two anti-fundamental indices is invariant: `ḡ ⊗ ḡ` scales it
> by the conjugate of `det g = 1`.

```lean
lemma epsilonAntiFund_invariant (g : SU 2) : g • epsilonAntiFund = epsilonAntiFund
```

## C. Two indices of `SU(N)` for `N ≥ 3`: no invariants

**`suTensor.rootOfUnity`**, a def, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L222).

> The primitive `N`-th root of unity `exp (2 π i / N)`.

```lean
noncomputable def rootOfUnity (N : ℕ) : ℂ
```

**`suTensor.rootOfUnity_isPrimitiveRoot`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L224).

```lean
lemma rootOfUnity_isPrimitiveRoot (hN : N ≠ 0) : IsPrimitiveRoot (rootOfUnity N) N
```

**`suTensor.rootOfUnity_mul_star`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L227).

```lean
lemma rootOfUnity_mul_star : rootOfUnity N * star (rootOfUnity N) = 1
```

**`suTensor.centre`**, a def, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L234).

> The centre element `ω 1` of `SU(N)`, for `ω` the primitive `N`-th root of unity.

```lean
noncomputable def centre (N : ℕ) (hN : N ≠ 0) : SU N
```

**`suTensor.basis_repr_centre_smul_fund`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L242).

> The centre element scales the components of a tensor with two fundamental indices by `ω²`.

```lean
lemma basis_repr_centre_smul_fund (hN : N ≠ 0) (t : (suTensor N).Tensor fun _ : Fin 2 => .fund)
    (φ : Fin 2 → Fin N) :
    (Tensor.basis _).repr (centre N hN • t) φ
      = rootOfUnity N ^ 2 * (Tensor.basis _).repr t φ
```

**`suTensor.basis_repr_centre_smul_antiFund`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L256).

> The centre element scales the components of a tensor with two anti-fundamental indices by
> `ω̄²`.

```lean
lemma basis_repr_centre_smul_antiFund (hN : N ≠ 0)
    (t : (suTensor N).Tensor fun _ : Fin 2 => .antiFund) (φ : Fin 2 → Fin N) :
    (Tensor.basis _).repr (centre N hN • t) φ
      = starRingEnd ℂ (rootOfUnity N) ^ 2 * (Tensor.basis _).repr t φ
```

**`suTensor.rootOfUnity_sq_ne_one`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L269).

> For `N ≥ 3`, `ω² ≠ 1`.

```lean
lemma rootOfUnity_sq_ne_one (hN : 3 ≤ N) : rootOfUnity N ^ 2 ≠ 1
```

**`suTensor.eq_zero_of_invariant_fundPair`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L274).

> For `N ≥ 3` the only invariant tensor with two fundamental indices is zero: the centre
> element scales it by `ω² ≠ 1`.

```lean
lemma eq_zero_of_invariant_fundPair (hN : 3 ≤ N) (t : (suTensor N).Tensor fun _ : Fin 2 => .fund)
    (ht : ∀ g : SU N, g • t = t) : t = 0
```

**`suTensor.eq_zero_of_invariant_antiFundPair`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L286).

> For `N ≥ 3` the only invariant tensor with two anti-fundamental indices is zero: the centre
> element scales it by `ω̄² ≠ 1`.

```lean
lemma eq_zero_of_invariant_antiFundPair (hN : 3 ≤ N)
    (t : (suTensor N).Tensor fun _ : Fin 2 => .antiFund) (ht : ∀ g : SU N, g • t = t) :
    t = 0
```

## D. Maps from components

**`suTensor.fundMap`**, a def, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L310).

> The linear map out of the tensors with `n` fundamental indices sending the basis tensor with
> labels `l` to `T l`.

```lean
noncomputable def fundMap {n : ℕ} (T : (Fin n → Fin N) → B) :
    (suTensor N).Tensor (fun _ : Fin n => .fund) →ₗ[ℂ] B
```

**`suTensor.antiFundMap`**, a def, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L316).

> The linear map out of the tensors with `n` anti-fundamental indices sending the basis tensor
> with labels `l` to `T l`.

```lean
noncomputable def antiFundMap {n : ℕ} (T : (Fin n → Fin N) → B) :
    (suTensor N).Tensor (fun _ : Fin n => .antiFund) →ₗ[ℂ] B
```

**`suTensor.fundMap_basis`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L321).

```lean
lemma fundMap_basis {n : ℕ} (T : (Fin n → Fin N) → B) (l : Fin n → Fin N) :
    fundMap T (Tensor.basis (S := suTensor N) (fun _ : Fin n => Color.fund) l) = T l
```

**`suTensor.antiFundMap_basis`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L326).

```lean
lemma antiFundMap_basis {n : ℕ} (T : (Fin n → Fin N) → B) (l : Fin n → Fin N) :
    antiFundMap T (Tensor.basis (S := suTensor N) (fun _ : Fin n => Color.antiFund) l) = T l
```

**`suTensor.fundMap_smul_of_law`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L332).

> A linear map moving a family with `n` fundamental labels by one factor of `g` per label
> intertwines the map of the family with the action of `g`.

```lean
lemma fundMap_smul_of_law {n : ℕ} (T : (Fin n → Fin N) → B) {σ : B →ₗ[ℂ] B} (g : SU N)
    (hσ : ∀ l : Fin n → Fin N, σ (T l) = ∑ a : Fin n → Fin N, (∏ i, g.1 (a i) (l i)) • T a)
    (t : (suTensor N).Tensor fun _ : Fin n => .fund) :
    σ (fundMap T t) = fundMap T (g • t)
```

**`suTensor.antiFundMap_smul_of_law`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L345).

> A linear map moving a family with `n` anti-fundamental labels by one factor of the complex
> conjugate of `g` per label intertwines the map of the family with the action of `g`.

```lean
lemma antiFundMap_smul_of_law {n : ℕ} (T : (Fin n → Fin N) → B) {σ : B →ₗ[ℂ] B} (g : SU N)
    (hσ : ∀ l : Fin n → Fin N, σ (T l)
      = ∑ a : Fin n → Fin N, (∏ i, starRingEnd ℂ (g.1 (a i) (l i))) • T a)
    (t : (suTensor N).Tensor fun _ : Fin n => .antiFund) :
    σ (antiFundMap T t) = antiFundMap T (g • t)
```

**`suTensor.isEquivariant_fundMap`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L359).

> The map of a family with `n` fundamental labels is equivariant when the family moves by one
> factor of `g` per label, the summed label first.

```lean
lemma isEquivariant_fundMap {n : ℕ} (T : (Fin n → Fin N) → B)
    (hT : ∀ (g : SU N) (l : Fin n → Fin N), ρ g (T l)
      = ∑ a : Fin n → Fin N, (∏ i, g.1 (a i) (l i)) • T a) :
    (suTensor N).IsEquivariant (fun _ => .fund) ρ (fundMap T)
```

**`suTensor.isEquivariant_antiFundMap`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L367).

> The map of a family with `n` anti-fundamental labels is equivariant when the family moves by
> one factor of the complex conjugate of `g` per label, the summed label first.

```lean
lemma isEquivariant_antiFundMap {n : ℕ} (T : (Fin n → Fin N) → B)
    (hT : ∀ (g : SU N) (l : Fin n → Fin N), ρ g (T l)
      = ∑ a : Fin n → Fin N, (∏ i, starRingEnd ℂ (g.1 (a i) (l i))) • T a) :
    (suTensor N).IsEquivariant (fun _ => .antiFund) ρ (antiFundMap T)
```

**`suTensor.fundMap_epsilonFund`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L375).

> The map of a family with two fundamental labels sends the antisymmetric symbol to the
> epsilon contraction.

```lean
lemma fundMap_epsilonFund (T : (Fin 2 → Fin 2) → B) :
    fundMap T epsilonFund = T ![0, 1] - T ![1, 0]
```

**`suTensor.antiFundMap_epsilonAntiFund`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L381).

> The map of a family with two anti-fundamental labels sends the antisymmetric symbol to the
> epsilon contraction.

```lean
lemma antiFundMap_epsilonAntiFund (T : (Fin 2 → Fin 2) → B) :
    antiFundMap T epsilonAntiFund = T ![0, 1] - T ![1, 0]
```

**`suTensor.invariantReductionToEpsilonFund`**, a def, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L388).

> For a family with two fundamental labels of `SU(2)` whose map is equivariant, the invariants
> of the span reduce to the span of the epsilon contraction `T ![0, 1] - T ![1, 0]`.

```lean
noncomputable def invariantReductionToEpsilonFund {ρ : Representation ℂ (SU 2) B}
    {T : (Fin 2 → Fin 2) → B} (hT : (suTensor 2).IsEquivariant (fun _ => .fund) ρ (fundMap T)) :
    InvariantReductionToSpan (fun g : SU 2 => ρ g) (Submodule.span ℂ (Set.range T))
```

**`suTensor.invariantReductionToEpsilonAntiFund`**, a def, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L397).

> For a family with two anti-fundamental labels of `SU(2)` whose map is equivariant, the
> invariants of the span reduce to the span of the epsilon contraction
> `T ![0, 1] - T ![1, 0]`.

```lean
noncomputable def invariantReductionToEpsilonAntiFund {ρ : Representation ℂ (SU 2) B}
    {T : (Fin 2 → Fin 2) → B}
    (hT : (suTensor 2).IsEquivariant (fun _ => .antiFund) ρ (antiFundMap T)) :
    InvariantReductionToSpan (fun g : SU 2 => ρ g) (Submodule.span ℂ (Set.range T))
```

**`suTensor.reducesInvariantsTo_bot_span_of_fundMap`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L407).

> For `N ≥ 3` and a family with two fundamental labels whose map is equivariant, the
> invariants of the span reduce to `⊥`.

```lean
lemma reducesInvariantsTo_bot_span_of_fundMap (hN : 3 ≤ N) {T : (Fin 2 → Fin N) → B}
    (hT : (suTensor N).IsEquivariant (fun _ => .fund) ρ (fundMap T)) :
    ReducesInvariantsTo (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T)) ⊥
```

**`suTensor.reducesInvariantsTo_bot_span_of_antiFundMap`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean#L415).

> For `N ≥ 3` and a family with two anti-fundamental labels whose map is equivariant, the
> invariants of the span reduce to `⊥`.

```lean
lemma reducesInvariantsTo_bot_span_of_antiFundMap (hN : 3 ≤ N) {T : (Fin 2 → Fin N) → B}
    (hT : (suTensor N).IsEquivariant (fun _ => .antiFund) ρ (antiFundMap T)) :
    ReducesInvariantsTo (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T)) ⊥
```

## Depends on

- [Elements of `SU(N)` in a coordinate plane, and what commutes with them](localgaugedata-su-invariants-basic.md)
- [The complex tensor species of `SU(N)`](localgaugedata-su-tensorspecies.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/BiFund.lean)
