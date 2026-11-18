---
declaration: module
origin: cited
lean: Representation.trivial_dual_apply, Lorentz.iteratedD, Lorentz.iteratedD_zero, Lorentz.iteratedD_cons, Lorentz.iteratedD_singleton, Lorentz.iteratedD_add, Lorentz.iteratedD_cons', Lorentz.iteratedD_mul
statement: formalized
proof: formalized
---

# Class IsLorentzDeriv

The module `PhyslibAlpha.Relativity.IsLorentzDeriv`, [PhyslibAlpha/Relativity/IsLorentzDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean): 13 declarations, 10 with a docstring; 1 private, not shown.

## i. Overview

> A family of operators indexed by the four spacetime directions is a Lorentz derivative
> when the representation of `SL(2,ℂ)` intertwines it through the columns of the Lorentz
> matrix, as the jet derivatives on a jet algebra do. The iterated operator along a multiset
> of directions then transforms by one column of the Lorentz matrix per slot
> (`rep_iteratedD_ofFn`), which is the law `IsLorentzDerivTransforms` and its covariant form
> `IsLorentzCovDerivTransforms` record for a family of derivative symbols.

## ii. Key results

> - `IsLorentzDerivTransforms` : a family of derivative symbols `F : s ↦ [∂_s ψ^φ]`, indexed by the
>   dual of a value space `V` carrying a representation of `SL(2,ℂ)`, transforms as the derivative
>   symbols of a Lorentz-covariant field: each ordered symbol mixes into all tuples of directions by
>   the per-slot columns of the Lorentz matrix, while the value index transforms by the contragredient
>   action `rep.dual` on the dual of `V`
> - `IsLorentzCovDerivTransforms` : a family of *covariant*-derivative symbols, indexed by ordered
>   tuples of directions (covariant derivatives do not commute) and by the dual of a Lorentz
>   representation `V`, transforms as the covariant derivatives of a Lorentz-covariant field: each
>   derivative slot mixes by the columns of the Lorentz matrix, while the value index transforms by
>   the contragredient action `rep.dual` on the dual of `V` — the ordered-tuple analogue of
>   `IsLorentzDerivTransforms`
> - `rep_iteratedD_ofFn` : the Lorentz transformation of iterated derivatives: for a Lorentz
>   derivative the ordered derivative symbol `D_{l 0} ⋯ D_{l (n-1)} x` mixes into all tuples of
>   directions, with one Lorentz matrix factor per slot

## iv. References

> * None.

## A. Lorentz-covariant families of derivative symbols

**`Representation.trivial_dual_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L68).

> The dual of the trivial representation acts trivially.

```lean
lemma _root_.Representation.trivial_dual_apply {k G V : Type*} [CommSemiring k]
    [Group G] [AddCommMonoid V] [Module k V] (g : G) (φ : Module.Dual k V) :
    (Representation.trivial k G V).dual g φ = φ
```

**`Lorentz.iteratedD`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L78).

> The iterated operator `D_s = D_{ν₁} ⋯ D_{νₙ}` of a pairwise-commuting family of
> endomorphisms along a multiset `s` of indices. Commutativity is what makes the
> operator well-defined on a multiset, i.e. independent of any ordering of `s`.

```lean
def iteratedD {ι : Type*} (D : ι → A →ₗ[ℂ] A)
    (hD : ∀ i j, (D i).comp (D j) = (D j).comp (D i)) (s : Multiset ι) : A →ₗ[ℂ] A
```

**`Lorentz.iteratedD_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L84).

```lean
lemma iteratedD_zero {ι : Type*} (D : ι → A →ₗ[ℂ] A)
    (hD : ∀ i j, (D i).comp (D j) = (D j).comp (D i)) :
    iteratedD D hD (0 : Multiset ι) = LinearMap.id
```

**`Lorentz.iteratedD_cons`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L89).

```lean
lemma iteratedD_cons {ι : Type*} (D : ι → A →ₗ[ℂ] A)
    (hD : ∀ i j, (D i).comp (D j) = (D j).comp (D i)) (κ : ι) (s : Multiset ι) :
    iteratedD D hD (κ ::ₘ s) = (D κ).comp (iteratedD D hD s)
```

**`Lorentz.iteratedD_singleton`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L95).

> The iterated operator of a singleton is the operator itself.

```lean
lemma iteratedD_singleton {ι : Type*} (D : ι → A →ₗ[ℂ] A)
    (hD : ∀ i j, (D i).comp (D j) = (D j).comp (D i)) (κ : ι) :
    iteratedD D hD {κ} = D κ
```

**`Lorentz.iteratedD_add`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L103).

> The iterated operator is additive in the multiset of directions: applying along
> `s + t` is applying along `t` and then along `s`.

```lean
lemma iteratedD_add {ι : Type*} (D : ι → A →ₗ[ℂ] A)
    (hD : ∀ i j, (D i).comp (D j) = (D j).comp (D i)) (s t : Multiset ι) :
    iteratedD D hD (s + t) = (iteratedD D hD s).comp (iteratedD D hD t)
```

**`Lorentz.iteratedD_cons'`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L113).

> The companion of `iteratedD_cons`, peeling the new operator on the inside: for a
> commuting family the extra operator may equally be applied first.

```lean
lemma iteratedD_cons' {ι : Type*} (D : ι → A →ₗ[ℂ] A)
    (hD : ∀ i j, (D i).comp (D j) = (D j).comp (D i)) (κ : ι) (s : Multiset ι) :
    iteratedD D hD (κ ::ₘ s) = (iteratedD D hD s).comp (D κ)
```

**`Lorentz.iteratedD_mul`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L119).

```lean
lemma iteratedD_mul (D : (Fin 1 ⊕ Fin 3) → A →ₗ[ℂ] A)
    (D_comm : ∀ μ ν, (D μ).comp (D ν) = (D ν).comp (D μ))
    (D_mul : ∀ (μ : Fin 1 ⊕ Fin 3) (b₁ b₂ : A),
      D μ (b₁ * b₂) = D μ b₁ * b₂ + b₁ * D μ b₂)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (b₁ b₂ : A) :
    Lorentz.iteratedD D D_comm s (b₁ * b₂) =
      (s.antidiagonal.map fun p =>
        Lorentz.iteratedD D D_comm p.1 b₁ * Lorentz.iteratedD D D_comm p.2 b₂).sum
```

**`Lorentz.IsLorentzDeriv`**, a class, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L152).

> A family of operators indexed by the spacetime directions is a **Lorentz derivative**
> when the representation of `SL(2,ℂ)` intertwines it through the columns of the Lorentz
> matrix. The class needs only the module structure, so it applies uniformly to any
> representation space.

```lean
class IsLorentzDeriv {M : Type} [AddCommMonoid M] [Module ℂ M]
    (rep : Representation ℂ SL(2,ℂ) M) (D : (Fin 1 ⊕ Fin 3) → M →ₗ[ℂ] M) where
  rep_deriv {Λ μ x} : rep Λ (D μ x) =
    ∑ a, (((SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) • D a (rep Λ x)
```

**`Lorentz.IsLorentzDerivTransforms`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L166).

> A family of derivative symbols `F : s ↦ [∂_s ψ^φ]`, indexed by the dual of a value
> space `V` carrying a representation of `SL(2,ℂ)`, **transforms as the derivative
> symbols of a Lorentz-covariant field**: each ordered symbol mixes into all tuples of
> directions by the per-slot columns of the Lorentz matrix, while the value index
> transforms by the contragredient action `rep.dual` on the dual of `V`. This is the
> general form of the Lorentz law `GaugeAlgebraRealization.lorentz_apply`, for a field valued in an
> arbitrary Lorentz representation — the trivial representation for scalars, the Weyl
> representations for fermions, and their conjugates for the barred fields. At `n = 0`
> it reduces to the homogeneous law `Λ • F₀^φ = F₀^{Λ^{-⊤} φ}`.

```lean
def IsLorentzDerivTransforms {k V : Type*} [CommRing k] [AddCommGroup V] [Module k V]
    [Module k A]
    (repLorentz : Representation ℂ SL(2,ℂ) A) (rep : Representation k SL(2,ℂ) V)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual k V →ₗ[k] A) : Prop
```

**`Lorentz.IsLorentzCovDerivTransforms`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L182).

> A family of *covariant*-derivative symbols, indexed by ordered tuples of
> directions (covariant derivatives do not commute) and by the dual of a Lorentz
> representation `V`, **transforms as the covariant derivatives of a
> Lorentz-covariant field**: each derivative slot mixes by the columns of the Lorentz
> matrix, while the value index transforms by the contragredient action `rep.dual` on
> the dual of `V` — the ordered-tuple analogue of `IsLorentzDerivTransforms`.

```lean
def IsLorentzCovDerivTransforms {k V : Type*} [CommRing k] [AddCommGroup V]
    [Module k V] [Module k A] (repLorentz : Representation ℂ SL(2,ℂ) A)
    (rep : Representation k SL(2,ℂ) V)
    (F : {n : ℕ} → (Fin n → (Fin 1 ⊕ Fin 3)) → Module.Dual k V →ₗ[k] A) : Prop
```

**`Lorentz.IsLorentzCovDerivTransforms.neg_one_apply`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L195).

> **At the centre the derivative slots do not mix.** The element `-1` of `SL(2,ℂ)` covers
> the identity Lorentz transformation, so the sum over tuples collapses to the single term
> `p = l` and only the value index moves.

```lean
lemma IsLorentzCovDerivTransforms.neg_one_apply {k V : Type*} [CommRing k] [AddCommGroup V]
    [Module k V] [Module k A] {repLorentz : Representation ℂ SL(2,ℂ) A}
    {rep : Representation k SL(2,ℂ) V}
    {F : {n : ℕ} → (Fin n → (Fin 1 ⊕ Fin 3)) → Module.Dual k V →ₗ[k] A}
    (hF : IsLorentzCovDerivTransforms repLorentz rep F)
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual k V) :
    repLorentz (-1) (F l φ) = F l (rep.dual (-1) φ)
```

**`Lorentz.IsLorentzDeriv.rep_iteratedD_ofFn`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean#L221).

> **The Lorentz transformation of iterated derivatives**: for a Lorentz derivative the
> ordered derivative symbol `D_{l 0} ⋯ D_{l (n-1)} x` mixes into all tuples of
> directions, with one Lorentz matrix factor per slot.

```lean
lemma rep_iteratedD_ofFn [IsLorentzDeriv rep D]
    (D_comm : ∀ μ ν, (D μ).comp (D ν) = (D ν).comp (D μ))
    (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (x : A) :
    rep Λ (iteratedD D D_comm (List.ofFn l) x) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
        (∏ i, (((SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ) : ℂ)) •
          iteratedD D D_comm (List.ofFn p) (rep Λ x)
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../physlib/relativity/sl2c/basic.md)

## Proof depends on

- [Conjugation and the kernel of the covering map](sl2c/basic.md)

## Sources

- [PhyslibAlpha/Relativity/IsLorentzDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/IsLorentzDeriv.lean)
