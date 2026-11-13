---
declaration: section
origin: cited
lean: Rig.PerturbedPresentation.exists_algEquiv_of_perturbation, Rig.exists_finiteType_adicCompletion_algEquiv_henselization_quotient, Rig.exists_finiteType_adicCompletion_algEquiv_of_isGRing_of_isRigSmooth, Stacks.Smoothing.exists_etale_neighbourhood_algHom_approximation
statement: formalized
proof: formalized
---

# 88.6 Algebraization of rig-smooth algebras over G-rings

Section 88.6 of the Stacks Project, [Tag 0ALU](https://stacks.math.columbia.edu/tag/0ALU). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GAR, a lemma

[Tag 0GAR](https://stacks.math.columbia.edu/tag/0GAR) in the Stacks Project.

**`Rig.PerturbedPresentation.exists_algEquiv_of_perturbation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RigSmooth/PerturbationAlgEquiv.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RigSmooth/PerturbationAlgEquiv.lean#L147).

> **Stacks 0GAR.** Let `I` be an ideal of a Noetherian ring `A`, `r ≥ 0` and
> `P = A[x₁, …, x_r]^∧` the `I`-adic completion. Let `P^⊕t --K--> P^⊕m --(g₁, …, g_m)--> P → B → 0`
> be a resolution of the quotient `B = P/(g₁, …, g_m)`, and assume `B` is rig-smooth over `(A, I)`.
> Then there is an integer `n₀` such that for every `n ≥ n₀` and every complex
> `P^⊕t --K'--> P^⊕m --(g'₁, …, g'_m)--> P` with `gᵢ - g'ᵢ ∈ IⁿP` and
> `K - K' ∈ Iⁿ Mat(m × t, P)` there is an isomorphism of `A`-algebras `B ≅ B' = P/(g'₁, …, g'_m)`;
> moreover the perturbed complex is again a resolution.
>
> The proof is the source's.
> * (A) `I^c` annihilates `Ext¹_B(NL^∧_{B/A}, -)` for some `c`, by rig-smoothness
>   (`exists_extAnnihilated_of_isRigSmooth`).
> * (B) For `n` beyond an Artin-Rees constant of the resolution the perturbed complex is a
>   resolution (Stacks 07VE) and `Gr_I(B) ≅ Gr_I(B')` — as the equality of initial forms of the
>   two ideals (Stacks 07VF, `exists_perturbationBound_sameInitialForms`).
> * (C) The invariants of Local Cohomology, Section 0GA6 are those of `B`: `q₀ = q(Gr_I(B))` serves
>   for `B'` because `q` only depends on `Gr_I` (`isBaseThreshold_quotIdeal_of_sameInitialForms`),
>   and the vanishing degree `d` is read off a generating family of `I`, so it serves for every
>   quotient of `P` (`subsingleton_blowupHmod_of_span`).
> * Lemma 0GAQ (`Rig.exists_algHom_lift_of_dualSituation'`, via
>   `exists_comparison_algHom_of_liftingInputsAboveExponent`) lifts
>   the canonical `B → B'/IⁿB'` to an `A`-algebra map `φ : B → B'` congruent to it modulo a fixed
>   power of `I`; its inputs are the blowup's dual situations and the duality input of Tag 0GAC
>   (`liftingInputsOfIsBaseThreshold`).
> * The final paragraph: such a `φ` is an isomorphism (`exists_perturbationBound_algEquiv_of_algHom`,
>   by Artin-Rees and Nakayama).
>
> The integer `n₀` absorbs the precision loss of the lifting lemma, so its exact value is
> immaterial; the source's choice is `max(c₁ + 1, q₀ + (d₀ + 1)c, 2(d₀ + 1)c + 1)`.

```lean
public theorem exists_algEquiv_of_perturbation {t m : ℕ}
    (K : (Fin t → completedPolynomialAlgebra I r) →ₗ[completedPolynomialAlgebra I r]
      (Fin m → completedPolynomialAlgebra I r))
    (g : (Fin m → completedPolynomialAlgebra I r) →ₗ[completedPolynomialAlgebra I r]
      completedPolynomialAlgebra I r)
    (hexact : LinearMap.ker g = LinearMap.range K)
    (hB : IsRigSmooth (quotientObj A I r (LinearMap.range g))) :
    ∃ n₀ : ℕ, ∀ n ≥ n₀,
      ∀ (K' : (Fin t → completedPolynomialAlgebra I r) →ₗ[completedPolynomialAlgebra I r]
          (Fin m → completedPolynomialAlgebra I r))
        (g' : (Fin m → completedPolynomialAlgebra I r) →ₗ[completedPolynomialAlgebra I r]
          completedPolynomialAlgebra I r),
      g'.comp K' = 0 →
      CongruentModPow (I.map (algebraMap A (completedPolynomialAlgebra I r))) K K' n →
      CongruentModPow (I.map (algebraMap A (completedPolynomialAlgebra I r))) g g' n →
        LinearMap.ker g' = LinearMap.range K' ∧
        Nonempty
          ((completedPolynomialAlgebra I r ⧸
              (LinearMap.range g : Ideal (completedPolynomialAlgebra I r))) ≃ₐ[A]
            (completedPolynomialAlgebra I r ⧸
              (LinearMap.range g' : Ideal (completedPolynomialAlgebra I r))))
```

## Tag 0GAS, a lemma

[Tag 0GAS](https://stacks.math.columbia.edu/tag/0GAS) in the Stacks Project.

**`Rig.exists_finiteType_adicCompletion_algEquiv_henselization_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/GRing.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Algebraization/GRing.lean#L414).

> A quotient of the henselization of a finite type `A`-algebra has a completion algebraizable
> by a finite type `A`-algebra.

```lean
public theorem exists_finiteType_adicCompletion_algEquiv_henselization_quotient
    (A : Type u) (C : Type v) [CommRing A] [IsNoetherianRing A]
    [CommRing C] [Algebra A C] [Algebra.FiniteType A C]
    (I : Ideal A)
    (J : Ideal (henselization C (I.map (algebraMap A C)) : Type v)) :
    let H := (henselization C (I.map (algebraMap A C)) : Type v)
    letI : Algebra A H :=
      ((algebraMap C H).comp (algebraMap A C)).toAlgebra
    ∃ (B : Type (max u v)) (_ : CommRing B) (_ : Algebra A B)
      (_ : Algebra.FiniteType A B),
      Nonempty (AdicCompletion (I.map (algebraMap A B)) B ≃ₐ[A]
        AdicCompletion (I.map (algebraMap A (H ⧸ J))) (H ⧸ J))
```

## Tag 0GAT, a proposition

[Tag 0GAT](https://stacks.math.columbia.edu/tag/0GAT) in the Stacks Project.

**`Rig.exists_finiteType_adicCompletion_algEquiv_of_isGRing_of_isRigSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/PerturbationStableQuotients.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Algebraization/PerturbationStableQuotients.lean#L110).

> **Stacks Project, Proposition 0GAT.** Let `I` be an ideal of a Noetherian G-ring `A` and
> let `B` be an object of the category of Tag 0AL4. If `B` is rig-smooth over `(A, I)`, then
> there is a finite type `A`-algebra `C` and an isomorphism `B ≅ C^∧` of `A`-algebras.
>
> Every step of the source's proof is carried out:
> `Rig.exists_finiteType_adicCompletion_algEquiv_of_isRigSmooth'` runs the presentation (Tag 0AJP),
> its finite free resolution, the henselization `H` of `(A[x], I A[x])` with its G-ring property
> (Tags 07PV, 0AH3) and completion `P` (Tag 0AGV), the approximation of the resolution's relations
> over `H` (Tag 0AH5, with Popescu's Theorem 07GC and Tag 0AH2), and the final algebraization
> (Tag 0GAS); Lemma 0GAR is `Rig.perturbationStableQuotients`.

```lean
public theorem exists_finiteType_adicCompletion_algEquiv_of_isGRing_of_isRigSmooth
    (A : Type u) [CommRing A] [IsNoetherianRing A] (hA : IsGRing A) (I : Ideal A)
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (hB : IsRigSmooth B) :
    ∃ (C : Type (max u v)) (_ : CommRing C) (_ : Algebra A C),
      Algebra.FiniteType A C ∧
        Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)
```

## Tag 0AK4, a lemma

[Tag 0AK4](https://stacks.math.columbia.edu/tag/0AK4) in the Stacks Project.

**`Stacks.Smoothing.exists_etale_neighbourhood_algHom_approximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ApproximationOfCompletionMaps.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ApproximationOfCompletionMaps.lean#L188). The attribute's comment: “the full conclusion with NO carried hypotheses, for every `N ≥ 1`: an étale `C`-algebra `C'` inducing an isomorphism `C / IC ≅ C' / IC'` (indeed `C / (IC)^n ≅ C' / (IC)^n C'` for every `n`), and an `A`-algebra map `B → C'` agreeing modulo `I ^ N` with the given map of `I`-adic completions. Stacks 0AH5 is used, not assumed, and the `IsIndSmoothAdicCompletion` hypothesis it carries in place of the source's G-ring is discharged by Popescu's Theorem 07GC (`indSmooth_of_isRegularRingMap`) through `isIndSmoothAdicCompletion_of_isGRing`, applied once to the henselization of (C, IC), which is a G-ring by 0AH3 and whose completion map is regular by 0AH2. Stacks 0AKJ supplies the single étale stage.”.

> **Stacks 0AK4.** Let `A` be a Noetherian G-ring, `I ⊆ A` an ideal and `B`, `C` finite type
> `A`-algebras. Every `A`-algebra map `ψ` between the `I`-adic completions of `B` and `C` is
> approximated, to every positive order `N`, by an `A`-algebra map `φ : B → C'` into an étale
> `C`-algebra `C'` whose closed fibre agrees with that of `C`.

```lean
public theorem exists_etale_neighbourhood_algHom_approximation
    (A : Type u) (B : Type v) (C : Type w)
    [CommRing A] (hA : IsGRing A)
    [CommRing B] [Algebra A B] [Algebra.FiniteType A B]
    [CommRing C] [Algebra A C] [Algebra.FiniteType A C]
    (I : Ideal A)
    (ψ : AdicCompletion (I.map (algebraMap A B)) B →ₐ[A]
      AdicCompletion (I.map (algebraMap A C)) C)
    (N : ℕ) (hN : 1 ≤ N) :
    ∃ (C' : Type (max u v w)) (_ : CommRing C') (_ : Algebra C C')
      (_ : Algebra A C') (_ : IsScalarTower A C C') (_ : Algebra.Etale C C')
      (φ : B →ₐ[A] C'),
      (∀ n : ℕ, Function.Bijective
          (Ideal.quotientMap (((I.map (algebraMap A C)) ^ n).map (algebraMap C C'))
            (algebraMap C C') Ideal.le_comap_map)) ∧
      Function.Bijective
          (Ideal.quotientMap ((I.map (algebraMap A C)).map (algebraMap C C'))
            (algebraMap C C') Ideal.le_comap_map) ∧
      ∀ b : B,
        Ideal.quotientMap (((I.map (algebraMap A C)) ^ N).map (algebraMap C C'))
            (algebraMap C C') Ideal.le_comap_map
            (AdicCompletion.evalₐ (I.map (algebraMap A C)) N
              (ψ (algebraMap B (AdicCompletion (I.map (algebraMap A B)) B) b))) =
          Ideal.Quotient.mk (((I.map (algebraMap A C)) ^ N).map (algebraMap C C')) (φ b)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.6, Tag 0ALU](https://stacks.math.columbia.edu/tag/0ALU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
