---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.brillouinPoint, CondensedMatter.Crystal.brillouinPoint_apply, CondensedMatter.Crystal.brillouinPoint_single, CondensedMatter.Crystal.brillouinPoint_eq_iff, CondensedMatter.Crystal.brillouinZone_ext, CondensedMatter.Crystal.brillouinPoint_surjective, CondensedMatter.Crystal.apply_eq_sum_single, CondensedMatter.Crystal.smul_brillouinPoint
statement: formalized
proof: formalized
---

# Coordinates on the Brillouin zone and the action of the symmetries

The module `PhyslibAlpha.CondensedMatter.Crystal.BrillouinCoordinates`, [PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean): 12 declarations, 10 with a docstring.

> The Brillouin zone of `ℤ^d` is the torus of coordinates modulo `1`, and a symmetry acts on the
> coordinates by an explicit integer matrix.

## i. Overview

> A crystal momentum of the lattice `ℤ^d` is a character `r ↦ exp (2πi k · r)`, determined by the
> coordinates `k ∈ ℝ^d` modulo `ℤ^d`: the Brillouin zone is the torus `ℝ^d / ℤ^d`, in coordinates
> along the reciprocal basis. A symmetry with linear part `A` sends the momentum of coordinates `k`
> to the momentum of coordinates `k'`, with `k'_j = ∑_i k_i (A⁻¹ e_j)_i`: the transpose of the
> inverse of the matrix of `A`. Momenta with coordinates in `(1/n) ℤ`, which include the high-symmetry
> points of the standard lattices, are the points of finite order. Their equality and the action of a
> symmetry on them reduce to divisibility of integers, which can be decided by computation.
>
> Together with `littleGroup` and `IrreducibleZone`, this lets one prove which momenta are equivalent
> and what the little group of a momentum is for a given lattice, by integer arithmetic.

## ii. Key results

> - `brillouinPoint` : the momentum with given coordinates.
> - `brillouinPoint_eq_iff` : two sets of coordinates give the same momentum exactly when they
>   differ by integers.
> - `brillouinPoint_surjective` : every momentum has coordinates.
> - `smul_brillouinPoint` : the action of a symmetry on coordinates.
> - `torsionPoint`, `smul_torsionPoint`, `torsionPoint_eq_iff` : momenta of finite order.
> - `mem_littleGroup_torsionPoint_iff` : the little group of a momentum of finite order.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapters 5 and 7.

## A. Momenta from coordinates

**`CondensedMatter.Crystal.brillouinPoint`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L62).

> The momentum with coordinates `k` along the reciprocal basis: the character
> `r ↦ exp (2πi k · r)` of `ℤ^d`.

```lean
noncomputable def brillouinPoint (k : Fin d → ℝ) : BrillouinZone (Fin d → ℤ)
```

**`CondensedMatter.Crystal.brillouinPoint_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L71).

```lean
lemma brillouinPoint_apply (k : Fin d → ℝ) (r : Fin d → ℤ) :
    brillouinPoint k (Multiplicative.ofAdd r) =
      Circle.exp (2 * Real.pi * ∑ j, k j * (r j : ℝ))
```

**`CondensedMatter.Crystal.brillouinPoint_single`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L75).

```lean
lemma brillouinPoint_single (k : Fin d → ℝ) (j : Fin d) :
    brillouinPoint k (Multiplicative.ofAdd (Pi.single j 1)) = Circle.exp (2 * Real.pi * k j)
```

**`CondensedMatter.Crystal.brillouinPoint_eq_iff`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L85).

> **Two sets of coordinates give the same momentum exactly when they differ by integers.**

```lean
lemma brillouinPoint_eq_iff (k k' : Fin d → ℝ) :
    brillouinPoint k = brillouinPoint k' ↔ ∀ j, ∃ z : ℤ, k j - k' j = z
```

**`CondensedMatter.Crystal.brillouinZone_ext`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L116).

> A character of `ℤ^d` is determined by its values on the basis vectors.

```lean
lemma brillouinZone_ext {χ ψ : BrillouinZone (Fin d → ℤ)}
    (h : ∀ j, χ (Multiplicative.ofAdd (Pi.single j 1)) = ψ (Multiplicative.ofAdd (Pi.single j 1))) :
    χ = ψ
```

**`CondensedMatter.Crystal.brillouinPoint_surjective`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L137).

> **Every momentum has coordinates.**

```lean
lemma brillouinPoint_surjective : Function.Surjective (brillouinPoint (d := d))
```

## B. The action of a symmetry on coordinates

**`CondensedMatter.Crystal.apply_eq_sum_single`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L149).

> A lattice automorphism is determined by its values on the basis vectors.

```lean
lemma apply_eq_sum_single (A : (Fin d → ℤ) ≃+ (Fin d → ℤ)) (r : Fin d → ℤ) (i : Fin d) :
    A r i = ∑ j, r j * A (Pi.single j 1) i
```

**`CondensedMatter.Crystal.smul_brillouinPoint`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L161).

> **A symmetry acts on the coordinates of a momentum** by the transpose of the inverse of the
> matrix of its linear part.

```lean
lemma smul_brillouinPoint {F : Type*} (s : CellSymmetry (Fin d → ℤ) F) (k : Fin d → ℝ) :
    s • brillouinPoint k =
      brillouinPoint (fun j => ∑ i, k i * (s.linear.symm (Pi.single j 1) i : ℝ))
```

## C. Momenta of finite order

**`CondensedMatter.Crystal.torsionPoint`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L170).

> The momentum with coordinates `m / n`: a point of finite order of the Brillouin zone.

```lean
noncomputable def torsionPoint (n : ℕ) (m : Fin d → ℤ) : BrillouinZone (Fin d → ℤ)
```

**`CondensedMatter.Crystal.torsionPoint_eq_iff`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L174).

> **Momenta of finite order are equal exactly when the numerators agree modulo `n`.**

```lean
lemma torsionPoint_eq_iff {n : ℕ} (hn : 0 < n) (m m' : Fin d → ℤ) :
    torsionPoint n m = torsionPoint n m' ↔ ∀ j, (n : ℤ) ∣ m j - m' j
```

**`CondensedMatter.Crystal.smul_torsionPoint`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L195).

> A symmetry acts on a momentum of finite order by an integer matrix on the numerators.

```lean
lemma smul_torsionPoint {F : Type*} (n : ℕ) (s : CellSymmetry (Fin d → ℤ) F) (m : Fin d → ℤ) :
    s • torsionPoint n m =
      torsionPoint n (fun j => ∑ i, m i * s.linear.symm (Pi.single j 1) i)
```

**`CondensedMatter.Crystal.mem_littleGroup_torsionPoint_iff`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean#L209).

> **The little group of a momentum of finite order**, as integer arithmetic: a bond-preserving
> symmetry fixes the momentum with numerators `m` modulo `n` exactly when the integer vector
> obtained from the matrix of its linear part is congruent to `m` modulo `n`.

```lean
lemma mem_littleGroup_torsionPoint_iff {F : Type*} [Finite F]
    (g : PeriodicGraph (Crystal.ofUnitCell (Fin d → ℤ) F)) {n : ℕ} (hn : 0 < n)
    (m : Fin d → ℤ) (s : g.symmetries) :
    s ∈ g.littleGroup (torsionPoint n m) ↔
      ∀ j, (n : ℤ) ∣ (∑ i, m i * (s : CellSymmetry (Fin d → ℤ) F).linear.symm (Pi.single j 1) i) -
        m j
```

## Depends on

- [Symmetries of a crystal acting on its Brillouin zone](brillouin.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/BrillouinCoordinates.lean)
