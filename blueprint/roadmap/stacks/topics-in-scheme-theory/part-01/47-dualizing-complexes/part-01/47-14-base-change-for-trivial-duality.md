---
declaration: section
origin: cited
lean: Dualizing.derivedHomBaseChange, Dualizing.derivedHomBaseChangeCanonical, Dualizing.isIso_derivedHomBaseChange_app_iff_diagonal, Dualizing.isIso_derivedHomBaseChange_app_of_isModulePseudoCoherent_of_finiteTorDimension, Dualizing.isIso_derivedHomBaseChange_of_isPerfect
statement: formalized
proof: formalized
---

# 47.14 Base change for trivial duality

Section 47.14 of the Stacks Project, [Tag 0E28](https://stacks.math.columbia.edu/tag/0E28). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E29, an equation

[Tag 0E29](https://stacks.math.columbia.edu/tag/0E29) in the Stacks Project.

**`Dualizing.derivedHomBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChange.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChange.lean#L222).

> The canonical base-change map
> `RHom_R(A, -) ⊗ᴸ_A (A ⊗_R R') ⟶ RHom_{R'}(A ⊗_R R', - ⊗ᴸ_R R')`,
> functorial in the object of `D(R)`.

```lean
noncomputable def derivedHomBaseChange
    {R : Type uR} {A : Type uA} {R' : Type uRp} [CommRing R] [CommRing A] [CommRing R']
    [Algebra R A] [Algebra R R']
    (hTor : RingTheory.TorIndependence.TorIndependent R A R')
    (baseChangeR :
      DerivedCategory (ModuleCat.{max v uR uA uRp} R) ⥤
        DerivedCategory (ModuleCat.{max v uR uA uRp} R'))
    (comparisonR :
      DerivedCategory.Q ⋙ baseChangeR ⟶
        (ModuleCat.extendScalars.{uR, uRp, max v uR uA uRp}
          (algebraMap R R')).mapHomologicalComplex
          (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedR : baseChangeR.IsLeftDerivedFunctor comparisonR
      (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA uRp} R) (ComplexShape.up ℤ)))
    (baseChangeA :
      DerivedCategory (ModuleCat.{max v uR uA uRp} A) ⥤
        DerivedCategory (ModuleCat.{max v uR uA uRp} (TensorProduct R A R')))
    (comparisonA :
      DerivedCategory.Q ⋙ baseChangeA ⟶
        (ModuleCat.extendScalars.{uA, max uA uRp, max v uR uA uRp}
          (algebraMap A (TensorProduct R A R'))).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerivedA : baseChangeA.IsLeftDerivedFunctor comparisonA
      (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA uRp} A) (ComplexShape.up ℤ)))
    :
    derivedHom.{uR, max v uRp, uA} (algebraMap R A) ⋙ baseChangeA ⟶
      baseChangeR ⋙ derivedHom.{uRp, max v uR, max uA uRp}
        (Algebra.TensorProduct.includeRight :
          R' →ₐ[R] TensorProduct R A R').toRingHom
```

**`Dualizing.derivedHomBaseChangeCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChangeCanonical.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChangeCanonical.lean#L86). The attribute's comment: “at the constructed derived extensions of scalars; one universe for all rings”.

> The canonical base-change map
> `RHom_R(A, -) ⊗ᴸ_A (A ⊗_R R') ⟶ RHom_{R'}(A ⊗_R R', - ⊗ᴸ_R R')`
> of [Stacks, Equation 47.14.0.1], functorial in the object of `D(R)`, with the two derived
> extensions of scalars taken to be the constructed functor
> `StacksDraft.PseudoCoherence.extendScalarsDerived` rather than certified parameters.
>
> All three rings and the module size live in the single universe `u`, which is the generality
> `extendScalarsDerived` is available in.

```lean
noncomputable def derivedHomBaseChangeCanonical
    {R : Type u} {A : Type u} {R' : Type u} [CommRing R] [CommRing A] [CommRing R']
    [Algebra R A] [Algebra R R']
    (hTor : RingTheory.TorIndependence.TorIndependent R A R') :
    derivedHom.{u, u, u} (algebraMap R A) ⋙
        extendScalarsDerived (algebraMap A (TensorProduct R A R')) ⟶
      extendScalarsDerived (algebraMap R R') ⋙ derivedHom.{u, u, u}
        (Algebra.TensorProduct.includeRight :
          R' →ₐ[R] TensorProduct R A R').toRingHom
```

## Tag 0E2A, a lemma

[Tag 0E2A](https://stacks.math.columbia.edu/tag/0E2A) in the Stacks Project.

**`Dualizing.isIso_derivedHomBaseChange_app_iff_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomBaseChange/Criterion.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomBaseChange/Criterion.lean#L220).

> For `R → A` and `R → R'` with `A` and `R'` Tor independent over `R`, and `A' = A ⊗_R R'`, the
> base-change morphism `RHom_R(A, K) ⊗ᴸ_A A' ⟶ RHom_{R'}(A', K ⊗ᴸ_R R')` of Stacks 0E29 is an
> isomorphism exactly when the morphism `RHom_R(A, K) ⊗ᴸ_R R' ⟶ RHom_R(A, K ⊗ᴸ_R R')` of Stacks 0BYN
> is, read over `ULift R` through the scalar equivalence of Stacks 0E1W.

```lean
theorem isIso_derivedHomBaseChange_app_iff_diagonal
    (K : DerivedCategory (ModuleCat.{max v uR uA uRp} R)) :
    IsIso ((derivedHomBaseChange.{uR, uA, uRp, v} hTor baseChangeR comparisonR isLeftDerivedR
        baseChangeA comparisonA isLeftDerivedA).app K) ↔
      (let E := Stacks.DerivedHom.ScalarTransportedInternalHom.scalarEquivalence.{uR, max v uR uA
        uRp} R
       IsIso (StacksDraft.DerivedHom.derivedTensorHomDiagonal
         (E.functor.obj ((DerivedCategory.singleFunctor (ModuleCat.{max v uR uA uRp} R) 0).obj
           ((ModuleCat.restrictScalars (algebraMap R R')).obj
             (ModuleCat.of R' (ULift.{max v uR uA} R')))))
         (E.functor.obj K)
         (E.functor.obj (derivedAlgebraSingle.{uR, uA, max v uRp} (algebraMap R A)))) : Prop)
```

## Tag 0BZM, a lemma

[Tag 0BZM](https://stacks.math.columbia.edu/tag/0BZM) in the Stacks Project.

**`Dualizing.isIso_derivedHomBaseChange_app_of_isModulePseudoCoherent_of_finiteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChangeIsomorphismFiniteTorDimension.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChangeIsomorphismFiniteTorDimension.lean#L126).

> **Stacks 0BZM.** Let `R → A` and `R → R'` be homomorphisms of commutative rings and
> `A' = A ⊗_R R'`. If `A` is pseudo-coherent as an `R`-module, `R'` has finite Tor dimension as an
> `R`-module, and `A` and `R'` are Tor independent over `R`, then the base-change morphism
> `RHom_R(A, K) ⊗ᴸ_A A' ⟶ RHom_{R'}(A', K ⊗ᴸ_R R')` of Stacks 0E29 is an isomorphism for every
> `K` in `D⁺(R)`.

```lean
theorem isIso_derivedHomBaseChange_app_of_isModulePseudoCoherent_of_finiteTorDimension
    (hA : StacksDraft.PseudoCoherence.IsModulePseudoCoherent (R := R) A)
    (D : StacksDraft.TorAmplitude.CertifiedDerivedTensoring.{uR, max v uR uA uRp} R)
    (hFinite : StacksDraft.TorAmplitude.ModuleHasFiniteTorDimension D.tensor D.comparison
      D.isLeftDerived
      ((ModuleCat.restrictScalars (algebraMap R R')).obj
        (ModuleCat.of R' (ULift.{max v uR uA, uRp} R'))))
    (K : DerivedCategory (ModuleCat.{max v uR uA uRp} R))
    (hK : (DerivedCategory.TStructure.t (C := ModuleCat.{max v uR uA uRp} R)).plus K) :
    IsIso ((derivedHomBaseChange.{uR, uA, uRp, v} hTor baseChangeR comparisonR isLeftDerivedR
      baseChangeA comparisonA isLeftDerivedA).app K)
```

## Tag 0BZP, a lemma

[Tag 0BZP](https://stacks.math.columbia.edu/tag/0BZP) in the Stacks Project.

**`Dualizing.isIso_derivedHomBaseChange_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChangeIsomorphism.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/TrivialDuality/BaseChangeIsomorphism.lean#L233).

> **Stacks 0BZP.** Let `R → A` and `R → R'` be homomorphisms of commutative rings and
> `A' = A ⊗_R R'`. If `A` is perfect as an `R`-module and `A` and `R'` are Tor independent over
> `R`, then the base-change morphism of Stacks 0E29 is invertible — as a natural transformation,
> hence at every object of `D(R)` and with no boundedness hypothesis.
>
> The proof is that of the source. By Stacks 0E2A the restriction of the morphism along
> `R' → A'` is, up to isomorphisms of source and target, the derived-Hom base-change morphism of
> Stacks 0E1X at the algebra `A`; this is
> `Dualizing.exists_restrictScalars_map_derivedHomBaseChange_app_eq`. That morphism is
> invertible because `A` is perfect, by Stacks 0ATK (1), and restriction of scalars reflects
> isomorphisms.

```lean
theorem isIso_derivedHomBaseChange_of_isPerfect
    (hA : StacksDraft.Perfect.IsPerfectModule (R := R) A) :
    IsIso (derivedHomBaseChange.{uR, uA, uRp, v} hTor baseChangeR comparisonR isLeftDerivedR
      baseChangeA comparisonA isLeftDerivedA)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.14, Tag 0E28](https://stacks.math.columbia.edu/tag/0E28)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
