---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.IsNormalAt, AlgebraicGeometry.Scheme.Hom.IsNormal, AlgebraicGeometry.Scheme.Hom.isNormal_iff, AlgebraicGeometry.Scheme.Hom.isNormal_tfae, AlgebraicGeometry.Scheme.Hom.isNormal_of_smooth, AlgebraicGeometry.locallyNoetherianFibers_isLocalAtSource_fppf, AlgebraicGeometry.locallyNoetherianFibers_isLocalAtTarget_fppf, AlgebraicGeometry.normalWithLocallyNoetherianFibers_isLocalAtTarget_fppf
statement: formalized
proof: formalized
---

# 37.20 Normal morphisms

Section 37.20 of the Stacks Project, [Tag 038Z](https://stacks.math.columbia.edu/tag/038Z). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0390, a definition

[Tag 0390](https://stacks.math.columbia.edu/tag/0390) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsNormalAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/NormalMorphism.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/NormalMorphism.lean#L48). The attribute's comment: “part (1)”. References: EGA IV (6.8.1).

> A morphism of schemes is normal at `x` if it is flat at `x` and its fibre over the image
> of `x` is geometrically normal at the point induced by `x`.

```lean
public abbrev IsNormalAt {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X) : Prop
```

**`AlgebraicGeometry.Scheme.Hom.IsNormal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/NormalMorphism.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/NormalMorphism.lean#L54). The attribute's comment: “part (2)”. References: EGA IV (6.8.1).

> A morphism of schemes is normal if it is normal at every point of its source.

```lean
public abbrev IsNormal {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

## Tag 0391, a lemma

[Tag 0391](https://stacks.math.columbia.edu/tag/0391) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isNormal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/Characterization.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/Characterization.lean#L70). The attribute's comment: “stated without the source's standing hypothesis that all fibres are locally Noetherian, which neither implication uses”. References: SGA 6 XII (1.6).

> A morphism of schemes is normal exactly when it is flat and each of its fibres is a
> geometrically normal scheme over the residue field of its base point.

```lean
public theorem isNormal_iff {X Y : Scheme.{u}} (f : X ⟶ Y) :
    IsNormal f ↔ Flat f ∧ ∀ s : Y, IsGeometricallyNormal (f.fiberToSpecResidueField s)
```

**`AlgebraicGeometry.Scheme.Hom.isNormal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/Characterization.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/Characterization.lean#L78).

> **Stacks Project, Tag 0391.** For a morphism of schemes all of whose fibres are locally
> Noetherian, being normal is equivalent to being flat with geometrically normal fibres.

```lean
public theorem isNormal_tfae {X Y : Scheme.{u}} (f : X ⟶ Y)
    (_hfib : locallyNoetherianFibers f) :
    List.TFAE
      [IsNormal f, Flat f ∧ ∀ s : Y, IsGeometricallyNormal (f.fiberToSpecResidueField s)]
```

## Tag 056W, a lemma

[Tag 056W](https://stacks.math.columbia.edu/tag/056W) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isNormal_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Normal.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/Normal.lean#L56). References: EGA IV (18.10.5), “more general”.

> **Stacks Project, Tag 056W.** A smooth morphism of schemes is normal: it is flat at every
> point and all of its fibres are geometrically normal.

```lean
public theorem isNormal_of_smooth {X Y : Scheme.{u}} (f : X ⟶ Y) [Smooth f] : f.IsNormal
```

## Tag 0392, a lemma

[Tag 0392](https://stacks.math.columbia.edu/tag/0392) in the Stacks Project.

**`AlgebraicGeometry.locallyNoetherianFibers_isLocalAtSource_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/LocallyNoetherianFibres.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/LocallyNoetherianFibres.lean#L112). The attribute's comment: “fppf local on the source”.

> **Stacks Project, Tag 0392.** Having locally Noetherian fibres is local on the source for the
> fppf topology.

```lean
public instance locallyNoetherianFibers_isLocalAtSource_fppf :
    (locallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtSource
      Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.locallyNoetherianFibers_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/LocallyNoetherianFibres.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/LocallyNoetherianFibres.lean#L124). The attribute's comment: “fppf local on the target”.

> **Stacks Project, Tag 0392.** Having locally Noetherian fibres is local on the target for the
> fppf topology.

```lean
public instance locallyNoetherianFibers_isLocalAtTarget_fppf :
    (locallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtTarget
      Scheme.fppfPrecoverage
```

## Tag 0393, a lemma

[Tag 0393](https://stacks.math.columbia.edu/tag/0393) in the Stacks Project.

**`AlgebraicGeometry.normalWithLocallyNoetherianFibers_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/FppfLocalTarget.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/FppfLocalTarget.lean#L198). The attribute's comment: “fppf local on the target”.

> Having locally Noetherian fibres and being normal is local on
> the target for the fppf topology.

```lean
public instance normalWithLocallyNoetherianFibers_isLocalAtTarget_fppf :
    (normalWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtTarget
      Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.normalWithLocallyNoetherianFibers_isLocalAtSource_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/SmoothLocalSource.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/NormalMorphism/SmoothLocalSource.lean#L186). The attribute's comment: “smooth local on the source”.

> Having locally Noetherian fibres and being normal is local on
> the source for the smooth topology.

```lean
public instance normalWithLocallyNoetherianFibers_isLocalAtSource_smooth :
    (normalWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtSource
      (Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.20, Tag 038Z](https://stacks.math.columbia.edu/tag/038Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
