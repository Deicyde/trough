---
declaration: section
origin: cited
lean: AlgebraicGeometry.quasiCoherentPresheaf, AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_fpqc', AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_etale', AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_smooth', AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_syntomic', AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_fppf', AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_zariski', AlgebraicGeometry.SmallEtale.associatedModule
statement: formalized
proof: formalized
---

# 35.8 Quasi-coherent sheaves and topologies, I

Section 35.8 of the Stacks Project, [Tag 03DR](https://stacks.math.columbia.edu/tag/03DR). 11 tags here are carried by 332 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03DS, an equation

[Tag 03DS](https://stacks.math.columbia.edu/tag/03DS) in the Stacks Project.

**`AlgebraicGeometry.quasiCoherentPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/PullbackSections.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/PullbackSections.lean#L298).

> The contravariant functor on schemes over `S` which sends `f : T ⟶ S` to
> `Γ(T, f⁺ F)`.

```lean
noncomputable def quasiCoherentPresheaf (S : Scheme.{u})
    (F : S.Modules) [F.IsQuasicoherent] : PullbackSectionsPresheaf S F
```

## Tag 03DT, a lemma

[Tag 03DT](https://stacks.math.columbia.edu/tag/03DT) in the Stacks Project.

**`AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_fpqc'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean#L362). The attribute's comment: “fpqc covering”.

> The pullback-sections presheaf of Stacks 03DS of a quasi-coherent module satisfies the sheaf
> condition for every fpqc covering.

```lean
theorem quasiCoherentPresheaf_isSheaf_fpqc' (S : Scheme.{u}) (F : S.Modules)
    [F.IsQuasicoherent] :
    Presheaf.IsSheaf (Scheme.fpqcTopology.over S) (quasiCoherentPresheafFunctor S F)
```

**`AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_etale'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean#L370). The attribute's comment: “étale covering”.

> The pullback-sections presheaf of Stacks 03DS of a quasi-coherent module satisfies the sheaf
> condition for every étale covering.

```lean
theorem quasiCoherentPresheaf_isSheaf_etale' (S : Scheme.{u}) (F : S.Modules)
    [F.IsQuasicoherent] :
    Presheaf.IsSheaf (Scheme.etaleTopology.over S) (quasiCoherentPresheafFunctor S F)
```

**`AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_smooth'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean#L378). The attribute's comment: “smooth covering”.

> The pullback-sections presheaf of Stacks 03DS of a quasi-coherent module satisfies the sheaf
> condition for every smooth covering.

```lean
theorem quasiCoherentPresheaf_isSheaf_smooth' (S : Scheme.{u}) (F : S.Modules)
    [F.IsQuasicoherent] :
    Presheaf.IsSheaf ((Scheme.grothendieckTopology (@Smooth)).over S)
      (quasiCoherentPresheafFunctor S F)
```

**`AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_syntomic'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean#L387). The attribute's comment: “syntomic covering”.

> The pullback-sections presheaf of Stacks 03DS of a quasi-coherent module satisfies the sheaf
> condition for every syntomic covering.

```lean
theorem quasiCoherentPresheaf_isSheaf_syntomic' (S : Scheme.{u}) (F : S.Modules)
    [F.IsQuasicoherent] :
    Presheaf.IsSheaf ((Scheme.grothendieckTopology (@Syntomic)).over S)
      (quasiCoherentPresheafFunctor S F)
```

**`AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_fppf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean#L396). The attribute's comment: “fppf covering”.

> The pullback-sections presheaf of Stacks 03DS of a quasi-coherent module satisfies the sheaf
> condition for every fppf covering.

```lean
theorem quasiCoherentPresheaf_isSheaf_fppf' (S : Scheme.{u}) (F : S.Modules)
    [F.IsQuasicoherent] :
    Presheaf.IsSheaf (Scheme.fppfTopology.over S) (quasiCoherentPresheafFunctor S F)
```

**`AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_zariski'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ZariskiHomAmalgamation.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/ZariskiHomAmalgamation.lean#L660). The attribute's comment: “Zariski covering”.

> The pullback-sections presheaf of a quasi-coherent module satisfies the sheaf condition for
> the Zariski topology on the schemes over `S`.

```lean
theorem quasiCoherentPresheaf_isSheaf_zariski' (S : Scheme.{u}) (F : S.Modules)
    [F.IsQuasicoherent] :
    Presheaf.IsSheaf (Scheme.zariskiTopology.over S) (quasiCoherentPresheafFunctor S F)
```

## Tag 03DU, a definition

[Tag 03DU](https://stacks.math.columbia.edu/tag/03DU) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.associatedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedSite.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedSite.lean#L425). The attribute's comment: “associated module on the small site, clause (4) at τ = étale, functor only”.

> **Stacks 03DU (4), at `τ = étale`.**  The associated-module functor of the small étale site
> of `S`: the pullback of sheaves of modules along the morphism of ringed sites
> `(S_étale, 𝒪) → (S_Zar, 𝒪_S)`.

```lean
public noncomputable def associatedModule :
    S.Modules ⥤ SheafOfModules.{u} (structureSheaf B S hS)
```

**`AlgebraicGeometry.SmallZariski.associatedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRingedSite.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRingedSite.lean#L193). The attribute's comment: “associated module on the small site, clause (4) at τ = Zariski, functor only”.

> **Stacks 03DU (4), at `τ = Zariski`.**  The associated-module functor of the small Zariski
> site of `S`: the pullback of sheaves of modules along the morphism of ringed sites
> `(S_Zar, 𝒪) → (S_Zar, 𝒪_S)`.
>
> This is the functor of clause (4), as the pullback of Remark 03FH (1), like its étale
> counterpart `AlgebraicGeometry.SmallEtale.associatedModule`.  The sections formula
> `T ↦ Γ(T, f^*𝓕)` by which the source also names it is
> `AlgebraicGeometry.SmallZariski.associatedModuleOfSections`, and the two descriptions are
> identified by `AlgebraicGeometry.SmallZariski.associatedModuleIsoOfSections`, which is
> Remark 03FH (1) for the morphism `id_{small, Zar, Zar}`.

```lean
public noncomputable def associatedModule :
    S.Modules ⥤ SheafOfModules.{u} (structureSheaf B S hS)
```

**`Stacks.Sites.associatedPresheaf_map_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/AssociatedModuleOnSite.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/AssociatedModuleOnSite.lean#L174). The attribute's comment: “module restriction maps”.

> **Tag 03DU, the module restriction maps.**  The restriction maps of the presheaf of
> pullback sections are semilinear over the restriction maps of the presheaf of global
> functions.

```lean
public theorem associatedPresheaf_map_smul {X Y : Cᵒᵖ} (f : X ⟶ Y)
    (r : (structurePresheaf S toOver).obj X) (m : (associatedPresheaf S F toOver).obj X) :
    letI := associatedPresheafModule S F toOver X
    letI := associatedPresheafModule S F toOver Y
    (associatedPresheaf S F toOver).map f (r • m) =
      (structurePresheaf S toOver).map f r • (associatedPresheaf S F toOver).map f m
```

**`AlgebraicGeometry.BigEtaleOver.structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigEtaleStructureSheaf.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigEtaleStructureSheaf.lean#L50). The attribute's comment: “big étale structure sheaf”.

> **Stacks 03DU, big étale structure sheaf.**  The presheaf of global functions is a sheaf of
> rings on the big étale site over `S`: a covering family of that site is étale and surjective,
> hence an fpqc covering, and global functions satisfy fpqc descent.

```lean
public theorem structure_isSheaf :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.structurePresheaf S (Over.post B.inclusion))
```

**`AlgebraicGeometry.BigEtaleOver.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigEtaleStructureSheaf.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigEtaleStructureSheaf.lean#L60). The attribute's comment: “big étale structure sheaf construction”. References: SGA 4½ Arcata (2.2), “structure sheaf O_S”.

> **Stacks 03DU, big étale structure sheaf construction.**  The structure sheaf of rings of
> the big étale site over `S`, whose value at `T/S` is `Γ(T, 𝒪_T)`.

```lean
public noncomputable def structureSheaf : Sheaf (topology B S hS) RingCat.{u}
```

**`AlgebraicGeometry.BigFppfOver.structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigFppfStructureSheaf.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigFppfStructureSheaf.lean#L113). The attribute's comment: “big fppf structure sheaf”.

> The presheaf of global functions is a sheaf of rings on the big fppf site over `S`.

```lean
theorem structure_isSheaf :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.structurePresheaf S (Over.post B.inclusion))
```

**`AlgebraicGeometry.BigFppfOver.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigFppfStructureSheaf.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigFppfStructureSheaf.lean#L120). The attribute's comment: “big fppf structure sheaf construction”.

> The structure sheaf of the big fppf site over `S`.

```lean
noncomputable def structureSheaf : Sheaf (topology B S hS) RingCat.{u}
```

**`AlgebraicGeometry.isSheaf_overAssociatedPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSiteAssociatedModule.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSiteAssociatedModule.lean#L167). The attribute's comment: “part (3), the sheaf condition for `Fᵃ`”.

> **The sheaf condition of [Stacks, Tag 03DU] (3), uniform in `τ`.**  The presheaf
> `(f : T → S) ↦ Γ(T, f^* F)` of [Stacks, Tag 03DS] satisfies the sheaf condition on the
> localized big `τ`-site: it is an fpqc sheaf on all schemes over `S` by [Stacks, Tag 03DT], and
> the functor into that slice is continuous.

```lean
public theorem isSheaf_overAssociatedPresheaf :
    Presheaf.IsSheaf (overTopology τ B S hS)
      (Stacks.Sites.associatedPresheaf S F (overToSlice τ B S hS))
```

**`AlgebraicGeometry.overAssociatedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSiteAssociatedModule.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSiteAssociatedModule.lean#L178). The attribute's comment: “part (3)”.

> **[Stacks, Tag 03DU] (3), uniform in `τ`.**  The associated module `Fᵃ` of a quasi-coherent
> `𝒪_S`-module `F` on the big `τ`-site of `S`, as a sheaf of modules over the structure sheaf of
> clause (1).  Its sections over an object `f : T → S` of the site are the global sections
> `Γ(T, f^* F)`, and no sheafification occurs.

```lean
public noncomputable def overAssociatedModule :
    SheafOfModules.{u} (overStructureSheaf τ B S hS)
```

**`AlgebraicGeometry.bigSite_structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean#L128). The attribute's comment: “the structure sheaf of a localized big site, uniformly in the topology”.

> **Stacks 03DU, uniformly in the topology.**  The presheaf of global functions
> `T/S ↦ Γ(T, 𝒪_T)` is a sheaf of rings on the localization at `S` of a big `τ`-site, for each of
> the five topologies.

```lean
public theorem bigSite_structure_isSheaf :
    Presheaf.IsSheaf (overTopology τ B S hS)
      (Stacks.Sites.structurePresheaf S (bigSiteToOver B S hS))
```

**`AlgebraicGeometry.BigSmoothOver.structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSmoothStructureSheaf.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSmoothStructureSheaf.lean#L50). The attribute's comment: “big smooth structure sheaf”.

> **Stacks 03DU, big smooth structure sheaf.**  The presheaf of global functions is a sheaf of
> rings on the big smooth site over `S`: a covering family of that site is smooth and surjective,
> hence an fpqc covering, and global functions satisfy fpqc descent.

```lean
public theorem structure_isSheaf :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.structurePresheaf S (Over.post (ObjectProperty.ι _)))
```

**`AlgebraicGeometry.BigSmoothOver.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSmoothStructureSheaf.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSmoothStructureSheaf.lean#L60). The attribute's comment: “big smooth structure sheaf construction”.

> **Stacks 03DU, big smooth structure sheaf construction.**  The structure sheaf of rings of
> the big smooth site over `S`, whose value at `T/S` is `Γ(T, 𝒪_T)`.

```lean
public noncomputable def structureSheaf : Sheaf (topology B S hS) RingCat.{u}
```

**`AlgebraicGeometry.BigSyntomicOver.structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSyntomicStructureSheaf.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSyntomicStructureSheaf.lean#L52). The attribute's comment: “big syntomic structure sheaf”.

> **Stacks 03DU, big syntomic structure sheaf.**  The presheaf of global functions is a sheaf
> of rings on the big syntomic site over `S`: a covering family of that site is syntomic and
> surjective, hence an fpqc covering, and global functions satisfy fpqc descent.

```lean
public theorem structure_isSheaf :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.structurePresheaf S (Over.post B.inclusion))
```

**`AlgebraicGeometry.BigSyntomicOver.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSyntomicStructureSheaf.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSyntomicStructureSheaf.lean#L62). The attribute's comment: “big syntomic structure sheaf construction”.

> **Stacks 03DU, big syntomic structure sheaf construction.**  The structure sheaf of rings of
> the big syntomic site over `S`, whose value at `T/S` is `Γ(T, 𝒪_T)`.

```lean
public noncomputable def structureSheaf : Sheaf (topology B S hS) RingCat.{u}
```

**`AlgebraicGeometry.BigZariskiOver.structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariskiStructureSheaf.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigZariskiStructureSheaf.lean#L55). The attribute's comment: “big Zariski structure sheaf”.

> **Stacks 03DU, big Zariski structure sheaf.**  The presheaf of global functions is a sheaf
> of rings on the big Zariski site over `S`: a covering family of that site is a jointly
> surjective family of open immersions, hence an fpqc covering, and global functions satisfy
> fpqc descent.

```lean
public theorem structure_isSheaf :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.structurePresheaf S
        (Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion))
```

**`AlgebraicGeometry.BigZariskiOver.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigZariskiStructureSheaf.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigZariskiStructureSheaf.lean#L66). The attribute's comment: “big Zariski structure sheaf construction”.

> **Stacks 03DU, big Zariski structure sheaf construction.**  The structure sheaf of rings of
> the big Zariski site over `S`, whose value at `T/S` is `Γ(T, 𝒪_T)`.

```lean
public noncomputable def structureSheaf : Sheaf (topology B S hS) RingCat.{u}
```

**`AlgebraicGeometry.BigFppfSite.carriedOver_structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L291). The attribute's comment: “the structure sheaf of the five localized big sites carried by a big fppf site”.

> **Stacks 03DU on all five localized sites at once.**  Global functions are a sheaf of rings
> on the localization at `S` of the big `τ`-site carried by `B`.

```lean
public theorem carriedOver_structure_isSheaf (τ : CoveringTopology) :
    Presheaf.IsSheaf (B.carriedOverTopology S hS τ)
      (Stacks.Sites.structurePresheaf S (Over.post B.inclusion))
```

**`AlgebraicGeometry.SmallEtale.structure_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleStructureSheaf.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleStructureSheaf.lean#L99). The attribute's comment: “small étale structure sheaf”.

> **Stacks 03DU, small étale structure sheaf.**  The presheaf of global functions on the small
> étale site of `S` is a sheaf of rings.

```lean
public theorem structure_isSheaf :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.structurePresheaf S (inclusion B S hS ⋙ Over.post B.inclusion))
```

**`AlgebraicGeometry.SmallEtale.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleStructureSheaf.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleStructureSheaf.lean#L106). The attribute's comment: “small étale structure sheaf construction”.

> The structure sheaf of the small étale site of `S`.

```lean
public noncomputable def structureSheaf : Sheaf (topology B S hS) RingCat.{u}
```

**`AlgebraicGeometry.SmallZariski.isSheaf_associatedPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean#L120). The attribute's comment: “part (4) at τ = Zariski, the sheaf condition for `Fᵃ`”.

> **The sheaf condition of [Stacks, Tag 03DU] (4) at `τ = Zariski`.**  The presheaf
> `T ↦ Γ(T, f^* F)` of [Stacks, Tag 03DS] satisfies the sheaf condition on the small Zariski site
> of `S`: it is an fpqc sheaf on all schemes over `S` by [Stacks, Tag 03DT], and the presenting
> functor of the small Zariski site is continuous.

```lean
public theorem isSheaf_associatedPresheaf :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.associatedPresheaf S F
        (inclusion B S hS ⋙ Over.post (X := (⟨S, hS⟩ : B.Schemes)) B.inclusion))
```

**`AlgebraicGeometry.SmallZariski.associatedModuleOfSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean#L133). The attribute's comment: “part (4) at τ = Zariski”.

> **[Stacks, Tag 03DU] (4) at `τ = Zariski`.**  The associated module `Fᵃ` of a quasi-coherent
> `𝒪_S`-module `F` on the small Zariski site `S_Zar`, as a sheaf of modules over the structure
> sheaf of clause (2).  Its sections over an open `T ⊆ S` are the global sections of the pullback
> of `F` to `T`, and no sheafification occurs.

```lean
public noncomputable def associatedModuleOfSections :
    SheafOfModules.{u} (structureSheaf B S hS)
```

**`AlgebraicGeometry.SmallEtale.isSheaf_associatedPresheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean#L170). The attribute's comment: “part (4) at τ = étale, the sheaf condition for `Fᵃ`”.

> **The sheaf condition of [Stacks, Tag 03DU] (4) at `τ = étale`, with no hypothesis.**
> `AlgebraicGeometry.SmallEtale.isSheaf_associatedPresheaf` with its argument discharged: the fpqc
> sheaf condition it asks for is [Stacks, Tag 03DT], which
> `AlgebraicGeometry.quasiCoherentPresheaf_isSheaf_fpqc'` proves unconditionally.

```lean
public theorem isSheaf_associatedPresheaf' :
    Presheaf.IsSheaf (topology B S hS)
      (Stacks.Sites.associatedPresheaf S F
        (inclusion B S hS ⋙ Over.post (X := B.obj S hS) B.inclusion))
```

**`AlgebraicGeometry.SmallEtale.associatedModuleOfSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallSiteAssociatedModule.lean#L189). The attribute's comment: “part (4) at τ = étale”.

> **[Stacks, Tag 03DU] (4) at `τ = étale`.**  The associated module `Fᵃ` of a quasi-coherent
> `𝒪_S`-module `F` on the small étale site `S_étale`, as a sheaf of modules over the structure
> sheaf of clause (2).  Its sections over an object `T` of the site are the global sections of the
> pullback of `F` to `T`, and no sheafification occurs.
>
> This is the construction [Stacks, Tag 03DU] (4) performs.  It is not
> `AlgebraicGeometry.SmallEtale.associatedModule`, which is the pullback of sheaves of modules
> along the morphism of ringed sites `(S_étale, 𝒪) → (S_Zar, 𝒪_S)`; the two agree by
> [Stacks, Remark 03FH], which for quasi-coherent `F` is
> `AlgebraicGeometry.SmallEtale.associatedModuleIsoSectionsSheaf`.

```lean
public noncomputable def associatedModuleOfSections :
    SheafOfModules.{u} (structureSheaf B S hS)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.SmallZariski.structure_isSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiStructureSheaf.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SmallZariskiStructureSheaf.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallZariskiStructureSheaf.lean#L31) (StacksFrontier): “small Zariski structure sheaf”.
- [`AlgebraicGeometry.SmallZariski.structureSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiStructureSheaf.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SmallZariskiStructureSheaf.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallZariskiStructureSheaf.lean#L32) (StacksFrontier): “small Zariski structure sheaf construction”.

## Tag 03FG, a remark

[Tag 03FG](https://stacks.math.columbia.edu/tag/03FG) in the Stacks Project.

**`AlgebraicGeometry.smallZariskiModuleEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallZariskiModules.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallZariskiModules.lean#L73). The attribute's comment: “equivalence of module categories”.

> Sheaves of modules on the small Zariski site are the same as sheaves of
> modules on the ringed space of the scheme.

```lean
public noncomputable def smallZariskiModuleEquiv
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    SheafOfModules.{m} (SmallZariski.structureSheaf B S hS) ≌
      SheafOfModules.{m} S.ringCatSheaf
```

**`AlgebraicGeometry.smallZariskiModuleEquiv_forgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallZariskiModules.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallZariskiModules.lean#L185). The attribute's comment: “compatibility with underlying sheaves”.

> The module equivalence induces the usual equivalence on underlying sheaves
> of sets.

```lean
public noncomputable def smallZariskiModuleEquiv_forgetIso
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (SheafOfModules.toSheaf.{m} (SmallZariski.structureSheaf B S hS) ⋙
      sheafCompose (SmallZariski.topology B S hS)
        (forget AddCommGrpCat.{m}) ⋙
      (smallZariskiSheafEquiv B S hS).functor) ≅
    ((smallZariskiModuleEquiv.{u, m} B S hS).functor ⋙
      SheafOfModules.toSheaf.{m} S.ringCatSheaf ⋙
      sheafCompose (Opens.grothendieckTopology S.carrier)
        (forget AddCommGrpCat.{m}))
```

**`AlgebraicGeometry.smallZariskiModuleEquiv_comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallZariskiModules.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallZariskiModules.lean#L252). The attribute's comment: “canonical sectionwise comparison”.

> The equivalence is the usual open-subscheme comparison, including its
> sectionwise scalar action and both naturality properties.

```lean
public noncomputable def smallZariskiModuleEquiv_comparison
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    SmallZariskiModuleComparison B S hS
      (smallZariskiModuleEquiv.{u, m} B S hS)
```

## Tag 070R, a remark

[Tag 070R](https://stacks.math.columbia.edu/tag/070R) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.toZariskiRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedToposHom.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedToposHom.lean#L156). The attribute's comment: “the morphism of ringed sites `id_{small, étale, Zar} : (S_étale, 𝒪) → (S_Zar, 𝒪_S)`, item (26) of the list of Topologies, Section 03FE at `f = id`”.

> **Stacks 070R.** The morphism of ringed sites
> `id_{small, étale, Zar} : (S_étale, 𝒪) ⟶ (S_Zar, 𝒪_S)`: the continuous inclusion of the small
> Zariski site of `S` into the small étale site of `S`, with structure map the identification of
> the sections of `𝒪_S` over an open with the functions on it.

```lean
public noncomputable def toZariskiRingedToposHom :
    RingedToposSiteHom (ringedTopos B S hS) S.zariskiRingedTopos
```

**`AlgebraicGeometry.BigFppfOver.baseStructureComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean#L128). The attribute's comment: “part (1): `f_big^♯` for the big fppf, syntomic, smooth, étale and Zariski sites, at the structure sheaves over which modules are taken”.

> **Stacks 070R, part (1): the structure-sheaf map `f_big^♯ : 𝒪_Y ⟶ f_{big, *}𝒪_X`**, in each
> of the five topologies.  Its component at an object `T/Y` is the map on global functions induced
> by the projection `X ×_Y T ⟶ T`, that is, the map `𝒪(T/Y) ⟶ 𝒪(X ×_Y T/X)` of the source.
>
> This is `AlgebraicGeometry.BigFppfOver.structureComparison` read at the `τ`-localized
> topologies: the same map of presheaves of rings, the topology entering only through the sheaf
> conditions and the continuity instance.

```lean
public noncomputable def baseStructureComparison :
    FibredSite.baseRingStructureSheaf B Y hY τ ⟶
      ((baseChange B hX hY f).sheafPushforwardContinuous RingCat.{u}
        (baseOverTopology B Y hY τ) (baseOverTopology B X hX τ)).obj
        (FibredSite.baseRingStructureSheaf B X hX τ)
```

**`AlgebraicGeometry.BigFppfOver.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigFppfRingedMorphism.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigFppfRingedMorphism.lean#L130). The attribute's comment: “part (1): the functor underlying the morphism of big fppf sites `f_big`”.

> The continuous functor giving the morphism of big fppf sites
> `f_big : (Sch/X)_fppf → (Sch/Y)_fppf`: base change along `f`, sending `T / Y` to `X ×_Y T / X`.

```lean
public noncomputable def baseChange : BigFppfOver B Y hY ⥤ BigFppfOver B X hX
```

**`AlgebraicGeometry.BigFppfOver.isMorphismOfSites_baseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigFppfRingedMorphism.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigFppfRingedMorphism.lean#L157). The attribute's comment: “part (1): base change is a morphism of sites, so `f_big` is one”.

> Base change along `f` defines a morphism of big fppf sites
> `f_big : (Sch/X)_fppf → (Sch/Y)_fppf` in the sense of Stacks 00X1: it is continuous, and the
> pushforward it induces on sheaves of sets has a left exact left adjoint.
>
> That left adjoint is the inverse image of `f_big`, which is restriction along postcomposition:
> the pushforward along the cocontinuous functor `CategoryTheory.Over.map` agrees with the
> pushforward along its continuous right adjoint `CategoryTheory.Over.pullback`, and restriction
> along postcomposition is left exact.

```lean
public instance isMorphismOfSites_baseChange :
    IsMorphismOfSites.{u + 1} (baseChange B hX hY f) (topology B Y hY) (topology B X hX)
```

**`AlgebraicGeometry.BigFppfOver.structureComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigFppfRingedMorphism.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigFppfRingedMorphism.lean#L188). The attribute's comment: “part (1): the structure-sheaf map `f_big^♯` of the morphism of ringed sites”.

> The map of structure sheaves `f_big^♯ : 𝒪_Y → f_{big, *} 𝒪_X` which, together with the
> morphism of sites `f_big`, makes `f_big` a morphism of ringed sites
> `((Sch/X)_fppf, 𝒪_X) ⟶ ((Sch/Y)_fppf, 𝒪_Y)` as in Stacks Definition 03AD.
>
> Its component at an object `T / Y` is the map on global functions induced by the projection
> `X ×_Y T → T`, that is, the map `𝒪(T / Y) → 𝒪(X ×_Y T / X)` of the source.

```lean
public noncomputable def structureComparison :
    structureSheaf B Y hY ⟶
      ((baseChange B hX hY f).sheafPushforwardContinuous RingCat.{u}
        (topology B Y hY) (topology B X hX)).obj (structureSheaf B X hX)
```

**`AlgebraicGeometry.smallEtaleRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedSiteHom.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedSiteHom.lean#L236). The attribute's comment: “part (2): the morphism of ringed sites of the small étale sites of schemes”.

> **Stacks 070R, part (2).** The morphism of ringed sites
> `(f_small, f_small^♯) : (X_étale, 𝒪_X) ⟶ (Y_étale, 𝒪_Y)` attached to a morphism of schemes
> `a : X ⟶ Y`: the underlying morphism of sites is base change of étale `Y`-schemes along `a`, and
> the structure map pulls a global function on an étale `V / Y` back along the projection
> `X ×_Y V ⟶ V`.

```lean
public def smallEtaleRingedSiteHom {X Y : B.Scheme} (a : X ⟶ Y) :
    RingedSite.HomGeneral (smallEtaleRingedSite B X.obj X.property)
      (smallEtaleRingedSite B Y.obj Y.property)
```

**`AlgebraicGeometry.smallEtaleRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/RingedToposTwoIso.lean#L60). The attribute's comment: “part (2), read in the 2-category of ringed topoi”.

> The morphism of small étale *ringed topoi* `(a_small, a_small^♯) : (X_étale, 𝒪_X) ⟶
> (Y_étale, 𝒪_Y)` of a morphism of schemes `a : X ⟶ Y`.

```lean
def smallEtaleRingedToposHom (a : X ⟶ Y) :
    RingedToposHom (RingedSite.toRingedTopos (smallEtaleRingedSite B X.obj X.property))
      (RingedSite.toRingedTopos (smallEtaleRingedSite B Y.obj Y.property))
```

**`AlgebraicGeometry.isMorphismOfSites_bigSiteBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean#L169). The attribute's comment: “part (1): `f_big` is a morphism of sites, in each of the five topologies”.

> **Stacks 070R, part (1): `f_big` is a morphism of sites**, at the universe of the sections
> of the structure sheaves, which is the universe at which a morphism of ringed sites reads its
> site condition.
>
> A localized big site is essentially small at the universe of its morphisms
> (`AlgebraicGeometry.essentiallySmall_overBase`) and base change is continuous and flat, so this
> is `isMorphismOfSites_of_essentiallySmall`.

```lean
public theorem isMorphismOfSites_bigSiteBaseChange :
    IsMorphismOfSites.{u} (Over.pullback f) (overTopology τ B S hS) (overTopology τ B T hT)
```

**`AlgebraicGeometry.bigSiteStructureSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean#L193). The attribute's comment: “part (1): `f_big^♯`, in each of the five topologies”.

> **Stacks 070R, part (1): the structure map `f_big^♯ : 𝒪_S ⟶ f_{big, *}𝒪_T`**, in each of
> the five topologies.  On an object `S'/S` it is the map on global functions induced by the
> projection `T ×_S S' ⟶ S'`, that is, the usual `pr_{S'}^♯`.

```lean
public noncomputable def bigSiteStructureSharp :
    commStructureSheaf S (overTopology τ B S hS) (bigSiteToOver B S hS)
        (bigSite_structure_isSheaf B S hS) ⟶
      ((Over.pullback f).sheafPushforwardContinuous CommRingCat.{u} (overTopology τ B S hS)
        (overTopology τ B T hT)).obj
      (commStructureSheaf T (overTopology τ B T hT) (bigSiteToOver B T hT)
        (bigSite_structure_isSheaf B T hT))
```

**`AlgebraicGeometry.bigSiteRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedBigSiteHom.lean#L223). The attribute's comment: “part (1): `(f_big, f_big^♯)` for the big fppf, syntomic, smooth, étale and Zariski sites”.

> **Stacks 070R, part (1), in all five topologies at once.**  A morphism of schemes of a big
> `τ`-site makes the morphism of big sites `f_big : (\Sch/T)_τ ⟶ (\Sch/S)_τ` a morphism of ringed
> sites
>
> ```
>   (f_big, f_big^♯) : ((\Sch/T)_τ, 𝒪_T) ⟶ ((\Sch/S)_τ, 𝒪_S)
> ```
>
> in the sense of Stacks 03AD, for `τ` the fppf, syntomic, smooth, étale or Zariski topology.

```lean
public noncomputable def bigSiteRingedSiteHom :
    RingedSite.HomGeneral (bigSiteRingedSite B T hT) (bigSiteRingedSite B S hS)
```

**`AlgebraicGeometry.smallZariskiPiRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L127). The attribute's comment: “`π_S` on the Zariski sites, as a morphism of ringed sites”.

> The projection `π_S : (\Sch/S)_{Zar} ⟶ S_{Zar}` of Topologies, Lemma 020Z, as a morphism of
> ringed sites
>
> ```
>   (π_S, π_S^♯) : ((\Sch/S)_{Zar}, 𝒪) ⟶ (S_{Zar}, 𝒪).
> ```
>
> Its structure map is the identity, by
> `AlgebraicGeometry.smallZariskiPiStructureSharp_eq_id`.

```lean
public noncomputable def smallZariskiPiRingedSiteHom :
    RingedSite.HomGeneral (bigSiteRingedSite (τ := .zariski) B S.1 S.property)
      (smallZariskiRingedSite B S.1 S.property)
```

**`AlgebraicGeometry.smallZariskiPiStructureSharp_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L148). The attribute's comment: “`π_S^♯` is the identity on the Zariski sites”.

> **The structure map of `π_S` is the identity.**  Both structure sheaves are global functions
> on the underlying scheme, and the inclusion of the small site into the big one is compatible
> with the two underlying-scheme functors on the nose, so no comparison map intervenes.

```lean
public theorem smallZariskiPiStructureSharp_eq_id :
    (smallZariskiPiRingedSiteHom B (S := S)).fsharp = 𝟙 _
```

**`AlgebraicGeometry.smallZariskiToBig_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L160). The attribute's comment: “the identity `i_f^{-1}𝒪 = 𝒪` for the big and small Zariski sites”.

> **`i_f^{-1}𝒪 = 𝒪` for the Zariski sites.**  Restricting the structure sheaf of the big
> Zariski site over `S` along the functor `V/T ↦ V/S` which presents the morphism of topoi
> `i_f : \mathrm{Sh}(T_{Zar}) ⟶ \mathrm{Sh}((\Sch/S)_{Zar})` of Topologies, Lemma 020Y returns the
> structure sheaf of the small Zariski site of `T`.
>
> By the inverse-image formula of that lemma the inverse image of `i_f` is that restriction, so
> this is the identity `i_f^{-1}𝒪 = 𝒪` which the remark gives as the reason `i_f` becomes a
> morphism of ringed topoi.

```lean
public theorem smallZariskiToBig_structureSheaf :
    ((smallZariskiToBigZariskiFunctor B T S f).sheafPushforwardContinuous CommRingCat.{u}
          (SmallZariski.topology B T.1 T.property)
          (BigZariskiOver.topology B S.1 S.property)).obj
        (bigSiteRingedSite (τ := .zariski) B S.1 S.property).O =
      (smallZariskiRingedSite B T.1 T.property).O
```

**`AlgebraicGeometry.smallEtalePiRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L210). The attribute's comment: “`π_S` on the étale sites, as a morphism of ringed sites”.

> The projection `π_S : (\Sch/S)_\etale ⟶ S_\etale` of Topologies, Lemma 021G, as a morphism
> of ringed sites
>
> ```
>   (π_S, π_S^♯) : ((\Sch/S)_\etale, 𝒪) ⟶ (S_\etale, 𝒪).
> ```
>
> Its structure map is the identity, by
> `AlgebraicGeometry.smallEtalePiStructureSharp_eq_id`.

```lean
public noncomputable def smallEtalePiRingedSiteHom :
    RingedSite.HomGeneral (bigSiteRingedSite (τ := .etale) B S.obj S.property)
      (smallEtaleRingedSite B S.obj S.property)
```

**`AlgebraicGeometry.smallEtalePiStructureSharp_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L231). The attribute's comment: “`π_S^♯` is the identity on the étale sites”.

> **The structure map of `π_S` is the identity**, for the same reason as on the Zariski
> sites.

```lean
public theorem smallEtalePiStructureSharp_eq_id :
    (smallEtalePiRingedSiteHom B (S := S)).fsharp = 𝟙 _
```

**`AlgebraicGeometry.smallEtaleToBig_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedProjectionAndIf.lean#L239). The attribute's comment: “the identity `i_f^{-1}𝒪 = 𝒪` for the big and small étale sites”.

> **`i_f^{-1}𝒪 = 𝒪` for the étale sites.**  Restricting the structure sheaf of the big étale
> site over `S` along the functor `V/T ↦ V/S` which presents the morphism of topoi
> `i_f : \mathrm{Sh}(T_\etale) ⟶ \mathrm{Sh}((\Sch/S)_\etale)` of Topologies, Lemma 021F returns
> the structure sheaf of the small étale site of `T`.

```lean
public theorem smallEtaleToBig_structureSheaf :
    ((smallEtaleToBigEtaleFunctor B T S f).sheafPushforwardContinuous CommRingCat.{u}
          (SmallEtale.topology B T.obj T.property)
          (BigEtaleOver.topology B S.obj S.property)).obj
        (bigSiteRingedSite (τ := .etale) B S.obj S.property).O =
      (smallEtaleRingedSite B T.obj T.property).O
```

**`AlgebraicGeometry.smallZariskiToBigZariski_inverseImageStructureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L130). The attribute's comment: “`i_f^{-1}𝒪 = 𝒪` for the Zariski sites, as an isomorphism of ring sheaves”.

> **`i_f^{-1}𝒪 = 𝒪` for the Zariski sites**, as an isomorphism of sheaves of commutative
> rings.  The inverse image of `i_f` is restriction, and restricting the structure sheaf of the
> big Zariski site over `S` along `V/T ↦ V/S` returns the structure sheaf of the small Zariski
> site of `T` — which is `AlgebraicGeometry.smallZariskiToBig_structureSheaf`, an equality by
> `rfl`.  The comparison is the identity on sections.

```lean
public noncomputable def smallZariskiToBigZariski_inverseImageStructureIso :
    (inverseImageCommRingFunctor (smallZariskiToBigZariskiToposHom B f)).obj
        (bigSiteRingedSite (τ := .zariski) B S.1 S.property).O ≅
      (smallZariskiRingedSite B T.1 T.property).O
```

**`AlgebraicGeometry.smallZariskiToBigZariskiRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L148). The attribute's comment: “`i_f` on the Zariski sites, as a morphism of ringed topoi”.

> **Stacks 070R for `i_f` on the Zariski sites.**  The morphism of topoi
> `i_f : \mathrm{Sh}(T_{Zar}) ⟶ \mathrm{Sh}((\Sch/S)_{Zar})` of Topologies, Lemma 020Y, as a
> morphism of ringed topoi
>
> ```
>   (i_f, i_f^♯) : (\mathrm{Sh}(T_{Zar}), 𝒪) ⟶ (\mathrm{Sh}((\Sch/S)_{Zar}), 𝒪),
> ```
>
> in the sense of Stacks 01D3.  Its structure map is the one determined by `i_f^{-1}𝒪 = 𝒪`.

```lean
public noncomputable def smallZariskiToBigZariskiRingedToposHom :
    RingedToposHom (smallZariskiRingedSite B T.1 T.property).toRingedTopos
      (bigSiteRingedSite (τ := .zariski) B S.1 S.property).toRingedTopos
```

**`AlgebraicGeometry.isIso_smallZariskiToBigZariskiRingedToposHom_fSharpInverseImage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L176). The attribute's comment: “`i_f` is a morphism of ringed topoi because `i_f^{-1}𝒪 = 𝒪`, Zariski case”.

> **The formal content of "because `i_f^{-1}𝒪 = 𝒪`":** the structure map of `i_f` in
> inverse-image form is an isomorphism.

```lean
public instance isIso_smallZariskiToBigZariskiRingedToposHom_fSharpInverseImage :
    IsIso (smallZariskiToBigZariskiRingedToposHom B f).fSharpInverseImage
```

**`AlgebraicGeometry.smallEtaleToBigEtale_inverseImageStructureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L215). The attribute's comment: “`i_f^{-1}𝒪 = 𝒪` for the étale sites, as an isomorphism of ring sheaves”.

> **`i_f^{-1}𝒪 = 𝒪` for the étale sites**, as an isomorphism of sheaves of commutative rings.
> The underlying equality of ring sheaves is
> `AlgebraicGeometry.smallEtaleToBig_structureSheaf`, which holds by `rfl`.

```lean
public noncomputable def smallEtaleToBigEtale_inverseImageStructureIso :
    (inverseImageCommRingFunctor (smallEtaleToBigEtaleToposHom B f)).obj
        (bigSiteRingedSite (τ := .etale) B S.obj S.property).O ≅
      (smallEtaleRingedSite B T.obj T.property).O
```

**`AlgebraicGeometry.smallEtaleToBigEtaleRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L227). The attribute's comment: “`i_f` on the étale sites, as a morphism of ringed topoi”.

> **Stacks 070R for `i_f` on the étale sites.**  The morphism of topoi
> `i_f : \mathrm{Sh}(T_\etale) ⟶ \mathrm{Sh}((\Sch/S)_\etale)` of Topologies, Lemma 021F, as a
> morphism of ringed topoi, in the sense of Stacks 01D3.

```lean
public noncomputable def smallEtaleToBigEtaleRingedToposHom :
    RingedToposHom (smallEtaleRingedSite B T.obj T.property).toRingedTopos
      (bigSiteRingedSite (τ := .etale) B S.obj S.property).toRingedTopos
```

**`AlgebraicGeometry.isIso_smallEtaleToBigEtaleRingedToposHom_fSharpInverseImage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/RingedToposIf.lean#L255). The attribute's comment: “`i_f` is a morphism of ringed topoi because `i_f^{-1}𝒪 = 𝒪`, étale case”.

> **The formal content of "because `i_f^{-1}𝒪 = 𝒪`":** the structure map of `i_f` in
> inverse-image form is an isomorphism.

```lean
public instance isIso_smallEtaleToBigEtaleRingedToposHom_fSharpInverseImage :
    IsIso (smallEtaleToBigEtaleRingedToposHom B f).fSharpInverseImage
```

**`AlgebraicGeometry.smallZariskiStructureSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiRingedSiteHom.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiRingedSiteHom.lean#L191). The attribute's comment: “part (2): `f_small^♯` for the small Zariski sites”.

> **Stacks 070R, part (2): the structure map `f_small^♯ : 𝒪_S ⟶ f_{small, *}𝒪_T`** on the
> small Zariski sites.  On an open `V/S` it is the map on global functions induced by the
> projection `T ×_S V ⟶ V`, through the identification of small Zariski base change with the
> fibre product.

```lean
public noncomputable def smallZariskiStructureSharp :
    (smallZariskiRingedSite B S.1 S.property).O ⟶
      ((smallZariskiBaseChange B f).sheafPushforwardContinuous CommRingCat.{u}
          (SmallZariski.topology B S.1 S.property)
          (SmallZariski.topology B T.1 T.property)).obj
        (smallZariskiRingedSite B T.1 T.property).O
```

**`AlgebraicGeometry.smallZariskiRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiRingedSiteHom.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/SmallZariskiRingedSiteHom.lean#L223). The attribute's comment: “part (2): `(f_small, f_small^♯)` for the small Zariski sites”.

> **Stacks 070R, part (2), for the small Zariski site.**  A morphism of schemes `f : T ⟶ S` of
> a big Zariski site makes the morphism of small sites `f_small : T_{Zar} ⟶ S_{Zar}` a morphism of
> ringed sites
>
> ```
>   (f_small, f_small^♯) : (T_{Zar}, 𝒪_T) ⟶ (S_{Zar}, 𝒪_S)
> ```
>
> in the sense of Stacks 03AD.  This is the "similarly for the small Zariski site" of part (2),
> and item (27) of the change-of-topologies list of Topologies, Section 03FE.

```lean
public noncomputable def smallZariskiRingedSiteHom :
    RingedSite.HomGeneral (smallZariskiRingedSite B T.1 T.property)
      (smallZariskiRingedSite B S.1 S.property)
```

**`AlgebraicGeometry.BigFppfSite.isMorphismOfSites_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L325). The attribute's comment: “`id_{τ, τ'}` is a morphism of sites, at the universe of the structure rings”.

> **Stacks 070R, the generator `id_{τ, τ'}` of the 03FE list: it is a morphism of sites**, at
> the universe of the sections of the structure sheaves.
>
> The identity functor is representably flat, and a localized big site is essentially small at the
> universe of its morphisms, so this is `isMorphismOfSites_of_essentiallySmall`.

```lean
public theorem isMorphismOfSites_id (h : τ.IsFiner τ') :
    IsMorphismOfSites.{u} (𝟭 (Over (B.obj hS)))
      (B.carriedOverTopology S hS τ') (B.carriedOverTopology S hS τ)
```

**`AlgebraicGeometry.BigFppfSite.idRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L345). The attribute's comment: “`id_{τ, τ'}` as a morphism of ringed sites”.

> **Stacks 070R for the generator `id_{τ, τ'}`.**  The identity
> `id_{τ, τ'} : (\Sch/S)_τ ⟶ (\Sch/S)_{τ'}`, for `τ` finer than `τ'`, as a morphism of ringed
> sites
>
> ```
>   (id_{τ, τ'}, id_{τ, τ'}^♯) : ((\Sch/S)_τ, 𝒪) ⟶ ((\Sch/S)_{τ'}, 𝒪).
> ```
>
> Its structure map is the identity, by
> `AlgebraicGeometry.BigFppfSite.idRingedSiteHom_fsharp`.

```lean
public noncomputable def idRingedSiteHom (h : τ.IsFiner τ') :
    RingedSite.HomGeneral (B.carriedOverRingedSite S hS τ) (B.carriedOverRingedSite S hS τ')
```

**`AlgebraicGeometry.BigFppfSite.idRingedSiteHom_fsharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L361). The attribute's comment: “`id_{τ, τ'}^♯` is the identity”.

> **`id_{τ, τ'}^♯` is the identity.**  The two sites are presented by the one functor to the
> schemes over `S`, so their structure presheaves are literally the same presheaf and no
> comparison map intervenes.

```lean
public theorem idRingedSiteHom_fsharp (h : τ.IsFiner τ') :
    (B.idRingedSiteHom S hS h).fsharp = 𝟙 _
```

**`AlgebraicGeometry.BigFppfSite.bigBaseChangeRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L392). The attribute's comment: “part (1): `f_big` on the five big sites carried by one big fppf site”.

> **Stacks 070R, part (1) on the sites carried by `B`.**  `f_big` as a morphism of ringed
> sites, for each of the five topologies.

```lean
public noncomputable def bigBaseChangeRingedSiteHom (τ : CoveringTopology)
    (f : B.obj hT ⟶ B.obj hS) :
    RingedSite.HomGeneral (B.carriedOverRingedSite T hT τ) (B.carriedOverRingedSite S hS τ)
```

**`AlgebraicGeometry.BigFppfSite.bigRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologies.lean#L420). The attribute's comment: “entries (1)-(15) of the 03FE list: `(Sch/T)_τ ⟶ (Sch/S)_τ'` for τ finer than τ'”.

> **Stacks 070R for every big-site entry of the change-of-topologies list.**  For a morphism of
> schemes `f : T ⟶ S` of a chosen big fppf site and `τ` finer than `τ'`, the morphism of sites
> `f_{sites} : (\Sch/T)_τ ⟶ (\Sch/S)_{τ'}` of Topologies, Section 03FE is a morphism of ringed
> sites
>
> ```
>   (f_{sites}, f_{sites}^♯) : ((\Sch/T)_τ, 𝒪_T) ⟶ ((\Sch/S)_{τ'}, 𝒪_S).
> ```
>
> This is entries (1)–(15) of that list: `f_{sites}` is `id_{τ, τ'} ∘ f_{big}`, and the
> composition of morphisms of ringed sites is Stacks 03AD, part (3).

```lean
public noncomputable def bigRingedSiteHom (h : τ.IsFiner τ') (f : B.obj hT ⟶ B.obj hS) :
    RingedSite.HomGeneral (B.carriedOverRingedSite T hT τ) (B.carriedOverRingedSite S hS τ')
```

**`AlgebraicGeometry.BigFppfSite.bigToSmallEtaleRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologiesList.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologiesList.lean#L99). The attribute's comment: “entries (16)-(19) of the 03FE list: `(Sch/T)_τ ⟶ S_étale`”.

> **Stacks 070R, entries (16)–(19) of the change-of-topologies list.**  For `τ` finer than the
> étale topology, the morphism of sites `f_{sites} : (\Sch/T)_τ ⟶ S_\etale` is a morphism of
> ringed sites.  It is `π_S ∘ f_{sites}`, with `f_{sites} : (\Sch/T)_τ ⟶ (\Sch/S)_\etale` the
> big-site entry and `π_S : (\Sch/S)_\etale ⟶ S_\etale` the projection of Topologies,
> Lemma 021G.

```lean
public noncomputable def bigToSmallEtaleRingedSiteHom (h : τ.IsFiner .etale)
    (f : B.obj hT ⟶ B.obj hS) :
    RingedSite.HomGeneral (B.carriedOverRingedSite T hT τ)
      (smallEtaleRingedSite B.toBigEtaleSite S hS)
```

**`AlgebraicGeometry.BigFppfSite.bigToSmallZariskiRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologiesList.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologiesList.lean#L111). The attribute's comment: “entries (20)-(24) of the 03FE list: `(Sch/T)_τ ⟶ S_Zar`”.

> **Stacks 070R, entries (20)–(24) of the change-of-topologies list.**  For every one of the
> five topologies, the morphism of sites `f_{sites} : (\Sch/T)_τ ⟶ S_{Zar}` is a morphism of
> ringed sites.  It is `π_S ∘ f_{sites}`, with `π_S : (\Sch/S)_{Zar} ⟶ S_{Zar}` the projection of
> Topologies, Lemma 020Z.

```lean
public noncomputable def bigToSmallZariskiRingedSiteHom (h : τ.IsFiner .zariski)
    (f : B.obj hT ⟶ B.obj hS) :
    RingedSite.HomGeneral (B.carriedOverRingedSite T hT τ)
      (smallZariskiRingedSite B.toBigZariskiSite S hS)
```

**`AlgebraicGeometry.smallEtaleToSmallZariskiRingedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologiesList.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedChangeOfTopologiesList.lean#L134). The attribute's comment: “entry (26) of the 03FE list: `T_étale ⟶ S_Zar`”.

> **Stacks 070R, entry (26) of the change-of-topologies list.**  The morphism of sites
> `T_\etale ⟶ S_{Zar}` is a morphism of ringed sites: it is
> `id_{small, \etale, Zar} ∘ f_{small}`, with `f_{small} : T_\etale ⟶ S_\etale` the morphism of
> ringed small étale sites of Stacks 070R part (2) and `id_{small, \etale, Zar}` the inclusion of
> the small Zariski site of `S` into its small étale site.
>
> The target is the opens model of the small Zariski site of `S`, which is the model in which
> `AlgebraicGeometry.SmallEtale.toZariskiRingedSiteHom` is stated; see the implementation notes.

```lean
public noncomputable def smallEtaleToSmallZariskiRingedSiteHom (B : BigEtaleSite.{u})
    {X Y : B.Scheme} (a : X ⟶ Y) :
    RingedSite.HomGeneral (smallEtaleRingedSite B X.obj X.property)
      Y.obj.zariskiRingedSite
```

**`AlgebraicGeometry.ChangeOfSites.structureSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean#L119). The attribute's comment: “the structure-sheaf homomorphism `f_sites^♯` of a change-of-topologies morphism”.

> **Stacks 070R.**  The structure-sheaf homomorphism `f_sites^♯ : 𝒪 ⟶ f_{sites, *}𝒪` of a
> change-of-topologies morphism of sites.
>
> Here `F` is the continuous functor representing `f_sites`, in the direction opposite to it, and
> `p` is the family of projections `T ×_S S' ⟶ S'` of underlying schemes, natural in the object
> `S'` of the target site.  The homomorphism is pullback of global functions along `p`.

```lean
public noncomputable def structureSharp [F.IsContinuous J K]
    (p : F ⋙ toOver' ⋙ Over.forget T ⟶ toOver ⋙ Over.forget S)
    (hJ : Presheaf.IsSheaf J (Stacks.Sites.structurePresheaf S toOver))
    (hK : Presheaf.IsSheaf K (Stacks.Sites.structurePresheaf T toOver')) :
    commStructureSheaf S J toOver hJ ⟶
      (F.sheafPushforwardContinuous CommRingCat.{u} J K).obj
        (commStructureSheaf T K toOver' hK)
```

**`AlgebraicGeometry.ChangeOfSites.structureSharpOfBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean#L160). The attribute's comment: “`f_sites^♯` for a functor exhibited as base change along `f : T ⟶ S`”.

> **Stacks 070R.**  The structure-sheaf homomorphism of a change-of-topologies morphism of
> sites whose continuous functor is exhibited as scheme-theoretic base change along
> `f : T ⟶ S`: on an object `S'/S` it is the usual map
> `pr_{S'}^♯ : 𝒪(S') ⟶ 𝒪(T ×_S S')`.

```lean
public noncomputable def structureSharpOfBaseChange [F.IsContinuous J K] (f : T ⟶ S)
    (bc : F ⋙ toOver' ≅ toOver ⋙ Over.pullback f)
    (hJ : Presheaf.IsSheaf J (Stacks.Sites.structurePresheaf S toOver))
    (hK : Presheaf.IsSheaf K (Stacks.Sites.structurePresheaf T toOver')) :
    commStructureSheaf S J toOver hJ ⟶
      (F.sheafPushforwardContinuous CommRingCat.{u} J K).obj
        (commStructureSheaf T K toOver' hK)
```

**`AlgebraicGeometry.ChangeOfSites.ringedSiteHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean#L188). The attribute's comment: “a change-of-topologies morphism of sites is one of ringed sites”.

> **Stacks 070R.**  A change-of-topologies morphism of sites, together with its
> structure-sheaf homomorphism, is a morphism of ringed sites
>
> ```
>   (f_sites, f_sites^♯) : ((Sch/T)_τ, 𝒪_T) ⟶ ((Sch/S)_{τ'}, 𝒪_S)
> ```
>
> in the sense of Stacks 03AD.

```lean
public noncomputable def ringedSiteHom (hF : IsMorphismOfSites.{u} F J K)
    (p : F ⋙ toOver' ⋙ Over.forget T ⟶ toOver ⋙ Over.forget S)
    (hJ : Presheaf.IsSheaf J (Stacks.Sites.structurePresheaf S toOver))
    (hK : Presheaf.IsSheaf K (Stacks.Sites.structurePresheaf T toOver')) :
    RingedSite.HomGeneral (ringedSite T K toOver' hK) (ringedSite S J toOver hJ)
```

**`AlgebraicGeometry.ChangeOfSites.ringedSiteHomOfBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/RingedSiteHom.lean#L219). The attribute's comment: “the morphism of ringed sites of a base-change morphism of sites”.

> **Stacks 070R.**  The same, for a continuous functor exhibited as scheme-theoretic base
> change along `f : T ⟶ S`, which is the form every morphism of the change-of-topologies list
> takes.

```lean
public noncomputable def ringedSiteHomOfBaseChange (hF : IsMorphismOfSites.{u} F J K)
    (f : T ⟶ S) (bc : F ⋙ toOver' ≅ toOver ⋙ Over.pullback f)
    (hJ : Presheaf.IsSheaf J (Stacks.Sites.structurePresheaf S toOver))
    (hK : Presheaf.IsSheaf K (Stacks.Sites.structurePresheaf T toOver')) :
    RingedSite.HomGeneral (ringedSite T K toOver' hK) (ringedSite S J toOver hJ)
```

## Tag 070S, a lemma

[Tag 070S](https://stacks.math.columbia.edu/tag/070S) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.associatedModuleIsoPullbackSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleArbitraryModule.lean, line 1141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleArbitraryModule.lean#L1141). The attribute's comment: “part (2)”.

> **Stacks 070S (2).**  Let `F` be an arbitrary sheaf of `𝒪_S`-modules.  The pullback of `F`
> along the morphism of ringed sites `id_{small,étale,Zar} : (S_étale, 𝒪) → (S_Zar, 𝒪_S)` is the
> étale sheafification of the presheaf `(f : T → S) ↦ Γ(T, f^*F)` on `S_étale`.
>
> The pullback is `AlgebraicGeometry.SmallEtale.associatedModule`, presented by
> `AlgebraicGeometry.SmallEtale.associatedModuleSheafificationIso` as the sheafification of the
> pullback of presheaves of modules, and the identification is the sheafification of the
> comparison `AlgebraicGeometry.SmallEtale.pullbackSectionsComparison`, an isomorphism by
> `AlgebraicGeometry.SmallEtale.isIso_sheafification_map_pullbackSectionsComparison`.

```lean
public noncomputable def associatedModuleIsoPullbackSections (F : S.Modules) :
    (associatedModule B S hS).obj F ≅
      (PresheafOfModules.sheafification.{u} (𝟙 (structureSheaf B S hS).obj)).obj
        (pullbackSectionsPresheaf B S hS F)
```

**`AlgebraicGeometry.SmallEtale.associatedModuleIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleAssociatedModuleSections.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleAssociatedModuleSections.lean#L82). The attribute's comment: “part (2), in the shape of part (1): 𝓕^a is the étale sheafification of the pullback-sections presheaf of Stacks 03DS”.

> **Stacks 070S for the small étale site of `S`.** The associated module `𝓕^a` of a
> quasi-coherent `𝒪_S`-module `𝓕` is the étale sheafification of the pullback-sections presheaf
> `(f : T → S) ↦ Γ(T, f⁺𝓕)` of Stacks 03DS.
>
> `AlgebraicGeometry.SmallEtale.associatedModuleSheafificationIso` presents `𝓕^a` as the
> sheafification of the presheaf-level pullback along the structure map, and
> `AlgebraicGeometry.SmallEtale.sectionsComparisonSheafifiesToIso` — Stacks 070S (2), with no
> hypothesis — says the comparison of that pullback with the pullback-sections presheaf becomes an
> isomorphism after sheafification.

```lean
public noncomputable def associatedModuleIsoSections (F : S.Modules) [F.IsQuasicoherent] :
    (associatedModule B S hS).obj F ≅
      (PresheafOfModules.sheafification.{u} (𝟙 (structureSheaf B S hS).obj)).obj
        (sectionsPresheafOfModules B S hS F)
```

**`AlgebraicGeometry.SmallEtale.sectionsComparisonSheafifiesToIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean#L635). The attribute's comment: “part (2), small site at τ = étale”.

> **Stacks 070S part (2) for `S_étale`**: the hypothesis
> `AlgebraicGeometry.SmallEtale.SectionsComparisonSheafifiesToIso` holds.

```lean
public theorem sectionsComparisonSheafifiesToIso :
    SectionsComparisonSheafifiesToIso B S hS
```

**`AlgebraicGeometry.BigFppfOver.baseSmallEtalePullbackIsoSectionsSheafification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleSectionsSheafTauBigSite.lean, line 1129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleSectionsSheafTauBigSite.lean#L1129). The attribute's comment: “part (3)”.

> **Stacks 070S part (3).**  For an *arbitrary* sheaf of `𝒪`-modules `𝓖` on the small étale
> site `S_étale`, the inverse image `(id_{τ,étale})^*𝓖` along the morphism of ringed sites
> `id_{τ,étale} : ((Sch/S)_τ, 𝒪) ⟶ (S_étale, 𝒪)` is the `τ`-sheafification of the étale sheaf
> `(f : T → S) ↦ Γ(T, f_small^*𝓖)` on `(Sch/S)_τ`, where `f_small : T_étale ⟶ S_étale` is the
> morphism of ringed small étale sites of Stacks 070R (2).
>
> Here `(id_{τ,étale})^*` is
> `AlgebraicGeometry.BigFppfOver.smallEtaleToBaseModulePullback`, the sections rule is
> `AlgebraicGeometry.BigFppfOver.smallEtaleSectionsPresheafOfModules`, and the identification is
> `CategoryTheory.SheafOfModules.pullbackIso` — which presents `(id_{τ,étale})^*𝓖` as the
> `τ`-sheafification of the presheaf-level inverse image — followed by the `τ`-sheafification of
> the comparison `AlgebraicGeometry.BigFppfOver.smallEtaleSectionsGamma`, which is locally
> bijective by `AlgebraicGeometry.BigFppfOver.isIso_baseSheafification_map_smallEtaleSectionsGamma`.
>
> The topology `τ` is one refining the étale topology: that is the range `τ ∈ {étale, smooth,
> syntomic, fppf}` over which the source states this clause, the Zariski topology being excluded
> there.  By
> `AlgebraicGeometry.BigFppfOver.isContinuous_smallEtaleToFppf_of_etaleTopology_le` that single
> hypothesis also supplies the continuity of the inclusion of the small étale site, i.e. the
> existence of `id_{τ,étale}`, so the instance argument below is never an extra assumption: it is
> discharged at each of the four `τ`, and nothing discharges it at `τ = Zariski`, which is exactly
> why the source excludes that one.  `AlgebraicGeometry.BigFppfOver.baseSmallEtaleIsoSectionsEtale`
> and `AlgebraicGeometry.BigFppfOver.baseSmallEtaleIsoSectionsFppf` are the hypothesis-free
> instances at `τ = étale` and `τ = fppf`; `.baseSmallEtaleIsoSectionsSmooth` and
> `.baseSmallEtaleIsoSectionsSyntomic`, in
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigToSmallEtale.lean`, are the
> other two.

```lean
public noncomputable def baseSmallEtalePullbackIsoSectionsSheafification
    (hτ : B.etaleTopology ≤ B.baseTopology τ) :
    (smallEtaleToBaseModulePullback B S hS τ).obj 𝓖 ≅
      (PresheafOfModules.sheafification.{u}
          (𝟙 (FibredSite.baseRingStructureSheaf B S hS τ).obj)).obj
        (smallEtaleSectionsPresheafOfModules B S hS τ 𝓖)
```

**`AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoPullbackSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SectionsPullbackComparison/ArbitraryModule/LocalInjectivity.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SectionsPullbackComparison/ArbitraryModule/LocalInjectivity.lean#L427). The attribute's comment: “part (1)”.

> **Stacks 070S (1).**  Let `F` be an arbitrary sheaf of `𝒪_S`-modules.  For each of the five
> topologies `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, the pullback of `F` along the
> morphism of ringed sites `id_{τ,Zar} : ((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪_S)` is the
> `τ`-sheafification of the presheaf `(f : T → S) ↦ Γ(T, f^*F)` on `(Sch/S)_τ`.
>
> The pullback is `AlgebraicGeometry.BigFppfOver.baseAssociatedModule`, presented by
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleSheafificationIso` as the
> `τ`-sheafification of the pullback of presheaves of modules; the presheaf of sections is
> `AlgebraicGeometry.BigFppfOver.pullbackSectionsPresheaf`; and the identification is the
> `τ`-sheafification of the comparison
> `AlgebraicGeometry.BigFppfOver.pullbackSectionsComparison`, which is locally surjective and
> locally injective for every `τ`
> (`AlgebraicGeometry.BigFppfOver.isLocallySurjective_pullbackSectionsComparison` and
> `AlgebraicGeometry.BigFppfOver.isLocallyInjective_pullbackSectionsComparison`).

```lean
public noncomputable def baseAssociatedModuleIsoPullbackSections (τ : SiteKind)
    (F : S.Modules) :
    (baseAssociatedModule B S hS τ).obj F ≅
      (PresheafOfModules.sheafification.{u}
          (𝟙 (FibredSite.baseRingStructureSheaf B S hS τ).obj)).obj
        (pullbackSectionsPresheaf B S hS F)
```

**`AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SectionsPullbackComparison/Comparison.lean, line 1073](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SectionsPullbackComparison/Comparison.lean#L1073). The attribute's comment: “part (1)”.

> For each of the five topologies `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, the
> associated module of a quasi-coherent module `F` on `S` — the pullback along the morphism of
> ringed sites `id_{τ,Zar} : ((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪_S)` — is the `τ`-sheafification of the
> pullback-sections presheaf `(f : T → S) ↦ Γ(T, f⁺F)` of Stacks 03DS.
>
> This is `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleSheafificationIso` at `F`, which
> presents the associated module as the `τ`-sheafification of the presheaf-level pullback, followed
> by the `τ`-sheafification of `AlgebraicGeometry.BigFppfOver.sectionsComparison`.

```lean
public noncomputable def baseAssociatedModuleIsoSections (τ : SiteKind) (F : S.Modules)
    [F.IsQuasicoherent] :
    (baseAssociatedModule B S hS τ).obj F ≅
      (PresheafOfModules.sheafification.{u}
          (𝟙 (FibredSite.baseRingStructureSheaf B S hS τ).obj)).obj
        (sectionsPresheafOfModules B S hS F)
```

## Tag 03FH, a remark

[Tag 03FH](https://stacks.math.columbia.edu/tag/03FH) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.associatedModuleBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleMorphismBaseChange.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleMorphismBaseChange.lean#L388). The attribute's comment: “part (2), for the morphism f_small : X_étale → Y_étale of Stacks 070R (2)”.

> **The associated module of a pullback is the pullback of the associated module.**  For
> `a : X ⟶ Y` a morphism of schemes of the big étale site, with `r` the underlying morphism of
> schemes and `ε_a` the morphism of ringed sites of Stacks 070R (2),
>
> `(r^*𝓕)^a ≅ ε_a^*(𝓕^a)`,
>
> naturally in the `𝒪_Y`-module `𝓕`, with no quasi-coherence hypothesis.  This **is Stacks 03LC
> part (1) at `τ = étale`**, for the small étale sites of two schemes and a morphism between them:
> the equivalence of Stacks 03DX (2) at `τ = étale` is compatible with pullback.  It is proved
> here for arbitrary modules, not only quasi-coherent ones.
>
> Each side is a composite of two pullbacks of sheaves of modules round the square of ringed sites
> whose geometric half is `AlgebraicGeometry.SmallEtale.baseChangeOpensIso` and whose ring half is
> `AlgebraicGeometry.SmallEtale.structureMap_comp_baseChangeOpensIso`, so the two agree because a
> left adjoint is determined by its right adjoint.
>
> **This also carries Stacks 03FH (2)** for the morphism `f_{small} : X_étale ⟶ Y_étale` of
> Remark 070R (2): that clause asserts `(f^*𝓕)^a = f_{sites}^*𝓕^a` for every `f_{sites}` of
> Remark 070R, and this is the small étale one.  The big fppf one is
> `AlgebraicGeometry.BigFppfOver.associatedModuleBigPullbackIso`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigFppf.lean`); the big Zariski,
> étale, smooth and syntomic ones are
> `AlgebraicGeometry.BigFppfOver.associatedModuleBasePullbackIso`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean`), and the small
> Zariski one is `AlgebraicGeometry.SmallZariski.lcAssociatedModulePullbackIso`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiPushforwardSquare.lean:458`).
> (It was formerly cited as `AlgebraicGeometry.SmallZariski.associatedModulePullbackIso`, which
> states the commutation over the *identity reading* of `𝓕 ↦ 𝓕^a` and is a tautology about `𝟭`;
> that declaration is untagged, and naming it here made this enumeration a false completeness
> claim.)
> Those are every `f_sites` the enumeration of Remark 070R lists; the mixed-topology entries
> `(Sch/X)_τ ⟶ (Sch/Y)_{τ'}` with `τ ≠ τ'` of the Topologies, Section 03FE list that the remark's
> opening sentence also covers are not claimed.

```lean
public def associatedModuleBaseChangeIso :
    Scheme.Modules.pullback (schemeHom B a) ⋙ associatedModule B X.obj X.property ≅
      associatedModule B Y.obj Y.property ⋙
        SheafOfModules.pullback.{u} (smallEtaleStructureMapRing B a)
```

**`AlgebraicGeometry.SmallEtale.associatedModuleIsoOfSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleSectionsIso.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleSectionsIso.lean#L151). The attribute's comment: “part (1), for the morphism id_{small, étale, Zar} : (S_étale, 𝒪) → (S_Zar, 𝒪)”.

> **The two constructions of `𝓕^a` on the small étale site agree**: the pullback of `𝓕` along
> the morphism of ringed sites `id_{small, étale, Zar} : (S_étale, 𝒪) → (S_Zar, 𝒪_S)`,
> `AlgebraicGeometry.SmallEtale.associatedModule`, is the sheaf
> `AlgebraicGeometry.SmallEtale.associatedModuleOfSections` whose sections over an object
> `f : T → S` of `S_étale` are `Γ(T, f^*𝓕)`.
>
> This is the content of [Stacks, Remark 03FH] (1) on the small étale site: [Stacks, Tag 03DU] (4)
> defines `𝓕^a` by its sections, and the remark observes that it is the pullback along
> `id_{small, étale, Zar}`.  It is [Stacks, Tag 070S] (2) in the object form
> `AlgebraicGeometry.SmallEtale.associatedModuleIsoSections`, followed by the removal of the
> sheafification, `AlgebraicGeometry.SmallEtale.sheafificationIsoAssociatedModuleOfSections`.
>
> **This carries [Stacks, Remark 03FH] (1) for the second of the two morphisms that clause
> offers**, `id_{small, étale, Zar} : (S_étale, 𝒪) → (S_Zar, 𝒪_S)`.  Its `τ = Zariski` counterpart
> is `AlgebraicGeometry.SmallZariski.associatedModuleIsoOfSections`.  The first morphism of the
> clause, `id_{τ, Zar} : ((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪)`, is carried at all five `τ` by
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSectionsSheaf`
> (`StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean`),
> which identifies the pullback with the sections-defined `𝓕^a` of [Stacks, Tag 03DU] (3), the
> big-site sheafification being removed by [Stacks, Tag 03DT] exactly as it is removed here;
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSections`
> (`StacksFrontier/AlgebraicGeometry/Descent/SectionsPullbackComparison/Comparison.lean`) is its
> [Stacks, Tag 070S] (1) half, before that removal.  The two morphisms together are the whole of
> clause (1).
>
> The quasi-coherence hypothesis is not an addition to 03FH: the construction `𝓕 ↦ 𝓕^a` whose two
> descriptions the remark identifies is [Stacks, Tag 03DU] (4), which is stated for a
> quasi-coherent `𝒪_S`-module.

```lean
public noncomputable def associatedModuleIsoOfSections :
    (associatedModule B S hS).obj F ≅ associatedModuleOfSections B S hS F
```

**`AlgebraicGeometry.SmallZariski.lcAssociatedModulePullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiPushforwardSquare.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiPushforwardSquare.lean#L464). The attribute's comment: “part (2), for the morphism f_small : (T_Zar, 𝒪_T) → (S_Zar, 𝒪_S) of Stacks 070R (2), for the associated-module functor of Definition 03DU (4)”.

> **Stacks 03LC part (1) at `τ = Zariski`, for the small Zariski sites.**  The equivalence of
> Stacks 03DX (2) at `τ = Zariski` is compatible with pullback: for `f : T ⟶ S` a morphism of
> schemes of the big Zariski site, with `f_small : (T_Zar, 𝒪) ⟶ (S_Zar, 𝒪)` the morphism of ringed
> sites of Stacks 070R (2) and `𝓖` an `𝒪_S`-module,
>
>     `(f^*𝓖)^a ≅ f_small^*(𝓖^a)`,
>
> naturally in `𝓖` and with no quasi-coherence hypothesis.
>
> Here `𝓖 ↦ 𝓖^a` is `AlgebraicGeometry.SmallZariski.associatedModule`, the functor of
> Definition 03DU (4) at `τ = Zariski` over the structure sheaf `T/S ↦ Γ(T, 𝒪_T)` of the small
> Zariski site — not the identity reading introduced in
> `StacksFrontier.AlgebraicGeometry.Descent.AssociatedModule.SmallZariskiFullyFaithful`.  That
> distinction is what gives this declaration its content.
> `AlgebraicGeometry.SmallZariski.associatedModulePullbackIso` states the corresponding
> commutation over the identity reading, and it does **not** state this clause: the identity
> reading is pullback along the identity morphism of ringed sites, isomorphic to `𝟭`, so that
> statement reads `f_small^* ⋙ 𝟭 ≅ 𝟭 ⋙ f_small^*` and is proved by whiskering the two unit
> isomorphisms and applying the two unitors, never touching the coefficient sheaf
> `T/S ↦ Γ(T, 𝒪_T)` that clause (2) is about.  It is accordingly untagged.
>
> The proof is `SheafOfModules.pullbackSquareIso`, Stacks 03D8 for a square: the geometric half of
> the square is `AlgebraicGeometry.SmallZariski.lcBaseChangeOpensIso`, that the base change of the
> object chosen over an open `V` of `S` is the object chosen over `f⁻¹(V)`, and the ring half is
> `AlgebraicGeometry.SmallZariski.lcStructureMap_comp_baseChangeOpensIso`.
>
> **This is also Stacks 03FH part (2)** for the small Zariski `f_small` of Remark 070R (2).  That
> clause asserts `(f^*𝓕)^a = f_sites^*𝓕^a` for every `f_sites` the enumeration of Remark 070R
> lists, and the two clauses coincide at this `f_sites`: both are the statement that the
> associated-module functor of Definition 03DU (4) at `τ = Zariski` commutes with pullback along
> the morphism of ringed small Zariski sites of Stacks 070R (2).  The companions are
> `AlgebraicGeometry.BigFppfOver.associatedModuleBasePullbackIso` — which carries the same two
> clauses on one declaration — for the big site at each of the five topologies, and
> `AlgebraicGeometry.SmallEtale.associatedModuleBaseChangeIso` for the small étale `f_small`.
> Those are every `f_sites` of the enumeration; the mixed-topology entries
> `(Sch/X)_τ ⟶ (Sch/Y)_{τ'}` with `τ ≠ τ'` of Topologies, Section 03FE are not claimed.

```lean
public noncomputable def lcAssociatedModulePullbackIso :
    Scheme.Modules.pullback (lcSchemeHom B f) ⋙ associatedModule B T.1 T.property ≅
      associatedModule B S.1 S.property ⋙
        SheafOfModules.pullback.{u} (lcStructureMapRing B f)
```

**`AlgebraicGeometry.SmallZariski.lcAssociatedModuleObjPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiPushforwardSquare.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiPushforwardSquare.lean#L479). The attribute's comment: “part (2) at one module, for the morphism f_small of the small Zariski sites and the associated-module functor of Definition 03DU (4)”.

> **Stacks 03FH part (2) at one module**, and equally **Stacks 03LC part (1) at `τ = Zariski`
> at one module**: `(f^*𝓕)^a ≅ f_small^*(𝓕^a)` for the morphism `f_small` of the small Zariski
> sites of Stacks 070R (2) and the associated-module functor of Definition 03DU (4).  This is the
> form in which Stacks 03FH states its clause, read off from
> `AlgebraicGeometry.SmallZariski.lcAssociatedModulePullbackIso`.

```lean
public noncomputable def lcAssociatedModuleObjPullbackIso (𝓖 : (S.1).Modules) :
    (associatedModule B T.1 T.property).obj
        ((Scheme.Modules.pullback (lcSchemeHom B f)).obj 𝓖) ≅
      (SheafOfModules.pullback.{u} (lcStructureMapRing B f)).obj
        ((associatedModule B S.1 S.property).obj 𝓖)
```

**`AlgebraicGeometry.SmallZariski.associatedModuleIsoOfSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsIso.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsIso.lean#L481). The attribute's comment: “part (1), for the morphism id_{small, Zariski, Zar} : (S_Zar, 𝒪) → (S_Zar, 𝒪_S)”.

> **The two constructions of `𝓕ᵃ` on the small Zariski site agree**: the pullback of `𝓕` along
> the morphism of ringed sites `(S_Zar, 𝒪) → (S_Zar, 𝒪_S)`,
> `AlgebraicGeometry.SmallZariski.associatedModule`, is the sheaf
> `AlgebraicGeometry.SmallZariski.associatedModuleOfSections` whose sections over an object
> `f : T → S` of `S_Zar` are `Γ(T, f^*𝓕)`.
>
> This is the content of [Stacks, Remark 03FH] (1) on the small Zariski site: [Stacks, Tag 03DU]
> (4) defines `𝓕ᵃ` by its sections, and the remark observes that it is the pullback along
> `id_{small, Zar, Zar}`.  At `τ = Zariski` that morphism of ringed sites is an equivalence, so
> `AlgebraicGeometry.SmallZariski.restrictModule` is fully faithful and the identification follows
> from the two isomorphisms `𝓕 ≅ f_*f^*𝓕`
> (`AlgebraicGeometry.SmallZariski.restrictAssociatedModuleIso`) and `𝓕 ≅ f_*(𝓕ᵃ)`
> (`AlgebraicGeometry.SmallZariski.sectionsUnitIso`); no sheafification argument is needed, where
> `τ = étale` needs [Stacks, Tag 070S] (2).
>
> **This carries [Stacks, Remark 03FH] (1) at `τ = Zariski` for the second of the two morphisms
> that clause offers**, `id_{small, Zar, Zar} : (S_Zar, 𝒪) → (S_Zar, 𝒪_S)`.  Its `τ = étale`
> counterpart is `AlgebraicGeometry.SmallEtale.associatedModuleIsoOfSections`, and the first
> morphism of the clause, `id_{τ, Zar} : ((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪)`, is carried at all five `τ`
> by `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSections`.
>
> The quasi-coherence hypothesis is not an added hypothesis of 03FH: the construction `𝓕 ↦ 𝓕ᵃ`
> whose two descriptions the remark identifies is [Stacks, Tag 03DU] (4), which is stated for a
> quasi-coherent `𝒪_S`-module.

```lean
public noncomputable def associatedModuleIsoOfSections :
    (associatedModule B S hS).obj F ≅ associatedModuleOfSections B S hS F
```

**`AlgebraicGeometry.BigFppfOver.associatedModuleBigPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigFppf.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigFppf.lean#L280). The attribute's comment: “part (2), for the morphism of big fppf sites f_big of Stacks 070R”.

> **Stacks 03FH, part (2), for the morphism of big fppf sites
> `f_big : ((Sch/X)_fppf, 𝒪_X) ⟶ ((Sch/Y)_fppf, 𝒪_Y)` of Stacks 070R.**  The associated module of
> a pullback is the pullback of the associated module, `(f^*𝓕)^a ≅ f_{big}^*(𝓕^a)`.
>
> No hypothesis: the morphism of ringed sites is
> `AlgebraicGeometry.BigFppfOver.baseChange` together with
> `AlgebraicGeometry.BigFppfOver.structureComparison`, both available, and the two provisos of
> `SheafOfModules.pullbackSquareIso` are
> `AlgebraicGeometry.BigFppfOver.opensBaseChangeIso` and
> `AlgebraicGeometry.BigFppfOver.comparisonComp_opensBaseChangeIso`.
>
> Only the fppf `f_big` is claimed here.  Stacks 03FH (2) ranges over every morphism of ringed
> sites `f_{sites}` of Remark 070R; the other morphisms that remark enumerates are claimed
> elsewhere — `f_big` at the other four topologies by
> `AlgebraicGeometry.BigFppfOver.associatedModuleBasePullbackIso`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean`, which is this
> construction read at a variable topology), the small étale `f_small` by
> `AlgebraicGeometry.SmallEtale.associatedModuleBaseChangeIso` and the small Zariski `f_small` by
> `AlgebraicGeometry.SmallZariski.lcAssociatedModulePullbackIso`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiPushforwardSquare.lean:458`).
> (The last was formerly cited as
> `AlgebraicGeometry.SmallZariski.associatedModulePullbackIso`, which states the commutation over
> the *identity reading* of `𝓕 ↦ 𝓕^a` and is a tautology about `𝟭`; it is untagged, and naming it
> here made this enumeration a false completeness claim.)

```lean
public noncomputable def associatedModuleBigPullbackIso :
    Scheme.Modules.pullback f ⋙ associatedModule B X hX ≅
      associatedModule B Y hY ⋙
        SheafOfModules.pullback.{u} (structureComparison B hX hY f)
```

**`AlgebraicGeometry.BigFppfOver.associatedModuleBigObjPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigFppf.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigFppf.lean#L290). The attribute's comment: “part (2) at one module, for the morphism of big fppf sites f_big”.

> **Stacks 03FH, part (2), at one module**: `(f^*𝓕)^a ≅ f_{big}^*(𝓕^a)`.

```lean
public noncomputable def associatedModuleBigObjPullbackIso (𝓕 : Y.Modules) :
    (associatedModule B X hX).obj ((Scheme.Modules.pullback f).obj 𝓕) ≅
      (SheafOfModules.pullback.{u} (structureComparison B hX hY f)).obj
        ((associatedModule B Y hY).obj 𝓕)
```

**`AlgebraicGeometry.BigFppfOver.associatedModuleBasePullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean#L220). The attribute's comment: “part (2), for the morphism of big sites f_big : ((Sch/X)_τ, 𝒪_X) → ((Sch/Y)_τ, 𝒪_Y) of Stacks 070R (1), at each of τ = Zariski, étale, smooth, syntomic, fppf”.

> **Stacks 03FH, part (2), for the morphism of big sites
> `f_big : ((Sch/X)_τ, 𝒪_X) ⟶ ((Sch/Y)_τ, 𝒪_Y)` of Stacks 070R (1), at each of the five
> topologies `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  The associated module of a
> pullback is the pullback of the associated module, `(f^*𝓕)^a ≅ f_big^*(𝓕^a)`, naturally in the
> `𝒪_Y`-module `𝓕`.
>
> No hypothesis: the morphism of ringed sites is `AlgebraicGeometry.BigFppfOver.baseChange`
> together with `AlgebraicGeometry.BigFppfOver.baseStructureComparison`, and the two provisos of
> `SheafOfModules.pullbackSquareIso` are
> `AlgebraicGeometry.BigFppfOver.opensBaseChangeIso`, which is topology-free, and
> `AlgebraicGeometry.BigFppfOver.comparisonComp_baseOpensBaseChangeIso`.
>
> Together with
> `AlgebraicGeometry.SmallEtale.associatedModuleBaseChangeIso` (the small étale `f_small`) and
> `AlgebraicGeometry.SmallZariski.lcAssociatedModulePullbackIso` (the small Zariski `f_small`,
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiPushforwardSquare.lean:458`)
> this is every `f_sites` the enumeration of Remark 070R lists: clause (1) of that remark gives
> the big site at each of these five topologies, and clause (2) the small site at the two
> topologies that have one.  (The small Zariski entry was formerly cited as
> `AlgebraicGeometry.SmallZariski.associatedModulePullbackIso`, which states the commutation over
> the *identity reading* of `𝓕 ↦ 𝓕^a` and is a tautology about `𝟭`; it is untagged, and naming it
> here made this enumeration a false completeness claim.)

```lean
public noncomputable def associatedModuleBasePullbackIso :
    Scheme.Modules.pullback f ⋙ baseAssociatedModule B X hX τ ≅
      baseAssociatedModule B Y hY τ ⋙
        SheafOfModules.pullback.{u} (baseStructureComparison B hX hY f τ)
```

**`AlgebraicGeometry.BigFppfOver.associatedModuleBaseObjPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackBigSites.lean#L237). The attribute's comment: “part (2) at one module, for the morphism of big sites f_big at each of τ = Zariski, étale, smooth, syntomic, fppf”.

> **Stacks 03FH, part (2), at one module**: `(f^*𝓕)^a ≅ f_big^*(𝓕^a)` for the morphism of big
> sites `f_big` at each of the five topologies, read off from
> `AlgebraicGeometry.BigFppfOver.associatedModuleBasePullbackIso`.

```lean
public noncomputable def associatedModuleBaseObjPullbackIso (𝓕 : Y.Modules) :
    (baseAssociatedModule B X hX τ).obj ((Scheme.Modules.pullback f).obj 𝓕) ≅
      (SheafOfModules.pullback.{u} (baseStructureComparison B hX hY f τ)).obj
        ((baseAssociatedModule B Y hY τ).obj 𝓕)
```

**`AlgebraicGeometry.BigFppfSite.associatedModuleBigBaseChangeRingedSiteHomPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean#L324). The attribute's comment: “part (2), for the morphism of ringed sites f_big : ((Sch/T)_τ, 𝒪_T) → ((Sch/S)_τ, 𝒪_S) of Stacks 070R (entries (1), (6), (10), (13), (15) of Stacks 03FE), at the registered morphism bigBaseChangeRingedSiteHom, for each of the five topologies: (f^*𝓕)^a ≅ f_big^*(𝓕^a), naturally in 𝓕”.

> **Stacks 03FH, part (2), for the morphism of ringed sites
> `f_big : ((Sch/T)_τ, 𝒪_T) ⟶ ((Sch/S)_τ, 𝒪_S)` of Remark 070R** — entries (1), (6), (10), (13),
> (15) of the Topologies, Section 03FE list — at its registered form
> `AlgebraicGeometry.BigFppfSite.bigBaseChangeRingedSiteHom`, for each of the five topologies:
>
> `(f^*𝓕)^a ≅ f_big^*(𝓕^a)`,
>
> naturally in the `𝒪_S`-module `𝓕`, where `f_big^*` is the pullback along that single morphism
> and `(-)^a` is the pullback along `id_{τ, Zar}`
> (`AlgebraicGeometry.BigFppfSite.carriedOverToZariskiRingedSiteHom`), as in clause (1).  Nothing
> is assumed of `𝓕`.
>
> The proof is the source's: by Lemma 03D8 both sides are pullbacks along a composite morphism
> `(Sch/T)_τ ⟶ S_Zar`, namely `f_small ∘ id_{τ, Zar}` and `id_{τ, Zar} ∘ f_big`, and these have
> isomorphic functors, `V ↦ f⁻¹(V)` and `V ↦ T ×_S V`, compatibly with the structure maps.

```lean
public def associatedModuleBigBaseChangeRingedSiteHomPullbackIso (τ : CoveringTopology)
    (f : B.obj hT ⟶ B.obj hS) :
    Scheme.Modules.pullback f.hom ⋙
        (B.carriedOverToZariskiRingedSiteHom T hT τ).pullbackModulesGeneral ≅
      (B.carriedOverToZariskiRingedSiteHom S hS τ).pullbackModulesGeneral ⋙
        (B.bigBaseChangeRingedSiteHom τ f).pullbackModulesGeneral
```

**`AlgebraicGeometry.BigFppfSite.associatedModuleBigRingedSiteHomPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean#L404). The attribute's comment: “part (2), for the morphisms of ringed sites f_sites : ((Sch/T)_τ, 𝒪_T) → ((Sch/S)_τ', 𝒪_S) of Stacks 070R, entries (1)-(15) of the Stacks 03FE list (τ finer than τ'), at the registered morphism bigRingedSiteHom: (f^*𝓕)^a ≅ f_sites^*(𝓕^a), naturally in 𝓕”.

> **Stacks 03FH, part (2), for the morphisms of ringed sites
> `f_sites : ((Sch/T)_τ, 𝒪_T) ⟶ ((Sch/S)_{τ'}, 𝒪_S)` of Remark 070R** — entries (1)–(15) of the
> Topologies, Section 03FE list, one for each pair with `τ` finer than `τ'` — at their registered
> form `AlgebraicGeometry.BigFppfSite.bigRingedSiteHom`:
>
> `(f^*𝓕)^a ≅ f_sites^*(𝓕^a)`,
>
> naturally in the `𝒪_S`-module `𝓕`, where `f_sites^*` is the pullback along that single morphism
> and `(-)^a` is the pullback along `id_{τ, Zar}`, as in clause (1).  The hypothesis is Section
> 03FE's own condition for the entry to be on its list; nothing is assumed of `𝓕`.
>
> The registered morphism is `id_{τ, τ'} ∘ f_big`, so by Lemma 03D8 its pullback is
> `id_{τ, τ'}^*` followed by `f_big^*`, and
> `AlgebraicGeometry.BigFppfSite.associatedModuleBigBaseChangeRingedSiteHomPullbackIso` together
> with `AlgebraicGeometry.BigFppfSite.idRingedSiteHomPullbackIso` finishes.

```lean
public def associatedModuleBigRingedSiteHomPullbackIso {τ τ' : CoveringTopology} (h : τ.IsFiner τ')
    (f : B.obj hT ⟶ B.obj hS) :
    Scheme.Modules.pullback f.hom ⋙
        (B.carriedOverToZariskiRingedSiteHom T hT τ).pullbackModulesGeneral ≅
      (B.carriedOverToZariskiRingedSiteHom S hS τ').pullbackModulesGeneral ⋙
        (B.bigRingedSiteHom h f).pullbackModulesGeneral
```

**`AlgebraicGeometry.BigFppfSite.associatedModuleBigToSmallEtaleRingedSiteHomPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean#L435). The attribute's comment: “part (2), for the morphisms of ringed sites f_sites : ((Sch/T)_τ, 𝒪_T) → (S_étale, 𝒪_S) of Stacks 070R, entries (16)-(19) of the Stacks 03FE list, at the registered morphism bigToSmallEtaleRingedSiteHom: (f^*𝓕)^a ≅ f_sites^*(𝓕^a), naturally in 𝓕”.

> **Stacks 03FH, part (2), for the morphisms of ringed sites
> `f_sites : ((Sch/T)_τ, 𝒪_T) ⟶ (S_étale, 𝒪_S)` of Remark 070R** — entries (16)–(19) of the
> Topologies, Section 03FE list, `τ ∈ {étale, smooth, syntomic, fppf}` — at their registered form
> `AlgebraicGeometry.BigFppfSite.bigToSmallEtaleRingedSiteHom`:
>
> `(f^*𝓕)^a ≅ f_sites^*(𝓕^a)`,
>
> naturally in the `𝒪_S`-module `𝓕`, with `𝓕^a` the associated module of the small étale site of
> `S` and `(f^*𝓕)^a` that of the big `τ`-site of `T`.  The hypothesis, `τ` finer than the étale
> topology, is Section 03FE's condition for the entry to be on its list.
>
> The registered morphism is `π_S ∘ f_sites` with `f_sites : (Sch/T)_τ ⟶ (Sch/S)_étale`; Lemma 03D8
> reduces the clause to that for `f_sites`,
> `AlgebraicGeometry.BigFppfSite.associatedModuleBigRingedSiteHomPullbackIso`, and to
> `AlgebraicGeometry.BigFppfSite.smallEtalePiRingedSiteHomPullbackIso`.

```lean
public def associatedModuleBigToSmallEtaleRingedSiteHomPullbackIso {τ : CoveringTopology}
    (h : τ.IsFiner .etale) (f : B.obj hT ⟶ B.obj hS) :
    Scheme.Modules.pullback f.hom ⋙
        (B.carriedOverToZariskiRingedSiteHom T hT τ).pullbackModulesGeneral ≅
      SmallEtale.associatedModule B.toBigEtaleSite S hS ⋙
        (B.bigToSmallEtaleRingedSiteHom h f).pullbackModulesGeneral
```

**`AlgebraicGeometry.BigFppfSite.associatedModuleBigToSmallZariskiRingedSiteHomPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackChangeOfTopologies.lean#L466). The attribute's comment: “part (2), for the morphisms of ringed sites f_sites : ((Sch/T)_τ, 𝒪_T) → (S_Zar, 𝒪_S) of Stacks 070R, entries (20)-(24) of the Stacks 03FE list, at the registered morphism bigToSmallZariskiRingedSiteHom: (f^*𝓕)^a ≅ f_sites^*(𝓕^a), naturally in 𝓕”.

> **Stacks 03FH, part (2), for the morphisms of ringed sites
> `f_sites : ((Sch/T)_τ, 𝒪_T) ⟶ (S_Zar, 𝒪_S)` of Remark 070R** — entries (20)–(24) of the
> Topologies, Section 03FE list, one for each of the five topologies — at their registered form
> `AlgebraicGeometry.BigFppfSite.bigToSmallZariskiRingedSiteHom`:
>
> `(f^*𝓕)^a ≅ f_sites^*(𝓕^a)`,
>
> naturally in the `𝒪_S`-module `𝓕`, with `𝓕^a` the associated module of the small Zariski site
> of `S` and `(f^*𝓕)^a` that of the big `τ`-site of `T`.  The hypothesis holds at every `τ`
> (`AlgebraicGeometry.BigFppfSite.isFiner_zariski`).
>
> The registered morphism is `π_S ∘ f_sites` with `f_sites : (Sch/T)_τ ⟶ (Sch/S)_Zar`; Lemma 03D8
> reduces the clause to that for `f_sites`,
> `AlgebraicGeometry.BigFppfSite.associatedModuleBigRingedSiteHomPullbackIso`, and to
> `AlgebraicGeometry.BigFppfSite.smallZariskiPiRingedSiteHomPullbackIso`.

```lean
public def associatedModuleBigToSmallZariskiRingedSiteHomPullbackIso {τ : CoveringTopology}
    (h : τ.IsFiner .zariski) (f : B.obj hT ⟶ B.obj hS) :
    Scheme.Modules.pullback f.hom ⋙
        (B.carriedOverToZariskiRingedSiteHom T hT τ).pullbackModulesGeneral ≅
      SmallZariski.associatedModule B.toBigZariskiSite S hS ⋙
        (B.bigToSmallZariskiRingedSiteHom h f).pullbackModulesGeneral
```

**`AlgebraicGeometry.SmallEtale.associatedModuleSmallEtaleToSmallZariskiPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackToSmallZariski.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackToSmallZariski.lean#L320). The attribute's comment: “part (2), for the morphism of ringed sites f_sites : (X_étale, 𝒪_X) → (Y_Zar, 𝒪_Y) of Stacks 070R — entry (26) of the Stacks 03FE list: (f^*𝓕)^a ≅ f_sites^*𝓕, naturally in 𝓕, the 𝓕^a of the target being 𝓕 because the target is (Y_Zar, 𝒪_Y) itself”.

> **Stacks 03FH, part (2), for the morphism of ringed sites
> `f_sites : (X_étale, 𝒪_X) ⟶ (Y_Zar, 𝒪_Y)` of Remark 070R** — entry (26) of the list of
> Topologies, Section 03FE, the one mixed pair of small sites.  The associated module of a pullback
> is the pullback of the associated module,
>
> `(f^*𝓕)^a ≅ f_sites^*𝓕`,
>
> naturally in the `𝒪_Y`-module `𝓕`, with `(f^*𝓕)^a` the associated module on the small étale site
> of `X`.  As for entries (20) to (24) the target of `f_sites` is `(Y_Zar, 𝒪_Y)` itself, so the
> `𝓕^a` of the source's formulation is `𝓕`.
>
> There is no hypothesis: the étale topology is finer than the Zariski one, which is Section 03FE's
> condition for this entry to be on its list.  Nothing is assumed of `𝓕`, and nothing of the
> morphism beyond `X` and `Y` lying in the chosen big étale site.
>
> `f_sites` is the registered
> `AlgebraicGeometry.smallEtaleToSmallZariskiRingedSiteHom`, Section 03FE's factorization
>
> `X_étale --f_small--> Y_étale --id_{small,étale,Zar}--> Y_Zar`,
>
> and `f_sites^*` is the pullback of sheaves of modules along that single morphism of ringed sites.
> The proof is the source's: Lemma 03D8 splits it as `f_small^*` followed by
> `id_{small,étale,Zar}^*`, the second of which is the associated-module functor of the small étale
> site by `AlgebraicGeometry.SmallEtale.pullbackToposGeneral_toZariskiRingedToposHom`, and the
> clause for `f_small` on the small étale sites — entry (25) —
> `AlgebraicGeometry.SmallEtale.associatedModuleBaseChangeIso`, finishes.

```lean
public def associatedModuleSmallEtaleToSmallZariskiPullbackIso :
    Scheme.Modules.pullback (SmallEtale.schemeHom B a) ⋙
        SmallEtale.associatedModule B X.obj X.property ≅
      (smallEtaleToSmallZariskiRingedSiteHom B a).pullbackModulesGeneral
```

**`AlgebraicGeometry.SmallEtale.associatedModuleSmallEtaleToSmallZariskiObjPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackToSmallZariski.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModulePullbackToSmallZariski.lean#L334). The attribute's comment: “part (2) at one module, for the morphism of ringed sites f_sites : (X_étale, 𝒪_X) → (Y_Zar, 𝒪_Y) of Stacks 070R — entry (26) of the Stacks 03FE list”.

> **Stacks 03FH, part (2), at one module**, for the morphism of ringed sites
> `f_sites : (X_étale, 𝒪_X) ⟶ (Y_Zar, 𝒪_Y)` of Remark 070R — entry (26) of the Section 03FE list:
> `(f^*𝓕)^a ≅ f_sites^*𝓕`, read off from
> `AlgebraicGeometry.SmallEtale.associatedModuleSmallEtaleToSmallZariskiPullbackIso`.

```lean
public def associatedModuleSmallEtaleToSmallZariskiObjPullbackIso (𝓕 : Y.obj.Modules) :
    (SmallEtale.associatedModule B X.obj X.property).obj
        ((Scheme.Modules.pullback (SmallEtale.schemeHom B a)).obj 𝓕) ≅
      (smallEtaleToSmallZariskiRingedSiteHom B a).pullbackModulesGeneral.obj 𝓕
```

**`AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSectionsSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean#L583). The attribute's comment: “part (1) for the first of the two morphisms of ringed sites that clause offers, id_{τ, Zar} : ((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪), on the big site (Sch/S)_τ at each of the five τ: the construction 𝓕 ↦ 𝓕^a of Definition 03DU (3), the sheaf of sections (f : T → S) ↦ Γ(T, f^*𝓕), is the pullback under that morphism”.

> **Stacks 03FH (1) on the big sites.**  The construction `𝓕 ↦ 𝓕^a` of Definition 03DU (3) —
> the sheaf on `(Sch/S)_τ` whose value at `f : T → S` is `Γ(T, f^*𝓕)` — **is** the pullback of
> `𝓕` under the morphism of ringed sites
> `id_{τ, Zar} : ((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪)`, at each of the five
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.
>
> **No sheafification is left in the statement.**  Two inputs compose.  Stacks 070S (1),
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSections`, presents the pullback as the
> `τ`-sheafification of the pullback-sections presheaf of modules of Stacks 03DS; and Stacks 03DT
> on the five big sites,
> `AlgebraicGeometry.BigFppfOver.isSheaf_sectionsPresheafOfModules_baseOverTopology`, says that for
> a quasi-coherent `𝓕` that presheaf is **already** a `τ`-sheaf — it is what
> `AlgebraicGeometry.BigFppfOver.sectionsSheafOfModules` packages.  So the counit of
> `CategoryTheory.PresheafOfModules.sheafificationAdjunction` is invertible there and removes the
> sheafification, which is the step that turns 070S (1) into the remark's own identification with
> `𝓕^a` itself.
>
> **The right-hand side is `𝓕^a` as Definition 03DU (3) defines it**, by its sections: the
> underlying presheaf of modules of `AlgebraicGeometry.BigFppfOver.sectionsSheafOfModules` is
> `AlgebraicGeometry.BigFppfOver.sectionsPresheafOfModules`, the presheaf of Stacks 03DS, and at
> `τ = fppf` the packaging is the tagged clause-(3) definition
> `AlgebraicGeometry.overAssociatedModule` on the nose —
> `AlgebraicGeometry.BigFppfOver.overAssociatedModule_fppf`, in
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/OverAssociatedModuleIso.lean`, which is
> `rfl`.
>
> **What the other 03FH registrations carry.**  Clause (1) of the remark offers two morphisms.
> This is the first of them, `id_{τ, Zar}`, on the big site, at all five `τ`; the second,
> `id_{small, étale, Zar} : (S_étale, 𝒪) → (S_Zar, 𝒪)`, is
> `AlgebraicGeometry.SmallEtale.associatedModuleIsoOfSections`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleSectionsIso.lean`), with the
> small Zariski reading in
> `AlgebraicGeometry.SmallZariski.associatedModuleIsoOfSections`.  The two together are the whole
> of clause (1).  `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSections` is the same
> comparison read before the sheafification is removed, where it is Stacks 070S (1).
>
> **Quasi-coherence is not an added hypothesis.**  The construction whose two descriptions the
> remark identifies is `𝓕 ↦ 𝓕^a` of Definition 03DU (3), which is made for a quasi-coherent
> `𝒪_S`-module; the sheafified form above, which is 070S's own statement, needs nothing of `𝓕`.
>
> The declaration is also what reads the comparison of
> `AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso` below off the sections
> description, and so is **the key to Stacks 0GNE**: both of the modules compared there are this
> one sheaf.

```lean
noncomputable def baseAssociatedModuleIsoSectionsSheaf (τ : SiteKind) (F : S.Modules)
    [F.IsQuasicoherent] :
    (baseAssociatedModule B S hS τ).obj F ≅ sectionsSheafOfModules B S hS τ F
```

**`AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SectionsPullbackComparison/Comparison.lean, line 1073](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SectionsPullbackComparison/Comparison.lean#L1073). The attribute's comment: “part (1)”.

> For each of the five topologies `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, the
> associated module of a quasi-coherent module `F` on `S` — the pullback along the morphism of
> ringed sites `id_{τ,Zar} : ((Sch/S)_τ, 𝒪) → (S_Zar, 𝒪_S)` — is the `τ`-sheafification of the
> pullback-sections presheaf `(f : T → S) ↦ Γ(T, f⁺F)` of Stacks 03DS.
>
> This is `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleSheafificationIso` at `F`, which
> presents the associated module as the `τ`-sheafification of the presheaf-level pullback, followed
> by the `τ`-sheafification of `AlgebraicGeometry.BigFppfOver.sectionsComparison`.

```lean
public noncomputable def baseAssociatedModuleIsoSections (τ : SiteKind) (F : S.Modules)
    [F.IsQuasicoherent] :
    (baseAssociatedModule B S hS τ).obj F ≅
      (PresheafOfModules.sheafification.{u}
          (𝟙 (FibredSite.baseRingStructureSheaf B S hS τ).obj)).obj
        (sectionsPresheafOfModules B S hS F)
```

## Tag 03DV, a lemma

[Tag 03DV](https://stacks.math.columbia.edu/tag/03DV) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_baseAssociatedModule_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseOpenCoverQuasicoherence.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseOpenCoverQuasicoherence.lean#L226). The attribute's comment: “part (1), every τ”.

> For every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}` the associated module `𝓕^a` of a
> quasi-coherent `𝒪_S`-module `𝓕` is a quasi-coherent `𝒪`-module on the big site `(Sch/S)_τ`, in
> the sense of Modules on Sites, Definition 03DL (6).

```lean
public theorem isQuasicoherentOnSite_baseAssociatedModule_of_isQuasicoherent (τ : SiteKind)
    (𝓕 : S.Modules) (h : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    ((baseAssociatedModule B S hS τ).obj 𝓕).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleOpenCoverQuasicoherence.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleOpenCoverQuasicoherence.lean#L262). The attribute's comment: “part (2) at τ = étale”.

> The associated module `𝓕^a` of a quasi-coherent `𝒪_S`-module `𝓕` is a quasi-coherent
> `𝒪`-module on the small étale site `S_étale`, in the sense of Modules on Sites,
> Definition 03DL (6).
>
> The corresponding statement for the small Zariski site is
> `AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent`.

```lean
public theorem isQuasicoherentOnSite_associatedModule_of_isQuasicoherent (𝓕 : S.Modules)
    (h : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    ((associatedModule B S hS).obj 𝓕).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiOpenCoverQuasicoherence.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiOpenCoverQuasicoherence.lean#L272). The attribute's comment: “part (2) at τ = Zariski”.

> **Stacks 03DV, clause (2), at `τ = Zariski`.**  The associated module `𝓕^a` of a
> quasi-coherent `𝒪_S`-module `𝓕` is a quasi-coherent `𝒪`-module on the small Zariski site `S_Zar`,
> in the sense of Modules on Sites, Definition 03DL (6).
>
> The clause string records exactly the scope proved.  Clause (2) of the source
> quantifies over `τ ∈ {Zariski, étale}` — the two topologies for which Definition 03DU (4) defines
> the functor at all — and this is the `τ = Zariski` half, for an arbitrary quasi-coherent `𝓕`; the
> `τ = étale` half is
> `AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent`, so with
> this declaration clause (2) is complete.  Clause (1) of the source, at all five `τ`, is
> `AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_baseAssociatedModule_of_isQuasicoherent`.

```lean
public theorem isQuasicoherentOnSite_associatedModule_of_isQuasicoherent (𝓕 : S.Modules)
    (h : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    ((associatedModule B S hS).obj 𝓕).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_associatedModuleOfSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean#L145). The attribute's comment: “part (2) at τ = Zariski, for the SECTIONS-defined 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedModuleOfSections, whose sections over f : T → S are Γ(T, f^*𝓕). The same clause for the pullback-defined 𝓕ᵃ of Remark 03FH is isQuasicoherentOnSite_associatedModule_of_isQuasicoherent; the two sheaves are identified by associatedModuleIsoOfSections”.

> **[Stacks, Tag 03DV] (2) at `τ = Zariski`, for the sheaf the source constructs.**  The
> associated module `𝓕ᵃ` of [Stacks, Tag 03DU] (4) — the sheaf on `S_Zar` whose sections over an
> object `f : T → S` are `Γ(T, f^*𝓕)`,
> `AlgebraicGeometry.SmallZariski.associatedModuleOfSections` — is a quasi-coherent `𝒪`-module in
> the sense of [Stacks, Tag 03DL] (6).
>
> `AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent` is the
> same clause for the *pullback*-defined `𝓕ᵃ` of [Stacks, Remark 03FH]; this is it read through
> `AlgebraicGeometry.SmallZariski.associatedModuleIsoOfSections`, which identifies the two, and
> quasi-coherence on a site is invariant under isomorphism.

```lean
public theorem isQuasicoherentOnSite_associatedModuleOfSections (F : S.Modules)
    [F.IsQuasicoherent] : (associatedModuleOfSections B S hS F).IsQuasicoherentOnSite
```

## Tag 0GN7, a lemma

[Tag 0GN7](https://stacks.math.columbia.edu/tag/0GN7) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.fullyFaithfulBaseAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseFullyFaithful.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseFullyFaithful.lean#L208). The attribute's comment: “big site (Sch/S)_τ, every τ”.

> **Stacks 0GN7 for the big site, and clause (1) of Stacks 06VE for it.**  For every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}` the functor `𝓕 ↦ 𝓕^a` of Definition 03DU, from
> the quasi-coherent `𝒪_S`-modules to the `𝒪`-modules on the big site `(Sch/S)_τ`, is fully
> faithful.
>
> The two tags assert one thing of one functor, and the clause strings record the scope this
> declaration proves — on **one source line**, because a tag registry that reads the attributes
> matches a second `stacks` clause only when it is on the same line as the first, and two clause
> strings plus the attribute syntax do not fit in a hundred characters unless both are short.  The
> 0GN7 string therefore no longer ends `; small site S_τ untreated`: that is information about
> *where else the tag is registered*, not about the scope proved, and
> `big site (Sch/S)_τ, every τ` already states the scope exactly.  The other registrations are
> named in the last paragraph below.
>
> 06VE's first functor is `QCoh(𝒪_S) → Mod((Sch/S)_τ, 𝒪)`, whose target is
> `Mod` — which is the target below on the nose, `SheafOfModules` over the structure sheaf of
> `(Sch/S)_τ` — so clause (1) of 06VE needs no reading through a subcategory.  0GN7 spells the
> same functor with target `QCoh((Sch/S)_τ, 𝒪)`, and that too is the same statement: full
> faithfulness of a functor into a category is full faithfulness into any full subcategory
> containing its image, and the image does land in `QCoh` by Stacks 03DV (1),
> `AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_baseAssociatedModule_of_isQuasicoherent`.
>
> What is **not** claimed by either tag here is the source's second functor,
> `QCoh(𝒪_S) → Mod(S_τ, 𝒪)` into the *small* site of `S` for `τ ∈ {Zariski, étale}` — a different
> construction, Definition 03DU (4).  It is claimed elsewhere, and 0GN7 quantifies over nothing
> beyond these: Definition 03DU gives a small site only at `τ ∈ {Zariski, étale}`, so this
> declaration together with
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean`)
> and `AlgebraicGeometry.SmallEtale.fullyFaithfulAssociatedModuleQcoh'`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean`) is
> every functor the lemma speaks of.  At `τ = Zariski` the *sections*-defined form of the functor
> carries the tag too, as
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedSheafFunctor`.
>
> (The small étale functor is `AlgebraicGeometry.SmallEtale.associatedModule`, in
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedSite.lean`, and its full
> faithfulness rests on `AlgebraicGeometry.SmallEtale.unitIsoOnQuasicoherent` of
> `SmallEtaleLocalBijectivity.lean`, which proves
> `AlgebraicGeometry.SmallEtale.UnitIsoOnQuasicoherent` with no hypothesis.)

```lean
public noncomputable def fullyFaithfulBaseAssociatedModuleQcoh (τ : SiteKind) :
    (baseAssociatedModuleQcoh B S hS τ).FullyFaithful
```

**`AlgebraicGeometry.SmallEtale.fullyFaithfulAssociatedModuleQcoh'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean#L660). The attribute's comment: “small site at τ = étale”.

> **The small étale half of Stacks 0GN7 and of Stacks 06VE (1), with no hypothesis at all**:
> the functor `𝓕 ↦ 𝓕^a` of Definition 03DU (4) at `τ = étale`, from the quasi-coherent
> `𝒪_S`-modules to the `𝒪`-modules on `S_étale`, is fully faithful.

```lean
public noncomputable def fullyFaithfulAssociatedModuleQcoh' :
    (associatedModuleQcoh B S hS).FullyFaithful
```

**`AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean#L275). The attribute's comment: “small site at τ = Zariski”.

> **Stacks 0GN7 for the small site at `τ = Zariski`, and clause (1) of Stacks 06VE for it.**
> The functor `𝓕 ↦ 𝓕^a` of Definition 03DU (4) at `τ = Zariski` — the pullback of sheaves of
> modules along the morphism of ringed sites `(S_Zar, 𝒪) → (S_Zar, 𝒪_S)` of Remark 03FH, with the
> coefficient sheaf `T/S ↦ Γ(T, 𝒪_T)` of Definition 03DU (2) — from the quasi-coherent
> `𝒪_S`-modules to the `𝒪`-modules on the small Zariski site, is fully faithful.
>
> Together with `AlgebraicGeometry.BigFppfOver.fullyFaithfulBaseAssociatedModuleQcoh` (the big
> site, every `τ`) and `AlgebraicGeometry.SmallEtale.fullyFaithfulAssociatedModuleQcoh'` (the
> small site at `τ = étale`) this completes the covering set of 0GN7: Definition 03DU gives a small
> site only for `τ ∈ {Zariski, étale}`, so those three statements are every functor the lemma
> quantifies over.
>
> 0GN7 spells the target `QCoh(S_Zar, 𝒪)` where this is `Mod(S_Zar, 𝒪)`, and that is the same
> statement for the same reason as at `τ = étale` and on the big site: full faithfulness of a
> functor into a category is full faithfulness into any full subcategory containing its image, and
> the image lands in `QCoh(S_Zar, 𝒪)` by Stacks 03DV (2),
> `AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent`;
> the corestriction itself is
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcohOnSite` below.  06VE's second
> functor has target `Mod(S_τ, 𝒪)`, which is the target here with nothing to read through.

```lean
public noncomputable def fullyFaithfulAssociatedModuleQcoh :
    (associatedModuleQcoh B S hS).FullyFaithful
```

**`AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedSheafFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsIso.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsIso.lean#L572). The attribute's comment: “small site at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedSheafFunctor, whose value at 𝓕 is SmallZariski.associatedModuleOfSections. The same clause for the pullback-defined functor of Remark 03FH is fullyFaithfulAssociatedModuleQcoh; the two functors are identified by associatedModuleQcohIsoAssociatedSheafFunctor”.

> **[Stacks, Tag 0GN7] for the small site at `τ = Zariski`, for the functor the source
> defines**: the assignment `𝓕 ↦ 𝓕ᵃ` of [Stacks, Tag 03DU] (4) — the sheaf of `𝒪`-modules on
> `S_Zar` whose sections over `f : T → S` are `Γ(T, f^*𝓕)`,
> `AlgebraicGeometry.SmallZariski.associatedSheafFunctor` — is fully faithful on the quasi-coherent
> `𝒪_S`-modules.
>
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh` is the same statement for the
> *pullback*-defined functor of [Stacks, Remark 03FH]; this is it read through
> `AlgebraicGeometry.SmallZariski.associatedModuleQcohIsoAssociatedSheafFunctor`, which identifies
> the two.  Both are 0GN7 at `τ = Zariski`, and the source's own statement is about the sections
> description, so the clause is only about the object the source names once this form exists.
>
> 0GN7 spells the target `QCoh(S_Zar, 𝒪)` where this is `Mod(S_Zar, 𝒪)`; that is the same
> statement for the reason recorded on
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh`, full faithfulness into a
> category being full faithfulness into any full subcategory containing the image, and the image
> landing in `QCoh(S_Zar, 𝒪)` by [Stacks, Tag 03DV] (2).
>
> **This is also clause (1) of [Stacks, Tag 06VE] at `τ = Zariski` for the sections-defined
> functor**, that clause being the same assertion of full faithfulness; its second functor has
> target `Mod(S_τ, 𝒪)`, which is the target here with nothing to read through.  The two attributes
> sit together for the same reason they do on
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh` for the pullback-defined
> functor.

```lean
public noncomputable def fullyFaithfulAssociatedSheafFunctor :
    (associatedSheafFunctor B S hS).FullyFaithful
```

**`Stacks.Sites.bijective_associatedModuleMap_of_mem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/AssociatedModuleArbitraryBaseFpqc.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/AssociatedModuleArbitraryBaseFpqc.lean#L85). The attribute's comment: “the lemma over a base that is NOT assumed affine, on a site of schemes over S presented by a precoverage K and a functor toOver : C -> Over S. The two registrations that stood before this one are at particular sites and neither covers this presentation: Stacks.Descent.fullyFaithfulAssociatedModuleQcoh' is the small site at a topology tau (StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean:717) and Stacks.Descent.fullyFaithfulBaseAssociatedModuleQcoh is the big site (Sch/S)_tau (StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseFullyFaithful.lean:211); the abstract presentation has neither the objScheme/objRestrict apparatus of the second nor a functor out of S.Opens as the first uses, so neither transfers. WHAT IS REMOVED relative to the affine-base case Stacks.Sites.bijective_associatedModuleMap is exactly IsAffine S, and nothing else: both sheaf conditions of bijective_associatedModuleMap_of_isPrestack are discharged here, the presheaf of morphisms by isPrestackOver_of_mem_fpqcPrecoverage and the associated presheaf by isSheaf_associatedPresheaf_of_mem_fpqcPrecoverage, the latter being the SECOND assertion of Stacks 03OJ. CARRIED: hcover, that the arrows factoring through an object with affine underlying scheme cover every object. That is a real hypothesis and not a restatement of the conclusion, but it is NOT supplied by condition (2) of Stacks 03OJ -- condition (2) yields covering only at the class Stacks.Sites.OverAffineOpen, of objects whose structure morphism has image inside an affine open, and at that class the local half of this lemma is BLOCKED: the required agreement of two Gamma(T,O)-linear maps on all of Gamma(g^+M, top) needs AlgebraicGeometry.Scheme.Modules.span_range_pullbackSection_eq_top at W = top, which needs T affine, and that file's own documentation records that both of its affineness hypotheses are needed and that the statement is false for U affine and V arbitrary. So hcover at the AFFINE class is what this form asks for, and supplying it from Stacks 03OJ's conditions is the open problem that the third assertion of that tag now rests on. The full and faithful forms of this clause are full_ and faithful_associatedModuleFunctor_of_mem_fpqcPrecoverage below”.

> On a site of schemes over `S` whose coverings are fpqc coverings of schemes, the map
> `φ ↦ φᵃ` is bijective on morphisms of quasi-coherent modules on `S`, with **no affineness
> assumption on `S`**, as soon as the arrows factoring through an object with affine underlying
> scheme cover every object and the site contains an object `X₀` with invertible structure morphism
> receiving a morphism from every object.

```lean
public theorem bijective_associatedModuleMap_of_mem_fpqcPrecoverage
    (hfpqc : ∀ ⦃T : C⦄ (R : Presieve T), R ∈ K T →
      Presieve.map (toOver ⋙ Over.forget S) R ∈
        Scheme.fpqcPrecoverage.{u} ((toOver ⋙ Over.forget S).obj T))
    (hcover : ∀ X : C, Sieve.coverByImage
      (ObjectProperty.ι (fun Y : C ↦ IsAffine (toOver.obj Y).left)) X ∈ K.toGrothendieck X)
    (X₀ : C) [IsIso (toOver.obj X₀).hom] (hterm : ∀ X : C, Nonempty (X ⟶ X₀))
    (M N : S.Modules) [M.IsQuasicoherent] [N.IsQuasicoherent] :
    Function.Bijective fun φ : M ⟶ N => associatedModuleMap S toOver φ
```

## Tag 03DX, a proposition

[Tag 03DX](https://stacks.math.columbia.edu/tag/03DX) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isEquivalence_associatedModuleQcohOnSite_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/EffectiveGlueAgreementRestrFun.lean, line 661](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/EffectiveGlueAgreementRestrFun.lean#L661). The attribute's comment: “clause (1) at τ = fppf: 𝓕 ↦ 𝓕^a is an equivalence QCoh(𝒪_S) ⥤ QCoh((Sch/S)_fppf, 𝒪)”.

> **Stacks 03DX (1) for `τ = fppf`: `𝓕 ↦ 𝓕^a` is an equivalence.**  The functor
> `QCoh(𝒪_S) ⥤ QCoh((Sch/S)_fppf, 𝒪)` is fully faithful unconditionally
> (`AlgebraicGeometry.BigFppfOver.fullyFaithfulAssociatedModuleQcohOnSite'`, Stacks 0GN7) and
> essentially surjective by
> `AlgebraicGeometry.BigFppfOver.quasicoherentIsEssImageAssociatedModule'`.

```lean
public theorem isEquivalence_associatedModuleQcohOnSite_fppf :
    (associatedModuleQcohOnSite' B S hS).IsEquivalence
```

**`AlgebraicGeometry.BigFppfOver.associatedModuleEquivalence_fppf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/EffectiveGlueAgreementRestrFun.lean, line 670](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/EffectiveGlueAgreementRestrFun.lean#L670). The attribute's comment: “clause (1) at τ = fppf: the equivalence of categories QCoh(𝒪_S) ≌ QCoh((Sch/S)_fppf, 𝒪)”.

> **The equivalence of categories of Stacks 03DX (1) for `τ = fppf`**,
> `QCoh(𝒪_S) ≌ QCoh((Sch/S)_fppf, 𝒪)`, with `𝓕 ↦ 𝓕^a` as its functor.

```lean
public noncomputable def associatedModuleEquivalence_fppf :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (structureSheaf B S hS)).FullSubcategory
```

**`AlgebraicGeometry.SmallEtale.bijective_restrictionBaseChange_affineChartModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleAffineFiniteTypeSections.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleAffineFiniteTypeSections.lean#L140). The attribute's comment: “quasi-coherent implies cartesian over the small affine étale site of a scheme”.

> **A quasi-coherent sheaf of modules on the small étale site of a scheme is cartesian over
> every arrow of the small affine étale site**, for the chart rings.

```lean
theorem bijective_restrictionBaseChange_affineChartModule
    (G : SheafOfModules.{u} (structureSheaf B S hS)) (hG : G.IsQuasicoherentOnSite)
    {X Y : (SmallAffineEtale B S hS)ᵒᵖ} (a : X ⟶ Y) :
    Function.Bijective (restrictionBaseChange.{u + 1, u, u, u}
      (R := affineChartRings B S hS) (affineChartPresheaf B S hS G) a)
```

**`AlgebraicGeometry.SmallEtale.bijective_restrictionBaseChange_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleCartesian.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleCartesian.lean#L322). The attribute's comment: “quasi-coherent implies cartesian between affine objects of the small étale site”.

> A quasi-coherent sheaf of modules on the small étale site of a scheme is cartesian between
> affine objects: for a morphism `f : T ⟶ T'` of objects of `S_étale` whose underlying schemes are
> affine, the base-change comparison `Γ(T) ⊗_{Γ(T')} 𝒢(T') ⟶ 𝒢(T)` is bijective.
>
> This is a step of Stacks 03DX (2) at `τ = étale`, whose statement as an equivalence of categories
> is `AlgebraicGeometry.SmallEtale.isEquivalence_associatedModuleQcohOnSite'`.

```lean
theorem bijective_restrictionBaseChange_of_isQuasicoherentOnSite
    (G : SheafOfModules.{u} (structureSheaf B S hS)) (hG : G.IsQuasicoherentOnSite)
    {T T' : SmallEtale B S hS}
    (hT : AlgebraicGeometry.IsAffine ((toScheme B S hS).obj T))
    (hT' : AlgebraicGeometry.IsAffine ((toScheme B S hS).obj T'))
    (f : T ⟶ T') :
    Function.Bijective
      (restrictionBaseChange (R := commStructurePresheaf B S hS) G.val f.op)
```

**`AlgebraicGeometry.SmallZariski.isEquivalence_associatedModuleQcohOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean#L404). The attribute's comment: “clause (2) at τ = Zariski: 𝓕 ↦ 𝓕^a is an equivalence QCoh(𝒪_S) ⥤ QCoh(S_Zar, 𝒪)”.

> **Stacks 03DX clause (2) at `τ = Zariski`**: `𝓕 ↦ 𝓕^a` is an equivalence
> `QCoh(𝒪_S) ⥤ QCoh(S_Zar, 𝒪)`.
>
> `CategoryTheory.Functor.IsEquivalence` is fullness, faithfulness and essential surjectivity
> together, which is the decomposition the source's proof uses: Stacks 03DV (2) for the functor,
> Stacks 0GN7 for full faithfulness, and
> `AlgebraicGeometry.SmallZariski.isQuasicoherent_restrictModule` for essential surjectivity.
> Clause (2) also ranges over `τ = étale`, which is
> `AlgebraicGeometry.SmallEtale.isEquivalence_associatedModuleQcohOnSite'`; clause (1), over the
> big sites, is untouched here.

```lean
public theorem isEquivalence_associatedModuleQcohOnSite :
    (AlgebraicGeometry.SmallZariski.associatedModuleQcohOnSite B S hS).IsEquivalence
```

**`AlgebraicGeometry.SmallZariski.associatedModuleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean#L420). The attribute's comment: “clause (2) at τ = Zariski: the equivalence of categories QCoh(𝒪_S) ≌ QCoh(S_Zar, 𝒪)”.

> **The equivalence of categories of Stacks 03DX (2) at `τ = Zariski`**,
> `QCoh(𝒪_S) ≌ QCoh(S_Zar, 𝒪)`, with `𝓕 ↦ 𝓕^a` as its functor.
>
> The source states the clause as an equivalence rather than as the three properties of the
> functor, and this is that statement; its `CategoryTheory.Equivalence.functor` is
> `AlgebraicGeometry.SmallZariski.associatedModuleQcohOnSite` by definition.

```lean
public noncomputable def associatedModuleEquivalence :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (structureSheaf B S hS)).FullSubcategory
```

**`AlgebraicGeometry.SmallZariski.isEquivalence_associatedSheafFunctorOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean#L195). The attribute's comment: “clause (2) at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedSheafFunctor corestricted to QCoh(S_Zar, 𝒪) — is an equivalence QCoh(𝒪_S) ⥤ QCoh(S_Zar, 𝒪). The same clause for the pullback-defined functor of Remark 03FH is isEquivalence_associatedModuleQcohOnSite; the two functors are identified by associatedModuleQcohIsoAssociatedSheafFunctor”.

> **[Stacks, Tag 03DX] clause (2) at `τ = Zariski`, for the functor the source defines**: the
> sections-defined `𝓕 ↦ 𝓕ᵃ` of [Stacks, Tag 03DU] (4) is an equivalence
> `QCoh(𝒪_S) ⥤ QCoh(S_Zar, 𝒪)`.
>
> `AlgebraicGeometry.SmallZariski.isEquivalence_associatedModuleQcohOnSite` is the same clause for
> the pullback-defined functor of [Stacks, Remark 03FH]; this is it read through
> `AlgebraicGeometry.SmallZariski.associatedModuleQcohIsoAssociatedSheafFunctor`.  The
> decomposition is the source's own: [Stacks, Tag 03DV] (2) for the functor,
> [Stacks, Tag 0GN7] for full faithfulness, and
> `AlgebraicGeometry.SmallZariski.isQuasicoherent_restrictModule` for essential surjectivity.

```lean
public theorem isEquivalence_associatedSheafFunctorOnSite :
    (associatedSheafFunctorOnSite B S hS).IsEquivalence
```

**`AlgebraicGeometry.SmallZariski.associatedSheafFunctorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean#L214). The attribute's comment: “clause (2) at τ = Zariski, the equivalence of categories QCoh(𝒪_S) ≌ QCoh(S_Zar, 𝒪) whose functor is the SECTIONS-defined 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4), SmallZariski.associatedSheafFunctor corestricted to QCoh(S_Zar, 𝒪). The same clause for the pullback-defined functor of Remark 03FH is associatedModuleEquivalence”.

> **The equivalence of categories of [Stacks, Tag 03DX] (2) at `τ = Zariski`, for the functor
> the source defines**: `QCoh(𝒪_S) ≌ QCoh(S_Zar, 𝒪)`, with the sections-defined `𝓕 ↦ 𝓕ᵃ` as its
> functor.
>
> The source states the clause as an equivalence rather than as the three properties of the
> functor, and this is that statement; its `CategoryTheory.Equivalence.functor` is
> `AlgebraicGeometry.SmallZariski.associatedSheafFunctorOnSite` by definition.  Its
> pullback-defined counterpart is
> `AlgebraicGeometry.SmallZariski.associatedModuleEquivalence`.

```lean
public noncomputable def associatedSheafFunctorEquivalence :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (structureSheaf B S hS)).FullSubcategory
```

**`AlgebraicGeometry.BigFppfOver.baseAssociatedModuleEquivalenceOnSite'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSmallEtaleBigSite.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSmallEtaleBigSite.lean#L195). The attribute's comment: “clause (1) at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}: 𝓕 ↦ 𝓕ᵃ is an equivalence QCoh(𝒪_S) ≌ QCoh((Sch/S)_τ, 𝒪)”.

> **Stacks 03DX (1) at every `τ`, as an equivalence of categories**:
> `QCoh(𝒪_S) ≌ QCoh((Sch/S)_τ, 𝒪)`, with `𝓕 ↦ 𝓕^a` as its functor and with no hypothesis.

```lean
public noncomputable def baseAssociatedModuleEquivalenceOnSite' (τ : SiteKind) :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (FibredSite.baseRingStructureSheaf B S hS τ)).FullSubcategory
```

**`Stacks.AlgebraicGeometry.AffinePresentation.hasGlobalPresentation_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/QuasicoherentAffineGlobalPresentation.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/QuasicoherentAffineGlobalPresentation.lean#L186). The attribute's comment: “a quasi-coherent module on an affine has a global presentation”. References: SGA 6 0 (2.5), “partial”.

> **Stacks 03DX, the presentation step, on the Zariski site.**  A quasi-coherent
> `𝒪_T`-module on an affine scheme `T` has a *global* presentation: it is the module associated
> with a module over the coordinate ring `Γ(T, ⊤)`, and a presentation of that module by
> generators and relations transports to a presentation of the sheaf over the whole of `T`.
>
> Quasi-coherence here is `SheafOfModules.IsQuasicoherentOnSite`, Stacks 03DL(6), which asks only
> for a presentation *locally*; the content of the step is that on an affine no covering is
> needed.  The two quasi-coherence predicates agree on the Zariski site by
> `SheafOfModules.isQuasicoherent_iff_isQuasicoherentOnSite`, whose size hypothesis is automatic
> there.
>
> The clause string records exactly this much: a quasi-coherent module on an affine has a global
> presentation.  Stacks 03DX states its clauses as equivalences of categories, and those are
> carried by the declarations named in the module docstring, whose descent arguments consume what
> is proved here; the same statement at an affine object of the big fppf site is
> `AlgebraicGeometry.BigFppfOver.hasGlobalPresentation_over_of_isQuasicoherentOnSite`.

```lean
theorem hasGlobalPresentation_of_isQuasicoherentOnSite (T : Scheme.{u}) [IsAffine T]
    (M : SheafOfModules.{u} T.ringCatSheaf) (hM : M.IsQuasicoherentOnSite) :
    M.HasGlobalPresentation
```

**`AlgebraicGeometry.Space.isCartesianOnAffineCharts_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentCartesianOnAffineCharts.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentCartesianOnAffineCharts.lean#L542). The attribute's comment: “quasi-coherent implies cartesian”.

> **The forward half of the chart criterion for quasi-coherence on the small étale site of an
> algebraic space**: a quasi-coherent `𝒪_F`-module, with sections in the universe of the schemes, is
> cartesian on affine charts.

```lean
theorem isCartesianOnAffineCharts_of_isQuasicoherentOnSite
    (G : Modules.{u, u} B S hS F hF) (hG : G.IsQuasicoherentOnSite) :
    IsCartesianOnAffineCharts G
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_iff_isCartesianOnAffineCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentCartesianOnAffineCharts.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentCartesianOnAffineCharts.lean#L553). The attribute's comment: “part (2)”.

> **The chart criterion for quasi-coherence on the small étale site of an algebraic space**: an
> `𝒪_F`-module, with sections in the universe of the schemes, is quasi-coherent if and only if it
> is cartesian on affine charts.  The base `F` is an algebraic space, and the statement is a
> criterion on a single module rather than the equivalence of categories
> `QCoh(𝒪_S) ⥤ QCoh(S_étale, 𝒪)` for a scheme `S`.

```lean
theorem isQuasicoherentOnSite_iff_isCartesianOnAffineCharts
    (G : Modules.{u, u} B S hS F hF) :
    G.IsQuasicoherentOnSite ↔ IsCartesianOnAffineCharts G
```

Declarations registered for the tag:

- [`baseQuasicoherentIsEssImageAssociatedModule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=baseQuasicoherentIsEssImageAssociatedModule#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseEssentialSurjectivity.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseEssentialSurjectivity.lean#L132) (StacksFrontier): “clause (1) at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}: essential surjectivity of 𝓕 ↦ 𝓕ᵃ onto the quasi-coherent 𝒪-modules of the big τ site of S”.
- [`quasicoherentIsEssImageAssociatedModule'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=quasicoherentIsEssImageAssociatedModule'#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/EffectiveGlueAgreementTransport.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/EffectiveGlueAgreementTransport.lean#L522) (StacksFrontier): “clause (1) at τ = fppf: essential surjectivity of 𝓕 ↦ 𝓕^a onto the quasi-coherent 𝒪-modules of the big fppf site of S, with no assumption”.
- [`quasicoherentIsEssImageAssociatedModule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=quasicoherentIsEssImageAssociatedModule#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleCounit.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleCounit.lean#L339) (StacksFrontier): “clause (2) at τ = étale: essential surjectivity of 𝓕 ↦ 𝓕^a onto the quasi-coherent 𝒪-modules of the small étale site of S, with no hypothesis”.
- [`isEquivalence_associatedModuleQcohOnSite'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isEquivalence_associatedModuleQcohOnSite'#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleCounit.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleCounit.lean#L344) (StacksFrontier): “clause (2) at τ = étale: 𝓕 ↦ 𝓕^a is an equivalence QCoh(𝒪_S) ⥤ QCoh(S_étale, 𝒪), with no hypothesis”.

## Tag 05VG, a lemma

[Tag 05VG](https://stacks.math.columbia.edu/tag/05VG) in the Stacks Project.

**`Stacks.Sheaves.GlobalTypeComparison.isFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean#L171). The attribute's comment: “free; global properties only, and the comparison functor of 03DX hypothesised”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (1).**  A module is free if
> and only if its image under the comparison is free: both sides are the assertion that some
> family of global sections exhibits the module as a coproduct of copies of the structure
> sheaf, and `Stacks.Sheaves.GlobalTypeComparison.isColimitCofanMap` and
> `.isColimitCofanOfMap` move such a family in the two directions without changing its index
> type.

```lean
theorem isFree_iff (F : SheafOfModules.{w} R₁) : F.IsFree ↔ (Φ.obj F).IsFree
```

**`Stacks.Sheaves.GlobalTypeComparison.isFiniteFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean#L185). The attribute's comment: “finite free; global properties only, and the comparison functor of 03DX hypothesised”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (2).**  A module is finite
> free if and only if its image under the comparison is finite free.  The ring and module
> universes agreeing, `SheafOfModules.isFiniteFree_iff_exists_isColimit` reduces both sides to
> a cofan with index type `Fin n`, and the same `n` works on both sides.

```lean
theorem isFiniteFree_iff (F : SheafOfModules.{w} R₁) :
    SheafOfModules.IsFiniteFree R₁ F ↔ SheafOfModules.IsFiniteFree R₂ (Φ.obj F)
```

**`Stacks.Sheaves.GlobalTypeComparison.isGeneratedByGlobalSections_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean#L241). The attribute's comment: “generated by global sections; global properties only, and the comparison functor of 03DX hypothesised”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (3).**  A module is generated
> by global sections if and only if its image under the comparison is.

```lean
theorem isGeneratedByGlobalSections_iff (F : SheafOfModules.{w} R₁) :
    F.IsGeneratedByGlobalSections ↔ (Φ.obj F).IsGeneratedByGlobalSections
```

**`Stacks.Sheaves.GlobalTypeComparison.isGeneratedByGlobalSectionsOfCard_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean#L251). The attribute's comment: “generated by r global sections; global properties only, and the comparison functor of 03DX hypothesised”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (4).**  A module is generated
> by `r` global sections if and only if its image under the comparison is: the transported
> generating family is indexed by the same type, so the same `r` works.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff (F : SheafOfModules.{w} R₁) (r : ℕ) :
    F.IsGeneratedByGlobalSectionsOfCard r ↔
      (Φ.obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`Stacks.Sheaves.GlobalTypeComparison.exists_isGeneratedByGlobalSectionsOfCard_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean#L262). The attribute's comment: “generated by finitely many global sections; global properties only, and the comparison functor of 03DX hypothesised”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (5).**  A module is generated
> by finitely many global sections if and only if its image under the comparison is.

```lean
theorem exists_isGeneratedByGlobalSectionsOfCard_iff (F : SheafOfModules.{w} R₁) :
    (∃ r : ℕ, F.IsGeneratedByGlobalSectionsOfCard r) ↔
      ∃ r : ℕ, (Φ.obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`Stacks.Sheaves.GlobalTypeComparison.isPresentedByGlobalSections_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean#L279). The attribute's comment: “global presentation; global properties only, and the comparison functor of 03DX hypothesised”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (6).**  A module has a global
> presentation if and only if its image under the comparison has one.
>
> The preservation half maps the two coproducts and the cokernel across.  The reverse half
> cannot take preimages of the two given coproducts, `Φ` not being essentially surjective; it
> takes `SheafOfModules.free` on the two given index types instead, compares them with the given
> coproducts through `Stacks.Sheaves.GlobalTypeComparison.mapFreeIso`, and moves the cokernel
> across that comparison with `CategoryTheory.Limits.Cofork.isColimitOfIsos` before reflecting
> it along `Φ`.  The two index types are unchanged.

```lean
theorem isPresentedByGlobalSections_iff (F : SheafOfModules.{w} R₁) :
    F.IsPresentedByGlobalSections ↔ (Φ.obj F).IsPresentedByGlobalSections
```

**`Stacks.Sheaves.GlobalTypeComparison.isFinitelyPresentedByGlobalSections_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GlobalTypesUnderComparison.lean#L310). The attribute's comment: “finite global presentation; global properties only, and the comparison functor of 03DX hypothesised”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (7).**  A module has a finite
> global presentation if and only if its image under the comparison has one, with the same two
> finite index types `Fin n` and `Fin k`.
>
> Those index types do not live in the universe of sections, so the two coproducts the reverse
> half builds are the free modules on `ULift (Fin n)` and `ULift (Fin k)`, with their cofans
> reindexed by `CategoryTheory.Limits.Cofan.isColimitEquivOfEquiv`; the presentation produced is
> still indexed by `Fin n` and `Fin k`, so the finiteness is not weakened.

```lean
theorem isFinitelyPresentedByGlobalSections_iff (F : SheafOfModules.{w} R₁) :
    F.IsFinitelyPresentedByGlobalSections ↔
      (Φ.obj F).IsFinitelyPresentedByGlobalSections
```

**`Stacks.Sheaves.LocalTypeComparison.isFlat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean#L154). The attribute's comment: “flat; local properties, with the comparison of 03DX carried as an equivalence of ringed topoi rather than of quasi-coherent modules alone”. References: SGA 4 V (1.7.1), “special case”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3): flatness.**  A sheaf of
> modules on the target of an equivalence of ringed topoi is flat if and only if its image under
> the comparison is flat.
>
> The forward implication is Modules on Sites, Lemma 05VD,
> `Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules`, which holds for an arbitrary
> morphism of ringed topoi.  The reverse one applies 05VD to the inverse morphism
> `AlgebraicGeometry.RingedToposHom.inverse` and carries the conclusion back along
> `AlgebraicGeometry.RingedToposHom.pullbackModulesInverseObjIso`, the identification of the
> round trip with the identity, using that flatness is invariant under isomorphism of sheaves of
> modules.  This is the pattern of the three statements of Modules on Sites, Lemma 03DM in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ModuleTypesUnderEquivalence`, which flatness is
> not a clause of, 03DM covering 03DL rather than 03ER.
>
> The three universes of each ringed topos are taken equal because
> `Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules` already forces the source's object
> and section universes to agree; applying it to `f` and to the inverse of `f` in turn forces the
> same of the target, and the round-trip isomorphism needs the two section universes to agree.

```lean
theorem isFlat_iff (f : AlgebraicGeometry.RingedToposHom X Y)
    [f.toToposHom.pushforward.IsEquivalence] [IsIso f.fSharp]
    (F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := Y.J)) Y.O)) :
    Stacks.SheafOfModules.IsFlat (O := Y.O) F ↔
      Stacks.SheafOfModules.IsFlat (O := X.O)
        ((f.toModulesHom.pullbackModules).obj F)
```

**`AlgebraicGeometry.BigFppfOver.isFlat_baseAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteFlatAgreement.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteFlatAgreement.lean#L431). The attribute's comment: “flat (03ER (3)), big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3), at the big site
> `(Sch/S)_τ`, for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  A quasi-coherent
> `𝒪_S`-module `𝓗` is flat if and only if `𝓗ᵃ` is flat as an `𝒪`-module on `(Sch/S)_τ`.
>
> The `only if` half is `AlgebraicGeometry.BigFppfOver.isFlat_baseAssociatedModule_of_isFlat`,
> which needs neither quasi-coherence nor anything about the coverings of the big site; the `if`
> half is `AlgebraicGeometry.BigFppfOver.isFlat_of_isFlat_baseAssociatedModule`, and that is where
> the source's quasi-coherence hypothesis is used — the sections of `𝓗ᵃ` at an object `T → S` are
> the sections of the pullback of `𝓗` to `T` only for a quasi-coherent `𝓗`.

```lean
public theorem isFlat_baseAssociatedModule_iff :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓗 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u} (O := (baseRingedSite B S hS τ).O)
        ((baseAssociatedModule B S hS τ).obj 𝓗)
```

**`AlgebraicGeometry.Cells05VG.isCoherentOnSite_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Coherent.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Coherent.lean#L97). The attribute's comment: “coherent, small site S_Zar, S locally Noetherian”.

> **Descent, Lemma 05VG, coherent (03DL (8)), on the small site `S_Zar`.**  For a locally
> Noetherian scheme `S`, a quasi-coherent `𝒪_S`-module `𝓕` is coherent on `(Opens(S), 𝒪_S)` if
> and only if `𝓕^a` is coherent as an `𝒪`-module on `S_Zar`.

```lean
theorem isCoherentOnSite_iff_smallZariskiAssociatedModule [IsLocallyNoetherian S]
    (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsCoherentOnSite 𝓕 ↔
      SheafOfModules.IsCoherentOnSite ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isCoherentOnSite_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Coherent.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Coherent.lean#L114). The attribute's comment: “coherent, small site S_étale, S locally Noetherian”.

> **Descent, Lemma 05VG, coherent (03DL (8)), on the small site `S_étale`.**  For a locally
> Noetherian scheme `S`, a quasi-coherent `𝒪_S`-module `𝓕` is coherent on `(Opens(S), 𝒪_S)` if
> and only if `𝓕^a` is coherent as an `𝒪`-module on `S_étale`.

```lean
theorem isCoherentOnSite_iff_smallEtaleAssociatedModule [IsLocallyNoetherian S]
    (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsCoherentOnSite 𝓕 ↔
      SheafOfModules.IsCoherentOnSite ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L75). The attribute's comment: “finite free, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, finite freeness, big Zariski site.**  A quasi-coherent `𝒪_S`-module
> `𝓕` is finite free if and only if `𝓕^a` is finite free on `(Sch/S)_Zar`.

```lean
theorem isFiniteFree_iff_baseAssociatedModule_zariski (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L83). The attribute's comment: “finite free, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, finite freeness, big étale site.**  A quasi-coherent `𝒪_S`-module
> `𝓕` is finite free if and only if `𝓕^a` is finite free on `(Sch/S)_étale`.

```lean
theorem isFiniteFree_iff_baseAssociatedModule_etale (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L91). The attribute's comment: “finite free, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, finite freeness, big smooth site.**  A quasi-coherent `𝒪_S`-module
> `𝓕` is finite free if and only if `𝓕^a` is finite free on `(Sch/S)_smooth`.

```lean
theorem isFiniteFree_iff_baseAssociatedModule_smooth (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L99). The attribute's comment: “finite free, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, finite freeness, big syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite free if and only if `𝓕^a` is finite free on `(Sch/S)_syntomic`.

```lean
theorem isFiniteFree_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L109). The attribute's comment: “finite free, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, finite freeness, big fppf site.**  A quasi-coherent `𝒪_S`-module
> `𝓕` is finite free if and only if `𝓕^a` is finite free on `(Sch/S)_fppf`.

```lean
theorem isFiniteFree_iff_baseAssociatedModule_fppf (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L119). The attribute's comment: “finite free, small site S_Zar”.

> **Descent, Lemma 05VG, finite freeness, small Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite free if and only if `𝓕^a` is finite free on `S_Zar`.

```lean
theorem isFiniteFree_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L128). The attribute's comment: “finite free, small site S_étale”.

> **Descent, Lemma 05VG, finite freeness, small étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite free if and only if `𝓕^a` is finite free on `S_étale`.

```lean
theorem isFiniteFree_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L141). The attribute's comment: “finite free, small site S_smooth”.

> **Descent, Lemma 05VG, finite freeness, small smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite free if and only if `𝓕^a` is finite free on `S_smooth`.

```lean
theorem isFiniteFree_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L150). The attribute's comment: “finite free, small site S_syntomic”.

> **Descent, Lemma 05VG, finite freeness, small syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite free if and only if `𝓕^a` is finite free on `S_syntomic`.

```lean
theorem isFiniteFree_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteFree_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteFree.lean#L159). The attribute's comment: “finite free, small site S_fppf”.

> **Descent, Lemma 05VG, finite freeness, small fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite free if and only if `𝓕^a` is finite free on `S_fppf`.

```lean
theorem isFiniteFree_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
      SheafOfModules.IsFiniteFree _ ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L75). The attribute's comment: “finite locally free, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, finite local freeness, big Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `(Sch/S)_Zar`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L86). The attribute's comment: “finite locally free, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, finite local freeness, big étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `(Sch/S)_étale`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L97). The attribute's comment: “finite locally free, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, finite local freeness, big smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `(Sch/S)_smooth`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L108). The attribute's comment: “finite locally free, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, finite local freeness, big syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `(Sch/S)_syntomic`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L119). The attribute's comment: “finite locally free, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, finite local freeness, big fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `(Sch/S)_fppf`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L132). The attribute's comment: “finite locally free, small site S_Zar”.

> **Descent, Lemma 05VG, finite local freeness, small Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `S_Zar`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L143). The attribute's comment: “finite locally free, small site S_étale”.

> **Descent, Lemma 05VG, finite local freeness, small étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `S_étale`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L159). The attribute's comment: “finite locally free, small site S_smooth”.

> **Descent, Lemma 05VG, finite local freeness, small smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `S_smooth`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L170). The attribute's comment: “finite locally free, small site S_syntomic”.

> **Descent, Lemma 05VG, finite local freeness, small syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `S_syntomic`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteLocallyFreeOnSite_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteLocallyFree.lean#L181). The attribute's comment: “finite locally free, small site S_fppf”.

> **Descent, Lemma 05VG, finite local freeness, small fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is finite locally free if and only if `𝓕^a` is finite locally free on
> `S_fppf`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L81). The attribute's comment: “of finite presentation, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, finite presentation, big Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `(Sch/S)_Zar`.

```lean
theorem isFinitePresentationOnSite_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L92). The attribute's comment: “of finite presentation, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, finite presentation, big étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `(Sch/S)_étale`.

```lean
theorem isFinitePresentationOnSite_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L103). The attribute's comment: “of finite presentation, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, finite presentation, big smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `(Sch/S)_smooth`.

```lean
theorem isFinitePresentationOnSite_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L114). The attribute's comment: “of finite presentation, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, finite presentation, big syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `(Sch/S)_syntomic`.

```lean
theorem isFinitePresentationOnSite_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L125). The attribute's comment: “of finite presentation, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, finite presentation, big fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `(Sch/S)_fppf`.

```lean
theorem isFinitePresentationOnSite_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L138). The attribute's comment: “of finite presentation, small site S_Zar”.

> **Descent, Lemma 05VG, finite presentation, small Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `S_Zar`.

```lean
theorem isFinitePresentationOnSite_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L149). The attribute's comment: “of finite presentation, small site S_étale”.

> **Descent, Lemma 05VG, finite presentation, small étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `S_étale`.

```lean
theorem isFinitePresentationOnSite_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L164). The attribute's comment: “of finite presentation, small site S_smooth”.

> **Descent, Lemma 05VG, finite presentation, small smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `S_smooth`.

```lean
theorem isFinitePresentationOnSite_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L175). The attribute's comment: “of finite presentation, small site S_syntomic”.

> **Descent, Lemma 05VG, finite presentation, small syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `S_syntomic`.

```lean
theorem isFinitePresentationOnSite_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFinitePresentationOnSite_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FinitePresentation.lean#L186). The attribute's comment: “of finite presentation, small site S_fppf”.

> **Descent, Lemma 05VG, finite presentation, small fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation on
> `S_fppf`.

```lean
theorem isFinitePresentationOnSite_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFinitePresentationOnSite
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L106). The attribute's comment: “finite type, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the big site `(Sch/S)_Zar`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `(Sch/S)_Zar`.

```lean
theorem isFiniteTypeOnSite_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L118). The attribute's comment: “finite type, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the big site `(Sch/S)_étale`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `(Sch/S)_étale`.

```lean
theorem isFiniteTypeOnSite_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L130). The attribute's comment: “finite type, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the big site `(Sch/S)_smooth`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `(Sch/S)_smooth`.

```lean
theorem isFiniteTypeOnSite_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L142). The attribute's comment: “finite type, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the big site `(Sch/S)_syntomic`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `(Sch/S)_syntomic`.

```lean
theorem isFiniteTypeOnSite_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L154). The attribute's comment: “finite type, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the big site `(Sch/S)_fppf`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `(Sch/S)_fppf`.

```lean
theorem isFiniteTypeOnSite_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L172). The attribute's comment: “finite type, small site S_Zar”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the small site `S_Zar`.**  An
> `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an `𝒪`-module on
> `S_Zar`.  On this site no quasi-coherence is needed.

```lean
theorem isFiniteTypeOnSite_iff_smallZariskiAssociatedModule (𝓕 : S.Modules) :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallZariski.associatedModule B S hS).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L189). The attribute's comment: “finite type, small site S_étale”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the small site `S_étale`.**  An
> `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an `𝒪`-module on
> `S_étale`.  On this site no quasi-coherence is needed.

```lean
theorem isFiniteTypeOnSite_iff_smallEtaleAssociatedModule (𝓕 : S.Modules) :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallEtale.associatedModule B S hS).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L206). The attribute's comment: “finite type, small site S_smooth”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the small site `S_smooth`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `S_smooth`.

```lean
theorem isFiniteTypeOnSite_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L218). The attribute's comment: “finite type, small site S_syntomic”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the small site `S_syntomic`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `S_syntomic`.

```lean
theorem isFiniteTypeOnSite_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFiniteTypeOnSite_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/FiniteType.lean#L230). The attribute's comment: “finite type, small site S_fppf”.

> **Descent, Lemma 05VG, finite type (03DL (5)), on the small site `S_fppf`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕^a` is of finite type as an
> `𝒪`-module on `S_fppf`.

```lean
theorem isFiniteTypeOnSite_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteTypeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L87). The attribute's comment: “flat, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, flat, on the big site `(Sch/S)_Zar`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `(Sch/S)_Zar`.

```lean
theorem isFlat_iff_baseAssociatedModule_zariski (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (BigFppfOver.baseRingedSite B S hS .zariski).O)
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L98). The attribute's comment: “flat, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, flat, on the big site `(Sch/S)_étale`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `(Sch/S)_étale`.

```lean
theorem isFlat_iff_baseAssociatedModule_etale (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (BigFppfOver.baseRingedSite B S hS .etale).O)
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L109). The attribute's comment: “flat, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, flat, on the big site `(Sch/S)_smooth`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `(Sch/S)_smooth`.

```lean
theorem isFlat_iff_baseAssociatedModule_smooth (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (BigFppfOver.baseRingedSite B S hS .smooth).O)
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L121). The attribute's comment: “flat, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, flat, on the big site `(Sch/S)_syntomic`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on
> `(Sch/S)_syntomic`.

```lean
theorem isFlat_iff_baseAssociatedModule_syntomic (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (BigFppfOver.baseRingedSite B S hS .syntomic).O)
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L132). The attribute's comment: “flat, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, flat, on the big site `(Sch/S)_fppf`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `(Sch/S)_fppf`.

```lean
theorem isFlat_iff_baseAssociatedModule_fppf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (BigFppfOver.baseRingedSite B S hS .fppf).O)
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L148). The attribute's comment: “flat, small site S_Zar”.

> **Descent, Lemma 05VG, flat, on the small site `S_Zar`.**  A quasi-coherent `𝒪_S`-module `𝓕`
> is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `S_Zar`.
>
> Quasi-coherence is the source's hypothesis and is not used:
> `AlgebraicGeometry.SmallZariski.isFlat_iff_associatedModule` holds for every `𝒪_S`-module.

```lean
theorem isFlat_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (smallZariskiRingedSite B S hS).O)
        ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L162). The attribute's comment: “flat, small site S_étale”.

> **Descent, Lemma 05VG, flat, on the small site `S_étale`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `S_étale`.
>
> Quasi-coherence is the source's hypothesis and is not used:
> `AlgebraicGeometry.SmallEtale.isFlat_associatedModule_iff` holds for every `𝒪_S`-module.

```lean
theorem isFlat_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (smallEtaleRingedSite B S hS).O)
        ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L173). The attribute's comment: “flat, small site S_smooth”.

> **Descent, Lemma 05VG, flat, on the small site `S_smooth`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `S_smooth`.

```lean
theorem isFlat_iff_smallFlatSiteAssociatedModule_smooth (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (SmallFlatSite.ringedSite B S hS .smooth).O)
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L184). The attribute's comment: “flat, small site S_syntomic”.

> **Descent, Lemma 05VG, flat, on the small site `S_syntomic`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `S_syntomic`.

```lean
theorem isFlat_iff_smallFlatSiteAssociatedModule_syntomic (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (SmallFlatSite.ringedSite B S hS .syntomic).O)
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFlat_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Flat.lean#L195). The attribute's comment: “flat, small site S_fppf”.

> **Descent, Lemma 05VG, flat, on the small site `S_fppf`.**  A quasi-coherent `𝒪_S`-module
> `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `S_fppf`.

```lean
theorem isFlat_iff_smallFlatSiteAssociatedModule_fppf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
        (O := (SmallFlatSite.ringedSite B S hS .fppf).O)
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L74). The attribute's comment: “free, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, freeness, big Zariski site.**  A quasi-coherent `𝒪_S`-module `𝓕` is
> free if and only if `𝓕^a` is free on `(Sch/S)_Zar`.

```lean
theorem isFree_iff_baseAssociatedModule_zariski (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L82). The attribute's comment: “free, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, freeness, big étale site.**  A quasi-coherent `𝒪_S`-module `𝓕` is
> free if and only if `𝓕^a` is free on `(Sch/S)_étale`.

```lean
theorem isFree_iff_baseAssociatedModule_etale (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L90). The attribute's comment: “free, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, freeness, big smooth site.**  A quasi-coherent `𝒪_S`-module `𝓕` is
> free if and only if `𝓕^a` is free on `(Sch/S)_smooth`.

```lean
theorem isFree_iff_baseAssociatedModule_smooth (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L98). The attribute's comment: “free, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, freeness, big syntomic site.**  A quasi-coherent `𝒪_S`-module `𝓕` is
> free if and only if `𝓕^a` is free on `(Sch/S)_syntomic`.

```lean
theorem isFree_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L106). The attribute's comment: “free, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, freeness, big fppf site.**  A quasi-coherent `𝒪_S`-module `𝓕` is
> free if and only if `𝓕^a` is free on `(Sch/S)_fppf`.

```lean
theorem isFree_iff_baseAssociatedModule_fppf (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L116). The attribute's comment: “free, small site S_Zar”.

> **Descent, Lemma 05VG, freeness, small Zariski site.**  A quasi-coherent `𝒪_S`-module `𝓕`
> is free if and only if `𝓕^a` is free on `S_Zar`.

```lean
theorem isFree_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L125). The attribute's comment: “free, small site S_étale”.

> **Descent, Lemma 05VG, freeness, small étale site.**  A quasi-coherent `𝒪_S`-module `𝓕`
> is free if and only if `𝓕^a` is free on `S_étale`.

```lean
theorem isFree_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L138). The attribute's comment: “free, small site S_smooth”.

> **Descent, Lemma 05VG, freeness, small smooth site.**  A quasi-coherent `𝒪_S`-module `𝓕`
> is free if and only if `𝓕^a` is free on `S_smooth`.

```lean
theorem isFree_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L147). The attribute's comment: “free, small site S_syntomic”.

> **Descent, Lemma 05VG, freeness, small syntomic site.**  A quasi-coherent `𝒪_S`-module `𝓕`
> is free if and only if `𝓕^a` is free on `S_syntomic`.

```lean
theorem isFree_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isFree_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/Free.lean#L156). The attribute's comment: “free, small site S_fppf”.

> **Descent, Lemma 05VG, freeness, small fppf site.**  A quasi-coherent `𝒪_S`-module `𝓕`
> is free if and only if `𝓕^a` is free on `S_fppf`.

```lean
theorem isFree_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFree ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L168). The attribute's comment: “generated by finitely many global sections, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the big site
> `(Sch/S)_Zar`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections
> if and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on
> `(Sch/S)_Zar`.

```lean
theorem hasFiniteGlobalGenerators_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L181). The attribute's comment: “generated by finitely many global sections, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the big site
> `(Sch/S)_étale`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections
> if and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on
> `(Sch/S)_étale`.

```lean
theorem hasFiniteGlobalGenerators_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L194). The attribute's comment: “generated by finitely many global sections, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the big site
> `(Sch/S)_smooth`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global
> sections if and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on
> `(Sch/S)_smooth`.

```lean
theorem hasFiniteGlobalGenerators_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L207). The attribute's comment: “generated by finitely many global sections, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the big site
> `(Sch/S)_syntomic`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global
> sections if and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on
> `(Sch/S)_syntomic`.

```lean
theorem hasFiniteGlobalGenerators_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L220). The attribute's comment: “generated by finitely many global sections, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the big site
> `(Sch/S)_fppf`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections
> if and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on
> `(Sch/S)_fppf`.

```lean
theorem hasFiniteGlobalGenerators_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L239). The attribute's comment: “generated by finitely many global sections, small site S_Zar”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the small site
> `S_Zar`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections if and
> only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on `S_Zar`.  The
> comparison used here does not need quasi-coherence.

```lean
theorem hasFiniteGlobalGenerators_iff_smallZariskiAssociatedModule (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallZariski.associatedModule B S hS).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L257). The attribute's comment: “generated by finitely many global sections, small site S_étale”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the small site
> `S_étale`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections if
> and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on `S_étale`.

```lean
theorem hasFiniteGlobalGenerators_iff_smallEtaleAssociatedModule (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallEtale.associatedModule B S hS).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L275). The attribute's comment: “generated by finitely many global sections, small site S_smooth”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the small site
> `S_smooth`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections if
> and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on `S_smooth`.

```lean
theorem hasFiniteGlobalGenerators_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L288). The attribute's comment: “generated by finitely many global sections, small site S_syntomic”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the small site
> `S_syntomic`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections if
> and only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on
> `S_syntomic`.

```lean
theorem hasFiniteGlobalGenerators_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalGenerators_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByFinitelyManyGlobalSections.lean#L300). The attribute's comment: “generated by finitely many global sections, small site S_fppf”.

> **Descent, Lemma 05VG, generated by finitely many global sections (03DE (5)), on the small site
> `S_fppf`.**  A quasi-coherent `𝒪_S`-module `𝓕` is generated by finitely many global sections if and
> only if `𝓕^a` is generated by finitely many global sections as an `𝒪`-module on `S_fppf`.

```lean
theorem hasFiniteGlobalGenerators_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalGenerators (R := S.ringCatSheaf) 𝓕 ↔
      ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕).HasFiniteGlobalGenerators
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L80). The attribute's comment: “generated by global sections, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, generation by global sections, big Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `(Sch/S)_Zar`.

```lean
theorem isGeneratedByGlobalSections_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L92). The attribute's comment: “generated by global sections, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, generation by global sections, big étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `(Sch/S)_étale`.

```lean
theorem isGeneratedByGlobalSections_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L104). The attribute's comment: “generated by global sections, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, generation by global sections, big smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `(Sch/S)_smooth`.

```lean
theorem isGeneratedByGlobalSections_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L116). The attribute's comment: “generated by global sections, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, generation by global sections, big syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `(Sch/S)_syntomic`.

```lean
theorem isGeneratedByGlobalSections_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L128). The attribute's comment: “generated by global sections, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, generation by global sections, big fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `(Sch/S)_fppf`.

```lean
theorem isGeneratedByGlobalSections_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L142). The attribute's comment: “generated by global sections, small site S_Zar”.

> **Descent, Lemma 05VG, generation by global sections, small Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `S_Zar`.

```lean
theorem isGeneratedByGlobalSections_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L153). The attribute's comment: “generated by global sections, small site S_étale”.

> **Descent, Lemma 05VG, generation by global sections, small étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `S_étale`.

```lean
theorem isGeneratedByGlobalSections_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L169). The attribute's comment: “generated by global sections, small site S_smooth”.

> **Descent, Lemma 05VG, generation by global sections, small smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `S_smooth`.

```lean
theorem isGeneratedByGlobalSections_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L181). The attribute's comment: “generated by global sections, small site S_syntomic”.

> **Descent, Lemma 05VG, generation by global sections, small syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `S_syntomic`.

```lean
theorem isGeneratedByGlobalSections_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSections_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByGlobalSections.lean#L193). The attribute's comment: “generated by global sections, small site S_fppf”.

> **Descent, Lemma 05VG, generation by global sections, small fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by global sections if and only if `𝓕^a` is generated by global
> sections on `S_fppf`.

```lean
theorem isGeneratedByGlobalSections_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsGeneratedByGlobalSections
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L92). The attribute's comment: “generated by r global sections, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `(Sch/S)_Zar`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is
> generated by `r` global sections as an `𝒪`-module on the big Zariski site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L103). The attribute's comment: “generated by r global sections, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `(Sch/S)_étale`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is
> generated by `r` global sections as an `𝒪`-module on the big étale site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L114). The attribute's comment: “generated by r global sections, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `(Sch/S)_smooth`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is
> generated by `r` global sections as an `𝒪`-module on the big smooth site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L125). The attribute's comment: “generated by r global sections, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `(Sch/S)_syntomic`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is
> generated by `r` global sections as an `𝒪`-module on the big syntomic site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L136). The attribute's comment: “generated by r global sections, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `(Sch/S)_fppf`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is
> generated by `r` global sections as an `𝒪`-module on the big fppf site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L154). The attribute's comment: “generated by r global sections, small site S_Zar”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `S_Zar`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is generated by `r`
> global sections as an `𝒪`-module on the small Zariski site of `S`.  Quasi-coherence is the
> source's hypothesis;
> `AlgebraicGeometry.SmallZariski.isGeneratedByGlobalSectionsOfCard_iff_associatedModule` proves
> the equivalence without it.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_smallZariskiAssociatedModule
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((SmallZariski.associatedModule B S hS).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L166). The attribute's comment: “generated by r global sections, small site S_étale”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `S_étale`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is generated by `r`
> global sections as an `𝒪`-module on the small étale site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_smallEtaleAssociatedModule
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((SmallEtale.associatedModule B S hS).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L184). The attribute's comment: “generated by r global sections, small site S_smooth”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `S_smooth`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is generated by `r`
> global sections as an `𝒪`-module on the small smooth site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_smallFlatSiteAssociatedModule_smooth
    (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L195). The attribute's comment: “generated by r global sections, small site S_syntomic”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `S_syntomic`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is generated by `r`
> global sections as an `𝒪`-module on the small syntomic site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_smallFlatSiteAssociatedModule_syntomic
    (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isGeneratedByGlobalSectionsOfCard_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GeneratedByRGlobalSections.lean#L206). The attribute's comment: “generated by r global sections, small site S_fppf”.

> **Descent, Lemma 05VG, "generated by `r` global sections", on `S_fppf`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is generated by `r` global sections if and only if `𝓕^a` is generated by `r`
> global sections as an `𝒪`-module on the small fppf site of `S`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_smallFlatSiteAssociatedModule_fppf
    (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsGeneratedByGlobalSectionsOfCard
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L151). The attribute's comment: “having a global finite presentation, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, having a global finite presentation, big Zariski site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `(Sch/S)_Zar`.

```lean
theorem hasFiniteGlobalPresentation_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L164). The attribute's comment: “having a global finite presentation, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, having a global finite presentation, big étale site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `(Sch/S)_étale`.

```lean
theorem hasFiniteGlobalPresentation_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L177). The attribute's comment: “having a global finite presentation, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, having a global finite presentation, big smooth site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `(Sch/S)_smooth`.

```lean
theorem hasFiniteGlobalPresentation_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L190). The attribute's comment: “having a global finite presentation, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, having a global finite presentation, big syntomic site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `(Sch/S)_syntomic`.

```lean
theorem hasFiniteGlobalPresentation_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L203). The attribute's comment: “having a global finite presentation, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, having a global finite presentation, big fppf site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `(Sch/S)_fppf`.

```lean
theorem hasFiniteGlobalPresentation_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L218). The attribute's comment: “having a global finite presentation, small site S_Zar”.

> **Descent, Lemma 05VG, having a global finite presentation, small Zariski site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `S_Zar`.

```lean
theorem hasFiniteGlobalPresentation_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L230). The attribute's comment: “having a global finite presentation, small site S_étale”.

> **Descent, Lemma 05VG, having a global finite presentation, small étale site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `S_étale`.

```lean
theorem hasFiniteGlobalPresentation_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L246). The attribute's comment: “having a global finite presentation, small site S_smooth”.

> **Descent, Lemma 05VG, having a global finite presentation, small smooth site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `S_smooth`.

```lean
theorem hasFiniteGlobalPresentation_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L259). The attribute's comment: “having a global finite presentation, small site S_syntomic”.

> **Descent, Lemma 05VG, having a global finite presentation, small syntomic site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `S_syntomic`.

```lean
theorem hasFiniteGlobalPresentation_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasFiniteGlobalPresentation_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalFinitePresentation.lean#L272). The attribute's comment: “having a global finite presentation, small site S_fppf”.

> **Descent, Lemma 05VG, having a global finite presentation, small fppf site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global finite presentation if and only if `𝓕^a` has one on
> `S_fppf`.

```lean
theorem hasFiniteGlobalPresentation_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasFiniteGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasFiniteGlobalPresentation
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L130). The attribute's comment: “having a global presentation, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, having a global presentation, big Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `(Sch/S)_Zar`.

```lean
theorem hasGlobalPresentation_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L143). The attribute's comment: “having a global presentation, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, having a global presentation, big étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `(Sch/S)_étale`.

```lean
theorem hasGlobalPresentation_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L156). The attribute's comment: “having a global presentation, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, having a global presentation, big smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `(Sch/S)_smooth`.

```lean
theorem hasGlobalPresentation_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L169). The attribute's comment: “having a global presentation, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, having a global presentation, big syntomic site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `(Sch/S)_syntomic`.

```lean
theorem hasGlobalPresentation_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L182). The attribute's comment: “having a global presentation, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, having a global presentation, big fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `(Sch/S)_fppf`.

```lean
theorem hasGlobalPresentation_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L197). The attribute's comment: “having a global presentation, small site S_Zar”.

> **Descent, Lemma 05VG, having a global presentation, small Zariski site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `S_Zar`.

```lean
theorem hasGlobalPresentation_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L209). The attribute's comment: “having a global presentation, small site S_étale”.

> **Descent, Lemma 05VG, having a global presentation, small étale site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `S_étale`.

```lean
theorem hasGlobalPresentation_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L225). The attribute's comment: “having a global presentation, small site S_smooth”.

> **Descent, Lemma 05VG, having a global presentation, small smooth site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `S_smooth`.

```lean
theorem hasGlobalPresentation_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L238). The attribute's comment: “having a global presentation, small site S_syntomic”.

> **Descent, Lemma 05VG, having a global presentation, small syntomic site.**  A
> quasi-coherent `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global
> presentation on `S_syntomic`.

```lean
theorem hasGlobalPresentation_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.hasGlobalPresentation_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/GlobalPresentation.lean#L251). The attribute's comment: “having a global presentation, small site S_fppf”.

> **Descent, Lemma 05VG, having a global presentation, small fppf site.**  A quasi-coherent
> `𝒪_S`-module `𝓕` has a global presentation if and only if `𝓕^a` has a global presentation on
> `S_fppf`.

```lean
theorem hasGlobalPresentation_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.HasGlobalPresentation (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.HasGlobalPresentation
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L91). The attribute's comment: “locally generated by r sections, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `(Sch/S)_Zar`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on the big Zariski site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L102). The attribute's comment: “locally generated by r sections, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `(Sch/S)_étale`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on the big étale site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L113). The attribute's comment: “locally generated by r sections, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `(Sch/S)_smooth`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on the big smooth site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L124). The attribute's comment: “locally generated by r sections, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `(Sch/S)_syntomic`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on the big syntomic site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L135). The attribute's comment: “locally generated by r sections, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `(Sch/S)_fppf`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on the big fppf site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L153). The attribute's comment: “locally generated by r sections, small site S_Zar”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `S_Zar`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is locally generated
> by `r` sections as an `𝒪`-module on the small Zariski site of `S`.  Quasi-coherence is the
> source's hypothesis;
> `AlgebraicGeometry.SmallZariski.isLocallyGeneratedByOnSite_iff_associatedModule` proves the
> equivalence without it.

```lean
theorem isLocallyGeneratedByOnSite_iff_smallZariskiAssociatedModule (B : BigZariskiSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((SmallZariski.associatedModule B S hS).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L164). The attribute's comment: “locally generated by r sections, small site S_étale”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `S_étale`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is locally generated
> by `r` sections as an `𝒪`-module on the small étale site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_smallEtaleAssociatedModule (B : BigEtaleSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules) [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((SmallEtale.associatedModule B S hS).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L181). The attribute's comment: “locally generated by r sections, small site S_smooth”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `S_smooth`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on the small smooth site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_smallFlatSiteAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L192). The attribute's comment: “locally generated by r sections, small site S_syntomic”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `S_syntomic`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on the small syntomic site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_smallFlatSiteAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedByOnSite_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedByR.lean#L203). The attribute's comment: “locally generated by r sections, small site S_fppf”.

> **Descent, Lemma 05VG, "locally generated by `r` sections", on `S_fppf`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is locally generated by `r` sections if and only if `𝓕^a` is locally generated
> by `r` sections as an `𝒪`-module on the small fppf site of `S`.

```lean
theorem isLocallyGeneratedByOnSite_iff_smallFlatSiteAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕) r
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_zariski`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L78). The attribute's comment: “locally generated by sections, big site (Sch/S)_Zar”.

> **Descent, Lemma 05VG, locally generated by sections, big site `(Sch/S)_Zar`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `(Sch/S)_Zar`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_zariski (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .zariski).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L89). The attribute's comment: “locally generated by sections, big site (Sch/S)_étale”.

> **Descent, Lemma 05VG, locally generated by sections, big site `(Sch/S)_étale`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `(Sch/S)_étale`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_etale (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .etale).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L100). The attribute's comment: “locally generated by sections, big site (Sch/S)_smooth”.

> **Descent, Lemma 05VG, locally generated by sections, big site `(Sch/S)_smooth`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `(Sch/S)_smooth`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_smooth (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L111). The attribute's comment: “locally generated by sections, big site (Sch/S)_syntomic”.

> **Descent, Lemma 05VG, locally generated by sections, big site `(Sch/S)_syntomic`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `(Sch/S)_syntomic`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_syntomic (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L122). The attribute's comment: “locally generated by sections, big site (Sch/S)_fppf”.

> **Descent, Lemma 05VG, locally generated by sections, big site `(Sch/S)_fppf`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `(Sch/S)_fppf`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_baseAssociatedModule_fppf (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((BigFppfOver.baseAssociatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_smallZariskiAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L135). The attribute's comment: “locally generated by sections, small site S_Zar”.

> **Descent, Lemma 05VG, locally generated by sections, small site `S_Zar`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `S_Zar`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_smallZariskiAssociatedModule
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((SmallZariski.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_smallEtaleAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L147). The attribute's comment: “locally generated by sections, small site S_étale”.

> **Descent, Lemma 05VG, locally generated by sections, small site `S_étale`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `S_étale`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_smallEtaleAssociatedModule
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((SmallEtale.associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_smallFlatSiteAssociatedModule_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L163). The attribute's comment: “locally generated by sections, small site S_smooth”.

> **Descent, Lemma 05VG, locally generated by sections, small site `S_smooth`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `S_smooth`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_smallFlatSiteAssociatedModule_smooth
    (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((SmallFlatSite.associatedModule B S hS .smooth).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_smallFlatSiteAssociatedModule_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L174). The attribute's comment: “locally generated by sections, small site S_syntomic”.

> **Descent, Lemma 05VG, locally generated by sections, small site `S_syntomic`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `S_syntomic`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_smallFlatSiteAssociatedModule_syntomic
    (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((SmallFlatSite.associatedModule B S hS .syntomic).obj 𝓕)
```

**`AlgebraicGeometry.Cells05VG.isLocallyGeneratedBySectionsOnSite_iff_smallFlatSiteAssociatedModule_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/Cells05VG/LocallyGeneratedBySections.lean#L185). The attribute's comment: “locally generated by sections, small site S_fppf”.

> **Descent, Lemma 05VG, locally generated by sections, small site `S_fppf`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally
> generated by sections as an `𝒪`-module on `S_fppf`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_smallFlatSiteAssociatedModule_fppf
    (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((SmallFlatSite.associatedModule B S hS .fppf).obj 𝓕)
```

**`AlgebraicGeometry.BigFppfOver.isFinitePresentationOnSite_baseAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean#L88). The attribute's comment: “of finite presentation (03DL (7)), on (Sch/S)_τ for every τ ∈ {Zariski, étale, smooth, syntomic, fppf}, at the functor 𝓕 ↦ 𝓕ᵃ of 03DX”.

> **Descent, Lemma 05VG for "of finite presentation" (Modules on Sites, Definition 03DL (7)),
> on the big site `(Sch/S)_τ`, for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  A
> quasi-coherent `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite
> presentation as an `𝒪`-module on `(Sch/S)_τ`, where `𝓕 ↦ 𝓕^a` is the functor of Descent,
> Proposition 03DX (1).

```lean
theorem isFinitePresentationOnSite_baseAssociatedModule_iff (τ : SiteKind) (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((baseAssociatedModule B S hS τ).obj 𝓕).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.SmallZariski.isFinitePresentationOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean#L107). The attribute's comment: “of finite presentation (03DL (7)), on S_Zar, at the functor 𝓕 ↦ 𝓕ᵃ of 03DX”.

> **Descent, Lemma 05VG for "of finite presentation" (Modules on Sites, Definition 03DL (7)),
> on the small Zariski site `S_Zar`.**  An `𝒪_S`-module `𝓕` is of finite presentation if and
> only if `𝓕^a` is of finite presentation as an `𝒪`-module on `S_Zar`, where `𝓕 ↦ 𝓕^a` is the
> functor of Descent, Proposition 03DX (2).  On this site no quasi-coherence is needed.

```lean
theorem isFinitePresentationOnSite_iff_associatedModule (𝓕 : S.Modules) :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((associatedModule B S hS).obj 𝓕).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.SmallEtale.isFinitePresentationOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean#L125). The attribute's comment: “of finite presentation (03DL (7)), on S_étale, at the functor 𝓕 ↦ 𝓕ᵃ of 03DX”.

> **Descent, Lemma 05VG for "of finite presentation" (Modules on Sites, Definition 03DL (7)),
> on the small étale site `S_étale`.**  A quasi-coherent `𝒪_S`-module `𝓕` is of finite
> presentation if and only if `𝓕^a` is of finite presentation as an `𝒪`-module on `S_étale`, where
> `𝓕 ↦ 𝓕^a` is the functor of Descent, Proposition 03DX (2).

```lean
theorem isFinitePresentationOnSite_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((associatedModule B S hS).obj 𝓕).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.SmallFlatSite.isFinitePresentationOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean#L144). The attribute's comment: “of finite presentation (03DL (7)), on S_τ for every τ ∈ {smooth, syntomic, fppf}, at the functor 𝓕 ↦ 𝓕ᵃ”.

> **Descent, Lemma 05VG for "of finite presentation" (Modules on Sites, Definition 03DL (7)),
> on the small site `S_τ`, for every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is of finite presentation if and only if `𝓕^a` is of finite presentation as an
> `𝒪`-module on `S_τ`, where `𝓕 ↦ 𝓕^a` is the pullback along `(S_τ, 𝒪) ⟶ (S_Zar, 𝒪_S)`.

```lean
theorem isFinitePresentationOnSite_iff_associatedModule (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
      ((associatedModule B S hS κ).obj 𝓕).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.Scheme.Modules.isFinitePresentationOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/FinitePresentationAgreement03DX.lean#L168). The attribute's comment: “of finite presentation (03DL (7)): 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "of finite presentation" (Modules on Sites,
> Definition 03DL (7)).**  For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` is of finite presentation
> if and only if `𝓕^a` is of finite presentation as an `𝒪`-module, at each of the functors
> `𝓕 ↦ 𝓕^a` of Descent, Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.  Both sides are finite presentation in the sense
> of Definition 03DL (7), `SheafOfModules.IsFinitePresentationOnSite`; on the left it is taken on
> the site of opens of `S`.

```lean
theorem isFinitePresentationOnSite_iff_associatedModule (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
        ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕).IsFinitePresentationOnSite) ∧
      (SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
        ((SmallZariski.associatedModule Bz S hz).obj 𝓕).IsFinitePresentationOnSite) ∧
      (SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
        ((SmallEtale.associatedModule Be S he).obj 𝓕).IsFinitePresentationOnSite) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsFinitePresentationOnSite (R := S.ringCatSheaf) 𝓕 ↔
        ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.BigFppfOver.isGeneratedByGlobalSections_iff_baseAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L316). The attribute's comment: “generated by global sections, big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (3), on the big site.**  A
> quasi-coherent `𝒪_S`-module is generated by global sections if and only if `𝓕^a` is generated by
> global sections as an `𝒪`-module on `(Sch/S)_τ`.

```lean
theorem isGeneratedByGlobalSections_iff_baseAssociatedModule (τ : SiteKind)
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsGeneratedByGlobalSections ↔
      ((baseAssociatedModuleQcoh B S hS τ).obj F).IsGeneratedByGlobalSections
```

**`AlgebraicGeometry.BigFppfOver.isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L332). The attribute's comment: “generated by r global sections, big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (4), on the big site.**  A
> quasi-coherent `𝒪_S`-module is generated by `r` global sections if and only if `𝓕^a` is, with
> the same `r`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule (τ : SiteKind)
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) (r : ℕ) :
    F.obj.IsGeneratedByGlobalSectionsOfCard r ↔
      ((baseAssociatedModuleQcoh B S hS τ).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.BigFppfOver.exists_isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L348). The attribute's comment: “generated by finitely many global sections, big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (5), on the big site.**  A
> quasi-coherent `𝒪_S`-module is generated by finitely many global sections if and only if `𝓕^a`
> is.

```lean
theorem exists_isGeneratedByGlobalSectionsOfCard_iff_baseAssociatedModule (τ : SiteKind)
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    (∃ r : ℕ, F.obj.IsGeneratedByGlobalSectionsOfCard r) ↔
      ∃ r : ℕ, ((baseAssociatedModuleQcoh B S hS τ).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.BigFppfOver.isPresentedByGlobalSections_iff_baseAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L372). The attribute's comment: “global presentation, big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (6), on the big site.**  A
> quasi-coherent `𝒪_S`-module has a global presentation if and only if `𝓕^a` has one as an
> `𝒪`-module on `(Sch/S)_τ`, with the same two index types.

```lean
theorem isPresentedByGlobalSections_iff_baseAssociatedModule (τ : SiteKind)
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsPresentedByGlobalSections ↔
      ((baseAssociatedModuleQcoh B S hS τ).obj F).IsPresentedByGlobalSections
```

**`AlgebraicGeometry.BigFppfOver.isFinitelyPresentedByGlobalSections_iff_baseAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L389). The attribute's comment: “finite global presentation, big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (7), on the big site.**  A
> quasi-coherent `𝒪_S`-module has a finite global presentation if and only if `𝓕^a` has one,
> with the same two finite index types.

```lean
theorem isFinitelyPresentedByGlobalSections_iff_baseAssociatedModule (τ : SiteKind)
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsFinitelyPresentedByGlobalSections ↔
      ((baseAssociatedModuleQcoh B S hS τ).obj F).IsFinitelyPresentedByGlobalSections
```

**`AlgebraicGeometry.SmallEtale.isGeneratedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L420). The attribute's comment: “generated by global sections, small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (3), on the small étale
> site.**  A quasi-coherent `𝒪_S`-module is generated by global sections if and only if `𝓕^a` is
> generated by global sections as an `𝒪`-module on `S_étale`.

```lean
theorem isGeneratedByGlobalSections_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsGeneratedByGlobalSections ↔
      ((associatedModuleQcoh B S hS).obj F).IsGeneratedByGlobalSections
```

**`AlgebraicGeometry.SmallEtale.isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L436). The attribute's comment: “generated by r global sections, small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (4), on the small étale
> site.**  A quasi-coherent `𝒪_S`-module is generated by `r` global sections if and only if `𝓕^a`
> is, with the same `r`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) (r : ℕ) :
    F.obj.IsGeneratedByGlobalSectionsOfCard r ↔
      ((associatedModuleQcoh B S hS).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.SmallEtale.exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L452). The attribute's comment: “generated by finitely many global sections, small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (5), on the small étale
> site.**  A quasi-coherent `𝒪_S`-module is generated by finitely many global sections if and
> only if `𝓕^a` is.

```lean
theorem exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    (∃ r : ℕ, F.obj.IsGeneratedByGlobalSectionsOfCard r) ↔
      ∃ r : ℕ, ((associatedModuleQcoh B S hS).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.SmallEtale.isPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L476). The attribute's comment: “global presentation, small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (6), on the small étale
> site.**  A quasi-coherent `𝒪_S`-module has a global presentation if and only if `𝓕^a` has one
> as an `𝒪`-module on `S_étale`, with the same two index types.

```lean
theorem isPresentedByGlobalSections_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsPresentedByGlobalSections ↔
      ((associatedModuleQcoh B S hS).obj F).IsPresentedByGlobalSections
```

**`AlgebraicGeometry.SmallEtale.isFinitelyPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalGenerationComparison.lean#L493). The attribute's comment: “finite global presentation, small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (7), on the small étale
> site.**  A quasi-coherent `𝒪_S`-module has a finite global presentation if and only if `𝓕^a`
> has one, with the same two finite index types.

```lean
theorem isFinitelyPresentedByGlobalSections_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsFinitelyPresentedByGlobalSections ↔
      ((associatedModuleQcoh B S hS).obj F).IsFinitelyPresentedByGlobalSections
```

**`AlgebraicGeometry.BigFppfOver.isFree_iff_baseAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean#L156). The attribute's comment: “free, big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (1), on the big site.**  A
> quasi-coherent `𝒪_S`-module is free if and only if `𝓕^a` is free as an `𝒪`-module on
> `(Sch/S)_τ`.

```lean
theorem isFree_iff_baseAssociatedModule (τ : SiteKind)
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsFree ↔ ((baseAssociatedModuleQcoh B S hS τ).obj F).IsFree
```

**`AlgebraicGeometry.BigFppfOver.isFiniteFree_iff_baseAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean#L169). The attribute's comment: “finite free, big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (2), on the big site.**  A
> quasi-coherent `𝒪_S`-module is finite free if and only if `𝓕^a` is finite free as an
> `𝒪`-module on `(Sch/S)_τ`, and with the same rank.

```lean
theorem isFiniteFree_iff_baseAssociatedModule (τ : SiteKind)
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    SheafOfModules.IsFiniteFree S.ringCatSheaf F.obj ↔
      SheafOfModules.IsFiniteFree (FibredSite.baseRingStructureSheaf B S hS τ)
        ((baseAssociatedModuleQcoh B S hS τ).obj F)
```

**`AlgebraicGeometry.SmallEtale.isFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean#L204). The attribute's comment: “free, small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (1), on the small étale
> site.**  A quasi-coherent `𝒪_S`-module is free if and only if `𝓕^a` is free as an
> `𝒪`-module on `S_étale`.

```lean
theorem isFree_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsFree ↔ ((associatedModuleQcoh B S hS).obj F).IsFree
```

**`AlgebraicGeometry.SmallEtale.isFiniteFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/GlobalTypesComparison.lean#L216). The attribute's comment: “finite free, small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (2), on the small étale
> site.**  A quasi-coherent `𝒪_S`-module is finite free if and only if `𝓕^a` is finite free as
> an `𝒪`-module on `S_étale`, and with the same rank.

```lean
theorem isFiniteFree_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    SheafOfModules.IsFiniteFree S.ringCatSheaf F.obj ↔
      SheafOfModules.IsFiniteFree (structureSheaf B S hS)
        ((associatedModuleQcoh B S hS).obj F)
```

**`AlgebraicGeometry.BigFppfOver.isLocallyGeneratedBySectionsOnSite_baseAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/LocalGenerationBySectionsAgreement.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/LocalGenerationBySectionsAgreement.lean#L144). The attribute's comment: “locally generated by sections (03DL (3)), big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (3), at the big site
> `(Sch/S)_τ`, for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  A quasi-coherent
> `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is locally generated by
> sections as an `𝒪`-module on `(Sch/S)_τ`.
>
> Both sides hold, under the source's quasi-coherence hypothesis and nothing else.  On the scheme
> side the quasi-coherent data of `𝓕` is `SheafOfModules.IsQuasicoherent.nonempty_quasicoherentData`;
> on the big site it is `AlgebraicGeometry.BigFppfOver.baseQuasicoherentDataAssociatedModule`, the
> covering argument of Stacks 03DV, clause (1).  Each then gives local generation by sections
> through `Stacks.SheafOfModules.isLocallyGeneratedBySectionsOnSite_of_localGeneratorsData`.
>
> The clause string records the scope: this is clause 03DL (3) of 05VG at the **big** site, at all
> five `τ`.  The two small sites are
> `AlgebraicGeometry.SmallEtale.isLocallyGeneratedBySectionsOnSite_associatedModule_iff` and
> `AlgebraicGeometry.SmallZariski.isLocallyGeneratedBySectionsOnSite_associatedModule_iff`.

```lean
public theorem isLocallyGeneratedBySectionsOnSite_baseAssociatedModule_iff (τ : SiteKind)
    (𝓕 : S.Modules) (h𝓕 : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite
        ((baseAssociatedModule B S hS τ).obj 𝓕)
```

**`AlgebraicGeometry.SmallEtale.isLocallyGeneratedBySectionsOnSite_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/LocalGenerationBySectionsAgreement.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/LocalGenerationBySectionsAgreement.lean#L173). The attribute's comment: “locally generated by sections (03DL (3)), small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (3), at the small étale site.**
> A quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a` is
> locally generated by sections as an `𝒪`-module on `S_étale`.
>
> Both sides hold, under the source's quasi-coherence hypothesis and nothing else: the
> quasi-coherent data of `𝓕^a` is `AlgebraicGeometry.SmallEtale.quasicoherentDataAssociatedModule`,
> the covering argument of Stacks 03DV, clause (2), at `τ = étale`.
>
> The clause string records the scope: this is clause 03DL (3) of 05VG at the **small** site for
> `τ = étale`.  The small Zariski site is
> `AlgebraicGeometry.SmallZariski.isLocallyGeneratedBySectionsOnSite_associatedModule_iff`.

```lean
public theorem isLocallyGeneratedBySectionsOnSite_associatedModule_iff (𝓕 : S.Modules)
    (h𝓕 : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.SmallZariski.isLocallyGeneratedBySectionsOnSite_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/LocalGenerationBySectionsAgreement.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/LocalGenerationBySectionsAgreement.lean#L202). The attribute's comment: “locally generated by sections (03DL (3)), small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (3), at the small Zariski
> site.**  A quasi-coherent `𝒪_S`-module `𝓕` is locally generated by sections if and only if `𝓕^a`
> is locally generated by sections as an `𝒪`-module on `S_Zar`.
>
> Both sides hold, under the source's quasi-coherence hypothesis and nothing else: the
> quasi-coherent data of `𝓕^a` is
> `AlgebraicGeometry.SmallZariski.quasicoherentDataAssociatedModule`, the covering argument of
> Stacks 03DV, clause (2), at `τ = Zariski`.
>
> The clause string records the scope: this is clause 03DL (3) of 05VG at the **small** site for
> `τ = Zariski`.  The small étale site is
> `AlgebraicGeometry.SmallEtale.isLocallyGeneratedBySectionsOnSite_associatedModule_iff`.

```lean
public theorem isLocallyGeneratedBySectionsOnSite_associatedModule_iff (𝓕 : S.Modules)
    (h𝓕 : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L139). The attribute's comment: “free: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "free" (Modules on Sites, Definition 03DE (1)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "free" if and only if `𝓕^a` has it as
> an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent, Proposition 03DX: on the
> big site `(Sch/S)_τ` for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on
> `S_étale`, and on the small site `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isFree_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFree ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFree ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFree ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsFree (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFree ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isFiniteFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L161). The attribute's comment: “finite free: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "finite free" (Modules on Sites, Definition 03DE
> (2)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "finite free" if and only if `𝓕^a` has
> it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent, Proposition 03DX: on
> the big site `(Sch/S)_τ` for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on
> `S_étale`, and on the small site `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isFiniteFree_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
        SheafOfModules.IsFiniteFree _ ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
        SheafOfModules.IsFiniteFree _ ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
        SheafOfModules.IsFiniteFree _ ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsFiniteFree S.ringCatSheaf 𝓕 ↔
        SheafOfModules.IsFiniteFree _ ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isGeneratedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L184). The attribute's comment: “generated by global sections: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "generated by global sections" (Modules on Sites,
> Definition 03DE (3)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "generated by global sections" if and
> only if `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent,
> Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isGeneratedByGlobalSections_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsGeneratedByGlobalSections
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsGeneratedByGlobalSections
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsGeneratedByGlobalSections ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsGeneratedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsGeneratedByGlobalSections
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L210). The attribute's comment: “generated by r global sections: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "generated by r global sections" (Modules on Sites,
> Definition 03DE (4)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "generated by r global sections" if and
> only if `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent,
> Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_associatedModule (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    (∀ τ : SiteKind, SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕) r) ∧
      (SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕) r) ∧
      (SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((SmallEtale.associatedModule Be S he).obj 𝓕) r) ∧
      ∀ κ : FlatSiteKind,
        SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕) r
```

**`AlgebraicGeometry.Scheme.Modules.exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L241). The attribute's comment: “generated by finitely many global sections: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "generated by finitely many global sections" (Modules
> on Sites, Definition 03DE (5)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "generated by finitely many global
> sections" if and only if `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors
> `𝓕 ↦ 𝓕^a` of Descent, Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind,
      (∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r) ↔
        (∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕) r)) ∧
      ((∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r) ↔
        (∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕) r)) ∧
      ((∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r) ↔
        (∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((SmallEtale.associatedModule Be S he).obj 𝓕) r)) ∧
      ∀ κ : FlatSiteKind,
        (∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard (R := S.ringCatSheaf) 𝓕 r) ↔
        (∃ r : ℕ, SheafOfModules.IsGeneratedByGlobalSectionsOfCard
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕) r)
```

**`AlgebraicGeometry.Scheme.Modules.isPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L273). The attribute's comment: “having a global presentation: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "having a global presentation" (Modules on Sites,
> Definition 03DE (6)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "having a global presentation" if and
> only if `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent,
> Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isPresentedByGlobalSections_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsPresentedByGlobalSections
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsPresentedByGlobalSections
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsPresentedByGlobalSections ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsPresentedByGlobalSections
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isFinitelyPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L299). The attribute's comment: “having a global finite presentation: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "having a global finite presentation" (Modules on
> Sites, Definition 03DE (7)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "having a global finite presentation"
> if and only if `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of
> Descent, Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isFinitelyPresentedByGlobalSections_iff_associatedModule (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsFinitelyPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitelyPresentedByGlobalSections
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsFinitelyPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitelyPresentedByGlobalSections
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsFinitelyPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitelyPresentedByGlobalSections
          ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind,
        SheafOfModules.IsFinitelyPresentedByGlobalSections (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitelyPresentedByGlobalSections
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L329). The attribute's comment: “finite locally free: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "finite locally free" (Modules on Sites, Definition
> 03DL (2)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "finite locally free" if and only if
> `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent, Proposition
> 03DX: on the big site `(Sch/S)_τ` for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on
> `S_Zar`, on `S_étale`, and on the small site `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteLocallyFreeOnSite
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteLocallyFreeOnSite ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteLocallyFreeOnSite ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteLocallyFreeOnSite
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isLocallyGeneratedBySectionsOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L355). The attribute's comment: “locally generated by sections: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "locally generated by sections" (Modules on Sites,
> Definition 03DL (3)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "locally generated by sections" if and
> only if `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent,
> Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_associatedModule (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsLocallyGeneratedBySectionsOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsLocallyGeneratedBySectionsOnSite
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsLocallyGeneratedBySectionsOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsLocallyGeneratedBySectionsOnSite
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsLocallyGeneratedBySectionsOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsLocallyGeneratedBySectionsOnSite
          ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind,
        SheafOfModules.IsLocallyGeneratedBySectionsOnSite (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsLocallyGeneratedBySectionsOnSite
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isLocallyGeneratedByOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L384). The attribute's comment: “locally generated by r sections: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "locally generated by r sections" (Modules on Sites,
> Definition 03DL (4)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "locally generated by r sections" if
> and only if `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent,
> Proposition 03DX: on the big site `(Sch/S)_τ` for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and on the small site
> `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isLocallyGeneratedByOnSite_iff_associatedModule (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    (∀ τ : SiteKind, SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsLocallyGeneratedByOnSite
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕) r) ∧
      (SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsLocallyGeneratedByOnSite
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕) r) ∧
      (SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsLocallyGeneratedByOnSite ((SmallEtale.associatedModule Be S he).obj 𝓕) r) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
        SheafOfModules.IsLocallyGeneratedByOnSite
          ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕) r
```

**`AlgebraicGeometry.Scheme.Modules.isFiniteType_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L410). The attribute's comment: “finite type: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "finite type" (Modules on Sites, Definition 03DL
> (5)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "finite type" if and only if `𝓕^a` has
> it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent, Proposition 03DX: on
> the big site `(Sch/S)_τ` for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on
> `S_étale`, and on the small site `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isFiniteType_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsFiniteType (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteType ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsFiniteType (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteType ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsFiniteType (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteType ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsFiniteType (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFiniteType ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isFinitePresentation_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L432). The attribute's comment: “of finite presentation: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "of finite presentation" (Modules on Sites, Definition
> 03DL (7)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` has the property "of finite presentation" if and only if
> `𝓕^a` has it as an `𝒪`-module, at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent, Proposition
> 03DX: on the big site `(Sch/S)_τ` for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on
> `S_Zar`, on `S_étale`, and on the small site `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isFinitePresentation_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind, SheafOfModules.IsFinitePresentation (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitePresentation ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (SheafOfModules.IsFinitePresentation (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitePresentation ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsFinitePresentation (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitePresentation ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind, SheafOfModules.IsFinitePresentation (R := S.ringCatSheaf) 𝓕 ↔
        SheafOfModules.IsFinitePresentation ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isFlat_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L453). The attribute's comment: “flat: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on (Sch/S)_τ for every τ, on S_Zar, on S_étale, and on S_τ for τ ∈ {smooth, syntomic, fppf}”.

> **Descent, Lemma 05VG, for the property "flat" (Modules on Sites, Definition 03ER (3)).**
> For a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module,
> at each of the comparison functors `𝓕 ↦ 𝓕^a` of Descent, Proposition 03DX: on the big site
> `(Sch/S)_τ` for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, on `S_Zar`, on `S_étale`, and
> on the small site `S_τ` for every `τ ∈ {smooth, syntomic, fppf}`.

```lean
theorem isFlat_iff_associatedModule (𝓕 : S.Modules) [h𝓕 : 𝓕.IsQuasicoherent] :
    (∀ τ : SiteKind,
      Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
        Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
          (O := (BigFppfOver.baseRingedSite Bf S hf τ).O)
          ((BigFppfOver.baseAssociatedModule Bf S hf τ).obj 𝓕)) ∧
      (Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
        Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u} (O := (smallZariskiRingedSite Bz S hz).O)
          ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
        Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u} (O := (smallEtaleRingedSite Be S he).O)
          ((SmallEtale.associatedModule Be S he).obj 𝓕)) ∧
      ∀ κ : FlatSiteKind,
        Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕 ↔
          Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u}
            (O := (SmallFlatSite.ringedSite Bf S hf κ).O)
            ((SmallFlatSite.associatedModule Bf S hf κ).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isCoherent_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L481). The attribute's comment: “coherent, S locally Noetherian: 𝓕 has 𝒫 ⇔ 𝓕ᵃ has 𝒫 on S_Zar and on S_étale”.

> **Descent, Lemma 05VG, for the property "coherent" (Modules on Sites, Definition 03DL (8)).**
> For a locally Noetherian scheme `S` and a quasi-coherent `𝒪_S`-module `𝓕`, `𝓕` is coherent if and
> only if `𝓕^a` is coherent as an `𝒪`-module, at the comparison functors `𝓕 ↦ 𝓕^a` of Descent,
> Proposition 03DX for the small sites `S_Zar` and `S_étale`. These are the sites, and locally
> Noetherian is the hypothesis, under which the source asserts the coherent case.

```lean
theorem isCoherent_iff_associatedModule [IsLocallyNoetherian S] (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    (𝓕.IsCoherent ↔
        SheafOfModules.IsCoherentOnSite ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (𝓕.IsCoherent ↔
        SheafOfModules.IsCoherentOnSite ((SmallEtale.associatedModule Be S he).obj 𝓕))
```

**`AlgebraicGeometry.SmallEtale.isFiniteLocallyFree_of_isFiniteLocallyFreeOnSite_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteLocallyFree.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteLocallyFree.lean#L319). The attribute's comment: “finite locally free, τ = étale, small sites: the reflection half”.

> **Stacks 05VG for the clause 03DL (2) at `τ = étale`, the reflection half.**  A
> quasi-coherent `𝒪_S`-module whose associated module on the small étale site of `S` is finite
> locally free is finite locally free.

```lean
theorem isFiniteLocallyFree_of_isFiniteLocallyFreeOnSite_associatedModule
    (𝓕 : S.Modules) [𝓕.IsQuasicoherent]
    (h : SheafOfModules.IsFiniteLocallyFreeOnSite ((associatedModule B S hS).obj 𝓕)) :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} 𝓕
```

**`AlgebraicGeometry.SmallEtale.isFiniteLocallyFreeOnSite_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteLocallyFree.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteLocallyFree.lean#L343). The attribute's comment: “finite locally free, τ = étale, small sites: the forward half”.

> **Stacks 05VG for the clause 03DL (2) at `τ = étale`, the forward half.**  The associated
> module on the small étale site of a finite locally free `𝒪_S`-module is finite locally free.
>
> Stacks 03DN tests the conclusion on a single family covering the final object.  A finite locally
> free `𝓕` is finite free over the members of some Zariski covering of `S`; the images of those
> opens in `S_étale` cover its final object by
> `AlgebraicGeometry.SmallEtale.coversTop_opensToSmallEtale_ulift`, and over each of them `𝓕^a` is
> the pullback of `𝓕|_V` along the localized comparison of structure sheaves by Stacks 03DV
> (`AlgebraicGeometry.SmallEtale.associatedModuleOverObjIso`), which is finite free because a
> pullback of modules carries a finite free module to a finite free one.

```lean
theorem isFiniteLocallyFreeOnSite_associatedModule (𝓕 : S.Modules)
    (h : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} 𝓕) :
    SheafOfModules.IsFiniteLocallyFreeOnSite ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.SmallEtale.isFiniteLocallyFreeOnSite_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteLocallyFree.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFiniteLocallyFree.lean#L398). The attribute's comment: “finite locally free, τ = étale, small sites”.

> **Stacks 05VG for the clause 03DL (2) at `τ = étale`.**  A quasi-coherent `𝒪_S`-module is
> finite locally free if and only if its associated module on the small étale site of `S` is.

```lean
theorem isFiniteLocallyFreeOnSite_associatedModule_iff (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite ((associatedModule B S hS).obj 𝓕) ↔
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} 𝓕
```

**`AlgebraicGeometry.SmallEtale.isFiniteType_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFinitenessAgreement.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFinitenessAgreement.lean#L180). The attribute's comment: “finite type (03DL (5)), small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (5), at the small étale site.**
> An `𝒪_S`-module `𝓕` is of finite type if and only if `𝓕ᵃ` is of finite type as an `𝒪`-module on
> `S_étale`.
>
> Both implications are Stacks 08HD in the categorical rendering of 03DL (5),
> `AlgebraicGeometry.SmallEtale.isFiniteTypeOnSite_associatedModule` and
> `AlgebraicGeometry.SmallEtale.isFiniteTypeOnSite_of_associatedModule`; the comparison of that
> rendering with Mathlib's `SheafOfModules.IsFiniteType` is
> `Stacks.SheafOfModules.isFiniteTypeOnSite_of_isFiniteType` in one direction and
> `Stacks.SheafOfModules.isFiniteType_of_isFiniteTypeOnSite` in the other.
>
> The clause string records the scope: this is clause 03DL (5) of 05VG at the **small** site for
> `τ = étale`.  The small Zariski site is
> `AlgebraicGeometry.SmallZariski.isFiniteType_iff_associatedModule`.  No quasi-coherence is
> assumed, so this is the clause over a weaker hypothesis than the source's.

```lean
public theorem isFiniteType_associatedModule_iff (𝓕 : S.Modules) :
    SheafOfModules.IsFiniteType 𝓕 ↔
      SheafOfModules.IsFiniteType ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.SmallEtale.isFinitePresentation_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFinitePresentation.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFinitePresentation.lean#L308). The attribute's comment: “finite presentation; the local clause 03DL (7) of the small-site comparison at τ = étale, for a quasi-coherent module on a scheme, with the comparison read as the associated-module functor of Stacks 03DU (4) rather than as a morphism of ringed topoi”.

> **Stacks 05VG for Modules on Sites, Definition 03DL (7) at `τ = étale` on the small
> site.**  A quasi-coherent `𝒪_S`-module is of finite presentation if and only if its associated
> module on the small étale site of `S` is of finite presentation.
>
> The forward implication is
> `AlgebraicGeometry.SmallEtale.isFinitePresentation_associatedModule_of_isFinitePresentation`
> and needs no quasi-coherence; the reverse one is
> `AlgebraicGeometry.SmallEtale.isFinitePresentation_of_isFinitePresentation_associatedModule`,
> which goes through the reflection step and fpqc descent on `S`.

```lean
theorem isFinitePresentation_associatedModule_iff (𝓕 : S.Modules)
    (h𝓕 : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    SheafOfModules.IsFinitePresentation (R := S.ringCatSheaf) 𝓕 ↔
      ((associatedModule B S hS).obj 𝓕).IsFinitePresentation
```

**`AlgebraicGeometry.SmallEtale.isFlat_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFlatAgreement.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFlatAgreement.lean#L134). The attribute's comment: “flat (03ER (3)), small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3), on the small étale site.**
> A sheaf of `𝒪_S`-modules is flat if and only if `𝓕ᵃ` is flat as an `𝒪`-module on `S_étale`.
>
> The `only if` half is Stacks 05VD at `ε`; the `if` half is étale descent of flatness, in the form
> `Stacks.Sheaves.RingedToposModules.isFlat_of_isFlat_pullbackModules` — a pullback of sheaves of
> modules which preserves and reflects monomorphisms reflects flatness.  Both hypotheses hold at
> `ε` by the exactness and zero-detection assertions of Stacks 08H8, recorded above as instances.
>
> `𝓕` is arbitrary: no quasi-coherence is needed, so this is the source's clause over a weaker
> hypothesis.  The small Zariski counterpart is
> `AlgebraicGeometry.SmallZariski.isFlat_iff_associatedModule`.

```lean
public theorem isFlat_associatedModule_iff (𝓕 : S.Modules) :
    Stacks.SheafOfModules.IsFlat (O := S.zariskiRingedSite.O) 𝓕 ↔
      Stacks.SheafOfModules.IsFlat (O := (smallEtaleRingedSite B S hS).O)
        ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.SmallEtale.isLocallyGeneratedByOnSite_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalGenerationByRAgreement.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalGenerationByRAgreement.lean#L299). The attribute's comment: “locally generated by r sections (03DL (4)), small site at τ = étale, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (4), at the small étale site, as
> an equivalence.**  A quasi-coherent `𝒪_S`-module `𝓕` is locally generated by `r` sections on the
> small Zariski site of `S` if and only if `𝓕ᵃ` is locally generated by `r` sections as an
> `𝒪`-module on `S_étale`.
>
> The `only if` half is `isLocallyGeneratedByOnSite_associatedModule_of_isLocallyGeneratedByOnSite`,
> which needs no quasi-coherence; the `if` half is `isLocallyGeneratedByOnSite_of_associatedModule`,
> which uses it, and quasi-coherence is the hypothesis the source's clause carries.
>
> The clause string records the scope: this is clause 03DL (4) of 05VG at the **small** site for
> `τ = étale`.  The small Zariski site is
> `AlgebraicGeometry.SmallZariski.isLocallyGeneratedByOnSite_iff_associatedModule`, where the
> comparison is an equivalence of ringed topoi and Stacks 03DM applies directly.

```lean
theorem isLocallyGeneratedByOnSite_associatedModule_iff (𝓕 : S.Modules)
    [h𝓕 : 𝓕.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓕 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite ((associatedModule B S hS).obj 𝓕) r
```

**`AlgebraicGeometry.SmallFlatSite.isFlat_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteFlatAgreement.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteFlatAgreement.lean#L336). The attribute's comment: “flat (03ER (3)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module `𝓗` is flat if and only if
> `𝓗ᵃ` is flat as an `𝒪`-module on `S_τ`.
>
> The `only if` half is `AlgebraicGeometry.SmallFlatSite.isFlat_associatedModule_of_isFlat`, the
> `if` half `AlgebraicGeometry.SmallFlatSite.isFlat_of_isFlat_associatedModule`.

```lean
theorem isFlat_associatedModule_iff :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓗 ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u} (O := (ringedSite B S hS κ).O)
        ((associatedModule B S hS κ).obj 𝓗)
```

**`AlgebraicGeometry.SmallFlatSite.isFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L109). The attribute's comment: “free (03DE (1)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (1), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module is free if and only if
> `𝓕^a` is so as an `𝒪`-module on `S_τ`.

```lean
theorem isFree_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsFree ↔ ((associatedModuleQcoh B S hS κ).obj F).IsFree
```

**`AlgebraicGeometry.SmallFlatSite.isFiniteFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L122). The attribute's comment: “finite free (03DE (2)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (2), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module is finite free, with the
> same rank if and only if `𝓕^a` is so as an `𝒪`-module on `S_τ`.

```lean
theorem isFiniteFree_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    SheafOfModules.IsFiniteFree S.ringCatSheaf F.obj ↔
      SheafOfModules.IsFiniteFree (ringStructureSheaf B S hS κ)
        ((associatedModuleQcoh B S hS κ).obj F)
```

**`AlgebraicGeometry.SmallFlatSite.isGeneratedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L137). The attribute's comment: “generated by global sections (03DE (3)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (3), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module is generated by global
> sections if and only if `𝓕^a` is so as an `𝒪`-module on `S_τ`.

```lean
theorem isGeneratedByGlobalSections_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsGeneratedByGlobalSections ↔
      ((associatedModuleQcoh B S hS κ).obj F).IsGeneratedByGlobalSections
```

**`AlgebraicGeometry.SmallFlatSite.isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L153). The attribute's comment: “generated by r global sections (03DE (4)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (4), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module is generated by `r`
> global sections, with the same `r` if and only if `𝓕^a` is so as an `𝒪`-module on `S_τ`.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) (r : ℕ) :
    F.obj.IsGeneratedByGlobalSectionsOfCard r ↔
      ((associatedModuleQcoh B S hS κ).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.SmallFlatSite.exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L169). The attribute's comment: “generated by finitely many global sections (03DE (5)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (5), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module is generated by finitely
> many global sections if and only if `𝓕^a` is so as an `𝒪`-module on `S_τ`.

```lean
theorem exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    (∃ r : ℕ, F.obj.IsGeneratedByGlobalSectionsOfCard r) ↔
      ∃ r : ℕ, ((associatedModuleQcoh B S hS κ).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.SmallFlatSite.isPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L186). The attribute's comment: “having a global presentation (03DE (6)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (6), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module is has a global
> presentation, with the same two index types if and only if `𝓕^a` is so as an `𝒪`-module on
> `S_τ`.

```lean
theorem isPresentedByGlobalSections_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsPresentedByGlobalSections ↔
      ((associatedModuleQcoh B S hS κ).obj F).IsPresentedByGlobalSections
```

**`AlgebraicGeometry.SmallFlatSite.isFinitelyPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L204). The attribute's comment: “having a global finite presentation (03DE (7)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (7), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module is has a finite global
> presentation, with the same two finite index types if and only if `𝓕^a` is so as an `𝒪`-module
> on `S_τ`.

```lean
theorem isFinitelyPresentedByGlobalSections_iff_associatedModule
    (F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    F.obj.IsFinitelyPresentedByGlobalSections ↔
      ((associatedModuleQcoh B S hS κ).obj F).IsFinitelyPresentedByGlobalSections
```

**`AlgebraicGeometry.SmallFlatSite.isFiniteLocallyFreeOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L234). The attribute's comment: “finite locally free (03DL (2)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (2), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module `𝓗` is finite locally free
> if and only if `𝓗^a` is finite locally free as an `𝒪`-module on `S_τ`.
>
> The lower shriek to the big `τ`-site carries `𝓗^a|_{S_τ}` to `𝓗^a|_{(Sch/S)_τ}`, finite local
> freeness holds for a module on `S_τ` exactly when it holds for its lower shriek
> (`AlgebraicGeometry.SmallFlatSite.isFiniteLocallyFreeOnSite_lowerShriek_iff`), and on the big site
> this is `AlgebraicGeometry.BigFppfOver.isFiniteLocallyFreeOnSite_baseAssociatedModule_iff`.

```lean
theorem isFiniteLocallyFreeOnSite_iff_associatedModule (𝓗 : S.Modules)
    [𝓗.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓗 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite ((associatedModule B S hS κ).obj 𝓗)
```

**`AlgebraicGeometry.SmallFlatSite.isLocallyGeneratedBySectionsOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L253). The attribute's comment: “locally generated by sections (03DL (3)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (3), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module `𝓕` is locally generated
> by sections if and only if `𝓕^a` is locally generated by sections as an `𝒪`-module on `S_τ`.
>
> Both sides hold: a quasi-coherent module is locally generated by sections, and `𝓕^a` is
> quasi-coherent on `S_τ` (`AlgebraicGeometry.SmallFlatSite.isQuasicoherentOnSite_associatedModule`).

```lean
theorem isLocallyGeneratedBySectionsOnSite_iff_associatedModule (𝓕 : S.Modules)
    (h𝓕 : SheafOfModules.IsQuasicoherent (R := S.ringCatSheaf) 𝓕) :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite 𝓕 ↔
      SheafOfModules.IsLocallyGeneratedBySectionsOnSite ((associatedModule B S hS κ).obj 𝓕)
```

**`AlgebraicGeometry.SmallFlatSite.isLocallyGeneratedByOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L272). The attribute's comment: “locally generated by r sections (03DL (4)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (4), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module `𝓗` is locally generated
> by `r` sections if and only if `𝓗^a` is locally generated by `r` sections as an `𝒪`-module on
> `S_τ`.  The route is that of
> `AlgebraicGeometry.SmallFlatSite.isFiniteLocallyFreeOnSite_iff_associatedModule`, through
> `AlgebraicGeometry.SmallFlatSite.isLocallyGeneratedByOnSite_lowerShriek_iff` and
> `AlgebraicGeometry.BigFppfOver.isLocallyGeneratedByOnSite_baseAssociatedModule_iff`.

```lean
theorem isLocallyGeneratedByOnSite_iff_associatedModule (𝓗 : S.Modules)
    [𝓗.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓗 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite ((associatedModule B S hS κ).obj 𝓗) r
```

**`AlgebraicGeometry.SmallFlatSite.isFiniteType_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L288). The attribute's comment: “finite type (03DL (5)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (5), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module `𝓗` is of finite type if
> and only if `𝓗^a` is of finite type as an `𝒪`-module on `S_τ`, through
> `AlgebraicGeometry.SmallFlatSite.isFiniteType_lowerShriek_iff` and
> `AlgebraicGeometry.BigFppfOver.isFiniteType_baseAssociatedModule_iff`.

```lean
theorem isFiniteType_iff_associatedModule (𝓗 : S.Modules) [𝓗.IsQuasicoherent] :
    SheafOfModules.IsFiniteType (R := S.ringCatSheaf) 𝓗 ↔
      SheafOfModules.IsFiniteType ((associatedModule B S hS κ).obj 𝓗)
```

**`AlgebraicGeometry.SmallFlatSite.isFinitePresentation_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallFlatSiteTypesComparison.lean#L303). The attribute's comment: “finite presentation (03DL (7)): 𝓕 ↔ 𝓕^a, small site S_τ at every τ ∈ {smooth, syntomic, fppf} (the small sites extending the source's)”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (7), on the small `τ`-site, for
> every `τ ∈ {smooth, syntomic, fppf}`.**  A quasi-coherent `𝒪_S`-module `𝓗` is of finite
> presentation if and only if `𝓗^a` is of finite presentation as an `𝒪`-module on `S_τ`, through
> `AlgebraicGeometry.SmallFlatSite.isFinitePresentation_lowerShriek_iff` and
> `AlgebraicGeometry.BigFppfOver.isFinitePresentation_baseAssociatedModule_iff`.

```lean
theorem isFinitePresentation_iff_associatedModule (𝓗 : S.Modules) [𝓗.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentation (R := S.ringCatSheaf) 𝓗 ↔
      ((associatedModule B S hS κ).obj 𝓗).IsFinitePresentation
```

**`AlgebraicGeometry.SmallEtale.isCoherentOnSite_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteCoherenceAgreement.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteCoherenceAgreement.lean#L179). The attribute's comment: “coherent (03DL (8)), small site at τ = étale over a locally Noetherian base, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for coherence, at the small site for `τ = étale`.**  For a locally
> Noetherian scheme `S`, a quasi-coherent `𝒪_S`-module `𝓕` is coherent if and only if `𝓕ᵃ` is
> coherent as an `𝒪`-module on `S_étale`.
>
> Coherence on `S_étale` is Modules on Sites, Definition 03DL (8), and coherence of `𝓕` is the
> ringed-space predicate of Stacks 01BV at the Zariski site of `S`.  The source excludes coherence
> from the general assertion of 05VG and asserts exactly this restricted case, with the two
> hypotheses carried here: `S` locally Noetherian and `𝓕` quasi-coherent.
>
> Both directions run through Stacks 01XZ on the scheme, as the source does.  Forward: `𝓕` is of
> finite presentation, so `𝓕ᵃ` is of finite presentation by clause 03DL (7) of 05VG
> (`AlgebraicGeometry.SmallEtale.isFinitePresentation_associatedModule_iff`), and a module of
> finite presentation on a ringed site with coherent structure sheaf is coherent
> (`Stacks.SheafOfModules.isCoherentOnSite_of_isFinitePresentation_of_unit`, applied to
> `AlgebraicGeometry.SmallEtale.isCoherentOnSite_unit`).  Backward: coherence on the site contains
> finite type, so `𝓕` is of finite type by clause 03DL (5) of 05VG
> (`AlgebraicGeometry.SmallEtale.isFiniteType_associatedModule_iff`), and a quasi-coherent module of
> finite type over a locally Noetherian scheme is coherent.
>
> The clause string records the scope: this is the coherence clause of 05VG at the **small** site
> for `τ = étale`.  The small Zariski site is
> `AlgebraicGeometry.SmallZariski.isCoherentOnSite_associatedModule_iff`.

```lean
public theorem isCoherentOnSite_associatedModule_iff [IsLocallyNoetherian S] (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    𝓕.IsCoherent ↔
      SheafOfModules.IsCoherentOnSite ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.SmallZariski.isCoherentOnSite_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteCoherenceAgreement.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteCoherenceAgreement.lean#L267). The attribute's comment: “coherent (03DL (8)), small site at τ = Zariski over a locally Noetherian base, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for coherence, at the small site for `τ = Zariski`.**  For a locally
> Noetherian scheme `S`, a quasi-coherent `𝒪_S`-module `𝓕` is coherent if and only if `𝓕ᵃ` is
> coherent as an `𝒪`-module on `S_Zar`.
>
> This is the `τ = Zariski` half of the one case in which 05VG asserts coherence, under the two
> hypotheses the source carries: `S` locally Noetherian and `𝓕` quasi-coherent.  The route is the
> same as at `τ = étale`, with clause 03DL (7) read off
> `AlgebraicGeometry.SmallZariski.isFinitePresentation_iff_associatedModule` and clause 03DL (5)
> off `AlgebraicGeometry.SmallZariski.isFiniteType_iff_associatedModule`.
>
> The clause string records the scope: this is the coherence clause of 05VG at the **small** site
> for `τ = Zariski`.  The small étale site is
> `AlgebraicGeometry.SmallEtale.isCoherentOnSite_associatedModule_iff`.

```lean
public theorem isCoherentOnSite_associatedModule_iff [IsLocallyNoetherian S] (𝓕 : S.Modules)
    [𝓕.IsQuasicoherent] :
    𝓕.IsCoherent ↔
      SheafOfModules.IsCoherentOnSite ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.Scheme.Modules.isCoherentOnSite_iff_isCoherentOnSite_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteCoherenceOnSiteAgreement.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteCoherenceOnSiteAgreement.lean#L143). The attribute's comment: “coherent (03DL (8)) on both sides, S locally Noetherian: 𝓕 has 𝒫 on (Opens(S), 𝒪_S) ⇔ 𝓕ᵃ has 𝒫 on S_Zar, and ⇔ 𝓕ᵃ has 𝒫 on S_étale, at the comparison functors of 03DX (2)”.

> **Descent, Lemma 05VG, for the property "coherent" (Modules on Sites, Definition 03DL (8)).**
> Let `S` be a locally Noetherian scheme and `𝓕` a quasi-coherent `𝒪_S`-module.  Then `𝓕` is
> coherent if and only if `𝓕^a` is coherent as an `𝒪`-module, at the comparison functor
> `𝓕 ↦ 𝓕^a` of Descent, Proposition 03DX (2) for `τ = Zariski`
> (`AlgebraicGeometry.SmallZariski.associatedModule`, to `S_Zar`) and for `τ = étale`
> (`AlgebraicGeometry.SmallEtale.associatedModule`, to `S_étale`).
>
> "Coherent" is the one predicate `SheafOfModules.IsCoherentOnSite` of Definition 03DL (8) on both
> sides: for `𝓕` on the ringed site `(Opens(S), 𝒪_S)`, for `𝓕^a` on `(S_Zar, 𝒪)` and on
> `(S_étale, 𝒪)`.  On `𝓕` it agrees with coherence of `𝒪_S`-modules in the sense of Stacks 01BV by
> `AlgebraicGeometry.Scheme.Modules.isCoherentOnSite_iff_isCoherent`.  These are exactly the sites,
> and locally Noetherian is exactly the hypothesis, under which the source asserts the coherent
> case.

```lean
theorem isCoherentOnSite_iff_isCoherentOnSite_associatedModule [IsLocallyNoetherian S]
    (𝓕 : S.Modules) [𝓕.IsQuasicoherent] :
    (SheafOfModules.IsCoherentOnSite 𝓕 ↔
        SheafOfModules.IsCoherentOnSite ((SmallZariski.associatedModule Bz S hz).obj 𝓕)) ∧
      (SheafOfModules.IsCoherentOnSite 𝓕 ↔
        SheafOfModules.IsCoherentOnSite ((SmallEtale.associatedModule Be S he).obj 𝓕))
```

**`AlgebraicGeometry.SmallZariski.isFlat_iff_associatedModuleEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteFlatAgreement.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteFlatAgreement.lean#L99). The attribute's comment: “flat (03ER (3)), small site S_Zar, at the equivalence QCoh(𝒪_S) ≌ QCoh(S_Zar, 𝒪) of 03DX (2) itself, with no hypothesis”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3), at the equivalence
> `QCoh(𝒪_S) ≌ QCoh(S_Zar, 𝒪)` of Descent, Proposition 03DX (2).**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `S_Zar`.
>
> There is no hypothesis beyond `𝓕`: the comparison `S_Zar → (S, 𝒪_S)` is proved to be an
> equivalence of ringed topoi
> (`AlgebraicGeometry.SmallZariski.isEquivalence_pushforward_toOpensRingedToposHom`,
> `AlgebraicGeometry.SmallZariski.isIso_fSharp_toOpensRingedToposHom`), and
> `AlgebraicGeometry.SmallZariski.isFlat_iff_associatedModule` transfers flatness across it.

```lean
theorem isFlat_iff_associatedModuleEquivalence
    (𝓕 : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕.obj ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u} (O := (smallZariskiRingedSite B S hS).O)
        ((associatedModuleEquivalence B S hS).functor.obj 𝓕).obj
```

**`AlgebraicGeometry.SmallEtale.isFlat_iff_associatedModuleEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteFlatAgreement.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteFlatAgreement.lean#L123). The attribute's comment: “flat (03ER (3)), small site S_étale, at the equivalence QCoh(𝒪_S) ≌ QCoh(S_étale, 𝒪) of 03DX (2) itself, with no hypothesis”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3), at the equivalence
> `QCoh(𝒪_S) ≌ QCoh(S_étale, 𝒪)` of Descent, Proposition 03DX (2).**  A quasi-coherent
> `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on `S_étale`.
>
> There is no hypothesis beyond `𝓕`, and no equivalence of ringed topoi is involved: the
> comparison `S_étale → S_Zar` is not one.  The proof is
> `AlgebraicGeometry.SmallEtale.isFlat_associatedModule_iff` — Stacks 05VD for the `only if` half,
> and for the `if` half the reflection of flatness by a pullback of modules which preserves and
> reflects monomorphisms, both of which hold at `ε` by Stacks 08H8.

```lean
theorem isFlat_iff_associatedModuleEquivalence
    (𝓕 : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕.obj ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u} (O := (smallEtaleRingedSite B S hS).O)
        ((associatedModuleEquivalence' B S hS).functor.obj 𝓕).obj
```

**`AlgebraicGeometry.SmallFlatSite.isFlat_iff_associatedModuleEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteFlatAgreement.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteFlatAgreement.lean#L146). The attribute's comment: “flat (03ER (3)), small site S_τ for every τ ∈ {smooth, syntomic, fppf}, at the equivalence QCoh(𝒪_S) ≌ QCoh(S_τ, 𝒪) of 03DX itself, with no hypothesis”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3), at the equivalence
> `QCoh(𝒪_S) ≌ QCoh(S_τ, 𝒪)` of the small site `S_τ`, for every `τ ∈ {smooth, syntomic, fppf}`.**
> A quasi-coherent `𝒪_S`-module `𝓕` is flat if and only if `𝓕^a` is flat as an `𝒪`-module on
> `S_τ`.
>
> There is no hypothesis beyond `𝓕`, and no equivalence of ringed topoi is involved.  The proof is
> `AlgebraicGeometry.SmallFlatSite.isFlat_associatedModule_iff`, both of whose halves are the
> equational criterion of Stacks 08FC.

```lean
theorem isFlat_iff_associatedModuleEquivalence
    (𝓕 : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory) :
    Stacks.SheafOfModules.IsFlat.{u, u, u, u} (O := S.zariskiRingedSite.O) 𝓕.obj ↔
      Stacks.SheafOfModules.IsFlat.{u, u + 1, u, u} (O := (ringedSite B S hS κ).O)
        ((associatedModuleEquivalence B S hS κ).functor.obj 𝓕).obj
```

**`AlgebraicGeometry.SmallZariski.isFiniteLocallyFreeOnSite_associatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiFiniteLocallyFreeAgreement.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiFiniteLocallyFreeAgreement.lean#L346). The attribute's comment: “finite locally free (03DL (2)), small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (2), at the small Zariski site,
> as an equivalence.**  An `𝒪_S`-module `𝓕` is finite locally free on the small Zariski site of `S`
> if and only if `𝓕^a` is finite locally free as an `𝒪`-module on `S_Zar`.
>
> The `only if` half is
> `SmallZariski.isFiniteLocallyFreeOnSite_associatedModule_of_isFiniteLocallyFreeOnSite` and the
> `if` half is
> `AlgebraicGeometry.SmallZariski.isFiniteLocallyFreeOnSite_of_associatedModule`.  **Neither needs
> quasi-coherence**, so this is the clause over a weaker hypothesis than the source's, which
> carries it: at `τ = Zariski` the comparison of Remark 03FH is an equivalence of ringed sites and
> its localization at an open of `S` is one too, so no restriction to the quasi-coherent modules
> is needed.
>
> The clause string records the scope: this is clause 03DL (2) of 05VG at the **small** site for
> `τ = Zariski`.  The small étale site is
> `AlgebraicGeometry.SmallEtale.isFiniteLocallyFreeOnSite_associatedModule_iff` and the five big
> sites `(Sch/S)_τ` are
> `AlgebraicGeometry.BigFppfOver.isFiniteLocallyFreeOnSite_baseAssociatedModule_iff`; with this
> statement the clause is covered at every one of 05VG's seven comparison functors.

```lean
public theorem isFiniteLocallyFreeOnSite_associatedModule_iff (𝓕 : S.Modules) :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite ((associatedModule B S hS).obj 𝓕)
```

**`AlgebraicGeometry.SmallZariski.isLocallyGeneratedByOnSite_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean#L278). The attribute's comment: “locally generated by r sections (03DL (4)), small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (4), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is locally generated by `r` sections if and only if `𝓕^a` is
> locally generated by `r` sections as an `𝒪`-module on `S_Zar`.
>
> This is Stacks 03DM for that clause,
> `AlgebraicGeometry.RingedToposHom.isLocallyGeneratedByOnSite_iff_pullbackModules`, instantiated
> at `AlgebraicGeometry.SmallZariski.toOpensRingedToposHom` and transported along
> `AlgebraicGeometry.SmallZariski.associatedModuleIsoPullbackModules`.  No quasi-coherence is
> needed, the comparison being an equivalence of the whole module categories.

```lean
theorem isLocallyGeneratedByOnSite_iff_associatedModule
    (F : SheafOfModules.{u} S.ringCatSheaf) (r : ℕ) :
    F.IsLocallyGeneratedByOnSite r ↔
      ((associatedModuleOfSheaf B S hS).obj F).IsLocallyGeneratedByOnSite r
```

**`AlgebraicGeometry.SmallZariski.isFiniteType_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean#L297). The attribute's comment: “finite type (03DL (5)), small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (5), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is of finite type if and only if `𝓕^a` is of finite type as
> an `𝒪`-module on `S_Zar`.
>
> This is Stacks 03DM for that clause,
> `AlgebraicGeometry.RingedToposHom.isFiniteType_iff_pullbackModules`, instantiated at
> `AlgebraicGeometry.SmallZariski.toOpensRingedToposHom` and transported along
> `AlgebraicGeometry.SmallZariski.associatedModuleIsoPullbackModules`.

```lean
theorem isFiniteType_iff_associatedModule (F : SheafOfModules.{u} S.ringCatSheaf) :
    F.IsFiniteType ↔ ((associatedModuleOfSheaf B S hS).obj F).IsFiniteType
```

**`AlgebraicGeometry.SmallZariski.isFinitePresentation_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean#L314). The attribute's comment: “finite presentation (03DL (7)), small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (7), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is of finite presentation if and only if `𝓕^a` is of finite
> presentation as an `𝒪`-module on `S_Zar`.
>
> This is Stacks 03DM for that clause,
> `AlgebraicGeometry.RingedToposHom.isFinitePresentation_iff_pullbackModules`, instantiated at
> `AlgebraicGeometry.SmallZariski.toOpensRingedToposHom` and transported along
> `AlgebraicGeometry.SmallZariski.associatedModuleIsoPullbackModules`.

```lean
theorem isFinitePresentation_iff_associatedModule (F : SheafOfModules.{u} S.ringCatSheaf) :
    F.IsFinitePresentation ↔ ((associatedModuleOfSheaf B S hS).obj F).IsFinitePresentation
```

**`AlgebraicGeometry.SmallZariski.isFlat_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiLocalTypesComparison.lean#L345). The attribute's comment: “flat (03ER (3)), small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03ER (3), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is flat if and only if `𝓕^a` is flat as an `𝒪`-module on
> `S_Zar`.
>
> This is `AlgebraicGeometry.RingedToposHom.isFlat_iff_pullbackModules` — the flatness clause for
> an equivalence of ringed topoi, whose forward half is Modules on Sites, Lemma 05VD — instantiated
> at
> `AlgebraicGeometry.SmallZariski.toOpensRingedToposHom` and transported along
> `AlgebraicGeometry.SmallZariski.associatedModuleIsoPullbackModules` by
> `Stacks.ModuleUp.isFlat_of_iso_anySite`.  No quasi-coherence is needed, the comparison being an
> equivalence of the whole module categories; the source's clause carries quasi-coherence, so this
> is the clause over a weaker hypothesis than the source's.

```lean
public theorem isFlat_iff_associatedModule (F : SheafOfModules.{u} S.ringCatSheaf) :
    Stacks.SheafOfModules.IsFlat (O := S.zariskiRingedSite.O) F ↔
      Stacks.SheafOfModules.IsFlat (O := (smallZariskiRingedSite B S hS).O)
        ((associatedModuleOfSheaf B S hS).obj F)
```

**`AlgebraicGeometry.SmallZariski.isFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean#L117). The attribute's comment: “free, small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (1), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is free if and only if `𝓕^a` is free as an `𝒪`-module on
> `S_Zar`.  No quasi-coherence is needed, the comparison being an equivalence of the whole module
> categories.

```lean
theorem isFree_iff_associatedModule (F : SheafOfModules.{u} S.ringCatSheaf) :
    F.IsFree ↔ ((associatedModuleOfSheaf B S hS).obj F).IsFree
```

**`AlgebraicGeometry.SmallZariski.isFiniteFree_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean#L126). The attribute's comment: “finite free, small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (2), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is finite free if and only if `𝓕^a` is, with the same
> rank.

```lean
theorem isFiniteFree_iff_associatedModule (F : SheafOfModules.{u} S.ringCatSheaf) :
    SheafOfModules.IsFiniteFree S.ringCatSheaf F ↔
      SheafOfModules.IsFiniteFree (structureSheaf B S hS)
        ((associatedModuleOfSheaf B S hS).obj F)
```

**`AlgebraicGeometry.SmallZariski.isGeneratedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean#L136). The attribute's comment: “generated by global sections, small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (3), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is generated by global sections if and only if `𝓕^a` is.

```lean
theorem isGeneratedByGlobalSections_iff_associatedModule
    (F : SheafOfModules.{u} S.ringCatSheaf) :
    F.IsGeneratedByGlobalSections ↔
      ((associatedModuleOfSheaf B S hS).obj F).IsGeneratedByGlobalSections
```

**`AlgebraicGeometry.SmallZariski.isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean#L148). The attribute's comment: “generated by r global sections, small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (4), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is generated by `r` global sections if and only if `𝓕^a`
> is.

```lean
theorem isGeneratedByGlobalSectionsOfCard_iff_associatedModule
    (F : SheafOfModules.{u} S.ringCatSheaf) (r : ℕ) :
    F.IsGeneratedByGlobalSectionsOfCard r ↔
      ((associatedModuleOfSheaf B S hS).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.SmallZariski.exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean#L160). The attribute's comment: “generated by finitely many global sections, small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (5), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules is generated by finitely many global sections if and only if
> `𝓕^a` is.

```lean
theorem exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule
    (F : SheafOfModules.{u} S.ringCatSheaf) :
    (∃ r : ℕ, F.IsGeneratedByGlobalSectionsOfCard r) ↔
      ∃ r : ℕ, ((associatedModuleOfSheaf B S hS).obj F).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.SmallZariski.isPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean#L172). The attribute's comment: “global presentation, small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (6), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules has a global presentation if and only if `𝓕^a` has one, with
> the same two index types.

```lean
theorem isPresentedByGlobalSections_iff_associatedModule
    (F : SheafOfModules.{u} S.ringCatSheaf) :
    F.IsPresentedByGlobalSections ↔
      ((associatedModuleOfSheaf B S hS).obj F).IsPresentedByGlobalSections
```

**`AlgebraicGeometry.SmallZariski.isFinitelyPresentedByGlobalSections_iff_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiTypesComparison.lean#L184). The attribute's comment: “finite global presentation, small site at τ = Zariski, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DE (7), on the small Zariski
> site.**  A sheaf of `𝒪_S`-modules has a finite global presentation if and only if `𝓕^a` has
> one, with the same two finite index types.

```lean
theorem isFinitelyPresentedByGlobalSections_iff_associatedModule
    (F : SheafOfModules.{u} S.ringCatSheaf) :
    F.IsFinitelyPresentedByGlobalSections ↔
      ((associatedModuleOfSheaf B S hS).obj F).IsFinitelyPresentedByGlobalSections
```

**`AlgebraicGeometry.BigFppfOver.isFiniteLocallyFreeOnSite_baseAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteFiniteLocallyFreeAgreement.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteFiniteLocallyFreeAgreement.lean#L382). The attribute's comment: “finite locally free (03DL (2)), big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (2), on the big site, as an
> equivalence.**  A quasi-coherent `𝒪_S`-module `𝓗` is finite locally free on the small Zariski
> site of `S` if and only if `𝓗ᵃ` is finite locally free as an `𝒪`-module on `(Sch/S)_τ`, for
> every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.
>
> The `only if` half is
> `BigFppfOver.isFiniteLocallyFreeOnSite_baseAssociatedModule_of_isFiniteLocallyFreeOnSite`,
> valid at every `τ`.  The `if` half is proved at `τ = fppf` by
> `AlgebraicGeometry.BigFppfOver.isFiniteLocallyFreeOnSite_of_associatedModule`, and carried to the
> four coarser topologies by the monotonicity
> `Stacks.SheafOfModules.isFiniteLocallyFreeOnSite_of_comparisonPushforward` through the key to
> Stacks 0GNE, `AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso`, which exhibits
> `𝓗ᵃ` on `(Sch/S)_τ` as `𝓗ᵃ` on `(Sch/S)_fppf` read for the coarser topology.
>
> This is clause 03DL (2) of 05VG at the **big** site `(Sch/S)_τ`, at every `τ`; the small sites
> `S_τ` for `τ ∈ {Zariski, étale}`, which Stacks 03DU (4) also treats, are not covered.

```lean
public theorem isFiniteLocallyFreeOnSite_baseAssociatedModule_iff (τ : SiteKind) (𝓗 : S.Modules)
    [h𝓗 : 𝓗.IsQuasicoherent] :
    SheafOfModules.IsFiniteLocallyFreeOnSite (R := S.ringCatSheaf) 𝓗 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite ((baseAssociatedModule B S hS τ).obj 𝓗)
```

**`AlgebraicGeometry.BigFppfOver.isFinitePresentation_baseAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteFinitePresentationAgreement.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteFinitePresentationAgreement.lean#L414). The attribute's comment: “finite presentation (03DL (7)), big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (7), on the big site, as an
> equivalence.**  A quasi-coherent `𝒪_S`-module `𝓗` is of finite presentation on the small Zariski
> site of `S` if and only if `𝓗ᵃ` is of finite presentation as an `𝒪`-module on `(Sch/S)_τ`, for
> every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.
>
> The forward half is
> `AlgebraicGeometry.BigFppfOver.isFinitePresentation_baseAssociatedModule_of_isFinitePresentation`,
> proved at every `τ` and needing no quasi-coherence.  The reverse half is proved at `τ = fppf` by
> `AlgebraicGeometry.BigFppfOver.isFinitePresentation_of_associatedModule`, and carried to the four
> coarser topologies by the monotonicity
> `Stacks.SheafOfModules.isFinitePresentation_of_comparisonPushforward` through the key to
> Stacks 0GNE, `AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso`, which exhibits
> `𝓗ᵃ` on `(Sch/S)_τ` as `𝓗ᵃ` on `(Sch/S)_fppf` read for the coarser topology.
>
> The clause string records the scope: this is clause 03DL (7) of 05VG, at the **big** site
> `(Sch/S)_τ` and at every `τ`.  The small sites are
> `AlgebraicGeometry.SmallEtale.isFinitePresentation_associatedModule_iff` and
> `AlgebraicGeometry.SmallZariski.isFinitePresentation_iff_associatedModule`.

```lean
public theorem isFinitePresentation_baseAssociatedModule_iff (τ : SiteKind) (𝓗 : S.Modules)
    [h𝓗 : 𝓗.IsQuasicoherent] :
    SheafOfModules.IsFinitePresentation (R := S.ringCatSheaf) 𝓗 ↔
      ((baseAssociatedModule B S hS τ).obj 𝓗).IsFinitePresentation
```

**`AlgebraicGeometry.BigFppfOver.isLocallyGeneratedByOnSite_baseAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteLocalGenerationFinitenessAgreement.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteLocalGenerationFinitenessAgreement.lean#L544). The attribute's comment: “locally generated by r sections (03DL (4)), big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (4), on the big site, as an
> equivalence.**  A quasi-coherent `𝒪_S`-module `𝓗` is locally generated by `r` sections on the
> small Zariski site of `S` if and only if `𝓗^a` is locally generated by `r` sections as an
> `𝒪`-module on `(Sch/S)_τ`, for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.
>
> The `only if` half is
> `BigFppfOver.isLocallyGeneratedByOnSite_baseAssociatedModule_of_isLocallyGeneratedByOnSite`,
> proved at every `τ` and needing no quasi-coherence.  The `if` half is proved at `τ = fppf` by
> `AlgebraicGeometry.BigFppfOver.isLocallyGeneratedByOnSite_of_associatedModule`, and carried to the
> four coarser topologies by the monotonicity
> `Stacks.SheafOfModules.isLocallyGeneratedByOnSite_of_comparisonPushforward` through the key to
> Stacks 0GNE, `AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso`, which exhibits
> `𝓗^a` on `(Sch/S)_τ` as `𝓗^a` on `(Sch/S)_fppf` read for the coarser topology.  Quasi-coherence
> is used by that half alone, and it is the hypothesis the source's clause carries.
>
> The clause string records the scope: this is clause 03DL (4) of 05VG, at the **big** site
> `(Sch/S)_τ` and at every `τ`.  The small sites are
> `AlgebraicGeometry.SmallEtale.isLocallyGeneratedByOnSite_associatedModule_iff` and
> `AlgebraicGeometry.SmallZariski.isLocallyGeneratedByOnSite_iff_associatedModule`.

```lean
public theorem isLocallyGeneratedByOnSite_baseAssociatedModule_iff (τ : SiteKind)
    (𝓗 : S.Modules) [h𝓗 : 𝓗.IsQuasicoherent] (r : ℕ) :
    SheafOfModules.IsLocallyGeneratedByOnSite (R := S.ringCatSheaf) 𝓗 r ↔
      SheafOfModules.IsLocallyGeneratedByOnSite ((baseAssociatedModule B S hS τ).obj 𝓗) r
```

**`AlgebraicGeometry.BigFppfOver.isFiniteType_baseAssociatedModule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteLocalGenerationFinitenessAgreement.lean, line 579](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteLocalGenerationFinitenessAgreement.lean#L579). The attribute's comment: “finite type (03DL (5)), big site (Sch/S)_τ at every τ, at the comparison functor of 03DX itself”.

> **Descent, Lemma 05VG for Modules on Sites, Definition 03DL (5), on the big site, as an
> equivalence.**  A quasi-coherent `𝒪_S`-module `𝓗` is of finite type if and only if `𝓗^a` is of
> finite type as an `𝒪`-module on `(Sch/S)_τ`, for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.
>
> The `only if` half is
> `AlgebraicGeometry.BigFppfOver.isFiniteType_baseAssociatedModule_of_isFiniteType`, proved at every
> `τ` and needing no quasi-coherence.  The `if` half is proved at `τ = fppf` by
> `AlgebraicGeometry.BigFppfOver.isFiniteType_of_associatedModule`, and carried to the four coarser
> topologies by the monotonicity
> `Stacks.SheafOfModules.isFiniteType_of_comparisonPushforward` through
> `AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso`.  Quasi-coherence is used by
> that half alone, and it is the hypothesis the source's clause carries.
>
> The clause string records the scope: this is clause 03DL (5) of 05VG, at the **big** site
> `(Sch/S)_τ` and at every `τ`.  The small sites are
> `AlgebraicGeometry.SmallEtale.isFiniteType_associatedModule_iff` and
> `AlgebraicGeometry.SmallZariski.isFiniteType_iff_associatedModule`, both of which hold without
> quasi-coherence; at the big site the descent is fpqc descent of finite type, Stacks 05AZ, which
> is stated for a quasi-coherent module.

```lean
public theorem isFiniteType_baseAssociatedModule_iff (τ : SiteKind) (𝓗 : S.Modules)
    [h𝓗 : 𝓗.IsQuasicoherent] :
    SheafOfModules.IsFiniteType (R := S.ringCatSheaf) 𝓗 ↔
      SheafOfModules.IsFiniteType ((baseAssociatedModule B S hS τ).obj 𝓗)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedToposHom.isLocallyGeneratedByOnSite_iff_pullbackModules`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ModuleTypesUnderEquivalence.lean#L248), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean#L176) (StacksFrontier): “locally generated by r sections; local properties, with the comparison of 03DX carried as an equivalence of ringed topoi rather than of quasi-coherent modules alone”.
- [`AlgebraicGeometry.RingedToposHom.isFiniteType_iff_pullbackModules`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ModuleTypesUnderEquivalence.lean#L221), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean#L180) (StacksFrontier): “finite type; local properties, with the comparison of 03DX carried as an equivalence of ringed topoi rather than of quasi-coherent modules alone”.
- [`AlgebraicGeometry.RingedToposHom.isFinitePresentation_iff_pullbackModules`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ModuleTypesUnderEquivalence.lean#L194), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalTypesUnderComparison.lean#L184) (StacksFrontier): “of finite presentation; local properties, with the comparison of 03DX carried as an equivalence of ringed topoi rather than of quasi-coherent modules alone”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.8, Tag 03DR](https://stacks.math.columbia.edu/tag/03DR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
