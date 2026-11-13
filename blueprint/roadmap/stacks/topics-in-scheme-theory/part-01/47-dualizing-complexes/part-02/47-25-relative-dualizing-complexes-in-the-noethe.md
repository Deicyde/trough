---
declaration: section
origin: cited
lean: Dualizing.relativeDualizingComplexBaseChange_of_perfect, Dualizing.relativeDualizingComplexBaseChange_of_flatBaseChange, Dualizing.relativeDualizingComplexBaseChange_of_flatAlgebra, Dualizing.upperShriekFunctor_unit_derivedCategoryBBounded_of_perfect, Dualizing.PolynomialPresentation.relativeDualizingComplex_hasFiniteTorDimension_of_perfect, Dualizing.PolynomialPresentation.relativeDualizingComplex_isRelativelyPerfect, Dualizing.upperShriekFunctor_unit_isIso_derivedHomothety_of_perfect, Dualizing.isDualizingComplex_derivedExtensionScalars_relativeDualizing_of_flat
statement: formalized
proof: formalized
---

# 47.25 Relative dualizing complexes in the Noetherian case

Section 47.25 of the Stacks Project, [Tag 0E9M](https://stacks.math.columbia.edu/tag/0E9M). 9 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BZV, a lemma

[Tag 0BZV](https://stacks.math.columbia.edu/tag/0BZV) in the Stacks Project.

**`Dualizing.relativeDualizingComplexBaseChange_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingBaseChange.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingBaseChange.lean#L226). The attribute's comment: “case (3), R → A perfect and A, R' Tor independent”.

> Let `R → R'` be a ring homomorphism, let `φ : R → A` be a perfect homomorphism presented by
> `p`, and let `A` and `R'` be Tor independent over `R`.  Then the relative dualizing complex
> commutes with base change to `R'`: there is an isomorphism `ω^•_{A/R} ⊗_A^L A' ≅ ω^•_{A'/R'}` in
> `D(A')`, where `A' = R' ⊗_R A` and the derived tensor product is read at the given left-derived
> model of extension of scalars.  The Noetherian hypotheses of the source are not needed.

```lean
theorem relativeDualizingComplexBaseChange_of_perfect [Algebra.Perfect R A]
    (p : PolynomialPresentation (algebraMap R A))
    (hTor : TorIndependent R A R')
    (bcT : DerivedCategory (ModuleCat.{u} A) ⥤
      DerivedCategory (ModuleCat.{u} (TensorProduct R R' A)))
    (cmpT : DerivedCategory.Q ⋙ bcT ⟶
      (ModuleCat.extendScalars.{u, u, u}
          (Algebra.TensorProduct.includeRight :
            A →ₐ[R] TensorProduct R R' A).toRingHom).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (ldT : bcT.IsLeftDerivedFunctor cmpT
      (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    Nonempty (bcT.obj (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))) ≅
        (p.baseChange (R' := R')).upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R') 0).obj (ModuleCat.of R' R')))
```

**`Dualizing.relativeDualizingComplexBaseChange_of_flatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingBaseChange.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingBaseChange.lean#L270). The attribute's comment: “case (1), R → R' flat”.

> Let `R` be a Noetherian ring, `R → R'` a flat ring homomorphism, and let `φ : R → A` be of
> finite type, presented by `p`.  Then the relative dualizing complex commutes with base change to
> `R'`: there is an isomorphism `ω^•_{A/R} ⊗_A^L A' ≅ ω^•_{A'/R'}` in `D(A')`, where
> `A' = R' ⊗_R A` and the derived tensor product is read at the given left-derived model of
> extension of scalars.  The source's Noetherian hypothesis on `R'` is not needed.

```lean
theorem relativeDualizingComplexBaseChange_of_flatBaseChange [IsNoetherianRing R]
    (p : PolynomialPresentation (algebraMap R A))
    (hflat : (algebraMap R R').Flat)
    (bcT : DerivedCategory (ModuleCat.{u} A) ⥤
      DerivedCategory (ModuleCat.{u} (TensorProduct R R' A)))
    (cmpT : DerivedCategory.Q ⋙ bcT ⟶
      (ModuleCat.extendScalars.{u, u, u}
          (Algebra.TensorProduct.includeRight :
            A →ₐ[R] TensorProduct R R' A).toRingHom).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (ldT : bcT.IsLeftDerivedFunctor cmpT
      (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    Nonempty (bcT.obj (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))) ≅
        (p.baseChange (R' := R')).upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R') 0).obj (ModuleCat.of R' R')))
```

**`Dualizing.relativeDualizingComplexBaseChange_of_flatAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingBaseChange.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingBaseChange.lean#L316). The attribute's comment: “case (2), R → A flat”.

> Let `R` be a Noetherian ring, `R → R'` a ring homomorphism, and let `φ : R → A` be flat
> and of finite type, presented by `p`.  Then the relative dualizing complex commutes with base
> change to `R'`: there is an isomorphism `ω^•_{A/R} ⊗_A^L A' ≅ ω^•_{A'/R'}` in `D(A')`, where
> `A' = R' ⊗_R A` and the derived tensor product is read at the given left-derived model of
> extension of scalars.  The source's Noetherian hypothesis on `R'` is not needed.

```lean
theorem relativeDualizingComplexBaseChange_of_flatAlgebra [IsNoetherianRing R]
    (p : PolynomialPresentation (algebraMap R A))
    (hflat : (algebraMap R A).Flat)
    (bcT : DerivedCategory (ModuleCat.{u} A) ⥤
      DerivedCategory (ModuleCat.{u} (TensorProduct R R' A)))
    (cmpT : DerivedCategory.Q ⋙ bcT ⟶
      (ModuleCat.extendScalars.{u, u, u}
          (Algebra.TensorProduct.includeRight :
            A →ₐ[R] TensorProduct R R' A).toRingHom).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (ldT : bcT.IsLeftDerivedFunctor cmpT
      (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    Nonempty (bcT.obj (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))) ≅
        (p.baseChange (R' := R')).upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R') 0).obj (ModuleCat.of R' R')))
```

## Tag 0BZW, a lemma

[Tag 0BZW](https://stacks.math.columbia.edu/tag/0BZW) in the Stacks Project.

**`Dualizing.upperShriekFunctor_unit_derivedCategoryBBounded_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizing.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizing.lean#L147). The attribute's comment: “(1)(a)”. References: SGA 5 III (6.2), “partial”.

> Let `φ : R →+* A` be a perfect homomorphism of finite type of Noetherian rings. Then the
> relative dualizing complex `ω_{A/R} = φ^!(R)` lies in `Dᵇ_Coh(A)`.

```lean
theorem upperShriekFunctor_unit_derivedCategoryBBounded_of_perfect
    [IsNoetherianRing R] [IsNoetherianRing A] (p : PolynomialPresentation f) (hf : f.Perfect) :
    DerivedCategoryB.derivedCategoryBBounded
      (fun N : ModuleCat.{max v u} A ↦ Module.Finite A N)
      (p.upperShriekFunctor.{u, v}.obj
        ((DerivedCategory.singleFunctor (ModuleCat.{max v u} R) 0).obj
          (ModuleCat.of R (ULift.{v} R))))
```

**`Dualizing.PolynomialPresentation.relativeDualizingComplex_hasFiniteTorDimension_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingFiniteTorDimension.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingFiniteTorDimension.lean#L466). The attribute's comment: “(1)(b)”. References: SGA 5 III (6.2), “partial”.

> **[Stacks, Tag 0BZW] (1)(b).**  Let `φ : R →+* A` be a perfect homomorphism, presented by `p`.
> Then the relative dualizing complex `ω^•_{A/R} = φ^!(R)` has finite Tor dimension as a complex of
> `R`-modules.  The Noetherian hypotheses of the source are not needed.
>
> Perfectness of `φ` is perfectness of `A` over the polynomial algebra of any presentation
> ([stacks 068Y], `Algebra.Perfect.exists_finite_projective_resolution` read through [stacks 066Q]),
> and that is the hypothesis of `relativeDualizingComplex_hasFiniteTorDimension_of_isPerfectModule`.
>
> Finite Tor dimension over `R` is read at the canonical certified derived tensor product, which is
> the one the definition of relative perfection ([stacks 0DHS]) is written with.

```lean
theorem relativeDualizingComplex_hasFiniteTorDimension_of_perfect [Algebra.Perfect R A]
    (p : PolynomialPresentation (algebraMap R A)) :
    StacksDraft.TorAmplitude.HasFiniteTorDimension
      (CochainComplex.DerivedTensor.canonicalDerivedTensorProduct R).tensor
      (StacksDraft.TorAmplitude.canonicalTensorComparison R)
      (StacksDraft.TorAmplitude.canonicalTensorIsLeftDerived R)
      ((ModuleCat.restrictScalars (algebraMap R A)).mapDerivedCategory.obj
        (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))))
```

**`Dualizing.PolynomialPresentation.relativeDualizingComplex_isRelativelyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingFiniteTorDimension.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingFiniteTorDimension.lean#L523). The attribute's comment: “(2)(a)”.

> **[Stacks, Tag 0BZW] (2)(a).**  Let `φ : R → A` be a flat homomorphism of finite type of
> Noetherian rings, presented by `p`.  Then `ω^•_{A/R} = φ^!(R)` is perfect relative to `R` in the
> sense of [stacks 0DHS].
>
> Nothing is carried.  Relative perfection is by definition the conjunction of pseudo-coherence over
> `A` and finite Tor dimension over `R`: the first is [stacks 0BZW] (1)(a), available as
> `Dualizing.PolynomialPresentation.relativeDualizingComplex_isPseudoCoherent_of_flat`, and the
> second is [stacks 0BZW] (1)(b), which is
> `Dualizing.PolynomialPresentation.relativeDualizingComplex_hasFiniteTorDimension_of_flat` above.
>
> This is the same statement as
> `Dualizing.PolynomialPresentation.relativeDualizingComplex_isRelativelyPerfect_of_flat` of
> `StacksFrontier.RingTheory.Dualizing.UpperShriek.RelativePerfection`, which reaches it by the
> fibrewise criterion [stacks 0GHJ] and therefore carries the open projection-formula compatibility
> `Dualizing.PolynomialPresentation.ProjectionCompatibility` at every residue field of `R`.  Here
> nothing is carried; both are kept, the two routes being independent.

```lean
theorem relativeDualizingComplex_isRelativelyPerfect
    [IsNoetherianRing R] [IsNoetherianRing A]
    (p : PolynomialPresentation (algebraMap R A)) (hflat : (algebraMap R A).Flat) :
    letI : Module.Flat R A := RingHom.flat_algebraMap_iff.mp hflat
    letI : Algebra.FinitePresentation R A :=
      Algebra.FinitePresentation.of_finiteType.mp (RingHom.finiteType_algebraMap.mp p.finiteType)
    PseudoCoherence.IsRelativelyPerfect.{u, u, u}
      (CochainComplex.DerivedTensor.canonicalDerivedTensorProduct R).tensor
      (StacksDraft.TorAmplitude.canonicalTensorComparison R)
      (StacksDraft.TorAmplitude.canonicalTensorIsLeftDerived R)
      (p.upperShriekFunctor.{u, 0}.obj
        ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)))
```

**`Dualizing.upperShriekFunctor_unit_isIso_derivedHomothety_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingProperties.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingProperties.lean#L69). The attribute's comment: “(1)(c)”.

> **Stacks Project, Tag 0BZW (1)(c).**  Let `φ : R →+* A` be a perfect homomorphism of finite
> type of Noetherian rings, presented by an arbitrary polynomial presentation `p`.  Then the
> canonical map `A ⟶ RHom_A(ω_{A/R}, ω_{A/R})` of [Stacks, Tag 0A7C] — the derived homothety of the
> adjunction of [Stacks, Tag 0A63] at `ω_{A/R} = φ^!(R)` — is an isomorphism.
>
> The source's proof: a perfect ring map is perfect through the polynomial algebra `P` of every
> presentation ([Stacks, Tag 068Y], `Algebra.Perfect.exists_finite_projective_resolution` read
> through [Stacks, Tag 066Q]), perfectness survives the universe lift to the module universe in
> which upper shriek is formed (`StacksDraft.Perfect.isPerfectModule_ulift`), and then
> `Dualizing.upperShriekFunctor_unit_isIso_derivedHomothety_of_isPerfectModule` reads
> `RHom_A(ω_{A/R}, ω_{A/R})` in `D(P)` as the double dual of `A` and concludes by
> [Stacks, Tag 07VI].  Noetherianity of `A` is not needed by the proof.

```lean
theorem upperShriekFunctor_unit_isIso_derivedHomothety_of_perfect [IsNoetherianRing R]
    (p : PolynomialPresentation f) (hf : f.Perfect) :
    IsIso (derivedHomothety (StacksDraft.DerivedHom.derivedHomAdjunctionOverRing.{u, v} A)
      (StacksDraft.DerivedHom.derivedTensorUnit.{u, v} A)
      (StacksDraft.DerivedHom.derivedTensorUnitLeft.{u, v} A)
      (p.upperShriekFunctor.{u, v}.obj
        ((DerivedCategory.singleFunctor (ModuleCat.{max v u} R) 0).obj
          (ModuleCat.of R (ULift.{v} R)))))
```

**`Dualizing.isDualizingComplex_derivedExtensionScalars_relativeDualizing_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingProperties.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingProperties.lean#L116). The attribute's comment: “(2)(b)”.

> **Stacks Project, Tag 0BZW (2)(b).**  Let `φ : R → A` be a flat homomorphism of finite type of
> Noetherian rings, presented by an arbitrary polynomial presentation `p`, and let `R → k` be a
> homomorphism to a field.  Then the derived base change of `ω^•_{A/R} = φ^!(R)` along the
> coprojection `A → k ⊗_R A` is a dualizing complex for the fibre ring `k ⊗_R A`.
>
> The source's proof: base change for the relative dualizing complex, [Stacks, Tag 0BZV] case (2)
> at `R' = k`, identifies the derived base change with `ω^•_{A'/k}` for `A' = k ⊗_R A`, which is a
> dualizing complex by [Stacks, Tag 0BZL]; this is
> `Dualizing.isDualizingComplex_derivedExtensionScalars_upperShriekFunctor_unit_of_field`.

```lean
theorem isDualizingComplex_derivedExtensionScalars_relativeDualizing_of_flat
    {R A : Type u} [CommRing R] [CommRing A] [IsNoetherianRing R] [IsNoetherianRing A]
    [Algebra R A] (k : Type u) [Field k] [Algebra R k]
    (p : PolynomialPresentation (algebraMap R A)) (hflat : (algebraMap R A).Flat) :
    letI : IsNoetherianRing (TensorProduct R k A) := isNoetherianRing_baseChange k p
    IsDualizingComplex
      ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
          (Algebra.TensorProduct.includeRight :
            A →ₐ[R] TensorProduct R k A).toRingHom).functor.obj
        (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))))
```

## Tag 0E0P, a lemma

[Tag 0E0P](https://stacks.math.columbia.edu/tag/0E0P) in the Stacks Project.

**`Dualizing.isDualizingComplex_derivedExtensionScalars_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/FieldExtensionBaseChange.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/FieldExtensionBaseChange.lean#L123).

> **Stacks Project, Tag 0E0P.** Let `k ⊆ K` be an extension of fields and let `A` be a
> `k`-algebra of finite type.  The derived base change of a dualizing complex for `A` along
> `A → A_K = K ⊗_k A` is a dualizing complex for `A_K`.

```lean
theorem isDualizingComplex_derivedExtensionScalars_fieldExtension
    {ω : DerivedCategory (ModuleCat.{u} A)}
    (hω : letI : IsNoetherianRing A := Algebra.FiniteType.isNoetherianRing k A
      IsDualizingComplex ω) :
    letI : IsNoetherianRing (TensorProduct k K A) :=
      Algebra.FiniteType.isNoetherianRing K (TensorProduct k K A)
    IsDualizingComplex
      ((totalDerivedExtensionScalars.{u, u, u}
        (Algebra.TensorProduct.includeRight :
          A →ₐ[k] TensorProduct k K A).toRingHom).functor.obj ω)
```

## Tag 0E4B, a lemma

[Tag 0E4B](https://stacks.math.columbia.edu/tag/0E4B) in the Stacks Project.

**`Dualizing.PolynomialPresentation.isInvertible_upperShriekFunctor_obj_unit_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/CompleteIntersection.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/CompleteIntersection.lean#L477).

> **Stacks 0E4B**, invertibility of the relative dualizing complex of a local complete
> intersection homomorphism.  Let `φ : R → A` be a local complete intersection homomorphism with
> `R` Noetherian and let `p` be any polynomial presentation of `φ`.  Then `ω_{A/R} = φ^!(R)` is an
> invertible object of `D(A)`.
>
> The kernel of one presentation is Koszul-regular by the definition of a local complete
> intersection, hence the kernel of every presentation is, by [Stacks, Tag 07CZ]; so
> `isInvertible_upperShriekFunctor_obj_unit_of_isKoszulRegular` applies to `p`.

```lean
theorem isInvertible_upperShriekFunctor_obj_unit_of_isLocalCompleteIntersection
    [IsNoetherianRing R] (p : PolynomialPresentation f)
    (hf : f.IsLocalCompleteIntersection) :
    letI : MonoidalCategoryStruct (ModuleCat.{u} R) :=
      ModuleCat.liftedModuleMonoidalStruct.{u, u}
    letI : MonoidalCategory (ModuleCat.{u} R) := ModuleCat.liftedModuleMonoidal.{u, u}
    let R₀ := (DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
      (MonoidalCategoryStruct.tensorUnit (ModuleCat.{u} R))
    letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory A).choose
    MonoidalCategory.IsInvertible (p.upperShriekFunctor.{u, u}.obj R₀)
```

**`Dualizing.PolynomialPresentation.upperShriekFunctor_iso_derivedTensorProduct_of_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/CompleteIntersection.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/CompleteIntersection.lean#L507). The attribute's comment: “the formula φ^!(K) = K ⊗\_R^L ω\_\{A/R}, at an arbitrary polynomial presentation and an arbitrary module universe”.

> **Stacks 0E4B**, the formula for upper shriek.  Let `φ : R → A` be a local complete
> intersection homomorphism and let `p` be a polynomial presentation of `φ`.
> Then `φ^!(K) = K ⊗_R^L ω_{A/R}` with `ω_{A/R} = φ^!(R)`, naturally in `K` in `D(R)`.
>
> A local complete intersection homomorphism is perfect by [Stacks, Tag 07EN], so `A` is a perfect
> module over the polynomial algebra of `p` by [Stacks, Tag 068Y], which is what the tensor formula
> of [Stacks, Tag 0BZU] asks for, and that formula asks for nothing else: the
> conclusion of [Stacks, Tag 0BZE] for the surjection of the presentation holds at the arbitrary
> module universe `max v u` of this statement, by
> `Dualizing.nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect_anyModuleUniverse`.

```lean
theorem upperShriekFunctor_iso_derivedTensorProduct_of_lci
    (p : PolynomialPresentation f)
    (hf : f.IsLocalCompleteIntersection) :
    letI : MonoidalCategoryStruct (ModuleCat.{max v u} R) :=
      ModuleCat.liftedModuleMonoidalStruct.{u, max v u}
    letI : MonoidalCategory (ModuleCat.{max v u} R) :=
      ModuleCat.liftedModuleMonoidal.{u, max v u}
    let R₀ := (DerivedCategory.singleFunctor (ModuleCat.{max v u} R) 0).obj
      (MonoidalCategoryStruct.tensorUnit (ModuleCat.{max v u} R))
    Nonempty (p.upperShriekFunctor.{u, v} ≅
      derivedTensorProductOver.{u, v} f (p.upperShriekFunctor.{u, v}.obj R₀))
```

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso_derivedTensorProduct_of_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean#L207). The attribute's comment: “the formula φ^!(K) = K ⊗\_R^L ω\_\{A/R}, at an arbitrary polynomial presentation, at module universe equal to the ring universe; the same statement at an arbitrary module universe is Dualizing.PolynomialPresentation.upperShriekFunctor\_iso\_derivedTensorProduct\_of\_lci”.

> **Stacks 0E4B, with no carried hypothesis.** Let `φ : R → A` be a local complete intersection
> homomorphism and `p` a polynomial presentation of it. Then
> `φ^!(K) = K ⊗_R^L ω_{A/R}` with `ω_{A/R} = φ^!(R)`, naturally in `K`.
>
> This is `Dualizing.PolynomialPresentation.upperShriekFunctor_iso_derivedTensorProduct_of_lci`
> read at module universe equal to the ring universe; that statement holds at any module
> universe.

```lean
theorem nonempty_upperShriekFunctor_iso_derivedTensorProduct_of_lci
    (p : PolynomialPresentation f)
    (hf : f.IsLocalCompleteIntersection) :
    letI : MonoidalCategoryStruct (ModuleCat.{u} R) :=
      ModuleCat.liftedModuleMonoidalStruct.{u, u}
    letI : MonoidalCategory (ModuleCat.{u} R) :=
      ModuleCat.liftedModuleMonoidal.{u, u}
    let R₀ := (DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
      (MonoidalCategoryStruct.tensorUnit (ModuleCat.{u} R))
    Nonempty (p.upperShriekFunctor.{u, u} ≅
      derivedTensorProductOver.{u, u} f (p.upperShriekFunctor.{u, u}.obj R₀))
```

## Tag 0E4C, a lemma

[Tag 0E4C](https://stacks.math.columbia.edu/tag/0E4C) in the Stacks Project.

**`Dualizing.isGorensteinRing_fiber_iff_isInvertible_upperShriekFunctor_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/GorensteinFibres.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/GorensteinFibres.lean#L379).

> **Stacks Project, Tag 0E4C.**  Let `φ : R → A` be a flat homomorphism of finite type of
> Noetherian rings.  Then the fibres `A ⊗_R κ(q)` are Gorenstein for every prime `q ⊆ R` if and
> only if the relative dualizing complex `ω^•_{A/R} = φ^!(R)` is an invertible object of `D(A)`.
>
> The statement is made for an arbitrary polynomial presentation `p` of `φ`, so it holds for every
> model of `φ^!`.

```lean
theorem isGorensteinRing_fiber_iff_isInvertible_upperShriekFunctor_unit
    {R A : Type u} [CommRing R] [CommRing A] [IsNoetherianRing R] [IsNoetherianRing A]
    [Algebra R A] [Module.Flat R A] (p : PolynomialPresentation (algebraMap R A)) :
    letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory A).choose
    (∀ (q : Ideal R) [q.IsPrime], letI := isNoetherianRing_baseChange q.ResidueField p
        IsGorensteinRing (q.Fiber A)) ↔
      MonoidalCategory.IsInvertible
        (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)))
```

## Tag 0E9N, a lemma

[Tag 0E9N](https://stacks.math.columbia.edu/tag/0E9N) in the Stacks Project.

**`Dualizing.PolynomialPresentation.upperShriekFunctor_localization_isNormalizedDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Normalized.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/Normalized.lean#L421).

> Let `φ : R → A` be a finite type homomorphism of Noetherian rings with `R` local, and let
> `m ⊆ A` be a maximal ideal lying over the maximal ideal of `R`.  If `ω_R` is a normalized
> dualizing complex for `R`, then `φ^!(ω_R)_m` is a normalized dualizing complex for `A_m`, for
> every polynomial presentation of `φ`.

```lean
theorem PolynomialPresentation.upperShriekFunctor_localization_isNormalizedDualizingComplex
    {R A : Type u} [CommRing R] [CommRing A] [IsNoetherianRing R] [IsNoetherianRing A]
    [IsLocalRing R] {f : R →+* A} (p : PolynomialPresentation f)
    (m : Ideal A) [m.IsMaximal] (hlies : m.comap f = IsLocalRing.maximalIdeal R)
    (K : DerivedCategory (ModuleCat.{u} R)) (hK : IsNormalizedDualizingComplex.{u, u} K) :
    IsNormalizedDualizingComplex.{u, u}
      ((StacksDraft.PseudoCoherence.derivedExtensionScalars
        (algebraMap A (Localization.AtPrime m))).obj (p.upperShriekFunctor.{u, u}.obj K))
```

## Tag 0E9P, a lemma

[Tag 0E9P](https://stacks.math.columbia.edu/tag/0E9P) in the Stacks Project.

**`Dualizing.upperShriekFunctor_neg_relativeDimensionAt_le_of_nontrivial_localizedHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/FibreDimensionBound.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/FibreDimensionBound.lean#L422). The attribute's comment: “for the upper shriek functor of an arbitrary polynomial presentation of the homomorphism, the relative dualizing complex being well defined only up to isomorphism, and with the fibre dimension named by a hypothesis identifying it with a natural number”.

> **[Stacks, Tag 0E9P].** Let `R → A` be a finite type homomorphism of Noetherian rings, let
> `𝔮 ⊂ A` be a prime and let `d` be the dimension at `𝔮` of the fibre of `Spec(A) → Spec(R)` over
> the prime below `𝔮`.  If the localization at `𝔮` of `H^i(ω^•_{A/R})` is nonzero then `-d ≤ i`.
> Here `ω^•_{A/R} = f^!(R)` is computed from an arbitrary polynomial presentation of `f`.

```lean
theorem upperShriekFunctor_neg_relativeDimensionAt_le_of_nontrivial_localizedHomology
    {R A : Type u} [CommRing R] [CommRing A] [IsNoetherianRing R] [IsNoetherianRing A]
    [Algebra R A] (p : PolynomialPresentation (algebraMap R A))
    (q : PrimeSpectrum A) (d : ℕ)
    (hd : Algebra.relativeDimensionAt R q.asIdeal = (d : WithBot ℕ∞)) (i : ℤ) :
    Nontrivial
        (LocalizedModule q.asIdeal.primeCompl
          ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
            (p.upperShriekFunctor.{u, 0}.obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
                (ModuleCat.of R R))))) →
      -(d : ℤ) ≤ i
```

## Tag 0E9Q, a lemma

[Tag 0E9Q](https://stacks.math.columbia.edu/tag/0E9Q) in the Stacks Project.

**`Dualizing.upperShriekFunctor_relativeDimensionAt_bounds_of_nontrivial_localizedHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/FibreDimensionBoundUpper.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/FibreDimensionBoundUpper.lean#L238). The attribute's comment: “the local bounds: H^i(omega)\_q nonzero implies -d <= i <= 0, d the dimension at q of the fibre through q, for the upper shriek functor of an arbitrary polynomial presentation of the homomorphism, the relative dualizing complex being well defined only up to isomorphism; the Tor amplitude clause is Dualizing.upperShriekFunctor\_hasTorAmplitude\_of\_fiber\_dimension\_le”.

> **[Stacks, Tag 0E9Q], the local bounds.** Let `R → A` be a flat finite type homomorphism of
> Noetherian rings, let `𝔮 ⊂ A` be a prime and let `d` be the dimension at `𝔮` of the fibre of
> `Spec(A) → Spec(R)` over the prime below `𝔮`.  If the localization at `𝔮` of `H^i(ω^•_{A/R})` is
> nonzero then `-d ≤ i ≤ 0`.  Here `ω^•_{A/R} = f^!(R)` is computed from an arbitrary polynomial
> presentation of `f`.

```lean
theorem upperShriekFunctor_relativeDimensionAt_bounds_of_nontrivial_localizedHomology
    {R A : Type u} [CommRing R] [IsNoetherianRing R] [CommRing A] [IsNoetherianRing A]
    [Algebra R A] [Module.Flat R A] (p : PolynomialPresentation (algebraMap R A))
    (q : PrimeSpectrum A) (d : ℕ)
    (hd : Algebra.relativeDimensionAt R q.asIdeal = (d : WithBot ℕ∞)) (i : ℤ) :
    Nontrivial
        (LocalizedModule q.asIdeal.primeCompl
          ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
            (p.upperShriekFunctor.{u, 0}.obj
              ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
                (ModuleCat.of R R))))) →
      -(d : ℤ) ≤ i ∧ i ≤ 0
```

**`Dualizing.upperShriekFunctor_hasTorAmplitude_of_fiber_dimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingTorAmplitude.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingTorAmplitude.lean#L505). The attribute's comment: “the Tor amplitude clause: if all fibres of Spec(A) -> Spec(R) have dimension at most d then the relative dualizing complex has Tor amplitude in [-d, 0] over R; the relative dualizing complex is read at the upper shriek functor of an arbitrary polynomial presentation of the homomorphism, being well defined only up to isomorphism”.

> **[Stacks, Tag 0E9Q], the Tor amplitude clause.**  Let `R → A` be a flat finite type
> homomorphism of Noetherian rings.  If all fibres of `Spec(A) → Spec(R)` have dimension at most
> `d`, then `ω^•_{A/R}` has Tor amplitude in `[-d, 0]` as a complex of `R`-modules.
>
> Here `ω^•_{A/R} = f^!(R)` is read at an arbitrary polynomial presentation of `R → A`, being
> defined only up to isomorphism, and Tor amplitude is read at the canonical certified derived
> tensor product of `R`.  Nothing is carried.  Following the source, the Tor test at a finitely
> presented module `M` is the cohomology of `ω^•_{A/R} ⊗_R^L (R ⊕ M)`, a base change to a Noetherian
> ring whose fibres have dimension at most `d`: that is
> `Dualizing.isZero_homology_totalDerivedExtensionScalars_upperShriekFunctor_of_lt`, proved by
> computing the base change on a finite projective resolution of `A` over the polynomial algebra,
> which needs no comparison of `A`-linear structures; arbitrary modules are filtered colimits of
> finitely presented ones.

```lean
theorem upperShriekFunctor_hasTorAmplitude_of_fiber_dimension_le
    {R A : Type u} [CommRing R] [CommRing A] [IsNoetherianRing R] [IsNoetherianRing A]
    [Algebra R A] [Module.Flat R A] (p : PolynomialPresentation (algebraMap R A)) (d : ℕ)
    (hd : ∀ 𝔭 : AlgebraicGeometry.Spec (.of R),
      topologicalKrullDim ((AlgebraicGeometry.Spec.map
        (CommRingCat.ofHom (algebraMap R A))).fiber 𝔭) ≤ (d : WithBot ℕ∞)) :
    StacksDraft.TorAmplitude.HasTorAmplitude
      (StacksDraft.TorAmplitude.canonicalCertifiedDerivedTensoring R).tensor
      (StacksDraft.TorAmplitude.canonicalCertifiedDerivedTensoring R).comparison
      (StacksDraft.TorAmplitude.canonicalCertifiedDerivedTensoring R).isLeftDerived
      ((ModuleCat.restrictScalars (algebraMap R A)).mapDerivedCategory.obj
        (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))))
      (-(d : ℤ)) 0
```

## Tag 0E9R, a lemma

[Tag 0E9R](https://stacks.math.columbia.edu/tag/0E9R) in the Stacks Project.

**`Dualizing.le_of_nontrivial_localizedModule_homology_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingCohenMacaulay.lean, line 813](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingCohenMacaulay.lean#L813). The attribute's comment: “the vanishing H^i(ω\_\{A/R})\_𝔭 = 0 for i < -r, in full”.

> **[Stacks, Tag 0E9R], the vanishing.**  Let `R → A` be a finite type homomorphism of
> Noetherian rings and let `𝔭 ⊂ R` be a prime.  Assume that `R_𝔭` is Cohen--Macaulay and that
> `trdeg_{κ(R ∩ 𝔮)} κ(𝔮) ≤ r` for every minimal prime `𝔮 ⊂ A`.  Then
>
> `H^i(ω^•_{A/R})_𝔭 ≠ 0 ⟹ -r ≤ i` .
>
> Here `ω^•_{A/R} = φ^!(R)` is the relative dualizing complex, computed from an arbitrary polynomial
> presentation `p` of `R → A` (it is well defined only up to isomorphism, so the statement is made
> for every presentation), and the localization at `𝔭` is the localization of the `A`-module at the
> image of `R ∖ 𝔭`.
>
> The proof does not go through a dualizing complex of `R_𝔭`.  At a prime `𝔮 ⊂ A` over a prime
> contained in `𝔭`, the localization of `H^i(ω^•_{A/R})` is `Ext^{i+n}_{P_𝔯}(A_𝔯, P_𝔯)`, where
> `P_𝔯` is Cohen--Macaulay and `depth_{I}(P_𝔯) ≥ n - r` by the dimension formula; see
> `Dualizing.subsingleton_and_min_two_le_moduleDepth_localizedModule_homology_upperShriek`.

```lean
theorem le_of_nontrivial_localizedModule_homology_relativeDualizingComplex
    {R A : Type u} [CommRing R] [CommRing A] [IsNoetherianRing R] [IsNoetherianRing A]
    [Algebra R A] (p : PolynomialPresentation (algebraMap R A)) (𝔭 : Ideal R) [𝔭.IsPrime]
    (hCM : IsCohenMacaulayLocalRing (Localization.AtPrime 𝔭)) (r : ℕ)
    (htrdeg : ∀ (q : Ideal A) [q.IsPrime], q ∈ minimalPrimes A →
      letI := Ideal.ResidueField.algebraOfLiesOver (q.under R) q
      Algebra.trdeg (q.under R).ResidueField q.ResidueField ≤ r)
    (i : ℤ) :
    Nontrivial (LocalizedModule (Submonoid.map (algebraMap R A) 𝔭.primeCompl)
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
        (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))))) →
      -(r : ℤ) ≤ i
```

**`Dualizing.propertySkModule_localizedModule_homology_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingCohenMacaulay.lean, line 847](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingCohenMacaulay.lean#L847). The attribute's comment: “the (S\_2) clause, H^\{-r}(ω\_\{A/R})\_𝔭 is (S\_2) as an A\_𝔭-module, in full”.

> **[Stacks, Tag 0E9R], the `(S₂)` clause.**  Let `R → A` be a finite type homomorphism of
> Noetherian rings and let `𝔭 ⊂ R` be a prime.  Assume that `R_𝔭` is Cohen--Macaulay and that
> `trdeg_{κ(R ∩ 𝔮)} κ(𝔮) ≤ r` for every minimal prime `𝔮 ⊂ A`.  Then `H^{-r}(ω^•_{A/R})_𝔭`
> satisfies Serre's condition `(S₂)` as an `A_𝔭`-module, where `A_𝔭` is the localization of `A` at
> the image of `R ∖ 𝔭`.
>
> As in `Dualizing.le_of_nontrivial_localizedModule_homology_relativeDualizingComplex`,
> `ω^•_{A/R} = φ^!(R)` is computed from an arbitrary polynomial presentation `p`. At a prime `𝔮`
> of `A_𝔭`, the module is `Ext^{n-r}_{P_𝔯}(A_𝔯, P_𝔯)` with `P_𝔯` Cohen--Macaulay and
> `n - r ≤ depth_I(P_𝔯)`, and such an `Ext` satisfies `(S₂)`
> (`Dualizing.min_two_le_moduleDepth_ext_of_le_depth`).

```lean
theorem propertySkModule_localizedModule_homology_relativeDualizingComplex
    {R A : Type u} [CommRing R] [CommRing A] [IsNoetherianRing R] [IsNoetherianRing A]
    [Algebra R A] (p : PolynomialPresentation (algebraMap R A)) (𝔭 : Ideal R) [𝔭.IsPrime]
    (hCM : IsCohenMacaulayLocalRing (Localization.AtPrime 𝔭)) (r : ℕ)
    (htrdeg : ∀ (q : Ideal A) [q.IsPrime], q ∈ minimalPrimes A →
      letI := Ideal.ResidueField.algebraOfLiesOver (q.under R) q
      Algebra.trdeg (q.under R).ResidueField q.ResidueField ≤ r) :
    letI : Module.Finite A ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(r : ℤ))).obj
        (p.upperShriekFunctor.{u, 0}.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)))) :=
      finite_homology_upperShriekFunctor p _
    PropertySkModule (Localization (Submonoid.map (algebraMap R A) 𝔭.primeCompl))
      (LocalizedModule (Submonoid.map (algebraMap R A) 𝔭.primeCompl)
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(r : ℤ))).obj
          (p.upperShriekFunctor.{u, 0}.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))))) 2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.25, Tag 0E9M](https://stacks.math.columbia.edu/tag/0E9M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
