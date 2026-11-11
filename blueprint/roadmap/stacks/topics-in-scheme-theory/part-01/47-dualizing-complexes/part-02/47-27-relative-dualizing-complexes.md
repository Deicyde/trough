---
declaration: section
origin: cited
lean: Dualizing.IsRelativeDualizingComplex, Dualizing.IsRelativeDualizingComplex.nonempty_iso, Dualizing.PolynomialPresentation.relativeDualizingComplex_isRelativeDualizingComplex, Dualizing.exists_isRelativeDualizingComplex_of_flat, Dualizing.IsRelativeDualizingComplex.baseChange, Dualizing.IsRelativeDualizingComplex.span_derivedBaseChange_diagonalGenerator, Dualizing.isIso_relativeHomothety_of_isRelativeDualizingComplex, Dualizing.isRelativeDualizingComplex_derivedTensorProductOver
statement: formalized
proof: formalized
---

# 47.27 Relative dualizing complexes

Section 47.27 of the Stacks Project, [Tag 0E2B](https://stacks.math.columbia.edu/tag/0E2B). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E2C, a definition

[Tag 0E2C](https://stacks.math.columbia.edu/tag/0E2C) in the Stacks Project.

**`Dualizing.IsRelativeDualizingComplex`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Relative.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Relative.lean#L152).

> **Stacks Project, Tag 0E2C.** A relative dualizing complex for a flat, finitely
> presented map `R → A` is an `R`-perfect object `K` of `D(A)` such that
> `RHom_{A ⊗[R] A}(A, K ⊗[A]ᴸ (A ⊗[R] A))` is isomorphic to `A`.

```lean
structure IsRelativeDualizingComplex (R A : Type u) [CommRing R] [CommRing A]
    [Algebra R A] [Module.Flat R A] [Algebra.FinitePresentation R A]
    (K : DerivedCategory (ModuleCat.{u} A)) : Prop
```

## Tag 0E2D, a lemma

[Tag 0E2D](https://stacks.math.columbia.edu/tag/0E2D) in the Stacks Project.

**`Dualizing.IsRelativeDualizingComplex.nonempty_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RelativeUniquenessTensor.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RelativeUniquenessTensor.lean#L41).

> Let `R → A` be a flat ring map of finite presentation. Any two relative dualizing complexes
> for `R → A` are isomorphic.

```lean
theorem IsRelativeDualizingComplex.nonempty_iso {R A : Type u} [CommRing R] [CommRing A]
    [Algebra R A] [Module.Flat R A] [Algebra.FinitePresentation R A]
    {K L : DerivedCategory (ModuleCat.{u} A)}
    (hK : IsRelativeDualizingComplex R A K) (hL : IsRelativeDualizingComplex R A L) :
    Nonempty (K ≅ L)
```

## Tag 0E2E, a lemma

[Tag 0E2E](https://stacks.math.columbia.edu/tag/0E2E) in the Stacks Project.

**`Dualizing.PolynomialPresentation.relativeDualizingComplex_isRelativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingDiagonal.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UpperShriek/RelativeDualizingDiagonal.lean#L370).

> **Stacks Project, Tag 0E2E.**  Let `φ : R → A` be a flat homomorphism of finite type of
> Noetherian rings.  Then the relative dualizing complex `ω^•_{A/R} = φ^!(R)` is a relative
> dualizing complex in the sense of [stacks 0E2C]; here `φ^!` is read at `p`, which is an arbitrary
> polynomial presentation of `φ`.
>
> Relative perfection is [stacks 0BZW] (2)(a),
> `Dualizing.PolynomialPresentation.relativeDualizingComplex_isRelativelyPerfect`, and the diagonal
> condition is `Dualizing.PolynomialPresentation.relativeDualizingComplex_diagonalDerivedHom`, from
> flat base change [stacks 0BZN], the composition [stacks 0BZT] and the independence of the
> presentation [stacks 0BZJ].  Finite presentation of `φ`, which [stacks 0E2C] is stated for, is
> not a hypothesis: a flat map of finite type of Noetherian rings is of finite presentation, and a
> polynomial presentation exists only for a map of finite type.

```lean
theorem relativeDualizingComplex_isRelativeDualizingComplex
    [IsNoetherianRing R] [IsNoetherianRing A]
    (p : PolynomialPresentation (algebraMap R A)) (hflat : (algebraMap R A).Flat) :
    letI : Module.Flat R A := RingHom.flat_algebraMap_iff.mp hflat
    letI : Algebra.FinitePresentation R A :=
      Algebra.FinitePresentation.of_finiteType.mp (RingHom.finiteType_algebraMap.mp p.finiteType)
    IsRelativeDualizingComplex R A
      (p.upperShriekFunctor.{u, 0}.obj
        ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)))
```

## Tag 0E2F, a lemma

[Tag 0E2F](https://stacks.math.columbia.edu/tag/0E2F) in the Stacks Project.

**`Dualizing.exists_isRelativeDualizingComplex_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RelativeExistenceInputs.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RelativeExistenceInputs.lean#L206). The attribute's comment: “(1)”.

> **Stacks Project, Tag 0E2F (1).** A flat ring map of finite presentation `R → A` admits a
> relative dualizing complex.
>
> The source's proof: a Noetherian model `R₀ → A₀` of `R → A` has the relative dualizing complex
> `φ₀^!(R₀)` of [stacks 0E2E], and its derived base change to `A` is one by (2) at the model and
> transitivity of derived base change.

```lean
theorem exists_isRelativeDualizingComplex_of_flat (R A : Type u) [CommRing R] [CommRing A]
    [Algebra R A] [Module.Flat R A] [Algebra.FinitePresentation R A] :
    ∃ K : DerivedCategory (ModuleCat.{u} A), IsRelativeDualizingComplex R A K
```

**`Dualizing.IsRelativeDualizingComplex.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RelativeExistenceInputs.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RelativeExistenceInputs.lean#L215). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0E2F (2).** Let `R → A` be a flat ring map of finite presentation, `K`
> a relative dualizing complex for `R → A` and `R → R'` any ring map. Then
> `K' = K ⊗ᴸ_A (A ⊗_R R')` is a relative dualizing complex for `R' → A ⊗_R R'`.

```lean
theorem IsRelativeDualizingComplex.baseChange {R A : Type u} [CommRing R] [CommRing A]
    [Algebra R A] [Module.Flat R A] [Algebra.FinitePresentation R A]
    {K : DerivedCategory (ModuleCat.{u} A)} (hK : IsRelativeDualizingComplex R A K)
    (R' : Type u) [CommRing R'] [Algebra R R'] :
    letI : Module.Flat R' (A ⊗[R] R') := flat_baseChange R A R'
    letI : Algebra.FinitePresentation R' (A ⊗[R] R') :=
      Algebra.FinitePresentation.equiv (baseChangeComm R A R')
    IsRelativeDualizingComplex R' (A ⊗[R] R')
      ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
        (Algebra.TensorProduct.includeLeftRingHom : A →+* A ⊗[R] R')).functor.obj K)
```

**`Dualizing.IsRelativeDualizingComplex.span_derivedBaseChange_diagonalGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RelativeExistenceInputs.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RelativeExistenceInputs.lean#L235). The attribute's comment: “moreover clause”.

> **Stacks Project, Tag 0E2F, the "moreover" clause.** Let `R → A` be flat of finite
> presentation, `K` a relative dualizing complex for `R → A`, and `ξ : A ⟶ K ⊗ᴸ_A (A ⊗_R A)` a
> generator of the cyclic module `Hom_{D(A ⊗_R A)}(A, K ⊗ᴸ_A (A ⊗_R A))`. For every `R → R'` the
> derived base change of `ξ` along `A ⊗_R A → A' ⊗_{R'} A'` generates
> `Hom_{D(A' ⊗_{R'} A')}(A', K' ⊗ᴸ_{A'} (A' ⊗_{R'} A'))`, through any identifications `eΔ` of the
> base change of `A` with `A'` and `eM` of the base change of `K ⊗ᴸ_A (A ⊗_R A)` with
> `K' ⊗ᴸ_{A'} (A' ⊗_{R'} A')`.

```lean
theorem IsRelativeDualizingComplex.span_derivedBaseChange_diagonalGenerator {R A : Type u}
    [CommRing R] [CommRing A] [Algebra R A] [Module.Flat R A] [Algebra.FinitePresentation R A]
    {K : DerivedCategory (ModuleCat.{u} A)} (hK : IsRelativeDualizingComplex R A K)
    (R' : Type u) [CommRing R'] [Algebra R R']
    (ξ : diagonalSingle R A ⟶ (diagonalDerivedExtension R A).obj K)
    (hξ : Submodule.span (A ⊗[R] A) ({ξ} : Set _) = ⊤) :
    letI : Module.Flat R' (A ⊗[R] R') := flat_baseChange R A R'
    ∀ (eΔ : (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
            (envelopingBaseChangeRingHom R A R')).functor.obj (diagonalSingle R A) ≅
          diagonalSingle R' (A ⊗[R] R'))
      (eM : (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
            (envelopingBaseChangeRingHom R A R')).functor.obj
              ((diagonalDerivedExtension R A).obj K) ≅
          (diagonalDerivedExtension R' (A ⊗[R] R')).obj
            ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
              (Algebra.TensorProduct.includeLeftRingHom : A →+* A ⊗[R] R')).functor.obj K)),
      Submodule.span ((A ⊗[R] R') ⊗[R'] (A ⊗[R] R'))
        ({eΔ.inv ≫ (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
          (envelopingBaseChangeRingHom R A R')).functor.map ξ ≫ eM.hom} : Set _) = ⊤
```

## Tag 0E2G, a lemma

[Tag 0E2G](https://stacks.math.columbia.edu/tag/0E2G) in the Stacks Project.

**`Dualizing.isIso_relativeHomothety_of_isRelativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RelativeHomothetyGeneral.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RelativeHomothetyGeneral.lean#L241).

> **Stacks Project, Tag 0E2G.**  Let `R → A` be a flat ring map of finite presentation and let
> `K` be a relative dualizing complex for `R → A` ([stacks 0E2C]).  Then the canonical map
> `A ⟶ RHom_A(K, K)` is an isomorphism.
>
> This is `Dualizing.isIso_relativeHomothety_of_isRelativeDualizingComplex_of_uniqueness` with the
> uniqueness of relative dualizing complexes supplied by [stacks 0E2D],
> `Dualizing.IsRelativeDualizingComplex.nonempty_iso`.  The proof is the source's: reduction to a
> Noetherian model by [stacks 02JO], the Noetherian case through [stacks 0E2E], [stacks 0E2F] and
> [stacks 0BZW], and the passage to an arbitrary base by [stacks 0DHX]; see the module
> documentation.

```lean
theorem isIso_relativeHomothety_of_isRelativeDualizingComplex
    {R A : Type u} [CommRing R] [CommRing A] [Algebra R A] [Module.Flat R A]
    [Algebra.FinitePresentation R A] (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsRelativeDualizingComplex R A K) :
    IsIso (relativeHomothety A K)
```

## Tag 0E2H, a lemma

[Tag 0E2H](https://stacks.math.columbia.edu/tag/0E2H) in the Stacks Project.

**`Dualizing.isRelativeDualizingComplex_derivedTensorProductOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RelativeCompositionTag.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RelativeCompositionTag.lean#L175).

> **Stacks 0E2H.**  Let `R → A → B` be ring maps which are flat and of finite presentation,
> let `K_{A/R}` be a relative dualizing complex for `R → A` and `K_{B/A}` one for `A → B`.  Then
> `K = K_{A/R} ⊗ᴸ_A K_{B/A}` is a relative dualizing complex for `R → B`.
>
> Clause (1) of [stacks 0E2C] is `Dualizing.relativelyPerfectOverBase_derivedTensorProductOver`
> and clause (2) follows from the isomorphism (★),
> `Dualizing.diagonalQuotientDerivedHom_derivedTensorProductOver`; see the module
> documentation.

```lean
theorem isRelativeDualizingComplex_derivedTensorProductOver
    (KA : DerivedCategory (ModuleCat.{u} A)) (KB : DerivedCategory (ModuleCat.{u} B))
    (hKA : IsRelativeDualizingComplex R A KA)
    (hKB : IsRelativeDualizingComplex A B KB) :
    letI : Module.Flat R B := Module.Flat.trans R A B
    letI : Algebra.FinitePresentation R B := Algebra.FinitePresentation.trans R A B
    IsRelativeDualizingComplex R B
      ((derivedTensorProductOver.{u, u} (algebraMap A B) KB).obj KA)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.27, Tag 0E2B](https://stacks.math.columbia.edu/tag/0E2B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
