---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.box, CondensedMatter.Crystal.card_box, CondensedMatter.Crystal.image_add_box, CondensedMatter.Crystal.card_image_add_box, CondensedMatter.Crystal.card_inter_box, CondensedMatter.Crystal.card_Ico_inter, CondensedMatter.Crystal.card_sdiff_add_card_sdiff, CondensedMatter.Crystal.tendsto_box_sdiff
statement: formalized
proof: formalized
---

# Boxes of a lattice are asymptotically translation invariant

The module `PhyslibAlpha.CondensedMatter.Crystal.Folner`, [PhyslibAlpha/CondensedMatter/Crystal/Folner.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean): 11 declarations, 6 with a docstring.

> The cubes `{0, …, n-1}^d` of the lattice `ℤ^d` satisfy the Følner condition for the translations.

## i. Overview

> A translation by `h` moves the cube `B_n = {0, …, n-1}^d` to a cube that overlaps `B_n` in
> `∏_j (n - |h_j|)` points, so the fraction of points not shared is `1 - ∏_j (1 - |h_j|/n)`, which
> tends to zero. This is the Følner condition (`ProbabilisticTheory.IsRightFolner`) that makes the
> averages of a state over the translations by the elements of `B_n` invariant in the limit.

## ii. Key results

> - `box` : the cube `{0, …, m-1}^d` of `ℤ^d`.
> - `card_box` : it has `m ^ d` points.
> - `isRightFolner_boxes` : the cubes are asymptotically invariant under translations along any
>   ultrafilter finer than the filter of large cubes.

## iv. References

> * F. Greenleaf, Invariant Means on Topological Groups.

## A. Cubes and their translates

**`CondensedMatter.Crystal.box`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L54).

> The cube `{0, …, m-1}^d` of the lattice `ℤ^d`.

```lean
def box (d m : ℕ) : Finset (Fin d → ℤ)
```

**`CondensedMatter.Crystal.card_box`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L56).

```lean
lemma card_box (d m : ℕ) : (box d m).card = m ^ d
```

**`CondensedMatter.Crystal.image_add_box`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L59).

```lean
lemma image_add_box (d m : ℕ) (h : Fin d → ℤ) :
    (box d m).image (· + h) = Fintype.piFinset fun j => Finset.Ico (h j) (m + h j)
```

**`CondensedMatter.Crystal.card_image_add_box`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L74).

```lean
lemma card_image_add_box (d m : ℕ) (h : Fin d → ℤ) : ((box d m).image (· + h)).card = m ^ d
```

**`CondensedMatter.Crystal.card_inter_box`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L78).

> The overlap of the cube with its translate.

```lean
lemma card_inter_box (d m : ℕ) (h : Fin d → ℤ) :
    ((box d m).image (· + h) ∩ box d m).card =
      ∏ j, (Finset.Ico (h j) (m + h j) ∩ Finset.Ico (0 : ℤ) m).card
```

## B. The Følner property

**`CondensedMatter.Crystal.card_Ico_inter`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L85).

```lean
lemma card_Ico_inter (m : ℕ) (a : ℤ) (ha : |a| ≤ m) :
    (Finset.Ico a (m + a) ∩ Finset.Ico (0 : ℤ) m).card = m - a.natAbs
```

**`CondensedMatter.Crystal.card_sdiff_add_card_sdiff`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L92).

> The number of points of the cube not shared with its translate.

```lean
lemma card_sdiff_add_card_sdiff (d m : ℕ) (h : Fin d → ℤ) :
    (((box d m).image (· + h) \ box d m).card + (box d m \ (box d m).image (· + h)).card : ℝ) =
      2 * ((m : ℝ) ^ d - ∏ j, ((Finset.Ico (h j) (m + h j) ∩ Finset.Ico (0 : ℤ) m).card : ℝ))
```

**`CondensedMatter.Crystal.tendsto_box_sdiff`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L108).

> **The cubes are asymptotically invariant under translation**: the fraction of the points of
> `{0, …, n}^d` that are not shared with a fixed translate tends to zero.

```lean
lemma tendsto_box_sdiff (d : ℕ) (h : Fin d → ℤ) :
    Tendsto (fun n : ℕ => (((box d (n + 1)).image (· + h) \ box d (n + 1)).card +
      (box d (n + 1) \ (box d (n + 1)).image (· + h)).card : ℝ) / ((n + 1 : ℕ) : ℝ) ^ d)
      atTop (𝓝 0)
```

**`CondensedMatter.Crystal.boxes`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L143).

> The cubes `{0, …, n}^d`, as finite sets of the translation group.

```lean
def boxes (d n : ℕ) : Finset (Multiplicative (Fin d → ℤ))
```

**`CondensedMatter.Crystal.image_mul_boxes`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L146).

```lean
lemma image_mul_boxes (d n : ℕ) (h : Multiplicative (Fin d → ℤ)) :
    (boxes d n).image (· * h) =
      ((box d (n + 1)).image (· + Multiplicative.toAdd h)).map
        Multiplicative.ofAdd.toEmbedding
```

**`CondensedMatter.Crystal.isRightFolner_boxes`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean#L160).

> **The cubes are a Følner family** for the translations of `ℤ^d`, along any ultrafilter on
> `ℕ` finer than the filter of large cubes.

```lean
lemma isRightFolner_boxes (d : ℕ) (𝒰 : Ultrafilter ℕ) (h𝒰 : (𝒰 : Filter ℕ) ≤ atTop) :
    IsRightFolner (boxes d) 𝒰
```

## Depends on

- [Invariant states by Følner averaging](../../../probabilistictheory/staralgebra/invariant.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Folner.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Folner.lean)
