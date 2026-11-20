---
declaration: section
origin: cited
lean: AlgebraicGeometry.FlatnessSituation.exists_closedUniversalFlattening_of_isArtinianRing, AlgebraicGeometry.FlatnessSituation.hasFlatteningStratification_of_isArtinianRing
statement: formalized
proof: formalized
---

# 38.22 Flattening stratification over an Artinian ring

Section 38.22 of the Stacks Project, [Tag 05PA](https://stacks.math.columbia.edu/tag/05PA). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 05PB, a lemma

[Tag 05PB](https://stacks.math.columbia.edu/tag/05PB) in the Stacks Project.

**`AlgebraicGeometry.FlatnessSituation.exists_closedUniversalFlattening_of_isArtinianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Artinian.lean, line 236](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Artinian.lean#L236). The attribute's comment: “the closed universal flattening”. References: SGA 6 XII (4.5), “special case”.

> **Stacks Project, Tag 05PB.** A quasi-coherent module on a scheme over the spectrum of an
> Artinian ring admits a universal flattening, and the representing morphism is a closed
> immersion.

```lean
public theorem exists_closedUniversalFlattening_of_isArtinianRing {R : Type u} [CommRing R]
    [IsArtinianRing R] (D : FlatnessSituation.{u}) (hS : D.S = Spec (.of R)) :
    ∃ W : Over D.S, IsClosedImmersion W.hom ∧ Nonempty (D.flatFunctor.RepresentableBy W)
```

**`AlgebraicGeometry.FlatnessSituation.hasFlatteningStratification_of_isArtinianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Artinian.lean, line 270](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Artinian.lean#L270). The attribute's comment: “the flattening stratification”. References: SGA 6 XII (4.5), “special case”.

> **Stacks Project, Tag 05PB.** A quasi-coherent module on a scheme over the spectrum of an
> Artinian ring has a flattening stratification.

```lean
public theorem hasFlatteningStratification_of_isArtinianRing {R : Type u} [CommRing R]
    [IsArtinianRing R] (D : FlatnessSituation.{u}) (hS : D.S = Spec (.of R)) :
    D.HasFlatteningStratification
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.22, Tag 05PA](https://stacks.math.columbia.edu/tag/05PA)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
