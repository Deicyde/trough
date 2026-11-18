---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.Geometry, CondensedMatter.Crystal.Geometry.distance, CondensedMatter.Crystal.Geometry.distance_vadd, CondensedMatter.Crystal.Geometry.distance_eq_zero, CondensedMatter.Crystal.Geometry.metricSpace, CondensedMatter.Crystal.Geometry.isometry_position, CondensedMatter.Crystal.Geometry.ofUnitCell, CondensedMatter.Crystal.Geometry.ofDisplacements
statement: formalized
proof: formalized
---

# Crystal geometry

The module `PhyslibAlpha.CondensedMatter.Crystal.Geometry`, [PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean): 15 declarations, 15 with a docstring.

## i. Overview

> The geometry of a crystal assigns a physical position to each site. Positions lie in a
> metric space `A`, on which the translation group `G` acts by isometries. Translating a
> site translates its position by the same group element. Distinct sites occupy distinct
> positions.
>
> The physical space may be Euclidean for an infinite crystal,
> or a torus for a finite periodic crystal. Its translation action specifies the
> physical displacement associated with each cell translation. The periodic and ambient
> dimensions need not coincide: a sheet can be embedded in three-dimensional space.
>
> `Geometry C A` supplies the embedding `position` of a crystal `C` into `A`. The physical
> distance between sites is the distance between their positions. It is invariant under a
> common translation and vanishes exactly when the sites coincide. The same distances
> define a metric on the site set through `Geometry.metricSpace`.

## ii. Key results

> - `Geometry` : an embedding of a crystal into a metric space compatible with translations.
> - `Geometry.ofDisplacements` : positions from lattice displacements and unit-cell offsets.
> - `latticeMap` : the linear map from cell indices to physical translations.
> - `Geometry.distance_eq_of_adj` : bond lengths depend only on the bond.

## iv. References

> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapter 4.

## A. Positions and translations

**`CondensedMatter.Crystal.Geometry`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L60).

> An embedding of a crystal into physical space, compatible with translations.

```lean
structure Geometry {G : Type*} [AddGroup G] (C : Crystal G) (A : Type*)
    [MetricSpace A] where
  /-- Physical translations of the ambient space. -/
  [translations : AddAction G A]
  /-- Physical translations preserve ambient distances. -/
  [isometricTranslations : IsIsometricVAdd G A]
  /-- Physical positions, with distinct sites mapped to distinct points. -/
  position : C.Site ↪ A
  /-- A translated site occupies the corresponding translated position. -/
  position_vadd : ∀ (a : G) (x : C.Site), position (a +ᵥ x) = a +ᵥ position x
```

## B. Physical distances

**`CondensedMatter.Crystal.Geometry.distance`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L79).

> Physical distance between two sites.

```lean
noncomputable def distance (R : Geometry C A) (x y : C.Site) : ℝ
```

**`CondensedMatter.Crystal.Geometry.distance_vadd`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L83).

> A common cell translation preserves the distance between sites.

```lean
lemma distance_vadd (R : Geometry C A) (a : G) (x y : C.Site) :
    R.distance (a +ᵥ x) (a +ᵥ y) = R.distance x y
```

**`CondensedMatter.Crystal.Geometry.distance_eq_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L91).

> Zero physical distance identifies the same site.

```lean
lemma distance_eq_zero (R : Geometry C A) (x y : C.Site) :
    R.distance x y = 0 ↔ x = y
```

**`CondensedMatter.Crystal.Geometry.metricSpace`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L97).

> The metric on crystal sites inherited from their physical positions.

```lean
noncomputable def metricSpace (R : Geometry C A) : MetricSpace C.Site
```

**`CondensedMatter.Crystal.Geometry.isometry_position`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L101).

> The position embedding preserves the induced physical metric.

```lean
lemma isometry_position (R : Geometry C A) :
    letI := R.metricSpace
    Isometry R.position
```

## C. Positions from a unit cell

> Specify the positions of the sites in the reference cell. The position of site `i` in
> cell `n` is the translate `n +ᵥ basisPositions i`. These positions must distinguish all
> sites, including copies in different cells.

**`CondensedMatter.Crystal.Geometry.ofUnitCell`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L116).

> Embed a repeated unit cell by translating its reference positions.
> The injectivity condition ensures that no two site addresses occupy the same point.

```lean
def ofUnitCell (G F : Type*) [AddGroup G] [Finite F] (A : Type*)
    [MetricSpace A] [AddAction G A] [IsIsometricVAdd G A]
    (basisPositions : F → A)
    (injective : Function.Injective (fun x : CellSite G F => x.cell +ᵥ basisPositions x.label)) :
    Geometry (Crystal.ofUnitCell G F) A
```

**`CondensedMatter.Crystal.Geometry.ofDisplacements`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L131).

> Embed a unit cell using physical displacements and reference positions.
> The translation map specifies the displacement of each cell; the injectivity condition
> ensures that different sites have different physical positions.

```lean
def ofDisplacements {G F A : Type*} [AddGroup G] [Finite F] [NormedAddCommGroup A]
    (displacement : G →+ A) (basisPositions : F → A)
    (injective : Function.Injective
      (fun x : CellSite G F => displacement x.cell + basisPositions x.label)) :
    Geometry (Crystal.ofUnitCell G F) A
```

**`CondensedMatter.Crystal.Geometry.position_ofDisplacements`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L141).

> A site's position is its cell displacement plus its position within the reference cell.

```lean
lemma position_ofDisplacements {G F A : Type*} [AddGroup G] [Finite F]
    [NormedAddCommGroup A] (displacement : G →+ A) (basisPositions : F → A)
    (injective : Function.Injective
      (fun x : CellSite G F => displacement x.cell + basisPositions x.label))
    (x : CellSite G F) :
    (ofDisplacements displacement basisPositions injective).position x =
      displacement x.cell + basisPositions x.label
```

**`CondensedMatter.Crystal.Geometry.ofLattice`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L150).

> A one-site unit cell embedded by an injective physical translation map.

```lean
def ofLattice {G A : Type*} [AddGroup G] [NormedAddCommGroup A]
    (displacement : G →+ A) (injective : Function.Injective displacement) :
    Geometry (Crystal.ofUnitCell G Unit) A
```

**`CondensedMatter.Crystal.Geometry.position_ofLattice`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L160).

> In a one-site cell, the site's position is its cell displacement.

```lean
lemma position_ofLattice {G A : Type*} [AddGroup G] [NormedAddCommGroup A]
    (displacement : G →+ A) (injective : Function.Injective displacement)
    (x : CellSite G Unit) : (ofLattice displacement injective).position x =
      displacement x.cell
```

## D. Bond lengths

> Translations preserve bond lengths. It therefore suffices to check the bonds starting
> in the reference cell to determine the lengths of all graph edges.

**`CondensedMatter.Crystal.Geometry.distance_of_links`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L174).

> Every translated copy of a bond has its reference-cell length.

```lean
lemma distance_of_links {G F A : Type*} [AddGroup G] [Finite F] [MetricSpace A]
    (R : Geometry (Crystal.ofUnitCell G F) A) (b : Bond G F)
    {x y : CellSite G F} (h : b.Links x y) :
    R.distance x y = R.distance ⟨0, b.source⟩ ⟨b.displacement, b.target⟩
```

**`CondensedMatter.Crystal.Geometry.distance_eq_of_adj`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L186).

> A common reference bond length gives the length of every generated graph edge.

```lean
lemma distance_eq_of_adj {G F A : Type*} [AddGroup G] [Finite F] [MetricSpace A]
    (R : Geometry (Crystal.ofUnitCell G F) A) (bonds : List (Bond G F)) (length : ℝ)
    (h : ∀ b ∈ bonds, R.distance ⟨0, b.source⟩ ⟨b.displacement, b.target⟩ = length)
    {x y : CellSite G F} (hxy : (graphFromBonds bonds).Adj x y) : R.distance x y = length
```

## E. Euclidean lattice displacements

> Primitive vectors specify the physical displacement of an integer cell index. Their
> linear independence ensures that distinct cells have distinct displacements.

**`CondensedMatter.Crystal.latticeMap`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L205).

> Convert integer cell coordinates into physical displacements along primitive vectors.

```lean
noncomputable def latticeMap {d D : ℕ} (vectors : Fin d → EuclideanSpace ℝ (Fin D)) :
    (Fin d → ℤ) →+ EuclideanSpace ℝ (Fin D)
```

**`CondensedMatter.Crystal.latticeMap_injective`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean#L212).

> Independent primitive vectors separate the displacements of different cells.

```lean
lemma latticeMap_injective {d D : ℕ} {vectors : Fin d → EuclideanSpace ℝ (Fin D)}
    (independent : LinearIndependent ℝ vectors) : Function.Injective (latticeMap vectors)
```

## Depends on

- [Crystal bonds and connectivity](graph.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/Geometry.lean)
