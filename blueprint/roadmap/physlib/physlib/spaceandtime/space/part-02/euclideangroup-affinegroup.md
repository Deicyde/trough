---
declaration: module
origin: cited
lean: EuclideanGroup.orthogonalToLinearIsometryEquiv, EuclideanGroup.orthogonalToLinearIsometryEquiv_apply, EuclideanGroup.toAffineIsometryHom, EuclideanGroup.toAffineIsometryHom_apply, AffineIsometryEquiv.toAffineEquivHom, EuclideanGroup.toAffineEquiv, EuclideanGroup.linearIsometryEquivToOrthogonal, EuclideanGroup.orthogonalToLinearIsometryEquiv_left_inv
statement: formalized
proof: formalized
---

# The inclusion of the Euclidean group into the affine automorphism group

The module `Physlib.SpaceAndTime.Space.EuclideanGroup.AffineGroup`, [Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean): 12 declarations, 11 with a docstring.

> This file has two parts.
>
> **Part 1: the inclusion.** The abstract Euclidean group `EuclideanGroup n = ℝⁿ ⋊ O(n)` is
> included into Mathlib's affine automorphism group as the composite of two monoid homomorphisms
>
> `EuclideanGroup n →* AffineIsometryEquiv ℝ (EuclideanSpace ℝ (Fin n)) _ →* AffineEquiv ℝ _ _`.
>
> * `EuclideanGroup.orthogonalToLinearIsometryEquiv` : an orthogonal matrix as a linear isometry
>   equivalence of `EuclideanSpace ℝ (Fin n)`; the linear ingredient of the first leg.
> * `EuclideanGroup.toAffineIsometryHom` : the first leg, `⟨t, Q⟩ ↦ (x ↦ Q x + t)`.
> * `AffineIsometryEquiv.toAffineEquivHom` : the second leg, `AffineIsometryEquiv.toAffineEquiv`
>   as a monoid homomorphism.
> * `EuclideanGroup.toAffineEquiv` : the composite of the two legs; the result intended for use
>   elsewhere.
>
> **Part 2: strengthening the first leg to an isomorphism.** Every affine isometry of
> `EuclideanSpace ℝ (Fin n)` is `x ↦ Q x + t` for a unique orthogonal `Q` and translation `t`, so
> the first leg is in fact a group isomorphism. We record it as
> `EuclideanGroup.toAffineIsometryMulEquiv`, a `MulEquiv` whose fields are supplied as follows:
>
> * `toFun`, `map_mul'` : reused from `EuclideanGroup.toAffineIsometryHom` in part 1;
> * `invFun` : built from `EuclideanGroup.linearIsometryEquivToOrthogonal`, the inverse of the
>   linear bridge `orthogonalToLinearIsometryEquiv`;
> * `left_inv` : from the round trip `orthogonalToLinearIsometryEquiv_left_inv` together with the
>   projection lemma `linearIsometryEquiv_constVAdd_mul`;
> * `right_inv` : from the round trip `orthogonalToLinearIsometryEquiv_right_inv`.
>
> Part 2 is self-contained; nothing in part 1 depends on it.

## Part 1: the inclusion

> The chain is: `orthogonalToLinearIsometryEquiv` (linear ingredient) → `toAffineIsometryHom`
> (first leg) → `AffineIsometryEquiv.toAffineEquivHom` (second leg) → `toAffineEquiv`
> (the composite).

**`EuclideanGroup.orthogonalToLinearIsometryEquiv`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L58).

> An orthogonal matrix viewed as a linear isometry equivalence of `EuclideanSpace ℝ (Fin n)`;
> the linear ingredient of the first leg `toAffineIsometryHom`.

```lean
noncomputable def orthogonalToLinearIsometryEquiv
    (Q : Matrix.orthogonalGroup (Fin n) ℝ) :
    EuclideanSpace ℝ (Fin n) ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin n)
```

**`EuclideanGroup.orthogonalToLinearIsometryEquiv_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L68).

```lean
lemma orthogonalToLinearIsometryEquiv_apply
    (Q : Matrix.orthogonalGroup (Fin n) ℝ) (x : EuclideanSpace ℝ (Fin n)) :
    orthogonalToLinearIsometryEquiv Q x = Q • x
```

**`EuclideanGroup.toAffineIsometryHom`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L74).

> The first leg of the inclusion: `⟨t, Q⟩ ↦ (x ↦ Q x + t)`, bundled as a monoid homomorphism
> from the Euclidean group into the affine isometry group of `EuclideanSpace ℝ (Fin n)`.

```lean
noncomputable def toAffineIsometryHom :
    EuclideanGroup n →*
      AffineIsometryEquiv ℝ (EuclideanSpace ℝ (Fin n)) (EuclideanSpace ℝ (Fin n))
```

**`EuclideanGroup.toAffineIsometryHom_apply`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L88).

> Unfolds `toAffineIsometryHom` into its translation and linear factors.

```lean
lemma toAffineIsometryHom_apply (A : EuclideanGroup n) :
    toAffineIsometryHom A =
      AffineIsometryEquiv.constVAdd ℝ (EuclideanSpace ℝ (Fin n)) A.translation *
        (orthogonalToLinearIsometryEquiv A.linear).toAffineIsometryEquiv
```

**`AffineIsometryEquiv.toAffineEquivHom`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L95).

> The second leg of the inclusion: `AffineIsometryEquiv.toAffineEquiv` bundled as a monoid
> homomorphism into the affine automorphism group.

```lean
noncomputable def _root_.AffineIsometryEquiv.toAffineEquivHom :
    AffineIsometryEquiv ℝ (EuclideanSpace ℝ (Fin n)) (EuclideanSpace ℝ (Fin n)) →*
      AffineEquiv ℝ (EuclideanSpace ℝ (Fin n)) (EuclideanSpace ℝ (Fin n))
```

**`EuclideanGroup.toAffineEquiv`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L106).

> The inclusion of the Euclidean group into Mathlib's affine automorphism group: the composite
> of the two legs `toAffineIsometryHom` and `AffineIsometryEquiv.toAffineEquivHom`.

```lean
noncomputable def toAffineEquiv :
    EuclideanGroup n →* AffineEquiv ℝ (EuclideanSpace ℝ (Fin n)) (EuclideanSpace ℝ (Fin n))
```

## Part 2: strengthening the first leg to an isomorphism

> The first leg `toAffineIsometryHom` is in fact a group isomorphism: every affine isometry of
> `EuclideanSpace ℝ (Fin n)` is `x ↦ Q x + t` for a unique orthogonal `Q` and translation `t`. The
> declarations below supply the remaining fields of the `MulEquiv` `toAffineIsometryMulEquiv`, in
> field order: the `invFun` ingredient, the two lemmas proving `left_inv`, and the lemma proving
> `right_inv`. Nothing in part 1 depends on this section.

**`EuclideanGroup.linearIsometryEquivToOrthogonal`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L121).

> The `invFun` ingredient of `toAffineIsometryMulEquiv`: a linear isometry equivalence read back
> as an orthogonal matrix, inverse to the linear bridge `orthogonalToLinearIsometryEquiv` (see the
> round-trip `@[simp]` lemmas below).

```lean
noncomputable def linearIsometryEquivToOrthogonal
    (L : EuclideanSpace ℝ (Fin n) ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin n)) :
    Matrix.orthogonalGroup (Fin n) ℝ
```

**`EuclideanGroup.orthogonalToLinearIsometryEquiv_left_inv`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L137).

> `linearIsometryEquivToOrthogonal` is a left inverse of `orthogonalToLinearIsometryEquiv`.
> Together with `linearIsometryEquiv_constVAdd_mul`, this proves `left_inv` of
> `toAffineIsometryMulEquiv`.

```lean
lemma orthogonalToLinearIsometryEquiv_left_inv
    (Q : Matrix.orthogonalGroup (Fin n) ℝ) :
    linearIsometryEquivToOrthogonal (orthogonalToLinearIsometryEquiv Q) = Q
```

**`EuclideanGroup.linearIsometryEquiv_constVAdd_mul`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L155).

> The affine map `x ↦ t +ᵥ L x`, projected to its linear isometry component, is `L`.
> Together with `orthogonalToLinearIsometryEquiv_left_inv`, this proves `left_inv` of
> `toAffineIsometryMulEquiv`.

```lean
lemma linearIsometryEquiv_constVAdd_mul
    (t : EuclideanSpace ℝ (Fin n))
    (L : EuclideanSpace ℝ (Fin n) ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin n)) :
    ((AffineIsometryEquiv.constVAdd ℝ (EuclideanSpace ℝ (Fin n)) t *
        L.toAffineIsometryEquiv).linearIsometryEquiv) = L
```

**`EuclideanGroup.orthogonalToLinearIsometryEquiv_right_inv`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L169).

> `linearIsometryEquivToOrthogonal` is a right inverse of `orthogonalToLinearIsometryEquiv`;
> this proves `right_inv` of `toAffineIsometryMulEquiv`.

```lean
lemma orthogonalToLinearIsometryEquiv_right_inv
    (L : EuclideanSpace ℝ (Fin n) ≃ₗᵢ[ℝ] EuclideanSpace ℝ (Fin n)) :
    orthogonalToLinearIsometryEquiv (linearIsometryEquivToOrthogonal L) = L
```

**`EuclideanGroup.toAffineIsometryMulEquiv`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L185).

> `EuclideanGroup n ≃* AffineIsometryEquiv ℝ (EuclideanSpace ℝ (Fin n)) _`: the Euclidean group
> is the full group of affine isometries of Euclidean space. This upgrades `toAffineIsometryHom` to
> a group isomorphism with the same underlying map.

```lean
noncomputable def toAffineIsometryMulEquiv :
    EuclideanGroup n ≃*
      AffineIsometryEquiv ℝ (EuclideanSpace ℝ (Fin n)) (EuclideanSpace ℝ (Fin n))
```

**`EuclideanGroup.toAffineIsometryMulEquiv_apply`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean#L207).

> `toAffineIsometryMulEquiv` agrees with `toAffineIsometryHom`.

```lean
lemma toAffineIsometryMulEquiv_apply (A : EuclideanGroup n) :
    toAffineIsometryMulEquiv A = toAffineIsometryHom A
```

## Depends on

- [Euclidean group](euclideangroup-basic.md)

## Sources

- [Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/AffineGroup.lean)
