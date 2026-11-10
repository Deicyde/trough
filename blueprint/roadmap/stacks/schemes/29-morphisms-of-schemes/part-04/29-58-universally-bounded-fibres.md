---
declaration: section
origin: cited
lean: AlgebraicGeometry.BoundsFiberDegrees, AlgebraicGeometry.HasUniversallyBoundedFibers, AlgebraicGeometry.cardinalMk_pullback_le_of_degree_le, AlgebraicGeometry.sum_finrank_residueField_le_of_degree_le, AlgebraicGeometry.hasUniversallyBoundedFibers_of_boundsFiberDegrees, AlgebraicGeometry.boundsFiberDegrees_iff_field_baseChange, AlgebraicGeometry.boundsFiberDegrees_iff_field_baseChange_of_nonneg, AlgebraicGeometry.boundsFiberDegrees_of_isFiniteLocallyFreeOfRank
statement: formalized
proof: formalized
---

# 29.58 Universally bounded fibres

Section 29.58 of the Stacks Project, [Tag 03J3](https://stacks.math.columbia.edu/tag/03J3). 10 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03J4, a definition

[Tag 03J4](https://stacks.math.columbia.edu/tag/03J4) in the Stacks Project.

**`AlgebraicGeometry.BoundsFiberDegrees`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBounded.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBounded.lean#L50). The attribute's comment: “part (1)”.

> An integer bounds the degrees of the fibres of `f` if each fibre is finite locally free of
> some rank no greater than that integer.

```lean
public abbrev BoundsFiberDegrees {X Y : Scheme.{u}} (f : X ⟶ Y) (n : ℤ) : Prop
```

**`AlgebraicGeometry.HasUniversallyBoundedFibers`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBounded.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBounded.lean#L56). The attribute's comment: “part (2)”.

> The fibres of `f` are universally bounded if their degrees have a common integer bound.

```lean
public abbrev HasUniversallyBoundedFibers {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

## Tag 03J5, a lemma

[Tag 03J5](https://stacks.math.columbia.edu/tag/03J5) in the Stacks Project.

**`AlgebraicGeometry.cardinalMk_pullback_le_of_degree_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FibreCardinality.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FibreCardinality.lean#L77). The attribute's comment: “card\_fibre\_le\_bound”.

> **Stacks Project, Tag 03J5.** If all field-valued base changes of a morphism are finite of
> degree at most `n`, then each of them has at most `n` points.

```lean
theorem cardinalMk_pullback_le_of_degree_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) (n : ℕ)
    (h : ∀ (k : Type u) [Field k] (g : Spec (.of k) ⟶ Y),
      ∃ r ≤ n, Stacks.Morphisms.IsFiniteLocallyFreeOfRank (pullback.fst g f) r) :
    ∀ (k : Type u) [Field k] (g : Spec (.of k) ⟶ Y),
      Cardinal.mk (pullback g f : Scheme.{u}) ≤ n
```

**`AlgebraicGeometry.sum_finrank_residueField_le_of_degree_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/ResidueDegreeBound.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/ResidueDegreeBound.lean#L121). The attribute's comment: “sum\_residue\_degrees\_le\_bound”.

> **Stacks Project, Tag 03J5.** In a field-valued base change whose degree is uniformly bounded
> by `n`, the sum of the residue degrees at any finite family of distinct points is at most `n`.

```lean
public theorem sum_finrank_residueField_le_of_degree_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) (n : ℕ)
    (h : ∀ (k : Type u) [Field k] (g : Spec (.of k) ⟶ Y),
      ∃ r ≤ n, Stacks.Morphisms.IsFiniteLocallyFreeOfRank (pullback.fst g f) r) :
    ∀ (k : Type u) [Field k] (g : Spec (.of k) ⟶ Y) {t : ℕ}
      (x : Fin t → (pullback g f : Scheme.{u})), Function.Injective x →
      (∑ i,
        letI := ((Scheme.ΓSpecIso (.of k)).inv ≫ (pullback.fst g f).appTop ≫
          (pullback g f).Γevaluation (x i)).hom.toAlgebra
        Module.finrank k ((pullback g f).residueField (x i))) ≤ n
```

**`AlgebraicGeometry.hasUniversallyBoundedFibers_of_boundsFiberDegrees`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBounded.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBounded.lean#L62). The attribute's comment: “universally\_bounded”.

> A common integer bound on the degrees of the fibres makes those fibres universally
> bounded.

```lean
public lemma hasUniversallyBoundedFibers_of_boundsFiberDegrees {X Y : Scheme.{u}} (f : X ⟶ Y)
    (n : ℤ) (h : BoundsFiberDegrees f n) : HasUniversallyBoundedFibers f
```

**`AlgebraicGeometry.boundsFiberDegrees_iff_field_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedBaseChange.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedBaseChange.lean#L100). The attribute's comment: “bounded\_degree\_iff\_field\_base\_changes”.

> An integer bounds the degrees of the fibres of a morphism of schemes exactly when each of its
> base changes to the spectrum of a field is finite locally free of a rank bounded by that
> integer.

```lean
theorem boundsFiberDegrees_iff_field_baseChange {X Y : Scheme.{u}} (f : X ⟶ Y) (n : ℤ) :
    BoundsFiberDegrees f n ↔
      ∀ (k : Type u) [Field k] (g : Spec (.of k) ⟶ Y),
        ∃ r : ℕ, (r : ℤ) ≤ n ∧
          Stacks.Morphisms.IsFiniteLocallyFreeOfRank (pullback.fst g f) r
```

**`AlgebraicGeometry.boundsFiberDegrees_iff_field_baseChange_of_nonneg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Varieties/BoundedDegree/FieldBaseChange.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Varieties/BoundedDegree/FieldBaseChange.lean#L75). The attribute's comment: “bounded\_degree\_iff\_field\_base\_changes”.

> **Stacks Project, Tag 03J5.** A nonnegative integer bounds the degrees of the fibres of a
> scheme morphism exactly when every field-valued base change is finite locally free of rank at
> most that integer.
>
> The nonnegativity hypothesis is the source's and is not used, so it is named `_hn`; the form
> without it is `AlgebraicGeometry.boundsFiberDegrees_iff_field_baseChange`, in
> `StacksFrontier.AlgebraicGeometry.Morphisms.FibreDimension.UniversallyBoundedBaseChange`.

```lean
theorem boundsFiberDegrees_iff_field_baseChange_of_nonneg
    {X Y : Scheme.{u}} (f : X ⟶ Y) (n : ℤ) (_hn : 0 ≤ n) :
    BoundsFiberDegrees f n ↔
      ∀ (k : Type u) [Field k] (g : Spec (.of k) ⟶ Y),
        ∃ r : ℕ, (r : ℤ) ≤ n ∧
          Stacks.Morphisms.IsFiniteLocallyFreeOfRank (pullback.fst g f) r
```

## Tag 0CC2, a lemma

[Tag 0CC2](https://stacks.math.columbia.edu/tag/0CC2) in the Stacks Project.

**`AlgebraicGeometry.boundsFiberDegrees_of_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedBaseChange.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedBaseChange.lean#L132).

> The degree of a finite locally free morphism bounds the degrees of all of its fibres.

```lean
theorem boundsFiberDegrees_of_isFiniteLocallyFreeOfRank {X Y : Scheme.{u}} (f : X ⟶ Y) (d : ℕ)
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d] : BoundsFiberDegrees f (d : ℤ)
```

## Tag 03J6, a lemma

[Tag 03J6](https://stacks.math.columbia.edu/tag/03J6) in the Stacks Project.

**`AlgebraicGeometry.boundsFiberDegrees_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedComposition.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedComposition.lean#L183).

> **Stacks Project, Tag 03J6.** If a nonnegative integer `n` bounds the degrees of the fibres of
> `f` and an integer `m` bounds the degrees of the fibres of `g`, then `n * m` bounds the degrees of
> the fibres of the composite `f ≫ g`.

```lean
theorem boundsFiberDegrees_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) (n m : ℤ)
    (hn : 0 ≤ n) (hf : BoundsFiberDegrees f n) (hg : BoundsFiberDegrees g m) :
    BoundsFiberDegrees (f ≫ g) (n * m)
```

**`AlgebraicGeometry.hasUniversallyBoundedFibers_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedComposition.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedComposition.lean#L221).

> **Stacks Project, Tag 03J6.** A composition of morphisms with universally bounded fibres has
> universally bounded fibres.

```lean
theorem hasUniversallyBoundedFibers_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasUniversallyBoundedFibers f) (hg : HasUniversallyBoundedFibers g) :
    HasUniversallyBoundedFibers (f ≫ g)
```

## Tag 03J7, a lemma

[Tag 03J7](https://stacks.math.columbia.edu/tag/03J7) in the Stacks Project.

**`AlgebraicGeometry.boundsFiberDegrees_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedBaseChange.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedBaseChange.lean#L60).

> Every integer bound on the degrees of the fibres of a morphism
> of schemes is preserved by arbitrary base change.

```lean
instance boundsFiberDegrees_isStableUnderBaseChange (n : ℤ) :
    MorphismProperty.IsStableUnderBaseChange
      (fun {X Y : Scheme.{u}} (f : X ⟶ Y) ↦ BoundsFiberDegrees f n)
```

## Tag 03J8, a lemma

[Tag 03J8](https://stacks.math.columbia.edu/tag/03J8) in the Stacks Project.

**`AlgebraicGeometry.boundsFiberDegrees_of_isPullback_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedSurjectiveDescent.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedSurjectiveDescent.lean#L44). The attribute's comment: “specified bound”.

> Let `f'` be a base change of `f` along a surjective morphism. An integer bounding the degrees
> of the fibres of `f'` also bounds the degrees of the fibres of `f`.

```lean
theorem boundsFiberDegrees_of_isPullback_of_surjective {X Y X' Y' : Scheme.{u}} {f : X ⟶ Y}
    {f' : X' ⟶ Y'} {g' : X' ⟶ X} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g) [Surjective g]
    (n : ℤ) (h : BoundsFiberDegrees f' n) : BoundsFiberDegrees f n
```

**`AlgebraicGeometry.hasUniversallyBoundedFibers_of_isPullback_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedSurjectiveDescent.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedSurjectiveDescent.lean#L65). The attribute's comment: “universally bounded fibres”.

> Let `f'` be a base change of `f` along a surjective morphism. If `f'` has universally bounded
> fibres, then so does `f`.

```lean
theorem hasUniversallyBoundedFibers_of_isPullback_of_surjective {X Y X' Y' : Scheme.{u}}
    {f : X ⟶ Y} {f' : X' ⟶ Y'} {g' : X' ⟶ X} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    [Surjective g] (h : HasUniversallyBoundedFibers f') : HasUniversallyBoundedFibers f
```

## Tag 03J9, a lemma

[Tag 03J9](https://stacks.math.columbia.edu/tag/03J9) in the Stacks Project.

**`AlgebraicGeometry.hasUniversallyBoundedFibers_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/ImmersionBounded.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/ImmersionBounded.lean#L46).

> An immersion of schemes has universally bounded fibres; the integer one bounds the degrees of
> its fibres.

```lean
theorem hasUniversallyBoundedFibers_of_isImmersion {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsImmersion f] : HasUniversallyBoundedFibers f
```

## Tag 03WU, a lemma

[Tag 03WU](https://stacks.math.columbia.edu/tag/03WU) in the Stacks Project.

**`AlgebraicGeometry.etale_boundsFiberDegrees_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/EtaleUniversallyBounded.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/EtaleUniversallyBounded.lean#L209).

> For an étale morphism, bounding fibre degrees, bounding the points of every field-valued base
> change, and bounding the points after passage to separable closures of residue fields are
> equivalent.

```lean
theorem etale_boundsFiberDegrees_tfae {X Y : Scheme.{u}} (f : X ⟶ Y) [Etale f] (n : ℕ) :
    List.TFAE [
      BoundsFiberDegrees f (n : ℤ),
      ∀ (k : Type u) [Field k] (g : Spec (.of k) ⟶ Y),
        Cardinal.mk (pullback g f : Scheme.{u}) ≤ n,
      ∀ (y : Y) (ksep : Type u) [Field ksep] [Algebra (Y.residueField y) ksep]
        [IsSepClosure (Y.residueField y) ksep],
        Cardinal.mk
          (pullback
            (Spec.map (CommRingCat.ofHom (algebraMap (Y.residueField y) ksep)))
            (f.fiberToSpecResidueField y) : Scheme.{u}) ≤ n]
```

## Tag 03JA, a lemma

[Tag 03JA](https://stacks.math.columbia.edu/tag/03JA) in the Stacks Project.

**`AlgebraicGeometry.hasUniversallyBoundedFibers_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/QuasiFiniteUniversallyBounded.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/QuasiFiniteUniversallyBounded.lean#L437).

> **Stacks 03JA.** A locally quasi-finite morphism of finite type whose source is quasi-compact
> has universally bounded fibres.

```lean
theorem hasUniversallyBoundedFibers_of_locallyQuasiFinite {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] [CompactSpace X] :
    HasUniversallyBoundedFibers f
```

## Tag 03JB, a lemma

[Tag 03JB](https://stacks.math.columbia.edu/tag/03JB) in the Stacks Project.

**`AlgebraicGeometry.boundsFiberDegrees_of_comp_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedFlatDescent.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedFlatDescent.lean#L130). The attribute's comment: “specified bound”.

> **Stacks Project, Tag 03JB**, the precise form. If `f` is surjective and flat, then an
> integer bounding the degrees of the fibres of `f ≫ h` also bounds the degrees of the fibres
> of `h`.

```lean
public theorem boundsFiberDegrees_of_comp_of_surjective_flat {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (h : Y ⟶ Z) [Surjective f] [Flat f] (n : ℤ)
    (hbound : BoundsFiberDegrees (f ≫ h) n) :
    BoundsFiberDegrees h n
```

**`AlgebraicGeometry.hasUniversallyBoundedFibers_of_comp_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedFlatDescent.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UniversallyBoundedFlatDescent.lean#L164). The attribute's comment: “universally bounded fibres”.

> **Stacks Project, Tag 03JB.** If `f` is surjective and flat and the fibres of `f ≫ h` are
> universally bounded, then so are the fibres of `h`.

```lean
public theorem hasUniversallyBoundedFibers_of_comp_of_surjective_flat {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (h : Y ⟶ Z) [Surjective f] [Flat f]
    (hbound : HasUniversallyBoundedFibers (f ≫ h)) :
    HasUniversallyBoundedFibers h
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.58, Tag 03J3](https://stacks.math.columbia.edu/tag/03J3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
