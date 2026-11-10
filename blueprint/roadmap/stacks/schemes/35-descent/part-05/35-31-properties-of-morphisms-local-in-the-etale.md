---
declaration: section
origin: cited
lean: AlgebraicGeometry.etale_isLocalAtSource, AlgebraicGeometry.locallyQuasiFinite_isLocalAtSource_etale, AlgebraicGeometry.unramified_isLocalAtSource, AlgebraicGeometry.gUnramified_isLocalAtSource_etale
statement: formalized
proof: formalized
---

# 35.31 Properties of morphisms local in the étale topology on the source

Section 35.31 of the Stacks Project, [Tag 036V](https://stacks.math.columbia.edu/tag/036V). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 036W, a lemma

[Tag 036W](https://stacks.math.columbia.edu/tag/036W) in the Stacks Project.

**`AlgebraicGeometry.etale_isLocalAtSource`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Etale.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Etale.lean#L62).

> **Stacks Project, Tag 036W.** Being an étale morphism of schemes is local on the source for
> the étale topology.

```lean
instance etale_isLocalAtSource :
    MorphismProperty.IsLocalAtSource (@Etale.{u}) Scheme.etalePrecoverage
```

## Tag 03X4, a lemma

[Tag 03X4](https://stacks.math.columbia.edu/tag/03X4) in the Stacks Project.

**`AlgebraicGeometry.locallyQuasiFinite_isLocalAtSource_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Etale.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Etale.lean#L82).

> **Stacks Project, Tag 03X4.** Being locally quasi-finite is local on the source for the
> étale topology.

```lean
instance locallyQuasiFinite_isLocalAtSource_etale :
    MorphismProperty.IsLocalAtSource
      ((@LocallyOfFiniteType.{u} ⊓ @LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      Scheme.etalePrecoverage
```

## Tag 03YV, a lemma

[Tag 03YV](https://stacks.math.columbia.edu/tag/03YV) in the Stacks Project.

**`AlgebraicGeometry.unramified_isLocalAtSource`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Unramified.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Unramified.lean#L94). The attribute's comment: “unramified”.

> **Stacks Project, Tag 03YV, unramified case.** Unramifiedness of morphisms of schemes is
> local on the source for the étale topology.

```lean
instance unramified_isLocalAtSource :
    MorphismProperty.IsLocalAtSource (@Unramified.{u}) Scheme.etalePrecoverage
```

**`AlgebraicGeometry.gUnramified_isLocalAtSource_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Unramified.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Unramified.lean#L126). The attribute's comment: “g\_unramified”. References: SGA 4 IV (8.5.5), “special case”.

> **Stacks Project, Tag 03YV, G-unramified case.** G-unramifiedness of morphisms of schemes
> is local on the source for the étale topology.

```lean
instance gUnramified_isLocalAtSource_etale :
    MorphismProperty.IsLocalAtSource (@GUnramified.{u}) Scheme.etalePrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.31, Tag 036V](https://stacks.math.columbia.edu/tag/036V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
