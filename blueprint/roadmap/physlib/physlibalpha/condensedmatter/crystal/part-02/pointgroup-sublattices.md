---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.PeriodicGraph.bondDisplacements, CondensedMatter.Crystal.PeriodicGraph.bonded_ofBonds_iff, CondensedMatter.Crystal.PeriodicGraph.mem_symmetries_ofBonds_iff, CondensedMatter.Crystal.PeriodicGraph.bondDifferences, CondensedMatter.Crystal.PeriodicGraph.mem_bondDifferences, CondensedMatter.Crystal.PeriodicGraph.linear_mem_bondDifferences, CondensedMatter.Crystal.PeriodicGraph.linear_mem_bondDifferences_iff, CondensedMatter.Crystal.PeriodicGraph.linearToLattice
statement: formalized
proof: formalized
---

# The point group of a crystal with several sites per cell

The module `PhyslibAlpha.CondensedMatter.Crystal.PointGroup.Sublattices`, [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean): 13 declarations, 9 with a docstring.

> The point group of a crystal with several sites per cell is compared with the point group of a
> Bravais lattice, the lattice of differences of its bonds.

## i. Overview

> For a graph given by a list of bonds, the displacements `d` for which site `i` of the reference
> cell is bonded to site `j` of the cell `d` form a finite set `E i j`. A cell symmetry `(A, σ, b)`
> preserves the bonds exactly when it maps each `E i j` onto `E (σ i) (σ j)` by
> `d ↦ A d + b j - b i`, a finite condition.
>
> If site `i` is bonded to site `j` in the cells `d₁` and `d₂`, the difference `d₁ - d₂` is a
> translation between two sites with the same label. A symmetry maps both bonds to bonds with
> common labels, so its linear part maps these differences to differences. When the differences are
> the neighbours of a Bravais lattice, for instance the face-centred cubic lattice for diamond or the
> triangular lattice for the honeycomb, the linear parts of the symmetries lie in the point group
> of that lattice. If moreover only translations have the identity as linear part, and every point
> operation of the lattice lifts to a symmetry, the two point groups are isomorphic. Both conditions
> reduce to finite checks.

## ii. Key results

> - `PeriodicGraph.bondDisplacements` : the finite sets `E i j` of a bond list.
> - `PeriodicGraph.mem_symmetries_ofBonds_iff` : the finite criterion for symmetries.
> - `PeriodicGraph.bondDifferences` : the differences `d₁ - d₂` of displacements in a common `E i j`.
> - `PeriodicGraph.linear_mem_bondDifferences_iff` : linear parts of symmetries preserve them.
> - `PeriodicGraph.pointGroupMulEquivOfLift` : the point group is that of the lattice of
>   differences, when the linear part is injective modulo translations and every point operation
>   lifts.
> - `PeriodicGraph.mem_translations_of_linear_eq` and `PeriodicGraph.lift_of_admissible` : the
>   finite checks of these two conditions.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. Bonded displacements of a bond list

**`CondensedMatter.Crystal.PeriodicGraph.bondDisplacements`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L70).

> The displacements `d` such that site `i` of the reference cell is bonded to site `j` of the
> cell `d`, in the graph of a bond list.

```lean
def bondDisplacements (bonds : List (Bond G F)) (i j : F) : Finset G
```

**`CondensedMatter.Crystal.PeriodicGraph.bonded_ofBonds_iff`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L75).

```lean
lemma bonded_ofBonds_iff (bonds : List (Bond G F)) (i j : F) (d : G) :
    (ofBonds bonds).Bonded i j d ↔ d ∈ bondDisplacements bonds i j
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_symmetries_ofBonds_iff`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L93).

> **A finite criterion for the symmetries of the graph of a bond list**: `(A, σ, b)` is a
> symmetry exactly when `d ↦ A d + b j - b i` maps `E i j` onto `E (σ i) (σ j)` for all labels.

```lean
lemma mem_symmetries_ofBonds_iff (bonds : List (Bond G F)) (s : CellSymmetry G F) :
    s ∈ (ofBonds bonds).symmetries ↔ ∀ i j, (bondDisplacements bonds i j).image
      (fun d => s.linear d + s.shift j - s.shift i) =
        bondDisplacements bonds (s.perm i) (s.perm j)
```

## B. Differences of bonds

**`CondensedMatter.Crystal.PeriodicGraph.bondDifferences`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L116).

> The nonzero differences `d₁ - d₂` of two displacements in a common `E i j`: translations
> between two sites with the same label that are bonded to a common site.

```lean
def bondDifferences (bonds : List (Bond G F)) : Finset G
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_bondDifferences`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L121).

```lean
lemma mem_bondDifferences (bonds : List (Bond G F)) (e : G) :
    e ∈ bondDifferences bonds ↔ e ≠ 0 ∧ ∃ i j, ∃ d₁ ∈ bondDisplacements bonds i j,
      ∃ d₂ ∈ bondDisplacements bonds i j, e = d₁ - d₂
```

**`CondensedMatter.Crystal.PeriodicGraph.linear_mem_bondDifferences`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L132).

```lean
lemma linear_mem_bondDifferences {bonds : List (Bond G F)} {s : CellSymmetry G F}
    (hs : s ∈ (ofBonds bonds).symmetries) {e : G} (he : e ∈ bondDifferences bonds) :
    s.linear e ∈ bondDifferences bonds
```

**`CondensedMatter.Crystal.PeriodicGraph.linear_mem_bondDifferences_iff`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L148).

> **The linear part of a symmetry preserves the differences of bonds.**

```lean
lemma linear_mem_bondDifferences_iff {bonds : List (Bond G F)} {s : CellSymmetry G F}
    (hs : s ∈ (ofBonds bonds).symmetries) (e : G) :
    s.linear e ∈ bondDifferences bonds ↔ e ∈ bondDifferences bonds
```

## C. Comparison of point groups

**`CondensedMatter.Crystal.PeriodicGraph.linearToLattice`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L163).

> The linear part of a symmetry, as an element of the point stabilizer of the lattice of
> differences.

```lean
def linearToLattice (hΔ : bondDifferences bonds = bondNeighbors bonds') :
    (ofBonds bonds).symmetries →* (ofBonds bonds').pointStabilizer
```

**`CondensedMatter.Crystal.PeriodicGraph.ker_linearToLattice`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L169).

```lean
lemma ker_linearToLattice (hΔ : bondDifferences bonds = bondNeighbors bonds')
    (hker : ∀ s ∈ (ofBonds bonds).symmetries, s.linear = AddEquiv.refl _ →
      s ∈ CellSymmetry.translations (Fin n → ℤ) F) :
    (linearToLattice hΔ).ker =
      (CellSymmetry.translations (Fin n → ℤ) F).subgroupOf (ofBonds bonds).symmetries
```

**`CondensedMatter.Crystal.PeriodicGraph.pointGroupMulEquivOfLift`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L189).

> **The point group of a crystal with several sites per cell is the point group of its lattice
> of differences**, if only translations have the identity as linear part and every point
> operation of the lattice lifts to a symmetry.

```lean
noncomputable def pointGroupMulEquivOfLift (hΔ : bondDifferences bonds = bondNeighbors bonds')
    (hker : ∀ s ∈ (ofBonds bonds).symmetries, s.linear = AddEquiv.refl _ →
      s ∈ CellSymmetry.translations (Fin n → ℤ) F)
    (hlift : Function.Surjective (linearToLattice hΔ)) :
    (ofBonds bonds).pointGroup ≃* (ofBonds bonds').pointGroup
```

## D. Finite checks

**`CondensedMatter.Crystal.PeriodicGraph.shiftCandidates`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L200).

> The candidates for the cell offsets of a symmetry, relative to the label `i₀`.

```lean
def shiftCandidates (bonds : List (Bond (Fin n → ℤ) F)) (i₀ : F) : Finset (Fin n → ℤ)
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_translations_of_linear_eq`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L207).

> **Only translations have the identity as linear part**, if every label is bonded to `i₀` and
> this holds for the finitely many candidate offsets.

```lean
lemma mem_translations_of_linear_eq (i₀ : F)
    (hconn : ∀ i, i = i₀ ∨ (bondDisplacements bonds i₀ i).Nonempty)
    (h : ∀ σ : Equiv.Perm F, ∀ r ∈ Fintype.piFinset fun _ => shiftCandidates bonds i₀,
      r i₀ = 0 → (∀ i j, (bondDisplacements bonds i j).image (fun d => d + r j - r i) =
        bondDisplacements bonds (σ i) (σ j)) → σ = 1 ∧ r = 0)
    (s : CellSymmetry (Fin n → ℤ) F) (hs : s ∈ (ofBonds bonds).symmetries)
    (hL : s.linear = AddEquiv.refl _) : s ∈ CellSymmetry.translations (Fin n → ℤ) F
```

**`CondensedMatter.Crystal.PeriodicGraph.lift_of_admissible`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean#L242).

> **Every point operation of the lattice of differences lifts to a symmetry**, if every
> admissible tuple of neighbours does, with a permutation and offsets `b i ∈ T i`.

```lean
lemma lift_of_admissible (hΔ : bondDifferences bonds = bondNeighbors bonds')
    (hN : ∀ j, (Pi.single j 1 : Fin n → ℤ) ∈ bondNeighbors bonds') (T : F → Finset (Fin n → ℤ))
    (h : ∀ w : Fin n → bondNeighbors bonds', Admissible (bondNeighbors bonds') (fun j => w j) →
      ∃ σ : Equiv.Perm F, ∃ b ∈ Fintype.piFinset T, ∀ i j, (bondDisplacements bonds i j).image
        (fun d => act (fun j => w j) d + b j - b i) = bondDisplacements bonds (σ i) (σ j)) :
    Function.Surjective (linearToLattice hΔ)
```

## Depends on

- [The point groups of the face-centred and body-centred cubic lattices](pointgroup-cubic.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/PointGroup/Sublattices.lean)
