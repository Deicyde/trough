---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AffineCategory.tfae_isQuasicoherent, AlgebraicGeometry.Stack.tfae_locallyQuasicoherent_affine
statement: formalized
proof: formalized
---

# 96.25 Quasi-coherent modules and affines

Section 96.25 of the Stacks Project, [Tag 0H0D](https://stacks.math.columbia.edu/tag/0H0D). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H0E, a lemma

[Tag 0H0E](https://stacks.math.columbia.edu/tag/0H0E) in the Stacks Project.

**`AlgebraicGeometry.Stack.AffineCategory.tfae_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentModulesAndAffines.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasiCoherentModulesAndAffines.lean#L210).

> **Stacks 0H0E.** Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category fibred in groupoids and let `𝓕`
> be an `𝒪`-module on `𝒳_{affine}`, that is, a sheaf of modules on the chaotic ringed site
> `(𝒳_{affine}, 𝒪)` of Stacks 0H09 and 0H0D. The following are equivalent:
>
> 1. for every morphism `x ⟶ x'` of `𝒳_{affine}` the map
>    `𝓕(x') ⊗_{𝒪(x')} 𝒪(x) ⟶ 𝓕(x)` is an isomorphism;
> 2. `𝓕` is a quasi-coherent module on `(𝒳_{affine}, 𝒪)` in the sense of Stacks 03DL;
> 3. `𝓕` is a sheaf for the Zariski topology on `𝒳_{affine}` and a quasi-coherent module on
>    `(𝒳_{affine, Zar}, 𝒪)`;
> 4. the same for the étale topology;
> 5. the same for the smooth topology;
> 6. the same for the syntomic topology;
> 7. the same for the fppf topology;
> 8. `𝓕` corresponds to a quasi-coherent module on `𝒳` via the equivalence of Stacks 0H0C: it is a
>    sheaf for the fppf topology, and as such it is isomorphic to the restriction to
>    `𝒳_{affine, fppf}` of a quasi-coherent module on `(𝒳_{fppf}, 𝒪_𝒳)`.
>
> The equivalence of Stacks 0H0C is restriction along the affine inclusion, which on sheaves of
> modules with sections in the universe of the schemes is an equivalence by
> `AlgebraicGeometry.Stack.AffineCategory.isEquivalence_moduleRestriction`; condition (8) asks
> that `𝓕` lie in its image of the quasi-coherent modules.

```lean
theorem tfae_isQuasicoherent (hp : p.IsFiberedInGroupoids)
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (siteKindRingedSite B S hS p hp .fppf).chaotic.O)) :
    [∀ ⦃x x' : AffineCategory B S hS p⦄ (f : x ⟶ x'),
        IsIso (Stacks.SheafOfModules.canonicalMap
          (siteKindRingedSite B S hS p hp .fppf).chaotic F f),
      F.IsQuasicoherentOnSite,
      ∃ h : Presheaf.IsSheaf (siteKindRingedSite B S hS p hp .zariski).J F.val.presheaf,
        (⟨F.val, h⟩ : SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (siteKindRingedSite B S hS p hp .zariski).O)).IsQuasicoherentOnSite,
      ∃ h : Presheaf.IsSheaf (siteKindRingedSite B S hS p hp .etale).J F.val.presheaf,
        (⟨F.val, h⟩ : SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (siteKindRingedSite B S hS p hp .etale).O)).IsQuasicoherentOnSite,
      ∃ h : Presheaf.IsSheaf (siteKindRingedSite B S hS p hp .smooth).J F.val.presheaf,
        (⟨F.val, h⟩ : SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (siteKindRingedSite B S hS p hp .smooth).O)).IsQuasicoherentOnSite,
      ∃ h : Presheaf.IsSheaf (siteKindRingedSite B S hS p hp .syntomic).J F.val.presheaf,
        (⟨F.val, h⟩ : SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (siteKindRingedSite B S hS p hp .syntomic).O)).IsQuasicoherentOnSite,
      ∃ h : Presheaf.IsSheaf (siteKindRingedSite B S hS p hp .fppf).J F.val.presheaf,
        (⟨F.val, h⟩ : SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (siteKindRingedSite B S hS p hp .fppf).O)).IsQuasicoherentOnSite,
      ∃ h : Presheaf.IsSheaf (siteKindRingedSite B S hS p hp .fppf).J F.val.presheaf,
        letI := isDenseSubsite_inclusion_siteKind B S hS p hp .fppf
        ∃ G : SheafOfModules.{u} (FibredSite.ringStructureSheafCore B S hS p hp .fppf),
          G.IsQuasicoherentOnSite ∧
            Nonempty ((Stacks.DenseSubsiteModules.moduleRestriction
              (siteKindRingedSite B S hS p hp .fppf).J
              (BigFppfOver.associatedTopology B S hS p .fppf) (inclusion B S hS p)
              (FibredSite.ringStructureSheafCore B S hS p hp .fppf)).obj G ≅
              (⟨F.val, h⟩ : SheafOfModules.{u}
                (Stacks.SheafOfModules.Tensor.ringSheaf
                  (siteKindRingedSite B S hS p hp .fppf).O)))].TFAE
```

## Tag 0H0F, a lemma

[Tag 0H0F](https://stacks.math.columbia.edu/tag/0H0F) in the Stacks Project.

**`AlgebraicGeometry.Stack.tfae_locallyQuasicoherent_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LocallyQuasiCoherentModulesAndAffines.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/LocallyQuasiCoherentModulesAndAffines.lean#L314).

> Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category fibred in groupoids and `𝓕` a module over the
> structure sheaf `𝒪` of the affine subcategory `𝒳_{affine}`. The following are equivalent:
>
> 1. for every arrow `x ⟶ x'` of `𝒳_{affine}` lying over an étale morphism of affine schemes, the
>    map `𝓕(x') ⊗_{𝒪(x')} 𝒪(x) ⟶ 𝓕(x)` is an isomorphism;
> 2. `𝓕` is a sheaf for the étale topology on `𝒳_{affine}` and, for every object `x` of
>    `𝒳_{affine}`, the restriction `x^*𝓕|_{U_{affine, étale}}` to the small affine étale site of
>    `U = p(x)` is quasi-coherent;
> 3. `𝓕` corresponds to a locally quasi-coherent module on `𝒳` via the equivalence of Stacks 0H0C
>    for the étale topology: it is isomorphic to the restriction to `𝒳_{affine}` of a locally
>    quasi-coherent module `𝓖` on `𝒳`.

```lean
theorem tfae_locallyQuasicoherent_affine
    (F : PresheafOfModules.{u} (affineStructurePresheaf B S hS p)) :
    List.TFAE [
      ∀ ⦃x x' : AffineCategory B S hS p⦄ (f : x ⟶ x'),
        Etale ((p ⋙ BigFppfOver.toScheme B S hS).map f.hom) →
          IsIso (restrictionBaseChange.{v, w, u, u}
            (R := affineStructureCommPresheaf B S hS p) F f.op),
      Presheaf.IsSheaf
          (associatedAffineTopology B S hS p (BigAffineEtale.topology B.toBigEtaleSite S hS))
          F.presheaf ∧
        ∀ x : AffineCategory B S hS p,
          ∃ hM : Presheaf.IsSheaf
              (SmallAffineEtale.topology E (p.obj x.obj).left.1 (contains_base B E h S hS p x.obj))
              (affineChartModule B E h S hS p hp x F).presheaf,
            (⟨affineChartModule B E h S hS p hp x F, hM⟩ : SheafOfModules.{u}
              (Stacks.SheafOfModules.Tensor.ringSheaf
                (smallAffineEtaleRingedSite E (p.obj x.obj).left.1
                  (contains_base B E h S hS p x.obj)).O)).IsQuasicoherentOnSite,
      ∃ G : PresheafOfModules.{u}
          (ringStructureSheafCore B S hS p hp (etaleTopology B) (etaleTopology_le_topology B)).obj,
        IsLocallyQuasicoherent B E h S hS p hp G ∧
          Nonempty ((PresheafOfModules.pushforward₀ (AffineCategory.inclusion B S hS p) _).obj G ≅
            F)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.25, Tag 0H0D](https://stacks.math.columbia.edu/tag/0H0D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
