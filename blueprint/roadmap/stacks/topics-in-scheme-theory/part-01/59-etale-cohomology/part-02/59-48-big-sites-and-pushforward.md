---
declaration: section
origin: cited
lean: AlgebraicGeometry.bigZariskiMorphism_counit_isIso, AlgebraicGeometry.bigEtaleMorphism_counit_isIso, AlgebraicGeometry.bigSmoothMorphism_counit_isIso, AlgebraicGeometry.bigSyntomicMorphism_counit_isIso, AlgebraicGeometry.bigFppfMorphism_counit_isIso, AlgebraicGeometry.bigZariskiLowerShriek_unit_isIso, AlgebraicGeometry.bigEtaleLowerShriek_unit_isIso, AlgebraicGeometry.bigSmoothLowerShriek_unit_isIso
statement: formalized
proof: formalized
---

# 59.48 Big sites and pushforward

Section 59.48 of the Stacks Project, [Tag 04E2](https://stacks.math.columbia.edu/tag/04E2). 6 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04C7, a lemma

[Tag 04C7](https://stacks.math.columbia.edu/tag/04C7) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiMorphism_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean#L90). The attribute's comment: “Zariski case”.

> **Stacks 04C7, the Zariski case.** The inverse-image/direct-image counit is invertible for
> a monomorphism on the big Zariski site.

```lean
public theorem bigZariskiMorphism_counit_isIso
    (B : BigZariskiSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigZariskiOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((bigZariskiMorphism B X Y f).adj.counit.app F)
```

**`AlgebraicGeometry.bigEtaleMorphism_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean#L99). The attribute's comment: “étale case”.

> **Stacks 04C7, the étale case.** The inverse-image/direct-image counit is invertible for a
> monomorphism on the big étale site.

```lean
public theorem bigEtaleMorphism_counit_isIso
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigEtaleOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((bigEtaleMorphism B X Y f).adj.counit.app F)
```

**`AlgebraicGeometry.bigSmoothMorphism_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean#L108). The attribute's comment: “smooth case”.

> **Stacks 04C7, the smooth case.** The inverse-image/direct-image counit is invertible for a
> monomorphism on the big smooth site.

```lean
public theorem bigSmoothMorphism_counit_isIso
    (B : BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigSmoothOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((bigSmoothMorphismOfTopoi B f).adj.counit.app F)
```

**`AlgebraicGeometry.bigSyntomicMorphism_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean#L117). The attribute's comment: “syntomic case”.

> **Stacks 04C7, the syntomic case.** The inverse-image/direct-image counit is invertible for
> a monomorphism on the big syntomic site.

```lean
public theorem bigSyntomicMorphism_counit_isIso
    (B : BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigSyntomicOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((bigSyntomicMorphismOfTopoi B f).adj.counit.app F)
```

**`AlgebraicGeometry.bigFppfMorphism_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismCounit.lean#L126). The attribute's comment: “fppf case”.

> **Stacks 04C7, the fppf case.** The inverse-image/direct-image counit is invertible for a
> monomorphism on the big fppf site.

```lean
public theorem bigFppfMorphism_counit_isIso
    (B : BigFppfSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (B.topology.over X) (Type (u + 1))) :
    IsIso ((bigFppfMorphism B X Y f).adj.counit.app F)
```

## Tag 04C8, a remark

[Tag 04C8](https://stacks.math.columbia.edu/tag/04C8) in the Stacks Project.

**`AlgebraicGeometry.bigZariskiLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L119). The attribute's comment: “sheaves of sets, Zariski case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, for the set-level `f_big!`”.

> **Stacks 04C8, the Zariski case for sheaves of sets.** The lower-shriek/inverse-image unit
> `F ⟶ f_big⁻¹ f_big! F` is invertible for a monomorphism on the big Zariski site.

```lean
public theorem bigZariskiLowerShriek_unit_isIso
    (B : BigZariskiSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigZariskiOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((bigZariskiLowerShriekAdjunction B X Y f).unit.app F)
```

**`AlgebraicGeometry.bigEtaleLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L131). The attribute's comment: “sheaves of sets, étale case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, for the set-level `f_big!`”.

> **Stacks 04C8, the étale case for sheaves of sets.** The lower-shriek/inverse-image unit
> `F ⟶ f_big⁻¹ f_big! F` is invertible for a monomorphism on the big étale site.

```lean
public theorem bigEtaleLowerShriek_unit_isIso
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigEtaleOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((bigEtaleLowerShriekAdjunction B X Y f).unit.app F)
```

**`AlgebraicGeometry.bigSmoothLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L143). The attribute's comment: “sheaves of sets, smooth case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, for the set-level `f_big!`”.

> **Stacks 04C8, the smooth case for sheaves of sets.** The lower-shriek/inverse-image unit
> `F ⟶ f_big⁻¹ f_big! F` is invertible for a monomorphism on the big smooth site.

```lean
public theorem bigSmoothLowerShriek_unit_isIso
    (B : BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigSmoothOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((Adjunction.ofIsRightAdjoint
      (bigSmoothMorphismOfTopoi B f).inverseImage).unit.app F)
```

**`AlgebraicGeometry.bigSyntomicLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L169). The attribute's comment: “sheaves of sets, syntomic case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, for the set-level `f_big!`”.

> **Stacks 04C8, the syntomic case for sheaves of sets.** The lower-shriek/inverse-image unit
> `F ⟶ f_big⁻¹ f_big! F` is invertible for a monomorphism on the big syntomic site.

```lean
public theorem bigSyntomicLowerShriek_unit_isIso
    (B : BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigSyntomicOver.topology B X.1 X.2) (Type (u + 1))) :
    IsIso ((bigSyntomicLowerShriekAdjunction B f).unit.app F)
```

**`AlgebraicGeometry.bigFppfLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L181). The attribute's comment: “sheaves of sets, fppf case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, for the set-level `f_big!`”.

> **Stacks 04C8, the fppf case for sheaves of sets.** The lower-shriek/inverse-image unit
> `F ⟶ f_big⁻¹ f_big! F` is invertible for a monomorphism on the big fppf site.

```lean
public theorem bigFppfLowerShriek_unit_isIso
    (B : BigFppfSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (B.topology.over X) (Type (u + 1))) :
    IsIso ((bigFppfLowerShriekAdjunction B X Y f).unit.app F)
```

**`AlgebraicGeometry.bigZariskiAbelianLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L200). The attribute's comment: “sheaves of abelian groups, Zariski case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, where `f_big!` is the abelian lower shriek of Modules on Sites 04BE, i.e. the left adjoint of `f_big⁻¹` on abelian sheaves, not the set-level `f_big!`”.

> **Stacks 04C8, the Zariski case for sheaves of abelian groups.** The unit
> `F ⟶ f_big⁻¹ f_big! F` of the abelian lower-shriek adjunction of Modules on Sites 04BE is
> invertible for a monomorphism on the big Zariski site.

```lean
public theorem bigZariskiAbelianLowerShriek_unit_isIso
    (B : BigZariskiSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigZariskiOver.topology B X.1 X.2) AbCat.{u, u + 1}) :
    IsIso (((Over.map f).sheafAdjunctionContinuous AbCat.{u, u + 1}
      (BigZariskiOver.topology B X.1 X.2)
      (BigZariskiOver.topology B Y.1 Y.2)).unit.app F)
```

**`AlgebraicGeometry.bigEtaleAbelianLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L214). The attribute's comment: “sheaves of abelian groups, étale case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, where `f_big!` is the abelian lower shriek of Modules on Sites 04BE, i.e. the left adjoint of `f_big⁻¹` on abelian sheaves, not the set-level `f_big!`”.

> **Stacks 04C8, the étale case for sheaves of abelian groups.** The unit
> `F ⟶ f_big⁻¹ f_big! F` of the abelian lower-shriek adjunction of Modules on Sites 04BE is
> invertible for a monomorphism on the big étale site.

```lean
public theorem bigEtaleAbelianLowerShriek_unit_isIso
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigEtaleOver.topology B X.1 X.2) AbCat.{u, u + 1}) :
    IsIso (((Over.map f).sheafAdjunctionContinuous AbCat.{u, u + 1}
      (BigEtaleOver.topology B X.1 X.2)
      (BigEtaleOver.topology B Y.1 Y.2)).unit.app F)
```

**`AlgebraicGeometry.bigSmoothAbelianLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L228). The attribute's comment: “sheaves of abelian groups, smooth case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, where `f_big!` is the abelian lower shriek of Modules on Sites 04BE, i.e. the left adjoint of `f_big⁻¹` on abelian sheaves, not the set-level `f_big!`”.

> **Stacks 04C8, the smooth case for sheaves of abelian groups.** The unit
> `F ⟶ f_big⁻¹ f_big! F` of the abelian lower-shriek adjunction of Modules on Sites 04BE is
> invertible for a monomorphism on the big smooth site.

```lean
public theorem bigSmoothAbelianLowerShriek_unit_isIso
    (B : BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigSmoothOver.topology B X.1 X.2) AbCat.{u, u + 1}) :
    IsIso (((Over.map f).sheafAdjunctionContinuous AbCat.{u, u + 1}
      (BigSmoothOver.topology B X.1 X.2)
      (BigSmoothOver.topology B Y.1 Y.2)).unit.app F)
```

**`AlgebraicGeometry.bigSyntomicAbelianLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L243). The attribute's comment: “sheaves of abelian groups, syntomic case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, where `f_big!` is the abelian lower shriek of Modules on Sites 04BE, i.e. the left adjoint of `f_big⁻¹` on abelian sheaves, not the set-level `f_big!`”.

> **Stacks 04C8, the syntomic case for sheaves of abelian groups.** The unit
> `F ⟶ f_big⁻¹ f_big! F` of the abelian lower-shriek adjunction of Modules on Sites 04BE is
> invertible for a monomorphism on the big syntomic site.

```lean
public theorem bigSyntomicAbelianLowerShriek_unit_isIso
    (B : BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (BigSyntomicOver.topology B X.1 X.2) AbCat.{u, u + 1}) :
    IsIso (((Over.map f).sheafAdjunctionContinuous AbCat.{u, u + 1}
      (BigSyntomicOver.topology B X.1 X.2)
      (BigSyntomicOver.topology B Y.1 Y.2)).unit.app F)
```

**`AlgebraicGeometry.bigFppfAbelianLowerShriek_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/MonomorphismLowerShriekUnit.lean#L257). The attribute's comment: “sheaves of abelian groups, fppf case: the canonical map `F → f_big⁻¹ f_big! F` is an isomorphism, where `f_big!` is the abelian lower shriek of Modules on Sites 04BE, i.e. the left adjoint of `f_big⁻¹` on abelian sheaves, not the set-level `f_big!`”.

> **Stacks 04C8, the fppf case for sheaves of abelian groups.** The unit
> `F ⟶ f_big⁻¹ f_big! F` of the abelian lower-shriek adjunction of Modules on Sites 04BE is
> invertible for a monomorphism on the big fppf site.

```lean
public theorem bigFppfAbelianLowerShriek_unit_isIso
    (B : BigFppfSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) [Mono f]
    (F : Sheaf (B.topology.over X) AbCat.{u, u + 1}) :
    IsIso (((Over.map f).sheafAdjunctionContinuous AbCat.{u, u + 1}
      (B.topology.over X) (B.topology.over Y)).unit.app F)
```

## Tag 04E3, a lemma

[Tag 04E3](https://stacks.math.columbia.edu/tag/04E3) in the Stacks Project.

**`AlgebraicGeometry.exists_etale_zariskiCover_baseChange_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/ClosedImmersionCoverings.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/ClosedImmersionCoverings.lean#L109). The attribute's comment: “etale\_cover”. References: EGA IV (18.1.1), “étale case”.

> An étale scheme over a closed subscheme has a Zariski covering by base changes of étale
> schemes over the ambient scheme.

```lean
public theorem exists_etale_zariskiCover_baseChange_of_isClosedImmersion
    {X Y U : Scheme.{u}} (i : X ⟶ Y) [IsClosedImmersion i]
    (p : U ⟶ X) [Etale p] :
    ∃ (I : Type u) (V : I → Scheme.{u}) (q : ∀ j, V j ⟶ Y)
      (g : ∀ j, pullback (q j) i ⟶ U),
      (∀ j, Etale (q j)) ∧
        (∀ j, g j ≫ p = pullback.snd (q j) i) ∧
          Presieve.ofArrows (fun j ↦ pullback (q j) i) g ∈ Scheme.zariskiPrecoverage U
```

**`AlgebraicGeometry.exists_smooth_zariskiCover_baseChange_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/ClosedImmersionCoverings.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/ClosedImmersionCoverings.lean#L178). The attribute's comment: “smooth\_cover”. References: EGA IV (18.1.1), “smooth case”.

> If `X ⟶ Y` is a closed immersion and `U ⟶ X` is smooth, then `U` has a Zariski covering
> by schemes obtained by base change from smooth schemes over `Y`.

```lean
public theorem exists_smooth_zariskiCover_baseChange_of_isClosedImmersion
    {X Y U : Scheme.{u}} (i : X ⟶ Y) [IsClosedImmersion i]
    (p : U ⟶ X) [Smooth p] :
    ∃ (I : Type u) (V : I → Scheme.{u}) (q : ∀ j, V j ⟶ Y)
      (g : ∀ j, pullback (q j) i ⟶ U),
      (∀ j, Smooth (q j)) ∧
        (∀ j, g j ≫ p = pullback.snd (q j) i) ∧
          Presieve.ofArrows (fun j ↦ pullback (q j) i) g ∈ Scheme.zariskiPrecoverage U
```

**`AlgebraicGeometry.exists_syntomic_zariskiCover_baseChange_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/ClosedImmersionCoverings.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/ClosedImmersionCoverings.lean#L193). The attribute's comment: “syntomic\_cover”.

> If `X ⟶ Y` is a closed immersion and `U ⟶ X` is syntomic, then `U` has a Zariski
> covering by schemes obtained by base change from syntomic schemes over `Y`.

```lean
public theorem exists_syntomic_zariskiCover_baseChange_of_isClosedImmersion
    {X Y U : Scheme.{u}} (i : X ⟶ Y) [IsClosedImmersion i]
    (p : U ⟶ X) (hp : AlgebraicGeometry.Syntomic p) :
    ∃ (I : Type u) (V : I → Scheme.{u}) (q : ∀ j, V j ⟶ Y)
      (g : ∀ j, pullback (q j) i ⟶ U),
      (∀ j, AlgebraicGeometry.Syntomic (q j)) ∧
        (∀ j, g j ≫ p = pullback.snd (q j) i) ∧
          Presieve.ofArrows (fun j ↦ pullback (q j) i) g ∈ Scheme.zariskiPrecoverage U
```

## Tag 04E4, a lemma

[Tag 04E4](https://stacks.math.columbia.edu/tag/04E4) in the Stacks Project.

**`AlgebraicGeometry.exists_syntomicCovering_subordinate_to_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/SubordinateCoverings.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/SubordinateCoverings.lean#L127). The attribute's comment: “syntomic case”.

> A syntomic covering of a closed subscheme can be prepared by a syntomic covering of the
> ambient scheme, with each base-changed member empty or subordinate to the original covering.

```lean
public theorem exists_syntomicCovering_subordinate_to_closedImmersion
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsClosedImmersion f]
    {I : Type v} (U : I → Scheme.{u}) (p : ∀ i, U i ⟶ X)
    (hp : AlgebraicGeometry.IsSyntomicCovering U p) :
    ∃ (J : Type (max u v)) (V : J → Scheme.{u}) (q : ∀ j, V j ⟶ Y),
      AlgebraicGeometry.IsSyntomicCovering V q ∧
        ∀ j, (IsEmpty (pullback (q j) f : Scheme.{u}) ∨
          ∃ i, ∃ h : pullback (q j) f ⟶ U i,
            h ≫ p i = pullback.snd (q j) f)
```

**`AlgebraicGeometry.exists_smoothCovering_subordinate_to_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/SubordinateCoverings.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/SubordinateCoverings.lean#L155). The attribute's comment: “smooth case”.

> A smooth covering of a closed subscheme can be prepared by a smooth covering of the
> ambient scheme, with each base-changed member empty or subordinate to the original covering.

```lean
public theorem exists_smoothCovering_subordinate_to_closedImmersion
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsClosedImmersion f]
    {I : Type v} (U : I → Scheme.{u}) (p : ∀ i, U i ⟶ X)
    (hp : Presieve.ofArrows U p ∈ Scheme.precoverage (@Smooth.{u}) X) :
    ∃ (J : Type (max u v)) (V : J → Scheme.{u}) (q : ∀ j, V j ⟶ Y),
      Presieve.ofArrows V q ∈ Scheme.precoverage (@Smooth.{u}) Y ∧
        ∀ j, (IsEmpty (pullback (q j) f : Scheme.{u}) ∨
          ∃ i, ∃ h : pullback (q j) f ⟶ U i,
            h ≫ p i = pullback.snd (q j) f)
```

**`AlgebraicGeometry.exists_etaleCovering_subordinate_to_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/SubordinateCoverings.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/SubordinateCoverings.lean#L177). The attribute's comment: “étale case”.

> An étale covering of a closed subscheme can be prepared by an étale covering of the
> ambient scheme, with each base-changed member empty or subordinate to the original covering.

```lean
public theorem exists_etaleCovering_subordinate_to_closedImmersion
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsClosedImmersion f]
    {I : Type v} (U : I → Scheme.{u}) (p : ∀ i, U i ⟶ X)
    (hp : Presieve.ofArrows U p ∈ Scheme.etalePrecoverage X) :
    ∃ (J : Type (max u v)) (V : J → Scheme.{u}) (q : ∀ j, V j ⟶ Y),
      Presieve.ofArrows V q ∈ Scheme.etalePrecoverage Y ∧
        ∀ j, (IsEmpty (pullback (q j) f : Scheme.{u}) ∨
          ∃ i, ∃ h : pullback (q j) f ⟶ U i,
            h ≫ p i = pullback.snd (q j) f)
```

## Tag 04C3, a lemma

[Tag 04C3](https://stacks.math.columbia.edu/tag/04C3) in the Stacks Project.

**`AlgebraicGeometry.bigSyntomicPullback_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/AlmostCocontinuousPullback.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/AlmostCocontinuousPullback.lean#L251). The attribute's comment: “syntomic case”.

> Base change by a closed immersion is almost cocontinuous on big syntomic sites.

```lean
public theorem bigSyntomicPullback_isAlmostCocontinuous
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    IsAlmostCocontinuous (Over.pullback f)
      (AlgebraicGeometry.BigSyntomicOver.topology B Y.1 Y.2)
      (AlgebraicGeometry.BigSyntomicOver.topology B X.1 X.2)
```

**`AlgebraicGeometry.bigSmoothPullback_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/AlmostCocontinuousPullback.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/AlmostCocontinuousPullback.lean#L284). The attribute's comment: “smooth case”.

> Base change by a closed immersion is almost cocontinuous on big smooth sites.

```lean
public theorem bigSmoothPullback_isAlmostCocontinuous
    (B : AlgebraicGeometry.BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion ((ObjectProperty.ι _).map f)] :
    IsAlmostCocontinuous (Over.pullback f)
      (AlgebraicGeometry.BigSmoothOver.topology B Y.1 Y.2)
      (AlgebraicGeometry.BigSmoothOver.topology B X.1 X.2)
```

**`AlgebraicGeometry.bigEtalePullback_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/AlmostCocontinuousPullback.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/AlmostCocontinuousPullback.lean#L327). The attribute's comment: “étale case”.

> Base change by a closed immersion is almost cocontinuous on big étale sites.

```lean
public theorem bigEtalePullback_isAlmostCocontinuous
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    IsAlmostCocontinuous (Over.pullback f)
      (AlgebraicGeometry.BigEtaleOver.topology B Y.1 Y.2)
      (AlgebraicGeometry.BigEtaleOver.topology B X.1 X.2)
```

## Tag 04C4, a lemma

[Tag 04C4](https://stacks.math.columbia.edu/tag/04C4) in the Stacks Project.

**`AlgebraicGeometry.bigSyntomicPushforward_preservesConnectedColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L171). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1).** Direct image of sheaves of sets by a closed immersion
> of big syntomic sites preserves colimits of every connected shape whose colimits of sets exist.
>
> This is Stacks Project, Tag 04B9 — the general form of the Tag 04BA that the source cites — fed
> the almost cocontinuity of base change supplied by Stacks Project, Tag 04C3. No passage to an
> equivalent small site is needed, Tag 04B9 being stated for an arbitrary pair of sites.

```lean
public theorem bigSyntomicPushforward_preservesConnectedColimits
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)]
    (I : Type t) [Category.{t'} I] [IsConnected I] [HasColimitsOfShape I (Type (u + 1))] :
    PreservesColimitsOfShape I
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigSyntomicOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSyntomicOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigSyntomicPushforward_preservesPushouts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L191). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1): pushouts.** Direct image of sheaves of sets by a closed
> immersion of big syntomic sites commutes with pushouts, `WalkingSpan` being a connected shape.

```lean
public theorem bigSyntomicPushforward_preservesPushouts
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    PreservesColimitsOfShape WalkingSpan
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigSyntomicOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSyntomicOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigSyntomicPushforward_preservesCoequalizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L204). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1): coequalizers.** Direct image of sheaves of sets by a
> closed immersion of big syntomic sites commutes with coequalizers, `WalkingParallelPair` being a
> connected shape.

```lean
public theorem bigSyntomicPushforward_preservesCoequalizers
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    PreservesColimitsOfShape WalkingParallelPair
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigSyntomicOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSyntomicOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigSmoothPushforward_preservesConnectedColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L216). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1).** Direct image of sheaves of sets by a closed immersion
> of big smooth sites preserves colimits of every connected shape whose colimits of sets exist.

```lean
public theorem bigSmoothPushforward_preservesConnectedColimits
    (B : AlgebraicGeometry.BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion ((ObjectProperty.ι _).map f)]
    (I : Type t) [Category.{t'} I] [IsConnected I] [HasColimitsOfShape I (Type (u + 1))] :
    PreservesColimitsOfShape I
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigSmoothOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSmoothOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigSmoothPushforward_preservesPushouts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L236). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1): pushouts.** Direct image of sheaves of sets by a closed
> immersion of big smooth sites commutes with pushouts.

```lean
public theorem bigSmoothPushforward_preservesPushouts
    (B : AlgebraicGeometry.BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion ((ObjectProperty.ι _).map f)] :
    PreservesColimitsOfShape WalkingSpan
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigSmoothOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSmoothOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigSmoothPushforward_preservesCoequalizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L248). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1): coequalizers.** Direct image of sheaves of sets by a
> closed immersion of big smooth sites commutes with coequalizers.

```lean
public theorem bigSmoothPushforward_preservesCoequalizers
    (B : AlgebraicGeometry.BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion ((ObjectProperty.ι _).map f)] :
    PreservesColimitsOfShape WalkingParallelPair
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigSmoothOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSmoothOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigEtalePushforward_preservesConnectedColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L260). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1).** Direct image of sheaves of sets by a closed immersion
> of big étale sites preserves colimits of every connected shape whose colimits of sets exist.

```lean
public theorem bigEtalePushforward_preservesConnectedColimits
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)]
    (I : Type t) [Category.{t'} I] [IsConnected I] [HasColimitsOfShape I (Type (u + 1))] :
    PreservesColimitsOfShape I
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigEtaleOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigEtaleOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigEtalePushforward_preservesPushouts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L280). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1): pushouts.** Direct image of sheaves of sets by a closed
> immersion of big étale sites commutes with pushouts.

```lean
public theorem bigEtalePushforward_preservesPushouts
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    PreservesColimitsOfShape WalkingSpan
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigEtaleOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigEtaleOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigEtalePushforward_preservesCoequalizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L292). The attribute's comment: “pushforward\_coequalizers\_pushouts”.

> **Stacks Project, Tag 04C4, part (1): coequalizers.** Direct image of sheaves of sets by a
> closed immersion of big étale sites commutes with coequalizers.

```lean
public theorem bigEtalePushforward_preservesCoequalizers
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    PreservesColimitsOfShape WalkingParallelPair
      ((Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (AlgebraicGeometry.BigEtaleOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigEtaleOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigSyntomicPushforward_isExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L305). The attribute's comment: “abelian\_pushforward\_exact”.

> Direct image of abelian sheaves by a closed immersion of big syntomic sites is exact.

```lean
public theorem bigSyntomicPushforward_isExact
    (B : AlgebraicGeometry.BigSyntomicSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    QuasiMorphismOfSites.IsExact
      ((Over.pullback f).sheafPushforwardContinuous Ab.{u + 1}
        (AlgebraicGeometry.BigSyntomicOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSyntomicOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigSmoothPushforward_isExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L317). The attribute's comment: “abelian\_pushforward\_exact”.

> Direct image of abelian sheaves by a closed immersion of big smooth sites is exact.

```lean
public theorem bigSmoothPushforward_isExact
    (B : AlgebraicGeometry.BigSmoothSite.{u}) {X Y : B.category} (f : X ⟶ Y)
    [IsClosedImmersion ((ObjectProperty.ι _).map f)] :
    QuasiMorphismOfSites.IsExact
      ((Over.pullback f).sheafPushforwardContinuous Ab.{u + 1}
        (AlgebraicGeometry.BigSmoothOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigSmoothOver.topology B X.1 X.2))
```

**`AlgebraicGeometry.bigEtalePushforward_isExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BigSitesPushforward/PushforwardExact.lean#L329). The attribute's comment: “abelian\_pushforward\_exact”.

> Direct image of abelian sheaves by a closed immersion of big étale sites is exact.

```lean
public theorem bigEtalePushforward_isExact
    (B : AlgebraicGeometry.BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsClosedImmersion (B.inclusion.map f)] :
    QuasiMorphismOfSites.IsExact
      ((Over.pullback f).sheafPushforwardContinuous Ab.{u + 1}
        (AlgebraicGeometry.BigEtaleOver.topology B Y.1 Y.2)
        (AlgebraicGeometry.BigEtaleOver.topology B X.1 X.2))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.48, Tag 04E2](https://stacks.math.columbia.edu/tag/04E2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
