---
declaration: section
origin: cited
lean: AlgebraicGeometry.FibredSite.quasicoherentModules, AlgebraicGeometry.Stack.isQuasicoherentOnSite_modulePullback, AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_iff_forall_objectInverseImage, AlgebraicGeometry.FibredSite.tfae_isQuasicoherentClause'
statement: formalized
proof: formalized
---

# 96.11 Quasi-coherent modules

Section 96.11 of the Stacks Project, [Tag 06WF](https://stacks.math.columbia.edu/tag/06WF). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06WG, a definition

[Tag 06WG](https://stacks.math.columbia.edu/tag/06WG) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.quasicoherentModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Modules.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Modules.lean#L53).

> The category of quasi-coherent modules on the fppf ringed site of a category fibred in
> groupoids over the schemes over `S`.

```lean
public abbrev quasicoherentModules
```

## Tag 06WH, a lemma

[Tag 06WH](https://stacks.math.columbia.edu/tag/06WH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasicoherentOnSite_modulePullback`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ModulePullback.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ModulePullback.lean#L215).

> **Stacks 06WH.** The inverse image of sheaves of modules along a 1-morphism of categories
> fibred in groupoids over the big fppf category of `S` preserves quasi-coherence.
>
> The inverse image is `AlgebraicGeometry.Stack.modulePullback`, which on underlying presheaves of
> modules is restriction along the 1-morphism followed by the change of scalars identifying the
> two structure presheaves; and the slices of a 1-morphism of categories fibred in groupoids are
> equivalences by Stacks 06W0.

```lean
instance isQuasicoherentOnSite_modulePullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : Type v} [Category.{w} 𝒳] [Category.{w} 𝒴]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (q : 𝒴 ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (f : 𝒳 ⥤ 𝒴) (hf : f ⋙ q = p)
    (M : SheafOfModules.{max u v w m}
      (ringStructureSheafCore B S hS q hq B.topology le_rfl))
    [M.IsQuasicoherentOnSite] :
    ((modulePullback.{u, v, w, max u v w m} B S hS p q hp hq f hf
      B.topology le_rfl).obj M).IsQuasicoherentOnSite
```

## Tag 06WI, a lemma

[Tag 06WI](https://stacks.math.columbia.edu/tag/06WI) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_iff_forall_objectInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/FibredSiteLocalization.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/FibredSiteLocalization.lean#L373).

> **Stacks 06WI.**  A sheaf of modules on the associated fppf site of a category fibred in
> groupoids is quasi-coherent if and only if its inverse image `x^*𝓕` is a quasi-coherent sheaf on
> the big fppf site `(Sch/U)_fppf` of the scheme `U = p(x)`, for every object `x` of `𝒳`.
>
> Necessity is stability of quasi-coherence under restriction to a slice site, transported along
> the equivalence of ringed sites `𝒳_fppf/x ≌ (Sch/U)_fppf`.  Sufficiency is Stacks 03DN for the
> family of all objects of `𝒳`, which covers the final object: quasi-coherence is a local and
> intrinsic property, so no further input is needed.

```lean
public theorem isQuasicoherentOnSite_iff_forall_objectInverseImage
    (M : SheafOfModules.{u} (ringStructureSheafCore B S hS p hp .fppf)) :
    M.IsQuasicoherentOnSite ↔
      ∀ x : 𝒳, (objectInverseImage B S hS p hp x M).IsQuasicoherentOnSite
```

## Tag 0EM8, a lemma

[Tag 0EM8](https://stacks.math.columbia.edu/tag/0EM8) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.tfae_isQuasicoherentClause'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SiteEquivalenceAffine.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SiteEquivalenceAffine.lean#L282). The attribute's comment: “the three-way equivalence of the conditions at the Zariski, étale and fppf topologies (a sheaf for the inherited topology and quasi-coherent on that ringed site), for any category fibred in groupoids over (Sch/S)\_fppf and any presheaf of modules on it; the inputs are proved by isSheafFppfOfQuasicoherentOnSite\_siteKind and quasicoherentOnSiteOfLeFppf\_siteKind”.

> **Stacks 0EM8.**  For a category `𝒳` fibred in groupoids over the big fppf category of
> schemes over `S` and a presheaf of modules `𝓕` on `𝒳`, the three conditions
>
> 1. `𝓕` is an object of `Mod(𝒳_Zar, 𝒪_𝒳)` and is quasi-coherent on `(𝒳_Zar, 𝒪_𝒳)`,
> 2. `𝓕` is an object of `Mod(𝒳_ét, 𝒪_𝒳)` and is quasi-coherent on `(𝒳_ét, 𝒪_𝒳)`,
> 3. `𝓕` is a quasi-coherent module on `𝒳` in the sense of Stacks 06WG, that is on
>    `(𝒳_fppf, 𝒪_𝒳)`,
>
> are equivalent.
>
> This is `AlgebraicGeometry.FibredSite.tfae_isQuasicoherentClause` with its four hypotheses
> discharged by `AlgebraicGeometry.FibredSite.isSheafFppfOfQuasicoherentOnSite_zariski`,
> `AlgebraicGeometry.FibredSite.isSheafFppfOfQuasicoherentOnSite_etale`,
> `AlgebraicGeometry.FibredSite.quasicoherentOnSiteOfLeFppf_zariski` and
> `AlgebraicGeometry.FibredSite.quasicoherentOnSiteOfLeFppf_etale`.

```lean
public theorem tfae_isQuasicoherentClause'
    (𝓕 : PresheafOfModules.{u} (structureRingPresheaf B S hS p hp)) :
    [IsQuasicoherentClause B S hS p hp .zariski 𝓕,
      IsQuasicoherentClause B S hS p hp .etale 𝓕,
      IsQuasicoherentClause B S hS p hp .fppf 𝓕].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.11, Tag 06WF](https://stacks.math.columbia.edu/tag/06WF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
