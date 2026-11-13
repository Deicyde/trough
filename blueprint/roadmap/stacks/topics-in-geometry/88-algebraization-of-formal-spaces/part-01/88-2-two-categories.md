---
declaration: section
origin: cited
lean: Rig.AdicAlgebraSystem, Rig.AdicFiniteTypeAlgebra, Rig.adicQuotientFunctor, Rig.exists_adicCompletion_mvPolynomial_quotient_equiv, Rig.iAdicallyCompleteRing_adicCompletion_mvPolynomial, Rig.finiteType_quotient_adicCompletion_mvPolynomial, Rig.adicQuotientEquivalence, Rig.isNoetherianRing
statement: formalized
proof: formalized
---

# 88.2 Two categories

Section 88.2 of the Stacks Project, [Tag 0AL2](https://stacks.math.columbia.edu/tag/0AL2). 8 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AL3, an equation

[Tag 0AL3](https://stacks.math.columbia.edu/tag/0AL3) in the Stacks Project.

**`Rig.AdicAlgebraSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean#L54).

> The category of inverse systems `… → B₃ → B₂ → B₁` in which `Bₙ` is a finite
> type `A ⧸ I ^ n`-algebra and each transition identifies its target with reduction of its
> source modulo `I ^ n`.  The Lean index `n` represents the mathematical index `n + 1`.

```lean
structure AdicAlgebraSystem (A : Type u) [CommRing A] (I : Ideal A)
```

## Tag 0AL4, an equation

[Tag 0AL4](https://stacks.math.columbia.edu/tag/0AL4) in the Stacks Project.

**`Rig.AdicFiniteTypeAlgebra`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/CompletedBaseChange.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/CompletedBaseChange.lean#L46).

> The category of `I`-adically complete `A`-algebras whose reduction modulo `I` is of
> finite type over `A ⧸ I`.

```lean
public abbrev AdicFiniteTypeAlgebra (A : Type u) [CommRing A] (I : Ideal A)
```

## Tag 0AJN, an equation

[Tag 0AJN](https://stacks.math.columbia.edu/tag/0AJN) in the Stacks Project.

**`Rig.adicQuotientFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean#L461).

> The functor which associates to an adically complete algebra `B` its inverse system
> of quotients
> `B ⧸ (I.map (algebraMap A B)) ^ (n + 1)`.
>
> Its transition maps are the canonical quotient maps, and its action on morphisms is induced
> by the underlying `A`-algebra maps.

```lean
public noncomputable def adicQuotientFunctor (A : Type u) [CommRing A]
    (I : Ideal A) :
    AdicFiniteTypeAlgebra.{u, v} A I ⥤
      AdicAlgebraSystem.{u, v} A I
```

## Tag 0AJP, a lemma

[Tag 0AJP](https://stacks.math.columbia.edu/tag/0AJP) in the Stacks Project.

**`Rig.exists_adicCompletion_mvPolynomial_quotient_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean#L77). The attribute's comment: “completed\_polynomial\_presentation”.

> **Stacks Project, Tag 0AJP.** An adically complete algebra of finite type modulo a
> finitely generated ideal is a quotient of a completed polynomial algebra in finitely many
> variables.

```lean
public theorem exists_adicCompletion_mvPolynomial_quotient_equiv
    {A : Type u} [CommRing A] (I : Ideal A) (hI : I.FG)
    (B : AdicFiniteTypeAlgebra.{u, v} A I) :
    ∃ r : ℕ,
      let P := AdicCompletion
        (I.map (MvPolynomial.C : A →+* MvPolynomial (Fin r) A))
        (MvPolynomial (Fin r) A)
    ∃ J : Ideal P, Nonempty ((P ⧸ J) ≃ₐ[A] B.carrier)
```

**`Rig.iAdicallyCompleteRing_adicCompletion_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean#L275). The attribute's comment: “polynomial\_completions”.

> The completion of a polynomial algebra is complete for the ideal extended
> from the coefficient ring.

```lean
public theorem iAdicallyCompleteRing_adicCompletion_mvPolynomial (hI : I.FG) :
    IsAdicComplete (I.map (algebraMap A
        (AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
          (MvPolynomial (Fin r) A))))
      (AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
        (MvPolynomial (Fin r) A))
```

**`Rig.finiteType_quotient_adicCompletion_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean#L292). The attribute's comment: “polynomial\_completions”.

> The reduction modulo `I` of a completed polynomial algebra is of finite
> type over `A ⧸ I`.

```lean
public theorem finiteType_quotient_adicCompletion_mvPolynomial (hI : I.FG) :
    Algebra.FiniteType (A ⧸ I)
      ((AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
          (MvPolynomial (Fin r) A)) ⧸
        I.map (algebraMap A
          (AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
            (MvPolynomial (Fin r) A))))
```

**`Rig.adicQuotientEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/CategoryLimit.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/CategoryLimit.lean#L570). The attribute's comment: “the functor (Bₙ) ↦ lim Bₙ is a quasi-inverse of the functor of 0AJN, so the two categories are equivalent”.

> **Stacks Project, Tag 0AJP.** The functor `(Bₙ) ↦ lim Bₙ` from systems of finite type
> algebras over the quotients `A ⧸ Iⁿ` to adically complete algebras of finite type modulo `I` is
> quasi-inverse to the functor `B ↦ (B ⧸ Iⁿ⁺¹B)` of [StacksProject 0AJN]: the two categories are
> equivalent.

```lean
public noncomputable def adicQuotientEquivalence (hI : I.FG) :
    AdicFiniteTypeAlgebra.{u, v} A I ≌ AdicAlgebraSystem.{u, v} A I
```

## Tag 0AJQ, a lemma

[Tag 0AJQ](https://stacks.math.columbia.edu/tag/0AJQ) in the Stacks Project.

**`Rig.isNoetherianRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean#L190). The attribute's comment: “noetherian\_objects”.

> Every adically complete algebra of finite type modulo an ideal over a Noetherian
> commutative ring has a Noetherian underlying ring.

```lean
public instance isNoetherianRing {A : Type u} [CommRing A] [IsNoetherianRing A]
    {I : Ideal A} (B : AdicFiniteTypeAlgebra.{u, v} A I) :
    IsNoetherianRing B.carrier
```

**`Rig.quotient_isAdicFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean#L229). The attribute's comment: “quotients\_remain\_objects”.

> Every quotient of an adically complete algebra of finite type modulo an ideal over a
> Noetherian ring is again an adically complete algebra of finite type modulo that ideal.

```lean
public theorem quotient_isAdicFiniteType {A : Type u} [CommRing A] [IsNoetherianRing A]
    {I : Ideal A} (B : AdicFiniteTypeAlgebra.{u, v} A I)
    (J : Ideal B.carrier) :
    IsAdicComplete (I.map (algebraMap A (B.carrier ⧸ J))) (B.carrier ⧸ J) ∧
      Algebra.FiniteType (A ⧸ I)
        ((B.carrier ⧸ J) ⧸ I.map (algebraMap A (B.carrier ⧸ J)))
```

**`Rig.iAdicallyCompleteRing_adicCompletion_mvPolynomial_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean#L322). The attribute's comment: “polynomial\_completions”.

> The completion of the polynomial ring in `r` variables over a Noetherian ring is
> complete for the ideal extended from the coefficient ring.

```lean
public theorem iAdicallyCompleteRing_adicCompletion_mvPolynomial_of_isNoetherianRing :
    IsAdicComplete
      (I.map (algebraMap A
        (AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
          (MvPolynomial (Fin r) A))))
      (AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
        (MvPolynomial (Fin r) A))
```

**`Rig.finiteType_quotient_adicCompletion_mvPolynomial_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/PolynomialPresentation.lean#L334). The attribute's comment: “polynomial\_completions”.

> The reduction modulo `I` of the completed polynomial ring in `r` variables is of
> finite type over `A ⧸ I`.

```lean
public theorem finiteType_quotient_adicCompletion_mvPolynomial_of_isNoetherianRing :
    Algebra.FiniteType (A ⧸ I)
      ((AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
          (MvPolynomial (Fin r) A)) ⧸
        I.map (algebraMap A
          (AdicCompletion (I.map (algebraMap A (MvPolynomial (Fin r) A)))
            (MvPolynomial (Fin r) A))))
```

**`Rig.adicCompletion_isAdicallyComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FiniteTypeCompletions.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FiniteTypeCompletions.lean#L37). The attribute's comment: “finite\_type\_completions”.

> The completion of a finite type algebra over a Noetherian ring is complete for the ideal
> extended directly from the base ring.

```lean
public theorem adicCompletion_isAdicallyComplete
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (C : Type v) [CommRing C] [Algebra A C] [Algebra.FiniteType A C] :
    IsAdicComplete
      (I.map (algebraMap A (AdicCompletion (I.map (algebraMap A C)) C)))
      (AdicCompletion (I.map (algebraMap A C)) C)
```

**`Rig.adicCompletion_finiteType_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FiniteTypeCompletions.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/FiniteTypeCompletions.lean#L54). The attribute's comment: “finite\_type\_completions”.

> The quotient modulo the ideal from the base ring of the completion of a finite type algebra
> is of finite type over the quotient of the base ring.

```lean
public theorem adicCompletion_finiteType_quotient
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (C : Type v) [CommRing C] [Algebra A C] [Algebra.FiniteType A C] :
    Algebra.FiniteType (A ⧸ I)
      ((AdicCompletion (I.map (algebraMap A C)) C) ⧸
        I.map (algebraMap A (AdicCompletion (I.map (algebraMap A C)) C)))
```

## Tag 0AL5, a remark

[Tag 0AL5](https://stacks.math.columbia.edu/tag/0AL5) in the Stacks Project.

**`Rig.adicBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/BaseChange.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/BaseChange.lean#L632).

> **Stacks Project, Tag 0AL5.** Let `A₁ → A₂` be a ring map and `I₁ ⊆ A₁`, `I₂ ⊆ A₂` ideals
> with `I₁ ^ c` mapping into `I₂` for some `c ≥ 1`. This induces ring maps
> `A₁ ⧸ I₁ ^ (cn) → A₂ ⧸ I₂ ^ n`, and there is a base change functor `(Bₙ) ↦ (B_{cn} ⊗ A₂ ⧸ I₂ ^ n)`
> between the categories of systems. If `I₂` is finitely generated there is a base change functor
> `B ↦ (B ⊗[A₁] A₂)^` between the categories of complete algebras, and if both ideals are
> finitely generated the two base change functors agree via the equivalences `B ↦ (B ⧸ IⁿB)ₙ`.

```lean
public noncomputable def adicBaseChange :
    AdicBaseChange.{v, u₁, u₂} A₁ A₂ I₁ I₂ hc hmap
```

## Tag 0AK0, an equation

[Tag 0AK0](https://stacks.math.columbia.edu/tag/0AK0) in the Stacks Project.

**`Rig.completedBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/CompletedBaseChange.lean, line 758](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/CompletedBaseChange.lean#L758).

> **Stacks Project, Tag 0AK0.** If a positive power of `I₁` maps into the finitely generated
> ideal `I₂`, then `B ↦ (B ⊗[A₁] A₂)⁁` is a functor between the categories of adically complete
> algebras of finite type modulo `I₁` and `I₂`.

```lean
public noncomputable def completedBaseChange (I₁ : Ideal A₁) (I₂ : Ideal A₂) (c : ℕ)
    (hc : 0 < c) (hmap : (I₁ ^ c).map (algebraMap A₁ A₂) ≤ I₂) (hI₂ : I₂.FG) :
    CompletedBaseChange (A₁ := A₁) (A₂ := A₂) (I₁ := I₁) (I₂ := I₂)
```

## Tag 0AL6, a remark

[Tag 0AL6](https://stacks.math.columbia.edu/tag/0AL6) in the Stacks Project.

**`Rig.quotient_isAdicallyComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean#L174). The attribute's comment: “the quotient is complete”.

> The quotient of an adically finite type algebra by an ideal from the base is
> complete for every ideal defining the induced adic topology.

```lean
public theorem quotient_isAdicallyComplete
    (hc : 0 < c) (hd : 0 < d)
    (hI : (I ^ c).map (Ideal.Quotient.mk a) ≤ barI)
    (hbarI : barI ^ d ≤ I.map (Ideal.Quotient.mk a))
    (B : AdicFiniteTypeAlgebra.{u, v} A I) :
    IsAdicComplete (barI.map (algebraMap (A ⧸ a)
        (B.carrier ⧸ a.map (algebraMap A B.carrier))))
      (B.carrier ⧸ a.map (algebraMap A B.carrier))
```

**`Rig.tensor_quotient_completion_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean#L205). The attribute's comment: “completed base change is the quotient”.

> The canonical map from the tensor-product presentation of the quotient algebra
> to its `barI`-adic completion is an isomorphism.

```lean
public theorem tensor_quotient_completion_bijective
    (hc : 0 < c) (hd : 0 < d)
    (hI : (I ^ c).map (Ideal.Quotient.mk a) ≤ barI)
    (hbarI : barI ^ d ≤ I.map (Ideal.Quotient.mk a))
    (B : AdicFiniteTypeAlgebra.{u, v} A I) :
    Function.Bijective
      (AdicCompletion.of
        (baseChangedIdeal (A₂ := A ⧸ a) (I₂ := barI) B)
        (baseChangedAlgebra (A₂ := A ⧸ a) B))
```

**`Rig.quotientBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/Category/AdicAlgebraSystem.lean#L242). The attribute's comment: “the quotient functor and its natural comparison”.

> Base change to a closed subscheme is the quotient functor. The isomorphism to
> completed base change is the canonical completion map, and quotienting a morphism
> acts by quotienting its underlying algebra homomorphism.

```lean
public theorem quotientBaseChange
    (hc : 0 < c) (hd : 0 < d)
    (hI : (I ^ c).map (Ideal.Quotient.mk a) ≤ barI)
    (hbarI : barI ^ d ≤ I.map (Ideal.Quotient.mk a)) :
    ∃ (Q : AdicFiniteTypeAlgebra.{u, v} A I ⥤
        AdicFiniteTypeAlgebra.{u, max v u} (A ⧸ a) barI),
      ∃ (η : Q ≅
          (completedBaseChange (A₁ := A) (A₂ := A ⧸ a)
            I barI c hc hI (Ideal.fg_of_isNoetherianRing barI)).functor),
        ∃ (e : ∀ B : AdicFiniteTypeAlgebra.{u, v} A I,
            (Q.obj B).carrier ≃+* (B.carrier ⧸ a.map (algebraMap A B.carrier))),
          (∀ (B : AdicFiniteTypeAlgebra.{u, v} A I) (x : B.carrier),
            ((completedBaseChange (A₁ := A) (A₂ := A ⧸ a)
              I barI c hc hI (Ideal.fg_of_isNoetherianRing barI)).completedTensorProductEquiv B)
                (AdicFiniteTypeAlgebra.hom (η.hom.app B)
                  ((e B).symm (Ideal.Quotient.mk (a.map (algebraMap A B.carrier)) x))) =
              AdicCompletion.of
                (baseChangedIdeal (A₂ := A ⧸ a) (I₂ := barI) B)
                (baseChangedAlgebra (A₂ := A ⧸ a) B)
                ((Algebra.TensorProduct.quotIdealMapEquivTensorQuot B.carrier a)
                  (Ideal.Quotient.mk (a.map (algebraMap A B.carrier)) x))) ∧
          (∀ {B C : AdicFiniteTypeAlgebra.{u, v} A I} (f : B ⟶ C) (x : B.carrier),
            e C (AdicFiniteTypeAlgebra.hom (Q.map f)
              ((e B).symm (Ideal.Quotient.mk (a.map (algebraMap A B.carrier)) x))) =
              Ideal.Quotient.mk (a.map (algebraMap A C.carrier))
                  (AdicFiniteTypeAlgebra.hom f x))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.2, Tag 0AL2](https://stacks.math.columbia.edu/tag/0AL2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
