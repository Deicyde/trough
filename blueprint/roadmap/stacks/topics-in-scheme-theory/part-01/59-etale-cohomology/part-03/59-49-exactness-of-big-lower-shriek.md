---
declaration: section
origin: cited
lean: AlgebraicGeometry.bigZariskiLowerShriek_preservesFiniteLimits, AlgebraicGeometry.bigZariskiLowerShriek_preservesFiniteColimits, AlgebraicGeometry.bigEtaleLowerShriek_preservesFiniteLimits, AlgebraicGeometry.bigEtaleLowerShriek_preservesFiniteColimits, AlgebraicGeometry.bigFppfLowerShriek_preservesFiniteLimits, AlgebraicGeometry.bigFppfLowerShriek_preservesFiniteColimits, AlgebraicGeometry.bigSmoothLowerShriek_preservesFiniteLimits, AlgebraicGeometry.bigSmoothLowerShriek_preservesFiniteColimits
statement: formalized
proof: formalized
---

# 59.49 Exactness of big lower shriek

Section 59.49 of the Stacks Project, [Tag 04CB](https://stacks.math.columbia.edu/tag/04CB). 2 tags here are carried by 38 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04CC, a lemma

[Tag 04CC](https://stacks.math.columbia.edu/tag/04CC) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiLowerShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L99). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), Zariski case.** Lower shriek on big Zariski abelian sheaves preserves
> finite limits.

```lean
public theorem bigZariskiLowerShriek_preservesFiniteLimits
    (B : BigZariskiSite.{u}) (T S : B.Schemes) (f : T ⟶ S) :
    PreservesFiniteLimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigZariskiOver.topology B T.1 T.property)
      (BigZariskiOver.topology B S.1 S.property))
```

**`AlgebraicGeometry.bigZariskiLowerShriek_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L109). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), Zariski case.** Lower shriek on big Zariski abelian sheaves preserves
> finite colimits.

```lean
public theorem bigZariskiLowerShriek_preservesFiniteColimits
    (B : BigZariskiSite.{u}) (T S : B.Schemes) (f : T ⟶ S) :
    PreservesFiniteColimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigZariskiOver.topology B T.1 T.property)
      (BigZariskiOver.topology B S.1 S.property))
```

**`AlgebraicGeometry.bigEtaleLowerShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L119). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), étale case.** Lower shriek on big étale abelian sheaves preserves
> finite limits.

```lean
public theorem bigEtaleLowerShriek_preservesFiniteLimits
    (B : BigEtaleSite.{u}) (T S : B.Scheme) (f : T ⟶ S) :
    PreservesFiniteLimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigEtaleOver.topology B T.obj T.property)
      (BigEtaleOver.topology B S.obj S.property))
```

**`AlgebraicGeometry.bigEtaleLowerShriek_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L129). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), étale case.** Lower shriek on big étale abelian sheaves preserves
> finite colimits.

```lean
public theorem bigEtaleLowerShriek_preservesFiniteColimits
    (B : BigEtaleSite.{u}) (T S : B.Scheme) (f : T ⟶ S) :
    PreservesFiniteColimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigEtaleOver.topology B T.obj T.property)
      (BigEtaleOver.topology B S.obj S.property))
```

**`AlgebraicGeometry.bigFppfLowerShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L139). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), fppf case.** Lower shriek on big fppf abelian sheaves preserves
> finite limits.

```lean
public theorem bigFppfLowerShriek_preservesFiniteLimits
    (B : BigFppfSite.{u}) (T S : B.Schemes) (f : T ⟶ S) :
    PreservesFiniteLimits ((Over.map f).sheafPullback Ab.{u + 1}
      (B.topology.over T) (B.topology.over S))
```

**`AlgebraicGeometry.bigFppfLowerShriek_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L148). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), fppf case.** Lower shriek on big fppf abelian sheaves preserves
> finite colimits.

```lean
public theorem bigFppfLowerShriek_preservesFiniteColimits
    (B : BigFppfSite.{u}) (T S : B.Schemes) (f : T ⟶ S) :
    PreservesFiniteColimits ((Over.map f).sheafPullback Ab.{u + 1}
      (B.topology.over T) (B.topology.over S))
```

**`AlgebraicGeometry.bigSmoothLowerShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L157). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), smooth case.** Lower shriek on big smooth abelian sheaves preserves
> finite limits.

```lean
public theorem bigSmoothLowerShriek_preservesFiniteLimits
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    PreservesFiniteLimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigSmoothOver.topology B T.1 T.2)
      (BigSmoothOver.topology B S.1 S.2))
```

**`AlgebraicGeometry.bigSmoothLowerShriek_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L167). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), smooth case.** Lower shriek on big smooth abelian sheaves preserves
> finite colimits.

```lean
public theorem bigSmoothLowerShriek_preservesFiniteColimits
    (B : BigSmoothSite.{u}) {T S : B.category} (f : T ⟶ S) :
    PreservesFiniteColimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigSmoothOver.topology B T.1 T.2)
      (BigSmoothOver.topology B S.1 S.2))
```

**`AlgebraicGeometry.bigSyntomicLowerShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L177). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), syntomic case.** Lower shriek on big syntomic abelian sheaves preserves
> finite limits.

```lean
public theorem bigSyntomicLowerShriek_preservesFiniteLimits
    (B : BigSyntomicSite.{u}) {T S : B.category} (f : T ⟶ S) :
    PreservesFiniteLimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigSyntomicOver.topology B T.1 T.2)
      (BigSyntomicOver.topology B S.1 S.2))
```

**`AlgebraicGeometry.bigSyntomicLowerShriek_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L187). The attribute's comment: “abelian\_lower\_shriek\_exact”.

> **Stacks 04CC(1), syntomic case.** Lower shriek on big syntomic abelian sheaves preserves
> finite colimits.

```lean
public theorem bigSyntomicLowerShriek_preservesFiniteColimits
    (B : BigSyntomicSite.{u}) {T S : B.category} (f : T ⟶ S) :
    PreservesFiniteColimits ((Over.map f).sheafPullback Ab.{u + 1}
      (BigSyntomicOver.topology B T.1 T.2)
      (BigSyntomicOver.topology B S.1 S.2))
```

**`AlgebraicGeometry.bigZariskiInverseImageRing_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L103). The attribute's comment: “module\_lower\_shriek\_inverse\_image\_structure\_sheaf”.

> **Stacks 04CC(2), Zariski case.** The inverse image of the structure sheaf of the big
> Zariski site over `S` is the structure sheaf of the big Zariski site over `T`.

```lean
public theorem bigZariskiInverseImageRing_eq :
    Stacks.SheafOfModules.inverseImageRing
        (BigZariskiOver.topology B T.1 T.property)
        (BigZariskiOver.topology B S.1 S.property) (Over.map f)
        (BigZariskiOver.structureSheaf B S.1 S.property) =
      BigZariskiOver.structureSheaf B T.1 T.property
```

**`AlgebraicGeometry.bigZariskiLowerShriekModulesAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L134). The attribute's comment: “module\_lower\_shriek\_adjunction”.

> **Stacks 04CC(2), Zariski case.** `f_big^*` on sheaves of modules of the big Zariski sites
> has `f_big!` as a left adjoint.

```lean
public def bigZariskiLowerShriekModulesAdjunction :
    bigZariskiLowerShriekModules B T S f ⊣ bigZariskiInverseImageModules B T S f
```

**`AlgebraicGeometry.bigZariskiLowerShriekModulesToSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L145). The attribute's comment: “module\_lower\_shriek\_agrees\_on\_abelian\_sheaves”.

> **Stacks 04CC(2), Zariski case.** The two `f_big!` agree on underlying sheaves of abelian
> groups: the underlying abelian sheaf of `f_big! M` is `f_big!` of the underlying abelian sheaf
> of `M`.

```lean
public def bigZariskiLowerShriekModulesToSheafIso :
    SheafOfModules.toSheaf.{u + 1} (BigZariskiOver.structureSheaf B T.1 T.property) ⋙
        (Over.map f).sheafPullback AddCommGrpCat.{u + 1}
          (BigZariskiOver.topology B T.1 T.property)
          (BigZariskiOver.topology B S.1 S.property) ≅
      bigZariskiLowerShriekModules B T S f ⋙
        SheafOfModules.toSheaf.{u + 1} (BigZariskiOver.structureSheaf B S.1 S.property)
```

**`AlgebraicGeometry.bigZariskiLowerShriekModules_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L161). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), Zariski case.** `f_big!` on sheaves of modules of the big Zariski sites
> preserves finite limits.  Lower shriek on abelian sheaves does, and forgetting the module
> structure both preserves and reflects finite limits.

```lean
public theorem bigZariskiLowerShriekModules_preservesFiniteLimits :
    PreservesFiniteLimits (bigZariskiLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigZariskiLowerShriekModules_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L171). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), Zariski case.** `f_big!` on sheaves of modules of the big Zariski sites
> preserves finite colimits: it is a left adjoint.

```lean
public theorem bigZariskiLowerShriekModules_preservesFiniteColimits :
    PreservesFiniteColimits (bigZariskiLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigEtaleInverseImageRing_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L189). The attribute's comment: “module\_lower\_shriek\_inverse\_image\_structure\_sheaf”.

> **Stacks 04CC(2), étale case.** The inverse image of the structure sheaf of the big étale
> site over `S` is the structure sheaf of the big étale site over `T`.

```lean
public theorem bigEtaleInverseImageRing_eq :
    Stacks.SheafOfModules.inverseImageRing
        (BigEtaleOver.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property) (Over.map f)
        (BigEtaleOver.structureSheaf B S.obj S.property) =
      BigEtaleOver.structureSheaf B T.obj T.property
```

**`AlgebraicGeometry.bigEtaleLowerShriekModulesAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L219). The attribute's comment: “module\_lower\_shriek\_adjunction”.

> **Stacks 04CC(2), étale case.** `f_big^*` on sheaves of modules of the big étale sites has
> `f_big!` as a left adjoint.

```lean
public def bigEtaleLowerShriekModulesAdjunction :
    bigEtaleLowerShriekModules B T S f ⊣ bigEtaleInverseImageModules B T S f
```

**`AlgebraicGeometry.bigEtaleLowerShriekModulesToSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L229). The attribute's comment: “module\_lower\_shriek\_agrees\_on\_abelian\_sheaves”.

> **Stacks 04CC(2), étale case.** The two `f_big!` agree on underlying sheaves of abelian
> groups.

```lean
public def bigEtaleLowerShriekModulesToSheafIso :
    SheafOfModules.toSheaf.{u + 1} (BigEtaleOver.structureSheaf B T.obj T.property) ⋙
        (Over.map f).sheafPullback AddCommGrpCat.{u + 1}
          (BigEtaleOver.topology B T.obj T.property)
          (BigEtaleOver.topology B S.obj S.property) ≅
      bigEtaleLowerShriekModules B T S f ⋙
        SheafOfModules.toSheaf.{u + 1} (BigEtaleOver.structureSheaf B S.obj S.property)
```

**`AlgebraicGeometry.bigEtaleLowerShriekModules_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L245). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), étale case.** `f_big!` on sheaves of modules of the big étale sites
> preserves finite limits.  Lower shriek on abelian sheaves does, and forgetting the module
> structure both preserves and reflects finite limits.

```lean
public theorem bigEtaleLowerShriekModules_preservesFiniteLimits :
    PreservesFiniteLimits (bigEtaleLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigEtaleLowerShriekModules_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L255). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), étale case.** `f_big!` on sheaves of modules of the big étale sites
> preserves finite colimits: it is a left adjoint.

```lean
public theorem bigEtaleLowerShriekModules_preservesFiniteColimits :
    PreservesFiniteColimits (bigEtaleLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigFppfInverseImageRing_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L273). The attribute's comment: “module\_lower\_shriek\_inverse\_image\_structure\_sheaf”.

> **Stacks 04CC(2), fppf case.** The inverse image of the structure sheaf of the big fppf
> site over `S` is the structure sheaf of the big fppf site over `T`.

```lean
public theorem bigFppfInverseImageRing_eq :
    Stacks.SheafOfModules.inverseImageRing
        (B.topology.over T)
        (B.topology.over S) (Over.map f)
        (BigFppfOver.structureSheaf B S.1 S.property) =
      BigFppfOver.structureSheaf B T.1 T.property
```

**`AlgebraicGeometry.bigFppfLowerShriekModulesAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L303). The attribute's comment: “module\_lower\_shriek\_adjunction”.

> **Stacks 04CC(2), fppf case.** `f_big^*` on sheaves of modules of the big fppf sites has
> `f_big!` as a left adjoint.

```lean
public def bigFppfLowerShriekModulesAdjunction :
    bigFppfLowerShriekModules B T S f ⊣ bigFppfInverseImageModules B T S f
```

**`AlgebraicGeometry.bigFppfLowerShriekModulesToSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L313). The attribute's comment: “module\_lower\_shriek\_agrees\_on\_abelian\_sheaves”.

> **Stacks 04CC(2), fppf case.** The two `f_big!` agree on underlying sheaves of abelian
> groups.

```lean
public def bigFppfLowerShriekModulesToSheafIso :
    SheafOfModules.toSheaf.{u + 1} (BigFppfOver.structureSheaf B T.1 T.property) ⋙
        (Over.map f).sheafPullback AddCommGrpCat.{u + 1}
          (B.topology.over T)
          (B.topology.over S) ≅
      bigFppfLowerShriekModules B T S f ⋙
        SheafOfModules.toSheaf.{u + 1} (BigFppfOver.structureSheaf B S.1 S.property)
```

**`AlgebraicGeometry.bigFppfLowerShriekModules_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L329). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), fppf case.** `f_big!` on sheaves of modules of the big fppf sites
> preserves finite limits.  Lower shriek on abelian sheaves does, and forgetting the module
> structure both preserves and reflects finite limits.

```lean
public theorem bigFppfLowerShriekModules_preservesFiniteLimits :
    PreservesFiniteLimits (bigFppfLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigFppfLowerShriekModules_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L339). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), fppf case.** `f_big!` on sheaves of modules of the big fppf sites
> preserves finite colimits: it is a left adjoint.

```lean
public theorem bigFppfLowerShriekModules_preservesFiniteColimits :
    PreservesFiniteColimits (bigFppfLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigSmoothInverseImageRing_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L357). The attribute's comment: “module\_lower\_shriek\_inverse\_image\_structure\_sheaf”.

> **Stacks 04CC(2), smooth case.** The inverse image of the structure sheaf of the big smooth
> site over `S` is the structure sheaf of the big smooth site over `T`.

```lean
public theorem bigSmoothInverseImageRing_eq :
    Stacks.SheafOfModules.inverseImageRing
        (BigSmoothOver.topology B T.1 T.2)
        (BigSmoothOver.topology B S.1 S.2) (Over.map f)
        (BigSmoothOver.structureSheaf B S.1 S.2) =
      BigSmoothOver.structureSheaf B T.1 T.2
```

**`AlgebraicGeometry.bigSmoothLowerShriekModulesAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L387). The attribute's comment: “module\_lower\_shriek\_adjunction”.

> **Stacks 04CC(2), smooth case.** `f_big^*` on sheaves of modules of the big smooth sites
> has `f_big!` as a left adjoint.

```lean
public def bigSmoothLowerShriekModulesAdjunction :
    bigSmoothLowerShriekModules B T S f ⊣ bigSmoothInverseImageModules B T S f
```

**`AlgebraicGeometry.bigSmoothLowerShriekModulesToSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L397). The attribute's comment: “module\_lower\_shriek\_agrees\_on\_abelian\_sheaves”.

> **Stacks 04CC(2), smooth case.** The two `f_big!` agree on underlying sheaves of abelian
> groups.

```lean
public def bigSmoothLowerShriekModulesToSheafIso :
    SheafOfModules.toSheaf.{u + 1} (BigSmoothOver.structureSheaf B T.1 T.2) ⋙
        (Over.map f).sheafPullback AddCommGrpCat.{u + 1}
          (BigSmoothOver.topology B T.1 T.2)
          (BigSmoothOver.topology B S.1 S.2) ≅
      bigSmoothLowerShriekModules B T S f ⋙
        SheafOfModules.toSheaf.{u + 1} (BigSmoothOver.structureSheaf B S.1 S.2)
```

**`AlgebraicGeometry.bigSmoothLowerShriekModules_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L413). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), smooth case.** `f_big!` on sheaves of modules of the big smooth sites
> preserves finite limits.  Lower shriek on abelian sheaves does, and forgetting the module
> structure both preserves and reflects finite limits.

```lean
public theorem bigSmoothLowerShriekModules_preservesFiniteLimits :
    PreservesFiniteLimits (bigSmoothLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigSmoothLowerShriekModules_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L423). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), smooth case.** `f_big!` on sheaves of modules of the big smooth sites
> preserves finite colimits: it is a left adjoint.

```lean
public theorem bigSmoothLowerShriekModules_preservesFiniteColimits :
    PreservesFiniteColimits (bigSmoothLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigSyntomicInverseImageRing_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L441). The attribute's comment: “module\_lower\_shriek\_inverse\_image\_structure\_sheaf”.

> **Stacks 04CC(2), syntomic case.** The inverse image of the structure sheaf of the big
> syntomic site over `S` is the structure sheaf of the big syntomic site over `T`.

```lean
public theorem bigSyntomicInverseImageRing_eq :
    Stacks.SheafOfModules.inverseImageRing
        (BigSyntomicOver.topology B T.1 T.2)
        (BigSyntomicOver.topology B S.1 S.2) (Over.map f)
        (BigSyntomicOver.structureSheaf B S.1 S.2) =
      BigSyntomicOver.structureSheaf B T.1 T.2
```

**`AlgebraicGeometry.bigSyntomicLowerShriekModulesAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L472). The attribute's comment: “module\_lower\_shriek\_adjunction”.

> **Stacks 04CC(2), syntomic case.** `f_big^*` on sheaves of modules of the big syntomic
> sites has `f_big!` as a left adjoint.

```lean
public def bigSyntomicLowerShriekModulesAdjunction :
    bigSyntomicLowerShriekModules B T S f ⊣ bigSyntomicInverseImageModules B T S f
```

**`AlgebraicGeometry.bigSyntomicLowerShriekModulesToSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L482). The attribute's comment: “module\_lower\_shriek\_agrees\_on\_abelian\_sheaves”.

> **Stacks 04CC(2), syntomic case.** The two `f_big!` agree on underlying sheaves of abelian
> groups.

```lean
public def bigSyntomicLowerShriekModulesToSheafIso :
    SheafOfModules.toSheaf.{u + 1} (BigSyntomicOver.structureSheaf B T.1 T.2) ⋙
        (Over.map f).sheafPullback AddCommGrpCat.{u + 1}
          (BigSyntomicOver.topology B T.1 T.2)
          (BigSyntomicOver.topology B S.1 S.2) ≅
      bigSyntomicLowerShriekModules B T S f ⋙
        SheafOfModules.toSheaf.{u + 1} (BigSyntomicOver.structureSheaf B S.1 S.2)
```

**`AlgebraicGeometry.bigSyntomicLowerShriekModules_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L498). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), syntomic case.** `f_big!` on sheaves of modules of the big syntomic sites
> preserves finite limits.  Lower shriek on abelian sheaves does, and forgetting the module
> structure both preserves and reflects finite limits.

```lean
public theorem bigSyntomicLowerShriekModules_preservesFiniteLimits :
    PreservesFiniteLimits (bigSyntomicLowerShriekModules B T S f)
```

**`AlgebraicGeometry.bigSyntomicLowerShriekModules_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/ModuleLowerShriek.lean#L508). The attribute's comment: “module\_lower\_shriek\_exact”.

> **Stacks 04CC(2), syntomic case.** `f_big!` on sheaves of modules of the big syntomic sites
> preserves finite colimits: it is a left adjoint.

```lean
public theorem bigSyntomicLowerShriekModules_preservesFiniteColimits :
    PreservesFiniteColimits (bigSyntomicLowerShriekModules B T S f)
```

Declarations registered for the tag:

- [`Functor.sheafPullbackConstruction.sheafAdjunctionContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.sheafPullbackConstruction.sheafAdjunctionContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesLowerShriek/AbelianExact.lean#L93) (StacksFrontier): “abelian\_lower\_shriek\_exact”.

## Tag 07AJ, a lemma

[Tag 07AJ](https://stacks.math.columbia.edu/tag/07AJ) in the Stacks Project.

**`AlgebraicGeometry.isIso_lowerShriekStructureSheafHom_of_isClosedUnderAffineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean#L236). The attribute's comment: “part (b)”.

> Let `C₁ ⊆ C₂` be full subcategories of the big fppf category over a scheme `X`, let `C₁`
> contain the base object `X/X` and the affine line over each of its objects, and let
> `g : Sh(C₁) ⟶ Sh(C₂)` be the morphism of topoi of the inclusion. Then the canonical map
> `g_!O₁ ⟶ O₂` from the lower shriek of the restricted structure sheaf to the structure sheaf is an
> isomorphism.
>
> The sheaf condition on the structure presheaf of `C₂` and the existence of `g_!`, a left adjoint
> of the pushforward along the inclusion, are taken as hypotheses.

```lean
theorem isIso_lowerShriekStructureSheafHom_of_isClosedUnderAffineLine
    {P₁ P₂ : ObjectProperty (BigFppfOver B X hX)} (h₁₂ : P₁ ≤ P₂)
    (J₁ : GrothendieckTopology P₁.FullSubcategory)
    (J₂ : GrothendieckTopology P₂.FullSubcategory)
    (hsh : Presheaf.IsSheaf J₂ (P₂.ι.op ⋙ bigOverPresheafAb B X hX))
    [(ObjectProperty.ιOfLE h₁₂).IsContinuous J₁ J₂]
    [((ObjectProperty.ιOfLE h₁₂).sheafPushforwardContinuous
      AddCommGrpCat.{t} J₁ J₂).IsRightAdjoint]
    (hbase : P₁ (Over.mk (𝟙 (B.obj hX)))) (hline : IsClosedUnderAffineLine P₁) :
    IsIso (lowerShriekStructureSheafHom h₁₂ J₁ J₂ hsh)
```

**`AlgebraicGeometry.fullyFaithful_isContinuous_isCocontinuous_ιOfLE_baseOverTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryBigFppfLowerShriek.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryBigFppfLowerShriek.lean#L373). The attribute's comment: “part (a), at the inherited topologies, for every τ”.

> **Stacks 07AJ (a).** Let `τ` be any of the Zariski, étale, smooth, syntomic and fppf
> topologies, and let `C₁ ⊆ C₂` be full subcategories of the big category over `X`, each with the
> topology it inherits from the big `τ`-site over `X`, both satisfying the closure condition (1)(a)
> of the source. Then the inclusion `C₁ ⊆ C₂` is fully faithful, continuous and cocontinuous.
>
> Full faithfulness holds for any inclusion of full subcategories; continuity and cocontinuity are
> `AlgebraicGeometry.isContinuous_ιOfLE_baseOverTopology` and
> `AlgebraicGeometry.isCocontinuous_ιOfLE_baseOverTopology`.

```lean
theorem fullyFaithful_isContinuous_isCocontinuous_ιOfLE_baseOverTopology (τ : CoveringTopology)
    {P₁ P₂ : ObjectProperty (BigFppfOver B X hX)} (h₁₂ : P₁ ≤ P₂)
    (hcov₁ : IsClosedUnderCoverings τ P₁) (hcov₂ : IsClosedUnderCoverings τ P₂) :
    (ObjectProperty.ιOfLE h₁₂).Full ∧ (ObjectProperty.ιOfLE h₁₂).Faithful ∧
      (ObjectProperty.ιOfLE h₁₂).IsContinuous
        (P₁.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind))
        (P₂.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind)) ∧
      (ObjectProperty.ιOfLE h₁₂).IsCocontinuous
        (P₁.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind))
        (P₂.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind))
```

**`AlgebraicGeometry.isIso_lowerShriekStructureSheafHom_baseOverTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryBigFppfLowerShriek.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryBigFppfLowerShriek.lean#L465). The attribute's comment: “part (b), at the inherited topologies, for every τ”.

> **Stacks 07AJ (b).** Let `τ` be any of the Zariski, étale, smooth, syntomic and fppf
> topologies, and let `C₁ ⊆ C₂` be full subcategories of the big category over a scheme `X`, each
> with the topology it inherits from the big `τ`-site over `X`, both satisfying the closure
> condition (1)(a) of the source, and let `C₁` contain the base object `X/X` and the affine line
> over each of its objects — conditions (2) and (1)(b). Writing `g : Sh(C₁) ⟶ Sh(C₂)` for the
> morphism of topoi of the inclusion, the canonical map `g_!O₁ ⟶ O₂` from the lower shriek of the
> restriction of the structure sheaf to the structure sheaf is an isomorphism.
>
> The continuity of the inclusion that `g` and `g_!` refer to is
> `AlgebraicGeometry.isContinuous_ιOfLE_baseOverTopology`; the existence of `g_!` is instance
> search on the essential smallness of the two sites; the descent witness for the structure
> presheaf of `C₂` is `AlgebraicGeometry.isSheaf_inheritedTopology_bigOverPresheafAb`. With those
> three supplied, the assertion is
> `AlgebraicGeometry.isIso_lowerShriekStructureSheafHom_of_isClosedUnderAffineLine` read at the
> inherited topologies.

```lean
theorem isIso_lowerShriekStructureSheafHom_baseOverTopology (τ : CoveringTopology)
    {P₁ P₂ : ObjectProperty (BigFppfOver B X hX)} (h₁₂ : P₁ ≤ P₂)
    (hcov₁ : IsClosedUnderCoverings τ P₁) (hcov₂ : IsClosedUnderCoverings τ P₂)
    (hbase : P₁ (Over.mk (𝟙 (B.obj hX)))) (hline : IsClosedUnderAffineLine P₁) :
    letI : (ObjectProperty.ιOfLE h₁₂).IsContinuous
        (P₁.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind))
        (P₂.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind)) :=
      isContinuous_ιOfLE_baseOverTopology τ h₁₂ hcov₁
    IsIso (lowerShriekStructureSheafHom h₁₂
      (P₁.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind))
      (P₂.ι.inheritedTopology (BigFppfOver.baseOverTopology B X hX τ.toSiteKind))
      (isSheaf_inheritedTopology_bigOverPresheafAb τ hcov₂))
```

Declarations registered for the tag:

- [`ObjectProperty.fullyFaithfulιOfLE`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ObjectProperty.fullyFaithfulιOfLE#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean#L257) (StacksFrontier): “part (a), full faithfulness”.
- [`ObjectProperty.isContinuous_ιOfLE_inheritedTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ObjectProperty.isContinuous_ιOfLE_inheritedTopology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean#L259) (StacksFrontier): “part (a), continuity”.
- [`ObjectProperty.isCocontinuous_ιOfLE_inheritedTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ObjectProperty.isCocontinuous_ιOfLE_inheritedTopology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SubcategoryAffineLineClosure.lean#L261) (StacksFrontier): “part (a), cocontinuity”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.49, Tag 04CB](https://stacks.math.columbia.edu/tag/04CB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
