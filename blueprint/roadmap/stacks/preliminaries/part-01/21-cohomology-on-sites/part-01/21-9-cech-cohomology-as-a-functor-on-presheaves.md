---
declaration: section
origin: cited
lean: Stacks.CechSite.cechComplexPlusFunctor, Stacks.CechSite.cechComplexPlusFunctor_exact, Stacks.CechSite.cechCohomologyDeltaFunctor, Stacks.CechSite.integralCechComplex, Stacks.CechSite.integralCechComplex_X, Stacks.CechSite.integralCechComplex_d, Stacks.CechSite.homIntegralCechComplexIso, Stacks.CechSite.integralCechComplex_homology_isZero
statement: formalized
proof: formalized
---

# 21.9 Čech cohomology as a functor on presheaves

Section 21.9 of the Stacks Project, [Tag 03AO](https://stacks.math.columbia.edu/tag/03AO). 7 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03AP, an equation

[Tag 03AP](https://stacks.math.columbia.edu/tag/03AP) in the Stacks Project.

**`Stacks.CechSite.cechComplexPlusFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsBoundedBelowFunctor.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsBoundedBelowFunctor.lean#L51).

> **Stacks 03AP.** The Čech complex as a functor of the coefficient presheaf, with its
> nonnegative grading regarded canonically as a bounded-below integer grading.

```lean
public noncomputable def cechComplexPlusFunctor {A : Type u'} [Category.{v'} A]
    [HasProducts.{w} A] [Preadditive A] [HasZeroObject A]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀), HasProduct (fun a ↦ Over.mk (E.f (i a)))] :
    CategoryTheory.Functor (CategoryTheory.Functor Cᵒᵖ A) (CochainComplex.Plus A)
```

## Tag 03AQ, a lemma

[Tag 03AQ](https://stacks.math.columbia.edu/tag/03AQ) in the Stacks Project.

**`Stacks.CechSite.cechComplexPlusFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexExactness.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexExactness.lean#L61).

> Taking the bounded-below Čech complex of a presheaf of abelian groups is an exact functor.

```lean
theorem cechComplexPlusFunctor_exact
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] :
    exactFunctor
      (CategoryTheory.Functor Cᵒᵖ AddCommGrpCat.{max w uAb})
      (CochainComplex.Plus AddCommGrpCat.{max w uAb})
      (cechComplexPlusFunctor (A := AddCommGrpCat.{max w uAb}) E)
```

## Tag 03AR, a lemma

[Tag 03AR](https://stacks.math.columbia.edu/tag/03AR) in the Stacks Project.

**`Stacks.CechSite.cechCohomologyDeltaFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DeltaFunctor.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DeltaFunctor.lean#L63).

> The Čech cohomology functors of a family of morphisms with fixed target
> form a cohomological delta functor on abelian presheaves, whose `n`-th functor is the `n`-th
> Čech cohomology functor of Stacks 03AM.

```lean
public noncomputable def cechCohomologyDeltaFunctor
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun b ↦ Over.mk (E.f (i b)))] :
    { F : DeltaFunctor
        (CategoryTheory.Functor Cᵒᵖ AddCommGrpCat.{max w a}) AddCommGrpCat.{max w a} //
      ∀ n : ℕ, F.functor n = cechComplexFunctor E ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{max w a} (ComplexShape.up ℕ) n }
```

## Tag 03AS, a lemma

[Tag 03AS](https://stacks.math.columbia.edu/tag/03AS) in the Stacks Project.

**`Stacks.CechSite.integralCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean#L146). The attribute's comment: “the integral Čech complex”.

> The canonical integral Čech chain complex. Its degree `n` term is
> `\bigoplus_{i : Fin (n+1) → E.I₀} ℤ[U_i]`, with `U_i` the corresponding fibre
> product over `X`.

```lean
public noncomputable def integralCechComplex
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{max v a})]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] :
    ChainComplex (Cᵒᵖ ⥤ AddCommGrpCat.{max v a}) ℕ
```

**`Stacks.CechSite.integralCechComplex_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean#L156). The attribute's comment: “the terms of the integral Čech complex”.

> The degree-`n` term of the integral Čech complex is the indicated direct sum of
> free abelian representable presheaves.

```lean
public theorem integralCechComplex_X
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{max v a})]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] (n : ℕ) :
    (integralCechComplex.{w, v, u, a} E).X n =
      ∐ fun i : Fin (n + 1) → E.I₀ ↦
      freeAbelianYoneda.{v, u, a}.obj ((∏ᶜ (fun a ↦ Over.mk (E.f (i a)))).left)
```

**`Stacks.CechSite.integralCechComplex_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean#L167). The attribute's comment: “the differential of the integral Čech complex”.

> The differential of the integral Čech complex is the alternating sum of the canonical maps
> which omit one factor.

```lean
public theorem integralCechComplex_d
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{max v a})]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] (n : ℕ) :
    (integralCechComplex.{w, v, u, a} E).d (n + 1) n =
      ∑ j : Fin (n + 2), (-1 : ℤ) ^ (j : ℕ) •
      (integralCechSimplicialObject.{w, v, u, a} E).δ j
```

**`Stacks.CechSite.homIntegralCechComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplex.lean#L282). The attribute's comment: “the functorial Hom identification”.

> Mapping the integral Čech chain complex into an abelian presheaf is naturally isomorphic, as a
> cochain complex, to its Čech complex.

```lean
public noncomputable def homIntegralCechComplexIso
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{max v a})]
    [HasProducts.{w} AddCommGrpCat.{max u v a}]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] :
    homComplexFunctor (integralCechComplex.{w, v, u, a} E) ≅
      liftedCechComplexFunctor.{w, v, u, a} E
```

## Tag 03AT, a lemma

[Tag 03AT](https://stacks.math.columbia.edu/tag/03AT) in the Stacks Project.

**`Stacks.CechSite.integralCechComplex_homology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexIsAResolution.lean, line 1008](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexIsAResolution.lean#L1008). References: SGA 4 V (1.11), “partial”.

> The homology presheaves of the integral Čech chain complex vanish in every positive degree:
> the complex of abelian presheaves is exact in all degrees except `0`. The degree-`0` term of
> `integralCechComplex` is `⊕_{i₀} Z_{U_{i₀}}`, so the hypothesis `0 < n` is exactly "all degrees
> except `0`", and nothing is asserted at `n = 0`.

```lean
public theorem integralCechComplex_homology_isZero (n : ℕ) (hn : 0 < n) :
    IsZero ((integralCechComplex.{w, v, u, a} E).homology n)
```

## Tag 03F5, a lemma

[Tag 03F5](https://stacks.math.columbia.edu/tag/03F5) in the Stacks Project.

**`Stacks.CechSite.integralCechComplexTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean, line 826](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean#L826). The attribute's comment: “the tensor product presheaf complex”.

> The presheaf-of-`O`-modules complex obtained by tensoring the integral Čech
> complex with `O` over the constant integer presheaf.

```lean
public noncomputable def integralCechComplexTensor
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{v})]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] :
    IntegralCechComplexTensorSpec E O
```

**`Stacks.CechSite.integralCechComplexTensor_homology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean, line 868](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean#L868). The attribute's comment: “positive-degree exactness”.

> **Stacks Project, Tag 03F5.** Tensoring the integral Čech complex with a
> presheaf of rings leaves it exact in every positive degree.

```lean
public theorem integralCechComplexTensor_homology_isZero
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{v})]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    (n : ℕ) (hn : 0 < n) :
    IsZero ((integralCechComplexTensor E O).K.homology n)
```

**`Stacks.CechSite.integralCechComplexTensorRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean, line 927](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean#L927). The attribute's comment: “the tensor product presheaf complex”.

> The presheaf-of-`R`-modules complex obtained by tensoring the integral Čech
> complex with `R` over the constant integer presheaf.

```lean
public noncomputable def integralCechComplexTensorRing
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{v})]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] :
    ChainComplex (_root_.PresheafOfModules.{max v z} R) ℕ
```

**`Stacks.CechSite.integralCechComplexTensorRing_homology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean, line 953](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexFlatness.lean#L953). The attribute's comment: “positive-degree exactness”.

> **Stacks Project, Tag 03F5.** Tensoring the integral Čech complex with a
> presheaf of rings leaves it exact in every positive degree.

```lean
public theorem integralCechComplexTensorRing_homology_isZero
    [HasCoproducts.{w} (Cᵒᵖ ⥤ AddCommGrpCat.{v})]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    (n : ℕ) (hn : 0 < n) :
    IsZero ((integralCechComplexTensorRing E R).homology n)
```

## Tag 03AU, a lemma

[Tag 03AU](https://stacks.math.columbia.edu/tag/03AU) in the Stacks Project.

**`Stacks.CechSite.existsUnique_cechCohomologyIsoRightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZero.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZero.lean#L244). The attribute's comment: “the canonical δ-functor isomorphism”.

> **Stacks Project, Tag 03AU.** The Čech cohomology functors `Ȟ^p(E, -)` of a family of
> morphisms with fixed target are canonically isomorphic, as a cohomological `δ`-functor on
> abelian presheaves, to the right derived functors `R^p Ȟ⁰(E, -)` of degree-zero Čech cohomology.
>
> "Canonically" is the uniqueness clause: there is exactly one isomorphism of `δ`-functors whose
> degree-zero component is the canonical comparison `Ȟ⁰(E, -) ⟶ R⁰ Ȟ⁰(E, -)` of Stacks 05TD, and
> it is `Stacks.CechSite.cechCohomologyDeltaFunctorIsoRightDerived`.

```lean
theorem existsUnique_cechCohomologyIsoRightDerived :
    ∃! e : (cechCohomologyDeltaFunctor.{w, v, max u v a, u} E).1 ≅
        cechH0RightDerivedDeltaFunctor.{w, v, a, u} E,
      e.hom.app 0 = (cechH0IsoRightDerivedZero.{w, v, a, u} E).hom
```

**`Stacks.CechSite.cechComplexIsoRightDerivedFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZero.lean, line 922](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZero.lean#L922). The attribute's comment: “the functorial quasi-isomorphism”. References: SGA 7 VI (3.1(b)), “RH^0 = Čech complex”.

> **Stacks Project, Tag 03AU**, the functorial quasi-isomorphism. For any right derived
> functor `RȞ⁰(E, -) : D⁺(PAb(C)) ⥤ D⁺(Ab)` of degree-zero Čech cohomology, the Čech complex is
> isomorphic, functorially in the abelian presheaf, to `RȞ⁰(E, -)` applied to the presheaf placed
> in degree zero.
>
> The isomorphism is the span of [Stacks, Tag 03AU]: for an injective resolution `F → I^•`, both
> `Č^•(E, F) ⟶ Tot(Č^•(E, I^•))` and `Ȟ⁰(E, I^•) ⟶ Tot(Č^•(E, I^•))` are quasi-isomorphisms,
> the first because the Čech complex functor is exact (Stacks 03AQ) and the second because the
> higher Čech cohomology of an injective presheaf vanishes (Stacks 03OR).

```lean
def cechComplexIsoRightDerivedFunctor
    (RF : DerivedCategory.Plus (Cᵒᵖ ⥤ AddCommGrpCat.{max u v w a}) ⥤
      DerivedCategory.Plus AddCommGrpCat.{max u v w a})
    (α : (cechH0Functor.{w, v, a, u} E).mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh ⟶
      DerivedCategory.Plus.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.Plus.quasiIso (Cᵒᵖ ⥤ AddCommGrpCat.{max u v w a}))] :
    cechComplexPlusFunctor (A := AddCommGrpCat.{max u v w a}) E ⋙
        DerivedCategory.Plus.Q (C := AddCommGrpCat.{max u v w a}) ≅
      DerivedCategory.Plus.singleFunctor (Cᵒᵖ ⥤ AddCommGrpCat.{max u v w a}) 0 ⋙ RF
```

**`Stacks.CechSite.cechH0IsoRightDerivedPlusZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean#L273). The attribute's comment: “the degree-zero comparison”.

> **Stacks 03AU.** The degree-zero Čech cohomology functor is its own zeroth right derived
> functor, normalized by `H ⁰` of the unit of the right derived functor.

```lean
noncomputable def cechH0IsoRightDerivedPlusZero :
    { e : cechCohomologyZeroFunctor.{w, v, a, u} E ≅
        cechCohomologyRightDerivedPlus.{w, v, a, u} E 0 //
      e.hom = (cechH0RightDerivedPlusZeroIso.{w, v, a, u} E).inv }
```

**`Stacks.CechSite.rightDerivedCechDeltaFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean#L282). The attribute's comment: “the delta functor of higher right derived functors”.

> **Stacks 03AU.** The higher right derived functors of degree-zero Čech cohomology, equipped
> with their universal cohomological δ-functor structure.

```lean
noncomputable def rightDerivedCechDeltaFunctor :
    { R : DeltaFunctor (Cᵒᵖ ⥤ AddCommGrpCat.{max w u v a}) AddCommGrpCat.{max w u v a} //
      (∀ n : ℕ, R.functor n = cechCohomologyRightDerivedPlus.{w, v, a, u} E n) ∧
      R.IsUniversal }
```

**`Stacks.CechSite.existsUnique_cechCohomologyDeltaFunctorIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean#L304). The attribute's comment: “the canonical delta-functor isomorphism”. References: SGA 7 VI (3.1(b)), “H^p = R^p H^0 of cover”.

> **Stacks 03AU.** Čech cohomology is canonically isomorphic, as a cohomological δ-functor, to
> the higher right derived functors of degree-zero Čech cohomology. The isomorphism is unique with
> its prescribed degree-zero component.

```lean
theorem existsUnique_cechCohomologyDeltaFunctorIso :
    ∃! e : (cechCohomologyDeltaFunctor.{w, v, max u v a, u} E).1 ≅
        (rightDerivedCechDeltaFunctor.{w, v, a, u} E).1,
      e.hom.app 0 = (cechH0IsoRightDerivedPlusZero.{w, v, a, u} E).1.hom ≫
        eqToHom ((rightDerivedCechDeltaFunctor.{w, v, a, u} E).2.1 0).symm
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.9, Tag 03AO](https://stacks.math.columbia.edu/tag/03AO)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
