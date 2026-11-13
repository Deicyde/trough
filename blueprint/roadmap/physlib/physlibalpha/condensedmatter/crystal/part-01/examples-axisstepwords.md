---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.axisStep, CondensedMatter.Crystal.twoStepWords, CondensedMatter.Crystal.threeStepWords, CondensedMatter.Crystal.twoStepSum, CondensedMatter.Crystal.threeStepSum, CondensedMatter.Crystal.twoStepSum_swap, CondensedMatter.Crystal.fccCoord, CondensedMatter.Crystal.bccCoord
statement: formalized
proof: formalized
---

# The nearest neighbours of fcc and bcc are words of axis steps

The module `PhyslibAlpha.CondensedMatter.Crystal.Examples.AxisStepWords`, [PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean): 15 declarations, 15 with a docstring.

## i. Overview

> The bonds `fccBonds` and `bccBonds` are written in the basis of primitive vectors. In the
> coordinates of the box, in units of half its sides, a site of the fcc lattice is a point of `ℤ³`
> and a nearest neighbour is the sum of two steps of length one along different axes: a face
> diagonal. A nearest neighbour of the bcc lattice is the sum of three steps along the three axes:
> a body diagonal. Here the converse: every such sum is a nearest neighbour.
>
> A step along an axis is forward or backward, so there are two steps per axis. Steps along
> different axes commute, so the two orders of a pair of steps reach the same site. Each face
> diagonal is reached by `2` words of two steps and each body diagonal by `6` words of three steps.

## ii. Key results

> - `fccBonds_eq_twoStepWords` : the nearest neighbours of fcc, up to sign, are the sums of two
>   steps along different axes.
> - `bccBonds_eq_threeStepWords` : the nearest neighbours of bcc, up to sign, are the sums of three
>   steps along the three axes.
> - `card_twoStepWords_fiber`, `card_threeStepWords_fiber` : each neighbour is reached by exactly
>   `2`, respectively `6`, words.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 4.

## A. Axis steps and their words

**`CondensedMatter.Crystal.axisStep`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L54).

> The step of length one along the axis `i`, forward or backward.

```lean
def axisStep (i : Fin 3) (s : Bool) : Fin 3 → ℤ
```

**`CondensedMatter.Crystal.twoStepWords`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L57).

> The words of two steps along different axes.

```lean
def twoStepWords : Finset ((Fin 3 × Bool) × (Fin 3 × Bool))
```

**`CondensedMatter.Crystal.threeStepWords`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L61).

> The words of three steps along the three different axes.

```lean
def threeStepWords : Finset ((Fin 3 × Bool) × (Fin 3 × Bool) × (Fin 3 × Bool))
```

**`CondensedMatter.Crystal.twoStepSum`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L65).

> The displacement of a word of two steps.

```lean
def twoStepSum (w : (Fin 3 × Bool) × (Fin 3 × Bool)) : Fin 3 → ℤ
```

**`CondensedMatter.Crystal.threeStepSum`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L69).

> The displacement of a word of three steps.

```lean
def threeStepSum (w : (Fin 3 × Bool) × (Fin 3 × Bool) × (Fin 3 × Bool)) : Fin 3 → ℤ
```

**`CondensedMatter.Crystal.twoStepSum_swap`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L74).

> Steps along different axes commute: both orders of a word of two steps reach the same
> site.

```lean
lemma twoStepSum_swap (w : (Fin 3 × Bool) × (Fin 3 × Bool)) :
    twoStepSum (w.2, w.1) = twoStepSum w
```

## B. Coordinates of the box

**`CondensedMatter.Crystal.fccCoord`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L80).

> The coordinates in the box, in units of half its sides, of the cell `n` of the fcc lattice.

```lean
def fccCoord (n : Fin 3 → ℤ) : Fin 3 → ℤ
```

**`CondensedMatter.Crystal.bccCoord`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L83).

> The coordinates in the box, in units of half its sides, of the cell `n` of the bcc lattice.

```lean
def bccCoord (n : Fin 3 → ℤ) : Fin 3 → ℤ
```

**`CondensedMatter.Crystal.signedDisplacements`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L87).

> The displacements of the bonds of a list, with both signs.

```lean
def signedDisplacements (bonds : List (Bond (Fin 3 → ℤ) Unit)) : Finset (Fin 3 → ℤ)
```

**`CondensedMatter.Crystal.latticeMap_fccVectors`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L92).

> The physical position of a cell of the fcc lattice is `fccCoord` in units of half the sides
> of the box.

```lean
lemma latticeMap_fccVectors (a b c : ℝ) (n : Fin 3 → ℤ) (k : Fin 3) :
    latticeMap (fccVectors a b c) n k = ![a, b, c] k / 2 * (fccCoord n k : ℝ)
```

**`CondensedMatter.Crystal.latticeMap_bccVectors`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L100).

> The physical position of a cell of the bcc lattice is `bccCoord` in units of half the sides
> of the box.

```lean
lemma latticeMap_bccVectors (a b c : ℝ) (n : Fin 3 → ℤ) (k : Fin 3) :
    latticeMap (bccVectors a b c) n k = ![a, b, c] k / 2 * (bccCoord n k : ℝ)
```

## C. The neighbours as words

**`CondensedMatter.Crystal.fccBonds_eq_twoStepWords`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L110).

> The nearest neighbours of the fcc lattice, up to sign, are the sums of two steps along
> different axes.

```lean
lemma fccBonds_eq_twoStepWords :
    (signedDisplacements fccBonds).image fccCoord = twoStepWords.image twoStepSum
```

**`CondensedMatter.Crystal.bccBonds_eq_threeStepWords`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L116).

> The nearest neighbours of the bcc lattice, up to sign, are the sums of three steps along the
> three axes.

```lean
lemma bccBonds_eq_threeStepWords :
    (signedDisplacements bccBonds).image bccCoord = threeStepWords.image threeStepSum
```

**`CondensedMatter.Crystal.card_twoStepWords_fiber`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L121).

> Each nearest neighbour of the fcc lattice is reached by exactly two words of two steps.

```lean
lemma card_twoStepWords_fiber :
    ∀ v ∈ twoStepWords.image twoStepSum, (twoStepWords.filter (twoStepSum · = v)).card = 2
```

**`CondensedMatter.Crystal.card_threeStepWords_fiber`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean#L126).

> Each nearest neighbour of the bcc lattice is reached by exactly six words of three steps.

```lean
lemma card_threeStepWords_fiber :
    ∀ v ∈ threeStepWords.image threeStepSum,
      (threeStepWords.filter (threeStepSum · = v)).card = 6
```

## Depends on

- [Orthorhombic, cubic and hexagonal close-packed crystals](examples-threedimensional.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Examples/AxisStepWords.lean)
