---
declaration: module
origin: cited
lean: CondensedMatter.Bloch.hypercubicCone, CondensedMatter.Bloch.hypercubicZone, CondensedMatter.Bloch.signedPerm_mem_symmetries, CondensedMatter.Bloch.smul_brillouinPoint_of_linear, CondensedMatter.Bloch.smul_brillouinPoint_signedPerm, CondensedMatter.Bloch.exists_signedPerm_to_cone, CondensedMatter.Bloch.coversOrbits_hypercubic, CondensedMatter.Bloch.hypercubicBand
statement: formalized
proof: formalized
---

# Nearest-neighbour hopping on the hypercubic lattice

The module `PhyslibAlpha.CondensedMatter.Bloch.Hypercubic`, [PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean): 17 declarations, 14 with a docstring; 3 private, not shown.

> The band of nearest-neighbour hopping on the hypercubic lattice, and the irreducible zone modulo
> the hyperoctahedral group.

## i. Overview

> Nearest-neighbour hopping with amplitude `t` on `ℤ^d` has the Bloch matrix, a `1 × 1` matrix,
> `2 t ∑_j cos (2π k_j)` at the momentum with coordinates `k`. Every signed permutation of the
> axes is a symmetry of the lattice, and acts on the coordinates by permuting them and changing
> their signs, so the band is invariant. Every momentum is carried by a signed permutation into the
> set `0 ≤ k_{d-1} ≤ … ≤ k_1 ≤ k_0 ≤ 1/2`, a simplex which is a fraction `1 / (2^d d!)` of the
> Brillouin zone. This is the irreducible zone: the Brillouin zone modulo the point group. The
> spectrum of the hopping is therefore the set of values of the band on this simplex.

## ii. Key results

> - `hypercubicZone` : the simplex `0 ≤ k_{d-1} ≤ … ≤ k_0 ≤ 1/2`.
> - `coversOrbits_hypercubic` : every momentum is equivalent to a momentum in the simplex.
> - `exists_signedPerm_to_cone` : an explicit signed permutation carrying a momentum into the
>   simplex.
> - `hypercubicBand`, `hoppingSymbol_hypercubic` : the Bloch matrix of nearest-neighbour hopping.
> - `iUnion_spectrum_hypercubic` : the spectrum is the set of values of the band on the simplex.
> - `littleGroup_gamma`, `littleGroup_corner` : the centre and the corner of the zone are fixed by
>   every symmetry.
> - `iUnion_spectrum_hypercubic_eq_Icc` : the spectrum is the interval `[-2 d |t|, 2 d |t|]`.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 8.

## A. The irreducible zone

**`CondensedMatter.Bloch.hypercubicCone`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L64).

> The cone `0 ≤ k_{d-1} ≤ … ≤ k_0 ≤ 1/2` of coordinates.

```lean
def hypercubicCone (d : ℕ) : Set (Fin d → ℝ)
```

**`CondensedMatter.Bloch.hypercubicZone`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L68).

> The irreducible zone of the hypercubic lattice: the momenta with coordinates in the cone.

```lean
def hypercubicZone (d : ℕ) : Set (BrillouinZone (Fin d → ℤ))
```

**`CondensedMatter.Bloch.signedPerm_mem_symmetries`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L72).

> **A signed permutation is a bond-preserving symmetry of the hypercubic lattice.**

```lean
lemma signedPerm_mem_symmetries (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) :
    (⟨signedPerm π ε, 1, 0⟩ : CellSymmetry (Fin d → ℤ) Unit) ∈
      (hypercubicGraph d).symmetries
```

**`CondensedMatter.Bloch.smul_brillouinPoint_of_linear`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L82).

> The coordinates of the image of a momentum under a symmetry whose linear part is a signed
> permutation.

```lean
lemma smul_brillouinPoint_of_linear {F : Type*} (s : CellSymmetry (Fin d → ℤ) F)
    (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) (h : s.linear = signedPerm π ε)
    (k : Fin d → ℝ) :
    s • brillouinPoint k = brillouinPoint (fun j => (signOf (ε j) : ℝ) * k (π.symm j))
```

**`CondensedMatter.Bloch.smul_brillouinPoint_signedPerm`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L105).

> The coordinates of the image of a momentum under a signed permutation.

```lean
lemma smul_brillouinPoint_signedPerm (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) (k : Fin d → ℝ) :
    (⟨signedPerm π ε, 1, 0⟩ : CellSymmetry (Fin d → ℤ) Unit) • brillouinPoint k =
      brillouinPoint (fun j => (signOf (ε j) : ℝ) * k (π.symm j))
```

**`CondensedMatter.Bloch.exists_signedPerm_to_cone`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L111).

> **Every momentum is carried into the irreducible zone by a signed permutation.**

```lean
lemma exists_signedPerm_to_cone (k : Fin d → ℝ) :
    ∃ (π : Equiv.Perm (Fin d)) (ε : Fin d → Bool) (k' : Fin d → ℝ), k' ∈ hypercubicCone d ∧
      (⟨signedPerm π ε, 1, 0⟩ : CellSymmetry (Fin d → ℤ) Unit) • brillouinPoint k =
        brillouinPoint k'
```

**`CondensedMatter.Bloch.coversOrbits_hypercubic`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L146).

> **The hypercubic zone covers the orbits of the point group.**

```lean
lemma coversOrbits_hypercubic :
    CoversOrbits (hypercubicGraph d) (hypercubicZone d)
```

## B. The nearest-neighbour band

**`CondensedMatter.Bloch.hypercubicBand`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L158).

> The band of nearest-neighbour hopping with amplitude `t` on the hypercubic lattice, at the
> momentum with coordinates `k`: `2 t ∑_j cos (2π k_j)`.

```lean
noncomputable def hypercubicBand (t : ℝ) (k : Fin d → ℝ) : ℝ
```

**`CondensedMatter.Bloch.hoppingSymbol_hypercubic`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L181).

> **The Bloch matrix of nearest-neighbour hopping on the hypercubic lattice** is the `1 × 1`
> matrix with the entry `2 t ∑_j cos (2π k_j)`.

```lean
lemma hoppingSymbol_hypercubic (t : ℝ) (k : Fin d → ℝ) :
    hoppingSymbol (uniformHopping (hypercubicGraph d) (t : ℂ)) (brillouinPoint k) =
      Matrix.of fun _ _ => ((hypercubicBand t k : ℝ) : ℂ)
```

**`CondensedMatter.Bloch.iUnion_spectrum_hypercubic`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L249).

> **The spectrum of nearest-neighbour hopping on the hypercubic lattice** is the set of values
> of the band `2 t ∑_j cos (2π k_j)` on the irreducible zone `0 ≤ k_{d-1} ≤ … ≤ k_0 ≤ 1/2`, which is
> `1 / (2^d d!)` of the Brillouin zone.

```lean
lemma iUnion_spectrum_hypercubic (t : ℝ) :
    (⋃ χ : BrillouinZone (Fin d → ℤ),
        spectrum ℂ (hoppingSymbol (uniformHopping (hypercubicGraph d) (t : ℂ)) χ)) =
      {z : ℂ | ∃ k ∈ hypercubicCone d, z = ((hypercubicBand t k : ℝ) : ℂ)}
```

## C. The spectrum is an interval

**`CondensedMatter.Bloch.convex_hypercubicCone`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L268).

```lean
lemma convex_hypercubicCone : Convex ℝ (hypercubicCone d)
```

**`CondensedMatter.Bloch.continuous_hypercubicBand`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L278).

```lean
lemma continuous_hypercubicBand (t : ℝ) : Continuous (hypercubicBand (d := d) t)
```

**`CondensedMatter.Bloch.abs_hypercubicBand_le`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L282).

```lean
lemma abs_hypercubicBand_le (t : ℝ) (k : Fin d → ℝ) :
    |hypercubicBand t k| ≤ 2 * d * |t|
```

**`CondensedMatter.Bloch.hypercubicBand_image`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L296).

> **The band of nearest-neighbour hopping takes exactly the values in `[-2 d |t|, 2 d |t|]` on
> the irreducible zone.**

```lean
lemma hypercubicBand_image (t : ℝ) :
    hypercubicBand t '' hypercubicCone d = Set.Icc (-(2 * d * |t|)) (2 * d * |t|)
```

**`CondensedMatter.Bloch.iUnion_spectrum_hypercubic_eq_Icc`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L328).

> **The spectrum of nearest-neighbour hopping on the hypercubic lattice is the interval
> `[-2 d |t|, 2 d |t|]`.**

```lean
lemma iUnion_spectrum_hypercubic_eq_Icc (t : ℝ) :
    (⋃ χ : BrillouinZone (Fin d → ℤ),
        spectrum ℂ (hoppingSymbol (uniformHopping (hypercubicGraph d) (t : ℂ)) χ)) =
      ((↑) : ℝ → ℂ) '' Set.Icc (-(2 * d * |t|)) (2 * d * |t|)
```

## D. The fully symmetric momenta

**`CondensedMatter.Bloch.littleGroup_gamma`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L342).

> **The centre `Γ` of the Brillouin zone is fixed by every symmetry.**

```lean
lemma littleGroup_gamma (d : ℕ) :
    (hypercubicGraph d).littleGroup (brillouinPoint (0 : Fin d → ℝ)) = ⊤
```

**`CondensedMatter.Bloch.littleGroup_corner`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean#L354).

> **The corner `R = (1/2, …, 1/2)` of the Brillouin zone is fixed by every symmetry**: its
> little group is the whole group.

```lean
lemma littleGroup_corner (d : ℕ) :
    (hypercubicGraph d).littleGroup (brillouinPoint (fun _ : Fin d => (1 / 2 : ℝ))) = ⊤
```

## Depends on

- [Symmetry of the Bloch matrices of a crystal](pointsymmetry.md)
- [Coordinates on the Brillouin zone and the action of the symmetries](../crystal/part-01/brillouincoordinates.md)
- [The point group of the hypercubic lattice in every dimension](../crystal/part-02/pointgroup-hypercubic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Hypercubic.lean)
