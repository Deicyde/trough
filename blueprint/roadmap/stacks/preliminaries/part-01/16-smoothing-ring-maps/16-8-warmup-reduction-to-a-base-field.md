---
declaration: section
origin: cited
lean: Stacks.Smoothing.RegularRingMapSituation, pt_product, Stacks.Smoothing.exists_factorization_isElementaryStandard, Stacks.Smoothing.indSmooth_of_indSmooth_of_field_base
statement: formalized
proof: formalized
---

# 16.8 Warmup: reduction to a base field

Section 16.8 of the Stacks Project, [Tag 07F1](https://stacks.math.columbia.edu/tag/07F1). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07F2, a situation

[Tag 07F2](https://stacks.math.columbia.edu/tag/07F2) in the Stacks Project.

**`Stacks.Smoothing.RegularRingMapSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/RegularRingMap.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/RegularRingMap.lean#L59).

> The standing data of Stacks 16.8.1: a regular ring map between Noetherian rings.

```lean
structure RegularRingMapSituation
```

## Tag 07F3, a lemma

[Tag 07F3](https://stacks.math.columbia.edu/tag/07F3) in the Stacks Project.

**`pt_product`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ProductOfFilteredColimits.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/ProductOfFilteredColimits.lean#L555).

> Let `R_i → Λ_i` (`i = 1, 2`) be ring maps of Noetherian rings. If PT holds for `R_1 → Λ_1`
> and for `R_2 → Λ_2`, then PT holds for the product ring map `R_1 × R_2 → Λ_1 × Λ_2` (with the
> componentwise algebra structure).

```lean
theorem pt_product
    (R₁ R₂ Λ₁ Λ₂ : Type)
    [CommRing R₁] [CommRing R₂] [CommRing Λ₁] [CommRing Λ₂]
    [Algebra R₁ Λ₁] [Algebra R₂ Λ₂]
    [IsNoetherianRing R₁] [IsNoetherianRing Λ₁]
    [IsNoetherianRing R₂] [IsNoetherianRing Λ₂]
    (hPT₁ : PT R₁ Λ₁) (hPT₂ : PT R₂ Λ₂) :
    letI : Algebra (R₁ × R₂) (Λ₁ × Λ₂) :=
      ((algebraMap R₁ Λ₁).prodMap (algebraMap R₂ Λ₂)).toAlgebra
    PT (R₁ × R₂) (Λ₁ × Λ₂)
```

## Tag 07F4, a lemma

[Tag 07F4](https://stacks.math.columbia.edu/tag/07F4) in the Stacks Project.

**`Stacks.Smoothing.exists_factorization_isElementaryStandard`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/DelocalizingSmoothFactorization/ElementaryStandard.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/DelocalizingSmoothFactorization/ElementaryStandard.lean#L86).

> **Stacks 07F4.** Let `R → A → Λ` be ring maps with `A` of finite presentation over `R` and
> let `S ⊆ R` be a multiplicative set. Given a factorization `S⁻¹A → B' → S⁻¹Λ` with `B'` smooth
> over `S⁻¹R`, there is a factorization `A → B → Λ` of `A → Λ` by `R`-algebras in which some
> `s ∈ S` maps to an elementary standard element of `B` over `R`.
>
> Step 1 of the source proof, the reduction to a standard smooth `B'`, is Stacks 07CH; it is
> supplied by `Stacks.Smoothing.exists_smooth_isStandardSmooth_retraction`.

```lean
theorem exists_factorization_isElementaryStandard
    (S : Submonoid R)
    [Algebra (Localization S) (Localization (S.map (algebraMap R A)))]
    [IsScalarTower R (Localization S) (Localization (S.map (algebraMap R A)))]
    [Algebra (Localization S) (Localization (S.map (algebraMap R Λ)))]
    [Algebra (Localization (S.map (algebraMap R A)))
      (Localization (S.map (algebraMap R Λ)))]
    [Algebra A (Localization (S.map (algebraMap R Λ)))]
    [IsScalarTower A Λ (Localization (S.map (algebraMap R Λ)))]
    (h : ∃ (B' : Type u') (_ : CommRing B')
      (_ : Algebra (Localization (S.map (algebraMap R A))) B')
      (_ : Algebra (Localization S) B')
      (_ : Algebra B' (Localization (S.map (algebraMap R Λ))))
      (_ : Algebra A B')
      (_ : IsScalarTower A (Localization (S.map (algebraMap R A))) B')
      (_ : IsScalarTower (Localization S)
        (Localization (S.map (algebraMap R A))) B')
      (_ : IsScalarTower (Localization (S.map (algebraMap R A))) B'
        (Localization (S.map (algebraMap R Λ))))
      (_ : IsScalarTower A B' (Localization (S.map (algebraMap R Λ)))),
      Algebra.Smooth (Localization S) B') :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B) (_ : Algebra B Λ)
      (_ : Algebra R B),
      IsScalarTower R A B ∧ IsScalarTower A B Λ ∧ IsScalarTower R B Λ ∧
        ∃ s : S, IsElementaryStandard (R := R) (algebraMap R B s)
```

## Tag 07F5, a lemma

[Tag 07F5](https://stacks.math.columbia.edu/tag/07F5) in the Stacks Project.

**`Stacks.Smoothing.indSmooth_of_indSmooth_of_field_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ReductionToBaseField.lean, line 876](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/ReductionToBaseField.lean#L876). The attribute's comment: “Situation 07F2 is `IsRegularRingMap` plus the Noetherian hypotheses, and PT is `IndSmooth`, the `ObjectProperty.ind` spelling of Lemma 07C3.”.

> **Stacks 07F5.** If property PT — that `Λ` is a filtered colimit of smooth `R`-algebras —
> holds for every regular ring map `R → Λ` of Noetherian rings whose source is a field, then it
> holds for every regular ring map of Noetherian rings.

```lean
theorem indSmooth_of_indSmooth_of_field_base
    (hfield : ∀ (k : Type u) [Field k] (Λ : Type u) [CommRing Λ] [Algebra k Λ]
      [IsNoetherianRing Λ], IsRegularRingMap k Λ → IndSmooth k Λ)
    (R : Type u) [CommRing R] (Λ : Type u) [CommRing Λ] [Algebra R Λ]
    [IsNoetherianRing R] [IsNoetherianRing Λ] (hregular : IsRegularRingMap R Λ) :
    IndSmooth R Λ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.8, Tag 07F1](https://stacks.math.columbia.edu/tag/07F1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
