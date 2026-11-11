---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.preservesFiniteLimits_etaleRestrictedModuleInverseImageFunctor, AlgebraicGeometry.Space.exactFunctor_etaleRestrictedModuleInverseImageFunctor, AlgebraicGeometry.Stack.FlatFppf.spaceChartRestrictionCoheratorInternalHomIso
statement: formalized
proof: formalized
---

# 103.12 Further remarks on quasi-coherent modules

Section 103.12 of the Stacks Project, [Tag 0GQS](https://stacks.math.columbia.edu/tag/0GQS). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GQS, the section

[Tag 0GQS](https://stacks.math.columbia.edu/tag/0GQS) in the Stacks Project.

**`AlgebraicGeometry.Space.preservesFiniteLimits_etaleRestrictedModuleInverseImageFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceExactness.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceExactness.lean#L166). The attribute's comment: “part (1), the left exact half: a preserves finite limits”.

> **Stacks 0GQS, part (1), the left exact half.** The functor
> `a : ℱ ↦ f^*ℱ|_{U_étale}` preserves finite limits.
>
> Limits of sheaves of modules are computed in presheaves, where restriction along a functor is
> pointwise, so this holds for the direct image along any continuous functor of ringed sites.

```lean
theorem preservesFiniteLimits_etaleRestrictedModuleInverseImageFunctor
    (hp : p.IsFiberedInGroupoids) (hr : r.IsFiberedInGroupoids)
    (eU : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (U.1 ⋙ typeToCat)).p)
    (f : 𝒰 ⥤ 𝒳) (hf : p.IsFibredOneMorphism r f) :
    PreservesFiniteLimits (etaleRestrictedModuleInverseImageFunctor B S hS p r hp hr eU f hf)
```

**`AlgebraicGeometry.Space.exactFunctor_etaleRestrictedModuleInverseImageFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceExactness.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceExactness.lean#L185). The attribute's comment: “part (1): the functor a from all modules on the étale site of the stack to all modules on the small étale site of the algebraic space is exact”.

> **Stacks 0GQS, part (1).** The functor `a : Mod(𝒳_étale, 𝒪_𝒳) ⥤ Mod(U_étale, 𝒪_U)`,
> `ℱ ↦ f^*ℱ|_{U_étale}`, is exact.
>
> The source's two reasons are the continuity and the cocontinuity of the functor `U_étale ⥤ 𝒳`
> along which the restriction is taken: `f^{-1}` is restriction along the 1-morphism `f` and
> `·|_{U_étale}` is restriction along `u_U`, and both functors are continuous and cocontinuous, so
> Stacks 04BD (2) applies to their composite.

```lean
theorem exactFunctor_etaleRestrictedModuleInverseImageFunctor [EssentiallySmall.{u} 𝒳]
    (hp : p.IsFiberedInGroupoids) (hr : r.IsFiberedInGroupoids)
    (eU : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (U.1 ⋙ typeToCat)).p)
    (f : 𝒰 ⥤ 𝒳) (hf : p.IsFibredOneMorphism r f) :
    exactFunctor (inheritedEtaleModules B S hS r hr)
      (SheafOfModules.{u} (structureRingSheaf B S hS U))
      (etaleRestrictedModuleInverseImageFunctor B S hS p r hp hr eU f hf)
```

## Tag 0GQT, an item

[Tag 0GQT](https://stacks.math.columbia.edu/tag/0GQT) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.spaceChartRestrictionCoheratorInternalHomIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorInternalHomRestriction.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorInternalHomRestriction.lean#L105).

> **Stacks 0GQT.** Let `f : 𝒰 ⟶ 𝒳` be a flat 1-morphism of algebraic stacks with `𝒰` the
> algebraic stack of an algebraic space `U`, and let `d : ℱ ↦ f^*ℱ|_{U_étale}` be the restriction of
> Stacks 0GQS. For `𝒪_𝒳`-modules `ℱ` and `𝒢` with `ℱ` quasi-coherent,
> `d(hom(ℱ, 𝒢)) = 𝓗om_{𝒪_U}(d(ℱ), d(𝒢))`, where `hom(ℱ, 𝒢) = Q(𝓗om_{𝒪_𝒳}(ℱ, 𝒢))` is the
> object of Stacks 0GQN.

```lean
def spaceChartRestrictionCoheratorInternalHomIso (hf : AlgebraicStacks.IsFlat B S hS f)
    (F G : _root_.SheafOfModules.{u} (ambientRingStructureSheaf B S hS 𝒳))
    (hF : F.IsQuasicoherentOnSite) :
    spaceChartRestriction B S hS 𝒳 U hU f (coheratorInternalHom B S hS 𝒳 F G) ≅
      Space.smallEtaleInternalHomSmall B S hS U hU (spaceChartRestriction B S hS 𝒳 U hU f F)
        (spaceChartRestriction B S hS 𝒳 U hU f G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.12, Tag 0GQS](https://stacks.math.columbia.edu/tag/0GQS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
