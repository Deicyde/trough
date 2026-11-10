---
declaration: section
origin: cited
lean: Dualizing.compareTorsionFunctors, Dualizing.TorsionCounit.isIso_derivedPowerTorsionCounit_app, Dualizing.TorsionCounit.isEquivalence_powerTorsionComparison, Dualizing.TorsionCounit.isIso_compareTorsionFunctors_app, Stacks.LocalCohomology.extendedCechComparison, Dualizing.localCohomologyOfRingBaseChangeIso, Dualizing.localCohomologyOfRingLiftedBaseChangeIso, Dualizing.derivedPowerTorsionOfRingBaseChangeIsoLocalCohomology
statement: formalized
proof: formalized
---

# 47.10 Local cohomology for Noetherian rings

Section 47.10 of the Stacks Project, [Tag 0BJD](https://stacks.math.columbia.edu/tag/0BJD). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A6U, an equation

[Tag 0A6U](https://stacks.math.columbia.edu/tag/0A6U) in the Stacks Project.

**`Dualizing.compareTorsionFunctors`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomologyDualizing/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomologyDualizing/Basic.lean#L159).

> **Stacks 0A6U.** The canonical natural transformation from derived power torsion followed
> by the comparison functor to local cohomology with support in `V(I)`.

```lean
noncomputable def compareTorsionFunctors
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    (derivedPowerTorsion.{u, v} A I hI ⋙
      powerTorsionComparison.{u, max u v} A I hI) ⟶
      localCohomologyFunctor.{u, max u v} A I hI
```

## Tag 0955, a lemma

[Tag 0955](https://stacks.math.columbia.edu/tag/0955) in the Stacks Project.

**`Dualizing.TorsionCounit.isIso_derivedPowerTorsionCounit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModelComparison/Noetherian.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModelComparison/Noetherian.lean#L430). The attribute's comment: “part (1)”.

> **Stacks 0955, part (1).** Let `A` be a Noetherian ring and `I ⊆ A` a finitely generated
> ideal. The counit `RΓ_I(K) ⟶ K` of [Stacks, Tag 0A6L] is an isomorphism at every object `K` of
> `D(A)` whose cohomology modules are `I`-power torsion.
>
> The object is represented by a K-injective complex with injective terms, where the counit is the
> degreewise torsion inclusion.

```lean
theorem isIso_derivedPowerTorsionCounit_app
    (K : PowerTorsionDerivedCategory.{u, max u v} A I hI) :
    IsIso ((derivedPowerTorsionCounit.{u, v} A I hI).app K.obj)
```

**`Dualizing.TorsionCounit.isEquivalence_powerTorsionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModelComparison/Noetherian.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModelComparison/Noetherian.lean#L458). The attribute's comment: “part (2)”.

> **Stacks 0955, part (2).** For a Noetherian ring the comparison functor
> `D(I^∞-torsion) ⥤ D_{I^∞-torsion}(A)` of [Stacks, Tag 0A6N] is an equivalence.

```lean
theorem isEquivalence_powerTorsionComparison :
    (powerTorsionComparison.{u, max u v} A I hI).IsEquivalence
```

**`Dualizing.TorsionCounit.isIso_compareTorsionFunctors_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModelComparison/Noetherian.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModelComparison/Noetherian.lean#L549). The attribute's comment: “part (3)”.

> **Stacks 0955, part (3).** Let `A` be a Noetherian ring and `I ⊆ A` a finitely generated
> ideal. The comparison `RΓ_I ⟶ RΓ_Z` of [Stacks, Tag 0A6U] is an isomorphism at every object of
> `D(A)`, with no torsion or boundedness hypothesis.
>
> Evaluate the naturality square of the comparison at the local cohomology counit
> `c : ι(RΓ_Z(K)) ⟶ K`. Its source has `I`-power-torsion cohomology, so the comparison is
> invertible there by part (1); `RΓ_Z(c)` is invertible because `RΓ_Z` is a coreflection; and
> `RΓ_I(c)` is invertible because the counit is universal among morphisms from torsion objects.

```lean
theorem isIso_compareTorsionFunctors_app
    (K : DerivedCategory (ModuleCat.{max u v} A)) :
    IsIso ((compareTorsionFunctors.{u, v} A I hI).app K)
```

## Tag 0956, a lemma

[Tag 0956](https://stacks.math.columbia.edu/tag/0956) in the Stacks Project.

**`Stacks.LocalCohomology.extendedCechComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModelComparison/ExtendedCech.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModelComparison/ExtendedCech.lean#L157).

> **Stacks 0956.** Let `A` be a Noetherian ring, let `I = (f₁, …, f_r)` be an ideal of `A` and
> let `Z = V(I)`. For every `A`-module `M` there are canonical isomorphisms
> `RΓ_I(M) ≅ C^•(f₁, …, f_r; M) ≅ RΓ_Z(M)` in `D(A)`, the middle term being the extended
> alternating Čech complex; the first carries the Čech augmentation to the structure map of
> `RΓ_I(M)` and the second carries the local-cohomology counit back to the Čech augmentation,
> which is what makes the pair canonical.

```lean
def extendedCechComparison (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    {r : ℕ} (f : Fin r → A) (hIf : Ideal.span (Set.range f) = I)
    (M : ModuleCat.{max u v} A) :
    { e : (derivedPowerTorsionObj.{u, v} A I (Ideal.fg_of_isNoetherianRing I) M ≅
              extendedCechObject f M) ×
            (extendedCechObject f M ≅
              (localCohomologyOnModules.{u, max u v} A I
                (Ideal.fg_of_isNoetherianRing I)).obj M) //
        e.1.hom ≫ extendedCechAugmentationHom f M =
            derivedPowerTorsionObjCounit.{u, v} A I (Ideal.fg_of_isNoetherianRing I) M ∧
          e.2.hom ≫ (Dualizing.localCohomologyAdjunction A I
              (Ideal.fg_of_isNoetherianRing I)).counit.app
                ((DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj M) =
            extendedCechAugmentationHom f M }
```

## Tag 0957, a lemma

[Tag 0957](https://stacks.math.columbia.edu/tag/0957) in the Stacks Project.

**`Dualizing.localCohomologyOfRingBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRings.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRings.lean#L86). The attribute's comment: “base change on regular modules”.

> **Stacks 0957.** Local cohomology of the regular module commutes with derived extension of
> scalars along a homomorphism of commutative rings, for a finitely generated ideal.

```lean
def localCohomologyOfRingBaseChangeIso (A B : Type uA) [CommRing A] [CommRing B]
    (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    (derivedExtensionScalarsGeneral.{uA, 0, uA} f).functor.obj (localCohomologyOfRing A I hI) ≅
      localCohomologyOfRing B (I.map f) (hI.map f)
```

**`Dualizing.localCohomologyOfRingLiftedBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRings.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRings.lean#L129). The attribute's comment: “base change across universes”.

> **Stacks 0957.** The change-of-rings isomorphism for local cohomology of the regular module,
> for two rings in independent universes, after transporting both regular modules into a common
> module universe.

```lean
def localCohomologyOfRingLiftedBaseChangeIso (A : Type uA) (B : Type uB) [CommRing A]
    [CommRing B] (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    (derivedExtensionScalarsGeneral.{uA, max uA uB, uB} f).functor.obj
        (localCohomologyOfRingLifted.{uA, max uA uB} A I hI) ≅
      localCohomologyOfRingLifted.{uB, max uA uB} B (I.map f) (hI.map f)
```

**`Dualizing.derivedPowerTorsionOfRingBaseChangeIsoLocalCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean#L142). The attribute's comment: “first equality: RΓ_I(A) ⊗ᴸ B = RΓ_Z(A) ⊗ᴸ B”.

> **Stacks 0957, the first equality.** `RΓ_I(A) ⊗ᴸ_A B ≅ RΓ_Z(A) ⊗ᴸ_A B`: derived extension of
> scalars applied to the identification of the two torsion models over the Noetherian ring `A`.

```lean
def derivedPowerTorsionOfRingBaseChangeIsoLocalCohomology (A B : Type uA) [CommRing A]
    [CommRing B] [IsNoetherianRing A] (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    (derivedExtensionScalarsGeneral.{uA, 0, uA} f).functor.obj
        (derivedPowerTorsionOfRing A I hI) ≅
      (derivedExtensionScalarsGeneral.{uA, 0, uA} f).functor.obj
        (localCohomologyOfRing A I hI)
```

**`Dualizing.localCohomologyOfRingIsoDerivedPowerTorsionOfRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean#L155). The attribute's comment: “last equality: RΓ_Y(B) = RΓ_{IB}(B)”.

> **Stacks 0957, the last equality.** `RΓ_Y(B) ≅ RΓ_{IB}(B)` for `Y = V(IB)`: the
> identification of the two torsion models over the Noetherian ring `B`, read backwards at the
> ideal `IB = Ideal.map f I`.

```lean
def localCohomologyOfRingIsoDerivedPowerTorsionOfRing (A B : Type uA) [CommRing A] [CommRing B]
    [IsNoetherianRing B] (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    localCohomologyOfRing B (I.map f) (hI.map f) ≅
      derivedPowerTorsionOfRing B (I.map f) (hI.map f)
```

**`Dualizing.derivedPowerTorsionOfRingBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean#L169). The attribute's comment: “the four-term chain, composed, for two rings in one universe”.

> **Stacks 0957, the whole chain.** For a homomorphism `f : A → B` of Noetherian rings and a
> finitely generated ideal `I ⊆ A`, there is an isomorphism
> `RΓ_I(A) ⊗ᴸ_A B ≅ RΓ_{IB}(B)` in `D(B)`, obtained by composing the three isomorphisms of the
> source: the first equality, the change-of-rings isomorphism
> `Dualizing.localCohomologyOfRingBaseChangeIso`, and the last equality.

```lean
def derivedPowerTorsionOfRingBaseChangeIso (A B : Type uA) [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B] (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    (derivedExtensionScalarsGeneral.{uA, 0, uA} f).functor.obj
        (derivedPowerTorsionOfRing A I hI) ≅
      derivedPowerTorsionOfRing B (I.map f) (hI.map f)
```

**`Dualizing.derivedPowerTorsionOfRingLiftedBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCohomologyNoetherian/ChangeOfRingsTorsion.lean#L181). The attribute's comment: “the four-term chain, composed, across universes”.

> **Stacks 0957, the whole chain, for two rings in independent universes**, after transporting
> both regular modules into a common module universe.

```lean
def derivedPowerTorsionOfRingLiftedBaseChangeIso (A : Type uA) (B : Type uB) [CommRing A]
    [CommRing B] [IsNoetherianRing A] [IsNoetherianRing B] (f : A →+* B) (I : Ideal A)
    (hI : I.FG) :
    (derivedExtensionScalarsGeneral.{uA, max uA uB, uB} f).functor.obj
        (derivedPowerTorsionOfRingLifted.{uA, max uA uB} A I hI) ≅
      derivedPowerTorsionOfRingLifted.{uB, max uA uB} B (I.map f) (hI.map f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.10, Tag 0BJD](https://stacks.math.columbia.edu/tag/0BJD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
