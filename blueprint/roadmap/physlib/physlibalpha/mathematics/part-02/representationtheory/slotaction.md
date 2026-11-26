---
declaration: module
origin: cited
lean: SlotAction.act, SlotAction.transform, SlotAction.transform_apply, SlotAction.act_eq_transform, SlotAction.sum_transform_mul_prod, SlotAction.act_transform, SlotAction.transform_transform, SlotAction.transform_one
statement: formalized
proof: formalized
---

# Matrices acting slot by slot on coefficient functions

The module `PhyslibAlpha.Mathematics.RepresentationTheory.SlotAction`, [PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean): 15 declarations, 15 with a docstring.

> A matrix acting on each index of a coefficient function, and its infinitesimal version.

## i. Overview

> A coefficient function `C : (ι → κ) → ℂ` has one index of type `κ` in each slot `s : ι`. A matrix
> `K` on `κ` acts on it one factor per slot, `(act K C) a = ∑_b C_b ∏_s K_{a_s b_s}`, which is how a
> group acts on the components of a tensor with `|ι|` indices of the same kind (A). A matrix `T`
> from `κ` to `κ'` likewise changes every index at once (`transform`). It intertwines the actions of
> `K` and `K'` as soon as it does so on a single slot, and it is injective as soon as it has a left
> inverse on a single slot (B).
>
> For a family `K t` with `K 0 = 1` and derivative `N` at `0`, the derivative of `act (K t) C` is the
> infinitesimal action `infinitesimalAct N C`, which applies `N` to one slot at a time. The same
> holds with a different matrix, and even a different kind of index, in each slot. So a coefficient
> function fixed by every `K t` is killed by `infinitesimalAct N` (C). With two indices `κ × κ'` in a
> slot, a pair of matrices acts on them one factor per kind, `pairMatrix` (D).

## ii. Key results

> - `SlotAction.act` : a matrix acting on every slot of a coefficient function.
> - `SlotAction.transform` : a change of every index, as a linear map.
> - `SlotAction.act_transform` : the change intertwines two actions if it does so on one slot.
> - `SlotAction.transform_injective` : the change is injective if it has a left inverse on one slot.
> - `SlotAction.infinitesimalAct` : the infinitesimal action of a matrix, one slot at a time.
> - `SlotAction.hasDerivAt_sum_mul_prod` : the derivative of the action of a one-parameter family,
>   with a matrix for each slot, is its infinitesimal action.
> - `SlotAction.infinitesimalAct_eq_zero_of_act_eq` : a coefficient function fixed by a
>   one-parameter family is killed by its derivative at the identity.
> - `SlotAction.pairMatrix` : a pair of matrices acting on two kinds of index.

## iv. References

> * None.

## A. The action of a matrix on every slot

**`SlotAction.act`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L75).

> A matrix `K` acting on every slot of a coefficient function, one factor per slot,
> `(act K C) a = ∑_b C_b ∏_s K_{a_s b_s}`, with `a` free and `b` summed.

```lean
def act (K : κ → κ → ℂ) (C : (ι → κ) → ℂ) (a : ι → κ) : ℂ
```

## B. Changing every index

**`SlotAction.transform`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L85).

> A matrix `T` from `κ` to `κ'` changing every index of a coefficient function,
> `(transform T C) α = ∑_d C_d ∏_s T_{d_s α_s}`.

```lean
def transform (T : κ → κ' → ℂ) : ((ι → κ) → ℂ) →ₗ[ℂ] ((ι → κ') → ℂ)
```

**`SlotAction.transform_apply`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L96).

> The change of every index by `T`, entrywise.

```lean
lemma transform_apply (T : κ → κ' → ℂ) (C : (ι → κ) → ℂ) (α : ι → κ') :
    transform T C α = ∑ d, C d * ∏ s, T (d s) (α s)
```

**`SlotAction.act_eq_transform`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L100).

> The action of `K` is the change by the transposed matrix.

```lean
lemma act_eq_transform (K : κ → κ → ℂ) (C : (ι → κ) → ℂ) :
    act K C = transform (fun d a => K a d) C
```

**`SlotAction.sum_transform_mul_prod`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L105).

> Contracting a changed coefficient function against a product over the slots is a sum over
> the old indices, slot by slot.

```lean
lemma sum_transform_mul_prod (T : κ → κ' → ℂ) (C : (ι → κ) → ℂ) (F : ι → κ' → ℂ) :
    ∑ β, transform T C β * ∏ s, F s (β s) = ∑ d, C d * ∏ s, ∑ p, T (d s) p * F s p
```

**`SlotAction.act_transform`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L116).

> A change of every index intertwines the actions of `K` and `K'` as soon as it does so on a
> single slot.

```lean
lemma act_transform {T : κ → κ' → ℂ} {K : κ → κ → ℂ} {K' : κ' → κ' → ℂ}
    (hT : ∀ μ q, ∑ p, T μ p * K' q p = ∑ ν, K ν μ * T ν q) (C : (ι → κ) → ℂ) :
    act K' (transform T C) = transform T (act K C)
```

**`SlotAction.transform_transform`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L126).

> Two changes of every index compose slot by slot.

```lean
lemma transform_transform (T : κ → κ' → ℂ) (T' : κ' → κ'' → ℂ) (C : (ι → κ) → ℂ) :
    transform T' (transform T C) = transform (fun μ ν => ∑ p, T μ p * T' p ν) C
```

**`SlotAction.transform_one`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L133).

> The identity matrix changes nothing.

```lean
lemma transform_one [DecidableEq κ] (C : (ι → κ) → ℂ) :
    transform (fun μ ν : κ => if μ = ν then (1 : ℂ) else 0) C = C
```

**`SlotAction.transform_injective`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L144).

> A change of every index with a left inverse on a single slot is injective.

```lean
lemma transform_injective [DecidableEq κ] {T : κ → κ' → ℂ} {T' : κ' → κ → ℂ}
    (hT : ∀ μ ν, ∑ p, T μ p * T' p ν = if μ = ν then 1 else 0) :
    Function.Injective (transform (ι := ι) T)
```

## C. The infinitesimal action

**`SlotAction.infinitesimalAct`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L160).

> The infinitesimal action of a matrix `N`, applied to one slot at a time,
> `(infinitesimalAct N C) a = ∑_s ∑_q N_{a_s q} C_{a[s ↦ q]}`.

```lean
def infinitesimalAct (N : κ → κ → ℂ) (C : (ι → κ) → ℂ) (a : ι → κ) : ℂ
```

**`SlotAction.sum_prod_erase_ite_mul`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L165).

> Summing over the index vectors that agree with `a` off the slot `s`, for a kind of index
> `κ s` that may depend on the slot.

```lean
lemma sum_prod_erase_ite_mul {κ : ι → Type*} [∀ s, Fintype (κ s)] [∀ s, DecidableEq (κ s)]
    (a : ∀ s, κ s) (s : ι) (G : (∀ s, κ s) → ℂ) :
    ∑ b, (∏ j ∈ univ.erase s, if a j = b j then (1 : ℂ) else 0) * G b
      = ∑ q, G (Function.update a s q)
```

**`SlotAction.hasDerivAt_sum_mul_prod`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L185).

> The derivative at the identity of the action of a one-parameter family of matrices `K t s`,
> one for each slot `s` and acting on a kind of index `κ s` that may depend on the slot, is the
> infinitesimal action of their derivatives `N s`, applied to one slot at a time.

```lean
lemma hasDerivAt_sum_mul_prod {κ : ι → Type*} [∀ s, Fintype (κ s)] [∀ s, DecidableEq (κ s)]
    {K : ℝ → ∀ s, κ s → κ s → ℂ} {N : ∀ s, κ s → κ s → ℂ}
    (h0 : ∀ s p q, K 0 s p q = if p = q then 1 else 0)
    (hK : ∀ s p q, HasDerivAt (fun t => K t s p q) (N s p q) 0) (C : (∀ s, κ s) → ℂ)
    (a : ∀ s, κ s) :
    HasDerivAt (fun t => ∑ b, C b * ∏ s, K t s (a s) (b s))
      (∑ s, ∑ q, N s (a s) q * C (Function.update a s q)) 0
```

**`SlotAction.hasDerivAt_act`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L205).

> The derivative at the identity of the action of a one-parameter family `K t` is the
> infinitesimal action of its derivative `N`.

```lean
lemma hasDerivAt_act [DecidableEq κ] {K : ℝ → κ → κ → ℂ} {N : κ → κ → ℂ}
    (h0 : ∀ p q, K 0 p q = if p = q then 1 else 0)
    (hK : ∀ p q, HasDerivAt (fun t => K t p q) (N p q) 0) (C : (ι → κ) → ℂ) (a : ι → κ) :
    HasDerivAt (fun t => act (K t) C a) (infinitesimalAct N C a) 0
```

**`SlotAction.infinitesimalAct_eq_zero_of_act_eq`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L213).

> A coefficient function fixed by every member of a one-parameter family through the identity
> is killed by the infinitesimal action of its derivative there.

```lean
lemma infinitesimalAct_eq_zero_of_act_eq [DecidableEq κ] {K : ℝ → κ → κ → ℂ} {N : κ → κ → ℂ}
    (h0 : ∀ p q, K 0 p q = if p = q then 1 else 0)
    (hK : ∀ p q, HasDerivAt (fun t => K t p q) (N p q) 0) {C : (ι → κ) → ℂ}
    (hC : ∀ t, act (K t) C = C) : infinitesimalAct N C = 0
```

## D. Two kinds of index in each slot

> With an index of `κ × κ'` in each slot, a pair of matrices acts on it one factor per kind.

**`SlotAction.pairMatrix`**, a def, [line 231](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean#L231).

> The product of two matrices, acting on an index of each kind.

```lean
def pairMatrix (K₁ : κ → κ → ℂ) (K₂ : κ' → κ' → ℂ) (p q : κ × κ') : ℂ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/SlotAction.lean)
