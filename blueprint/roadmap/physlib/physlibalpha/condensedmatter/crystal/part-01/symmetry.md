---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.CellSymmetry, CondensedMatter.Crystal.CellSymmetry.linear_mul, CondensedMatter.Crystal.CellSymmetry.perm_mul, CondensedMatter.Crystal.CellSymmetry.shift_mul, CondensedMatter.Crystal.CellSymmetry.linear_one, CondensedMatter.Crystal.CellSymmetry.perm_one, CondensedMatter.Crystal.CellSymmetry.shift_one, CondensedMatter.Crystal.CellSymmetry.linear_inv
statement: formalized
proof: formalized
---

# Symmetries of a crystal graph

The module `PhyslibAlpha.CondensedMatter.Crystal.Symmetry`, [PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean): 32 declarations (7 instances with no name), 14 with a docstring.

## i. Overview

> The symmetries of a crystal that map translated copies of the unit cell onto translated copies
> are described by finite data. A symmetry `(A, σ, b)` consists of an automorphism `A` of the
> translation group, a permutation `σ` of the site labels of the unit cell, and for each label `i`
> a cell offset `b i`. It sends the site `i` of cell `n` to the site `σ i` of cell `A n + b i`.
> Composing two symmetries composes these data, so they form a group `CellSymmetry G F`.
> Translations by `a` are the symmetries with `A = 1`, `σ = 1` and `b = a`. Conjugating a
> translation by a symmetry gives the translation by `A a`, so the translations form a normal
> subgroup. The quotient is the abstract point group, which need not be a subgroup: a screw axis or
> glide plane of a non-symmorphic crystal is a symmetry whose offsets cannot be removed.
>
> A symmetry preserves the bonds of a periodic graph exactly when the relation "site `i` in the
> reference cell is bonded to site `j` in the cell `d`" is carried to the same relation for the
> transformed data, namely `(σ i, σ j, A d + b j - b i)`. This is a finite condition on the bond
> data of one unit cell. Bond-preserving symmetries form a subgroup `PeriodicGraph.symmetries` and
> act by automorphisms of the bond graph. Conversely, every graph automorphism that normalises the
> translations arises this way.
>
> The graph alone knows nothing of physical lengths and angles. A square lattice has the symmetry
> group `ℤ² ⋊ D₄` as a graph, whether or not its two lattice constants are equal. The geometric
> point group is the subgroup of these symmetries compatible with a chosen `Geometry`.

## ii. Key results

> - `CellSymmetry` : the group of symmetries `(A, σ, b)` of the translation structure.
> - `CellSymmetry.translations` : the normal subgroup of translations.
> - `PeriodicGraph.symmetries` : the subgroup preserving the bonds of a periodic graph.
> - `PeriodicGraph.mem_symmetries_iff` : a finite criterion on the bond data of one unit cell.
> - `PeriodicGraph.exists_symmetry_of_equivariant` : every graph automorphism normalising the
>   translations is such a symmetry.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 7.

## A. The group of cell symmetries

**`CondensedMatter.Crystal.CellSymmetry`**, a structure, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L68).

> A symmetry of the translation structure of a crystal with unit-cell labels `F` and cell
> translations `G`: `(A, σ, b)` sends site `i` of cell `n` to site `σ i` of cell `A n + b i`.

```lean
@[ext] structure CellSymmetry (G F : Type*) [AddCommGroup G] where
  /-- The action on cell indices. -/
  linear : G ≃+ G
  /-- The permutation of the labels within a unit cell. -/
  perm : Equiv.Perm F
  /-- The cell offset accompanying each label. -/
  shift : F → G
```

**An instance with no name**, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L80).

```lean
instance : Mul (CellSymmetry G F)
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L84).

```lean
instance : One (CellSymmetry G F)
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L86).

```lean
instance : Inv (CellSymmetry G F)
```

**`CondensedMatter.Crystal.CellSymmetry.linear_mul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L89).

```lean
lemma linear_mul (s t : CellSymmetry G F) (x : G) :
    (s * t).linear x = s.linear (t.linear x)
```

**`CondensedMatter.Crystal.CellSymmetry.perm_mul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L91).

```lean
lemma perm_mul (s t : CellSymmetry G F) (i : F) :
    (s * t).perm i = s.perm (t.perm i)
```

**`CondensedMatter.Crystal.CellSymmetry.shift_mul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L93).

```lean
lemma shift_mul (s t : CellSymmetry G F) (i : F) :
    (s * t).shift i = s.linear (t.shift i) + s.shift (t.perm i)
```

**`CondensedMatter.Crystal.CellSymmetry.linear_one`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L95).

```lean
lemma linear_one (x : G) : (1 : CellSymmetry G F).linear x = x
```

**`CondensedMatter.Crystal.CellSymmetry.perm_one`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L96).

```lean
lemma perm_one (i : F) : (1 : CellSymmetry G F).perm i = i
```

**`CondensedMatter.Crystal.CellSymmetry.shift_one`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L97).

```lean
lemma shift_one (i : F) : (1 : CellSymmetry G F).shift i = 0
```

**`CondensedMatter.Crystal.CellSymmetry.linear_inv`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L98).

```lean
lemma linear_inv (s : CellSymmetry G F) (x : G) : (s⁻¹).linear x = s.linear.symm x
```

**`CondensedMatter.Crystal.CellSymmetry.perm_inv`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L99).

```lean
lemma perm_inv (s : CellSymmetry G F) (i : F) : (s⁻¹).perm i = s.perm.symm i
```

**`CondensedMatter.Crystal.CellSymmetry.shift_inv`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L100).

```lean
lemma shift_inv (s : CellSymmetry G F) (j : F) :
    (s⁻¹).shift j = -s.linear.symm (s.shift (s.perm.symm j))
```

**An instance with no name**, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L103).

```lean
instance : Group (CellSymmetry G F)
```

**An instance with no name**, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L109).

```lean
instance : SMul (CellSymmetry G F) (CellSite G F)
```

**`CondensedMatter.Crystal.CellSymmetry.smul_def`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L112).

```lean
lemma smul_def (s : CellSymmetry G F) (x : CellSite G F) :
    s • x = ⟨s.linear x.cell + s.shift x.label, s.perm x.label⟩
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L116).

> The site `σ i` of cell `A n + b i` to which a symmetry sends the site `i` of cell `n`.

```lean
instance : MulAction (CellSymmetry G F) (CellSite G F)
```

## B. Translations form a normal subgroup

**`CondensedMatter.Crystal.CellSymmetry.translation`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L126).

> Translation by `a`: it moves every cell by `a` and fixes the labels.

```lean
def translation (a : G) : CellSymmetry G F
```

**`CondensedMatter.Crystal.CellSymmetry.translation_smul`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L128).

```lean
lemma translation_smul (a : G) (x : CellSite G F) :
    (translation a : CellSymmetry G F) • x = a +ᵥ x
```

**`CondensedMatter.Crystal.CellSymmetry.translation_mul`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L133).

```lean
lemma translation_mul (a b : G) :
    (translation a : CellSymmetry G F) * translation b = translation (a + b)
```

**`CondensedMatter.Crystal.CellSymmetry.mul_translation_mul_inv`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L138).

> Conjugating a translation by a symmetry gives the translation by the transformed vector.

```lean
lemma mul_translation_mul_inv (s : CellSymmetry G F) (a : G) :
    s * translation a * s⁻¹ = translation (s.linear a)
```

**`CondensedMatter.Crystal.CellSymmetry.translations`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L143).

> The subgroup of translations.

```lean
def translations (G F : Type*) [AddCommGroup G] : Subgroup (CellSymmetry G F)
```

**An instance with no name**, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L156).

```lean
instance : (translations G F).Normal
```

**`CondensedMatter.Crystal.CellSymmetry.PointGroup`**, an abbrev, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L162).

> The abstract point group of a crystal: cell symmetries modulo translations.

```lean
abbrev PointGroup (G F : Type*) [AddCommGroup G]
```

## C. Bond-preserving symmetries

**`CondensedMatter.Crystal.PeriodicGraph.Bonded`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L173).

> Site `i` of the reference cell is bonded to site `j` of the cell `d`.

```lean
def Bonded (g : PeriodicGraph (Crystal.ofUnitCell G F)) (i j : F) (d : G) : Prop
```

**`CondensedMatter.Crystal.PeriodicGraph.adj_iff_bonded`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L177).

> Bonds between any two cells are the translates of bonds to the reference cell.

```lean
lemma adj_iff_bonded (g : PeriodicGraph (Crystal.ofUnitCell G F)) (n m : G) (i j : F) :
    g.toSimpleGraph.Adj ⟨n, i⟩ ⟨m, j⟩ ↔ g.Bonded i j (m - n)
```

**`CondensedMatter.Crystal.PeriodicGraph.symmetries`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L192).

> A symmetry preserves the bonds of the graph.

```lean
def symmetries (g : PeriodicGraph (Crystal.ofUnitCell G F)) : Subgroup (CellSymmetry G F)
```

**`CondensedMatter.Crystal.PeriodicGraph.mem_symmetries_iff`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L204).

> **A finite criterion for bond-preserving symmetries.** The data `(A, σ, b)` is a symmetry of
> the crystal graph exactly when site `i` is bonded to site `j` in the cell `d` if and only if site
> `σ i` is bonded to site `σ j` in the cell `A d + b j - b i`.

```lean
lemma mem_symmetries_iff (g : PeriodicGraph (Crystal.ofUnitCell G F)) (s : CellSymmetry G F) :
    s ∈ g.symmetries ↔ ∀ i j d, g.Bonded i j d ↔
      g.Bonded (s.perm i) (s.perm j) (s.linear d + s.shift j - s.shift i)
```

**`CondensedMatter.Crystal.PeriodicGraph.symmetryIso`**, a def, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L222).

> A bond-preserving symmetry is an automorphism of the bond graph.

```lean
def symmetryIso (g : PeriodicGraph (Crystal.ofUnitCell G F)) (s : g.symmetries) :
    g.toSimpleGraph ≃g g.toSimpleGraph
```

**`CondensedMatter.Crystal.PeriodicGraph.translation_mem_symmetries`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L228).

> Translations are bond-preserving symmetries.

```lean
lemma translation_mem_symmetries (g : PeriodicGraph (Crystal.ofUnitCell G F)) (a : G) :
    CellSymmetry.translation a ∈ g.symmetries
```

**`CondensedMatter.Crystal.PeriodicGraph.pointGroup`**, an abbrev, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L235).

> The point group of a periodic graph: its bond-preserving symmetries modulo translations.

```lean
abbrev pointGroup (g : PeriodicGraph (Crystal.ofUnitCell G F))
```

**`CondensedMatter.Crystal.PeriodicGraph.exists_symmetry_of_equivariant`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean#L241).

> **Every automorphism of the bond graph that normalises the translations is a cell symmetry.**
> If `φ` is a graph automorphism and `A` an automorphism of the translation group with
> `φ (a +ᵥ x) = A a +ᵥ φ x`, then `φ` acts as a bond-preserving cell symmetry with linear part `A`.

```lean
lemma exists_symmetry_of_equivariant (g : PeriodicGraph (Crystal.ofUnitCell G F))
    (φ : g.toSimpleGraph ≃g g.toSimpleGraph) (A : G ≃+ G)
    (hφ : ∀ (a : G) (x : CellSite G F), φ (a +ᵥ x) = A a +ᵥ φ x) :
    ∃ s ∈ g.symmetries, s.linear = A ∧ ∀ x, s • x = φ x
```

## Depends on

- [Crystal bonds and connectivity](graph.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Symmetry.lean)
