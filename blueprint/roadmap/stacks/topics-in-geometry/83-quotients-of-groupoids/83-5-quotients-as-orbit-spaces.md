---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PreRelation.pointOrbit, AlgebraicGeometry.Space.PreRelation.pointOrbit_eq_targets_of_source, AlgebraicGeometry.Space.pointsMap_eq_of_mem_pointOrbit, AlgebraicGeometry.Space.PreRelation.WeaklyEquivalent, AlgebraicGeometry.Space.PreRelation.Equivalent, AlgebraicGeometry.Space.PreRelation.weakOrbit, AlgebraicGeometry.Space.PreRelation.orbit, AlgebraicGeometry.Space.PreRelation.weakOrbit_eq_targets
statement: formalized
proof: formalized
---

# 83.5 Quotients as orbit spaces

Section 83.5 of the Stacks Project, [Tag 048M](https://stacks.math.columbia.edu/tag/048M). 21 tags here are carried by 53 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 048N, a definition

[Tag 048N](https://stacks.math.columbia.edu/tag/048N) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.pointOrbit`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/PointOrbits.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/PointOrbits.lean#L81).

> **Stacks 048N.** The *orbit* of a point of `|U|` under a pre-relation `j : R ⟶ U ×_Z U`:
> the set of points joined to it by a finite chain of arrows of `j`, traversed in either
> direction, with stationary steps allowed.

```lean
noncomputable abbrev PreRelation.pointOrbit (j : PreRelation R U)
    (u : points B S hS U.left) : Set (points B S hS U.left)
```

## Tag 048O, a lemma

[Tag 048O](https://stacks.math.columbia.edu/tag/048O) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.pointOrbit_eq_targets_of_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/PointOrbits.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/PointOrbits.lean#L90).

> **Stacks 048O.** For a pre-equivalence relation an orbit is cut out by a single arrow: it
> consists of the targets of the arrows of the pre-relation whose source is the given point.

```lean
theorem PreRelation.pointOrbit_eq_targets_of_source (j : PreRelation R U)
    (hj : IsPreEquivalenceRelation j) (u : points B S hS U.left) :
    j.pointOrbit u =
      {u' | ∃ r : points B S hS R.left,
        pointsMap B S hS R.left j.source.left r = u ∧
          pointsMap B S hS R.left j.target.left r = u'}
```

## Tag 048P, a lemma

[Tag 048P](https://stacks.math.columbia.edu/tag/048P) in the Stacks Project.

**`AlgebraicGeometry.Space.pointsMap_eq_of_mem_pointOrbit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/PointOrbits.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/PointOrbits.lean#L119).

> **Stacks 048P.** A morphism out of `U` which is invariant under a pre-relation takes the
> same value at any two points in one orbit.

```lean
theorem pointsMap_eq_of_mem_pointOrbit (j : PreRelation R U)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (φ : U.left ⟶ X)
    (hφ : IsInvariant j φ)
    {x y : points B S hS U.left} (hy : y ∈ j.pointOrbit x) :
    pointsMap B S hS U.left φ x = pointsMap B S hS U.left φ y
```

## Tag 048Q, a definition

[Tag 048Q](https://stacks.math.columbia.edu/tag/048Q) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.WeaklyEquivalent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean#L76). The attribute's comment: “part (1): weak equivalence”.

> Two points of `U` over a field-valued point `p` of `Z` are
> *weakly equivalent* when they are joined by a finite chain of arrows of the pre-relation over
> the field of `p`, traversed in either direction and with stationary steps allowed.

```lean
abbrev WeaklyEquivalent (j : PreRelation R U) (p : FieldValuedPoint B S hS Z)
    (x y : TestPoint (p.siteObject B S hS Z) (yonedaEquiv.symm p.value) U) : Prop
```

**`AlgebraicGeometry.Space.PreRelation.Equivalent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean#L84). The attribute's comment: “part (2): equivalence after extension”.

> Two points of `U` over a field-valued point `p` of `Z` are
> *equivalent* when their restrictions to some extension of the field of `p` are weakly
> equivalent.

```lean
abbrev Equivalent (j : PreRelation R U) (p : FieldValuedPoint B S hS Z)
    (x y : TestPoint (p.siteObject B S hS Z) (yonedaEquiv.symm p.value) U) : Prop
```

**`AlgebraicGeometry.Space.PreRelation.weakOrbit`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean#L94). The attribute's comment: “part (3): weak orbit”.

> The *weak orbit* of a point of `U` over a geometric point of
> `Z`: its class for weak equivalence over the given algebraically closed field.

```lean
abbrev weakOrbit (j : PreRelation R U) (p : GeometricPoint B S hS Z)
    (x : TestPoint (p.val.siteObject B S hS Z) (yonedaEquiv.symm p.val.value) U) :
    Set (TestPoint (p.val.siteObject B S hS Z) (yonedaEquiv.symm p.val.value) U)
```

**`AlgebraicGeometry.Space.PreRelation.orbit`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean#L102). The attribute's comment: “part (4): orbit”.

> The *orbit* of a point of `U` over a geometric point of `Z`:
> its class for equivalence, that is after allowing one extension of the field.

```lean
abbrev orbit (j : PreRelation R U) (p : GeometricPoint B S hS Z)
    (x : TestPoint (p.val.siteObject B S hS Z) (yonedaEquiv.symm p.val.value) U) :
    Set (TestPoint (p.val.siteObject B S hS Z) (yonedaEquiv.symm p.val.value) U)
```

## Tag 048R, a lemma

[Tag 048R](https://stacks.math.columbia.edu/tag/048R) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.weakOrbit_eq_targets`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean#L115). The attribute's comment: “weak orbit”.

> For a pre-equivalence relation the weak orbit of a point is cut out by a
> single arrow: it consists of the targets of the arrows whose source is that point.

```lean
theorem weakOrbit_eq_targets (j : PreRelation R U) (hj : IsPreEquivalenceRelation j)
    (p : GeometricPoint B S hS Z)
    (x : TestPoint (p.val.siteObject B S hS Z) (yonedaEquiv.symm p.val.value) U) :
    j.weakOrbit p x = {y | j.Rel (yonedaEquiv.symm p.val.value) y x}
```

**`AlgebraicGeometry.Space.PreRelation.orbit_eq_targets_after_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricOrbits.lean#L125). The attribute's comment: “orbit”.

> For a pre-equivalence relation the orbit of a point is cut out by a
> single arrow over some extension of the field of the geometric point.

```lean
theorem orbit_eq_targets_after_extension (j : PreRelation R U)
    (hj : IsPreEquivalenceRelation j) (p : GeometricPoint B S hS Z)
    (x : TestPoint (p.val.siteObject B S hS Z) (yonedaEquiv.symm p.val.value) U) :
    j.orbit p x =
      {y | ∃ (q : FieldValuedPoint B S hS Z)
          (f : q.siteObject B S hS Z ⟶ p.val.siteObject B S hS Z),
          Z.map f.op p.val.value = q.value ∧
            ∃ x' y' : TestPoint (q.siteObject B S hS Z) (yonedaEquiv.symm q.value) U,
              x'.1 = yoneda.map f ≫ x.1 ∧ y'.1 = yoneda.map f ≫ y.1 ∧
                j.Rel (yonedaEquiv.symm q.value) y' x'}
```

## Tag 048S, an equation

[Tag 048S](https://stacks.math.columbia.edu/tag/048S) in the Stacks Project.

**`AlgebraicGeometry.Space.flippedRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean#L80). The attribute's comment: “flip map”.

> The *flipped* arrow of a pre-relation, `r ↦ (s(r), t(r))`: the map to `U ×_B U` that
> reverses each arrow of `j`.

```lean
noncomputable def flippedRelation {R U : Over B} (j : PreRelation R U) : R ⟶ U ⨯ U
```

**`AlgebraicGeometry.Space.composedRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean#L86). The attribute's comment: “composable-pair map”.

> The endpoint map on composable pairs, `(r, r') ↦ (t(r), s(r'))`: the map to `U ×_B U`
> recording the outer endpoints of a pair of arrows of `j` that compose.

```lean
noncomputable def composedRelation {R U : Over B} (j : PreRelation R U) :
    pullback j.source j.target ⟶ U ⨯ U
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.diag`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.diag#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean#L71) (StacksFrontier): “diagonal map”. References: EGA I (10.15.1); EGA I (5.3.1); EGA IV (17.13.9), “binary diagonal”; SGA 4 IV (5.11.1).

## Tag 048T, a lemma

[Tag 048T](https://stacks.math.columbia.edu/tag/048T) in the Stacks Project.

**`AlgebraicGeometry.Space.allPathsRelation_source_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationFiniteType.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationFiniteType.lean#L127). The attribute's comment: “part (5): locally of finite type”.

> **Stacks 048T, part (5).** The source map of the relation of all finite paths is locally of
> finite type when both endpoint maps of the original pre-relation are.

```lean
theorem allPathsRelation_source_locallyOfFiniteType (P : PathConstruction j)
    (hs : IsLocallyOfFiniteType site S hS j.source.left.hom)
    (ht : IsLocallyOfFiniteType site S hS j.target.left.hom) :
    IsLocallyOfFiniteType site S hS P.allPathsRelation.source.left.hom
```

**`AlgebraicGeometry.Space.allPathsRelation_target_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationFiniteType.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationFiniteType.lean#L142). The attribute's comment: “part (5): locally of finite type”.

> **Stacks 048T, part (5).** The target map of the relation of all finite paths is locally of
> finite type when both endpoint maps of the original pre-relation are.

```lean
theorem allPathsRelation_target_locallyOfFiniteType (P : PathConstruction j)
    (hs : IsLocallyOfFiniteType site S hS j.source.left.hom)
    (ht : IsLocallyOfFiniteType site S hS j.target.left.hom) :
    IsLocallyOfFiniteType site S hS P.allPathsRelation.target.left.hom
```

**`AlgebraicGeometry.Space.isInvariant_allPathsRelation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationInvariance.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationInvariance.lean#L160). The attribute's comment: “part (1): invariance under the generated relation”.

> **Stacks 048T, part (1).** A morphism out of `U` is invariant under a pre-relation exactly
> when it is invariant under the relation of all finite paths that the pre-relation generates.
>
> The codomain is an arbitrary algebraic space over `S`; for a morphism `φ` of algebraic spaces
> over `B` take `φ.left`.

```lean
theorem isInvariant_allPathsRelation_iff (P : PathConstruction j) (φ : U.left ⟶ X) :
    IsInvariant P.allPathsRelation φ ↔ IsInvariant j φ
```

**`AlgebraicGeometry.Space.weakOrbit_allPathsRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationOrbits.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationOrbits.lean#L184). The attribute's comment: “part (3): weak orbits are unchanged”.

> **Stacks 048T, part (3).** The weak orbit of a point of `U` at a geometric point of `B` is
> unchanged when the pre-relation is replaced by the relation of all finite paths it
> generates.

```lean
theorem weakOrbit_allPathsRelation (p : GeometricPoint site S hS B.obj)
    (x : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value) ((overForgetSpace B).obj U)) :
    (presheafPreRelation P.allPathsRelation).weakOrbit p x =
      (presheafPreRelation j).weakOrbit p x
```

**`AlgebraicGeometry.Space.orbit_allPathsRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationOrbits.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationOrbits.lean#L209). The attribute's comment: “part (4): orbits are unchanged”.

> **Stacks 048T, part (4).** The orbit of a point of `U` at a geometric point of `B` is
> unchanged when the pre-relation is replaced by the relation of all finite paths it
> generates.

```lean
theorem orbit_allPathsRelation (p : GeometricPoint site S hS B.obj)
    (x : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value) ((overForgetSpace B).obj U)) :
    (presheafPreRelation P.allPathsRelation).orbit p x =
      (presheafPreRelation j).orbit p x
```

**`AlgebraicGeometry.Space.isPreEquivalenceRelation_allPathsRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationPreEquivalence.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationPreEquivalence.lean#L324). The attribute's comment: “the generated relation is a pre-equivalence relation”.

> **Stacks 048T.** The relation generated by a pre-relation of algebraic spaces over `B`,
> whose arrows are the finite composable paths of original, identity and reversed arrows, is a
> pre-equivalence relation over `B`: on the points of every test scheme over `B` it induces an
> equivalence relation.
>
> Reflexivity is witnessed by the identity arrow of a point, symmetry by the reverse of a path,
> and transitivity by the concatenation of two paths.

```lean
theorem isPreEquivalenceRelation_allPathsRelation (P : PathConstruction j) :
    IsPreEquivalenceRelation (presheafPreRelation P.allPathsRelation)
```

**`AlgebraicGeometry.Space.isIso_quotientSheafToAllPaths`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationQuotientSheaf.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GeneratedRelationQuotientSheaf.lean#L231). The attribute's comment: “part (2): the quotient sheaf is unchanged”.

> **Stacks 048T**, part (2). The canonical map of quotient sheaves `U/R ⟶ U/R_∞`, from the
> quotient by a pre-relation to the quotient by the relation of all the finite paths it generates,
> is an isomorphism.

```lean
theorem isIso_quotientSheafToAllPaths (P : PathConstruction j) :
    IsIso (quotientSheafToAllPaths P)
```

## Tag 048U, a lemma

[Tag 048U](https://stacks.math.columbia.edu/tag/048U) in the Stacks Project.

**`AlgebraicGeometry.Space.equivalent_iff_weaklyEquivalent_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricQuotient.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricQuotient.lean#L84). The attribute's comment: “finite\_type\_equivalence”.

> **Stacks 048U.** For a pre-relation whose source and target are locally of finite type,
> two points of `U` over a geometric point of `B` are equivalent exactly when they are already
> weakly equivalent over the field of that geometric point: no extension of the field is
> needed.

```lean
theorem equivalent_iff_weaklyEquivalent_of_locallyOfFiniteType (j : PreRelation R U)
    (hs : IsLocallyOfFiniteType site S hS j.source.left.hom)
    (ht : IsLocallyOfFiniteType site S hS j.target.left.hom)
    (p : GeometricPoint site S hS B.obj)
    (x y : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value)
      ((overForgetSpace B).obj U)) :
    (presheafPreRelation j).Equivalent p.val x y ↔
      (presheafPreRelation j).WeaklyEquivalent p.val x y
```

**`AlgebraicGeometry.Space.orbit_eq_weakOrbit_of_large_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/LargeFields.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/LargeFields.lean#L198). The attribute's comment: “large\_field\_orbits”.

> **Stacks 048U, part (2).** Over a sufficiently large algebraically closed field the orbit
> of a point of `U` under a pre-relation is its weak orbit over the same field: no extension of
> the field is needed. The bound is on the relation generated by the pre-relation, and is
> uniform in the geometric point and in the point whose orbit is taken.

```lean
theorem orbit_eq_weakOrbit_of_large_field {j : PreRelation R U} (P : PathConstruction j)
    (p : GeometricPoint site S hS B.obj)
    (hp : IsLargeField site S hS P.allPaths.left.obj p.val.carrier)
    (x : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value)
      ((overForgetSpace B).obj U)) :
    (presheafPreRelation j).orbit p x = (presheafPreRelation j).weakOrbit p x
```

**`AlgebraicGeometry.Space.equivalent_iff_weaklyEquivalent_of_large_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/LargeFields.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/LargeFields.lean#L213). The attribute's comment: “large\_field\_equivalence”.

> **Stacks 048U, part (2).** Over a sufficiently large algebraically closed field,
> equivalence of two points of `U` under a pre-relation is their weak equivalence over the same
> field. The bound is on the relation generated by the pre-relation, and is uniform in the
> geometric point and in the pair of points.

```lean
theorem equivalent_iff_weaklyEquivalent_of_large_field {j : PreRelation R U}
    (P : PathConstruction j) (p : GeometricPoint site S hS B.obj)
    (hp : IsLargeField site S hS P.allPaths.left.obj p.val.carrier)
    (x y : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value)
      ((overForgetSpace B).obj U)) :
    (presheafPreRelation j).Equivalent p.val x y ↔
      (presheafPreRelation j).WeaklyEquivalent p.val x y
```

## Tag 048V, a definition

[Tag 048V](https://stacks.math.columbia.edu/tag/048V) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSetTheoreticallyInvariant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean#L68). The attribute's comment: “part (1): set-theoretic invariance”.

> A morphism out of `U` is *set-theoretically invariant* under a
> pre-relation when it takes the same value at the two endpoints of every arrow of the
> pre-relation between points over an algebraically closed field.

```lean
abbrev IsSetTheoreticallyInvariant (j : PreRelation R U) (φ : U.left ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.SeparatesOrbits`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean#L77). The attribute's comment: “part (2): separation of orbits”.

> A morphism out of `U` *separates the orbits* of a pre-relation
> when it is set-theoretically invariant and two points over an algebraically closed field with
> the same image lie in one orbit.

```lean
abbrev SeparatesOrbits (j : PreRelation R U) (φ : U.left ⟶ X) : Prop
```

## Tag 048W, a lemma

[Tag 048W](https://stacks.math.columbia.edu/tag/048W) in the Stacks Project.

**`AlgebraicGeometry.Space.isSetTheoreticallyInvariant_iff_eq_of_mem_orbit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceOnOrbits.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceOnOrbits.lean#L190).

> A morphism from `U` to an algebraic space is set-theoretically invariant under a
> pre-relation if and only if, for every algebraically closed field over the base, the induced map
> on the points of `U` over that field is constant on the orbits of the pre-relation.

```lean
theorem isSetTheoreticallyInvariant_iff_eq_of_mem_orbit (hX : IsAlgebraicSpace B S hS X)
    (j : PreRelation R U) (φ : U.left ⟶ X) :
    IsSetTheoreticallyInvariant j φ ↔
      ∀ (p : GeometricPoint B S hS Z)
        (x y : TestPoint (p.val.siteObject B S hS Z) (yonedaEquiv.symm p.val.value) U),
        y ∈ j.orbit p x → x.1 ≫ φ = y.1 ≫ φ
```

## Tag 048X, a lemma

[Tag 048X](https://stacks.math.columbia.edu/tag/048X) in the Stacks Project.

**`AlgebraicGeometry.Space.isSetTheoreticallyInvariant_of_isInvariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean#L85).

> A morphism which is invariant under a pre-relation is set-theoretically invariant.

```lean
theorem isSetTheoreticallyInvariant_of_isInvariant (j : PreRelation R U) (φ : U.left ⟶ X)
    (hφ : IsInvariant j φ) :
    IsSetTheoreticallyInvariant j φ
```

## Tag 048Y, a lemma

[Tag 048Y](https://stacks.math.columbia.edu/tag/048Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isInvariant_of_isSetTheoreticallyInvariant_of_reduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/ReducedRelation.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/ReducedRelation.lean#L230).

> **Stacks 048Y.** On a reduced relation space, set-theoretic invariance of a morphism to a
> locally separated target implies that the morphism is invariant under the pre-relation.

```lean
theorem isInvariant_of_isSetTheoreticallyInvariant_of_reduced {R U X : Over Z}
    (j : PreRelation R U)
    (φ : U ⟶ X) (hφ : IsSetTheoreticallyInvariant j φ.left)
    (hR : HasEtaleLocalProperty B S hS R.left (fun Y : Scheme.{u} ↦ IsReduced Y))
    (hX : IsLocallySeparated B S hS X.hom)
    (hXsheaf : Presheaf.IsSheaf (BigFppfOver.topology B S hS) X.left) :
    IsInvariant j φ.left
```

## Tag 048Z, an example

[Tag 048Z](https://stacks.math.columbia.edu/tag/048Z) in the Stacks Project.

**`AlgebraicGeometry.Space.diskToInvolutionQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean#L328). The attribute's comment: “the coordinate map to the quotient”.

> **Stacks 048Z.** The morphism from the formal disk to the quotient of the affine line by
> the involution relation given by the power-series variable.

```lean
noncomputable def diskToInvolutionQuotient
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    yoneda.obj (siteFormalDisk k B hS hD) ⟶ (involutionQuotient k B hS).obj
```

**`AlgebraicGeometry.Space.diskToInvolutionQuotientNeg`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean#L337). The attribute's comment: “the negated coordinate map to the quotient”.

> **Stacks 048Z.** The morphism from the formal disk to the quotient of the affine line by
> the involution relation given by the negative of the power-series variable.

```lean
noncomputable def diskToInvolutionQuotientNeg
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    yoneda.obj (siteFormalDisk k B hS hD) ⟶ (involutionQuotient k B hS).obj
```

**`AlgebraicGeometry.Space.diskMaps_agree_on_fieldPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean#L412). The attribute's comment: “agreement on field-valued points”.

> **Stacks 048Z.** The two morphisms from the formal disk to the quotient agree after
> every field-valued point of the disk.

```lean
theorem diskMaps_agree_on_fieldPoints
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)]
    (K : Type u) [Field K] (hK : B.Contains (Spec (.of K)))
    (β : Spec (.of K) ⟶ Spec (.of k))
    (g : (Over.mk (ObjectProperty.homMk β : B.obj hK ⟶ B.obj hS) :
      BigFppfOver B (Spec (.of k)) hS) ⟶ siteFormalDisk k B hS hD) :
    yoneda.map g ≫ diskToInvolutionQuotient k B hS hD =
      yoneda.map g ≫ diskToInvolutionQuotientNeg k B hS hD
```

**`AlgebraicGeometry.Space.diskMaps_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean#L563). The attribute's comment: “distinct morphisms”.

> **Stacks 048Z.** Away from characteristic two, the two morphisms from the formal disk to
> the quotient are nevertheless distinct.

```lean
theorem diskMaps_ne (hchar : (2 : k) ≠ 0)
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    diskToInvolutionQuotient k B hS hD ≠ diskToInvolutionQuotientNeg k B hS hD
```

**`AlgebraicGeometry.Space.exists_setTheoreticallyInvariant_not_invariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean#L618). The attribute's comment: “quasi-separatedness does not suffice”.

> **Stacks 048Z.** Quasi-separatedness of the target cannot replace local separatedness in
> the criterion `AlgebraicGeometry.Space.isInvariant_of_isSetTheoreticallyInvariant_of_reduced`
> (**Stacks 048Y**): over a field in which two is invertible there is a pre-relation on a
> reduced algebraic space, with quasi-separated target, carrying a set-theoretically invariant
> morphism which is not invariant.
>
> The relation is the formal disk, acting on itself by the identity and by negation of the
> coordinate, and the morphism is the coordinate map to the quotient of the affine line by the
> involution relation.  Quasi-separatedness of that quotient is **Stacks 02Z1**, taken from
> `AlgebraicGeometry.AffineLineInvolution.isAbsolutelyQuasiSeparated_involutionQuotient` and
> converted to quasi-separatedness of the structure morphism by **Stacks 073B** part (2).

```lean
theorem exists_setTheoreticallyInvariant_not_invariant (hchar : (2 : k) ≠ 0)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    ∃ (Z : (BigFppfOver B (Spec (.of k)) hS)ᵒᵖ ⥤ Type u) (R U X : Over Z)
      (j : PreRelation R U) (φ : U ⟶ X),
      HasEtaleLocalProperty B (Spec (.of k)) hS R.left (fun T : Scheme.{u} ↦ IsReduced T) ∧
        IsQuasiSeparated B (Spec (.of k)) hS X.hom ∧
        IsSetTheoreticallyInvariant j φ.left ∧ ¬ IsInvariant j φ.left
```

**`AlgebraicGeometry.Space.exists_agree_on_fieldPoints_ne_and_not_invariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean, line 755](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NonInvariantFormalDiskExample.lean#L755).

> **Stacks 048Z.** Over a field in which two is invertible there are reduced
> quasi-separated algebraic spaces `X`, `Y` and two morphisms `a, b : Y ⟶ X` which agree on
> every field-valued point of `Y` yet are not equal; consequently quasi-separatedness of the
> target cannot replace local separatedness in the criterion
> `AlgebraicGeometry.Space.isInvariant_of_isSetTheoreticallyInvariant_of_reduced` (**Stacks
> 048Y**), because there is a pre-relation on a reduced algebraic space with quasi-separated
> target carrying a set-theoretically invariant morphism which is not invariant.
>
> The spaces are `Y = Spec k[[x]]` and `X = 𝔸¹_k/(Δ ⨿ {(x, -x) | x ≠ 0})`, the algebraic space
> of **Stacks 02Z1**, and the two morphisms are the coordinate and its negative followed by the
> projection to the quotient.  The pre-relation witnessing the second assertion is `Y` acting
> on itself by the identity and by negation of the coordinate.

```lean
theorem exists_agree_on_fieldPoints_ne_and_not_invariant (hchar : (2 : k) ≠ 0)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    (∃ (X Y : (BigFppfOver B (Spec (.of k)) hS)ᵒᵖ ⥤ Type u) (a b : Y ⟶ X),
        IsAlgebraicSpace B (Spec (.of k)) hS X ∧
        IsAlgebraicSpace B (Spec (.of k)) hS Y ∧
        HasEtaleLocalProperty B (Spec (.of k)) hS X (fun T : Scheme.{u} ↦ IsReduced T) ∧
        HasEtaleLocalProperty B (Spec (.of k)) hS Y (fun T : Scheme.{u} ↦ IsReduced T) ∧
        IsAbsolutelyQuasiSeparated B (Spec (.of k)) hS hZ X ∧
        IsAbsolutelyQuasiSeparated B (Spec (.of k)) hS hZ Y ∧
        (∀ (K : Type u) [Field K] (hK : B.Contains (Spec (.of K)))
            (β : Spec (.of K) ⟶ Spec (.of k))
            (g : yoneda.obj (Over.mk (ObjectProperty.homMk β : B.obj hK ⟶ B.obj hS) :
              BigFppfOver B (Spec (.of k)) hS) ⟶ Y),
          g ≫ a = g ≫ b) ∧
        a ≠ b) ∧
      ∃ (Z : (BigFppfOver B (Spec (.of k)) hS)ᵒᵖ ⥤ Type u) (R U X : Over Z)
        (j : PreRelation R U) (φ : U ⟶ X),
        HasEtaleLocalProperty B (Spec (.of k)) hS R.left
            (fun T : Scheme.{u} ↦ IsReduced T) ∧
          IsQuasiSeparated B (Spec (.of k)) hS X.hom ∧
          IsSetTheoreticallyInvariant j φ.left ∧ ¬ IsInvariant j φ.left
```

## Tag 0490, a definition

[Tag 0490](https://stacks.math.columbia.edu/tag/0490) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSetTheoreticPreEquivalenceRelation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean#L131). The attribute's comment: “part (1): set-theoretic pre-equivalence relation”.

> **Stacks 0490, part (1).** A pre-relation is a *set-theoretic pre-equivalence relation*
> when the relation it induces on the fibres of the points over every algebraically closed
> field in the site is an equivalence relation, arrows being allowed to appear only after a
> field extension.

```lean
abbrev IsSetTheoreticPreEquivalenceRelation (j : PreRelation R U) : Prop
```

**`AlgebraicGeometry.Space.IsSetTheoreticEquivalenceRelation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean#L139). The attribute's comment: “part (2): set-theoretic equivalence relation”.

> **Stacks 0490, part (2).** A *set-theoretic equivalence relation* is a universally
> injective set-theoretic pre-equivalence relation.

```lean
abbrev IsSetTheoreticEquivalenceRelation (j : PreRelation R U) : Prop
```

## Tag 0491, a lemma

[Tag 0491](https://stacks.math.columbia.edu/tag/0491) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.ContainsRelationImages`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean, line 837](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean#L837). The attribute's comment: “part (2): the three image containments”.

> **Stacks 0491, part (2).** A pre-relation *contains the relation images* when its image on
> topological points contains the images of the diagonal of `U`, of the flip of the pre-relation
> and of the endpoint map on composable pairs of arrows.

```lean
noncomputable abbrev PreRelation.ContainsRelationImages (j : PreRelation R U) : Prop
```

**`AlgebraicGeometry.Space.isSetTheoreticPreEquivalenceRelation_iff_containsRelationImages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean, line 850](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean#L850). The attribute's comment: “parts (1) and (2)”.

> **Stacks 0491, parts (1) and (2).** A pre-relation is a set-theoretic pre-equivalence
> relation exactly when its image on points contains the images of the diagonal, of the flip and
> of the endpoint map on composable pairs.

```lean
theorem isSetTheoreticPreEquivalenceRelation_iff_containsRelationImages
    (j : PreRelation R U) :
    IsSetTheoreticPreEquivalenceRelation (presheafPreRelation j) ↔
      j.ContainsRelationImages
```

**`AlgebraicGeometry.Space.containsRelationImages_iff_exists_geometricRel_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean, line 1051](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean#L1051). The attribute's comment: “parts (2) and (3)”.

> **Stacks 0491, parts (2) and (3).** The three image containments hold exactly when the
> relation cut out by the arrows already present over `k` is an equivalence relation for every
> algebraically closed field `k` in the site above one cardinal strictly below the size cutoff
> of the site.

```lean
theorem containsRelationImages_iff_exists_geometricRel_equivalence (j : PreRelation R U) :
    j.ContainsRelationImages ↔
      ∃ κ : Cardinal.{u}, κ < site.cutoff ∧ ∀ (k : Type u) [Field k] [IsAlgClosed k]
        (hk : site.Contains (Spec (.of k))) (b : Spec (.of k) ⟶ S)
        (β : B.obj.obj (Opposite.op (fieldObject (hS := hS) k hk b))),
        κ < Cardinal.mk k → Equivalence ((presheafPreRelation j).GeometricRel k hk b β)
```

**`AlgebraicGeometry.Space.isSetTheoreticPreEquivalenceRelation_iff_geometricRel_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean, line 1080](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/PreEquivalenceGeometricCriterion.lean#L1080). The attribute's comment: “part (4)”.

> **Stacks 0491, part (4).** For a pre-relation whose source and target are locally of
> finite type no cardinal bound is needed: the set-theoretic pre-equivalence condition is
> equivalent to the relation of actual arrows being an equivalence relation over *every*
> algebraically closed field in the site.

```lean
theorem isSetTheoreticPreEquivalenceRelation_iff_geometricRel_equivalence
    (j : PreRelation R U) (_hs : IsLocallyOfFiniteType site S hS j.source.left.hom)
    (ht : IsLocallyOfFiniteType site S hS j.target.left.hom) :
    IsSetTheoreticPreEquivalenceRelation (presheafPreRelation j) ↔
      ∀ (k : Type u) [Field k] [IsAlgClosed k] (hk : site.Contains (Spec (.of k)))
        (b : Spec (.of k) ⟶ S)
        (β : B.obj.obj (Opposite.op (fieldObject (hS := hS) k hk b))),
        Equivalence ((presheafPreRelation j).GeometricRel k hk b β)
```

## Tag 049X, a lemma

[Tag 049X](https://stacks.math.columbia.edu/tag/049X) in the Stacks Project.

**`AlgebraicGeometry.Space.isSetTheoreticEquivalenceRelation_iff_containsRelationImages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalenceCriterion.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalenceCriterion.lean#L405). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 049X, conditions (1) and (2).** A pre-relation of algebraic spaces is a
> set-theoretic equivalence relation exactly when it is universally injective and its image on
> topological points contains the images of the diagonal of `U`, of its flip, and of the endpoint
> map on composable pairs of its arrows.
>
> Universal injectivity is one of the two conditions on either side, and the other two are
> equivalent by **Stacks 0491**.

```lean
theorem isSetTheoreticEquivalenceRelation_iff_containsRelationImages (j : PreRelation R U) :
    IsSetTheoreticEquivalenceRelation (presheafPreRelation j) ↔
      UniversallyInjective site S hS (presheafPreRelation j).left ∧
        j.ContainsRelationImages
```

**`AlgebraicGeometry.Space.isSetTheoreticEquivalenceRelation_iff_exists_hasGeometricEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalenceCriterion.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalenceCriterion.lean#L421). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 049X, conditions (1) and (3).** A pre-relation of algebraic spaces is a
> set-theoretic equivalence relation exactly when, over every algebraically closed field in the
> site above one cardinal strictly below the size cutoff of the site, its map on arrows is
> injective and the relation its arrows cut out is an equivalence relation.
>
> The equivalence-relation half is **Stacks 0491**. Universal injectivity gives the injectivity
> over every sufficiently large field through the descent of a point of `R` along the relative
> diagonal of `j`, and conversely injectivity over all sufficiently large fields makes that
> diagonal surjective on points, which is universal injectivity by **Stacks 040X**.

```lean
theorem isSetTheoreticEquivalenceRelation_iff_exists_hasGeometricEquivalence
    (j : PreRelation R U) :
    IsSetTheoreticEquivalenceRelation (presheafPreRelation j) ↔
      ∃ κ : Cardinal.{u}, κ < site.cutoff ∧ ∀ (k : Type u) [Field k] [IsAlgClosed k]
        (hk : site.Contains (Spec (.of k))) (b : Spec (.of k) ⟶ S)
        (β : B.obj.obj (Opposite.op (fieldObject (hS := hS) k hk b))),
        κ < Cardinal.mk k → j.HasGeometricEquivalence k hk b β
```

**`AlgebraicGeometry.Space.isSetTheoreticEquivalenceRelation_iff_hasGeometricEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalenceCriterion.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalenceCriterion.lean#L547). The attribute's comment: “condition (4)”.

> **Stacks 049X, condition (4).** For a pre-relation of algebraic spaces which is decent,
> locally separated or quasi-separated the cardinality restriction can be dropped: it is a
> set-theoretic equivalence relation exactly when over *every* algebraically closed field in the
> site its map on arrows is injective and the relation its arrows cut out is an equivalence
> relation.
>
> Under any of the three hypotheses a universally injective pre-relation is radicial by
> **Stacks 0484**, and over an algebraically closed field a fibre of a radicial morphism has
> exactly one section as soon as it has a point: this gives the injectivity on arrows, and makes
> the relation cut out by the arrows present over the field agree with the one of
> **Stacks 0490**, where arrows are allowed to appear after a field extension.

```lean
theorem isSetTheoreticEquivalenceRelation_iff_hasGeometricEquivalence
    (j : PreRelation R U)
    (hsep : IsDecent site S hS (presheafPreRelation j).left ∨
      IsLocallySeparated site S hS (presheafPreRelation j).left ∨
      IsQuasiSeparated site S hS (presheafPreRelation j).left) :
    IsSetTheoreticEquivalenceRelation (presheafPreRelation j) ↔
      ∀ (k : Type u) [Field k] [IsAlgClosed k] (hk : site.Contains (Spec (.of k)))
        (b : Spec (.of k) ⟶ S)
        (β : B.obj.obj (Opposite.op (fieldObject (hS := hS) k hk b))),
        j.HasGeometricEquivalence k hk b β
```

## Tag 0492, a lemma

[Tag 0492](https://stacks.math.columbia.edu/tag/0492) in the Stacks Project.

**`AlgebraicGeometry.Space.isSetTheoreticPreEquivalenceRelation_of_isPreEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean#L182). The attribute's comment: “part (1): a pre-equivalence relation”.

> **Stacks 0492, part (1).** A pre-equivalence relation is a set-theoretic pre-equivalence
> relation: over every algebraically closed field over the base, the relation its arrows induce
> on the points of `U` — arrows being allowed to appear after an extension of the field — is an
> equivalence relation.

```lean
theorem isSetTheoreticPreEquivalenceRelation_of_isPreEquivalenceRelation
    (j : PreRelation R U) (hj : IsPreEquivalenceRelation j) :
    IsSetTheoreticPreEquivalenceRelation j
```

**`AlgebraicGeometry.Space.isSetTheoreticPreEquivalenceRelation_groupoidPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean#L249). The attribute's comment: “part (1): a groupoid in algebraic spaces”.

> **Stacks 0492, part (1).** The pre-relation of a groupoid in algebraic spaces is a
> set-theoretic pre-equivalence relation.

```lean
theorem isSetTheoreticPreEquivalenceRelation_groupoidPreRelation
    {A : AlgebraicSpaces B S hS} (G : GroupoidInAlgebraicSpaces B S hS A) :
    IsSetTheoreticPreEquivalenceRelation (groupoidPreRelation G)
```

**`AlgebraicGeometry.Space.isSetTheoreticPreEquivalenceRelation_groupoidOfAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean#L258). The attribute's comment: “part (1): an action of a group algebraic space”.

> **Stacks 0492, part (1).** The pre-relation of the groupoid of an action of a group
> algebraic space on an algebraic space is a set-theoretic pre-equivalence relation.

```lean
theorem isSetTheoreticPreEquivalenceRelation_groupoidOfAction
    (A : AlgebraicSpaces B S hS) (G W : Over A.obj) [GrpObj G] [ModObj G W]
    (hG : IsAlgebraicSpace B S hS G.left) (hW : IsAlgebraicSpace B S hS W.left) :
    IsSetTheoreticPreEquivalenceRelation
      (groupoidPreRelation (groupoidOfAction A G W hG hW).groupoid)
```

**`AlgebraicGeometry.Space.isSetTheoreticEquivalenceRelation_of_isEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/SetTheoreticEquivalence.lean#L269). The attribute's comment: “part (2)”.

> **Stacks 0492, part (2).** An equivalence relation is a set-theoretic equivalence
> relation: it is a monomorphism, hence universally injective, and a pre-equivalence relation,
> hence set-theoretically one.

```lean
theorem isSetTheoreticEquivalenceRelation_of_isEquivalenceRelation (j : PreRelation R U)
    (hj : CategoryTheory.IsEquivalenceRelation j.target j.source) :
    IsSetTheoreticEquivalenceRelation j
```

## Tag 049Y, a lemma

[Tag 049Y](https://stacks.math.columbia.edu/tag/049Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isSetTheoreticallyInvariant_iff_isSurjective_invarianceToRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean#L714). The attribute's comment: “part (1)”.

> **Stacks 049Y, part (1).** A morphism `φ : U ⟶ X` over the base, with `X` an algebraic
> space, is set-theoretically invariant under a pre-relation `j : R ⟶ U ×_Z U` if and only if
> the projection `p : (U ×_X U) ×_{U ×_Z U} R ⟶ R` is surjective.

```lean
theorem isSetTheoreticallyInvariant_iff_isSurjective_invarianceToRelation
    (hX : IsAlgebraicSpace B S hS X.left) (j : PreRelation R U) (φ : U ⟶ X) :
    IsSetTheoreticallyInvariant j φ.left ↔
      IsSurjective B S hS (j.invarianceToRelation φ).left
```

**`AlgebraicGeometry.Space.separatesOrbits_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean#L735). The attribute's comment: “part (3): separation of orbits”.

> **Stacks 049Y, part (3).** If both projections of the square are surjective, then the
> morphism `φ` separates the orbits of the pre-relation.

```lean
theorem separatesOrbits_of_isSurjective (hX : IsAlgebraicSpace B S hS X.left)
    (j : PreRelation R U) (φ : U ⟶ X)
    (hp : IsSurjective B S hS (j.invarianceToRelation φ).left)
    (hq : IsSurjective B S hS (j.invarianceToSelfFibreProduct φ).left) :
    SeparatesOrbits j φ.left
```

**`AlgebraicGeometry.Space.isSetTheoreticPreEquivalenceRelation_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean#L770). The attribute's comment: “part (3): set-theoretic pre-equivalence relation”.

> **Stacks 049Y, part (3).** If both projections of the square are surjective, then the
> pre-relation is a set-theoretic pre-equivalence relation.

```lean
theorem isSetTheoreticPreEquivalenceRelation_of_isSurjective
    (hX : IsAlgebraicSpace B S hS X.left) (j : PreRelation R U) (φ : U ⟶ X)
    (hp : IsSurjective B S hS (j.invarianceToRelation φ).left)
    (hq : IsSurjective B S hS (j.invarianceToSelfFibreProduct φ).left) :
    IsSetTheoreticPreEquivalenceRelation j
```

**`AlgebraicGeometry.Space.separatesOrbits_iff_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean, line 791](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean#L791). The attribute's comment: “part (2)”.

> **Stacks 049Y, part (2).** For a set-theoretic pre-equivalence relation, a morphism
> `φ : U ⟶ X` over the base, with `X` an algebraic space, separates the orbits of the
> pre-relation if and only if both projections `p` and `q` of the square are surjective.

```lean
theorem separatesOrbits_iff_isSurjective (hX : IsAlgebraicSpace B S hS X.left)
    (j : PreRelation R U) (φ : U ⟶ X) (hj : IsSetTheoreticPreEquivalenceRelation j) :
    SeparatesOrbits j φ.left ↔
      (IsSurjective B S hS (j.invarianceToRelation φ).left ∧
        IsSurjective B S hS (j.invarianceToSelfFibreProduct φ).left)
```

**`AlgebraicGeometry.Space.separatesOrbits_iff_isSurjective_toSelfFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean, line 857](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/InvarianceSquare.lean#L857). The attribute's comment: “part (4)”.

> **Stacks 049Y, part (4).** If `φ : U ⟶ X` is invariant under a set-theoretic
> pre-equivalence relation `j : R ⟶ U ×_Z U`, with `X` an algebraic space, then `φ` separates
> the orbits of `j` if and only if the induced morphism `(t, s) : R ⟶ U ×_X U` is
> surjective.

```lean
theorem separatesOrbits_iff_isSurjective_toSelfFibreProduct
    (hX : IsAlgebraicSpace B S hS X.left) (j : PreRelation R U) (φ : U ⟶ X)
    (hφ : IsInvariant j φ.left) (hj : IsSetTheoreticPreEquivalenceRelation j) :
    SeparatesOrbits j φ.left ↔
      IsSurjective B S hS (j.toSelfFibreProduct φ hφ).left
```

## Tag 0493, a definition

[Tag 0493](https://stacks.math.columbia.edu/tag/0493) in the Stacks Project.

**`AlgebraicGeometry.Space.IsOrbitSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSeparation.lean#L95).

> A morphism out of `U` is an *orbit space* for a pre-relation when it is
> invariant under the pre-relation, separates its orbits, and is surjective on points.

```lean
abbrev IsOrbitSpace (j : PreRelation R U) (φ : U.left ⟶ X) : Prop
```

## Tag 049Z, a lemma

[Tag 049Z](https://stacks.math.columbia.edu/tag/049Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isOrbitSpace_iff_isSurjective_toSelfFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSpaceCriterion.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/OrbitSpaceCriterion.lean#L84).

> **Stacks 049Z.** Let `j : R ⟶ U ×_Z U` be a set-theoretic pre-equivalence relation and
> let `φ : U ⟶ X` be a morphism over the base whose target is an algebraic space. Then `φ` is
> an orbit space for `j` if and only if
>
> 1. `φ` is invariant, `t ≫ φ = s ≫ φ`,
> 2. the induced morphism `(t, s) : R ⟶ U ×_X U` is surjective, and
> 3. the morphism `φ : U ⟶ X` is surjective.
>
> Condition (2) is stated for the morphism `(t, s)` built from the proof of condition (1), so
> the three conditions appear as an existential over that proof.

```lean
theorem isOrbitSpace_iff_isSurjective_toSelfFibreProduct
    (hX : IsAlgebraicSpace B S hS X.left) (j : PreRelation R U) (φ : U ⟶ X)
    (hj : IsSetTheoreticPreEquivalenceRelation j) :
    IsOrbitSpace j φ.left ↔
      ∃ hφ : IsInvariant j φ.left,
        IsSurjective B S hS (j.toSelfFibreProduct φ hφ).left ∧
          IsSurjective B S hS φ.left
```

## Tag 04A0, a lemma

[Tag 04A0](https://stacks.math.columbia.edu/tag/04A0) in the Stacks Project.

**`AlgebraicGeometry.Space.isOrbitSpace_iff_geometricPoints_quotient_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricQuotient.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/OrbitSpaces/GeometricQuotient.lean#L196).

> **Stacks 04A0.** For a pre-relation whose relation space and whose source are locally of
> finite type over the base, an invariant morphism out of `U` is an orbit space for the
> pre-relation exactly when, over every algebraically closed field-valued point of the base, it
> induces a bijection from the quotient of the points of `U` by the relation generated by the
> pre-relation onto the points of the target: every point of the target over that point of the
> base lifts, and two points of `U` have the same image precisely when they are weakly
> equivalent.

```lean
theorem isOrbitSpace_iff_geometricPoints_quotient_bijective {X : Over B}
    (j : PreRelation R U) (φ : U ⟶ X)
    (hR : IsLocallyOfFiniteType site S hS R.hom.hom)
    (hU : IsLocallyOfFiniteType site S hS U.hom.hom)
    (hφ : IsInvariant j φ.left) :
    IsOrbitSpace (presheafPreRelation j) φ.left.hom ↔
      ∀ p : GeometricPoint site S hS B.obj,
        (∀ y : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value)
            ((overForgetSpace B).obj X),
          ∃ x : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value)
            ((overForgetSpace B).obj U), x.1 ≫ φ.left.hom = y.1) ∧
        (∀ x y : TestPoint p.val.siteObject (yonedaEquiv.symm p.val.value)
            ((overForgetSpace B).obj U),
          x.1 ≫ φ.left.hom = y.1 ≫ φ.left.hom ↔
            (presheafPreRelation j).WeaklyEquivalent p.val x y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.5, Tag 048M](https://stacks.math.columbia.edu/tag/048M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
