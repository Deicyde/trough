---
declaration: module
origin: cited
lean: suTensor.basis_repr_smul_fund, suTensor.basis_repr_smul_antiFund, suTensor.leviCivitaCoeff, suTensor.sum_mul_leviCivitaCoeff, suTensor.leviCivitaCoeff_perm, suTensor.leviCivitaCoeff_of_not_injective, suTensor.leviCivitaCoeff_id, suTensor.sum_prod_mul_leviCivitaCoeff
statement: formalized
proof: formalized
---

# The Levi-Civita tensors of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Invariants.LeviCivita`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean): 46 declarations, 42 with a docstring.

> Up to scale, the Levi-Civita symbol is the only invariant with `N` fundamental indices of
> `SU(N)`, and the only one with `N` anti-fundamental indices.

## i. Overview

> The tensors with `n` fundamental indices, or with `n` anti-fundamental indices, have the tuples
> `Fin n → Fin N` as component indices, and `g` moves the components by one factor of `g`, or of
> its complex conjugate, per index (A).
>
> The Levi-Civita symbol `ε_a`, for `a : Fin N → Fin N`, is the sign of `a` when `a` is a
> permutation and zero when a label repeats (B). Contracting its indices with the rows `a` of a
> matrix `M` gives `ε_a det M`. So the tensors with these components, `leviCivitaFund N` with `N`
> fundamental indices and `leviCivitaAntiFund N` with `N` anti-fundamental indices, are invariant,
> because `det g = 1` (C).
>
> Conversely, let the components `c` of a tensor with `N` fundamental indices be fixed by `SU(N)`
> (D). If a label of `a` repeats, some label `q` is missed by `a`. Take a label `p` that `a` hits
> `m` times, and the diagonal element of `SU(N)` with a primitive `(N + 1)`-th root of unity `ω`
> at `p`, its conjugate at `q` and one elsewhere. It scales `c a` by `ω ^ m` with `0 < m ≤ N`, so
> `c a = 0`. The quarter turn in the plane of two labels `p` and `q` is a signed transposition, and
> it gives `c (swap p q ∘ σ) = -c σ` for every permutation `σ`. By induction over transpositions
> `c σ = sign σ * c id`, and so `c = c id • ε`. On anti-fundamental indices `g` acts through its
> complex conjugate, itself an element of `SU(N)`, and the same holds (E).
>
> The invariant tensors are therefore the line through the Levi-Civita tensor. For `N = 2` the
> Levi-Civita tensors are the antisymmetric symbols `epsilonFund` and `epsilonAntiFund`, so the
> invariant tensors with two fundamental, or two anti-fundamental, indices of `SU(2)` are the line
> through `ε` (F). For `N ≥ 3` there are none with two such indices, which is a centre argument
> (`PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.CentreEigenspace`).
>
> A family indexed by `Fin n → Fin N` is the map `liftComponents T` out of these tensors, and for
> `SU(2)` the invariants of the span of such a family with two indices reduce to the epsilon
> contraction `T ![0, 1] - T ![1, 0]` (G).

## ii. Key results

> - `suTensor.leviCivitaCoeff` : the Levi-Civita symbol.
> - `suTensor.sum_prod_mul_leviCivitaCoeff` : contracting it with the rows of a matrix gives the
>   determinant.
> - `suTensor.leviCivitaFund`, `suTensor.leviCivitaAntiFund` : the Levi-Civita tensors.
> - `suTensor.invariants_fund_pow_eq_span_leviCivitaFund` : the invariant tensors with `N`
>   fundamental indices are the line through it, and its anti-fundamental twin.
> - `suTensor.epsilonFund`, `suTensor.epsilonAntiFund` : the antisymmetric symbols of `SU(2)`.
> - `suTensor.leviCivitaFund_two` : for `SU(2)` the Levi-Civita tensor is the antisymmetric symbol.
> - `suTensor.invariants_fund_pow_two_eq_span_epsilonFund` : the invariant tensors with two
>   fundamental indices of `SU(2)` are the line through `ε`, and its anti-fundamental twin.
> - `suTensor.invariantReductionToEpsilonFund` : the reduction of the invariants of the span of a
>   family to the epsilon contraction, and its anti-fundamental twin.

## iv. References

> * None.

## A. Tensors with fundamental or with anti-fundamental indices

**`suTensor.basis_repr_smul_fund`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L97).

> The components of `g • t` for a tensor with `n` fundamental indices, with one factor of `g` per
> index.

```lean
lemma basis_repr_smul_fund {n : ℕ} (g : SU N) (t : (suTensor N).Tensor fun _ : Fin n => .fund)
    (φ : Fin n → Fin N) :
    (Tensor.basis _).repr (g • t) φ
      = ∑ ψ : Fin n → Fin N, (∏ i, g.1 (φ i) (ψ i)) * (Tensor.basis _).repr t ψ
```

**`suTensor.basis_repr_smul_antiFund`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L108).

> The components of `g • t` for a tensor with `n` anti-fundamental indices, with one factor of the
> complex conjugate of `g` per index.

```lean
lemma basis_repr_smul_antiFund {n : ℕ} (g : SU N)
    (t : (suTensor N).Tensor fun _ : Fin n => .antiFund) (φ : Fin n → Fin N) :
    (Tensor.basis _).repr (g • t) φ = ∑ ψ : Fin n → Fin N,
      (∏ i, starRingEnd ℂ (g.1 (φ i) (ψ i))) * (Tensor.basis _).repr t ψ
```

## B. The Levi-Civita symbol

**`suTensor.leviCivitaCoeff`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L127).

> The Levi-Civita symbol `ε_a` of `N` labels. It is the sign of `a` when `a` is a permutation of
> `Fin N`, and zero when a label repeats.

```lean
def leviCivitaCoeff (a : Fin N → Fin N) : ℂ
```

**`suTensor.sum_mul_leviCivitaCoeff`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L131).

> A sum against the Levi-Civita symbol is a signed sum over the permutations.

```lean
lemma sum_mul_leviCivitaCoeff (F : (Fin N → Fin N) → ℂ) :
    ∑ a, F a * leviCivitaCoeff a = ∑ σ : Perm (Fin N), (Perm.sign σ : ℂ) * F σ
```

**`suTensor.leviCivitaCoeff_perm`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L139).

> The Levi-Civita symbol at a permutation is its sign.

```lean
lemma leviCivitaCoeff_perm (σ : Perm (Fin N)) : leviCivitaCoeff ⇑σ = (Perm.sign σ : ℂ)
```

**`suTensor.leviCivitaCoeff_of_not_injective`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L145).

> The Levi-Civita symbol vanishes when a label repeats.

```lean
lemma leviCivitaCoeff_of_not_injective {a : Fin N → Fin N} (ha : ¬ Function.Injective a) :
    leviCivitaCoeff a = 0
```

**`suTensor.leviCivitaCoeff_id`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L154).

> The Levi-Civita symbol at the identity is one.

```lean
lemma leviCivitaCoeff_id : leviCivitaCoeff (id : Fin N → Fin N) = 1
```

**`suTensor.sum_prod_mul_leviCivitaCoeff`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L159).

> Contracting the indices of the Levi-Civita symbol with the rows `a` of a matrix `M` gives
> `ε_a det M`.

```lean
lemma sum_prod_mul_leviCivitaCoeff (M : Matrix (Fin N) (Fin N) ℂ) (a : Fin N → Fin N) :
    ∑ b, (∏ i, M (a i) (b i)) * leviCivitaCoeff b = leviCivitaCoeff a * M.det
```

## C. The Levi-Civita tensors are invariant

**`suTensor.leviCivitaFund`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L181).

> The Levi-Civita tensor `ε^{a₁ … a_N}` with `N` fundamental indices.

```lean
noncomputable def leviCivitaFund : (suTensor N).Tensor fun _ : Fin N => .fund
```

**`suTensor.leviCivitaAntiFund`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L187).

> The Levi-Civita tensor `ε_{a₁ … a_N}` with `N` anti-fundamental indices.

```lean
noncomputable def leviCivitaAntiFund : (suTensor N).Tensor fun _ : Fin N => .antiFund
```

**`suTensor.basis_repr_leviCivitaFund`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L191).

```lean
lemma basis_repr_leviCivitaFund (a : Fin N → Fin N) :
    (Tensor.basis _).repr (leviCivitaFund N) a = leviCivitaCoeff a
```

**`suTensor.basis_repr_leviCivitaAntiFund`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L195).

```lean
lemma basis_repr_leviCivitaAntiFund (a : Fin N → Fin N) :
    (Tensor.basis _).repr (leviCivitaAntiFund N) a = leviCivitaCoeff a
```

**`suTensor.det_val`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L199).

```lean
lemma det_val (g : SU N) : g.1.det = 1
```

**`suTensor.det_map_star_val`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L202).

> The complex conjugate of an element of `SU(N)` has determinant one.

```lean
lemma det_map_star_val (g : SU N) : (g.1.map star).det = 1
```

**`suTensor.leviCivitaFund_invariant`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L209).

> The Levi-Civita tensor with `N` fundamental indices is invariant, since `g^{⊗N}` scales it by
> `det g = 1`.

```lean
lemma leviCivitaFund_invariant (g : SU N) : g • leviCivitaFund N = leviCivitaFund N
```

**`suTensor.leviCivitaAntiFund_invariant`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L217).

> The Levi-Civita tensor with `N` anti-fundamental indices is invariant, since `ḡ^{⊗N}` scales it
> by the conjugate of `det g = 1`.

```lean
lemma leviCivitaAntiFund_invariant (g : SU N) :
    g • leviCivitaAntiFund N = leviCivitaAntiFund N
```

## D. Components fixed by `SU(N)`

**`suTensor.quarterTurn_val_apply`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L232).

> The quarter turn in the plane of `p` and `q` is the signed transposition sending `e_p` to
> `e_q` and `e_q` to `-e_p`.

```lean
lemma quarterTurn_val_apply {p q : Fin N} (hpq : p ≠ q) (x y : Fin N) :
    (planeEmbed p q hpq (rotation 0 1 (by norm_num))).1 x y
      = (if x = p then -1 else 1) * (if swap p q x = y then 1 else 0)
```

**`suTensor.eq_prod_mul_of_diagonal`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L250).

> A diagonal element of `SU(N)` scales each component by the product of its diagonal entries at
> the labels.

```lean
lemma eq_prod_mul_of_diagonal {g : SU N} {d : Fin N → ℂ} (hg : g.1 = diagonal d)
    (a : Fin N → Fin N) : c a = (∏ i, d (a i)) * c a
```

**`suTensor.eq_zero_of_not_injective`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L262).

> A component with a repeated label vanishes. Some label `q` is then missed, and the diagonal
> element with `ω` at `p = a q`, `ω̄` at `q` and one elsewhere, for `ω` a primitive `(N + 1)`-th
> root of unity, scales the component by `ω ^ m`, with `m` the number of labels equal to `p`.

```lean
lemma eq_zero_of_not_injective {a : Fin N → Fin N} (ha : ¬ Function.Injective a) : c a = 0
```

**`suTensor.prod_quarterTurn_val`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L285).

> The product of the quarter turn's entries along a permutation `σ` and labels `b` is `-1` when
> `b` is `swap p q ∘ σ` and zero otherwise.

```lean
lemma prod_quarterTurn_val {p q : Fin N} (hpq : p ≠ q) (σ : Perm (Fin N)) (b : Fin N → Fin N) :
    ∏ i, (planeEmbed p q hpq (rotation 0 1 (by norm_num))).1 (σ i) (b i)
      = if b = ⇑(swap p q * σ) then -1 else 0
```

**`suTensor.swap_mul_eq_neg`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L298).

> The quarter turn in the plane of `p` and `q` gives `c (swap p q ∘ σ) = -c σ`.

```lean
lemma swap_mul_eq_neg {p q : Fin N} (hpq : p ≠ q) (σ : Perm (Fin N)) :
    c ⇑(swap p q * σ) = -c σ
```

**`suTensor.eq_sign_mul`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L307).

> The component at a permutation is its sign times the component at the identity.

```lean
lemma eq_sign_mul (σ : Perm (Fin N)) : c σ = (Perm.sign σ : ℂ) * c id
```

**`suTensor.eq_mul_leviCivitaCoeff`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L317).

> Components fixed by `SU(N)` are those of a multiple of the Levi-Civita symbol.

```lean
lemma eq_mul_leviCivitaCoeff (a : Fin N → Fin N) : c a = c id * leviCivitaCoeff a
```

## E. The invariant tensors

**`suTensor.invariants_fund_pow_eq_span_leviCivitaFund`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L333).

> The invariant tensors with `N` fundamental indices of `SU(N)` are the line through the
> Levi-Civita tensor.

```lean
lemma invariants_fund_pow_eq_span_leviCivitaFund :
    ((suTensor N).tensorRep fun _ : Fin N => .fund).invariants = ℂ ∙ leviCivitaFund N
```

**`suTensor.starElem`**, a def, [line 344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L344).

> The complex conjugate of an element of `SU(N)`, itself an element of `SU(N)`.

```lean
noncomputable def starElem (g : SU N) : SU N
```

**`suTensor.starElem_val`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L349).

```lean
lemma starElem_val (g : SU N) : (starElem g).1 = g.1.map star
```

**`suTensor.invariants_antiFund_pow_eq_span_leviCivitaAntiFund`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L354).

> The invariant tensors with `N` anti-fundamental indices of `SU(N)` are the line through the
> Levi-Civita tensor. Here `g` acts through its complex conjugate, which runs over `SU(N)` with
> `g`.

```lean
lemma invariants_antiFund_pow_eq_span_leviCivitaAntiFund :
    ((suTensor N).tensorRep fun _ : Fin N => .antiFund).invariants
      = ℂ ∙ leviCivitaAntiFund N
```

## F. Two indices of `SU(2)`: the antisymmetric symbol

**`suTensor.epsilonFund`**, a def, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L374).

> The antisymmetric symbol `ε^{ab}` with two fundamental indices of `SU(2)`.

```lean
noncomputable def epsilonFund : (suTensor 2).Tensor fun _ : Fin 2 => .fund
```

**`suTensor.epsilonAntiFund`**, a def, [line 378](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L378).

> The antisymmetric symbol `ε_{ab}` with two anti-fundamental indices of `SU(2)`.

```lean
noncomputable def epsilonAntiFund : (suTensor 2).Tensor fun _ : Fin 2 => .antiFund
```

**`suTensor.basis_repr_epsilonFund`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L382).

> The components of the antisymmetric symbol.

```lean
lemma basis_repr_epsilonFund (φ : Fin 2 → Fin 2) :
    (Tensor.basis _).repr epsilonFund φ
      = (if φ = ![0, 1] then 1 else 0) - (if φ = ![1, 0] then 1 else 0)
```

**`suTensor.basis_repr_epsilonAntiFund`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L388).

> The components of the antisymmetric symbol.

```lean
lemma basis_repr_epsilonAntiFund (φ : Fin 2 → Fin 2) :
    (Tensor.basis _).repr epsilonAntiFund φ
      = (if φ = ![0, 1] then 1 else 0) - (if φ = ![1, 0] then 1 else 0)
```

**`suTensor.leviCivitaCoeff_two`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L394).

> On two labels the Levi-Civita symbol is `1` at `01`, `-1` at `10` and `0` otherwise.

```lean
lemma leviCivitaCoeff_two (a : Fin 2 → Fin 2) :
    leviCivitaCoeff a = (if a = ![0, 1] then 1 else 0) - (if a = ![1, 0] then 1 else 0)
```

**`suTensor.leviCivitaFund_two`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L421).

> For `SU(2)` the Levi-Civita tensor with two fundamental indices is the antisymmetric
> symbol.

```lean
lemma leviCivitaFund_two : leviCivitaFund 2 = epsilonFund
```

**`suTensor.leviCivitaAntiFund_two`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L427).

> For `SU(2)` the Levi-Civita tensor with two anti-fundamental indices is the antisymmetric
> symbol.

```lean
lemma leviCivitaAntiFund_two : leviCivitaAntiFund 2 = epsilonAntiFund
```

**`suTensor.epsilonFund_invariant`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L433).

> The antisymmetric symbol with two fundamental indices is invariant, being the Levi-Civita
> tensor of `SU(2)`.

```lean
lemma epsilonFund_invariant (g : SU 2) : g • epsilonFund = epsilonFund
```

**`suTensor.epsilonAntiFund_invariant`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L439).

> The antisymmetric symbol with two anti-fundamental indices is invariant, being the Levi-Civita
> tensor of `SU(2)`.

```lean
lemma epsilonAntiFund_invariant (g : SU 2) : g • epsilonAntiFund = epsilonAntiFund
```

**`suTensor.invariants_fund_pow_two_eq_span_epsilonFund`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L445).

> The invariant tensors with two fundamental indices of `SU(2)` are the line through the
> antisymmetric symbol, the Levi-Civita tensor of `SU(2)`.

```lean
lemma invariants_fund_pow_two_eq_span_epsilonFund :
    ((suTensor 2).tensorRep fun _ : Fin 2 => .fund).invariants = ℂ ∙ epsilonFund
```

**`suTensor.invariants_antiFund_pow_two_eq_span_epsilonAntiFund`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L452).

> The invariant tensors with two anti-fundamental indices of `SU(2)` are the line through the
> antisymmetric symbol, the Levi-Civita tensor of `SU(2)`.

```lean
lemma invariants_antiFund_pow_two_eq_span_epsilonAntiFund :
    ((suTensor 2).tensorRep fun _ : Fin 2 => .antiFund).invariants = ℂ ∙ epsilonAntiFund
```

## G. Maps from components

**`suTensor.liftComponents_fund_smul_of_law`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L467).

> A linear map moving a family with `n` fundamental labels by one factor of `g` per label
> intertwines the map of the family with the action of `g`.

```lean
lemma liftComponents_fund_smul_of_law {n : ℕ} (T : (Fin n → Fin N) → B) {σ : B →ₗ[ℂ] B} (g : SU N)
    (hσ : ∀ l : Fin n → Fin N, σ (T l) = ∑ a : Fin n → Fin N, (∏ i, g.1 (a i) (l i)) • T a)
    (t : (suTensor N).Tensor fun _ : Fin n => .fund) :
    σ (liftComponents (S := suTensor N) (c := fun _ : Fin n => .fund) T t)
      = liftComponents (S := suTensor N) (c := fun _ : Fin n => .fund) T (g • t)
```

**`suTensor.liftComponents_antiFund_smul_of_law`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L481).

> A linear map moving a family with `n` anti-fundamental labels by one factor of the complex
> conjugate of `g` per label intertwines the map of the family with the action of `g`.

```lean
lemma liftComponents_antiFund_smul_of_law {n : ℕ} (T : (Fin n → Fin N) → B) {σ : B →ₗ[ℂ] B}
    (g : SU N) (hσ : ∀ l : Fin n → Fin N, σ (T l)
      = ∑ a : Fin n → Fin N, (∏ i, starRingEnd ℂ (g.1 (a i) (l i))) • T a)
    (t : (suTensor N).Tensor fun _ : Fin n => .antiFund) :
    σ (liftComponents (S := suTensor N) (c := fun _ : Fin n => .antiFund) T t)
      = liftComponents (S := suTensor N) (c := fun _ : Fin n => .antiFund) T (g • t)
```

**`suTensor.isEquivariant_liftComponents_fund`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L497).

> The map of a family with `n` fundamental labels is equivariant when the family moves by one
> factor of `g` per label, the summed label first.

```lean
lemma isEquivariant_liftComponents_fund {n : ℕ} (T : (Fin n → Fin N) → B)
    (hT : ∀ (g : SU N) (l : Fin n → Fin N), ρ g (T l)
      = ∑ a : Fin n → Fin N, (∏ i, g.1 (a i) (l i)) • T a) :
    (suTensor N).IsEquivariant (fun _ => .fund) ρ (liftComponents T)
```

**`suTensor.isEquivariant_liftComponents_antiFund`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L505).

> The map of a family with `n` anti-fundamental labels is equivariant when the family moves by
> one factor of the complex conjugate of `g` per label, the summed label first.

```lean
lemma isEquivariant_liftComponents_antiFund {n : ℕ} (T : (Fin n → Fin N) → B)
    (hT : ∀ (g : SU N) (l : Fin n → Fin N), ρ g (T l)
      = ∑ a : Fin n → Fin N, (∏ i, starRingEnd ℂ (g.1 (a i) (l i))) • T a) :
    (suTensor N).IsEquivariant (fun _ => .antiFund) ρ (liftComponents T)
```

**`suTensor.liftComponents_epsilonFund`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L513).

> The map of a family with two fundamental labels sends the antisymmetric symbol to the
> epsilon contraction.

```lean
lemma liftComponents_epsilonFund (T : (Fin 2 → Fin 2) → B) :
    liftComponents (S := suTensor 2) (c := fun _ : Fin 2 => .fund) T epsilonFund
      = T ![0, 1] - T ![1, 0]
```

**`suTensor.liftComponents_epsilonAntiFund`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L520).

> The map of a family with two anti-fundamental labels sends the antisymmetric symbol to the
> epsilon contraction.

```lean
lemma liftComponents_epsilonAntiFund (T : (Fin 2 → Fin 2) → B) :
    liftComponents (S := suTensor 2) (c := fun _ : Fin 2 => .antiFund) T epsilonAntiFund
      = T ![0, 1] - T ![1, 0]
```

**`suTensor.invariantReductionToEpsilonFund`**, a def, [line 527](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L527).

> For a family with two fundamental labels of `SU(2)` whose map is equivariant, the invariants
> of the span reduce to the span of the epsilon contraction `T ![0, 1] - T ![1, 0]`.

```lean
noncomputable def invariantReductionToEpsilonFund {ρ : Representation ℂ (SU 2) B}
    {T : (Fin 2 → Fin 2) → B}
    (hT : (suTensor 2).IsEquivariant (fun _ => .fund) ρ (liftComponents T)) :
    InvariantReductionToSpan (fun g : SU 2 => ρ g) (Submodule.span ℂ (Set.range T))
```

**`suTensor.invariantReductionToEpsilonAntiFund`**, a def, [line 538](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean#L538).

> For a family with two anti-fundamental labels of `SU(2)` whose map is equivariant, the
> invariants of the span reduce to the span of the epsilon contraction
> `T ![0, 1] - T ![1, 0]`.

```lean
noncomputable def invariantReductionToEpsilonAntiFund {ρ : Representation ℂ (SU 2) B}
    {T : (Fin 2 → Fin 2) → B}
    (hT : (suTensor 2).IsEquivariant (fun _ => .antiFund) ρ (liftComponents T)) :
    InvariantReductionToSpan (fun g : SU 2 => ρ g) (Submodule.span ℂ (Set.range T))
```

## Depends on

- [The complex tensor species of `SU(N)`](globalgaugegroup-su-tensorspecies.md)

## Proof depends on

- [What commutes with the adjoint action of `SU(N)`, and the Reynolds element of its tensors](globalgaugegroup-su-invariants-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivita.lean)
