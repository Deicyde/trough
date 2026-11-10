---
declaration: section
origin: cited
lean: Stacks.Algebraization.isCompletion_iff_isCompletion_of_isKernelCokernelAnnihilatedByPower, Stacks.Algebraization.extendsToX_iff_extendsToX_of_isKernelCokernelAnnihilatedByPower, Stacks.Algebraization.epi_canonicalComparison_of_mittagLeffler, Stacks.Algebraization.limitQuotientSheaves_isCoherentAdicSystem, Stacks.Algebraization.comparison_hom_app_limitSection, Stacks.Algebraization.mono_comparison
statement: formalized
proof: formalized
---

# 52.17 Algebraization of coherent formal modules, II

Section 52.17 of the Stacks Project, [Tag 0EIT](https://stacks.math.columbia.edu/tag/0EIT). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EIU, a lemma

[Tag 0EIU](https://stacks.math.columbia.edu/tag/0EIU) in the Stacks Project.

**`Stacks.Algebraization.isCompletion_iff_isCompletion_of_isKernelCokernelAnnihilatedByPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/AnnihilatedComparison.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/AnnihilatedComparison.lean#L274). The attribute's comment: “part (2): membership in the essential image of the completion functor”.

> **Stacks 0EIU part (2).** In Situation 0EHC, let `α : (F_n) ⟶ (F'_n)` be a morphism of
> `Coh(U, I𝒪_U)` whose levelwise kernels and cokernels are annihilated by a power of `I𝒪_U`. Then
> `(F_n)` is the completion of a coherent `𝒪_U`-module if and only if `(F'_n)` is.
>
> This is `Stacks.Algebraization.essImage_iff_essImage_of_isKernelCokernelAnnihilatedByPower` on the
> open subscheme `U`, which is Noetherian because `X` is.

```lean
public theorem isCompletion_iff_isCompletion_of_isKernelCokernelAnnihilatedByPower
    (S : AlgebraizationSituation.{u})
    {F G : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι)} (α : F ⟶ G)
    (hα : IsKernelCokernelAnnihilatedByPower (S.Yι.ker.comap S.U.ι) α.hom) :
    (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage F ↔
      (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage G
```

**`Stacks.Algebraization.extendsToX_iff_extendsToX_of_isKernelCokernelAnnihilatedByPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/AnnihilatedComparison.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/AnnihilatedComparison.lean#L297). The attribute's comment: “part (1): extendability to the whole of X”.

> **Stacks 0EIU part (1).** In Situation 0EHC, let `α : (F_n) ⟶ (F'_n)` be a morphism of
> `Coh(U, I𝒪_U)` whose levelwise kernels and cokernels are annihilated by a power of `I𝒪_U`. Then
> `(F_n)` extends to `X` if and only if `(F'_n)` does.
>
> Stacks 0EIN, in the form `Stacks.Algebraization.extendsToX_iff_pullback_isCompletion`, replaces
> extendability to `X` by membership in the essential image of the completion functor on the
> preimage `U'` of `U` in the spectrum of the `I`-adic completion of the base. The pullback along
> that flat morphism carries `α` to a morphism of `Coh(U', I𝒪_{U'})` whose levelwise kernels and
> cokernels are still annihilated by a power of the ideal, by
> `Stacks.Coherent.isKernelCokernelAnnihilatedByPower_coherentAdicPullback_map`, so
> `Stacks.Algebraization.essImage_iff_essImage_of_isKernelCokernelAnnihilatedByPower` applies on
> `U'`. The flatness of the completion map is
> `AdicCompletion.flat_of_isNoetherian` read through `AlgebraicGeometry.Flat.SpecMap_iff`, in the
> form in which the restriction to the open `U` inherits it.

```lean
public theorem extendsToX_iff_extendsToX_of_isKernelCokernelAnnihilatedByPower
    (S : AlgebraizationSituation.{u})
    {F G : Stacks.Coherent.CoherentAdicSystems (S.Yι.ker.comap S.U.ι)} (α : F ⟶ G)
    (hα : IsKernelCokernelAnnihilatedByPower (S.Yι.ker.comap S.U.ι) α.hom) :
    ExtendsToX S F ↔ ExtendsToX S G
```

## Tag 0EHF, a lemma

[Tag 0EHF](https://stacks.math.columbia.edu/tag/0EHF) in the Stacks Project.

**`Stacks.Algebraization.epi_canonicalComparison_of_mittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/MittagLefflerCriterion.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/MittagLefflerCriterion.lean#L714).

> **Stacks Project, Tag 0EHF.** If the inverse system `H⁰(U, F_n)` is Mittag-Leffler, every
> canonical comparison map `(M / Iⁿ⁺¹M)^~|_U ⟶ F_n` is surjective.

```lean
public theorem epi_canonicalComparison_of_mittagLeffler
    (hML : IsMittagLefflerCategorical (globalSectionsSystem S F)) (n : ℕ) :
    Epi (canonicalComparison S F n).1
```

## Tag 0EHG, a lemma

[Tag 0EHG](https://stacks.math.columbia.edu/tag/0EHG) in the Stacks Project.

**`Stacks.Algebraization.limitQuotientSheaves_isCoherentAdicSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/LimitQuotientComparison.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/LimitQuotientComparison.lean#L261). The attribute's comment: “coherent inverse system”.

> **Stacks Project, Tag 0EHG (1).** If the limit topology on `M = limₙ H⁰(U, F_n)` agrees with
> its `I`-adic topology, then the restrictions `G_n|_U = (M/Iⁿ⁺¹M)^~|_U` form a coherent `I`-adic
> system on `U`. In particular every `G_n|_U` is a coherent `𝒪_U`-module.

```lean
public theorem limitQuotientSheaves_isCoherentAdicSystem (h : LimitTopologyAgrees S F) :
    Stacks.Coherent.IsCoherentAdicSystem (idealOnOpen S) (limitQuotientSheaves S F)
```

**`Stacks.Algebraization.comparison_hom_app_limitSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/LimitQuotientComparison.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/LimitQuotientComparison.lean#L336). The attribute's comment: “canonical comparison”.

> **Stacks Project, Tag 0EHG (the comparison is the canonical one).** On sections over `U`,
> the comparison sends the section of `G_n|_U` induced by an element `m` of the inverse limit
> `M = limₙ H⁰(U, F_n)` to the `n`-th projection of `m`.
>
> This pins the comparison down: it is the map induced by the limit projections, not an
> arbitrary morphism of inverse systems. `comparison_hom_app` records the same fact as the
> identification of each component with an adjunction transpose.

```lean
public theorem comparison_hom_app_limitSection (h : LimitTopologyAgrees S F) (n : ℕ)
    (m : limitGlobalSections S F) :
    (((comparison S F h).hom.app (op n)).app ⊤) (limitSection S F n m) =
      (limit.π (globalSectionsSystem S F) (op n)).hom m
```

**`Stacks.Algebraization.mono_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/LimitQuotientComparison.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/LimitQuotientComparison.lean#L386). The attribute's comment: “injective comparison”.

> **Stacks Project, Tag 0EHG (2).** The canonical comparison `(G_n|_U) ⟶ (F_n)` is a
> monomorphism in the abelian category `Coh(U, I 𝒪_U)`.
>
> It is *not* claimed to be an isomorphism: the comparison need not be surjective without a
> further hypothesis such as the Mittag-Leffler condition of Stacks 0EHF.

```lean
public theorem mono_comparison (h : LimitTopologyAgrees S F) : Mono (comparison S F h)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.17, Tag 0EIT](https://stacks.math.columbia.edu/tag/0EIT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
