---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEtale_isLocalAtSource_etale, AlgebraicGeometry.Space.isLocallyQuasiFinite_isLocalAtSource_etale, AlgebraicGeometry.Space.unramified_isLocalAtSource_etale
statement: formalized
proof: formalized
---

# 74.19 Properties of morphisms local in the étale topology on the source

Section 74.19 of the Stacks Project, [Tag 06F3](https://stacks.math.columbia.edu/tag/06F3). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06F4, a lemma

[Tag 06F4](https://stacks.math.columbia.edu/tag/06F4) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_isLocalAtSource_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Etale.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Etale.lean#L73).

> **Stacks 06F4.** Étaleness of a morphism of algebraic spaces over `S` is local on the
> source for the étale topology.

```lean
instance isEtale_isLocalAtSource_etale :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsEtale B S hS f.hom)
      (Topology.etale.precoverage.{u, v} B S hS)
```

## Tag 06F5, a lemma

[Tag 06F5](https://stacks.math.columbia.edu/tag/06F5) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_isLocalAtSource_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Etale.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Etale.lean#L92).

> **Stacks 06F5.** Local quasi-finiteness of a morphism of algebraic spaces over `S` is local
> on the source for the étale topology.

```lean
instance isLocallyQuasiFinite_isLocalAtSource_etale :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsLocallyQuasiFinite B S hS f.hom)
      (Topology.etale.precoverage.{u, v} B S hS)
```

## Tag 06F6, a lemma

[Tag 06F6](https://stacks.math.columbia.edu/tag/06F6) in the Stacks Project.

**`AlgebraicGeometry.Space.unramified_isLocalAtSource_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSourceLocalityTransfer.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSourceLocalityTransfer.lean#L153).

> **Stacks 06F6.** Unramifiedness of a morphism of algebraic spaces over `S` is local on the
> source for the étale topology of Stacks 03YH.
>
> Unramifiedness of morphisms of schemes is étale local on the source and target
> ([Stacks Project, Tag 04R3]) and local on the source for the étale topology of schemes
> ([Stacks Project, Tag 03YV]), so this is the instance of
> `AlgebraicGeometry.Space.isLocalAtSource_etale_of_schemes` at that property.

```lean
instance unramified_isLocalAtSource_etale :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsUnramified B S hS f.hom)
      (Topology.precoverage.{u, v} .etale B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.19, Tag 06F3](https://stacks.math.columbia.edu/tag/06F3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
