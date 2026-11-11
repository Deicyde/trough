---
declaration: section
origin: cited
lean: Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso, Dualizing.PolynomialPresentation.upperShriekFunctor_isBoundedBelow, Dualizing.PolynomialPresentation.upperShriekFunctor_derivedCategoryBPlus, Dualizing.upperShriekFunctor_isBoundedAbove_of_isPerfectRingMap, Dualizing.upperShriekFunctor_derivedCategoryBMinus_of_isPerfectRingMap, Dualizing.upperShriekFunctor_derivedCategoryBBounded_of_isPerfectRingMap, Dualizing.PolynomialPresentation.upperShriekFunctor_isDualizingComplex, Dualizing.PolynomialPresentation.isIso_upperShriekFlatBaseChange_app
statement: formalized
proof: formalized
---

# 47.24 Upper shriek algebraically

Section 47.24 of the Stacks Project, [Tag 0BZI](https://stacks.math.columbia.edu/tag/0BZI). 11 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BZJ, a lemma

[Tag 0BZJ](https://stacks.math.columbia.edu/tag/0BZJ) in the Stacks Project.

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/PolynomialEvalDualityProof.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/PolynomialEvalDualityProof.lean#L146).

> **Stacks 0BZJ.** The algebraic upper shriek functors attached to any two polynomial
> presentations of the same finite type homomorphism are naturally isomorphic, so `f^!` is well
> defined up to isomorphism.
>
> This is `Dualizing.PolynomialPresentation.upperShriekFunctor_iso` with its hypothesis `hBZH`
> supplied by `Dualizing.polynomialEvalDuality`.

```lean
theorem nonempty_upperShriekFunctor_iso {R A : Type u} [CommRing R] [CommRing A]
    (f : R →+* A) (p q : PolynomialPresentation f) :
    Nonempty (p.upperShriekFunctor.{u, v} ≅ q.upperShriekFunctor.{u, v})
```

## Tag 0BZK, a lemma

[Tag 0BZK](https://stacks.math.columbia.edu/tag/0BZK) in the Stacks Project.

**`Dualizing.PolynomialPresentation.upperShriekFunctor_isBoundedBelow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean#L92). The attribute's comment: “(1), the statement that φ^! maps D⁺(R) into D⁺(A)”.

> Algebraic upper shriek carries cohomologically bounded-below complexes to cohomologically
> bounded-below complexes.

```lean
theorem upperShriekFunctor_isBoundedBelow (p : PolynomialPresentation f)
    {K : DerivedCategory (ModuleCat.{max v u} R)} (hK : DerivedCategoryB.IsBoundedBelow K) :
    DerivedCategoryB.IsBoundedBelow (p.upperShriekFunctor.{u, v}.obj K)
```

**`Dualizing.PolynomialPresentation.upperShriekFunctor_derivedCategoryBPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean#L142). The attribute's comment: “(1), the statement that φ^! maps D⁺\_Coh(R) into D⁺\_Coh(A)”.

> Algebraic upper shriek along a finite type homomorphism of Noetherian rings carries
> bounded-below complexes with coherent cohomology to bounded-below complexes with coherent
> cohomology.

```lean
theorem upperShriekFunctor_derivedCategoryBPlus [IsNoetherianRing R] [IsNoetherianRing A]
    (p : PolynomialPresentation f) {K : DerivedCategory (ModuleCat.{max v u} R)}
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (fun M : ModuleCat.{max v u} R ↦ Module.Finite R M) K) :
    DerivedCategoryB.derivedCategoryBPlus
      (fun M : ModuleCat.{max v u} A ↦ Module.Finite A M)
      (p.upperShriekFunctor.{u, v}.obj K)
```

**`Dualizing.upperShriekFunctor_isBoundedAbove_of_isPerfectRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean#L295). The attribute's comment: “(2), the statement that φ^! maps D⁻(R) into D⁻(A)”.

> Algebraic upper shriek along a perfect homomorphism of Noetherian rings carries cohomologically
> bounded-above complexes to cohomologically bounded-above complexes.

```lean
theorem upperShriekFunctor_isBoundedAbove_of_isPerfectRingMap
    [IsNoetherianRing R] [IsNoetherianRing A] (p : PolynomialPresentation f)
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ N : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (hf : letI : Algebra R A := f.toAlgebra
      RingHom.IsPerfectRingMap R A derivedTensor comparison isLeftDerived)
    {K : DerivedCategory (ModuleCat.{max v u} R)} (hK : DerivedCategoryB.IsBoundedAbove K) :
    DerivedCategoryB.IsBoundedAbove (p.upperShriekFunctor.{u, v}.obj K)
```

**`Dualizing.upperShriekFunctor_derivedCategoryBMinus_of_isPerfectRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean#L321). The attribute's comment: “(2), the statement that φ^! maps D⁻\_Coh(R) into D⁻\_Coh(A)”.

> Algebraic upper shriek along a perfect homomorphism of Noetherian rings carries bounded-above
> complexes with coherent cohomology to bounded-above complexes with coherent cohomology.

```lean
theorem upperShriekFunctor_derivedCategoryBMinus_of_isPerfectRingMap
    [IsNoetherianRing R] [IsNoetherianRing A] (p : PolynomialPresentation f)
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ N : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (hf : letI : Algebra R A := f.toAlgebra
      RingHom.IsPerfectRingMap R A derivedTensor comparison isLeftDerived)
    {K : DerivedCategory (ModuleCat.{max v u} R)}
    (hK : DerivedCategoryB.derivedCategoryBMinus
      (fun M : ModuleCat.{max v u} R ↦ Module.Finite R M) K) :
    DerivedCategoryB.derivedCategoryBMinus
      (fun M : ModuleCat.{max v u} A ↦ Module.Finite A M)
      (p.upperShriekFunctor.{u, v}.obj K)
```

**`Dualizing.upperShriekFunctor_derivedCategoryBBounded_of_isPerfectRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/Bounded.lean#L351). The attribute's comment: “(2), the statement that φ^! maps Dᵇ\_Coh(R) into Dᵇ\_Coh(A)”.

> Algebraic upper shriek along a perfect homomorphism of Noetherian rings carries bounded
> complexes with coherent cohomology to bounded complexes with coherent cohomology.

```lean
theorem upperShriekFunctor_derivedCategoryBBounded_of_isPerfectRingMap
    [IsNoetherianRing R] [IsNoetherianRing A] (p : PolynomialPresentation f)
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ N : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (hf : letI : Algebra R A := f.toAlgebra
      RingHom.IsPerfectRingMap R A derivedTensor comparison isLeftDerived)
    {K : DerivedCategory (ModuleCat.{max v u} R)}
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : ModuleCat.{max v u} R ↦ Module.Finite R M) K) :
    DerivedCategoryB.derivedCategoryBBounded
      (fun M : ModuleCat.{max v u} A ↦ Module.Finite A M)
      (p.upperShriekFunctor.{u, v}.obj K)
```

## Tag 0BZL, a lemma

[Tag 0BZL](https://stacks.math.columbia.edu/tag/0BZL) in the Stacks Project.

**`Dualizing.PolynomialPresentation.upperShriekFunctor_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Dualizing.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/Dualizing.lean#L57).

> **Stacks Project, Tag 0BZL.** Algebraic upper shriek along a finite type homomorphism of
> Noetherian rings carries a dualizing complex to a dualizing complex.

```lean
theorem upperShriekFunctor_isDualizingComplex [IsNoetherianRing R] [IsNoetherianRing A]
    (p : PolynomialPresentation f) (K : DerivedCategory (ModuleCat.{u} R))
    (hK : IsDualizingComplex K) :
    IsDualizingComplex (p.upperShriekFunctor.{u, u}.obj K)
```

## Tag 0BZN, a lemma

[Tag 0BZN](https://stacks.math.columbia.edu/tag/0BZN) in the Stacks Project.

**`Dualizing.PolynomialPresentation.isIso_upperShriekFlatBaseChange_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/FlatBaseChangeIso.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/FlatBaseChangeIso.lean#L228).

> Let `R` be Noetherian, let `R → R'` be flat, let `φ : R → A` be of finite type, presented by
> `p`, and let `φ' : R' → A' = R' ⊗_R A` be its base change. The flat-base-change map
> `φ^!(K) ⊗_A^L A' ⟶ (φ')^!(K ⊗_R^L R')` of
> `Dualizing.PolynomialPresentation.upperShriekFlatBaseChange`, a natural transformation of functors
> `D(R) ⥤ D(A')`, is an isomorphism at every `K` in `D⁺(R)`; here `φ^!` is read at `p` and
> `(φ')^!` at its base change.

```lean
theorem PolynomialPresentation.isIso_upperShriekFlatBaseChange_app [IsNoetherianRing R]
    (p : PolynomialPresentation (algebraMap R A)) (hf : (algebraMap R R').Flat)
    (K : DerivedCategory (ModuleCat.{max v u} R)) (hK : DerivedCategoryB.IsBoundedBelow K) :
    IsIso ((p.upperShriekFlatBaseChange.{u, v} (R' := R') hf).app K)
```

## Tag 0BZR, a lemma

[Tag 0BZR](https://stacks.math.columbia.edu/tag/0BZR) in the Stacks Project.

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_comp_iso_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/TorIndependentBaseChangeIso.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/TorIndependentBaseChangeIso.lean#L385).

> **Stacks 0BZR.**  Let `R → R'` be a ring homomorphism, let `φ : R → A` be a perfect ring map
> such that `A` and `R'` are Tor independent over `R`, and let `φ' : R' → A' = R' ⊗_R A` be the
> induced map.  Then `φ^!(K) ⊗_A^L A' ≅ (φ')^!(K ⊗_R^L R')`, naturally in `K` in `D(R)`.
>
> Here `φ^!` is read at an arbitrary polynomial presentation `p` of `φ` and `(φ')^!` at an
> arbitrary polynomial presentation `p'` of `φ'`, the two derived tensor products at arbitrary
> left-derived models of extension of scalars, perfectness of `φ` relative to an arbitrary
> certified model of the derived tensor product on `D(R)`, and the modules in an arbitrary universe
> `max v u`.  The Noetherian hypotheses of the source are not needed.
>
> The isomorphism is the base-change map
> `Dualizing.PolynomialPresentation.upperShriekTorIndependentBaseChangeLarge` at `p` and its base
> change, invertible by
> `Dualizing.PolynomialPresentation.isIso_upperShriekTorIndependentBaseChangeLarge`, followed by the
> comparison of [stacks 0BZJ] between the base-changed presentation and `p'`.

```lean
theorem PolynomialPresentation.nonempty_upperShriekFunctor_comp_iso_of_torIndependent
    (p : PolynomialPresentation (algebraMap R A))
    (p' : PolynomialPresentation (algebraMap R' (TensorProduct R R' A)))
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ N : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (hperf : RingHom.IsPerfectRingMap R A derivedTensor comparison isLeftDerived)
    (hTor : TorIndependent R A R')
    (bcR : DerivedCategory (ModuleCat.{max v u} R) ⥤ DerivedCategory (ModuleCat.{max v u} R'))
    (cmpR : DerivedCategory.Q ⋙ bcR ⟶
      (ModuleCat.extendScalars.{u, u, max v u} (algebraMap R R')).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (ldR : bcR.IsLeftDerivedFunctor cmpR
      (HomologicalComplex.quasiIso (ModuleCat.{max v u} R) (ComplexShape.up ℤ)))
    (bcT : DerivedCategory (ModuleCat.{max v u} A) ⥤
      DerivedCategory (ModuleCat.{max v u} (TensorProduct R R' A)))
    (cmpT : DerivedCategory.Q ⋙ bcT ⟶
      (ModuleCat.extendScalars.{u, u, max v u}
          (Algebra.TensorProduct.includeRight :
            A →ₐ[R] TensorProduct R R' A).toRingHom).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (ldT : bcT.IsLeftDerivedFunctor cmpT
      (HomologicalComplex.quasiIso (ModuleCat.{max v u} A) (ComplexShape.up ℤ))) :
    Nonempty (p.upperShriekFunctor.{u, v} ⋙ bcT ≅ bcR ⋙ p'.upperShriekFunctor.{u, v})
```

## Tag 0BZS, a lemma

[Tag 0BZS](https://stacks.math.columbia.edu/tag/0BZS) in the Stacks Project.

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_comp_iso_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/FlatAlgebraBaseChangeIso.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/FlatAlgebraBaseChangeIso.lean#L257).

> **Stacks 0BZS.**  Let `R` be a Noetherian ring and `R → R'` any homomorphism, let
> `φ : R → A` be flat of finite type, presented by `p`, and let `φ' : R' → A' = R' ⊗_R A` be the
> induced map, presented by any `p'`.  Then there is an isomorphism of functors `D(R) ⥤ D(A')`
> `φ^!(K) ⊗_A^L A' ≅ (φ')^!(K ⊗_R^L R')`, natural in `K`, at every module universe `max v u`; the two
> derived tensor products are read at arbitrary left-derived models of extension of scalars.
>
> As in the source this is a special case of [stacks 0BZR],
> `Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_comp_iso_of_torIndependent`: over a
> Noetherian base a flat map of finite type is of finite presentation, hence perfect by
> [stacks 067J], and flatness of `A` makes `A` and `R'` Tor independent over `R`.  The source's
> Noetherian hypothesis on `R'` is not needed.

```lean
theorem PolynomialPresentation.nonempty_upperShriekFunctor_comp_iso_of_flat
    [IsNoetherianRing R]
    (hflat : (algebraMap R A).Flat)
    (p : PolynomialPresentation (algebraMap R A))
    (p' : PolynomialPresentation (algebraMap R' (TensorProduct R R' A)))
    (bcR : DerivedCategory (ModuleCat.{max v u} R) ⥤ DerivedCategory (ModuleCat.{max v u} R'))
    (cmpR : DerivedCategory.Q ⋙ bcR ⟶
      (ModuleCat.extendScalars.{u, u, max v u} (algebraMap R R')).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (ldR : bcR.IsLeftDerivedFunctor cmpR
      (HomologicalComplex.quasiIso (ModuleCat.{max v u} R) (ComplexShape.up ℤ)))
    (bcT : DerivedCategory (ModuleCat.{max v u} A) ⥤
      DerivedCategory (ModuleCat.{max v u} (TensorProduct R R' A)))
    (cmpT : DerivedCategory.Q ⋙ bcT ⟶
      (ModuleCat.extendScalars.{u, u, max v u}
          (Algebra.TensorProduct.includeRight :
            A →ₐ[R] TensorProduct R R' A).toRingHom).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (ldT : bcT.IsLeftDerivedFunctor cmpT
      (HomologicalComplex.quasiIso (ModuleCat.{max v u} A) (ComplexShape.up ℤ))) :
    Nonempty (p.upperShriekFunctor.{u, v} ⋙ bcT ≅ bcR ⋙ p'.upperShriekFunctor.{u, v})
```

## Tag 0BZT, a lemma

[Tag 0BZT](https://stacks.math.columbia.edu/tag/0BZT) in the Stacks Project.

**`Dualizing.PolynomialPresentation.exists_upperShriekComp_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/CompositionFiniteType.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/CompositionFiniteType.lean#L178).

> **Stacks Project, Tag 0BZT.**  Let `a : R →+* A` and `b : A →+* B` be homomorphisms of finite
> type with `R` Noetherian, let `p` be any polynomial presentation of `a`, `q` any polynomial
> presentation of `b` and `r` any polynomial presentation of `b ∘ a`.  Then there is a
> transformation of functors
>
> `b^! ∘ a^! ⟶ (b ∘ a)^!`
>
> upper shriek being read at `p`, at `q` and at `r` and modules taken in any universe `max v u`,
> which is an isomorphism at every object of `D⁺(R)`.  The Noetherian hypothesis is needed on `R`
> only; it passes to the polynomial algebras, which is all the proof uses.
>
> It is `Dualizing.PolynomialPresentation.exists_upperShriekComp_isIso_of_isBoundedBelow`, which
> states it at the induced presentation `p.comp q` of the composite, transported to an arbitrary `r`
> along the independence of the presentation, [Stacks, Tag 0BZJ],
> `Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso`.

```lean
theorem exists_upperShriekComp_of_finiteType [IsNoetherianRing R] {a : R →+* A} {b : A →+* B}
    (p : PolynomialPresentation a)
    (q : PolynomialPresentation b) (r : PolynomialPresentation (b.comp a)) :
    ∃ τ : p.upperShriekFunctor.{u, v} ⋙ q.upperShriekFunctor.{u, v} ⟶
        r.upperShriekFunctor.{u, v},
      ∀ K : DerivedCategory (ModuleCat.{max v u} R), DerivedCategoryB.IsBoundedBelow K →
        IsIso (τ.app K)
```

## Tag 0C0G, a lemma

[Tag 0C0G](https://stacks.math.columbia.edu/tag/0C0G) in the Stacks Project.

**`Dualizing.upperShriekFunctor_iso_derivedHom_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/Finite.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/Finite.lean#L159). The attribute's comment: “for a finite φ of Noetherian rings, at an arbitrary polynomial presentation, at module universe equal to the ring universe”.

> **Stacks Project, Tag 0C0G for a finite `φ`.**  Let `φ : R →+* A` be a finite homomorphism
> and let `p` be any polynomial presentation of `φ`.  Then the algebraic upper
> shriek functor of `p` is the derived coextension-of-scalars functor
>
> `φ^! ≅ RHom_R(A, -) : D(R) ⥤ D(A)`
>
> of [Stacks, Tag 0A70].
>
> `φ` factors as `R → C → A` through a monic quotient
> `C = R[T₀, …, Tₙ₋₁]/(f₀(T₀), …, fₙ₋₁(Tₙ₋₁))` by a surjection
> (`Dualizing.exists_monicIdeal_quotient_surjection`).  The bottom map is
> `Dualizing.nonempty_upperShriekFunctor_iso_derivedHom_monicIdeal`, whose inputs — the weak
> regularity of `f₀(T₀), …, fₙ₋₁(Tₙ₋₁)` and the finiteness, freeness and self-duality of `C` — are
> `MvPolynomial.isWeaklyRegular_ofFn_aeval_X_of_monic` and
> `Dualizing.finite_free_selfDual_monicIdeal`.  The surjection is Tag 0C0G at an arbitrary
> presentation, `Dualizing.upperShriekFunctor_iso_derivedHom_of_surjective`, and the two halves are
> put together by [Stacks, Tag 0BZT] for a surjective second map
> (`Dualizing.upperShriekFunctor_comp_of_surjective`) and [Stacks, Tag 0C0F]
> (`Dualizing.derivedHomCompIso`).
>
> The module universe is the ring universe here, unlike in the surjective case: the computation of
> `ω_{C/R}` and the tensor formula of [Stacks, Tag 0E4B] it is fed to are both stated at module
> universe equal to the ring universe.

```lean
theorem upperShriekFunctor_iso_derivedHom_of_finite (φ : R →+* A) (hφ : φ.Finite)
    (p : PolynomialPresentation φ) :
    Nonempty (p.upperShriekFunctor.{u, u} ≅ derivedHom.{u, u, u} φ)
```

## Tag 0C0H, a lemma

[Tag 0C0H](https://stacks.math.columbia.edu/tag/0C0H) in the Stacks Project.

**`Dualizing.upperShriekFunctor_iso_derivedTensorProduct_away_and_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/FlatEpimorphism.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/FlatEpimorphism.lean#L585).

> **[Stacks, Tag 0C0H].**  Let `R` be a ring.
>
> 1. For `f ∈ R` and `φ : R → R_f` the localization away from `f`, the algebraic upper shriek
>    functor `φ^!`, read at any polynomial presentation of `φ`, is isomorphic to `- ⊗_R^L R_f`.
> 2. More generally, if `φ : R → R'` is a ring map such that `Spec(R') → Spec(R)` is an open
>    immersion, then `φ` admits a polynomial presentation, and `φ^!` read at any of them is
>    isomorphic to `- ⊗_R^L R'`.
>
> Both hold at an arbitrary module universe.  `- ⊗_R^L R'` is derived tensor product over `R` with
> `R'` in degree zero, `Dualizing.derivedTensorProductOver`; `R_f` is any localization of `R` away
> from `f`.  The source assumes `R` Noetherian, which neither clause needs.  The first clause is
> `Dualizing.nonempty_upperShriekFunctor_iso_derivedTensorProduct_away`, computed from
> [Stacks, Tag 0BZH] at `R[x] → R[x]/(fx - 1)` as in the source; the second is
> `Dualizing.nonempty_upperShriekFunctor_iso_derivedTensorProduct_of_isOpenImmersion`.

```lean
theorem upperShriekFunctor_iso_derivedTensorProduct_away_and_of_isOpenImmersion
    {R : Type u} [CommRing R] :
    (∀ (f : R) (S : Type u) [CommRing S] [Algebra R S] [IsLocalization.Away f S]
        (p : PolynomialPresentation (algebraMap R S)),
        Nonempty (p.upperShriekFunctor.{u, v} ≅
          derivedTensorProductOver.{u, v} (algebraMap R S) (Stacks0BZE.unitObject.{u, v} S))) ∧
      ∀ (R' : Type u) [CommRing R'] (φ : R →+* R'),
        IsOpenImmersion (Spec.map (CommRingCat.ofHom φ)) →
          Nonempty (PolynomialPresentation φ) ∧
            ∀ p : PolynomialPresentation φ, Nonempty (p.upperShriekFunctor.{u, v} ≅
              derivedTensorProductOver.{u, v} φ (Stacks0BZE.unitObject.{u, v} R'))
```

## Tag 0BZU, a lemma

[Tag 0BZU](https://stacks.math.columbia.edu/tag/0BZU) in the Stacks Project.

**`Dualizing.PolynomialPresentation.upperShriekFunctor_iso_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensor.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensor.lean#L449). The attribute's comment: “at an arbitrary polynomial presentation and an arbitrary module universe”.

> **Stacks 0BZU.** Let `φ : R → A` be a ring homomorphism, let `p` be a
> polynomial presentation of `φ` with polynomial algebra `P` and surjection `ψ : P → A`, and assume
> `A` is a perfect `P`-module, which for a perfect `φ` is Tag 068Y.  Then the algebraic upper shriek
> functor of `p` is derived tensor product over `R` with the single object `φ^!(R)` of `D(A)`:
> `φ^!(K) = K ⊗_R^L φ^!(R)`, naturally in `K` in `D(R)`.
>
> Perfectness of `A` over `P` is exactly the hypothesis of Tag 0BZE, and Tag 0BZE for `ψ` is the one
> external input of the argument: it identifies `RHom_P(A, -)` with derived tensor product over `P`
> with `RHom_P(A, P)`.  At the arbitrary module universe `max v u` of this statement that tag is
> `Dualizing.nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect_anyModuleUniverse`.
>
> The rest is the cancellation of the intermediate `- ⊗_R^L P` by the iterated change of rings of
> Tag 08YU, the passage of the shift by `n` into the tensor factor through the universal property of
> the left derived functor, and the evaluation of that factor at `R` by the unitors of the tensor
> product of complexes.

```lean
public theorem upperShriekFunctor_iso_derivedTensorProduct
    (p : PolynomialPresentation f)
    (hp : letI : Module p.Poly A := Module.compHom A p.toRingHom
      StacksDraft.Perfect.IsPerfectModule (R := p.Poly) A) :
    letI : MonoidalCategoryStruct (ModuleCat.{max v u} R) :=
      ModuleCat.liftedModuleMonoidalStruct.{u, max v u}
    letI : MonoidalCategory (ModuleCat.{max v u} R) :=
      ModuleCat.liftedModuleMonoidal.{u, max v u}
    let R₀ := (DerivedCategory.singleFunctor (ModuleCat.{max v u} R) 0).obj
      (MonoidalCategoryStruct.tensorUnit (ModuleCat.{max v u} R))
    Nonempty (p.upperShriekFunctor.{u, v} ≅
      derivedTensorProductOver.{u, v} f (p.upperShriekFunctor.{u, v}.obj R₀))
```

**`Dualizing.PolynomialPresentation.upperShriekFunctor_iso_derivedTensorProduct_of_isPerfectRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensor.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensor.lean#L525). The attribute's comment: “for a perfect homomorphism of Noetherian rings, at an arbitrary polynomial presentation and an arbitrary module universe”.

> **Stacks 0BZU.** Let `φ : R → A` be a perfect ring homomorphism and let `p` be
> a polynomial presentation of `φ`.  Then the algebraic upper shriek functor of `p` is derived
> tensor product over `R` with the single object `φ^!(R)` of `D(A)`: `φ^!(K) = K ⊗_R^L φ^!(R)`,
> naturally in `K` in `D(R)`.  A flat homomorphism of finite type is perfect, so the hypothesis is
> not vacuous.
>
> Perfectness is taken in the form of `RingHom.IsPerfectRingMap`, which is relative to a certified
> model of the derived tensor product on `D(R)`; by Tag 068Y it gives perfectness of `A` as a module
> over the polynomial algebra of `p`, which is the hypothesis of Tag 0BZE.  That is the only thing
> `Dualizing.PolynomialPresentation.upperShriekFunctor_iso_derivedTensorProduct` asks for, so this
> is exactly that statement with its perfectness rewritten.

```lean
public theorem upperShriekFunctor_iso_derivedTensorProduct_of_isPerfectRingMap
    (p : PolynomialPresentation f)
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ N : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (hf : letI : Algebra R A := f.toAlgebra
      RingHom.IsPerfectRingMap R A derivedTensor comparison isLeftDerived) :
    letI : MonoidalCategoryStruct (ModuleCat.{max v u} R) :=
      ModuleCat.liftedModuleMonoidalStruct.{u, max v u}
    letI : MonoidalCategory (ModuleCat.{max v u} R) :=
      ModuleCat.liftedModuleMonoidal.{u, max v u}
    let R₀ := (DerivedCategory.singleFunctor (ModuleCat.{max v u} R) 0).obj
      (MonoidalCategoryStruct.tensorUnit (ModuleCat.{max v u} R))
    Nonempty (p.upperShriekFunctor.{u, v} ≅
      derivedTensorProductOver.{u, v} f (p.upperShriekFunctor.{u, v}.obj R₀))
```

**`Dualizing.PolynomialPresentation.tensorFormulaOfPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensor.lean, line 673](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensor.lean#L673). The attribute's comment: “at an arbitrary polynomial presentation and an arbitrary module universe, with the tensor formula built as an isomorphism at a constructed tensor factor whose class in D(A) is the value of upper shriek at R”.

> **Stacks 0BZU with the isomorphism built, from perfectness alone.** Let `φ : R → A` be a ring
> homomorphism and `p` a polynomial presentation of `φ` whose polynomial algebra
> makes `A` a perfect module. Then the algebraic upper shriek functor of `p` *is* derived tensor
> product over `R` with a constructed complex whose class in `D(A)` is `φ^!(R)`.
>
> This is `Dualizing.PolynomialPresentation.tensorFormulaOfDerivedHomIso` at the representative of
> `RHom_P(A, P)` chosen by `objPreimage`, with the isomorphism of Tag 0BZE there taken from
> `Dualizing.nonempty_derivedHom_iso_canonicalDerivedTensor_of_perfect_anyModuleUniverse`. That tag
> is available as a proposition rather than as data, because passing between two representatives of
> one object of `D(A)` goes through a fraction, so the isomorphism is chosen; everything after the
> choice is a construction.

```lean
public def tensorFormulaOfPerfect
    (p : PolynomialPresentation f)
    (hp : letI : Module p.Poly A := Module.compHom A p.toRingHom
      StacksDraft.Perfect.IsPerfectModule (R := p.Poly) A) :
    TensorFormula.{u, v} p
```

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean#L134). The attribute's comment: “at an arbitrary polynomial presentation, at module universe equal to the ring universe; the same statement at an arbitrary module universe is Dualizing.PolynomialPresentation.upperShriekFunctor\_iso\_derivedTensorProduct”.

> **Stacks 0BZU, with no carried hypothesis.** Let `φ : R → A` be a ring homomorphism and `p` a
> polynomial presentation of it whose polynomial algebra makes `A` a perfect
> module. Then the algebraic upper shriek functor of `p` is derived tensor product over `R` with
> the single object `φ^!(R)` of `D(A)`.
>
> This is `Dualizing.PolynomialPresentation.upperShriekFunctor_iso_derivedTensorProduct` read at
> module universe equal to the ring universe, which is the generality the rest of this module works
> in; that statement holds at any module universe.

```lean
theorem nonempty_upperShriekFunctor_iso_derivedTensorProduct
    (p : PolynomialPresentation f)
    (hp : letI : Module p.Poly A := Module.compHom A p.toRingHom
      StacksDraft.Perfect.IsPerfectModule.{u, u, u + 1} (R := p.Poly) A) :
    letI : MonoidalCategoryStruct (ModuleCat.{u} R) :=
      ModuleCat.liftedModuleMonoidalStruct.{u, u}
    letI : MonoidalCategory (ModuleCat.{u} R) :=
      ModuleCat.liftedModuleMonoidal.{u, u}
    let R₀ := (DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
      (MonoidalCategoryStruct.tensorUnit (ModuleCat.{u} R))
    Nonempty (p.upperShriekFunctor.{u, u} ≅
      derivedTensorProductOver.{u, u} f (p.upperShriekFunctor.{u, u}.obj R₀))
```

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso_derivedTensorProduct_of_isPerfectRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean#L165). The attribute's comment: “for a perfect homomorphism of Noetherian rings, at an arbitrary polynomial presentation, at module universe equal to the ring universe; the same statement at an arbitrary module universe is Dualizing.PolynomialPresentation.upperShriekFunctor\_iso\_derivedTensorProduct\_of\_isPerfectRingMap”.

> **Stacks 0BZU for a perfect homomorphism, with no carried hypothesis.** Let `φ : R → A` be a
> perfect ring homomorphism and `p` a polynomial presentation of it. Then the
> algebraic upper shriek functor of `p` is derived tensor product over `R` with the single object
> `φ^!(R)` of `D(A)`.
>
> This is the hypothesis shape of Stacks 0BZU itself: perfectness of `φ`, in the form of
> `RingHom.IsPerfectRingMap` relative to a model of the derived tensor product on `D(R)`, rather
> than perfectness of `A` over the polynomial algebra of `p`. Tag 068Y passes between the two, as
> `RingHom.isPerfectModule_of_isPerfectRingMap`, which is what feeds
> `Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso_derivedTensorProduct` here. So
> this is
> `Dualizing.PolynomialPresentation.upperShriekFunctor_iso_derivedTensorProduct_of_isPerfectRingMap`
> read at module universe equal to the ring universe.

```lean
theorem nonempty_upperShriekFunctor_iso_derivedTensorProduct_of_isPerfectRingMap
    (p : PolynomialPresentation f)
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} R) ⥤
        DerivedCategory (ModuleCat.{u} R) ⥤ DerivedCategory (ModuleCat.{u} R))
    (comparison : ∀ N : ModuleCat.{u} R,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} R,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} R) (ComplexShape.up ℤ)))
    (hf : letI : Algebra R A := f.toAlgebra
      RingHom.IsPerfectRingMap R A derivedTensor comparison isLeftDerived) :
    letI : MonoidalCategoryStruct (ModuleCat.{u} R) :=
      ModuleCat.liftedModuleMonoidalStruct.{u, u}
    letI : MonoidalCategory (ModuleCat.{u} R) :=
      ModuleCat.liftedModuleMonoidal.{u, u}
    let R₀ := (DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj
      (MonoidalCategoryStruct.tensorUnit (ModuleCat.{u} R))
    Nonempty (p.upperShriekFunctor.{u, u} ≅
      derivedTensorProductOver.{u, u} f (p.upperShriekFunctor.{u, u}.obj R₀))
```

**`Dualizing.PolynomialPresentation.tensorFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/DerivedTensorUnconditional.lean#L212). The attribute's comment: “at an arbitrary polynomial presentation, at module universe equal to the ring universe, with no carried hypothesis, and with the isomorphism built rather than shown to exist — at the constructed tensor factor of Tag 08YU, whose class in D(A) is the value of upper shriek at R rather than a prescribed representative of it”.

> **Stacks 0BZU with the isomorphism built, and no carried hypothesis.** Same hypotheses as
> `Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_iso_derivedTensorProduct`, but the
> conclusion is data: a complex of `A`-modules whose class in `D(A)` is `φ^!(R)` — by
> `Dualizing.PolynomialPresentation.TensorFormula.classIso` — together with the isomorphism of the
> algebraic upper shriek functor of `p` with derived tensor product over `R` with that complex.
>
> The two inputs are `Dualizing.derivedHomIsoCanonicalDerivedTensorOfPerfect`, which is Tag 0BZE in
> the change-of-rings shape with the isomorphism built at the canonical Tate tensor factor, and
> `Dualizing.PolynomialPresentation.tensorFormulaOfDerivedHomIso`, which turns such an isomorphism
> into the tensor formula. Neither extracts a witness from an existential.

```lean
def tensorFormula (p : PolynomialPresentation f)
    (hp : letI : Module p.Poly A := Module.compHom A p.toRingHom
      StacksDraft.Perfect.IsPerfectModule.{u, u, u + 1} (R := p.Poly) A) :
    TensorFormula.{u, u} p
```

## Tag 0E9L, a lemma

[Tag 0E9L](https://stacks.math.columbia.edu/tag/0E9L) in the Stacks Project.

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_natIso_dualizingDerivedHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/FiniteTypeDualityFormula.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/FiniteTypeDualityFormula.lean#L193). The attribute's comment: “in general: an arbitrary finite-type φ of Noetherian rings at an arbitrary polynomial presentation, as an isomorphism of functors on D\_Coh(A), with no surjectivity and no projection-formula keystone”.

> **[Stacks, Tag 0E9L] for an arbitrary finite-type `φ`, as an isomorphism of functors on
> `D_Coh(A)`.**  Let `φ : A →+* B` be a homomorphism of finite type with `A` Noetherian, let `p` be
> any polynomial presentation of `φ` and let `ω` be a dualizing complex for `A`.  Write `φ^!` for
> the algebraic upper shriek functor of `p`, put `ω_B = φ^!(ω)`, `D_A(-) = RHom_A(-, ω)` and
> `D_B(-) = RHom_B(-, ω_B)`.  Then
>
> `φ^!(K) ≅ D_B(D_A(K) ⊗_A^L B)`
>
> as an isomorphism of functors on `D_Coh(A)`.
>
> **No surjectivity, and no projection-formula keystone.**  The surjective case is
> `Dualizing.upperShriekFunctor_natIso_dualizingDerivedHom_of_surjective`; the passage to a general
> finite-type `φ` is made here by reading that statement's engine — the tag for derived coextension
> of scalars along an arbitrary ring homomorphism — at the object `K ⊗_A^L P` over the polynomial
> algebra of the presentation, and feeding it the flat base change of derived Hom along `A → P`.
> That base change is the unconditional [Stacks, Tag 0A6A], not the Tor-independent square of
> [Stacks, Tag 0BZM]; so unlike [Stacks, Tag 0BZT] in general
> (`Dualizing.PolynomialPresentation.exists_upperShriekComp_of_finiteType`) this carries no
> `Dualizing.KFlatAlgebraActionEq`.  See the module documentation for the chain.
>
> The derived base change `- ⊗_A^L B` is the chosen model; for an arbitrary model see
> `Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_natIso_dualizingDerivedHom_model`.
> The statement is a `Nonempty` because the adjunction of [Stacks, Tag 0A70] that the engine
> consumes is itself only known to exist.

```lean
theorem nonempty_upperShriekFunctor_natIso_dualizingDerivedHom [IsNoetherianRing A]
    (p : PolynomialPresentation φ) (ω : DerivedCategory (ModuleCat.{u} A))
    (hω : IsDualizingComplex ω) :
    Nonempty ((hasFiniteCohomology.{u, u} A).ι ⋙ p.upperShriekFunctor.{u, u} ≅
      (hasFiniteCohomology.{u, u} A).ι ⋙ dualizingBaseChangeFunctor.{u, u} φ
        (totalDerivedExtension φ) ω (p.upperShriekFunctor.{u, u}.obj ω))
```

**`Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_natIso_dualizingDerivedHom_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/FiniteTypeDualityFormula.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/FiniteTypeDualityFormula.lean#L254). The attribute's comment: “in general, at an arbitrary model of derived base change as well as an arbitrary polynomial presentation”.

> **[Stacks, Tag 0E9L] in general, at an arbitrary model of derived base change.**  This is
> `Dualizing.PolynomialPresentation.nonempty_upperShriekFunctor_natIso_dualizingDerivedHom` with the
> chosen model of `- ⊗_A^L B` replaced by an arbitrary one.  Two models of derived extension of
> scalars along `φ` are isomorphic by uniqueness of the total left derived functor,
> `CategoryTheory.Functor.leftDerivedNatIso`, and
> `Dualizing.PolynomialPresentation.dualizingBaseChangeFunctorIsoOfModelIso` carries that
> isomorphism into the right-hand side of the tag.

```lean
theorem nonempty_upperShriekFunctor_natIso_dualizingDerivedHom_model [IsNoetherianRing A]
    (p : PolynomialPresentation φ)
    (E : CochainComplex.DerivedExtensionScalars.TotalDerivedExtensionScalars.{u, u, u,
      u + 1, u + 1} φ)
    (ω : DerivedCategory (ModuleCat.{u} A)) (hω : IsDualizingComplex ω) :
    Nonempty ((hasFiniteCohomology.{u, u} A).ι ⋙ p.upperShriekFunctor.{u, u} ≅
      (hasFiniteCohomology.{u, u} A).ι ⋙ dualizingBaseChangeFunctor.{u, u} φ E ω
        (p.upperShriekFunctor.{u, u}.obj ω))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.24, Tag 0BZI](https://stacks.math.columbia.edu/tag/0BZI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
