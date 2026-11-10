---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleAt_of_unramifiedAt_of_specializes_genericPoint, AlgebraicGeometry.etale_of_unramified_of_dominant_component, AlgebraicGeometry.irreducibleSpace_of_unramified_of_dominant_component, AlgebraicGeometry.etaleAt_left_of_comp_etaleAt_of_specializes_genericPoint, AlgebraicGeometry.etaleAt_right_of_comp_etaleAt_of_specializes_genericPoint, AlgebraicGeometry.etale_left_of_comp_etale_of_dominant_components, AlgebraicGeometry.etaleAt_right_of_comp_etale_of_dominant_components
statement: formalized
proof: formalized
---

# 37.37 Unramified and étale morphisms

Section 37.37 of the Stacks Project, [Tag 0GS7](https://stacks.math.columbia.edu/tag/0GS7). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GS8, a lemma

[Tag 0GS8](https://stacks.math.columbia.edu/tag/0GS8) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_of_unramifiedAt_of_specializes_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Unibranch.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/Unibranch.lean#L41). References: EGA IV (18.10.1), “suff.; generic pt in”.

> Let `f : X ⟶ Y` be locally of finite type with `Y` integral,
> and let `x : X` be a point whose image is a point where `Y` is geometrically unibranch. If `f`
> is unramified at `x` and `x` is a specialization of a point lying over the generic point of `Y`,
> then `f` is étale at `x`.

```lean
theorem etaleAt_of_unramifiedAt_of_specializes_genericPoint
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegral Y] [LocallyOfFiniteType f] {x x' : X}
    (hy : IsGeometricallyUnibranchAt Y (f x))
    (hxx' : x' ⤳ x) (hx' : f x' = genericPoint Y)
    (hunramified : UnramifiedAt f x) :
    EtaleAt f x
```

## Tag 0GS9, a lemma

[Tag 0GS9](https://stacks.math.columbia.edu/tag/0GS9) in the Stacks Project.

**`AlgebraicGeometry.etale_of_unramified_of_dominant_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchConnected.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchConnected.lean#L156). The attribute's comment: “etaleness”. References: EGA IV (18.10.3), “f étale”; SGA 1 I (9.11), “f étale”.

> An unramified morphism from a connected scheme to an integral geometrically unibranch scheme
> is étale as soon as one irreducible component of its source dominates the target.

```lean
theorem etale_of_unramified_of_dominant_component
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegral Y] [Unramified f] [ConnectedSpace X]
    (hY : IsGeometricallyUnibranch Y)
    (hdom : ∃ Z : irreducibleComponents X, closure (f '' (Z : Set X)) = Set.univ) :
    Etale f
```

**`AlgebraicGeometry.irreducibleSpace_of_unramified_of_dominant_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchConnected.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchConnected.lean#L169). The attribute's comment: “irreducibility”. References: EGA IV (18.10.3), “X irreducible”; SGA 1 I (9.11), “X irreducible”.

> The source of an unramified morphism from a connected scheme to an integral geometrically
> unibranch scheme is irreducible as soon as one of its irreducible components dominates the
> target.

```lean
theorem irreducibleSpace_of_unramified_of_dominant_component
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegral Y] [Unramified f] [ConnectedSpace X]
    (hY : IsGeometricallyUnibranch Y)
    (hdom : ∃ Z : irreducibleComponents X, closure (f '' (Z : Set X)) = Set.univ) :
    IrreducibleSpace X
```

## Tag 0GSA, a lemma

[Tag 0GSA](https://stacks.math.columbia.edu/tag/0GSA) in the Stacks Project.

**`AlgebraicGeometry.etaleAt_left_of_comp_etaleAt_of_specializes_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean#L51). The attribute's comment: “first factor”.

> If a composite `f ≫ g` is étale at `x`, the intermediate scheme is integral and
> geometrically unibranch at `f x`, and `x` is a specialization of a point whose image under `f` is
> the generic point, then `f` is étale at `x`.

```lean
theorem etaleAt_left_of_comp_etaleAt_of_specializes_genericPoint
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) [IsIntegral Y] {x x' : X}
    (hy : IsGeometricallyUnibranchAt Y (f x)) (hcomp : EtaleAt (f ≫ g) x)
    (hxx' : x' ⤳ x) (hx' : f x' = genericPoint Y) :
    EtaleAt f x
```

**`AlgebraicGeometry.etaleAt_right_of_comp_etaleAt_of_specializes_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean#L79). The attribute's comment: “second factor”.

> Under the hypotheses of
> `AlgebraicGeometry.etaleAt_left_of_comp_etaleAt_of_specializes_genericPoint`, the second factor
> is étale at the image of `x`.

```lean
theorem etaleAt_right_of_comp_etaleAt_of_specializes_genericPoint
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) [IsIntegral Y] {x x' : X}
    (hy : IsGeometricallyUnibranchAt Y (f x)) (hcomp : EtaleAt (f ≫ g) x)
    (hxx' : x' ⤳ x) (hx' : f x' = genericPoint Y) :
    EtaleAt g (f x)
```

## Tag 0GSB, a lemma

[Tag 0GSB](https://stacks.math.columbia.edu/tag/0GSB) in the Stacks Project.

**`AlgebraicGeometry.etale_left_of_comp_etale_of_dominant_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean#L133). The attribute's comment: “first factor”.

> If a composite `f ≫ g` is étale, the intermediate scheme is integral and geometrically
> unibranch, and every irreducible component of the source dominates it, then `f` is étale.

```lean
theorem etale_left_of_comp_etale_of_dominant_components
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) [IsIntegral Y]
    (hY : IsGeometricallyUnibranch Y) (hcomp : Etale (f ≫ g))
    (hdom : ∀ C : irreducibleComponents X, closure (f '' (C : Set X)) = Set.univ) :
    Etale f
```

**`AlgebraicGeometry.etaleAt_right_of_comp_etale_of_dominant_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/UnibranchComposition.lean#L148). The attribute's comment: “second factor”.

> Under the hypotheses of
> `AlgebraicGeometry.etale_left_of_comp_etale_of_dominant_components`, the second factor is étale
> at every point in the image of the first.

```lean
theorem etaleAt_right_of_comp_etale_of_dominant_components
    {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z) [IsIntegral Y]
    (hY : IsGeometricallyUnibranch Y) (hcomp : Etale (f ≫ g))
    (hdom : ∀ C : irreducibleComponents X, closure (f '' (C : Set X)) = Set.univ) :
    ∀ y ∈ Set.range f, EtaleAt g y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.37, Tag 0GS7](https://stacks.math.columbia.edu/tag/0GS7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
