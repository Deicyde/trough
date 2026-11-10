---
declaration: section
origin: cited
lean: AlgebraicGeometry.GermOfScheme.IsEtaleLocal, AlgebraicGeometry.GermOfScheme.IsSmoothLocal, AlgebraicGeometry.topologicalKrullDimAt_eq_of_etale, AlgebraicGeometry.ringKrullDim_stalk_eq_of_etale, AlgebraicGeometry.isRegularLocalRing_stalk_iff_of_etale
statement: formalized
proof: formalized
---

# 35.21 Local properties of germs

Section 35.21 of the Stacks Project, [Tag 04QT](https://stacks.math.columbia.edu/tag/04QT). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04N1, a definition

[Tag 04N1](https://stacks.math.columbia.edu/tag/04N1) in the Stacks Project.

**`AlgebraicGeometry.GermOfScheme.IsEtaleLocal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Local.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germ/Local.lean#L52). The attribute's comment: “etale”.

> A property of germs is étale local if it has the same truth value at the source and target
> of every étale morphism of germs.

```lean
abbrev GermOfScheme.IsEtaleLocal (P : GermOfScheme.{u} → Prop) : Prop
```

**`AlgebraicGeometry.GermOfScheme.IsSmoothLocal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Local.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germ/Local.lean#L59). The attribute's comment: “smooth”.

> A property of germs is smooth local if it has the same truth value at the source and
> target of every smooth morphism of germs.

```lean
abbrev GermOfScheme.IsSmoothLocal (P : GermOfScheme.{u} → Prop) : Prop
```

## Tag 04N4, a lemma

[Tag 04N4](https://stacks.math.columbia.edu/tag/04N4) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_eq_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleLocalDimension.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleLocalDimension.lean#L149).

> **Stacks Project, Tag 04N4.** An étale morphism preserves the local Krull dimension at
> corresponding points.

```lean
theorem topologicalKrullDimAt_eq_of_etale
    {U V : Scheme.{u}} (f : U ⟶ V) [Etale f] (u : U) :
    topologicalKrullDimAt U u = topologicalKrullDimAt V (f u)
```

## Tag 04N8, a lemma

[Tag 04N8](https://stacks.math.columbia.edu/tag/04N8) in the Stacks Project.

**`AlgebraicGeometry.ringKrullDim_stalk_eq_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleStalkDimension.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/EtaleStalkDimension.lean#L43). References: EGA IV (17.6.4).

> **Stacks Project, Tag 04N8.** An étale morphism preserves the Krull dimension of local
> rings at corresponding points.

```lean
theorem ringKrullDim_stalk_eq_of_etale {U V : Scheme.{u}} (f : U ⟶ V) [Etale f] (u : U) :
    ringKrullDim (U.presheaf.stalk u) = ringKrullDim (V.presheaf.stalk (f u))
```

## Tag 0AH7, a lemma

[Tag 0AH7](https://stacks.math.columbia.edu/tag/0AH7) in the Stacks Project.

**`AlgebraicGeometry.isRegularLocalRing_stalk_iff_of_etale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/RegularGerm.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/RegularGerm.lean#L48).

> **Stacks Project, Tag 0AH7.** For an étale morphism of schemes, the local ring at a
> point of the source is regular if and only if the local ring at its image is regular.

```lean
lemma isRegularLocalRing_stalk_iff_of_etale {U V : Scheme.{u}} (f : U ⟶ V) [Etale f] (u : U) :
    IsRegularLocalRing (U.presheaf.stalk u) ↔
      IsRegularLocalRing (V.presheaf.stalk (f u))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.21, Tag 04QT](https://stacks.math.columbia.edu/tag/04QT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
