---
declaration: section
origin: cited
lean: AlgebraicGeometry.FibredSite.quasicoherentModules, AlgebraicGeometry.Stack.isQuasicoherentOnSite_modulePullback, AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_iff_forall_objectInverseImage, AlgebraicGeometry.FibredSite.tfae_isQuasicoherentClause, AlgebraicGeometry.FibredSite.tfae_isQuasicoherentClause'
statement: formalized
proof: formalized
---

# 96.11 Quasi-coherent modules

Section 96.11 of the Stacks Project, [Tag 06WF](https://stacks.math.columbia.edu/tag/06WF). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06WG, a definition

[Tag 06WG](https://stacks.math.columbia.edu/tag/06WG) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.quasicoherentModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Modules.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Modules.lean#L53).

> The category of quasi-coherent modules on the fppf ringed site of a category fibred in
> groupoids over the schemes over `S`.

```lean
public abbrev quasicoherentModules
```

## Tag 06WH, a lemma

[Tag 06WH](https://stacks.math.columbia.edu/tag/06WH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasicoherentOnSite_modulePullback`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ModulePullback.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ModulePullback.lean#L215).

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

**`AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_iff_forall_objectInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/FibredSiteLocalization.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/FibredSiteLocalization.lean#L373).

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

**`AlgebraicGeometry.FibredSite.tfae_isQuasicoherentClause`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SiteEquivalence.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SiteEquivalence.lean#L282). The attribute's comment: “the three-way equivalence, with the two inputs at each of the Zariski and the étale topology carried as explicit hypotheses: `h₁z`/`h₁e`, a `τ`-sheaf of modules that is quasi-coherent on `(𝒳_τ, 𝒪_𝒳)` is a sheaf for the inherited fppf topology, and `h₂z`/`h₂e`, quasi-coherence passes from the inherited fppf topology to a coarser one. At `τ = .fppf` both are discharged here. Neither is discharged at `τ = .zariski` or `τ = .etale`: both funnel into the essential-surjectivity half of Descent, Proposition 03DX, which this repository does not prove and carries as the hypothesis `AlgebraicGeometry.BigFppfOver.QuasicoherentIsEssImageAssociatedModule`, its only open reduction being `AlgebraicGeometry.BigFppfOver.AssociatedModuleGlueDescentDatum`; the two existing 03DX declarations state the different criterion that quasi-coherence on the small étale site of an algebraic space is equivalent to being cartesian on affine charts”.

> **The three-way equivalence of Stacks 0EM8**, over its two inputs at the Zariski and the
> étale topology: for a presheaf of modules on a category fibred in groupoids over the big fppf
> category of schemes over `S`, being a quasi-coherent Zariski module, being a quasi-coherent
> étale module, and being a quasi-coherent module on `𝒳` in the sense of Stacks 06WG are
> equivalent.

```lean
public theorem tfae_isQuasicoherentClause
    (h₁z : IsSheafFppfOfQuasicoherentOnSite B S hS p hp .zariski)
    (h₁e : IsSheafFppfOfQuasicoherentOnSite B S hS p hp .etale)
    (h₂z : QuasicoherentOnSiteOfLeFppf B S hS p hp .zariski)
    (h₂e : QuasicoherentOnSiteOfLeFppf B S hS p hp .etale)
    (𝓕 : PresheafOfModules.{u} (structureRingPresheaf B S hS p hp)) :
    [IsQuasicoherentClause B S hS p hp .zariski 𝓕,
      IsQuasicoherentClause B S hS p hp .etale 𝓕,
      IsQuasicoherentClause B S hS p hp .fppf 𝓕].TFAE
```

**`AlgebraicGeometry.FibredSite.tfae_isQuasicoherentClause'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SiteEquivalenceAffine.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SiteEquivalenceAffine.lean#L280). The attribute's comment: “the three-way equivalence, for a category fibred in groupoids over the big fppf category of schemes over S and a presheaf of modules on it”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
