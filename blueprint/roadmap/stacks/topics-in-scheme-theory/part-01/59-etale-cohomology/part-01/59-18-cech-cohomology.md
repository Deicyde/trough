---
declaration: section
origin: cited
lean: Stacks.CechSite.cechComplex, Stacks.CechSite.cechCohomology, Stacks.CechSite.cechComplexFunctor_exact, CategoryTheory.yonedaEquiv, CategoryTheory.yonedaLemma, PresheafOfModules.freeObj, Stacks.CechSite.homIntegralCechComplex_d, Stacks.CechSite.cechComplexIsoHomIntegralCechComplex
statement: formalized
proof: formalized
---

# 59.18 Čech cohomology

Section 59.18 of the Stacks Project, [Tag 03OK](https://stacks.math.columbia.edu/tag/03OK). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03OL, a definition

[Tag 03OL](https://stacks.math.columbia.edu/tag/03OL) in the Stacks Project.

**`Stacks.CechSite.cechComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean#L153). The attribute's comment: “the Čech complex of an abelian presheaf along a family with fixed target”. References: SGA 4 V (2.4.3), “Čech complex”.

> The Čech complex associated to an additive presheaf and a family of morphisms with fixed
> target whose finite nonempty fibre products exist.

```lean
noncomputable abbrev cechComplex
    {A : Type u'} [Category.{v'} A] [HasProducts.{w} A] [Preadditive A]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    (F : CategoryTheory.Functor Cᵒᵖ A) : CochainComplex A ℕ
```

**`Stacks.CechSite.cechCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean#L165). The attribute's comment: “the Čech cohomology groups, as the cohomology of the Čech complex”. References: SGA 4 V (2.4.3), “Čech cohomology of 𝒰”.

> The degree-`n` Čech cohomology object of a presheaf with respect to a family of morphisms
> with fixed target. For abelian-group-valued presheaves this is the Čech cohomology group.

```lean
noncomputable abbrev cechCohomology
    {A : Type u'} [Category.{v'} A] [HasProducts.{w} A] [Abelian A]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    (F : CategoryTheory.Functor Cᵒᵖ A) (n : ℕ) : A
```

## Tag 03OM, a lemma

[Tag 03OM](https://stacks.math.columbia.edu/tag/03OM) in the Stacks Project.

**`Stacks.CechSite.cechComplexFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexExactnessOnAbelianPresheaves.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexExactnessOnAbelianPresheaves.lean#L70).

> **Stacks Project, Tag 03OM.** The Čech complex functor of Stacks 03OL is exact on the
> category `PAb(C)` of abelian presheaves on `C`.

```lean
theorem cechComplexFunctor_exact
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))] :
    exactFunctor
      (CategoryTheory.Functor Cᵒᵖ AddCommGrpCat.{max w uAb})
      (CochainComplex AddCommGrpCat.{max w uAb} ℕ)
      (cechComplexFunctor (A := AddCommGrpCat.{max w uAb}) E)
```

## Tag 03ON, a lemma

[Tag 03ON](https://stacks.math.columbia.edu/tag/03ON) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.yonedaEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.yonedaEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L315) (StacksFrontier): “the bijection”. References: EGA 0 (8.1.3); EGA 0 (8.1.4); EGA 0 (8.1.6), “more general”; EGA 0 (8.1.8), “partial, special case”; SGA 3 I (1.1); SGA 3 I (1.1.1), “more general”; SGA 3 I (1.6.1), “Hom(h_S, F) ≃ F(S)”; SGA 3 I (1.7.0), “partial”; SGA 3 IV (4.3.1), “partial”; SGA 4 I (1.4), “bijection Hom(h(X)”; SGA 4 I (8.3.2), “partial”.
- [`CategoryTheory.yonedaLemma`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.yonedaLemma#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L316) (StacksFrontier): “functoriality”. References: EGA 0 (8.1.4); SGA 3 I (1.1); SGA 3 VIIB (0.4.2), “more general”; SGA 4 I (1.4).

## Tag 03OO, a definition

[Tag 03OO](https://stacks.math.columbia.edu/tag/03OO) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.freeObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.freeObj#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L155) (StacksFrontier): “Z_G(U) = Z[G(U)]: the free presheaf of modules on G, over the constant presheaf of rings Z (Z_U is the case G = h_U)”.

## Tag 03OP, a lemma

[Tag 03OP](https://stacks.math.columbia.edu/tag/03OP) in the Stacks Project.

**`Stacks.CechSite.homIntegralCechComplex_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean#L118). The attribute's comment: “the differential”.

> **Stacks 03OP.** The differential of the complex of maps out of the integral Čech complex is
> the alternating sum of the maps induced by the face maps of the simplicial formal coproduct of
> fibre products, that is, of the maps which repeat one of the indices.

```lean
theorem homIntegralCechComplex_d (F : Cᵒᵖ ⥤ AddCommGrpCat.{max v a}) (n : ℕ) :
    ((homComplexFunctor (integralCechComplex.{w, v, u, a} E)).obj F).d n (n + 1) =
      ∑ j : Fin (n + 2), (-1 : ℤ) ^ (j : ℕ) •
        (preadditiveYoneda.obj F).map
          ((integralCechRealization.{w, v, u, a} (X := X)).map
            ((cechSimplicialObject E).δ j)).op
```

**`Stacks.CechSite.cechComplexIsoHomIntegralCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean#L140). The attribute's comment: “the identification of the Čech complex with maps out of the integral complex”.

> **Stacks 03OP.** The Čech complex of an abelian presheaf `F` is the complex of maps out of
> the integral Čech complex of Stacks 03OQ, naturally in `F`. This is the second of the two
> displays of 03OP, and it is the Hom identification of Stacks 03AS; the values of the Čech
> complex are lifted to the universe in which maps of abelian presheaves live.

```lean
noncomputable def cechComplexIsoHomIntegralCechComplex :
    liftedCechComplexFunctor.{w, v, u, a} E ≅
      homComplexFunctor (integralCechComplex.{w, v, u, a} E)
```

**`Stacks.CechSite.homIntegralCechComplexXIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean#L150). The attribute's comment: “the degreewise product of Hom-groups”.

> **Stacks 03OP.** The degree-`n` term of the complex of maps out of the integral Čech complex
> is the product, over `(n+1)`-tuples `i` of indices, of the groups of maps from the free abelian
> presheaf on the fibre product `U_{i 0} ×_U ⋯ ×_U U_{i n}` to `F`. This is the first of the two
> displays of 03OP.

```lean
noncomputable def homIntegralCechComplexXIso (F : Cᵒᵖ ⥤ AddCommGrpCat.{max v a}) (n : ℕ) :
    ((homComplexFunctor (integralCechComplex.{w, v, u, a} E)).obj F).X n ≅
      ((∏ᶜ (fun i : Fin (n + 1) → E.I₀ ↦ AddCommGrpCat.of
        (freeAbelianYoneda.{v, u, a}.obj ((∏ᶜ (fun b ↦ Over.mk (E.f (i b)))).left) ⟶ F)) :
          AddCommGrpCat.{max u v a}))
```

**`Stacks.CechSite.cechComplexIsoHomIntegralCechComplexObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexAsHomOutOfIntegralComplex.lean#L175). The attribute's comment: “the identification for the Čech complex itself”.

> **Stacks 03OP.** When the coefficient universe contains the universe of objects of `C`, so
> that the groups of maps of abelian presheaves lie in the coefficient universe too, the Čech
> complex of `F` itself -- and not merely a universe lift of it -- is the complex of maps out of
> the integral Čech complex.

```lean
noncomputable def cechComplexIsoHomIntegralCechComplexObj
    (F : Cᵒᵖ ⥤ AddCommGrpCat.{max u v a}) :
    cechComplex E F ≅
      (homComplexFunctor (integralCechComplex.{w, v, u, max u a} E)).obj F
```

## Tag 03OQ, a lemma

[Tag 03OQ](https://stacks.math.columbia.edu/tag/03OQ) in the Stacks Project.

**`Stacks.CechSite.integralCechComplex_homology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexIsAResolution.lean, line 1015](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/IntegralComplexIsAResolution.lean#L1015). References: SGA 4 V (1.11), “partial”.

> The homology presheaves of the integral Čech chain complex vanish in every positive degree:
> the complex of abelian presheaves is exact in all degrees except `0`. The degree-`0` term of
> `integralCechComplex` is `⊕_{i₀} Z_{U_{i₀}}`, so the hypothesis `0 < n` is exactly "all degrees
> except `0`", and nothing is asserted at `n = 0`.

```lean
public theorem integralCechComplex_homology_isZero (n : ℕ) (hn : 0 < n) :
    IsZero ((integralCechComplex.{w, v, u, a} E).homology n)
```

## Tag 03OR, a lemma

[Tag 03OR](https://stacks.math.columbia.edu/tag/03OR) in the Stacks Project.

**`Stacks.CechSite.injective_presheaf_cechCohomology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectivePresheafVanishing.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/InjectivePresheafVanishing.lean#L66).

> **Stacks Project, Tag 03OR.** The positive-degree Čech cohomology of an injective
> presheaf of abelian groups vanishes.

```lean
theorem injective_presheaf_cechCohomology_isZero (p : ℕ) (hp : 0 < p) :
    IsZero (cechCohomology E I p)
```

## Tag 03OS, a theorem

[Tag 03OS](https://stacks.math.columbia.edu/tag/03OS) in the Stacks Project.

**`Stacks.CechSite.cechCohomologyIsoRightDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean#L229). The attribute's comment: “the isomorphism in each degree”.

> **Stacks 03AU.** For each `n`, the natural isomorphism `ČH ⁿ(E, -) ≅ R ⁿ(ČH ⁰(E, -))` of
> functors on abelian presheaves.
>
> This is also [Stacks Project, Tag 03OS], the Étale Cohomology chapter's form of the same
> statement: on abelian presheaves the functors `Ȟ ᵖ(U, -)` are the right derived functors of
> `Ȟ ⁰(U, -)`.

```lean
noncomputable def cechCohomologyIsoRightDerived (n : ℕ) :
    cechComplexFunctor E ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{max w u v a} (ComplexShape.up ℕ) n ≅
      cechCohomologyRightDerived.{w, v, a, u} E n
```

**`Stacks.CechSite.existsUnique_cechCohomologyDeltaFunctorIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/RightDerivedOfDegreeZeroViaDeltaFunctors.lean#L304). The attribute's comment: “the delta-functor isomorphism”. References: SGA 7 VI (3.1(b)), “H^p = R^p H^0 of cover”.

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

- [Section 59.18, Tag 03OK](https://stacks.math.columbia.edu/tag/03OK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
