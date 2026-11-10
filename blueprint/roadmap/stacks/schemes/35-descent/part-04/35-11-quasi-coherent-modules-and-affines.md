---
declaration: section
origin: cited
lean: AlgebraicGeometry.zariski_affineToBigRingedToposEquivalence, AlgebraicGeometry.etale_affineToBigRingedToposEquivalence, AlgebraicGeometry.smooth_affineToBigRingedToposEquivalence, AlgebraicGeometry.syntomic_affineToBigRingedToposEquivalence, AlgebraicGeometry.fppf_affineToBigRingedToposEquivalence, AlgebraicGeometry.bigAffineZariski_isIso_restrictionBaseChange_associatedModule, AlgebraicGeometry.bigAffineEtale_isIso_restrictionBaseChange_associatedModule, AlgebraicGeometry.bigAffineSmooth_isIso_restrictionBaseChange_associatedModule
statement: formalized
proof: formalized
---

# 35.11 Quasi-coherent modules and affines

Section 35.11 of the Stacks Project, [Tag 0GZT](https://stacks.math.columbia.edu/tag/0GZT). 4 tags here are carried by 95 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GZU, an equation

[Tag 0GZU](https://stacks.math.columbia.edu/tag/0GZU) in the Stacks Project.

**`AlgebraicGeometry.zariski_affineToBigRingedToposEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean#L273). The attribute's comment: “Zariski site”.

> **Stacks 0GZU, Zariski site.** The affine-to-big morphism of ringed topoi over the big
> Zariski site of `S` is an equivalence of ringed topoi: its inverse image is an equivalence and
> its structure morphism is an isomorphism.

```lean
public theorem zariski_affineToBigRingedToposEquivalence
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    let f := affineToBigRingedToposHom.{u + 1, u, u + 1, u, w}
      (BigAffineZariski.topology B S hS) (BigZariskiOver.topology B S hS)
      (BigAffineZariski.inclusion B S hS)
      (uliftRingSheaf.{w} (commStructureSheaf S (BigZariskiOver.topology B S hS)
        (Over.post B.inclusion) (BigZariskiOver.structure_isSheaf B S hS)))
    f.toToposHom.inverseImage.IsEquivalence ∧ IsIso f.fSharpInverseImage
```

**`AlgebraicGeometry.etale_affineToBigRingedToposEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean#L287). The attribute's comment: “étale site”.

> **Stacks 0GZU, étale site.** The affine-to-big morphism of ringed topoi over the big étale
> site of `S` is an equivalence of ringed topoi: its inverse image is an equivalence and its
> structure morphism is an isomorphism.

```lean
public theorem etale_affineToBigRingedToposEquivalence
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    let f := affineToBigRingedToposHom.{u + 1, u, u + 1, u, w}
      (BigAffineEtale.topology B S hS) (BigEtaleOver.topology B S hS)
      (BigAffineEtale.inclusion B S hS)
      (uliftRingSheaf.{w} (commStructureSheaf S (BigEtaleOver.topology B S hS)
        (Over.post B.inclusion) (BigEtaleOver.structure_isSheaf B S hS)))
    f.toToposHom.inverseImage.IsEquivalence ∧ IsIso f.fSharpInverseImage
```

**`AlgebraicGeometry.smooth_affineToBigRingedToposEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean#L301). The attribute's comment: “smooth site”.

> **Stacks 0GZU, smooth site.** The affine-to-big morphism of ringed topoi over the big smooth
> site of `S` is an equivalence of ringed topoi: its inverse image is an equivalence and its
> structure morphism is an isomorphism.

```lean
public theorem smooth_affineToBigRingedToposEquivalence
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff) :
    let f := affineToBigRingedToposHom.{u + 1, u, u + 1, u, w}
      (BigAffineSmooth.topology B S hS) (BigSmoothOver.topology B S hS)
      (BigAffineSmooth.inclusion B S hS)
      (uliftRingSheaf.{w} (commStructureSheaf S (BigSmoothOver.topology B S hS)
        (Over.post (ObjectProperty.ι _)) (BigSmoothOver.structure_isSheaf B S hS)))
    f.toToposHom.inverseImage.IsEquivalence ∧ IsIso f.fSharpInverseImage
```

**`AlgebraicGeometry.syntomic_affineToBigRingedToposEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean#L315). The attribute's comment: “syntomic site”.

> **Stacks 0GZU, syntomic site.** The affine-to-big morphism of ringed topoi over the big
> syntomic site of `S` is an equivalence of ringed topoi: its inverse image is an equivalence and
> its structure morphism is an isomorphism.

```lean
public theorem syntomic_affineToBigRingedToposEquivalence
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    let f := affineToBigRingedToposHom.{u + 1, u, u + 1, u, w}
      (BigAffineSyntomic.topology B S hS) (BigSyntomicOver.topology B S hS)
      (BigAffineSyntomic.inclusion B S hS)
      (uliftRingSheaf.{w} (commStructureSheaf S (BigSyntomicOver.topology B S hS)
        (Over.post B.inclusion) (BigSyntomicOver.structure_isSheaf B S hS)))
    f.toToposHom.inverseImage.IsEquivalence ∧ IsIso f.fSharpInverseImage
```

**`AlgebraicGeometry.fppf_affineToBigRingedToposEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffineRingedToposEquivalence.lean#L329). The attribute's comment: “fppf site”.

> **Stacks 0GZU, fppf site.** The affine-to-big morphism of ringed topoi over the big fppf
> site of `S` is an equivalence of ringed topoi: its inverse image is an equivalence and its
> structure morphism is an isomorphism.

```lean
public theorem fppf_affineToBigRingedToposEquivalence
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    let f := affineToBigRingedToposHom.{u + 1, u, u + 1, u, w}
      (BigAffineFppf.topology B S hS) (BigFppfOver.topology B S hS)
      (BigAffineFppf.inclusion B S hS)
      (uliftRingSheaf.{w} (commStructureSheaf S (BigFppfOver.topology B S hS)
        (Over.post B.inclusion) (BigFppfOver.structure_isSheaf B S hS)))
    f.toToposHom.inverseImage.IsEquivalence ∧ IsIso f.fSharpInverseImage
```

## Tag 0GZV, a lemma

[Tag 0GZV](https://stacks.math.columbia.edu/tag/0GZV) in the Stacks Project.

**`AlgebraicGeometry.bigAffineZariski_isIso_restrictionBaseChange_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean#L210). The attribute's comment: “(8) ⇒ (1) on the big affine Zariski category”.

> **Stacks 0GZV, condition (8) implies condition (1), on `(Aff/S)_Zar`.**

```lean
public theorem bigAffineZariski_isIso_restrictionBaseChange_associatedModule
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : S.Modules) [G.IsQuasicoherent] {X Y : (BigAffineZariski B S hS)ᵒᵖ} (f : X ⟶ Y) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange
      (R := (bigAffineZariskiRingedSite B S hS).O.obj)
      (associatedModulePresheaf S G (bigAffineZariskiToOver B S hS)) f)
```

**`AlgebraicGeometry.bigAffineEtale_isIso_restrictionBaseChange_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean#L238). The attribute's comment: “(8) ⇒ (1) on the big affine étale category”.

> **Stacks 0GZV, condition (8) implies condition (1), on `(Aff/S)_étale`.**

```lean
public theorem bigAffineEtale_isIso_restrictionBaseChange_associatedModule
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : S.Modules) [G.IsQuasicoherent] {X Y : (BigAffineEtale B S hS)ᵒᵖ} (f : X ⟶ Y) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange
      (R := (bigAffineEtaleRingedSite B S hS).O.obj)
      (associatedModulePresheaf S G (bigAffineEtaleToOver B S hS)) f)
```

**`AlgebraicGeometry.bigAffineSmooth_isIso_restrictionBaseChange_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean#L266). The attribute's comment: “(8) ⇒ (1) on the big affine smooth category”.

> **Stacks 0GZV, condition (8) implies condition (1), on `(Aff/S)_smooth`.**

```lean
public theorem bigAffineSmooth_isIso_restrictionBaseChange_associatedModule
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (G : S.Modules) [G.IsQuasicoherent] {X Y : (BigAffineSmooth B S hS)ᵒᵖ} (f : X ⟶ Y) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange
      (R := (bigAffineSmoothRingedSite B S hS).O.obj)
      (associatedModulePresheaf S G (bigAffineSmoothToOver B S hS)) f)
```

**`AlgebraicGeometry.bigAffineSyntomic_isIso_restrictionBaseChange_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean#L294). The attribute's comment: “(8) ⇒ (1) on the big affine syntomic category”.

> **Stacks 0GZV, condition (8) implies condition (1), on `(Aff/S)_syntomic`.**

```lean
public theorem bigAffineSyntomic_isIso_restrictionBaseChange_associatedModule
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : S.Modules) [G.IsQuasicoherent] {X Y : (BigAffineSyntomic B S hS)ᵒᵖ} (f : X ⟶ Y) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange
      (R := (bigAffineSyntomicRingedSite B S hS).O.obj)
      (associatedModulePresheaf S G (bigAffineSyntomicToOver B S hS)) f)
```

**`AlgebraicGeometry.bigAffineFppf_isIso_restrictionBaseChange_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AffineSiteAssociatedModuleCartesian.lean#L325). The attribute's comment: “(8) ⇒ (1) on the big affine fppf category”.

> **Stacks 0GZV, condition (8) implies condition (1).** The presheaf `𝒢ᵃ` of Section 35.8
> attached to a quasi-coherent `𝒪_S`-module `𝒢` has all its base-change comparisons
> `𝒢ᵃ(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝒢ᵃ(U)` isomorphisms on `(Aff/S)_fppf`, the category the source states
> the lemma for.

```lean
public theorem bigAffineFppf_isIso_restrictionBaseChange_associatedModule
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : S.Modules) [G.IsQuasicoherent] {X Y : (BigAffineFppf B S hS)ᵒᵖ} (f : X ⟶ Y) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange
      (R := (bigAffineFppfRingedSite B S hS).O.obj)
      (associatedModulePresheaf S G (bigAffineFppfToOver B S hS)) f)
```

**`AlgebraicGeometry.fullyFaithfulBigAffineFppfAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean#L205). The attribute's comment: “(8) at τ = fppf, uniqueness of 𝒢”.

> **Stacks 0GZV, the uniqueness of `𝒢` in condition (8) at `τ = fppf`.** The functor
> `𝒢 ↦ 𝒢^a|_{(Aff/S)_fppf}` from the quasi-coherent `𝒪_S`-modules to the `𝒪_Aff`-modules on
> `(Aff/S)_fppf` is fully faithful: it is Stacks 0GN7 for the big site followed by the Comparison
> Lemma for sheaves of modules on the dense subsite of affine objects. No part of Descent,
> Proposition 03DX is used.

```lean
public noncomputable def fullyFaithfulBigAffineFppfAssociatedModuleQcoh :
    (bigAffineFppfAssociatedModuleQcoh B S hS).FullyFaithful
```

**`AlgebraicGeometry.bigAffineFppf_iso_of_associatedModuleQcoh_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean#L214). The attribute's comment: “(8) at τ = fppf, uniqueness of 𝒢”.

> **Stacks 0GZV, the uniqueness of `𝒢` in condition (8) at `τ = fppf`**, read as a uniqueness
> statement: two quasi-coherent `𝒪_S`-modules whose associated modules have isomorphic
> restrictions to the big affine fppf site of `S` are isomorphic.

```lean
public theorem bigAffineFppf_iso_of_associatedModuleQcoh_restriction_iso
    (G₁ G₂ : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory)
    (e : (bigAffineFppfAssociatedModuleQcoh B S hS).obj G₁ ≅
      (bigAffineFppfAssociatedModuleQcoh B S hS).obj G₂) :
    Nonempty (G₁.obj ≅ G₂.obj)
```

**`AlgebraicGeometry.bigAffineFppf_isRestrictionOfQuasicoherent_of_isRestrictedAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean#L249). The attribute's comment: “(8) ⇒ (7) at τ = fppf”.

> **Stacks 0GZV, (8) ⇒ (7) at `τ = fppf`.** The module on `(Sch/S)_fppf` that condition (7)
> asks for is `𝒢^a` itself, which is quasi-coherent there by Stacks 03DV (1).

```lean
public theorem bigAffineFppf_isRestrictionOfQuasicoherent_of_isRestrictedAssociatedModule
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O))
    (hF : BigAffineFppf.IsRestrictedAssociatedModule B S hS F) :
    BigAffineFppf.IsRestrictionOfQuasicoherent B S hS F
```

**`AlgebraicGeometry.bigAffineFppf_isRestrictedAssociatedModule_of_isRestrictionOfQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean#L266). The attribute's comment: “(7) ⇒ (8) at τ = fppf, existence and uniqueness of 𝒢”.

> **Stacks 0GZV, (7) ⇒ (8) at `τ = fppf`**, with the uniqueness of `𝒢` included. The module
> `𝓜` on `(Sch/S)_fppf` given by condition (7) is quasi-coherent, hence isomorphic to `𝒢^a` for a
> quasi-coherent `𝒪_S`-module `𝒢` by the essential surjectivity half of Descent,
> Proposition 03DX (1) at `τ = fppf`; restricting that isomorphism to the affine objects gives
> `𝓕 ≅ 𝒢^a|_{(Aff/S)_fppf}`, and `𝒢` is unique up to isomorphism by
> `AlgebraicGeometry.fullyFaithfulBigAffineFppfAssociatedModuleQcoh`.

```lean
public theorem bigAffineFppf_isRestrictedAssociatedModule_of_isRestrictionOfQuasicoherent
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O))
    (hF : BigAffineFppf.IsRestrictionOfQuasicoherent B S hS F) :
    BigAffineFppf.IsRestrictedAssociatedModule B S hS F
```

**`AlgebraicGeometry.bigAffineFppf_isRestrictionOfQuasicoherent_iff_isRestrictedAssociatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteAssociatedModuleUnique.lean#L280). The attribute's comment: “(7) ⇔ (8) at τ = fppf”.

> **Stacks 0GZV, conditions (7) and (8) are equivalent at `τ = fppf`**, which is how the
> source reads them off each other from Descent, Proposition 03DX.

```lean
public theorem bigAffineFppf_isRestrictionOfQuasicoherent_iff_isRestrictedAssociatedModule
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O)) :
    BigAffineFppf.IsRestrictionOfQuasicoherent B S hS F ↔
      BigAffineFppf.IsRestrictedAssociatedModule B S hS F
```

**`AlgebraicGeometry.bigAffineFppf_isSheaf_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean#L195). The attribute's comment: “(1) ⇒ the sheaf conjunct of (6), at τ = fppf”.

> **Stacks 0GZV, condition (1) implies the sheaf conjunct of condition (6).** A presheaf of
> `𝒪_Aff`-modules on `(Aff/S)_fppf` all of whose base-change comparisons
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms satisfies the fppf sheaf axiom. The coverings of
> `(Aff/S)_fppf` are finite flat coverings of affine schemes, so this is flat descent of modules,
> Stacks 023M.

```lean
public theorem bigAffineFppf_isSheaf_of_cartesian
    (M : PresheafOfModules.{max m u}
      ((bigAffineFppfRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineFppf B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, m} M f)) :
    Presheaf.IsSheaf (BigAffineFppf.topology B S hS) M.presheaf
```

**`AlgebraicGeometry.bigAffineZariski_isSheaf_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean#L232). The attribute's comment: “(1) ⇒ the sheaf conjunct of (2), at τ = Zariski”.

> **Stacks 0GZV, condition (1) implies the sheaf conjunct of condition (2).** A presheaf of
> `𝒪_Aff`-modules on `(Aff/S)_Zar` all of whose base-change comparisons
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms satisfies the Zariski sheaf axiom. The
> coverings of `(Aff/S)_Zar` are finite flat coverings of affine schemes, so this is flat
> descent of modules, Stacks 023M.

```lean
public theorem bigAffineZariski_isSheaf_of_cartesian
    (M : PresheafOfModules.{max m u}
      ((bigAffineZariskiRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineZariski B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, m} M f)) :
    Presheaf.IsSheaf (BigAffineZariski.topology B S hS) M.presheaf
```

**`AlgebraicGeometry.bigAffineEtale_isSheaf_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean#L269). The attribute's comment: “(1) ⇒ the sheaf conjunct of (3), at τ = étale”.

> **Stacks 0GZV, condition (1) implies the sheaf conjunct of condition (3).** A presheaf of
> `𝒪_Aff`-modules on `(Aff/S)_étale` all of whose base-change comparisons
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms satisfies the étale sheaf axiom. The coverings
> of `(Aff/S)_étale` are finite flat coverings of affine schemes, so this is flat descent of
> modules, Stacks 023M.

```lean
public theorem bigAffineEtale_isSheaf_of_cartesian
    (M : PresheafOfModules.{max m u}
      ((bigAffineEtaleRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineEtale B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, m} M f)) :
    Presheaf.IsSheaf (BigAffineEtale.topology B S hS) M.presheaf
```

**`AlgebraicGeometry.bigAffineSmooth_isSheaf_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean#L306). The attribute's comment: “(1) ⇒ the sheaf conjunct of (4), at τ = smooth”.

> **Stacks 0GZV, condition (1) implies the sheaf conjunct of condition (4).** A presheaf of
> `𝒪_Aff`-modules on `(Aff/S)_smooth` all of whose base-change comparisons
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms satisfies the smooth sheaf axiom. The coverings
> of `(Aff/S)_smooth` are finite flat coverings of affine schemes, so this is flat descent of
> modules, Stacks 023M.

```lean
public theorem bigAffineSmooth_isSheaf_of_cartesian
    (M : PresheafOfModules.{max m u}
      ((bigAffineSmoothRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineSmooth B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, m} M f)) :
    Presheaf.IsSheaf (BigAffineSmooth.topology B S hS) M.presheaf
```

**`AlgebraicGeometry.bigAffineSyntomic_isSheaf_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCartesianSheaf.lean#L347). The attribute's comment: “(1) ⇒ the sheaf conjunct of (5), at τ = syntomic”.

> **Stacks 0GZV, condition (1) implies the sheaf conjunct of condition (5).** A presheaf of
> `𝒪_Aff`-modules on `(Aff/S)_syntomic` all of whose base-change comparisons
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms satisfies the syntomic sheaf axiom. The
> coverings of `(Aff/S)_syntomic` are finite flat coverings of affine schemes, so this is flat
> descent of modules, Stacks 023M.

```lean
public theorem bigAffineSyntomic_isSheaf_of_cartesian
    (M : PresheafOfModules.{max m u}
      ((bigAffineSyntomicRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineSyntomic B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, m} M f)) :
    Presheaf.IsSheaf (BigAffineSyntomic.topology B S hS) M.presheaf
```

**`AlgebraicGeometry.fullyFaithfulBigAffineAssociatedModuleQcohOf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L351). The attribute's comment: “(8) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}, uniqueness of 𝒢”.

> **Stacks 0GZV, the uniqueness of `𝒢` in condition (8), at every `τ`.** The functor
> `𝒢 ↦ 𝒢^a|_{(Aff/S)_τ}` from the quasi-coherent `𝒪_S`-modules to the `𝒪_Aff`-modules on
> `(Aff/S)_τ` is fully faithful: it is Stacks 0GN7 for the big `τ`-site followed by the Comparison
> Lemma for sheaves of modules on the dense subsite of affine objects.  No part of Descent,
> Proposition 03DX is used.

```lean
public noncomputable def fullyFaithfulBigAffineAssociatedModuleQcohOf (τ : SiteKind) :
    (bigAffineAssociatedModuleQcohOf B S hS τ).FullyFaithful
```

**`AlgebraicGeometry.bigAffine_iso_of_associatedModuleQcohOf_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L360). The attribute's comment: “(8) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}, uniqueness of 𝒢”.

> **Stacks 0GZV, the uniqueness of `𝒢` in condition (8) at every `τ`**, read as a uniqueness
> statement: two quasi-coherent `𝒪_S`-modules whose associated modules have isomorphic
> restrictions to `(Aff/S)_τ` are isomorphic.

```lean
public theorem bigAffine_iso_of_associatedModuleQcohOf_restriction_iso (τ : SiteKind)
    (G₁ G₂ : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory)
    (e : (bigAffineAssociatedModuleQcohOf B S hS τ).obj G₁ ≅
      (bigAffineAssociatedModuleQcohOf B S hS τ).obj G₂) :
    Nonempty (G₁.obj ≅ G₂.obj)
```

**`AlgebraicGeometry.bigAffine_isRestrictionOfQuasicoherentOf_of_isRestrictedAssociatedModuleOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L411). The attribute's comment: “(8) ⇒ (7) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}”.

> **Stacks 0GZV, (8) ⇒ (7) at every `τ`.** The module on `(Sch/S)_τ` that condition (7) asks
> for is `𝒢^a` itself, which is quasi-coherent there by Stacks 03DV (1).

```lean
public theorem bigAffine_isRestrictionOfQuasicoherentOf_of_isRestrictedAssociatedModuleOf
    (τ : SiteKind) (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineRingedSiteOf B S hS τ).O))
    (hF : BigAffineFppf.IsRestrictedAssociatedModuleOf B S hS τ F) :
    BigAffineFppf.IsRestrictionOfQuasicoherentOf B S hS τ F
```

**`AlgebraicGeometry.bigAffine_isRestrictionOfQuasicoherentOf_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L429). The attribute's comment: “(1) ⇒ (7) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}”.

> **Stacks 0GZV, (1) ⇒ (7) at every `τ`.** A sheaf of `𝒪_Aff`-modules on `(Aff/S)_τ` all of
> whose base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms corresponds, under the
> equivalence of ringed topoi of Stacks 0GZU, to a quasi-coherent module on `(Sch/S)_τ`.
>
> The three inputs are the quasi-coherence conjunct of condition (2)–(6) at `τ`; the existence of
> an ambient lift, by the Comparison Lemma at `τ`; and the quasi-coherence of that lift, by the
> reflection of quasi-coherence along the dense subsite.

```lean
public theorem bigAffine_isRestrictionOfQuasicoherentOf_of_canonicalMap_isIso (τ : SiteKind)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineRingedSiteOf B S hS τ).O))
    (h : ∀ ⦃U V : BigAffineFppf B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineRingedSiteOf B S hS τ) F f)) :
    BigAffineFppf.IsRestrictionOfQuasicoherentOf B S hS τ F
```

**`AlgebraicGeometry.bigAffine_isIso_canonicalMapOf_of_isRestrictionOfQuasicoherentOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L445). The attribute's comment: “(7) ⇒ (1) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}”.

> **Stacks 0GZV, (7) ⇒ (1) at every `τ`.** The restriction to `(Aff/S)_τ` of the quasi-coherent
> module given by condition (7) is quasi-coherent, hence cartesian by Stacks 0H04.

```lean
public theorem bigAffine_isIso_canonicalMapOf_of_isRestrictionOfQuasicoherentOf (τ : SiteKind)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineRingedSiteOf B S hS τ).O))
    (hF : BigAffineFppf.IsRestrictionOfQuasicoherentOf B S hS τ F)
    ⦃U V : BigAffineFppf B S hS⦄ (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineRingedSiteOf B S hS τ) F f)
```

**`AlgebraicGeometry.bigAffine_isRestrictedAssociatedModuleOf_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L466). The attribute's comment: “(1) ⇒ (8) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}, existence and uniqueness of 𝒢”.

> **Stacks 0GZV, (1) ⇒ (8) at every `τ`**, with the uniqueness of `𝒢` included.
>
> A cartesian sheaf of modules on `(Aff/S)_τ` satisfies the fppf sheaf axiom, so it is a sheaf of
> modules on `(Aff/S)_fppf` with the same underlying presheaf, where (1) ⇒ (8) is proved as
> `AlgebraicGeometry.bigAffineFppf_isRestrictedAssociatedModule_of_canonicalMap_isIso`.  Reading
> the resulting isomorphism back for `τ` and applying Stacks 0GNE to its right-hand side gives
> condition (8) at `τ`; the uniqueness is
> `AlgebraicGeometry.fullyFaithfulBigAffineAssociatedModuleQcohOf`.

```lean
public theorem bigAffine_isRestrictedAssociatedModuleOf_of_canonicalMap_isIso (τ : SiteKind)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineRingedSiteOf B S hS τ).O))
    (h : ∀ ⦃U V : BigAffineFppf B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineRingedSiteOf B S hS τ) F f)) :
    BigAffineFppf.IsRestrictedAssociatedModuleOf B S hS τ F
```

**`AlgebraicGeometry.bigAffine_isRestrictedAssociatedModuleOf_of_isRestrictionOfQuasicoherentOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L487). The attribute's comment: “(7) ⇒ (8) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}, existence and uniqueness of 𝒢”.

> **Stacks 0GZV, (7) ⇒ (8) at every `τ`**, with the uniqueness of `𝒢` included.  The route is
> (7) ⇒ (1) ⇒ (8); in particular clause (1) of Descent, Proposition 03DX at `τ` is not used.

```lean
public theorem bigAffine_isRestrictedAssociatedModuleOf_of_isRestrictionOfQuasicoherentOf
    (τ : SiteKind) (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineRingedSiteOf B S hS τ).O))
    (hF : BigAffineFppf.IsRestrictionOfQuasicoherentOf B S hS τ F) :
    BigAffineFppf.IsRestrictedAssociatedModuleOf B S hS τ F
```

**`AlgebraicGeometry.bigAffine_isRestrictionOfQuasicoherentOf_iff_isRestrictedAssociatedModuleOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteCoarserAssociatedModule.lean#L499). The attribute's comment: “(7) ⇔ (8) at every τ ∈ \{Zariski, étale, smooth, syntomic, fppf}”.

> **Stacks 0GZV, conditions (7) and (8) are equivalent, at every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`**, which is how the source reads them off each
> other from Descent, Proposition 03DX.

```lean
public theorem bigAffine_isRestrictionOfQuasicoherentOf_iff_isRestrictedAssociatedModuleOf
    (τ : SiteKind) (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineRingedSiteOf B S hS τ).O)) :
    BigAffineFppf.IsRestrictionOfQuasicoherentOf B S hS τ F ↔
      BigAffineFppf.IsRestrictedAssociatedModuleOf B S hS τ F
```

**`AlgebraicGeometry.bigAffineFppf_isRestrictionOfQuasicoherent_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteModuleComparisonLemma.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteModuleComparisonLemma.lean#L142). The attribute's comment: “(1) ⇒ (7) at τ = fppf”.

> **Stacks 0GZV, (1) ⇒ (7) at `τ = fppf`.** A sheaf of `𝒪_Aff`-modules on `(Aff/S)_fppf` all
> of whose base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms corresponds, under
> the equivalence of ringed topoi of Stacks 0GZU, to a quasi-coherent module on `(Sch/S)_fppf`.
>
> The three inputs are condition (6), by
> `AlgebraicGeometry.bigAffineFppf_isQuasicoherentOnSite_of_canonicalMap_isIso`; the existence of
> an ambient lift, by `AlgebraicGeometry.bigAffineFppf_exists_moduleLift`; and the quasi-coherence
> of that lift, by `AlgebraicGeometry.bigAffineFppf_isQuasicoherentOnSite_reflect`.

```lean
public theorem bigAffineFppf_isRestrictionOfQuasicoherent_of_canonicalMap_isIso
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O))
    (h : ∀ ⦃U V : BigAffineFppf B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineFppfRingedSite B S hS) F f)) :
    BigAffineFppf.IsRestrictionOfQuasicoherent B S hS F
```

**`AlgebraicGeometry.bigAffineFppf_isRestrictedAssociatedModule_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteModuleComparisonLemma.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteModuleComparisonLemma.lean#L161). The attribute's comment: “(1) ⇒ (8) at τ = fppf, existence and uniqueness of 𝒢”.

> **Stacks 0GZV, (1) ⇒ (8) at `τ = fppf`**, with the uniqueness of `𝒢` included. A sheaf of
> `𝒪_Aff`-modules on `(Aff/S)_fppf` all of whose base-change maps are isomorphisms is the
> restriction to the affine objects of the associated module `𝒢^a` of a quasi-coherent
> `𝒪_S`-module `𝒢`, unique up to isomorphism.
>
> This is (1) ⇒ (7) followed by the equivalence of conditions (7) and (8),
> `AlgebraicGeometry.bigAffineFppf_isRestrictionOfQuasicoherent_iff_isRestrictedAssociatedModule`.

```lean
public theorem bigAffineFppf_isRestrictedAssociatedModule_of_canonicalMap_isIso
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O))
    (h : ∀ ⦃U V : BigAffineFppf B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineFppfRingedSite B S hS) F f)) :
    BigAffineFppf.IsRestrictedAssociatedModule B S hS F
```

**`AlgebraicGeometry.bigAffineZariski_isSheaf_and_isQuasicoherentOnSite_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean#L66). The attribute's comment: “(1) ⇒ (2) in full, for a presheaf of modules”.

> **Stacks 0GZV, condition (1) implies condition (2) in full.** A presheaf of `𝒪_Aff`-modules
> on `(Aff/S)_Zar` all of whose base-change comparisons `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are
> isomorphisms satisfies the Zariski sheaf axiom and is quasi-coherent on the ringed site
> `((Aff/S)_Zar, 𝒪_Aff)`.

```lean
public theorem bigAffineZariski_isSheaf_and_isQuasicoherentOnSite_of_cartesian
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : PresheafOfModules.{u}
      ((bigAffineZariskiRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineZariski B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} M f)) :
    ∃ hsheaf : Presheaf.IsSheaf (BigAffineZariski.topology B S hS) M.presheaf,
      (⟨M, hsheaf⟩ : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (bigAffineZariskiRingedSite B S hS).O)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineEtale_isSheaf_and_isQuasicoherentOnSite_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean#L84). The attribute's comment: “(1) ⇒ (3) in full, for a presheaf of modules”.

> **Stacks 0GZV, condition (1) implies condition (3) in full.** A presheaf of `𝒪_Aff`-modules
> on `(Aff/S)_étale` all of whose base-change comparisons `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are
> isomorphisms satisfies the étale sheaf axiom and is quasi-coherent on the ringed site
> `((Aff/S)_étale, 𝒪_Aff)`.

```lean
public theorem bigAffineEtale_isSheaf_and_isQuasicoherentOnSite_of_cartesian
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : PresheafOfModules.{u}
      ((bigAffineEtaleRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineEtale B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} M f)) :
    ∃ hsheaf : Presheaf.IsSheaf (BigAffineEtale.topology B S hS) M.presheaf,
      (⟨M, hsheaf⟩ : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (bigAffineEtaleRingedSite B S hS).O)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineSmooth_isSheaf_and_isQuasicoherentOnSite_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean#L102). The attribute's comment: “(1) ⇒ (4) in full, for a presheaf of modules”.

> **Stacks 0GZV, condition (1) implies condition (4) in full.** A presheaf of `𝒪_Aff`-modules
> on `(Aff/S)_smooth` all of whose base-change comparisons `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are
> isomorphisms satisfies the smooth sheaf axiom and is quasi-coherent on the ringed site
> `((Aff/S)_smooth, 𝒪_Aff)`.

```lean
public theorem bigAffineSmooth_isSheaf_and_isQuasicoherentOnSite_of_cartesian
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (M : PresheafOfModules.{u}
      ((bigAffineSmoothRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineSmooth B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} M f)) :
    ∃ hsheaf : Presheaf.IsSheaf (BigAffineSmooth.topology B S hS) M.presheaf,
      (⟨M, hsheaf⟩ : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (bigAffineSmoothRingedSite B S hS).O)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineSyntomic_isSheaf_and_isQuasicoherentOnSite_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean#L120). The attribute's comment: “(1) ⇒ (5) in full, for a presheaf of modules”.

> **Stacks 0GZV, condition (1) implies condition (5) in full.** A presheaf of `𝒪_Aff`-modules
> on `(Aff/S)_syntomic` all of whose base-change comparisons `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are
> isomorphisms satisfies the syntomic sheaf axiom and is quasi-coherent on the ringed site
> `((Aff/S)_syntomic, 𝒪_Aff)`.

```lean
public theorem bigAffineSyntomic_isSheaf_and_isQuasicoherentOnSite_of_cartesian
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : PresheafOfModules.{u}
      ((bigAffineSyntomicRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineSyntomic B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} M f)) :
    ∃ hsheaf : Presheaf.IsSheaf (BigAffineSyntomic.topology B S hS) M.presheaf,
      (⟨M, hsheaf⟩ : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (bigAffineSyntomicRingedSite B S hS).O)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineFppf_isSheaf_and_isQuasicoherentOnSite_of_cartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSitePresheafConditions.lean#L138). The attribute's comment: “(1) ⇒ (6) in full, for a presheaf of modules”.

> **Stacks 0GZV, condition (1) implies condition (6) in full.** A presheaf of `𝒪_Aff`-modules
> on `(Aff/S)_fppf` all of whose base-change comparisons `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are
> isomorphisms satisfies the fppf sheaf axiom and is quasi-coherent on the ringed site
> `((Aff/S)_fppf, 𝒪_Aff)`.

```lean
public theorem bigAffineFppf_isSheaf_and_isQuasicoherentOnSite_of_cartesian
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : PresheafOfModules.{u}
      ((bigAffineFppfRingedSite B S hS).O.obj ⋙ forget₂ CommRingCat RingCat))
    (hM : ∀ {X Y : (BigAffineFppf B S hS)ᵒᵖ} (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} M f)) :
    ∃ hsheaf : Presheaf.IsSheaf (BigAffineFppf.topology B S hS) M.presheaf,
      (⟨M, hsheaf⟩ : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (bigAffineFppfRingedSite B S hS).O)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineFppf_isIso_canonicalMap_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L302). The attribute's comment: “(6) ⇒ (1), from the quasi-coherence conjunct of (6)”.

> **Stacks 0GZV, condition (6) implies condition (1).** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_fppf` which is quasi-coherent on the ringed site `((Aff/S)_fppf, 𝒪_Aff)` has all its
> base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` isomorphisms.

```lean
theorem bigAffineFppf_isIso_canonicalMap_of_isQuasicoherentOnSite
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) {U V : BigAffineFppf B S hS} (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineFppfRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineZariski_isIso_canonicalMap_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L372). The attribute's comment: “(2) ⇒ (1), from the quasi-coherence conjunct of (2)”.

> **Stacks 0GZV, condition (2) implies condition (1).** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_Zar` which is quasi-coherent on the ringed site `((Aff/S)_Zar, 𝒪_Aff)` has all its
> base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` isomorphisms.

```lean
theorem bigAffineZariski_isIso_canonicalMap_of_isQuasicoherentOnSite
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineZariskiRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) {U V : BigAffineZariski B S hS} (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineZariskiRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineEtale_isIso_canonicalMap_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L390). The attribute's comment: “(3) ⇒ (1), from the quasi-coherence conjunct of (3)”.

> **Stacks 0GZV, condition (3) implies condition (1).** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_étale` which is quasi-coherent on the ringed site `((Aff/S)_étale, 𝒪_Aff)` has all its
> base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` isomorphisms.

```lean
theorem bigAffineEtale_isIso_canonicalMap_of_isQuasicoherentOnSite
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineEtaleRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) {U V : BigAffineEtale B S hS} (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineEtaleRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineSmooth_isIso_canonicalMap_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L408). The attribute's comment: “(4) ⇒ (1), from the quasi-coherence conjunct of (4)”.

> **Stacks 0GZV, condition (4) implies condition (1).** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_smooth` which is quasi-coherent on the ringed site `((Aff/S)_smooth, 𝒪_Aff)` has all its
> base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` isomorphisms.

```lean
theorem bigAffineSmooth_isIso_canonicalMap_of_isQuasicoherentOnSite
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSmoothRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) {U V : BigAffineSmooth B S hS} (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineSmoothRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineSyntomic_isIso_canonicalMap_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L426). The attribute's comment: “(5) ⇒ (1), from the quasi-coherence conjunct of (5)”.

> **Stacks 0GZV, condition (5) implies condition (1).** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_syntomic` which is quasi-coherent on the ringed site `((Aff/S)_syntomic, 𝒪_Aff)` has all
> its base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` isomorphisms.

```lean
theorem bigAffineSyntomic_isIso_canonicalMap_of_isQuasicoherentOnSite
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSyntomicRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) {U V : BigAffineSyntomic B S hS} (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineSyntomicRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineFppf_isQuasicoherentOnSite_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L447). The attribute's comment: “(1) ⇔ (6), for a sheaf of modules”.

> **Stacks 0GZV, (1) ⇔ (6), for a sheaf of modules.** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_fppf` is quasi-coherent on the ringed site `((Aff/S)_fppf, 𝒪_Aff)` exactly when all of
> its base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms.
>
> The sheaf conjunct of condition (6) is carried by the type of `M`; for a presheaf of modules it
> is `AlgebraicGeometry.bigAffineFppf_isSheaf_of_cartesian`.

```lean
theorem bigAffineFppf_isQuasicoherentOnSite_iff_canonicalMap_isIso
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O)) :
    M.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : BigAffineFppf B S hS⦄ (f : U ⟶ V),
        IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineFppfRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineZariski_isQuasicoherentOnSite_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L464). The attribute's comment: “(1) ⇔ (2), for a sheaf of modules”.

> **Stacks 0GZV, (1) ⇔ (2), for a sheaf of modules.** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_Zar` is quasi-coherent on the ringed site `((Aff/S)_Zar, 𝒪_Aff)` exactly when all of
> its base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms.
>
> The sheaf conjunct of condition (2) is carried by the type of `M`; for a presheaf of modules it
> is `AlgebraicGeometry.bigAffineZariski_isSheaf_of_cartesian`.

```lean
theorem bigAffineZariski_isQuasicoherentOnSite_iff_canonicalMap_isIso
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineZariskiRingedSite B S hS).O)) :
    M.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : BigAffineZariski B S hS⦄ (f : U ⟶ V),
        IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineZariskiRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineEtale_isQuasicoherentOnSite_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L481). The attribute's comment: “(1) ⇔ (3), for a sheaf of modules”.

> **Stacks 0GZV, (1) ⇔ (3), for a sheaf of modules.** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_étale` is quasi-coherent on the ringed site `((Aff/S)_étale, 𝒪_Aff)` exactly when all of
> its base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms.
>
> The sheaf conjunct of condition (3) is carried by the type of `M`; for a presheaf of modules it
> is `AlgebraicGeometry.bigAffineEtale_isSheaf_of_cartesian`.

```lean
theorem bigAffineEtale_isQuasicoherentOnSite_iff_canonicalMap_isIso
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineEtaleRingedSite B S hS).O)) :
    M.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : BigAffineEtale B S hS⦄ (f : U ⟶ V),
        IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineEtaleRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineSmooth_isQuasicoherentOnSite_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L498). The attribute's comment: “(1) ⇔ (4), for a sheaf of modules”.

> **Stacks 0GZV, (1) ⇔ (4), for a sheaf of modules.** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_smooth` is quasi-coherent on the ringed site `((Aff/S)_smooth, 𝒪_Aff)` exactly when all of
> its base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms.
>
> The sheaf conjunct of condition (4) is carried by the type of `M`; for a presheaf of modules it
> is `AlgebraicGeometry.bigAffineSmooth_isSheaf_of_cartesian`.

```lean
theorem bigAffineSmooth_isQuasicoherentOnSite_iff_canonicalMap_isIso
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSmoothRingedSite B S hS).O)) :
    M.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : BigAffineSmooth B S hS⦄ (f : U ⟶ V),
        IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineSmoothRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineSyntomic_isQuasicoherentOnSite_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/BigAffineSiteQuasicoherentCartesian.lean#L515). The attribute's comment: “(1) ⇔ (5), for a sheaf of modules”.

> **Stacks 0GZV, (1) ⇔ (5), for a sheaf of modules.** A sheaf of `𝒪_Aff`-modules on
> `(Aff/S)_syntomic` is quasi-coherent on the ringed site `((Aff/S)_syntomic, 𝒪_Aff)` exactly when
> all of its base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms.
>
> The sheaf conjunct of condition (5) is carried by the type of `M`; for a presheaf of modules it
> is `AlgebraicGeometry.bigAffineSyntomic_isSheaf_of_cartesian`.

```lean
theorem bigAffineSyntomic_isQuasicoherentOnSite_iff_canonicalMap_isIso
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSyntomicRingedSite B S hS).O)) :
    M.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : BigAffineSyntomic B S hS⦄ (f : U ⟶ V),
        IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineSyntomicRingedSite B S hS) M f)
```

**`AlgebraicGeometry.bigAffineZariski_isQuasicoherentOnSite_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L506). The attribute's comment: “(1) ⇒ (2), quasi-coherence conjunct of (2)”.

> **Stacks 0GZV, condition (2).** A sheaf of modules on `(Aff/S)_Zar` whose base-change maps
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are all isomorphisms is quasi-coherent on the ringed site
> `((Aff/S)_Zar, 𝒪_Aff)`.

```lean
public theorem bigAffineZariski_isQuasicoherentOnSite_of_canonicalMap_isIso
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineZariskiRingedSite B S hS).O))
    (h : ∀ ⦃U V : BigAffineZariski B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineZariskiRingedSite B S hS) F f)) :
    F.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineZariski_isQuasicoherentOnSite_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L518). The attribute's comment: “(7) ⇒ (2) at τ = Zariski, quasi-coherence conjunct of (2)”.

> **Stacks 0GZV, condition (2).** The restriction to `(Aff/S)_Zar` of a quasi-coherent module
> on the ringed site `((Sch/S)_Zar, 𝒪)` is quasi-coherent on `((Aff/S)_Zar, 𝒪_Aff)`.

```lean
public theorem bigAffineZariski_isQuasicoherentOnSite_restriction
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigZariskiOverRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) :
    ((SheafOfModules.pushforward.{u} (F := BigAffineZariski.inclusion B S hS)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (bigZariskiOverRingedSite B S hS).O))
      (S := (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineZariskiRingedSite B S hS).O))
        (𝟙 _)).obj
        M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineEtale_isQuasicoherentOnSite_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L534). The attribute's comment: “(1) ⇒ (3), quasi-coherence conjunct of (3)”.

> **Stacks 0GZV, condition (3).** A sheaf of modules on `(Aff/S)_étale` whose base-change maps
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are all isomorphisms is quasi-coherent on the ringed site
> `((Aff/S)_étale, 𝒪_Aff)`.

```lean
public theorem bigAffineEtale_isQuasicoherentOnSite_of_canonicalMap_isIso
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineEtaleRingedSite B S hS).O))
    (h : ∀ ⦃U V : BigAffineEtale B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineEtaleRingedSite B S hS) F f)) :
    F.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineEtale_isQuasicoherentOnSite_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L547). The attribute's comment: “(7) ⇒ (3) at τ = étale, quasi-coherence conjunct of (3)”.

> **Stacks 0GZV, condition (3).** The restriction to `(Aff/S)_étale` of a quasi-coherent
> module on the ringed site `((Sch/S)_étale, 𝒪)` is quasi-coherent on
> `((Aff/S)_étale, 𝒪_Aff)`.

```lean
public theorem bigAffineEtale_isQuasicoherentOnSite_restriction
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigEtaleOverRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) :
    ((SheafOfModules.pushforward.{u} (F := BigAffineEtale.inclusion B S hS)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (bigEtaleOverRingedSite B S hS).O))
      (S := (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineEtaleRingedSite B S hS).O))
        (𝟙 _)).obj
        M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineSmooth_isQuasicoherentOnSite_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L563). The attribute's comment: “(1) ⇒ (4), quasi-coherence conjunct of (4)”.

> **Stacks 0GZV, condition (4).** A sheaf of modules on `(Aff/S)_smooth` whose base-change
> maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are all isomorphisms is quasi-coherent on the ringed site
> `((Aff/S)_smooth, 𝒪_Aff)`.

```lean
public theorem bigAffineSmooth_isQuasicoherentOnSite_of_canonicalMap_isIso
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSmoothRingedSite B S hS).O))
    (h : ∀ ⦃U V : BigAffineSmooth B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineSmoothRingedSite B S hS) F f)) :
    F.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineSmooth_isQuasicoherentOnSite_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L576). The attribute's comment: “(7) ⇒ (4) at τ = smooth, quasi-coherence conjunct of (4)”.

> **Stacks 0GZV, condition (4).** The restriction to `(Aff/S)_smooth` of a quasi-coherent
> module on the ringed site `((Sch/S)_smooth, 𝒪)` is quasi-coherent on
> `((Aff/S)_smooth, 𝒪_Aff)`.

```lean
public theorem bigAffineSmooth_isQuasicoherentOnSite_restriction
    (B : BigSmoothSite.{u}) (S : Scheme.{u}) (hS : S.size < B.cutoff)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigSmoothOverRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) :
    ((SheafOfModules.pushforward.{u} (F := BigAffineSmooth.inclusion B S hS)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (bigSmoothOverRingedSite B S hS).O))
      (S := (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSmoothRingedSite B S hS).O))
        (𝟙 _)).obj
        M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineSyntomic_isQuasicoherentOnSite_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L592). The attribute's comment: “(1) ⇒ (5), quasi-coherence conjunct of (5)”.

> **Stacks 0GZV, condition (5).** A sheaf of modules on `(Aff/S)_syntomic` whose base-change
> maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are all isomorphisms is quasi-coherent on the ringed site
> `((Aff/S)_syntomic, 𝒪_Aff)`.

```lean
public theorem bigAffineSyntomic_isQuasicoherentOnSite_of_canonicalMap_isIso
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSyntomicRingedSite B S hS).O))
    (h : ∀ ⦃U V : BigAffineSyntomic B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineSyntomicRingedSite B S hS) F f)) :
    F.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineSyntomic_isQuasicoherentOnSite_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L605). The attribute's comment: “(7) ⇒ (5) at τ = syntomic, quasi-coherence conjunct of (5)”.

> **Stacks 0GZV, condition (5).** The restriction to `(Aff/S)_syntomic` of a quasi-coherent
> module on the ringed site `((Sch/S)_syntomic, 𝒪)` is quasi-coherent on
> `((Aff/S)_syntomic, 𝒪_Aff)`.

```lean
public theorem bigAffineSyntomic_isQuasicoherentOnSite_restriction
    (B : BigSyntomicSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigSyntomicOverRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) :
    ((SheafOfModules.pushforward.{u} (F := BigAffineSyntomic.inclusion B S hS)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (bigSyntomicOverRingedSite B S hS).O))
      (S := (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineSyntomicRingedSite B S hS).O))
        (𝟙 _)).obj
        M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineFppf_isQuasicoherentOnSite_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L621). The attribute's comment: “(1) ⇒ (6), quasi-coherence conjunct of (6)”.

> **Stacks 0GZV, condition (6).** A sheaf of modules on `(Aff/S)_fppf` whose base-change maps
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are all isomorphisms is quasi-coherent on the ringed site
> `((Aff/S)_fppf, 𝒪_Aff)`.

```lean
public theorem bigAffineFppf_isQuasicoherentOnSite_of_canonicalMap_isIso
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O))
    (h : ∀ ⦃U V : BigAffineFppf B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (bigAffineFppfRingedSite B S hS) F f)) :
    F.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.bigAffineFppf_isQuasicoherentOnSite_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 633](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L633). The attribute's comment: “(7) ⇒ (6) at τ = fppf, quasi-coherence conjunct of (6)”.

> **Stacks 0GZV, condition (6).** The restriction to `(Aff/S)_fppf` of a quasi-coherent module
> on the ringed site `((Sch/S)_fppf, 𝒪)` is quasi-coherent on `((Aff/S)_fppf, 𝒪_Aff)`.

```lean
public theorem bigAffineFppf_isQuasicoherentOnSite_restriction
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (bigFppfOverRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) :
    ((SheafOfModules.pushforward.{u} (F := BigAffineFppf.inclusion B S hS)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (bigFppfOverRingedSite B S hS).O))
      (S := (Stacks.SheafOfModules.Tensor.ringSheaf (bigAffineFppfRingedSite B S hS).O))
        (𝟙 _)).obj
        M).IsQuasicoherentOnSite
```

## Tag 0GZW, an equation

[Tag 0GZW](https://stacks.math.columbia.edu/tag/0GZW) in the Stacks Project.

**`AlgebraicGeometry.SmallAffineZariski.ringedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L181). The attribute's comment: “Zariski case”.

> The morphism of ringed topoi `(Sh(S_{affine, Zar}), 𝒪_affine) ⟶ (Sh(S_Zar), 𝒪)` given by the
> inclusion of the affine objects of the small Zariski site of `S`, with structure morphism the
> adjunct of the identification of `g⁻¹𝒪` with the restriction `𝒪_affine` of `𝒪`.

```lean
public noncomputable def ringedToposHom :
    RingedToposHom (ringedTopos B S hS) (SmallZariski.ringedTopos B S hS)
```

**`AlgebraicGeometry.SmallAffineZariski.ringedToposHom_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L190). The attribute's comment: “Zariski case”.

> The inverse image of the equivalence is restriction along the inclusion of the affine objects,
> on the nose.

```lean
public theorem ringedToposHom_inverseImage :
    (ringedToposHom B S hS).toToposHom.inverseImage =
      (inclusion B S hS).sheafPushforwardContinuous (Type u)
        (topology B S hS) (SmallZariski.topology B S hS)
```

**`AlgebraicGeometry.SmallAffineZariski.ringedToposHom_inverseImage_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L199). The attribute's comment: “Zariski case”.

> The underlying morphism of topoi is an equivalence of topoi: its inverse image, restriction
> along the inclusion of the affine objects, is an equivalence of categories of sheaves.

```lean
public theorem ringedToposHom_inverseImage_isEquivalence :
    (ringedToposHom B S hS).toToposHom.inverseImage.IsEquivalence
```

**`AlgebraicGeometry.SmallAffineZariski.isIso_ringedToposHom_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L215). The attribute's comment: “Zariski case”.

> The structure morphism `g⁻¹𝒪 ⟶ 𝒪_affine` is an isomorphism, so the morphism of ringed topoi is
> an equivalence of ringed topoi and not merely a morphism whose underlying morphism of topoi is an
> equivalence.

```lean
public theorem isIso_ringedToposHom_fSharpInverseImage :
    IsIso (ringedToposHom B S hS).fSharpInverseImage
```

**`AlgebraicGeometry.SmallAffineZariski.ringedToposHom_fSharpInverseImage_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L223). The attribute's comment: “Zariski case”.

> The structure morphism is the canonical one: on underlying sheaves of sets it is the identity
> of the restriction of the underlying sheaf of sets of `𝒪`, so `𝒪_affine` really is `𝒪` restricted
> and not an arbitrary sheaf of rings with the same underlying sheaf of sets.

```lean
public theorem ringedToposHom_fSharpInverseImage_forget :
    (sheafCompose (topology B S hS) (forget CommRingCat.{u})).map
        (ringedToposHom B S hS).fSharpInverseImage =
      𝟙 ((inclusion B S hS).sheafPushforwardContinuous (Type u)
        (topology B S hS) (SmallZariski.topology B S hS) |>.obj
        ((sheafCompose (SmallZariski.topology B S hS) (forget CommRingCat.{u})).obj
          (SmallZariski.ringedTopos B S hS).O))
```

**`AlgebraicGeometry.SmallAffineEtale.ringedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L328). The attribute's comment: “étale case”.

> The morphism of ringed topoi `(Sh(S_{affine, étale}), 𝒪_affine) ⟶ (Sh(S_étale), 𝒪)` given by
> the inclusion of the affine objects of the small étale site of `S`, with structure morphism the
> adjunct of the identification of `g⁻¹𝒪` with the restriction `𝒪_affine` of `𝒪`.

```lean
public noncomputable def ringedToposHom :
    RingedToposHom (ringedTopos B S hS) (SmallEtale.ringedTopos B S hS)
```

**`AlgebraicGeometry.SmallAffineEtale.ringedToposHom_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L337). The attribute's comment: “étale case”.

> The inverse image of the equivalence is restriction along the inclusion of the affine objects,
> on the nose.

```lean
public theorem ringedToposHom_inverseImage :
    (ringedToposHom B S hS).toToposHom.inverseImage =
      (inclusion B S hS).sheafPushforwardContinuous (Type u)
        (topology B S hS) (SmallEtale.topology B S hS)
```

**`AlgebraicGeometry.SmallAffineEtale.ringedToposHom_inverseImage_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L346). The attribute's comment: “étale case”.

> The underlying morphism of topoi is an equivalence of topoi: its inverse image, restriction
> along the inclusion of the affine objects, is an equivalence of categories of sheaves.

```lean
public theorem ringedToposHom_inverseImage_isEquivalence :
    (ringedToposHom B S hS).toToposHom.inverseImage.IsEquivalence
```

**`AlgebraicGeometry.SmallAffineEtale.isIso_ringedToposHom_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L362). The attribute's comment: “étale case”.

> The structure morphism `g⁻¹𝒪 ⟶ 𝒪_affine` is an isomorphism, so the morphism of ringed topoi is
> an equivalence of ringed topoi and not merely a morphism whose underlying morphism of topoi is an
> equivalence.

```lean
public theorem isIso_ringedToposHom_fSharpInverseImage :
    IsIso (ringedToposHom B S hS).fSharpInverseImage
```

**`AlgebraicGeometry.SmallAffineEtale.ringedToposHom_fSharpInverseImage_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineRingedTopos.lean#L370). The attribute's comment: “étale case”.

> The structure morphism is the canonical one: on underlying sheaves of sets it is the identity
> of the restriction of the underlying sheaf of sets of `𝒪`, so `𝒪_affine` really is `𝒪` restricted
> and not an arbitrary sheaf of rings with the same underlying sheaf of sets.

```lean
public theorem ringedToposHom_fSharpInverseImage_forget :
    (sheafCompose (topology B S hS) (forget CommRingCat.{u})).map
        (ringedToposHom B S hS).fSharpInverseImage =
      𝟙 ((inclusion B S hS).sheafPushforwardContinuous (Type u)
        (topology B S hS) (SmallEtale.topology B S hS) |>.obj
        ((sheafCompose (SmallEtale.topology B S hS) (forget CommRingCat.{u})).obj
          (SmallEtale.ringedTopos B S hS).O))
```

## Tag 0GZX, a lemma

[Tag 0GZX](https://stacks.math.columbia.edu/tag/0GZX) in the Stacks Project.

**`AlgebraicGeometry.smallAffineZariski_isQuasicoherentOnSite_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L366). The attribute's comment: “(1) ⇒ (2) at τ = Zariski, quasi-coherence conjunct of (2)”.

> **Stacks 0GZX, Zariski case.** A sheaf of modules on the small affine Zariski site of `S`
> whose base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are all isomorphisms is quasi-coherent on
> the ringed site `(S_{affine, Zar}, 𝒪_affine)`.

```lean
public theorem smallAffineZariski_isQuasicoherentOnSite_of_canonicalMap_isIso
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallAffineZariskiRingedSite B S hS).O))
    (h : ∀ ⦃U V : SmallAffineZariski B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineZariskiRingedSite B S hS) F f)) :
    F.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.smallAffineZariski_isQuasicoherentOnSite_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L379). The attribute's comment: “(3) ⇒ (2) at τ = Zariski, quasi-coherence conjunct of (2)”.

> **Stacks 0GZX, Zariski case.** The restriction to the small affine Zariski site of `S` of a
> quasi-coherent module on the ringed site `(S_Zar, 𝒪)` is quasi-coherent on
> `(S_{affine, Zar}, 𝒪_affine)`.

```lean
public theorem smallAffineZariski_isQuasicoherentOnSite_restriction
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallZariskiRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) :
    ((SheafOfModules.pushforward.{u} (F := SmallAffineZariski.inclusion B S hS)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (smallZariskiRingedSite B S hS).O))
      (S := (Stacks.SheafOfModules.Tensor.ringSheaf (smallAffineZariskiRingedSite B S hS).O))
        (𝟙 _)).obj
        M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.smallAffineEtale_isQuasicoherentOnSite_of_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L395). The attribute's comment: “(1) ⇒ (2) at τ = étale, quasi-coherence conjunct of (2)”.

> **Stacks 0GZX, étale case.** A sheaf of modules on the small affine étale site of `S` whose
> base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are all isomorphisms is quasi-coherent on the
> ringed site `(S_{affine, étale}, 𝒪_affine)`.

```lean
public theorem smallAffineEtale_isQuasicoherentOnSite_of_canonicalMap_isIso
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallAffineEtaleRingedSite B S hS).O))
    (h : ∀ ⦃U V : SmallAffineEtale B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineEtaleRingedSite B S hS) F f)) :
    F.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.smallAffineEtale_isQuasicoherentOnSite_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffines.lean#L408). The attribute's comment: “(3) ⇒ (2) at τ = étale, quasi-coherence conjunct of (2)”.

> **Stacks 0GZX, étale case.** The restriction to the small affine étale site of `S` of a
> quasi-coherent module on the ringed site `(S_étale, 𝒪)` is quasi-coherent on
> `(S_{affine, étale}, 𝒪_affine)`.

```lean
public theorem smallAffineEtale_isQuasicoherentOnSite_restriction
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (M : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS).O))
    (hM : M.IsQuasicoherentOnSite) :
    ((SheafOfModules.pushforward.{u} (F := SmallAffineEtale.inclusion B S hS)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS).O))
      (S := (Stacks.SheafOfModules.Tensor.ringSheaf (smallAffineEtaleRingedSite B S hS).O))
        (𝟙 _)).obj
        M).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.smallAffineEtale_exists_isQuasicoherentOnSite_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean#L125). The attribute's comment: “(2) ⇒ (3) at τ = étale”.

> A sheaf of modules on the small affine étale site of `S` which is quasi-coherent on the ringed
> site `(S_{affine, étale}, 𝒪_affine)` is the restriction of a quasi-coherent `𝒪`-module on
> `(S_étale, 𝒪)`.

```lean
public theorem smallAffineEtale_exists_isQuasicoherentOnSite_restriction_iso
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineEtaleRingedSite B S hS).O))
    (hF : F.IsQuasicoherentOnSite) :
    ∃ N : SheafOfModules.{u} (SmallEtale.structureSheaf B S hS), N.IsQuasicoherentOnSite ∧
      Nonempty ((smallAffineEtaleModuleRestriction B S hS).obj N ≅ F)
```

**`AlgebraicGeometry.smallAffineEtale_essImage_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean#L142). The attribute's comment: “(4) at τ = étale, existence of 𝒢”.

> A sheaf of modules `𝓕` on the small affine étale site of `S` which is quasi-coherent on the
> ringed site `(S_{affine, étale}, 𝒪_affine)` lies in the essential image of the functor
> `𝒢 ↦ 𝒢ᵃ|_{S_{affine, étale}}` on quasi-coherent `𝒪_S`-modules.

```lean
public theorem smallAffineEtale_essImage_associatedModuleQcoh
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineEtaleRingedSite B S hS).O))
    (hF : F.IsQuasicoherentOnSite) :
    (smallAffineEtaleAssociatedModuleQcoh B S hS).essImage F
```

**`AlgebraicGeometry.smallAffineEtale_exists_associatedModuleQcoh_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean#L161). The attribute's comment: “(1) ⇒ (4) at τ = étale, existence of 𝒢”.

> A sheaf of modules on the small affine étale site of `S` all of whose base-change maps
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms is isomorphic to `𝒢ᵃ|_{S_{affine, étale}}` for a
> quasi-coherent `𝒪_S`-module `𝒢`.

```lean
public theorem smallAffineEtale_exists_associatedModuleQcoh_restriction_iso
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineEtaleRingedSite B S hS).O))
    (hF : ∀ ⦃U V : SmallAffineEtale B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineEtaleRingedSite B S hS) F f)) :
    ∃ G : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory,
      Nonempty ((smallAffineEtaleAssociatedModuleQcoh B S hS).obj G ≅ F)
```

**`AlgebraicGeometry.isEquivalence_smallAffineEtaleModuleRestrictionQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean#L206). The attribute's comment: “(2) ⇔ (3) at τ = étale”.

> Restriction to the affine objects is an equivalence
> `QCoh(S_étale, 𝒪) ≌ QCoh(S_{affine, étale}, 𝒪_affine)` between the categories of quasi-coherent
> modules.

```lean
public theorem isEquivalence_smallAffineEtaleModuleRestrictionQcoh :
    (smallAffineEtaleModuleRestrictionQcoh B S hS).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_smallAffineEtaleAssociatedModuleQcohOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean#L249). The attribute's comment: “(2) ⇔ (4) at τ = étale”.

> The functor `𝒢 ↦ 𝒢ᵃ|_{S_{affine, étale}}` is an equivalence from the quasi-coherent
> `𝒪_S`-modules onto the quasi-coherent modules on the ringed site `(S_{affine, étale}, 𝒪_affine)`:
> every such module comes from a `𝒢`, and from a unique one.

```lean
public theorem isEquivalence_smallAffineEtaleAssociatedModuleQcohOnSite :
    (smallAffineEtaleAssociatedModuleQcohOnSite B S hS).IsEquivalence
```

**`AlgebraicGeometry.smallAffineEtaleAssociatedModuleQcohEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesExists.lean#L260). The attribute's comment: “(2) ⇔ (4) at τ = étale”.

> The equivalence of categories `QCoh(𝒪_S) ≌ QCoh(S_{affine, étale}, 𝒪_affine)` with functor
> `𝒢 ↦ 𝒢ᵃ|_{S_{affine, étale}}`.

```lean
public noncomputable def smallAffineEtaleAssociatedModuleQcohEquivalence :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallAffineEtaleRingedSite B S hS).O)).FullSubcategory
```

**`AlgebraicGeometry.smallAffineZariski_isSheaf_of_baseChange_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L68). The attribute's comment: “(1) ⇒ (2) at τ = Zariski, sheaf conjunct of (2)”.

> A presheaf of `𝒪_affine`-modules on the small affine Zariski site of `S` all of whose
> base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms is a sheaf.

```lean
theorem smallAffineZariski_isSheaf_of_baseChange_isIso
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : PresheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineZariskiRingedSite B S hS).O).obj)
    (h : ∀ ⦃X Y : (SmallAffineZariski B S hS)ᵒᵖ⦄ (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} F f)) :
    Presheaf.IsSheaf (smallAffineZariskiRingedSite B S hS).J F.presheaf
```

**`AlgebraicGeometry.smallAffineEtale_isSheaf_of_baseChange_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L80). The attribute's comment: “(1) ⇒ (2) at τ = étale, sheaf conjunct of (2)”.

> A presheaf of `𝒪_affine`-modules on the small affine étale site of `S` all of whose base-change
> maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms is a sheaf.

```lean
theorem smallAffineEtale_isSheaf_of_baseChange_isIso
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : PresheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineEtaleRingedSite B S hS).O).obj)
    (h : ∀ ⦃X Y : (SmallAffineEtale B S hS)ᵒᵖ⦄ (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} F f)) :
    Presheaf.IsSheaf (smallAffineEtaleRingedSite B S hS).J F.presheaf
```

**`AlgebraicGeometry.smallAffineZariski_isSheaf_and_isQuasicoherentOnSite_of_baseChange_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L110). The attribute's comment: “(1) ⇒ (2) at τ = Zariski, for a presheaf of modules”.

> A presheaf of `𝒪_affine`-modules on the small affine Zariski site of `S` all of whose
> base-change maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms is a sheaf, and the resulting sheaf
> of modules is quasi-coherent on the ringed site `(S_{affine, Zar}, 𝒪_affine)`.

```lean
theorem smallAffineZariski_isSheaf_and_isQuasicoherentOnSite_of_baseChange_isIso
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : PresheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineZariskiRingedSite B S hS).O).obj)
    (h : ∀ ⦃X Y : (SmallAffineZariski B S hS)ᵒᵖ⦄ (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} F f)) :
    ∃ hs : Presheaf.IsSheaf (smallAffineZariskiRingedSite B S hS).J F.presheaf,
      (⟨F, hs⟩ : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallAffineZariskiRingedSite B S hS).O)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.smallAffineEtale_isSheaf_and_isQuasicoherentOnSite_of_baseChange_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L127). The attribute's comment: “(1) ⇒ (2) at τ = étale, for a presheaf of modules”.

> A presheaf of `𝒪_affine`-modules on the small affine étale site of `S` all of whose base-change
> maps `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms is a sheaf, and the resulting sheaf of modules
> is quasi-coherent on the ringed site `(S_{affine, étale}, 𝒪_affine)`.

```lean
theorem smallAffineEtale_isSheaf_and_isQuasicoherentOnSite_of_baseChange_isIso
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : PresheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineEtaleRingedSite B S hS).O).obj)
    (h : ∀ ⦃X Y : (SmallAffineEtale B S hS)ᵒᵖ⦄ (f : X ⟶ Y),
      IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u, u} F f)) :
    ∃ hs : Presheaf.IsSheaf (smallAffineEtaleRingedSite B S hS).J F.presheaf,
      (⟨F, hs⟩ : SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallAffineEtaleRingedSite B S hS).O)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.smallAffineZariski_canonicalMap_isIso_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L146). The attribute's comment: “(2) ⇒ (1) at τ = Zariski”.

> If a sheaf of modules on the small affine Zariski site of `S` is quasi-coherent on the ringed
> site `(S_{affine, Zar}, 𝒪_affine)`, then its base-change map `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` along
> every morphism is an isomorphism.

```lean
theorem smallAffineZariski_canonicalMap_isIso_of_isQuasicoherentOnSite
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineZariskiRingedSite B S hS).O))
    (hF : F.IsQuasicoherentOnSite)
    {U V : SmallAffineZariski B S hS} (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineZariskiRingedSite B S hS) F f)
```

**`AlgebraicGeometry.smallAffineEtale_canonicalMap_isIso_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L165). The attribute's comment: “(2) ⇒ (1) at τ = étale”.

> If a sheaf of modules on the small affine étale site of `S` is quasi-coherent on the ringed
> site `(S_{affine, étale}, 𝒪_affine)`, then its base-change map `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` along
> every morphism is an isomorphism.

```lean
theorem smallAffineEtale_canonicalMap_isIso_of_isQuasicoherentOnSite
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineEtaleRingedSite B S hS).O))
    (hF : F.IsQuasicoherentOnSite)
    {U V : SmallAffineEtale B S hS} (f : U ⟶ V) :
    IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineEtaleRingedSite B S hS) F f)
```

**`AlgebraicGeometry.smallAffineZariski_isQuasicoherentOnSite_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L186). The attribute's comment: “(1) ⇔ (2) at τ = Zariski, for a sheaf of modules”.

> A sheaf of modules on the small affine Zariski site of `S` is quasi-coherent on the ringed site
> `(S_{affine, Zar}, 𝒪_affine)` exactly when all of its base-change maps
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms.

```lean
theorem smallAffineZariski_isQuasicoherentOnSite_iff_canonicalMap_isIso
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineZariskiRingedSite B S hS).O)) :
    F.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : SmallAffineZariski B S hS⦄ (f : U ⟶ V),
        IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineZariskiRingedSite B S hS) F f)
```

**`AlgebraicGeometry.smallAffineEtale_isQuasicoherentOnSite_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesSheaf.lean#L201). The attribute's comment: “(1) ⇔ (2) at τ = étale, for a sheaf of modules”.

> A sheaf of modules on the small affine étale site of `S` is quasi-coherent on the ringed site
> `(S_{affine, étale}, 𝒪_affine)` exactly when all of its base-change maps
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms.

```lean
theorem smallAffineEtale_isQuasicoherentOnSite_iff_canonicalMap_isIso
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineEtaleRingedSite B S hS).O)) :
    F.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : SmallAffineEtale B S hS⦄ (f : U ⟶ V),
        IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineEtaleRingedSite B S hS) F f)
```

**`AlgebraicGeometry.fullyFaithfulSmallAffineEtaleAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesUnique.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesUnique.lean#L114). The attribute's comment: “(4) at τ = étale, uniqueness of 𝒢”.

> **Stacks 0GZX, the uniqueness of `𝒢` in condition (4) at `τ = étale`.**  The functor
> `𝒢 ↦ 𝒢ᵃ|_{S_{affine, étale}}` from the quasi-coherent `𝒪_S`-modules to the `𝒪_affine`-modules on
> `S_{affine, étale}` is fully faithful: it is Stacks 0GN7 at `τ = étale` followed by the
> Comparison Lemma for sheaves of modules on the dense subsite of affine objects.

```lean
public noncomputable def fullyFaithfulSmallAffineEtaleAssociatedModuleQcoh :
    (smallAffineEtaleAssociatedModuleQcoh B S hS).FullyFaithful
```

**`AlgebraicGeometry.smallAffineEtale_iso_of_associatedModuleQcoh_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesUnique.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesUnique.lean#L123). The attribute's comment: “(4) at τ = étale, uniqueness of 𝒢”.

> **Stacks 0GZX, the uniqueness of `𝒢` in condition (4) at `τ = étale`**, read as a
> uniqueness statement: two quasi-coherent `𝒪_S`-modules whose associated modules have isomorphic
> restrictions to the small affine étale site of `S` are isomorphic.

```lean
public theorem smallAffineEtale_iso_of_associatedModuleQcoh_restriction_iso
    (G₁ G₂ : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory)
    (e : (smallAffineEtaleAssociatedModuleQcoh B S hS).obj G₁ ≅
      (smallAffineEtaleAssociatedModuleQcoh B S hS).obj G₂) :
    Nonempty (G₁.obj ≅ G₂.obj)
```

**`AlgebraicGeometry.smallAffineZariski_exists_isQuasicoherentOnSite_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean#L239). The attribute's comment: “(2) ⇒ (3) at τ = Zariski”.

> A sheaf of modules on the small affine Zariski site of `S` which is quasi-coherent on the
> ringed site `(S_{affine, Zar}, 𝒪_affine)` is the restriction of a quasi-coherent `𝒪`-module on
> `(S_Zar, 𝒪)`, i.e. corresponds to one under the equivalence of ringed topoi (0GZW).

```lean
public theorem smallAffineZariski_exists_isQuasicoherentOnSite_restriction_iso
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineZariskiRingedSite B S hS).O))
    (hF : F.IsQuasicoherentOnSite) :
    ∃ N : SheafOfModules.{u} (SmallZariski.structureSheaf B S hS), N.IsQuasicoherentOnSite ∧
      Nonempty ((smallAffineZariskiModuleRestriction B S hS).obj N ≅ F)
```

**`AlgebraicGeometry.smallAffineZariski_essImage_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean#L261). The attribute's comment: “(4) at τ = Zariski, existence of 𝒢”.

> A sheaf of modules `𝓕` on the small affine Zariski site of `S` which is quasi-coherent on the
> ringed site `(S_{affine, Zar}, 𝒪_affine)` comes from a quasi-coherent `𝒪_S`-module `𝒢` by the
> procedure of Descent, Section 35.8: it is in the essential image of
> `𝒢 ↦ 𝒢ᵃ|_{S_{affine, Zar}}`.

```lean
public theorem smallAffineZariski_essImage_associatedModuleQcoh
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineZariskiRingedSite B S hS).O))
    (hF : F.IsQuasicoherentOnSite) :
    (smallAffineZariskiAssociatedModuleQcoh B S hS).essImage F
```

**`AlgebraicGeometry.smallAffineZariski_exists_associatedModuleQcoh_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean#L279). The attribute's comment: “(1) ⇒ (4) at τ = Zariski, existence of 𝒢”.

> A sheaf of modules `𝓕` on the small affine Zariski site of `S` all of whose base-change maps
> `𝓕(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝓕(U)` are isomorphisms is isomorphic to `𝒢ᵃ|_{S_{affine, Zar}}` for a
> quasi-coherent `𝒪_S`-module `𝒢`.

```lean
public theorem smallAffineZariski_exists_associatedModuleQcoh_restriction_iso
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallAffineZariskiRingedSite B S hS).O))
    (hF : ∀ ⦃U V : SmallAffineZariski B S hS⦄ (f : U ⟶ V),
      IsIso (Stacks.SheafOfModules.canonicalMap (smallAffineZariskiRingedSite B S hS) F f)) :
    ∃ G : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory,
      Nonempty ((smallAffineZariskiAssociatedModuleQcoh B S hS).obj G ≅ F)
```

**`AlgebraicGeometry.isEquivalence_smallAffineZariskiModuleRestrictionQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean#L323). The attribute's comment: “(2) ⇔ (3) at τ = Zariski”.

> The equivalence of ringed topoi (0GZW) induces an equivalence
> `QCoh(S_Zar, 𝒪) ≌ QCoh(S_{affine, Zar}, 𝒪_affine)` between the categories of quasi-coherent
> modules.

```lean
public theorem isEquivalence_smallAffineZariskiModuleRestrictionQcoh :
    (smallAffineZariskiModuleRestrictionQcoh B S hS).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_smallAffineZariskiAssociatedModuleQcohOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean#L364). The attribute's comment: “(2) ⇔ (4) at τ = Zariski”.

> The functor `𝒢 ↦ 𝒢ᵃ|_{S_{affine, Zar}}` is an equivalence from the quasi-coherent
> `𝒪_S`-modules onto the quasi-coherent modules on the ringed site `(S_{affine, Zar}, 𝒪_affine)`:
> every such module comes from a `𝒢`, and from a unique one.

```lean
public theorem isEquivalence_smallAffineZariskiAssociatedModuleQcohOnSite :
    (smallAffineZariskiAssociatedModuleQcohOnSite B S hS).IsEquivalence
```

**`AlgebraicGeometry.smallAffineZariskiAssociatedModuleQcohEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiExists.lean#L375). The attribute's comment: “(2) ⇔ (4) at τ = Zariski”.

> The equivalence of categories `QCoh(𝒪_S) ≌ QCoh(S_{affine, Zar}, 𝒪_affine)` whose functor
> is `𝒢 ↦ 𝒢ᵃ|_{S_{affine, Zar}}`.

```lean
public noncomputable def smallAffineZariskiAssociatedModuleQcohEquivalence :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallAffineZariskiRingedSite B S hS).O)).FullSubcategory
```

**`AlgebraicGeometry.fullyFaithfulSmallAffineZariskiAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiUnique.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiUnique.lean#L83). The attribute's comment: “(4) at τ = Zariski, uniqueness of 𝒢”.

> The functor `𝒢 ↦ 𝒢ᵃ|_{S_{affine, Zar}}` from the quasi-coherent `𝒪_S`-modules to the
> `𝒪_affine`-modules on `S_{affine, Zar}` is fully faithful.

```lean
public noncomputable def fullyFaithfulSmallAffineZariskiAssociatedModuleQcoh :
    (smallAffineZariskiAssociatedModuleQcoh B S hS).FullyFaithful
```

**`AlgebraicGeometry.smallAffineZariski_iso_of_associatedModuleQcoh_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiUnique.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentModulesAndAffinesZariskiUnique.lean#L91). The attribute's comment: “(4) at τ = Zariski, uniqueness of 𝒢”.

> Two quasi-coherent `𝒪_S`-modules whose associated modules have isomorphic restrictions to the
> small affine Zariski site of `S` are isomorphic.

```lean
public theorem smallAffineZariski_iso_of_associatedModuleQcoh_restriction_iso
    (G₁ G₂ : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory)
    (e : (smallAffineZariskiAssociatedModuleQcoh B S hS).obj G₁ ≅
      (smallAffineZariskiAssociatedModuleQcoh B S hS).obj G₂) :
    Nonempty (G₁.obj ≅ G₂.obj)
```

**`AlgebraicGeometry.smallAffineZariski_isIso_restrictionBaseChange_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineSiteAssociatedModuleCartesian.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineSiteAssociatedModuleCartesian.lean#L104). The attribute's comment: “(4) ⇒ (1) at τ = Zariski”.

> **Stacks 0GZX, condition (4) implies condition (1) at `τ = Zariski`.** The presheaf `𝒢ᵃ` of
> Descent, Section 35.8 attached to a quasi-coherent `𝒪_S`-module `𝒢` has all its base-change
> comparisons `𝒢ᵃ(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝒢ᵃ(U)` isomorphisms on the small affine Zariski site
> of `S`.

```lean
public theorem smallAffineZariski_isIso_restrictionBaseChange_associatedModule
    (B : BigZariskiSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : S.Modules) [G.IsQuasicoherent] {X Y : (SmallAffineZariski B S hS)ᵒᵖ} (f : X ⟶ Y) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange
      (R := (smallAffineZariskiRingedSite B S hS).O.obj)
      (associatedModulePresheaf S G (smallAffineZariskiToOver B S hS)) f)
```

**`AlgebraicGeometry.smallAffineEtale_isIso_restrictionBaseChange_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmallAffineSiteAssociatedModuleCartesian.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SmallAffineSiteAssociatedModuleCartesian.lean#L135). The attribute's comment: “(4) ⇒ (1) at τ = étale”.

> **Stacks 0GZX, condition (4) implies condition (1) at `τ = étale`.** The presheaf `𝒢ᵃ` of
> Descent, Section 35.8 attached to a quasi-coherent `𝒪_S`-module `𝒢` has all its base-change
> comparisons `𝒢ᵃ(U') ⊗_{𝒪(U')} 𝒪(U) ⟶ 𝒢ᵃ(U)` isomorphisms on the small affine étale site
> of `S`.

```lean
public theorem smallAffineEtale_isIso_restrictionBaseChange_associatedModule
    (B : BigEtaleSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : S.Modules) [G.IsQuasicoherent] {X Y : (SmallAffineEtale B S hS)ᵒᵖ} (f : X ⟶ Y) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange
      (R := (smallAffineEtaleRingedSite B S hS).O.obj)
      (associatedModulePresheaf S G (smallAffineEtaleToOver B S hS)) f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.11, Tag 0GZT](https://stacks.math.columbia.edu/tag/0GZT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
