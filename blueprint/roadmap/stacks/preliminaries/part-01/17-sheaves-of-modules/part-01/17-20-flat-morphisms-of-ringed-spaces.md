---
declaration: section
origin: cited
lean: Stacks.Cohomology.PerfectPushforward.isFlatOver_structureModule, AlgebraicGeometry.IsFlatAt, AlgebraicGeometry.IsFlat, RingedSpaceModuleAdjunction.exactFunctor_modulePullback_of_isFlat, AlgebraicGeometry.IsFlatOverAt, AlgebraicGeometry.IsFlatOver, Stacks.SheafOfModules.pullbackTensorFunctor_exact
statement: formalized
proof: formalized
---

# 17.20 Flat morphisms of ringed spaces

Section 17.20 of the Stacks Project, [Tag 02N2](https://stacks.math.columbia.edu/tag/02N2). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02N3, a definition

[Tag 02N3](https://stacks.math.columbia.edu/tag/02N3) in the Stacks Project.

**`Stacks.Cohomology.PerfectPushforward.isFlatOver_structureModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforward.lean, line 1709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforward.lean#L1709). The attribute's comment: “the structure sheaf of the source is flat over the target”. References: EGA IV (2.1.1), “partial”.

> **The structure sheaf of `X` is flat over `S` when `f` is flat**, which is
> [Stacks, Tag 02N3].  `AlgebraicGeometry.Flat.stalkMap` gives flatness of the stalk of the
> structure *sheaf* of `X` over the stalk of the structure sheaf of `S`, while
> `AlgebraicGeometry.IsFlatOverAt` asks for flatness of the stalk of the structure *module*, which
> is the same filtered colimit taken in `AddCommGrpCat` rather than in `CommRingCat`.
> `Stacks.Cohomology.PerfectPushforward.unitStalk_smul_eq` is the comparison of the two colimits,
> and `Stacks.Cohomology.PerfectPushforward.flat_compHom_of_addEquiv` transports flatness across
> it, restricting scalars along the stalk map of `f` on both sides.

```lean
theorem isFlatOver_structureModule [Flat f] :
    IsFlatOver f.toLRSHom.toShHom (structureModule X.toRingedSpace)
```

**`AlgebraicGeometry.IsFlatAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L51). The attribute's comment: “flat at a point”. References: EGA 0 (6.7.1), “f flat at x”.

> A morphism of ringed spaces is flat at `x` if its induced homomorphism from
> the stalk at the image of `x` to the stalk at `x` is flat.

```lean
public abbrev IsFlatAt {X Y : AlgebraicGeometry.RingedSpace.{u}} (f : X ⟶ Y) (x : X)
```

**`AlgebraicGeometry.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L57). The attribute's comment: “flat”. References: EGA 0 (6.7.1), “f flat”.

> A morphism of ringed spaces is flat if it is flat at every point of its
> source.

```lean
public abbrev IsFlat {X Y : AlgebraicGeometry.RingedSpace.{u}} (f : X ⟶ Y) : Prop
```

## Tag 02N4, a lemma

[Tag 02N4](https://stacks.math.columbia.edu/tag/02N4) in the Stacks Project.

**`RingedSpaceModuleAdjunction.exactFunctor_modulePullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/FlatPullback.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/FlatPullback.lean#L92). References: EGA 0 (6.7.8), “f* exact”; SGA 4 Vbis (2.4.0.1), “ringed spaces”.

> **Module pullback along a flat morphism of ringed spaces is exact.**

```lean
theorem exactFunctor_modulePullback_of_isFlat (hf : AlgebraicGeometry.IsFlat f) :
    exactFunctor (_root_.SheafOfModules.{u} (structureSheafRing Y))
      (_root_.SheafOfModules.{u} (structureSheafRing X)) (modulePullback f)
```

## Tag 08KT, a definition

[Tag 08KT](https://stacks.math.columbia.edu/tag/08KT) in the Stacks Project.

**`AlgebraicGeometry.IsFlatOverAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L63). The attribute's comment: “part (1)”. References: EGA 0 (6.7.1), “F f-flat at x”.

> An `O_X`-module is flat over `Y` at `x : X` if its stalk at `x`, regarded
> as an `O_{Y,f(x)}`-module through the stalk map of `f`, is flat.

```lean
public noncomputable abbrev IsFlatOverAt {X Y : AlgebraicGeometry.RingedSpace.{u}}
    (f : X ⟶ Y)
    (F : SheafOfModules.{u} ((sheafCompose (Opens.grothendieckTopology X)
      (forget₂ CommRingCat.{u} RingCat.{u})).obj X.sheaf))
    (x : X) : Prop
```

**`AlgebraicGeometry.IsFlatOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L80). The attribute's comment: “part (2)”. References: EGA 0 (6.7.1), “F f-flat (all x)”.

> An `O_X`-module is flat over `Y` if it is flat over `Y` at every point of
> `X`.

```lean
public abbrev IsFlatOver {X Y : AlgebraicGeometry.RingedSpace.{u}} (f : X ⟶ Y)
    (F : SheafOfModules.{u} ((sheafCompose (Opens.grothendieckTopology X)
      (forget₂ CommRingCat.{u} RingCat.{u})).obj X.sheaf)) : Prop
```

## Tag 0GMU, a lemma

[Tag 0GMU](https://stacks.math.columbia.edu/tag/0GMU) in the Stacks Project.

**`Stacks.SheafOfModules.pullbackTensorFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Flat/PullbackTensorExact.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Flat/PullbackTensorExact.lean#L490). References: SGA 4 V (1.7), “(ii) ⇒ (i)”.

> **Stacks Project, Tag 0GMU.** If `F` is an `𝒪_X`-module flat over `Y`, then the functor
> `G ↦ f^*G ⊗_{𝒪_X} F` is exact.

```lean
theorem pullbackTensorFunctor_exact (hF : AlgebraicGeometry.IsFlatOver f F) :
    exactFunctor (SheafOfModules.{u} (structureSheafRing Y))
      (SheafOfModules.{u} (structureSheafRing X)) (pullbackTensorFunctor f F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.20, Tag 02N2](https://stacks.math.columbia.edu/tag/02N2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
