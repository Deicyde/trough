---
declaration: section
origin: cited
lean: Stacks.Models.RegularProperModelSituation.eulerCharacteristic_addComponent, Stacks.Models.RegularProperModelSituation.cast_genus_eq_one_add_sum_specialFiberComponent, Stacks.Models.RegularProperModelSituation.associatedNumericalType_spec_and_genus, Stacks.Models.RegularProperModelSituation.associatedNumericalType, Stacks.Models.RegularProperModelSituation.isMinimalModel_iff_isMinimal_associatedNumericalType, AlgebraicGeometry.NumericalType.exists_genus_neg_not_equivalent_associatedNumericalType, AlgebraicGeometry.NumericalType.exists_isMinimal_genus_one_not_equivalent_associatedNumericalType, AlgebraicGeometry.NumericalType.exists_isMinimal_genus_seven_not_equivalent_associatedNumericalType
statement: formalized
proof: formalized
---

# 55.11 A formula for the genus

Section 55.11 of the Stacks Project, [Tag 0CA1](https://stacks.math.columbia.edu/tag/0CA1). 10 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CA2, a lemma

[Tag 0CA2](https://stacks.math.columbia.edu/tag/0CA2) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.eulerCharacteristic_addComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ComponentStepEulerCharacteristic.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ComponentStepEulerCharacteristic.lean#L335). The attribute's comment: “χ(X\_k, O\_D') - χ(X\_k, O\_D) = χ(X\_k, O\_X(-D)|\_Cᵢ) = -(D · Cᵢ) + χ(Cᵢ, O\_Cᵢ)”.

> **Stacks Project, Tag 0CA2.** In the situation of [Stacks, Tag 0C61] let `Cᵢ` be an
> irreducible component of the special fibre `X_k` and let `D, D' ⊂ X` be effective Cartier
> divisors with `D' = D + Cᵢ` and `D' ⊂ X_k`. Then
>
> `χ(X_k, 𝒪_{D'}) - χ(X_k, 𝒪_D) = χ(X_k, 𝒪_X(-D)|_{Cᵢ}) = -(D · Cᵢ) + χ(Cᵢ, 𝒪_{Cᵢ})`.
>
> Divisor sums are products of ideal sheaves, so `D' = D + Cᵢ` is `D' = D * Cᵢ`, and `D' ⊂ X_k` is
> the containment `ℐ_{X_k} ⊆ ℐ_{D'}`. The modules `𝒪_{D'}`, `𝒪_D` and `𝒪_X(-D)|_{Cᵢ}` are taken on
> `X_k` as direct images along the closed immersions into `X_k`. The intersection number
> `(D · Cᵢ)` is the intersection product `Stacks.Models.intersectionProduct` of [Stacks, Tag 0C65]
> on the components of `X_k`, with `D` read as the formal sum `∑ⱼ bⱼCⱼ` of its coefficients
> `bⱼ = Stacks.Models.RegularModelSituation.specialFiberDivisorCoeff D Cⱼ`, which is `D` by
> `Stacks.Models.RegularModelSituation.eq_prod_specialFiberDivisorCoeff`.
>
> The first equality is additivity of the Euler characteristic ([Stacks, Tag 08AA]) on the short
> exact sequence `0 ⟶ 𝒪_X(-D)|_{Cᵢ} ⟶ 𝒪_{D'} ⟶ 𝒪_D ⟶ 0` of [Stacks, Tag 0C4T], brought from `X`
> to `X_k` along the closed immersion `X_k ⟶ X`. The second is the definition of the degree,
> `deg(𝒪_X(-D)|_{Cᵢ}) = -deg(𝒪_X(D)|_{Cᵢ})`, and the symmetry of [Stacks, Tag 0C64].

```lean
public theorem eulerCharacteristic_addComponent
    [DecidableEq (irreducibleComponents S.specialFiber)]
    (Z : irreducibleComponents S.specialFiber) (D D' : S.X.IdealSheafData)
    [hD : Stacks.Divisors.IsEffectiveCartierDivisor D]
    (hsum : D' = D * S.specialFiberComponentIdeal Z) (hk : S.specialFiberIdeal ≤ D') :
    eulerCharacteristic S.k S.specialFiberToSpec
          ((Scheme.Modules.pushforward (S.fibreSubschemeι D' hk)).obj
            (SheafOfModules.unit D'.subscheme.ringCatSheaf)) -
        eulerCharacteristic S.k S.specialFiberToSpec
          ((Scheme.Modules.pushforward (S.fibreSubschemeι D
            (hk.trans (hsum ▸ Scheme.IdealSheafData.mul_le_left D _)))).obj
            (SheafOfModules.unit D.subscheme.ringCatSheaf)) =
      eulerCharacteristic S.k S.specialFiberToSpec
          ((Scheme.Modules.pushforward (S.specialFiberComponentι Z)).obj
            ((Scheme.Modules.pullback (S.specialFiberComponentIdeal Z).subschemeι).obj
              (Stacks.Divisors.negativeTwist D))) ∧
    eulerCharacteristic S.k S.specialFiberToSpec
          ((Scheme.Modules.pushforward (S.specialFiberComponentι Z)).obj
            ((Scheme.Modules.pullback (S.specialFiberComponentIdeal Z).subschemeι).obj
              (Stacks.Divisors.negativeTwist D))) =
      -intersectionProduct S Finset.univ (fun Y => S.specialFiberComponentIdeal Y)
          (fun Y => S.specialFiberComponentToSpec Y)
          (fun Y => S.isProper_specialFiberComponentToSpec Y)
          (fun Y => S.toRegularModelSituation.topologicalKrullDim_specialFiberComponent Y)
          (fun Y => (S.specialFiberDivisorCoeff D Y : ℤ)) (Pi.single Z 1)
          (fun Y _ => S.isEffectiveCartierDivisor_specialFiberComponent Y) +
        eulerCharacteristic S.k (S.specialFiberComponentToSpec Z)
          (SheafOfModules.unit (S.specialFiberComponentIdeal Z).subscheme.ringCatSheaf)
```

## Tag 0CA3, a lemma

[Tag 0CA3](https://stacks.math.columbia.edu/tag/0CA3) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.cast_genus_eq_one_add_sum_specialFiberComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GenusFormulaModel.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/GenusFormulaModel.lean#L335). The attribute's comment: “g\_C = 1 + Σ mᵢ([κᵢ : k\](gᵢ - 1) - (Cᵢ · Cᵢ)/2) at the canonical data of the model”.

> **Stacks Project, Tag 0CA3.** In the situation of [Stacks, Tag 0C61] — `R` a discrete
> valuation ring with fraction field `K` and residue field `k`, `C` a smooth projective curve over
> `K` with `H⁰(C, 𝒪_C) = K`, `X` a regular proper model of `C`, `C₁, …, Cₙ` the irreducible
> components of the special fibre and `X_k = Σ mᵢCᵢ` as in [Stacks, Tag 0C5Z] —
>
> `g_C = 1 + Σᵢ mᵢ([κᵢ : k](gᵢ - 1) - ½(Cᵢ · Cᵢ))`,
>
> where `κᵢ = H⁰(Cᵢ, 𝒪_{Cᵢ})`, `gᵢ` is the genus of `Cᵢ` (over `κᵢ`), `g_C` is the genus of `C` and
> `(Cᵢ · Cᵢ) = deg(𝒪_X(Cᵢ)|_{Cᵢ})` is the self-intersection number of [Stacks, Tag 0C64]. The
> components are indexed by `irreducibleComponents X_k`, and the formula is stated over `ℚ`.
>
> The proof is the source's: `1 - g_C = χ(C, 𝒪_C) = χ(X_k, 𝒪_{X_k})`, the chain of
> [Stacks, Tag 0CA2] from the empty divisor to `X_k` collapsed by part (2) of
> [Stacks, Tag 0C66], and `χ(Cᵢ, 𝒪_{Cᵢ}) = [κᵢ : k](1 - gᵢ)`.

```lean
public theorem cast_genus_eq_one_add_sum_specialFiberComponent :
    (genus S.C_to_K : ℚ) = 1 + ∑ Z, (S.specialFiberMultiplicity Z : ℚ) *
      ((S.specialFiberComponentWeight Z : ℚ) * ((S.specialFiberComponentGenus Z : ℚ) - 1) -
        (S.specialFiberIntersectionMatrix Z Z : ℚ) / 2)
```

## Tag 0CA4, a lemma

[Tag 0CA4](https://stacks.math.columbia.edu/tag/0CA4) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.associatedNumericalType_spec_and_genus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ModelNumericalTypeGenus.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ModelNumericalTypeGenus.lean#L60). The attribute's comment: “the data n, m\_i, (C\_i . C\_j), [kappa\_i : k], g\_i form a numerical type of genus the genus of C”.

> **Stacks Project, Tag 0CA4.** In the situation of [Stacks, Tag 0C61], with `C₁, …, Cₙ` the
> irreducible components of the special fibre enumerated by `e`, `κᵢ = H⁰(Cᵢ, 𝒪_{Cᵢ})` and `gᵢ`
> the genus of `Cᵢ` over `κᵢ`, the data `n, mᵢ, (Cᵢ · Cⱼ), [κᵢ : k], gᵢ` form a numerical type —
> the numerical type `Stacks.Models.RegularProperModelSituation.associatedNumericalType`, whose
> fields carry the laws of [Stacks, Tag 0C6Z] — and its genus is the genus `g_C` of `C`.

```lean
public theorem associatedNumericalType_spec_and_genus (n : ℕ)
    (e : Fin n ≃ irreducibleComponents S.specialFiber) :
    ((S.associatedNumericalType n e).componentCount = n ∧
      (∀ i, (S.associatedNumericalType n e).multiplicity i =
        (S.specialFiberMultiplicity (e i) : ℤ)) ∧
      (∀ i j, (S.associatedNumericalType n e).intersection i j =
        S.specialFiberIntersectionMatrix (e i) (e j)) ∧
      (∀ i, (S.associatedNumericalType n e).weight i =
        (S.specialFiberComponentWeight (e i) : ℤ)) ∧
      (∀ i, (S.associatedNumericalType n e).componentGenus i =
        (S.specialFiberComponentGenus (e i) : ℤ))) ∧
    (S.associatedNumericalType n e).genus = (genus S.C_to_K : ℤ)
```

## Tag 0CA5, a definition

[Tag 0CA5](https://stacks.math.columbia.edu/tag/0CA5) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.associatedNumericalType`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/AssociatedNumericalType.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/AssociatedNumericalType.lean#L88). The attribute's comment: “the numerical type associated to X: n, m\_i, (C\_i . C\_j), [kappa\_i : k], g\_i of the components of the special fibre”.

> **Stacks Project, Tag 0CA5: the numerical type associated to `X`**, in the situation of
> [Stacks, Tag 0C61]: the numerical type described in [Stacks, Tag 0CA4], whose data are the number
> `n` of irreducible components `C₁, …, Cₙ` of the special fibre (enumerated by `e`), their
> multiplicities `mᵢ` (Tag 0C5Z), their intersection numbers `(Cᵢ · Cⱼ)`, their weights
> `[κᵢ : k]` with `κᵢ = H⁰(Cᵢ, 𝒪_{Cᵢ})`, and their genera `gᵢ` over `κᵢ`. All the laws of a
> numerical type are proved: the multiplicities are positive, the intersection matrix is the degree
> matrix of the components, symmetric, nonnegative off the diagonal, connected and annihilates
> `(mᵢ)`, and `[κᵢ : k]` divides every `(Cᵢ · Cⱼ)`. The enumeration is immaterial by
> `Stacks.Models.RegularProperModelSituation.equivalent_associatedNumericalType`, which is what
> licenses the definite article.

```lean
public def associatedNumericalType (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber) :
    AlgebraicGeometry.NumericalType
```

## Tag 0CA6, a lemma

[Tag 0CA6](https://stacks.math.columbia.edu/tag/0CA6) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.isMinimalModel_iff_isMinimal_associatedNumericalType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelNumericalTypeIff.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelNumericalTypeIff.lean#L164).

> **Stacks Project, Tag 0CA6.** In the situation of [Stacks, Tag 0C61], let `C₁, …, Cₙ` be the
> irreducible components of the special fibre, enumerated by `e`. Then `X` is a minimal model if and
> only if the numerical type associated to `X` ([Stacks, Tag 0CA5]) is minimal
> ([Stacks, Tag 0C7A]).

```lean
theorem isMinimalModel_iff_isMinimal_associatedNumericalType
    (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber) :
    IsMinimalModel S.C_to_K S.X_to_R S.genericFiberIso ↔
      (S.associatedNumericalType n e).IsMinimal
```

## Tag 0CA7, a remark

[Tag 0CA7](https://stacks.math.columbia.edu/tag/0CA7) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.exists_genus_neg_not_equivalent_associatedNumericalType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotAssociated.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotAssociated.lean#L476). The attribute's comment: “not every numerical type is the numerical type associated to a model, as there are numerical types of negative genus”.

> **Not every numerical type comes from a model**: there is a numerical type of negative genus,
> and it is equivalent to no numerical type associated to a regular proper model of a smooth
> projective curve over the fraction field of a discrete valuation ring.

```lean
public theorem exists_genus_neg_not_equivalent_associatedNumericalType :
    ∃ T : NumericalType, genus T < 0 ∧
      ∀ (S : RegularProperModelSituation.{u}) [DecidableEq (irreducibleComponents S.specialFiber)]
        (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber),
        ¬ (S.associatedNumericalType n e).Equivalent T
```

**`AlgebraicGeometry.NumericalType.exists_isMinimal_genus_one_not_equivalent_associatedNumericalType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotAssociated.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotAssociated.lean#L493). The attribute's comment: “n = 1, m₁ = 1, a₁₁ = 0, w₁ = 6, g₁ = 1 is a minimal numerical type of genus one which is not the numerical type associated to a model”.

> **A minimal numerical type of positive genus not coming from a model**: the data `n = 1`,
> `m₁ = 1`, `a₁₁ = 0`, `w₁ = 6`, `g₁ = 1` form a minimal numerical type of genus one which is
> equivalent to no numerical type associated to a regular proper model, over a discrete valuation
> ring `R`, of a smooth projective curve `C` over the fraction field `K` with `H⁰(C, 𝒪_C) = K`; in
> particular of a smooth projective geometrically irreducible curve over `K`. The special fibre of
> such a model would live over an extension of degree `6` of the residue field, against its
> geometric connectedness.

```lean
public theorem exists_isMinimal_genus_one_not_equivalent_associatedNumericalType :
    ∃ T : NumericalType, T.componentCount = 1 ∧
      (∀ i, T.multiplicity i = 1) ∧
      (∀ i j, T.intersection i j = 0) ∧
      (∀ i, T.weight i = 6) ∧
      (∀ i, T.componentGenus i = 1) ∧
      IsMinimal T ∧ genus T = 1 ∧
      ∀ (S : RegularProperModelSituation.{u}) [DecidableEq (irreducibleComponents S.specialFiber)]
        (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber),
        ¬ (S.associatedNumericalType n e).Equivalent T
```

**`AlgebraicGeometry.NumericalType.exists_isMinimal_genus_seven_not_equivalent_associatedNumericalType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotAssociated.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotAssociated.lean#L517). The attribute's comment: “n = 2, m₁ = m₂ = 1, -a₁₁ = -a₂₂ = a₁₂ = a₂₁ = 6, w₁ = w₂ = 6, g₁ = g₂ = 1 is a minimal numerical type of genus seven which is not the numerical type associated to a model”.

> **A second minimal numerical type of positive genus not coming from a model**: the data
> `n = 2`, `m₁ = m₂ = 1`, `-a₁₁ = -a₂₂ = a₁₂ = a₂₁ = 6`, `w₁ = w₂ = 6`, `g₁ = g₂ = 1` form a minimal
> numerical type of genus seven which is equivalent to no numerical type associated to a regular
> proper model, over a discrete valuation ring `R`, of a smooth projective curve `C` over the
> fraction field `K` with `H⁰(C, 𝒪_C) = K`; in particular of a smooth projective geometrically
> irreducible curve over `K`. As for the one-component example, the reduced special fibre of such a
> model would live over an extension of degree `6` of the residue field, against its geometric
> connectedness.

```lean
public theorem exists_isMinimal_genus_seven_not_equivalent_associatedNumericalType :
    ∃ T : NumericalType, T.componentCount = 2 ∧
      (∀ i, T.multiplicity i = 1) ∧
      (∀ i, T.intersection i i = -6) ∧
      (∀ i j, i ≠ j → T.intersection i j = 6) ∧
      (∀ i, T.weight i = 6) ∧
      (∀ i, T.componentGenus i = 1) ∧
      IsMinimal T ∧ genus T = 7 ∧
      ∀ (S : RegularProperModelSituation.{u}) [DecidableEq (irreducibleComponents S.specialFiber)]
        (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber),
        ¬ (S.associatedNumericalType n e).Equivalent T
```

**`AlgebraicGeometry.NumericalType.exists_genus_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotFromModel.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotFromModel.lean#L63). The attribute's comment: “there exist numerical types whose genus is negative”.

> There is a numerical type whose genus is negative. The numerical type of a model has the
> genus of the generic curve, which is nonnegative, so no such type comes from a model.

```lean
public theorem exists_genus_neg : ∃ T : NumericalType, genus T < 0
```

**`AlgebraicGeometry.NumericalType.exists_isMinimal_genus_one_weight_six`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotFromModel.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotFromModel.lean#L83). The attribute's comment: “n = 1, m₁ = 1, a₁₁ = 0, w₁ = 6, g₁ = 1 is a minimal numerical type of genus one”.

> The data `n = 1`, `m₁ = 1`, `a₁₁ = 0`, `w₁ = 6`, `g₁ = 1` is a minimal numerical type of
> genus one.

```lean
public theorem exists_isMinimal_genus_one_weight_six :
    ∃ T : NumericalType, T.componentCount = 1 ∧
      (∀ i, T.multiplicity i = 1) ∧
      (∀ i j, T.intersection i j = 0) ∧
      (∀ i, T.weight i = 6) ∧
      (∀ i, T.componentGenus i = 1) ∧
      IsMinimal T ∧ genus T = 1
```

**`AlgebraicGeometry.NumericalType.exists_isMinimal_genus_seven_weight_six`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotFromModel.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/NotFromModel.lean#L146). The attribute's comment: “n = 2, m₁ = m₂ = 1, -a₁₁ = -a₂₂ = a₁₂ = a₂₁ = 6, w₁ = w₂ = 6, g₁ = g₂ = 1 is a minimal numerical type of genus seven”.

> The data `n = 2`, `m₁ = m₂ = 1`, `-a₁₁ = -a₂₂ = a₁₂ = a₂₁ = 6`, `w₁ = w₂ = 6`,
> `g₁ = g₂ = 1` is a minimal numerical type of genus seven.

```lean
public theorem exists_isMinimal_genus_seven_weight_six :
    ∃ T : NumericalType, T.componentCount = 2 ∧
      (∀ i, T.multiplicity i = 1) ∧
      (∀ i, T.intersection i i = -6) ∧
      (∀ i j, i ≠ j → T.intersection i j = 6) ∧
      (∀ i, T.weight i = 6) ∧
      (∀ i, T.componentGenus i = 1) ∧
      IsMinimal T ∧ genus T = 7
```

## Tag 0CE8, a lemma

[Tag 0CE8](https://stacks.math.columbia.edu/tag/0CE8) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.exists_isRationalPoint_smoothAt_specialFiber_and_genus_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/RationalPointSpecialFibre.lean, line 656](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/RationalPointSpecialFibre.lean#L656). The attribute's comment: “the k-rational smooth point x of X\_k, H⁰(Cᵢ) = k and mᵢ = 1 for the components through x, H⁰(X\_k) = k and g(X\_k) = g(C)”.

> **Stacks Project, Tag 0CE8.** In Situation [Stacks, Tag 0C61] assume that the curve `C` has a
> `K`-rational point. Then
>
> 1. the special fibre `X_k` has a `k`-rational point `x` at which `X_k ⟶ Spec(k)` is smooth;
> 2. every irreducible component `Cᵢ` of `X_k` through `x` has `H⁰(Cᵢ, 𝒪_{Cᵢ}) = k` and
>    multiplicity `mᵢ = 1` in `X_k = Σ mᵢCᵢ`;
> 3. `H⁰(X_k, 𝒪_{X_k}) = k`, and the genus of `X_k` is the genus of `C`.
>
> `H⁰(Y, 𝒪_Y) = k` is the assertion that the canonical map `k ⟶ Γ(Y, 𝒪_Y)` is an isomorphism, and
> the genus is `AlgebraicGeometry.genus`, `dim H¹(𝒪)` over the base field.

```lean
theorem exists_isRationalPoint_smoothAt_specialFiber_and_genus_eq (p : Spec (.of S.K) ⟶ S.C)
    (hp : p ≫ S.C_to_K = 𝟙 _) :
    (∃ x : S.specialFiber, IsRationalPoint S.specialFiberToSpec x ∧
      InfinitesimalLifting.SmoothAt S.specialFiberToSpec x ∧
      ∀ Z : irreducibleComponents S.specialFiber, x ∈ Z.1 →
        IsIso ((Scheme.ΓSpecIso (.of S.k)).inv ≫ (S.specialFiberComponentToSpec Z).appTop) ∧
          S.specialFiberMultiplicity Z = 1) ∧
    IsIso ((Scheme.ΓSpecIso (.of S.k)).inv ≫ S.specialFiberToSpec.appTop) ∧
      genus S.specialFiberToSpec = genus S.C_to_K
```

## Tag 0CE9, a lemma

[Tag 0CE9](https://stacks.math.columbia.edu/tag/0CE9) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.surjective_and_not_injective_of_isMinimalModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelNumericalTypeIff.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelNumericalTypeIff.lean#L187).

> **Stacks Project, Tag 0CE9.** In the situation of [Stacks, Tag 0C61] assume `X` is a minimal
> model, `gcd(m₁, …, mₙ) = 1` and `H⁰((X_k)_red, 𝒪) = k`. Then the map
> `H¹(X_k, 𝒪_{X_k}) ⟶ H¹((X_k)_red, 𝒪_{(X_k)_red})` induced by the reduction `(X_k)_red ⟶ X_k`
> (`AlgebraicGeometry.cohomologyOverFieldStructureSheafMap`) is surjective, and it has a nontrivial
> kernel, that is it is not injective, as soon as `(X_k)_red ≠ X_k`, that is as soon as `X_k` is not
> reduced.

```lean
theorem surjective_and_not_injective_of_isMinimalModel
    (hmin : IsMinimalModel S.C_to_K S.X_to_R S.genericFiberIso)
    (hgcd : Finset.univ.gcd S.specialFiberMultiplicity = 1)
    (hred : IsIso ((Scheme.ΓSpecIso (.of S.k)).inv ≫
      (S.specialFiber.reductionι ≫ S.specialFiberToSpec).appTop)) :
    Function.Surjective (cohomologyOverFieldStructureSheafMap S.k S.specialFiberToSpec
        S.specialFiber.reductionι 1) ∧
      (¬ IsReduced S.specialFiber →
        ¬ Function.Injective (cohomologyOverFieldStructureSheafMap S.k S.specialFiberToSpec
          S.specialFiber.reductionι 1))
```

## Tag 0CEA, a lemma

[Tag 0CEA](https://stacks.math.columbia.edu/tag/0CEA) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.topologicalGenus_add_geometricGenus_le_finrank_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedFibreGenusBound.lean, line 534](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ReducedFibreGenusBound.lean#L534). The attribute's comment: “dim\_k H^1((X\_k)\_red, O) >= g\_top + g\_geom(X\_k/k) when X\_k has a k-rational smooth point, g\_top the topological genus of the numerical type associated to X”.

> **Stacks Project, Tag 0CEA.** In the situation of [Stacks, Tag 0C61] suppose the special
> fibre `X_k` has a `k`-rational point `x` which is a smooth point of `X_k ⟶ Spec(k)`. Then
>
> `dim_k H¹((X_k)_red, 𝒪_{(X_k)_red}) ≥ g_top + g_geom(X_k/k)`,
>
> where `g_top` is the topological genus ([Stacks, Tag 0C79]) of the numerical type associated to
> `X` ([Stacks, Tag 0CA5]), for any enumeration `e` of the irreducible components of `X_k`, and
> `g_geom(X_k/k)` is the geometric genus of [Stacks, Section 0CE0]. The cohomology of the reduction
> `(X_k)_red` is taken over `k` through `(X_k)_red ⟶ X_k ⟶ Spec(k)`.
>
> Only the rationality of `x` is used; see the module documentation.

```lean
theorem topologicalGenus_add_geometricGenus_le_finrank_reduction
    (x : S.specialFiber) (hx : IsRationalPoint S.specialFiberToSpec x)
    (_hsm : InfinitesimalLifting.SmoothAt S.specialFiberToSpec x)
    (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber) :
    (S.associatedNumericalType n e).topologicalGenus +
        (geometricGenus S.k S.specialFiberToSpec : ℤ) ≤
      Module.finrank S.k (cohomologyOverField S.k
        (S.specialFiber.reductionι ≫ S.specialFiberToSpec)
        (SheafOfModules.unit S.specialFiber.reduction.ringCatSheaf) 1)
```

## Tag 0CEE, a lemma

[Tag 0CEE](https://stacks.math.columbia.edu/tag/0CEE) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.smooth_and_not_forall_isSeparable_of_genus_equality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/GenusEqualityComponents.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/GenusEqualityComponents.lean#L72). The attribute's comment: “Corrected form, with a counterexample to the statement as printed: (1) in full; (2) with kappa/k separable whenever H^1(C, O\_C) is nonzero; the last conjunct shows that separability fails in general (a model over F\_2(t)[[pi]] with a component P^1\_kappa, kappa = k(sqrt t)).”.

> **The corrected form of [Stacks, Tag 0CEE], together with the refutation of its separability
> clause.** In the situation of [Stacks, Tag 0C61] let `x` be a `k`-rational point of `X_k` at which
> `X_k ⟶ Spec(k)` is smooth, and suppose equality holds in [Stacks, Tag 0CEA]:
> `dim_k H¹((X_k)_red, 𝒪) = g_top + g_geom(X_k/k)`. Then
>
> 1. `x` lies on a unique irreducible component of `X_k`, and that component is a smooth,
>    H-projective, geometrically irreducible curve over `k`;
> 2. every other irreducible component `C` has `κ = H⁰(C, 𝒪_C)` finite over `k`, has a `κ`-rational
>    point and is smooth over `κ`; and `κ/k` is separable as soon as `H¹(C, 𝒪_C) ≠ 0`.
>
> The source asserts in (2) that `κ/k` is always separable. The second conjunct shows that this
> fails: there is a situation of [Stacks, Tag 0C61], with a smooth `k`-rational point and equality
> in [Stacks, Tag 0CEA], with a component `C` not through the point such that `H⁰(C, 𝒪_C)` is not
> separable over `k`. The model is `Stacks.Models.InseparableModel.situation`: over
> `R = 𝔽₂(t)⟦π⟧` it is the blow-up of `ℙ¹_R` at the closed point `X₁² = t X₀²` of the special
> fibre, written as the divisor `π X₀² V = (X₁² - t X₀²) U` of `ℙ¹_R × ℙ¹_R`. Its special fibre is
> `C₁ + E` with `C₁ ≅ ℙ¹_k` and `E ≅ ℙ¹_κ`, `κ = k(√t)` purely inseparable of degree two, meeting
> transversally in one `κ`-point; a section of the model gives a smooth `k`-rational point on
> `C₁ \ E`, `dim_k H¹((X_k)_red, 𝒪) = 0`, so equality holds, and `H⁰(E, 𝒪_E) = κ`.
>
> Where the source's argument breaks: equality in `[κ_i : k] g_i ≥ [κ_i : k]_s g_i ≥ g_geom(C_i/k)`
> gives `[κ_i : k] = [κ_i : k]_s` only when `g_i > 0`; for `g_i = 0`, as for `E`, it says nothing
> about `κ_i/k`. Every other assertion of the tag survives, with the proof recorded at
> `smooth_of_topologicalGenus_add_geometricGenus_eq_finrank_reduction`, which is the statement
> proved first and then paired here with the refutation.

```lean
theorem smooth_and_not_forall_isSeparable_of_genus_equality
    (x : S.specialFiber) (hx : IsRationalPoint S.specialFiberToSpec x)
    (hsm : InfinitesimalLifting.SmoothAt S.specialFiberToSpec x)
    (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber)
    (heq : (S.associatedNumericalType n e).topologicalGenus +
        (geometricGenus S.k S.specialFiberToSpec : ℤ) =
      Module.finrank S.k (cohomologyOverField S.k
        (S.specialFiber.reductionι ≫ S.specialFiberToSpec)
        (SheafOfModules.unit S.specialFiber.reduction.ringCatSheaf) 1)) :
    ((∃! Z : irreducibleComponents S.specialFiber, x ∈ Z.1) ∧
    (∀ Z : irreducibleComponents S.specialFiber, x ∈ Z.1 →
      Smooth (S.specialFiberComponentToSpec Z) ∧
        Stacks.HProjective.IsHProjective (S.specialFiberComponentToSpec Z) ∧
        GeometricallyIrreducible (S.specialFiberComponentToSpec Z) ∧
        IsCurve S.k (S.specialFiberComponentToSpec Z)) ∧
    (∀ Z : irreducibleComponents S.specialFiber, x ∉ Z.1 →
      letI : Field Γ((S.specialFiberComponentIdeal Z).subscheme, ⊤) :=
        (S.isField_and_finite_globalSections_specialFiberComponent Z).1.toField
      letI : Algebra S.k Γ((S.specialFiberComponentIdeal Z).subscheme, ⊤) :=
        ((Scheme.ΓSpecIso (.of S.k)).inv ≫ (S.specialFiberComponentToSpec Z).appTop).hom.toAlgebra
      FiniteDimensional S.k Γ((S.specialFiberComponentIdeal Z).subscheme, ⊤) ∧
        (genus (S.specialFiberComponentIdeal Z).subscheme.toSpecΓ ≠ 0 →
          Algebra.IsSeparable S.k Γ((S.specialFiberComponentIdeal Z).subscheme, ⊤)) ∧
        (∃ c : (S.specialFiberComponentIdeal Z).subscheme,
          IsRationalPoint (S.specialFiberComponentIdeal Z).subscheme.toSpecΓ c) ∧
        Smooth (S.specialFiberComponentIdeal Z).subscheme.toSpecΓ)) ∧
    ¬ ∀ (S' : RegularProperModelSituation.{0}) (x' : S'.specialFiber)
      (_hx' : IsRationalPoint S'.specialFiberToSpec x')
      (_hsm' : InfinitesimalLifting.SmoothAt S'.specialFiberToSpec x')
      (n' : ℕ) (e' : Fin n' ≃ irreducibleComponents S'.specialFiber)
      (_heq' : (S'.associatedNumericalType n' e').topologicalGenus +
          (geometricGenus S'.k S'.specialFiberToSpec : ℤ) =
        Module.finrank S'.k (cohomologyOverField S'.k
          (S'.specialFiber.reductionι ≫ S'.specialFiberToSpec)
          (SheafOfModules.unit S'.specialFiber.reduction.ringCatSheaf) 1))
      (Z : irreducibleComponents S'.specialFiber), x' ∉ Z.1 →
        letI : Field Γ((S'.specialFiberComponentIdeal Z).subscheme, ⊤) :=
          (S'.isField_and_finite_globalSections_specialFiberComponent Z).1.toField
        letI : Algebra S'.k Γ((S'.specialFiberComponentIdeal Z).subscheme, ⊤) :=
          ((Scheme.ΓSpecIso (.of S'.k)).inv ≫
            (S'.specialFiberComponentToSpec Z).appTop).hom.toAlgebra
        Algebra.IsSeparable S'.k Γ((S'.specialFiberComponentIdeal Z).subscheme, ⊤)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.11, Tag 0CA1](https://stacks.math.columbia.edu/tag/0CA1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
