---
declaration: section
origin: cited
lean: Stacks.Cohomology.AdicInverseSystems.exists_uniform_stable_image, Stacks.Cohomology.AdicInverseSystems.isMittagLefflerCategorical_cohomology, Stacks.Cohomology.AdicInverseSystems.exists_uniform_stable_image_of_stableImages, Stacks.Cohomology.AdicInverseSystems.isMittagLefflerCategorical_cohomology_of_stableImages, Stacks.Cohomology.AdicInverseSystems.limitTopology_eq_adicModuleTopology, Stacks.Cohomology.AdicInverseSystems.limitTopology_eq_adicModuleTopology_of_stableImages
statement: formalized
proof: formalized
---

# 21.22 Inverse systems and cohomology

Section 21.22 of the Stacks Project, [Tag 0GYP](https://stacks.math.columbia.edu/tag/0GYP). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GYQ, a lemma

[Tag 0GYQ](https://stacks.math.columbia.edu/tag/0GYQ) in the Stacks Project.

**`Stacks.Cohomology.AdicInverseSystems.exists_uniform_stable_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/MittagLeffler.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/MittagLeffler.lean#L274). The attribute's comment: “the uniform shift of the footnote”. References: SGA 2 IX (2.1), “(iii)”.

> **Stacks Project, Tag 0GYQ**, the footnote: the images of `Hᵖ(C, F_k) → Hᵖ(C, Fᵢ)` are the
> stable image already at `k = i + c`, for one `c` independent of `i`.

```lean
theorem exists_uniform_stable_image (hacc : WellFoundedGT (GradedSubmodule hF p)) :
    ∃ c : ℕ, ∀ i k : ℕ, ∀ h : i + c ≤ k,
      transitionImage (F ⋙ globalModuleCohomology.{u, v, r, w} O p) i k (by omega) =
        transitionImage (F ⋙ globalModuleCohomology.{u, v, r, w} O p) i (i + c) (by omega)
```

**`Stacks.Cohomology.AdicInverseSystems.isMittagLefflerCategorical_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/MittagLeffler.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/MittagLeffler.lean#L308).

> **Stacks Project, Tag 0GYQ.** For an inverse system of sheaves of modules on a site with
> `Fₙ = Fₙ₊₁/IⁿFₙ₊₁`, the ascending chain condition on the graded submodules of
> `⨁ₙ H^(p+1)(C, IⁿFₙ₊₁)` implies that the inverse system `n ↦ Hᵖ(C, Fₙ)` satisfies the
> Mittag-Leffler condition.

```lean
theorem isMittagLefflerCategorical_cohomology (hacc : WellFoundedGT (GradedSubmodule hF p)) :
    IsMittagLefflerCategorical (F ⋙ globalModuleCohomology.{u, v, r, w} O p)
```

## Tag 0GYR, a lemma

[Tag 0GYR](https://stacks.math.columbia.edu/tag/0GYR) in the Stacks Project.

**`Stacks.Cohomology.AdicInverseSystems.exists_uniform_stable_image_of_stableImages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/StableImages.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/StableImages.lean#L134). The attribute's comment: “the footnote: a uniform shift `c` with `Im(Mₙ → M_{n-c})` the stable image”.

> **Stacks Project, Tag 0GYR**, the footnote: the images of `Hᵖ(C, F_k) → Hᵖ(C, Fᵢ)` are the
> stable image already at `k = i + c`, for one `c` independent of `i`. In Stacks' indexing
> (`Mₙ = Hᵖ(C, Fₙ)` with Lean's `F i` standing for Stacks' `F_{i+1}`): there is `c ≥ 0` with
> `Im(Mₙ → M_{n-c})` the stable image for all `n ≥ c`, the stable image being the common value of
> `Im(M_k → M_{n-c})` for all `k ≥ n`.

```lean
theorem exists_uniform_stable_image_of_stableImages
    (hacc : WellFoundedGT (StableGradedSubmodule hF p)) :
    ∃ c : ℕ, ∀ i k : ℕ, ∀ h : i + c ≤ k,
      transitionImage (F ⋙ globalModuleCohomology.{u, v, r, w} O p) i k (by omega) =
        transitionImage (F ⋙ globalModuleCohomology.{u, v, r, w} O p) i (i + c) (by omega)
```

**`Stacks.Cohomology.AdicInverseSystems.isMittagLefflerCategorical_cohomology_of_stableImages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/StableImages.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/StableImages.lean#L171). The attribute's comment: “the Mittag-Leffler condition; the footnote's uniform shift is `exists_uniform_stable_image_of_stableImages`”.

> **Stacks Project, Tag 0GYR.** For an inverse system of sheaves of modules on a site with
> `Fₙ = Fₙ₊₁/IⁿFₙ₊₁`, the ascending chain condition on the graded submodules of `⨁ₙ Nₙ`, where
> `Nₙ = ⋂_{m ≥ n} Im(H^(p+1)(C, IⁿF_m) → H^(p+1)(C, IⁿFₙ))`, implies that the inverse system
> `n ↦ Hᵖ(C, Fₙ)` satisfies the Mittag-Leffler condition. The footnote's uniform shift is
> `exists_uniform_stable_image_of_stableImages`.

```lean
theorem isMittagLefflerCategorical_cohomology_of_stableImages
    (hacc : WellFoundedGT (StableGradedSubmodule hF p)) :
    IsMittagLefflerCategorical (F ⋙ globalModuleCohomology.{u, v, r, w} O p)
```

## Tag 0GYS, a lemma

[Tag 0GYS](https://stacks.math.columbia.edu/tag/0GYS) in the Stacks Project.

**`Stacks.Cohomology.AdicInverseSystems.limitTopology_eq_adicModuleTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/LimitTopology.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/LimitTopology.lean#L543).

> **Stacks Project, Tag 0GYS.** For an inverse system of sheaves of modules on a site with
> `Fₙ = Fₙ₊₁/IⁿFₙ₊₁`, the ascending chain condition on `⨁ₙ Hᵖ(C, IⁿFₙ₊₁)` as a graded
> `⨁ₙ Iⁿ/Iⁿ⁺¹`-module implies that the limit topology on `lim Hᵖ(C, Fₙ)` is the `I`-adic
> topology.

```lean
theorem limitTopology_eq_adicModuleTopology (hF : IsAdicQuotientSystem O I F) (p : ℕ)
    (hACC : HasGradedACC O I F hF p) :
    Stacks.AdicLimit.towerLimit.limitTopology
        (fun n => ((cohomologySystem O F p).obj (op n) : Type _))
        (cohomologyTransition O F p) =
      I.adicModuleTopology (cohomologyLimit O F p)
```

## Tag 0GYT, a lemma

[Tag 0GYT](https://stacks.math.columbia.edu/tag/0GYT) in the Stacks Project.

**`Stacks.Cohomology.AdicInverseSystems.limitTopology_eq_adicModuleTopology_of_stableImages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/StableImages.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InverseSystems/AdicQuotientSystems/StableImages.lean#L373).

> **Stacks Project, Tag 0GYT.** For an inverse system of sheaves of modules on a site with
> `Fₙ = Fₙ₊₁/IⁿFₙ₊₁`, the ascending chain condition on `⨁ₙ Nₙ` as a graded `⨁ₙ Iⁿ/Iⁿ⁺¹`-module,
> where `Nₙ = ⋂_{m ≥ n} Im(Hᵖ(C, IⁿF_m) → Hᵖ(C, IⁿFₙ))`, implies that the limit topology on
> `lim Hᵖ(C, Fₙ)` is the `I`-adic topology.

```lean
theorem limitTopology_eq_adicModuleTopology_of_stableImages
    (hF : IsAdicQuotientSystem O I F) (p : ℕ) (hACC : HasStableGradedACC O I F hF p) :
    Stacks.AdicLimit.towerLimit.limitTopology
        (fun n => ((cohomologySystem O F p).obj (op n) : Type _))
        (cohomologyTransition O F p) =
      I.adicModuleTopology (cohomologyLimit O F p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.22, Tag 0GYP](https://stacks.math.columbia.edu/tag/0GYP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
