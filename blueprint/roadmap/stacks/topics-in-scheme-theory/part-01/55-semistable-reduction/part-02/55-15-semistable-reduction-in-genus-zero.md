---
declaration: section
origin: cited
lean: Stacks.Models.RealConicModel.realConic_example
statement: formalized
proof: formalized
---

# 55.15 Semistable reduction in genus zero

Section 55.15 of the Stacks Project, [Tag 0CDK](https://stacks.math.columbia.edu/tag/0CDK). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CDL, an example

[Tag 0CDL](https://stacks.math.columbia.edu/tag/0CDL) in the Stacks Project.

**`Stacks.Models.RealConicModel.realConic_example`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/RealConicExample.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/RealConicExample.lean#L339).

> **Stacks Project, Tag 0CDL.** Let `R = ℝ[[π]]` with fraction field `K`, let
> `X = V(T₁² + T₂² - πT₀²) ⊆ ℙ²_R` and let `C = V(T₁² + T₂² - πT₀²) ⊆ ℙ²_K` be its generic fibre.
> 1. The base change of `X` to `ℂ[[π]]` is the scheme `V(T₁T₂ - πT₀²)` of [Stacks, Tag 0CA0].
> 2. `X` is regular, and its special fibre is irreducible yet singular.
> 3. `X` is a minimal model of `C`, and the unique one: every minimal model of `C` is isomorphic to
>    `X` as a model.
> 4. `C` has genus `0` and does not have good reduction over `R`: an extension of `R` is needed even
>    in genus `0`.

```lean
theorem realConic_example :
    IsPullback (splitMap PowerSeries.X (algebraMap (PowerSeries ℝ) (PowerSeries ℂ))
        iPowerSeries_sq two_mul_halfPowerSeries
        (GenusZero.isHomogeneous_conicEquation (PowerSeries.X : PowerSeries ℂ))
        (by rw [algebraMap_powerSeries_X]; rfl) ≫
        PlaneCurveModel.mapMap (equation PowerSeries.X) (isHomogeneous_equation _)
          (algebraMap (PowerSeries ℝ) (PowerSeries ℂ)))
      (GenusZero.conicToSpec (PowerSeries.X : PowerSeries ℂ))
      (toSpec (PowerSeries.X : PowerSeries ℝ))
      (Spec.map (CommRingCat.ofHom (algebraMap (PowerSeries ℝ) (PowerSeries ℂ)))) ∧
    IsRegular (scheme (PowerSeries.X : PowerSeries ℝ)) ∧
    IrreducibleSpace (specialFiber (PowerSeries.X : PowerSeries ℝ)
      (IsLocalRing.ResidueField (PowerSeries ℝ))) ∧
    ¬ IsRegular (specialFiber (PowerSeries.X : PowerSeries ℝ)
      (IsLocalRing.ResidueField (PowerSeries ℝ))) ∧
    IsMinimalModel (toSpec (algebraMap (PowerSeries ℝ) K PowerSeries.X))
      (toSpec (PowerSeries.X : PowerSeries ℝ)) (genericFiberIso K PowerSeries.X) ∧
    (∀ (Y : Scheme.{0}) (pY : Y ⟶ Spec (.of (PowerSeries ℝ)))
      (eY : scheme (algebraMap (PowerSeries ℝ) K PowerSeries.X) ≅
        pullback pY (Spec.map (CommRingCat.ofHom (algebraMap (PowerSeries ℝ) K)))),
      IsMinimalModel (toSpec (algebraMap (PowerSeries ℝ) K PowerSeries.X)) pY eY →
        ∃ φ : scheme (PowerSeries.X : PowerSeries ℝ) ≅ Y,
          φ.hom ≫ pY = toSpec (PowerSeries.X : PowerSeries ℝ) ∧
          (genericFiberIso K PowerSeries.X).hom ≫
              pullback.fst (toSpec (PowerSeries.X : PowerSeries ℝ))
                (Spec.map (CommRingCat.ofHom (algebraMap (PowerSeries ℝ) K))) ≫ φ.hom =
            eY.hom ≫
              pullback.fst pY (Spec.map (CommRingCat.ofHom (algebraMap (PowerSeries ℝ) K)))) ∧
    genus (toSpec (algebraMap (PowerSeries ℝ) K PowerSeries.X)) = 0 ∧
    ¬ HasGoodReduction (PowerSeries ℝ) (toSpec (algebraMap (PowerSeries ℝ) K PowerSeries.X))
      (isProjective_toSpec_powerSeries K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.15, Tag 0CDK](https://stacks.math.columbia.edu/tag/0CDK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
