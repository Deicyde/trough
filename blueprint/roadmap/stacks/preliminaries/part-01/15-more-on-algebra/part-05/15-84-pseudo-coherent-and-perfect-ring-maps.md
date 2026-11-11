---
declaration: section
origin: cited
lean: Algebra.PseudoCoherent, RingHom.IsPerfectRingMap, RingHom.isPerfectRingMap_iff_exists_finite_projective_resolution, Algebra.PseudoCoherent.of_finiteType, RingHom.isPerfectRingMap_of_flat_of_finitePresentation, RingHom.isPerfectRingMap_of_finiteType_of_isRegularRing, RingHom.IsLocalCompleteIntersection.isPerfectRingMap, PseudoCoherence.relativelyPseudoCoherent_iff_pseudoCoherent
statement: formalized
proof: formalized
---

# 15.84 Pseudo-coherent and perfect ring maps

Section 15.84 of the Stacks Project, [Tag 067G](https://stacks.math.columbia.edu/tag/067G). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 067H, a definition

[Tag 067H](https://stacks.math.columbia.edu/tag/067H) in the Stacks Project.

**`Algebra.PseudoCoherent`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean#L88). The attribute's comment: “(1)”.

> An `A`-algebra `B` is *pseudo-coherent* if `B` is a quotient `A[x₁, …, xₙ] ⧸ I` of a
> polynomial algebra such that the `A[x₁, …, xₙ]`-module `A[x₁, …, xₙ] ⧸ I` has a resolution by
> finite free modules.
>
> This is Stacks 067H (1) in the form of the remark that follows it, with `B` replaced by the
> isomorphic `A[x₁, …, xₙ]`-module `A[x₁, …, xₙ] ⧸ I`, which lives in the universe of `A`. By
> Stacks 0675 it says that `A → B` is of finite type and that `B`, as a module over itself, is
> pseudo-coherent relative to `A` (for `A` and `B` in one universe,
> `Algebra.pseudoCoherent_iff_exists_isModuleRelativelyPseudoCoherent`). The resolution then exists
> over every finite polynomial presentation
> (`Algebra.PseudoCoherent.nonempty_finiteFreeModuleResolution`). When `A` and `B` live in one
> universe, the condition is the same for `B` itself, made an `A[x₁, …, xₙ]`-module through the
> presentation (`Algebra.PseudoCoherent.nonempty_finiteFreeModuleResolution_quotient_iff_compHom`).

```lean
public class Algebra.PseudoCoherent (A : Type u) (B : Type v) [CommRing A] [CommRing B]
    [Algebra A B] : Prop
```

**`RingHom.IsPerfectRingMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Defs.lean#L114). The attribute's comment: “(2)”. References: SGA 6 III (4.1), “affine case”.

> A ring map `A → B` is perfect if it is pseudo-coherent and `B`, regarded as an `A`-module, has
> finite Tor dimension, read off the certified derived tensor product `derivedTensor` on a model of
> `D(A)`. Neither the model nor the certificate matters
> (`RingHom.isPerfectRingMap_iff_exists_flat_roof`).

```lean
public def IsPerfectRingMap
    (A : Type u) (B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    [HasDerivedCategory.{w} (ModuleCat.{u} A)]
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparison : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} A,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) : Prop
```

## Tag 068Y, a lemma

[Tag 068Y](https://stacks.math.columbia.edu/tag/068Y) in the Stacks Project.

**`RingHom.isPerfectRingMap_iff_exists_finite_projective_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/PerfectPresentation.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/PerfectPresentation.lean#L276).

> **Stacks 068Y.** A ring map `A → B` is perfect if and only if there is a presentation
> `B = A[x_1, …, x_n]/I` for which `B`, as a module over `A[x_1, …, x_n]`, admits a finite
> resolution by finite projective `A[x_1, …, x_n]`-modules.

```lean
public theorem isPerfectRingMap_iff_exists_finite_projective_resolution
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparison : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} A,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    IsPerfectRingMap A B derivedTensor comparison isLeftDerived ↔
      ∃ (n : ℕ) (α : MvPolynomial (Fin n) A →ₐ[A] B), Function.Surjective α ∧
        let : Module (MvPolynomial (Fin n) A) B := Module.compHom B α.toRingHom
        ∃ (d : ℕ) (F : ModuleResolution (MvPolynomial (Fin n) A) B),
          (∀ i : ℕ, Module.Finite (MvPolynomial (Fin n) A) (F.complex.X i) ∧
            Module.Projective (MvPolynomial (Fin n) A) (F.complex.X i)) ∧
          ∀ i : ℕ, d < i → IsZero (F.complex.X i)
```

## Tag 067I, a lemma

[Tag 067I](https://stacks.math.columbia.edu/tag/067I) in the Stacks Project.

**`Algebra.PseudoCoherent.of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Noetherian.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Noetherian.lean#L38). References: SGA 6 III (1.3), “third example, affine”.

> **Stacks 067I.** A finite-type ring map whose source is Noetherian is pseudo-coherent.

```lean
public theorem of_finiteType
    (A : Type u) (B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [Algebra.FiniteType A B] :
    Algebra.PseudoCoherent A B
```

## Tag 067J, a lemma

[Tag 067J](https://stacks.math.columbia.edu/tag/067J) in the Stacks Project.

**`RingHom.isPerfectRingMap_of_flat_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Flat.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Flat.lean#L320).

> **Stacks 067J.** A flat ring map of finite presentation is perfect: it is pseudo-coherent,
> and its target has finite Tor dimension over its source for every certified derived tensor
> product.

```lean
public theorem isPerfectRingMap_of_flat_of_finitePresentation
    (A : Type u) (B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    [Module.Flat A B] [Algebra.FinitePresentation A B] :
    Algebra.PseudoCoherent A B ∧
    ∀ (derivedTensor : DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
      (comparison : ∀ N : ModuleCat.{u} A,
        DerivedCategory.Q ⋙ derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
          (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
      (isLeftDerived : ∀ N : ModuleCat.{u} A,
        (derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
          (comparison N)
          (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))),
      IsPerfectRingMap A B derivedTensor comparison isLeftDerived
```

## Tag 067K, a lemma

[Tag 067K](https://stacks.math.columbia.edu/tag/067K) in the Stacks Project.

**`RingHom.isPerfectRingMap_of_finiteType_of_isRegularRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Regular.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Regular.lean#L75).

> **Stacks 067K.** A finite-type ring map out of a regular ring is perfect: it is
> pseudo-coherent, and its target has finite Tor dimension as a module over its source, for every
> certified derived tensor product.
>
> The source assumes in addition that the regular ring has finite Krull dimension; that hypothesis
> is not needed, because the bound on the length of the resolution is produced from
> quasi-compactness of the prime spectrum of the polynomial ring rather than from a bound on its
> global dimension.

```lean
public theorem isPerfectRingMap_of_finiteType_of_isRegularRing
    (A : Type u) (B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    [IsRegularRing A] [Algebra.FiniteType A B]
    (derivedTensor : DerivedCategory (ModuleCat.{u} A) ⥤
      DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparison : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙ derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
          (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} A,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    IsPerfectRingMap A B derivedTensor comparison isLeftDerived
```

## Tag 07EN, a lemma

[Tag 07EN](https://stacks.math.columbia.edu/tag/07EN) in the Stacks Project.

**`RingHom.IsLocalCompleteIntersection.isPerfectRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/CompleteIntersection.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/CompleteIntersection.lean#L273). References: SGA 6 III (4.1.1), “second part, affine”; SGA 6 VIII (1.7), “affine case”.

> **Stacks 07EN.** A local complete intersection homomorphism is perfect.

```lean
public theorem IsLocalCompleteIntersection.isPerfectRingMap
    {A : Type u} {B : Type u} [CommRing A] [CommRing B] (f : A →+* B)
    (h : IsLocalCompleteIntersection f)
    (derivedTensor :
      DerivedCategory (ModuleCat.{u} A) ⥤
        DerivedCategory (ModuleCat.{u} A) ⥤ DerivedCategory (ModuleCat.{u} A))
    (comparison : ∀ N : ModuleCat.{u} A,
      DerivedCategory.Q ⋙
          derivedTensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N) ⟶
        (StacksDraft.TorAmplitude.tensorModuleRight N).mapHomologicalComplex
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    (isLeftDerived : ∀ N : ModuleCat.{u} A,
      (derivedTensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N)).IsLeftDerivedFunctor
        (comparison N)
        (HomologicalComplex.quasiIso (ModuleCat.{u} A) (ComplexShape.up ℤ))) :
    letI := f.toAlgebra
    IsPerfectRingMap A B derivedTensor comparison isLeftDerived
```

## Tag 0DHQ, a lemma

[Tag 0DHQ](https://stacks.math.columbia.edu/tag/0DHQ) in the Stacks Project.

**`PseudoCoherence.relativelyPseudoCoherent_iff_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Absolute.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Absolute.lean#L132).

> **Stacks 0DHQ.** Let `R → A` be a pseudo-coherent ring map. An object of `D(A)` is
> `m`-pseudo-coherent relative to `R` exactly when it is `m`-pseudo-coherent, and it is
> pseudo-coherent relative to `R` exactly when it is pseudo-coherent.

```lean
public theorem relativelyPseudoCoherent_iff_pseudoCoherent
    {R : Type u} {A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    (hRA : Algebra.PseudoCoherent R A)
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) :
    (IsRelativelyPseudoCoherentFrom (R := R) K m ↔ IsPseudoCoherentFrom K m) ∧
    (IsRelativelyPseudoCoherent (R := R) K ↔ IsPseudoCoherent K)
```

## Tag 0E1T, a lemma

[Tag 0E1T](https://stacks.math.columbia.edu/tag/0E1T) in the Stacks Project.

**`PseudoCoherence.pseudoCoherent_tfae_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/PseudoCoherentMap/Surjection.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/PseudoCoherentMap/Surjection.lean#L51).

> For a surjection `B → A` of flat, finitely presented `R`-algebras, absolute
> pseudo-coherence in `D(A)`, relative pseudo-coherence over `R` and over `A`, and the two
> analogous conditions after restriction of scalars to `B` are equivalent; the same holds for
> `m`-pseudo-coherence.

```lean
public theorem pseudoCoherent_tfae_of_surjective
    {R : Type u} {B : Type u} {A : Type u}
    [CommRing R] [CommRing B] [CommRing A]
    [Algebra R B] [Algebra B A] [Algebra R A] [IsScalarTower R B A]
    [Module.Flat R B] [Algebra.FinitePresentation R B]
    [Module.Flat R A] [Algebra.FinitePresentation R A]
    (hsurj : Function.Surjective (algebraMap B A))
    (K : DerivedCategory (ModuleCat.{u} A)) (m : ℤ) :
    let Kₑ := (ModuleCat.restrictScalars.{u} (algebraMap B A)).mapDerivedCategory.obj K
    List.TFAE [
      IsPseudoCoherent K,
      IsRelativelyPseudoCoherent (R := R) K,
      IsRelativelyPseudoCoherent (R := A) K,
      IsPseudoCoherent Kₑ,
      IsRelativelyPseudoCoherent (R := R) Kₑ] ∧
    List.TFAE [
      IsPseudoCoherentFrom K m,
      IsRelativelyPseudoCoherentFrom (R := R) K m,
      IsRelativelyPseudoCoherentFrom (R := A) K m,
      IsPseudoCoherentFrom Kₑ m,
      IsRelativelyPseudoCoherentFrom (R := R) Kₑ m]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.84, Tag 067G](https://stacks.math.columbia.edu/tag/067G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
