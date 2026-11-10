---
declaration: section
origin: cited
lean: AlgebraicGeometry.bigAffineEtale_hasConservativeFamily, AlgebraicGeometry.bigAffineFppf_hasConservativeFamily, AlgebraicGeometry.bigAffineSmooth_hasConservativeFamily, AlgebraicGeometry.bigEtale_hasConservativeFamily, AlgebraicGeometry.bigFppf_hasConservativeFamily, AlgebraicGeometry.bigSmooth_hasConservativeFamily, AlgebraicGeometry.bigAffineSyntomic_hasConservativeFamily, AlgebraicGeometry.bigSyntomic_hasConservativeFamily
statement: formalized
proof: formalized
---

# 59.30 Points in other topologies

Section 59.30 of the Stacks Project, [Tag 06VW](https://stacks.math.columbia.edu/tag/06VW). 1 tag here is carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06VX, a lemma

[Tag 06VX](https://stacks.math.columbia.edu/tag/06VX) in the Stacks Project.

**`AlgebraicGeometry.bigAffineEtale_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigAffineEtale.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigAffineEtale.lean#L46). The attribute's comment: “big\_affine\_etale”.

> **Stacks 06VX, big affine étale case.** The big affine étale site over a
> scheme has enough points.

```lean
public theorem bigAffineEtale_hasConservativeFamily
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    GrothendieckTopology.HasConservativeFamily.{u + 1}
      (AlgebraicGeometry.BigAffineEtale.topology B S hS)
```

**`AlgebraicGeometry.bigAffineFppf_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigAffineFppf.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigAffineFppf.lean#L42). The attribute's comment: “big\_affine\_fppf”.

> **Stacks 06VX, big affine fppf case.** The big affine fppf site over a
> scheme has enough points.

```lean
public theorem bigAffineFppf_hasConservativeFamily
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (AlgebraicGeometry.BigAffineFppf.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.bigAffineSmooth_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigAffineSmooth.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigAffineSmooth.lean#L96). The attribute's comment: “big\_affine\_smooth”.

> **Stacks 06VX, big affine smooth case.** The big affine smooth site over
> `S` has enough points.

```lean
public theorem bigAffineSmooth_hasConservativeFamily
    (B : AlgebraicGeometry.BigSmoothSite.{u}) (S : Scheme.{u})
    (hS : S.size < B.cutoff) :
    (AlgebraicGeometry.BigAffineSmooth.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.bigEtale_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigEtale.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigEtale.lean#L42). The attribute's comment: “big\_etale”.

> **Stacks 06VX, big étale case.** The big étale site over a scheme has
> enough points.

```lean
public theorem bigEtale_hasConservativeFamily
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    GrothendieckTopology.HasConservativeFamily.{u + 1}
      (AlgebraicGeometry.BigEtaleOver.topology B S hS)
```

**`AlgebraicGeometry.bigFppf_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigFppf.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigFppf.lean#L41). The attribute's comment: “big\_fppf”.

> **Stacks 06VX, big fppf case.** The big fppf site over a scheme has
> enough points.

```lean
public theorem bigFppf_hasConservativeFamily
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (AlgebraicGeometry.BigFppfOver.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.bigSmooth_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigSmooth.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigSmooth.lean#L42). The attribute's comment: “big\_smooth”.

> **Stacks 06VX, big smooth case.** The big smooth site over `S` has enough
> points.

```lean
public theorem bigSmooth_hasConservativeFamily
    (B : AlgebraicGeometry.BigSmoothSite.{u}) (S : Scheme.{u})
    (hS : S.size < B.cutoff) :
    (AlgebraicGeometry.BigSmoothOver.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.bigAffineSyntomic_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigSyntomic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigSyntomic.lean#L46). The attribute's comment: “big\_affine\_syntomic”.

> **Stacks 06VX, big affine syntomic case.** The big affine syntomic site over a scheme has
> enough points.

```lean
public theorem bigAffineSyntomic_hasConservativeFamily
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (BigAffineSyntomic.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.bigSyntomic_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigSyntomic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigSyntomic.lean#L57). The attribute's comment: “big\_syntomic”.

> **Stacks 06VX, big syntomic case.** The big syntomic site over a scheme has enough
> points.

```lean
public theorem bigSyntomic_hasConservativeFamily
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (BigSyntomicOver.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.bigAffineZariski_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigZariski.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigZariski.lean#L46). The attribute's comment: “big\_affine\_zariski”.

> **Stacks 06VX, big affine Zariski case.** The big affine Zariski site over a scheme has
> enough points.

```lean
public theorem bigAffineZariski_hasConservativeFamily
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (BigAffineZariski.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.bigZariski_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigZariski.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/BigZariski.lean#L57). The attribute's comment: “big\_zariski”.

> **Stacks 06VX, big Zariski case.** The big Zariski site over a scheme has enough
> points.

```lean
public theorem bigZariski_hasConservativeFamily
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (BigZariskiOver.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.smallAffineEtale_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallAffineEtale.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallAffineEtale.lean#L193). The attribute's comment: “small\_affine\_etale”.

> **Stacks 06VX, small affine étale case.** The small affine étale site of a
> scheme has enough points.

```lean
public theorem smallAffineEtale_hasConservativeFamily
    (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    GrothendieckTopology.HasConservativeFamily.{u}
      (AlgebraicGeometry.SmallAffineEtale.topology B S hS)
```

**`AlgebraicGeometry.SmallEtale.hasConservativeFamily`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallEtale.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallEtale.lean#L414). The attribute's comment: “small\_etale”.

> The small étale site of a scheme has enough points.

```lean
public lemma hasConservativeFamily (B : AlgebraicGeometry.BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    (AlgebraicGeometry.SmallEtale.topology B S hS).HasConservativeFamily.{u}
```

**`AlgebraicGeometry.smallAffineZariski_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallZariski.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallZariski.lean#L51). The attribute's comment: “small\_affine\_zariski”.

> **Stacks 06VX, small affine Zariski case.** The small affine Zariski site of a scheme has
> enough points.

```lean
public theorem smallAffineZariski_hasConservativeFamily
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (SmallAffineZariski.topology B S hS).HasConservativeFamily.{u + 1}
```

**`AlgebraicGeometry.smallZariski_hasConservativeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallZariski.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointsOtherTopologies/SmallZariski.lean#L62). The attribute's comment: “small\_zariski”.

> **Stacks 06VX, small Zariski case.** The small Zariski site of a scheme has enough
> points.

```lean
public theorem smallZariski_hasConservativeFamily
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (SmallZariski.topology B S hS).HasConservativeFamily.{u + 1}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.30, Tag 06VW](https://stacks.math.columbia.edu/tag/06VW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
