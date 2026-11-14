---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.IsTensorIntertwiner, PhyslibAlpha.Sl2.IsTensorIntertwiner.smul, PhyslibAlpha.Sl2.IsTensorIntertwiner.add, PhyslibAlpha.Sl2.component_sumEnd, PhyslibAlpha.Sl2.cgProj, PhyslibAlpha.Sl2.cgProj_apply, PhyslibAlpha.Sl2.cgProj_isTensorIntertwiner, PhyslibAlpha.Sl2.cgProj_cgEquiv_symm_lof
statement: formalized
proof: formalized
---

# Intertwiners out of a tensor product of standard sl₂ modules

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.TensorIntertwiner`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean): 17 declarations, 12 with a docstring.

> Linear maps `V(m) ⊗ V(n) → V(p)` compatible with the diagonal `sl₂` action.

## i. Overview

> A tensor intertwiner is a linear map `φ : V(m) ⊗ V(n) → V(p)` that carries the diagonal raising,
> lowering and weight operators of `V(m) ⊗ V(n)` to those of `V(p)`. Composing with the inverse of
> the Clebsch–Gordan isomorphism `cgEquiv : V(m) ⊗ V(n) ≃ ⨁_j V(m + n - 2j)` gives, on each summand,
> an intertwiner `V(m + n - 2j) → V(p)`. By Schur's lemma these vanish unless `m + n - 2j = p`, and
> the summand with `m + n - 2j = p` contributes a scalar multiple of the identity. Hence:
>
> - if `p` is not of the form `m + n - 2j` with `j ≤ min m n`, every tensor intertwiner is zero;
> - if `p = m + n - 2j`, every tensor intertwiner is a scalar multiple of the projection `cgProj`
>   onto the summand `V(m + n - 2j)`, and this projection is not zero.
>
> In physics notation (`m = 2j₁`, `n = 2j₂`, `p = 2J`) the condition is the triangle rule
> `|j₁ - j₂| ≤ J ≤ j₁ + j₂` together with `j₁ + j₂ - J ∈ ℕ`.

## ii. Key results

> - `IsTensorIntertwiner` is the predicate for tensor intertwiners.
> - `cgProj` is the projection onto a summand of the Clebsch–Gordan decomposition, and
>   `cgProj_isTensorIntertwiner` shows that it is a tensor intertwiner.
> - `IsTensorIntertwiner.eq_zero_of_forall_ne` is the selection rule.
> - `IsTensorIntertwiner.exists_eq_smul_cgProj` shows that a tensor intertwiner onto
>   `V(m + n - 2j)` is a multiple of `cgProj`.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Tensor intertwiners

### A.1. Definition and closure properties

**`PhyslibAlpha.Sl2.IsTensorIntertwiner`**, a structure, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L73).

> A linear map `V(m) ⊗ V(n) → V(p)` is a tensor intertwiner if it carries the diagonal raising,
> lowering and weight operators on `V(m) ⊗ V(n)` to those on `V(p)`.

```lean
structure IsTensorIntertwiner
    (φ : StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K] StandardSl2Module K p) : Prop where
  comm_E : φ ∘ₗ tensorE m n = ρE ∘ₗ φ
  comm_F : φ ∘ₗ tensorF m n = ρF ∘ₗ φ
  comm_H : φ ∘ₗ tensorH m n = ρH ∘ₗ φ
```

**`PhyslibAlpha.Sl2.IsTensorIntertwiner.smul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L84).

> Scalar multiples of tensor intertwiners are tensor intertwiners.

```lean
lemma smul (hφ : IsTensorIntertwiner φ) (c : K) : IsTensorIntertwiner (c • φ)
```

**`PhyslibAlpha.Sl2.IsTensorIntertwiner.add`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L90).

> Sums of tensor intertwiners are tensor intertwiners.

```lean
lemma add (hφ : IsTensorIntertwiner φ) (hψ : IsTensorIntertwiner ψ) :
    IsTensorIntertwiner (φ + ψ)
```

### A.2. The Clebsch–Gordan projections

**`PhyslibAlpha.Sl2.component_sumEnd`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L105).

> The component of a direct sum commutes with a summand-wise endomorphism.

```lean
lemma component_sumEnd (A : ∀ j, Module.End K (CGSummand K m n j)) (j : Fin (min m n + 1))
    (y : CGSum K m n) :
    DirectSum.component K _ (CGSummand K m n) j (sumEnd A y) =
      A j (DirectSum.component K _ (CGSummand K m n) j y)
```

**`PhyslibAlpha.Sl2.cgProj`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L116).

> The projection of `V(m) ⊗ V(n)` onto the summand `V(m + n - 2j)` of the Clebsch–Gordan
> decomposition.

```lean
def cgProj (hmn : 0 < m + n) (j : Fin (min m n + 1)) :
    StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K]
      StandardSl2Module K (m + n - 2 * (j : ℕ))
```

**`PhyslibAlpha.Sl2.cgProj_apply`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L121).

```lean
lemma cgProj_apply (hmn : 0 < m + n) (j : Fin (min m n + 1))
    (x : StandardSl2Module K m ⊗[K] StandardSl2Module K n) :
    cgProj hmn j x = DirectSum.component K _ (CGSummand K m n) j (cgEquiv hmn x)
```

**`PhyslibAlpha.Sl2.cgProj_isTensorIntertwiner`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L126).

> The projections are tensor intertwiners.

```lean
lemma cgProj_isTensorIntertwiner (hmn : 0 < m + n) (j : Fin (min m n + 1)) :
    IsTensorIntertwiner (cgProj (K := K) hmn j)
```

**`PhyslibAlpha.Sl2.cgProj_cgEquiv_symm_lof`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L137).

> The projection sends the preimage of the highest-weight vector of the `j`-th summand to that
> vector; in particular it is not zero.

```lean
lemma cgProj_cgEquiv_symm_lof (hmn : 0 < m + n) (j : Fin (min m n + 1))
    (z : CGSummand K m n j) :
    cgProj hmn j ((cgEquiv hmn).symm (DirectSum.lof K _ (CGSummand K m n) j z)) = z
```

**`PhyslibAlpha.Sl2.cgProj_ne_zero`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L142).

```lean
lemma cgProj_ne_zero (hmn : 0 < m + n) (j : Fin (min m n + 1)) :
    cgProj (K := K) hmn j ≠ 0
```

### A.3. Restriction to the summands

**`PhyslibAlpha.Sl2.cgEquiv_symm_sumEnd_E`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L160).

```lean
lemma cgEquiv_symm_sumEnd_E (y : CGSum K m n) :
    (cgEquiv hmn).symm (sumEnd (fun _ => ρE) y) = tensorE m n ((cgEquiv hmn).symm y)
```

**`PhyslibAlpha.Sl2.cgEquiv_symm_sumEnd_F`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L164).

```lean
lemma cgEquiv_symm_sumEnd_F (y : CGSum K m n) :
    (cgEquiv hmn).symm (sumEnd (fun _ => ρF) y) = tensorF m n ((cgEquiv hmn).symm y)
```

**`PhyslibAlpha.Sl2.cgEquiv_symm_sumEnd_H`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L168).

```lean
lemma cgEquiv_symm_sumEnd_H (y : CGSum K m n) :
    (cgEquiv hmn).symm (sumEnd (fun _ => ρH) y) = tensorH m n ((cgEquiv hmn).symm y)
```

**`PhyslibAlpha.Sl2.cgRestrict`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L174).

> The restriction of a linear map on `V(m) ⊗ V(n)` to the `j`-th summand of the
> Clebsch–Gordan decomposition.

```lean
def cgRestrict
    (φ : StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K] StandardSl2Module K p)
    (j : Fin (min m n + 1)) : CGSummand K m n j →ₗ[K] StandardSl2Module K p
```

**`PhyslibAlpha.Sl2.IsTensorIntertwiner.cgRestrict_isIntertwiner`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L184).

> The restriction of a tensor intertwiner to a summand is an intertwiner.

```lean
lemma cgRestrict_isIntertwiner (hφ : IsTensorIntertwiner φ) (j : Fin (min m n + 1)) :
    IsIntertwiner (cgRestrict hmn φ j)
```

### A.4. Selection rule and uniqueness

**`PhyslibAlpha.Sl2.IsTensorIntertwiner.eq_of_cgRestrict_eq`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L215).

> A linear map on `V(m) ⊗ V(n)` is determined by its restrictions to the summands.

```lean
lemma eq_of_cgRestrict_eq (hmn : 0 < m + n) {M : Type*} [AddCommGroup M] [Module K M]
    {α β : StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K] M}
    (h : ∀ j, α ∘ₗ (cgEquiv hmn).symm.toLinearMap ∘ₗ DirectSum.lof K _ (CGSummand K m n) j =
      β ∘ₗ (cgEquiv hmn).symm.toLinearMap ∘ₗ DirectSum.lof K _ (CGSummand K m n) j) :
    α = β
```

**`PhyslibAlpha.Sl2.IsTensorIntertwiner.eq_zero_of_forall_ne`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L230).

> **Selection rule.** If `p` is not of the form `m + n - 2j` with `j ≤ min m n`, every tensor
> intertwiner `V(m) ⊗ V(n) → V(p)` is zero.

```lean
lemma eq_zero_of_forall_ne (hmn : 0 < m + n)
    {φ : StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K] StandardSl2Module K p}
    (hφ : IsTensorIntertwiner φ) (hp : ∀ j : Fin (min m n + 1), m + n - 2 * (j : ℕ) ≠ p) :
    φ = 0
```

**`PhyslibAlpha.Sl2.IsTensorIntertwiner.exists_eq_smul_cgProj`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean#L240).

> Every tensor intertwiner onto the summand `V(m + n - 2j)` is a scalar multiple of the
> projection `cgProj`.

```lean
lemma exists_eq_smul_cgProj (hmn : 0 < m + n) {j : Fin (min m n + 1)}
    {φ : StandardSl2Module K m ⊗[K] StandardSl2Module K n →ₗ[K]
      StandardSl2Module K (m + n - 2 * (j : ℕ))}
    (hφ : IsTensorIntertwiner φ) : ∃ c : K, φ = c • cgProj hmn j
```

## Depends on

- [Schur's lemma for the standard sl₂ modules](sl2-schur.md)
- [The equivariant Clebsch–Gordan decomposition](sl2-tensordecomposition.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/TensorIntertwiner.lean)
