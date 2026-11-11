---
declaration: section
origin: cited
lean: Stacks.Examples.finite_iff_piScalarRightHom_nat_surjective, Stacks.Examples.finitePresentation_iff_piScalarRightHom_nat_bijective, Stacks.Examples.isCoherentRing_iff_flat_pi_nat, Stacks.Examples.exists_powerSeries_not_flat, Stacks.Examples.normal_iff_isCompletelyNormal_of_powerSeries_flat, Stacks.Examples.instFlatPowerSeriesOfValuationRing, Stacks.Examples.not_flat_powerSeries_over_polynomial_of_dim_gt_one, Stacks.Examples.not_flat_powerSeries_map_localizationAway
statement: formalized
proof: formalized
---

# 110.12 Nonflat completions

Section 110.12 of the Stacks Project, [Tag 0AL8](https://stacks.math.columbia.edu/tag/0AL8). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AL9, a lemma

[Tag 0AL9](https://stacks.math.columbia.edu/tag/0AL9) in the Stacks Project.

**`Stacks.Examples.finite_iff_piScalarRightHom_nat_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/CountableCoherent.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/CountableCoherent.lean#L69).

> A countable module is finitely generated if and only if the canonical map
> `M ⊗[R] (ℕ → R) → (ℕ → M)` is surjective.

```lean
theorem finite_iff_piScalarRightHom_nat_surjective :
    Module.Finite R M ↔
      Function.Surjective (TensorProduct.piScalarRightHom R R M ℕ)
```

## Tag 0ALA, a lemma

[Tag 0ALA](https://stacks.math.columbia.edu/tag/0ALA) in the Stacks Project.

**`Stacks.Examples.finitePresentation_iff_piScalarRightHom_nat_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/CountableCoherent.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/CountableCoherent.lean#L105).

> A countable module over a countable ring is finitely presented if and only if the canonical
> map `M ⊗[R] (ℕ → R) → (ℕ → M)` is bijective.

```lean
theorem finitePresentation_iff_piScalarRightHom_nat_bijective :
    Module.FinitePresentation R M ↔
      Function.Bijective (TensorProduct.piScalarRightHom R R M ℕ)
```

## Tag 0ALB, a lemma

[Tag 0ALB](https://stacks.math.columbia.edu/tag/0ALB) in the Stacks Project.

**`Stacks.Examples.isCoherentRing_iff_flat_pi_nat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/CountableCoherent.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/CountableCoherent.lean#L168).

> A countable commutative ring is coherent if and only if its countable product, as a module
> over itself, is flat.

```lean
theorem isCoherentRing_iff_flat_pi_nat (R : Type u) [CommRing R] [Countable R] :
    IsCoherentRing R ↔ Module.Flat R (ℕ → R)
```

## Tag 0ALC, a lemma

[Tag 0ALC](https://stacks.math.columbia.edu/tag/0ALC) in the Stacks Project.

**`Stacks.Examples.exists_powerSeries_not_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/PowerSeriesNotFlat.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/PowerSeriesNotFlat.lean#L116).

> For some commutative ring, its formal power series ring is flat over neither the
> coefficient ring nor the polynomial ring.

```lean
theorem exists_powerSeries_not_flat :
    ∃ (R : Type u) (hR : CommRing R),
      letI : CommRing R := hR
      (¬ Module.Flat R (PowerSeries R)) ∧
        (¬ Module.Flat (Polynomial R) (PowerSeries R))
```

## Tag 0F1Y, a lemma

[Tag 0F1Y](https://stacks.math.columbia.edu/tag/0F1Y) in the Stacks Project.

**`Stacks.Examples.normal_iff_isCompletelyNormal_of_powerSeries_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/CompletelyNormalOfPowerSeriesFlat.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/CompletelyNormalOfPowerSeriesFlat.lean#L271).

> A domain whose power series ring is flat over its polynomial ring is normal
> if and only if it is completely normal.

```lean
theorem normal_iff_isCompletelyNormal_of_powerSeries_flat
    (R : Type*) [CommRing R] [IsDomain R]
    (hflat : Module.Flat (Polynomial R) (PowerSeries R)) :
    IsIntegrallyClosed R ↔ IsCompletelyNormal R
```

## Tag 0F1Z, a lemma

[Tag 0F1Z](https://stacks.math.columbia.edu/tag/0F1Z) in the Stacks Project.

**`Stacks.Examples.instFlatPowerSeriesOfValuationRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/PowerSeriesOverValuationRing.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/PowerSeriesOverValuationRing.lean#L63). The attribute's comment: “flat over the coefficient ring”.

> The power series ring over a valuation ring is flat over its coefficient ring.

```lean
instance instFlatPowerSeriesOfValuationRing (R : Type*) [CommRing R] [IsDomain R]
    [ValuationRing R] : Module.Flat R (PowerSeries R)
```

**`Stacks.Examples.not_flat_powerSeries_over_polynomial_of_dim_gt_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/PowerSeriesOverValuationRing.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/PowerSeriesOverValuationRing.lean#L130). The attribute's comment: “not flat over the polynomial ring”.

> In dimension greater than one, the power series ring over a valuation ring is not
> flat over its polynomial ring.

```lean
theorem not_flat_powerSeries_over_polynomial_of_dim_gt_one (R : Type*)
    [CommRing R] [IsDomain R] [ValuationRing R] (hdim : 1 < ringKrullDim R) :
    ¬ Module.Flat (Polynomial R) (PowerSeries R)
```

## Tag 0ALD, an equation

[Tag 0ALD](https://stacks.math.columbia.edu/tag/0ALD) in the Stacks Project.

**`Stacks.Examples.not_flat_powerSeries_map_localizationAway`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/PowerSeriesLocalizationNotFlat.lean, line 957](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/PowerSeriesLocalizationNotFlat.lean#L957).

> The coefficientwise localization map from the power series ring of
> `k[y, z, aᵢ]/(y aᵢ, aᵢ aⱼ)` to the power series ring of its localization at `z`
> is not flat.

```lean
theorem not_flat_powerSeries_map_localizationAway
    (k : Type u) [Field k] :
    ¬ (PowerSeries.map
      (algebraMap (nonflatPowerSeriesRing k)
        (Localization.Away (nonflatPowerSeriesElement k)))).Flat
```

## Tag 0ALE, a lemma

[Tag 0ALE](https://stacks.math.columbia.edu/tag/0ALE) in the Stacks Project.

**`Stacks.Examples.exists_nonflat_completed_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/CompletedLocalizationNotFlat.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/CompletedLocalizationNotFlat.lean#L384).

> There is a ring complete for a principal ideal whose completed principal
> localization is not flat over the ring.

```lean
theorem exists_nonflat_completed_localization :
    ∃ (A : Type*) (_ : CommRing A) (x f : A),
      IsAdicComplete (Ideal.span {x}) A ∧
        ¬ Module.Flat A
          (AdicCompletion
            ((Ideal.span {x}).map (algebraMap A (Localization.Away f)))
            (Localization.Away f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.12, Tag 0AL8](https://stacks.math.columbia.edu/tag/0AL8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
