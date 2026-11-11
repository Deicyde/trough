---
declaration: section
origin: cited
lean: Dualizing.IsDualizingComplex, Dualizing.derivedHom_finiteCohomology, Dualizing.derivedBiduality, Dualizing.dualizingDerivedHom_biduality_isIso, Dualizing.coherentDualizingDerivedHom_isEquivalence, Dualizing.dualizingDerivedHom_plus_iff_minus, Dualizing.dualizingDerivedHom_minus_iff_plus, Dualizing.boundedCoherentDualizingDerivedHom_isEquivalence
statement: formalized
proof: formalized
---

# 47.15 Dualizing complexes

Section 47.15 of the Stacks Project, [Tag 0A7A](https://stacks.math.columbia.edu/tag/0A7A). 12 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A7B, a definition

[Tag 0A7B](https://stacks.math.columbia.edu/tag/0A7B) in the Stacks Project.

**`Dualizing.IsDualizingComplex`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Complex.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Complex.lean#L176). References: SGA 5 I (1.7), “affine/ring case”.

> A dualizing complex over a Noetherian commutative ring is a derived object of finite
> injective dimension whose cohomology modules are finite and whose homothety map to its derived
> endomorphism complex is a quasi-isomorphism.

```lean
structure IsDualizingComplex {A : Type u} [CommRing A] [IsNoetherianRing A]
    [HasDerivedCategory.{w} (ModuleCat.{v} A)]
    (K : DerivedCategory (ModuleCat.{v} A)) : Prop
```

## Tag 0G4H, a lemma

[Tag 0G4H](https://stacks.math.columbia.edu/tag/0G4H) in the Stacks Project.

**`Dualizing.derivedHom_finiteCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomFiniteCohomology.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomFiniteCohomology.lean#L544). References: SGA 5 I (App.7.3), “affine case”.

> **Stacks 0G4H.** Let `A` be a Noetherian ring and let `K` and `L` be objects of the derived
> category of `A`-modules whose cohomology modules are all finite. If `L` has finite injective
> dimension, then every cohomology module of `RHom_A(K, L)` is finite as well.

```lean
public theorem derivedHom_finiteCohomology
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K L : DerivedCategory (ModuleCat.{max u v} A))
    (hK : DerivedCategoryB.derivedCategoryB
      (fun M : ModuleCat.{max u v} A => Module.Finite A M) K)
    (hL : DerivedCategoryB.derivedCategoryB
      (fun M : ModuleCat.{max u v} A => Module.Finite A M) L)
    (hLinj : StacksDraft.InjectiveDimension.HasFiniteInjectiveDimension L) :
    DerivedCategoryB.derivedCategoryB
      (fun M : ModuleCat.{max u v} A => Module.Finite A M)
      ((derivedHomAdjunctionOverRing A).hom.obj (.op K, L))
```

## Tag 0A7C, a lemma

[Tag 0A7C](https://stacks.math.columbia.edu/tag/0A7C) in the Stacks Project.

**`Dualizing.derivedBiduality`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean#L181). The attribute's comment: “canonical biduality morphism”.

> **The canonical biduality morphisms, natural in the derived object.** Each component is the
> canonical morphism `K ⟶ RHom_A(RHom_A(K, ω), ω)` of
> `Dualizing.dualizingBidualityMor`; naturality is `Dualizing.bidualityMor_naturality` at the
> adjunction of [stacks 0A63].

```lean
def derivedBiduality (ω : DerivedCategory (ModuleCat.{max u v} A)) :
    Functor.id (DerivedCategory (ModuleCat.{max u v} A)) ⟶
      opOp (DerivedCategory (ModuleCat.{max u v} A)) ⋙
        (dualizingDerivedHomFunctor.{u, v} A ω).op ⋙
          dualizingDerivedHomFunctor.{u, v} A ω
```

**`Dualizing.dualizingDerivedHom_biduality_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean#L244). The attribute's comment: “canonical biduality”.

> **Canonical biduality is a natural isomorphism on objects with finite cohomology.** Each
> component is invertible by `Dualizing.isIso_dualizingBidualityMor_of_finiteCohomology`, and a
> morphism of a full subcategory is invertible as soon as the underlying morphism is.

```lean
theorem dualizingDerivedHom_biduality_isIso
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (hω : IsDualizingComplex ω) :
    IsIso (coherentDerivedBiduality.{u, v} A ω hω)
```

**`Dualizing.coherentDualizingDerivedHom_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean#L266). The attribute's comment: “the anti-equivalence on coherent objects”. References: SGA 5 I (App.7.3), “affine case”.

> **Derived Hom into a dualizing complex is an anti-equivalence on the derived category of
> objects with finite cohomology, [stacks 0A7C].**

```lean
theorem coherentDualizingDerivedHom_isEquivalence
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (hω : IsDualizingComplex ω) :
    (coherentDualizingDerivedHomFunctor.{u, v} A ω hω).IsEquivalence
```

**`Dualizing.dualizingDerivedHom_plus_iff_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean#L278). The attribute's comment: “exchange of bounded below and bounded above”.

> **On objects with finite cohomology, derived Hom into a dualizing complex exchanges bounded
> below with bounded above.** The forward implication is the bound exchange
> `Dualizing.dualizingDerivedHom_isLE_of_isGE`; the converse applies the other bound exchange to
> `RHom_A(K, ω)` and transports the resulting bound along canonical biduality.

```lean
theorem dualizingDerivedHom_plus_iff_minus
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (hω : IsDualizingComplex ω)
    (K : DerivedCategory (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i).obj K)) :
    (DerivedCategory.TStructure.t).plus K ↔
      (DerivedCategory.TStructure.t).minus
        ((dualizingDerivedHomFunctor.{u, v} A ω).obj (Opposite.op K))
```

**`Dualizing.dualizingDerivedHom_minus_iff_plus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean#L301). The attribute's comment: “exchange of bounded above and bounded below”.

> **On objects with finite cohomology, derived Hom into a dualizing complex exchanges bounded
> above with bounded below.** The forward implication is the bound exchange
> `Dualizing.dualizingDerivedHom_isGE_of_isLE`; the converse applies the other bound exchange to
> `RHom_A(K, ω)` and transports the resulting bound along canonical biduality.

```lean
theorem dualizingDerivedHom_minus_iff_plus
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (hω : IsDualizingComplex ω)
    (K : DerivedCategory (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i).obj K)) :
    (DerivedCategory.TStructure.t).minus K ↔
      (DerivedCategory.TStructure.t).plus
        ((dualizingDerivedHomFunctor.{u, v} A ω).obj (Opposite.op K))
```

**`Dualizing.boundedCoherentDualizingDerivedHom_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/Duality.lean#L376). The attribute's comment: “the bounded anti-equivalence”. References: SGA 5 I (App.7.3), “affine case”.

> **Derived Hom into a dualizing complex is an anti-equivalence on bounded objects with finite
> cohomology, [stacks 0A7C].**

```lean
theorem boundedCoherentDualizingDerivedHom_isEquivalence
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (hω : IsDualizingComplex ω) :
    (boundedCoherentDualizingDerivedHomFunctor.{u, v} A ω hω).IsEquivalence
```

**`Dualizing.nonempty_extIntoOmegaAtIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/ExtComparison.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomDuality/ExtComparison.lean#L428). The attribute's comment: “Ext–cohomology comparison”.

> **The Ext--cohomology comparison for derived Hom**, natural in the source module.
> The `ULift` is necessary because derived morphisms live in a larger universe than the modules in
> the derived category. This comparison does not require `ω` to be dualizing.

```lean
public theorem nonempty_extIntoOmegaAtIso
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (i : ℤ) :
    Nonempty (extIntoOmegaAt.{u, v} A ω i ≅
      (DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).op ⋙
        dualizingDerivedHomFunctor.{u, v} A ω ⋙
          DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i ⋙
            ModuleCat.uliftFunctor.{max (u + 1) (v + 1), max u v} A)
```

**`Dualizing.dualizingDerivedHomFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingDerivedHom.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingDerivedHom.lean#L115). The attribute's comment: “the functor”.

> The contravariant functor `RHom_A(-, ω)` defined using the canonical derived
> tensor--Hom adjunction.

```lean
public def dualizingDerivedHomFunctor
    (ω : DerivedCategory (ModuleCat.{max u v} A)) :
    (DerivedCategory (ModuleCat.{max u v} A))ᵒᵖ ⥤
      DerivedCategory (ModuleCat.{max u v} A)
```

**`Dualizing.dualizingDerivedHom_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingDerivedHom.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingDerivedHom.lean#L237). The attribute's comment: “preservation of bounded coherent objects”.

> On objects with finite cohomology, derived Hom into a dualizing complex preserves
> cohomological boundedness.

```lean
public theorem dualizingDerivedHom_bounded [IsNoetherianRing A]
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (hω : IsDualizingComplex ω)
    (K : DerivedCategory (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i).obj K))
    (hK' : (DerivedCategory.TStructure.t).bounded K) :
    (DerivedCategory.TStructure.t).bounded
      ((dualizingDerivedHomFunctor.{u, v} A ω).obj (.op K))
```

**`Dualizing.dualizingDerivedHom_finiteCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingDerivedHom.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingDerivedHom.lean#L264). The attribute's comment: “preservation of coherent objects”.

> Derived Hom into a dualizing complex has finite cohomology when its argument does.
>
> This is Tag 0G4H specialized to a dualizing complex as target: a dualizing complex has finite
> cohomology and finite injective dimension, which are exactly the two hypotheses that tag puts
> on its second argument.

```lean
public theorem dualizingDerivedHom_finiteCohomology [IsNoetherianRing A]
    (ω : DerivedCategory (ModuleCat.{max u v} A)) (hω : IsDualizingComplex ω)
    (K : DerivedCategory (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i).obj K)) :
    ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i).obj
        ((dualizingDerivedHomFunctor.{u, v} A ω).obj (.op K)))
```

## Tag 0A7E, a lemma

[Tag 0A7E](https://stacks.math.columbia.edu/tag/0A7E) in the Stacks Project.

**`Dualizing.isInvertible_obj_ring_of_linear_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Complexes/InvertibleImage/RingImageInvertible.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Complexes/InvertibleImage/RingImageInvertible.lean#L645).

> **Stacks 0A7E.** An `A`-linear autoequivalence of the bounded derived category of complexes
> of `A`-modules with finite cohomology, an equivalence of categories with no compatibility with
> the shift or the triangulated structure assumed, sends the ring, placed in degree zero, to an
> invertible object of the unbounded derived category.

```lean
public theorem isInvertible_obj_ring_of_linear_isEquivalence [IsNoetherianRing A]
    (F : BoundedCoherentDerivedCategory A ⥤ BoundedCoherentDerivedCategory A)
    [F.IsEquivalence] [F.Linear A] :
    let m := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory A).choose
    letI := m
    MonoidalCategory.IsInvertible (F.obj (ringObject A)).obj
```

## Tag 0A7F, a lemma

[Tag 0A7F](https://stacks.math.columbia.edu/tag/0A7F) in the Stacks Project.

**`Dualizing.IsDualizingComplex.exists_iso_derivedTensorProduct_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Complexes/Uniqueness.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Complexes/Uniqueness.lean#L501). References: SGA 5 I (2.1), “affine case”.

> Two dualizing complexes over a Noetherian ring differ by derived tensor product with an
> invertible object.

```lean
public theorem IsDualizingComplex.exists_iso_derivedTensorProduct_invertible
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {K K' : DerivedCategory (ModuleCat.{max u v} A)}
    (hK : IsDualizingComplex K) (hK' : IsDualizingComplex K') :
    ∃ T : CochainComplex.DerivedTensor.DerivedTensorProductGeneral.{u, v} A,
      ∃ m : MonoidalCategory (DerivedCategory (ModuleCat.{max u v} A)),
        letI := m
        (Nonempty (MonoidalCategory.curriedTensor _ ≅ T.tensor) ∧
          Nonempty
          (𝟙_ (DerivedCategory (ModuleCat.{max u v} A)) ≅
            (DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj
              (ModuleCat.of A (ULift.{v} A)))) ∧
          ∃ L : DerivedCategory (ModuleCat.{max u v} A),
            MonoidalCategory.IsInvertible L ∧
              Nonempty (K' ≅ (T.tensor.obj K).obj L)
```

## Tag 0A7G, a lemma

[Tag 0A7G](https://stacks.math.columbia.edu/tag/0A7G) in the Stacks Project.

**`Dualizing.isDualizingComplex_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Complex.lean, line 1024](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Complex.lean#L1024).

> The derived extension of a dualizing complex along a localization is a dualizing complex
> over the localized ring.

```lean
theorem isDualizingComplex_localization {A : Type u} {B : Type w} [CommRing A] [CommRing B]
    [Algebra A B] [IsNoetherianRing A] (S : Submonoid A) [IsLocalization S B]
    (K : DerivedCategory (ModuleCat.{v} A)) (hK : IsDualizingComplex K) :
    @IsDualizingComplex (A := B) inferInstance
      (IsLocalization.isNoetherianRing S B inferInstance) inferInstance
      ((StacksDraft.PseudoCoherence.derivedExtensionScalars (algebraMap A B)).obj K)
```

## Tag 0A7H, a lemma

[Tag 0A7H](https://stacks.math.columbia.edu/tag/0A7H) in the Stacks Project.

**`Dualizing.isDualizingComplex_of_localizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalizationCriterion.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalizationCriterion.lean#L616).

> **Stacks Project, Tag 0A7H.** A complex over a Noetherian ring is dualizing as soon as its
> derived localization at every member of a family of elements generating the unit ideal is a
> dualizing complex over the corresponding localization.

```lean
theorem isDualizingComplex_of_localizations [IsNoetherianRing A]
    {ι : Type w} (f : ι → A) (K : DerivedCategory (ModuleCat.{u} A))
    (hspan : Ideal.span (Set.range f) = ⊤)
    (hK : ∀ i, IsDualizingComplex ((localizationAwayFunctorAux.{u, u} (f i)).obj K)) :
    IsDualizingComplex K
```

## Tag 0AX0, a lemma

[Tag 0AX0](https://stacks.math.columbia.edu/tag/0AX0) in the Stacks Project.

**`Dualizing.isDualizingComplex_derivedHom_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomothety/DerivedCoextensionIsDualizing.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomothety/DerivedCoextensionIsDualizing.lean#L187).

> **Stacks Project, Tag 0AX0.** For a finite homomorphism of Noetherian rings and a dualizing
> complex `ω` over the source, `RHom_A(B, ω)` is a dualizing complex over `B`.
>
> Noetherianity of `B` follows from that of `A` and finiteness of `f`, but it is a hypothesis here
> because `Dualizing.IsDualizingComplex` is only stated over a Noetherian ring, so the conclusion
> cannot be written down without it.

```lean
theorem isDualizingComplex_derivedHom_of_finite [IsNoetherianRing A] [IsNoetherianRing B]
    (f : A →+* B) (hf : f.Finite) (ω : DerivedCategory (ModuleCat.{max v u} A))
    (hω : IsDualizingComplex ω) :
    IsDualizingComplex ((derivedHom.{u, v, u} f).obj ω)
```

## Tag 0A7I, a lemma

[Tag 0A7I](https://stacks.math.columbia.edu/tag/0A7I) in the Stacks Project.

**`Dualizing.isDualizingComplex_derivedHom_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomothety/DerivedCoextensionIsDualizing.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DerivedHomothety/DerivedCoextensionIsDualizing.lean#L187). The attribute's comment: “the surjective case, a surjection being a finite ring map”.

> **Stacks Project, Tag 0AX0.** For a finite homomorphism of Noetherian rings and a dualizing
> complex `ω` over the source, `RHom_A(B, ω)` is a dualizing complex over `B`.
>
> Noetherianity of `B` follows from that of `A` and finiteness of `f`, but it is a hypothesis here
> because `Dualizing.IsDualizingComplex` is only stated over a Noetherian ring, so the conclusion
> cannot be written down without it.

```lean
theorem isDualizingComplex_derivedHom_of_finite [IsNoetherianRing A] [IsNoetherianRing B]
    (f : A →+* B) (hf : f.Finite) (ω : DerivedCategory (ModuleCat.{max v u} A))
    (hω : IsDualizingComplex ω) :
    IsDualizingComplex ((derivedHom.{u, v, u} f).obj ω)
```

## Tag 0A7J, a lemma

[Tag 0A7J](https://stacks.math.columbia.edu/tag/0A7J) in the Stacks Project.

**`Dualizing.polynomialBaseChange_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/PolynomialBaseChange/IsDualizingComplex.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/PolynomialBaseChange/IsDualizingComplex.lean#L107).

> A dualizing complex over a Noetherian ring remains dualizing after tensoring with the
> polynomial ring in one variable.

```lean
public theorem polynomialBaseChange_isDualizingComplex {A : Type u} [CommRing A]
    [IsNoetherianRing A] (K : DerivedCategory (ModuleCat.{v} A))
    (hK : IsDualizingComplex K) :
    IsDualizingComplex (polynomialBaseChange K)
```

## Tag 0A7K, a proposition

[Tag 0A7K](https://stacks.math.columbia.edu/tag/0A7K) in the Stacks Project.

**`Dualizing.exists_isDualizingComplex_of_isEssentiallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/EssentiallyFiniteType.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/EssentiallyFiniteType.lean#L61).

> **Stacks Project, Tag 0A7K.** If a Noetherian ring `A` has a dualizing complex, then every
> `A`-algebra essentially of finite type over `A` has a dualizing complex.

```lean
theorem exists_isDualizingComplex_of_isEssentiallyOfFiniteType {A B : Type u} [CommRing A]
    [CommRing B] [IsNoetherianRing A] [Algebra A B]
    (hB : IsEssentiallyOfFiniteType A B (algebraMap A B))
    (K : DerivedCategory (ModuleCat.{u} A)) (hK : IsDualizingComplex K) :
    ∃ (hB' : IsNoetherianRing B) (L : DerivedCategory (ModuleCat.{u} B)),
      @IsDualizingComplex B _ hB' _ L
```

## Tag 0A7L, a lemma

[Tag 0A7L](https://stacks.math.columbia.edu/tag/0A7L) in the Stacks Project.

**`Dualizing.derivedHom_residueField_iso_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldShift.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/ResidueFieldShift.lean#L279).

> **Stacks Project, Tag 0A7L.** Derived Hom from the residue field at a maximal ideal into a
> dualizing complex is isomorphic to an integral shift of the residue field.

```lean
theorem derivedHom_residueField_iso_shift
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsDualizingComplex K)
    (m : Ideal A) (hm : m.IsMaximal) :
    ∃ n : ℤ, Nonempty
      ((derivedHom.{u, v, u} (Ideal.Quotient.mk m)).obj K ≅
        ((DerivedCategory.singleFunctor (ModuleCat.{max v u} (A ⧸ m)) 0).obj
          ((ModuleCat.uliftFunctor.{v} (A ⧸ m)).obj
            (ModuleCat.of (A ⧸ m) (A ⧸ m))))⟦n⟧)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.15, Tag 0A7A](https://stacks.math.columbia.edu/tag/0A7A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
