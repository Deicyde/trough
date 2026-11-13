---
declaration: section
origin: cited
lean: Stacks.Cohomology.MittagLefflerCohomology.cohomology_transitionImage_stable_uniformly_of_powerCohomologyGradedACC, Stacks.Cohomology.MittagLefflerCohomology.isMittagLeffler_cohomology_of_powerCohomologyGradedACC, Stacks.Cohomology.MittagLefflerCohomology.cohomology_transitionImage_stable_uniformly, Stacks.Cohomology.MittagLefflerCohomology.isMittagLeffler_cohomology_of_stableImagesGradedACC, Stacks.Cohomology.QuotientTowers.cohomologyTowerLimit_topology_eq_adic
statement: formalized
proof: formalized
---

# 20.35 Inverse systems and cohomology, I

Section 20.35 of the Stacks Project, [Tag 0GYJ](https://stacks.math.columbia.edu/tag/0GYJ). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GYK, a lemma

[Tag 0GYK](https://stacks.math.columbia.edu/tag/0GYK) in the Stacks Project.

**`Stacks.Cohomology.MittagLefflerCohomology.cohomology_transitionImage_stable_uniformly_of_powerCohomologyGradedACC`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/PowerCohomologyACC.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/PowerCohomologyACC.lean#L299). The attribute's comment: “uniform stabilization (footnote)”.

> If the whole graded module `⨁ₙ Hᵖ⁺¹(X, Iⁿ𝓕ₙ₊₁)` satisfies graded ACC, there is a single
> lag `c` such that, for every `i`, the image of `Hᵖ(F_(i+c+1)) → Hᵖ(F_(i+1))` is already the
> stable image.

```lean
public theorem cohomology_transitionImage_stable_uniformly_of_powerCohomologyGradedACC
    (I : Ideal A) (F : ℕᵒᵖ ⥤ ModuleSheaf.{u, v, w} A X) (p : ℕ)
    (hquotient : IsQuotientTower.{u, v, w} I F)
    (hACC : PowerCohomologyHaveGradedACC.{u, v, w} I F (p + 1)) :
    ∃ c : ℕ, ∀ (i m : ℕ) (h : i + c ≤ m),
      transitionImage (F ⋙ cohomology.{u, v, w} (A := A) (X := X) p)
        i m ((Nat.le_add_right i c).trans h) =
      transitionImage (F ⋙ cohomology.{u, v, w} (A := A) (X := X) p)
        i (i + c) (Nat.le_add_right i c)
```

**`Stacks.Cohomology.MittagLefflerCohomology.isMittagLeffler_cohomology_of_powerCohomologyGradedACC`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/PowerCohomologyACC.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/PowerCohomologyACC.lean#L314). The attribute's comment: “Mittag-Leffler condition”.

> If the whole graded module `⨁ₙ Hᵖ⁺¹(X, Iⁿ𝓕ₙ₊₁)` satisfies graded ACC, the degree-`p`
> cohomology tower of an ideal-power quotient system satisfies the Mittag-Leffler condition.

```lean
public theorem isMittagLeffler_cohomology_of_powerCohomologyGradedACC
    (I : Ideal A) (F : ℕᵒᵖ ⥤ ModuleSheaf.{u, v, w} A X) (p : ℕ)
    (hquotient : IsQuotientTower.{u, v, w} I F)
    (hACC : PowerCohomologyHaveGradedACC.{u, v, w} I F (p + 1)) :
    IsMittagLefflerCategorical
      (F ⋙ cohomology.{u, v, w} (A := A) (X := X) p)
```

## Tag 0GYL, a lemma

[Tag 0GYL](https://stacks.math.columbia.edu/tag/0GYL) in the Stacks Project.

**`Stacks.Cohomology.MittagLefflerCohomology.cohomology_transitionImage_stable_uniformly`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/StableImagesACC.lean, line 1142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/StableImagesACC.lean#L1142). The attribute's comment: “uniform stabilization (footnote)”.

> Under the same hypotheses, there is a single lag `c` such that, for every
> `i`, the image of `Hᵖ(F_(i+c+1)) → Hᵖ(F_(i+1))` is already the stable image.

```lean
public theorem cohomology_transitionImage_stable_uniformly
    {A : Type u} [CommRing A] [Small.{v} A] (I : Ideal A)
    {X : Type w} [TopologicalSpace X]
    [UnivLE.{max w v, v}]
    (F : ℕᵒᵖ ⥤ ModuleSheaf.{u, v, w} A X) (p : ℕ)
    (hquotient : IsQuotientTower.{u, v, w} I F)
    (hACC : StableImagesHaveGradedACC.{u, v, w} I F (p + 1)) :
    ∃ c : ℕ, ∀ (i m : ℕ) (h : i + c ≤ m),
      transitionImage (F ⋙ cohomology.{u, v, w} (A := A) (X := X) p)
        i m ((Nat.le_add_right i c).trans h) =
      transitionImage (F ⋙ cohomology.{u, v, w} (A := A) (X := X) p)
        i (i + c) (Nat.le_add_right i c)
```

**`Stacks.Cohomology.MittagLefflerCohomology.isMittagLeffler_cohomology_of_stableImagesGradedACC`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/StableImagesACC.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/MittagLefflerCohomology/StableImagesACC.lean#L1180). The attribute's comment: “Mittag-Leffler condition”.

> If the stable images in degree `p + 1` satisfy graded ACC, the
> degree-`p` cohomology tower of an ideal-power quotient system satisfies the
> Mittag-Leffler condition.

```lean
public theorem isMittagLeffler_cohomology_of_stableImagesGradedACC
    {A : Type u} [CommRing A] [Small.{v} A] (I : Ideal A)
    {X : Type w} [TopologicalSpace X]
    [UnivLE.{max w v, v}]
    (F : ℕᵒᵖ ⥤ ModuleSheaf.{u, v, w} A X) (p : ℕ)
    (hquotient : IsQuotientTower.{u, v, w} I F)
    (hACC : StableImagesHaveGradedACC.{u, v, w} I F (p + 1)) :
    IsMittagLefflerCategorical
      (F ⋙ cohomology.{u, v, w} (A := A) (X := X) p)
```

## Tag 0GYM, a lemma

[Tag 0GYM](https://stacks.math.columbia.edu/tag/0GYM) in the Stacks Project.

**`Stacks.Cohomology.QuotientTowers.cohomologyTowerLimit_topology_eq_adic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/QuotientTowers.lean, line 1435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/QuotientTowers.lean#L1435). The attribute's comment: “the same conclusion under the stronger ACC hypothesis on the ambient graded”.

> For a quotient tower of sheaves `F` whose stable images satisfy ACC over `gr_I(A)`, the
> inverse-limit topology on `lim Hᵖ(X, F_n)` equals the `I`-adic topology.

```lean
public theorem cohomologyTowerLimit_topology_eq_adic
    [Small.{v} A] [UnivLE.{max w v, v}]
    (I : Ideal A) (X : Type w) [TopologicalSpace X]
    (F : ℕᵒᵖ ⥤ ModuleSheaf.{u, v, w} A X) (p : ℕ)
    (hquotient : IsQuotientTower.{u, v, w} I F)
    (hACC : StableImagesHaveGradedACC.{u, v, w} I F p) :
    CohomologyTowerLimit.limitTopology (fun n => cohomologyModule.{u, v, w} F p n)
        (cohomologyTransition.{u, v, w} F p) =
      I.adicModuleTopology
        (CohomologyTowerLimit (fun n => cohomologyModule.{u, v, w} F p n)
          (cohomologyTransition.{u, v, w} F p))
```

## Tag 0GYN, a lemma

[Tag 0GYN](https://stacks.math.columbia.edu/tag/0GYN) in the Stacks Project.

**`Stacks.Cohomology.QuotientTowers.cohomologyTowerLimit_topology_eq_adic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/QuotientTowers.lean, line 1435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/InverseSystems/QuotientTowers.lean#L1435).

> For a quotient tower of sheaves `F` whose stable images satisfy ACC over `gr_I(A)`, the
> inverse-limit topology on `lim Hᵖ(X, F_n)` equals the `I`-adic topology.

```lean
public theorem cohomologyTowerLimit_topology_eq_adic
    [Small.{v} A] [UnivLE.{max w v, v}]
    (I : Ideal A) (X : Type w) [TopologicalSpace X]
    (F : ℕᵒᵖ ⥤ ModuleSheaf.{u, v, w} A X) (p : ℕ)
    (hquotient : IsQuotientTower.{u, v, w} I F)
    (hACC : StableImagesHaveGradedACC.{u, v, w} I F p) :
    CohomologyTowerLimit.limitTopology (fun n => cohomologyModule.{u, v, w} F p n)
        (cohomologyTransition.{u, v, w} F p) =
      I.adicModuleTopology
        (CohomologyTowerLimit (fun n => cohomologyModule.{u, v, w} F p n)
          (cohomologyTransition.{u, v, w} F p))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.35, Tag 0GYJ](https://stacks.math.columbia.edu/tag/0GYJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
