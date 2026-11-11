---
declaration: section
origin: cited
lean: CategoryTheory.MorphismProperty.IsLocalAtSource, AlgebraicGeometry.Space.comp_isFlat, AlgebraicGeometry.Space.comp_isFlat_isLocallyOfFinitePresentation, AlgebraicGeometry.Space.comp_isSyntomic, AlgebraicGeometry.Space.comp_isSmooth, AlgebraicGeometry.Space.comp_isEtale, AlgebraicGeometry.Space.Topology.isLocalAtSource_holdsOnEveryEtaleChart
statement: formalized
proof: formalized
---

# 74.14 Properties of morphisms local on the source

Section 74.14 of the Stacks Project, [Tag 06EN](https://stacks.math.columbia.edu/tag/06EN). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06EP, a definition

[Tag 06EP](https://stacks.math.columbia.edu/tag/06EP) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsLocalAtSource`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsLocalAtSource#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Coverings.lean#L420) (StacksFrontier). References: SGA 4 IV (8.5.4).

## Tag 06EQ, a lemma

[Tag 06EQ](https://stacks.math.columbia.edu/tag/06EQ) in the Stacks Project.

**`AlgebraicGeometry.Space.comp_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean#L164). The attribute's comment: “fpqc”.

> **Stacks 06EQ**, the fpqc case. A property fpqc local on the source is stable under
> precomposition with a flat morphism.

```lean
theorem comp_isFlat [P.IsLocalAtSource (Topology.precoverage.{u, v} .fpqc B S hS)]
    {X Y Z : AlgebraicSpaces B S hS} (a : X ⟶ Y) (f : Y ⟶ Z)
    (ha : IsFlat B S hS a.hom) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.Space.comp_isFlat_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean#L172). The attribute's comment: “fppf”.

> **Stacks 06EQ**, the fppf case. A property fppf local on the source is stable under
> precomposition with a flat morphism which is locally of finite presentation.

```lean
theorem comp_isFlat_isLocallyOfFinitePresentation
    [P.IsLocalAtSource (Topology.precoverage.{u, v} .fppf B S hS)]
    {X Y Z : AlgebraicSpaces B S hS} (a : X ⟶ Y) (f : Y ⟶ Z)
    (hflat : IsFlat B S hS a.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS a.hom) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.Space.comp_isSyntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean#L182). The attribute's comment: “syntomic”.

> **Stacks 06EQ**, the syntomic case. A property syntomic local on the source is stable under
> precomposition with a syntomic morphism.

```lean
theorem comp_isSyntomic [P.IsLocalAtSource (Topology.precoverage.{u, v} .syntomic B S hS)]
    {X Y Z : AlgebraicSpaces B S hS} (a : X ⟶ Y) (f : Y ⟶ Z)
    (ha : IsSyntomic B S hS a.hom) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.Space.comp_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean#L190). The attribute's comment: “smooth”.

> **Stacks 06EQ**, the smooth case. A property smooth local on the source is stable under
> precomposition with a smooth morphism.

```lean
theorem comp_isSmooth [P.IsLocalAtSource (Topology.precoverage.{u, v} .smooth B S hS)]
    {X Y Z : AlgebraicSpaces B S hS} (a : X ⟶ Y) (f : Y ⟶ Z)
    (ha : IsSmooth B S hS a.hom) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.Space.comp_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Precomposition.lean#L198). The attribute's comment: “étale”.

> **Stacks 06EQ**, the étale case. A property étale local on the source is stable under
> precomposition with an étale morphism.

```lean
theorem comp_isEtale [P.IsLocalAtSource (Topology.precoverage.{u, v} .etale B S hS)]
    {X Y Z : AlgebraicSpaces B S hS} (a : X ⟶ Y) (f : Y ⟶ Z)
    (ha : IsEtale B S hS a.hom) (hf : P f) : P (a ≫ f)
```

## Tag 06ER, a lemma

[Tag 06ER](https://stacks.math.columbia.edu/tag/06ER) in the Stacks Project.

**`AlgebraicGeometry.Space.Topology.isLocalAtSource_holdsOnEveryEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/PropertyLocalOnSource.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/PropertyLocalOnSource.lean#L126).

> **Stacks 06ER.** Let `P` be a property of morphisms of schemes over `S` which is étale local
> on the source and target, and let `τ` be one of the five topologies of Stacks 03YH. If `P` is
> local on the source for the counterpart of `τ` on schemes, then the associated property of
> morphisms of algebraic spaces over `S` of Stacks 03MJ is local on the source for `τ`.

```lean
theorem Topology.isLocalAtSource_holdsOnEveryEtaleChart (τ : Topology)
    (P : MorphismProperty Scheme.{u}) (hP : IsEtaleLocalOnSourceAndTarget P)
    (hlocal : P.IsLocalAtSource τ.schemePrecoverage) :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        HoldsOnEveryEtaleChart B S hS P f.hom)
      (Topology.precoverage.{u, v} τ B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.14, Tag 06EN](https://stacks.math.columbia.edu/tag/06EN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
