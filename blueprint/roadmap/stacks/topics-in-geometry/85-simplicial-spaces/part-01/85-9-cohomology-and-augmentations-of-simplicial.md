---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.Augmentation.resolution, CategoryTheory.SimplicialSiteSituation.Augmentation.augmentedCechComplex_exactAt_zero, CategoryTheory.SimplicialSiteSituation.Augmentation.augmentedCechComplex_exactAt_one, CategoryTheory.SimplicialSiteSituation.Augmentation.augmentedCechComplex_exactAt_of_injective, CategoryTheory.SimplicialSiteSituation.Augmentation.higherDirectImageSpectralSequence
statement: formalized
proof: formalized
---

# 85.9 Cohomology and augmentations of simplicial sites

Section 85.9 of the Stacks Project, [Tag 0D9A](https://stacks.math.columbia.edu/tag/0D9A). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D78, a lemma

[Tag 0D78](https://stacks.math.columbia.edu/tag/0D78) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.Augmentation.resolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationResolutionTerms.lean, line 939](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationResolutionTerms.lean#L939).

> **Stacks 0D78.** The exact complex
> `… ⟶ g_{1!}(a_1⁻¹𝒢) ⟶ g_{0!}(a_0⁻¹𝒢) ⟶ a⁻¹𝒢 ⟶ 0`
> of abelian sheaves on the total site: the alternating-face complex of the simplex-coefficient
> resolution of `a⁻¹𝒢`, whose degree-`n` term is the extension by zero `g_{n!}(a_n⁻¹𝒢)`.

```lean
def resolution : Resolution S D K a G
```

## Tag 0D79, a lemma

[Tag 0D79](https://stacks.math.columbia.edu/tag/0D79) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.Augmentation.augmentedCechComplex_exactAt_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCechComplex.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCechComplex.lean#L485). The attribute's comment: “exactness in degree -1”.

> Exactness in degree `-1`: the complex
>
> `0 ⟶ a_*F ⟶ a_{0,*}F_0 ⟶ a_{1,*}F_1 ⟶ …`
>
> is exact at `a_*F`, which is Lean degree `0` because the augmentation shifts the complex by
> one.

```lean
theorem augmentedCechComplex_exactAt_zero : (augmentedCechComplex S D K a F).ExactAt 0
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.augmentedCechComplex_exactAt_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCechComplex.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCechComplex.lean#L496). The attribute's comment: “exactness in degree 0”.

> Exactness in degree `0`: the complex
>
> `0 ⟶ a_*F ⟶ a_{0,*}F_0 ⟶ a_{1,*}F_1 ⟶ …`
>
> is exact at `a_{0,*}F_0`, which is Lean degree `1` because the augmentation shifts the complex by
> one.

```lean
theorem augmentedCechComplex_exactAt_one : (augmentedCechComplex S D K a F).ExactAt 1
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.augmentedCechComplex_exactAt_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCechExact.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCechExact.lean#L210). The attribute's comment: “exactness in every degree for an injective abelian sheaf”.

> **Stacks 0D79**, exactness in every degree for an injective abelian sheaf: the complex
>
> `0 ⟶ a_*F ⟶ a_{0,*}F_0 ⟶ a_{1,*}F_1 ⟶ a_{2,*}F_2 ⟶ …`
>
> is exact at every term when `F` is an injective abelian sheaf on the total site. Degrees `0` and
> `1` — the source's degrees `-1` and `0` — hold for every `F` and are
> `augmentedCechComplex_exactAt_zero` and `augmentedCechComplex_exactAt_one`. Above them the
> argument is the source's: a complex of abelian sheaves is exact at a term as soon as `Hom(𝒢, -)`
> of it is exact for every `𝒢`, each term of this complex is a right adjoint whose left adjoint is
> the corresponding term of the resolution of Stacks 0D78, the mate of each cosimplicial transition
> is the corresponding structure map of that resolution, and `Hom(-, F)` of the resolution is exact
> because `F` is injective.

```lean
theorem augmentedCechComplex_exactAt_of_injective (F : Sheaf S.totalTopology Ab.{u})
    [Injective F] (k : ℕ) : (augmentedCechComplex S D K a F).ExactAt k
```

## Tag 0D7A, a lemma

[Tag 0D7A](https://stacks.math.columbia.edu/tag/0D7A) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.Augmentation.higherDirectImageSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationDerivedSpectralSequence.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationDerivedSpectralSequence.lean#L179).

> **Stacks 0D7A.** For an augmentation `a` of a simplicial-site situation towards a site
> `(D, K)` and `M` in `D⁺(C_total)` there is a spectral sequence
>
> `E_1^{p,q} = R^q a_{p,*} M_p  ⇒  R^{p+q} a_* M`,
>
> functorial in `M`. It is the spectral sequence of the double complex `A^{q,p} = a_{p,*} I^q_p` of
> a bounded below complex of injectives `I^•` representing `M`, filtered by the simplicial
> degree.

```lean
def higherDirectImageSpectralSequence : HigherDirectImageSpectralSequence S D K a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.9, Tag 0D9A](https://stacks.math.columbia.edu/tag/0D9A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
