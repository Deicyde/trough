---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.presheafImpliesHoldsOnEveryEtaleChart_of_etale_precomp, AlgebraicGeometry.Space.holdsOnEveryEtaleChart_iff_surjectiveChart, AlgebraicGeometry.Space.holdsOnEveryEtaleChart_iff_representable, AlgebraicGeometry.Space.holdsOnEveryEtaleChart_iff_relative, AlgebraicGeometry.Space.HoldsOnEveryEtaleChart, AlgebraicGeometry.Space.holdsOnEveryEtaleChart_isStableUnderComposition, AlgebraicGeometry.Space.holdsOnEveryEtaleChart_isStableUnderBaseChange, AlgebraicGeometry.Space.holdsOnEveryEtaleChartAtPoint_iff_some
statement: formalized
proof: formalized
---

# 67.22 Types of morphisms étale local on source-and-target

Section 67.22 of the Stacks Project, [Tag 03MI](https://stacks.math.columbia.edu/tag/03MI). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03MJ, a lemma

[Tag 03MJ](https://stacks.math.columbia.edu/tag/03MJ) in the Stacks Project.

**`AlgebraicGeometry.Space.presheafImpliesHoldsOnEveryEtaleChart_of_etale_precomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBridge.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBridge.lean#L114). The attribute's comment: “condition (1) from the represented base changes”.

> **Stacks 03MJ, condition (1) from the represented base changes.** A property `P` of scheme
> morphisms which survives composition with an étale morphism in front of it holds on every étale
> chart of a morphism of presheaves all of whose represented base changes have `P`.

```lean
theorem presheafImpliesHoldsOnEveryEtaleChart_of_etale_precomp (P : MorphismProperty Scheme.{u})
    (hP : ∀ {X Y Z : Scheme.{u}} (i : X ⟶ Y) (p : Y ⟶ Z), Etale i → P p → P (i ≫ p)) :
    PresheafImpliesHoldsOnEveryEtaleChart B S hS P
```

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChart_iff_surjectiveChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocality.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocality.lean#L89). The attribute's comment: “equivalence of conditions (1) and (2)”.

> **Stacks 03MJ**, the equivalence of conditions (1) and (2). A property of morphisms of
> schemes which is étale local on the source and target holds on every commuting square of étale
> charts of a morphism of algebraic spaces exactly when it holds on one such square whose chart
> of the source is surjective.

```lean
theorem holdsOnEveryEtaleChart_iff_surjectiveChart
    (hP : IsEtaleLocalOnSourceAndTarget P)
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    HoldsOnEveryEtaleChart B S hS P f ↔ HoldsOnSurjectiveEtaleChart B S hS P f
```

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChart_iff_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocality.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocality.lean#L142). The attribute's comment: “representable source and target”.

> **Stacks 03MJ** for a morphism of representable presheaves: a property of morphisms of
> schemes which is étale local on the source and target holds on every commuting square of étale
> charts of the morphism exactly when it holds of the morphism of schemes read off the canonical
> representations of source and target.

```lean
theorem holdsOnEveryEtaleChart_iff_representable
    (hP : IsEtaleLocalOnSourceAndTarget P)
    [F.IsRepresentable] [G.IsRepresentable] (f : F ⟶ G) :
    HoldsOnEveryEtaleChart B S hS P f ↔
      P ((BigFppfOver.toScheme B S hS).map
        (yoneda.preimage (F.reprW.hom ≫ f ≫ G.reprW.inv)))
```

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChart_iff_relative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocality.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocality.lean#L188). The attribute's comment: “representable morphism”.

> **Stacks 03MJ** for a representable morphism of algebraic spaces: when `P` is in addition
> stable under base change and local on the base for the fppf topology, the every-chart condition
> is exactly the relative morphism property of the inverse image of `P`, that is, `P` holds of
> every represented base change of the morphism.

```lean
theorem holdsOnEveryEtaleChart_iff_relative
    (hP : IsEtaleLocalOnSourceAndTarget P)
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (f : F ⟶ G) (hf : yoneda.relativelyRepresentable f) :
    HoldsOnEveryEtaleChart B S hS P f ↔
      (P.inverseImage (BigFppfOver.toScheme B S hS)).presheaf f
```

## Tag 04RD, a definition

[Tag 04RD](https://stacks.math.columbia.edu/tag/04RD) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.HoldsOnEveryEtaleChart`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L200), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean#L122) (StacksFrontier).

## Tag 0AML, a remark

[Tag 0AML](https://stacks.math.columbia.edu/tag/0AML) in the Stacks Project.

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChart_isStableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartComposition.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartComposition.lean#L143).

> **Stacks 0AML.** A property of morphisms of schemes which is étale local on the source and
> target and stable under composition induces a composition stable property of morphisms of
> algebraic spaces over `S`, namely the condition that it hold on every commuting square of
> étale charts.

```lean
theorem holdsOnEveryEtaleChart_isStableUnderComposition
    (P : MorphismProperty Scheme.{u})
    (hP : IsEtaleLocalOnSourceAndTarget P)
    [P.IsStableUnderComposition] :
    MorphismProperty.IsStableUnderComposition
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        HoldsOnEveryEtaleChart B S hS P f.hom)
```

## Tag 0AMM, a remark

[Tag 0AMM](https://stacks.math.columbia.edu/tag/0AMM) in the Stacks Project.

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChart_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBaseChange.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBaseChange.lean#L249).

> A property of morphisms of schemes which is étale local on the source and
> target and stable under base change induces a base-change stable property of morphisms of
> algebraic spaces over `S`, namely the condition that it hold on every commuting square of etale
> charts.

```lean
theorem holdsOnEveryEtaleChart_isStableUnderBaseChange
    (P : MorphismProperty Scheme.{u})
    (hP : IsEtaleLocalOnSourceAndTarget P)
    [P.IsStableUnderBaseChange] :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        HoldsOnEveryEtaleChart B S hS P f.hom)
```

## Tag 04NC, a lemma

[Tag 04NC](https://stacks.math.columbia.edu/tag/04NC) in the Stacks Project.

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChartAtPoint_iff_some`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPoint.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPoint.lean#L328). The attribute's comment: “equivalence of conditions (1) and (2)”.

> **Stacks 04NC, equivalence of conditions (1) and (2).** An étale-local property of germ
> morphisms holds in every pointed chart if and only if it holds in one pointed chart.

```lean
theorem holdsOnEveryEtaleChartAtPoint_iff_some
    (Q : ∀ {X Y : GermOfScheme.{u}}, MorphismOfGerms X Y → Prop)
    (hQ : MorphismOfGerms.IsEtaleLocalOnSourceAndTarget Q)
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (f : F ⟶ G) (x : points B S hS F) :
    HoldsOnEveryEtaleChartAtPoint B S hS Q f x ↔
      HoldsOnSomeEtaleChartAtPoint B S hS Q f x
```

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChartAtPoint_iff_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPoint.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPoint.lean#L431). The attribute's comment: “representable source and target”.

> **Stacks 04NC, representable source and target.** For representable algebraic spaces the
> chart condition is the property of the induced morphism of scheme germs at the corresponding
> scheme point.

```lean
theorem holdsOnEveryEtaleChartAtPoint_iff_representable
    (Q : ∀ {X Y : GermOfScheme.{u}}, MorphismOfGerms X Y → Prop)
    (hQ : MorphismOfGerms.IsEtaleLocalOnSourceAndTarget Q)
    [F.IsRepresentable] [G.IsRepresentable] (f : F ⟶ G) (x : points B S hS F)
    (p : FieldValuedPoint B S hS (yoneda.obj F.reprX)) (t : Spec (.of p.carrier))
    (hx : pointsMap B S hS (yoneda.obj F.reprX) F.reprW.hom
      (p.class B S hS (yoneda.obj F.reprX)) = x) :
    HoldsOnEveryEtaleChartAtPoint B S hS Q f x ↔
      Q (MorphismOfGerms.ofSchemeHom
        ((BigFppfOver.toScheme B S hS).map
          (yoneda.preimage (F.reprW.hom ≫ f ≫ G.reprW.inv)))
        (((BigFppfOver.toScheme B S hS).map p.value) t))
```

## Tag 04RE, a definition

[Tag 04RE](https://stacks.math.columbia.edu/tag/04RE) in the Stacks Project.

**`AlgebraicGeometry.Space.HoldsOnEveryEtaleChartAtPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPoint.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPoint.lean#L129).

> **Stacks 04RE.** The property holds in every pair of étale charts at the point. For a
> property of morphisms of germs of schemes which is étale local on the source-and-target this
> is the definition of a morphism of algebraic spaces *having that property at a point*: by
> `AlgebraicGeometry.Space.holdsOnEveryEtaleChartAtPoint_iff_some` it is equivalent to the
> some-chart condition, which is the equivalence the definition invokes.

```lean
abbrev HoldsOnEveryEtaleChartAtPoint
    (Q : ∀ {X Y : GermOfScheme.{u}}, MorphismOfGerms X Y → Prop)
    (f : F ⟶ G) (x : points B S hS F) : Prop
```

## Tag 04RF, a lemma

[Tag 04RF](https://stacks.math.columbia.edu/tag/04RF) in the Stacks Project.

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChartAtPoint_iff_exists_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPointOpen.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPointOpen.lean#L490). The attribute's comment: “part (2)”.

> A morphism has the germ property at a point exactly when it has the
> corresponding scheme-morphism property on an open neighbourhood of that point.

```lean
theorem holdsOnEveryEtaleChartAtPoint_iff_exists_open
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty Scheme.{u})
    (hP : AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget P)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (x : points B S hS X) :
    HoldsOnEveryEtaleChartAtPoint B S hS
      (MorphismOfGerms.HasRepresentativeWithProperty P) f x ↔
      ∃ (U : Subfunctor X), IsOpenSubspace B S hS U ∧
        x ∈ Set.range (pointsMap B S hS U.toFunctor U.ι) ∧
          HoldsOnEveryEtaleChart B S hS P (U.ι ≫ f)
```

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChart_iff_forall_atPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPointOpen.lean, line 658](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPointOpen.lean#L658). The attribute's comment: “part (3)”.

> A morphism of algebraic spaces has an étale-local property if and only if
> its germ has the associated property at every source point.

```lean
theorem holdsOnEveryEtaleChart_iff_forall_atPoint
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty Scheme.{u})
    (hP : AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget P)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    HoldsOnEveryEtaleChart B S hS P f ↔
      ∀ x : points B S hS X,
        HoldsOnEveryEtaleChartAtPoint B S hS
          (MorphismOfGerms.HasRepresentativeWithProperty P) f x
```

Declarations registered for the tag:

- [`MorphismOfGerms.hasRepresentativeWithProperty_isEtaleLocalOnSourceAndTarget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismOfGerms.hasRepresentativeWithProperty_isEtaleLocalOnSourceAndTarget#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPointOpen.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartAtPointOpen.lean#L485) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.22, Tag 03MI](https://stacks.math.columbia.edu/tag/03MI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
