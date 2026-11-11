---
declaration: section
origin: cited
lean: Dualizing.isDualizingComplex_of_faithfullyFlat, Dualizing.isDualizingComplex_iff_derivedExtensionScalars_of_syntomic_unconditional, Dualizing.isDualizingComplex_iff_derivedExtensionScalars_of_faithfullyFlat_lci_unconditional, Dualizing.isDualizingComplex_iff_derivedExtensionScalars_of_gorensteinFibres_unconditional, Dualizing.exists_isInjectiveHull_tensorProduct, Module.tensorProduct_injective_of_flat_of_map_comap_eq
statement: formalized
proof: formalized
---

# 47.26 More on dualizing complexes

Section 47.26 of the Stacks Project, [Tag 0E49](https://stacks.math.columbia.edu/tag/0E49). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E4A, a lemma

[Tag 0E4A](https://stacks.math.columbia.edu/tag/0E4A) in the Stacks Project.

**`Dualizing.isDualizingComplex_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/FaithfullyFlatDescent.lean, line 933](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/FaithfullyFlatDescent.lean#L933).

> **Stacks Project, Tag 0E4A.** If a complex becomes dualizing after faithfully flat
> base change between Noetherian rings, then it was already dualizing.

```lean
public theorem isDualizingComplex_of_faithfullyFlat
    {A : Type u} {B : Type w} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (f : A →+* B) (hf : f.FaithfullyFlat)
    (K : DerivedCategory (ModuleCat.{max v u w} A))
    (hK : IsDualizingComplex
      ((CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsGeneral.{u, v, w}
        f).functor.obj K)) :
    IsDualizingComplex K
```

## Tag 0E4D, a lemma

[Tag 0E4D](https://stacks.math.columbia.edu/tag/0E4D) in the Stacks Project.

**`Dualizing.isDualizingComplex_iff_derivedExtensionScalars_of_syntomic_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/SyntomicBaseChangeUnconditional.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/SyntomicBaseChangeUnconditional.lean#L322). The attribute's comment: “case (1): A → B syntomic and surjective on spectra”.

> **Stacks Project, Tag 0E4D, case (1).**  Let `φ : A → B` be a syntomic homomorphism of
> Noetherian rings which is surjective on spectra.  Then `K` in `D(A)` is a dualizing complex for
> `A` if and only if `K ⊗_A^L B` is a dualizing complex for `B`.
>
> Descent is [Stacks, Tag 0E4A] through the faithful flatness that syntomicity and surjectivity on
> spectra give ([Stacks, Tag 07D3] and [Stacks, Tag 00HQ]).  Ascent is [Stacks, Tag 0BZL] at a
> polynomial presentation of `φ`, which exists because a syntomic map is of finite type, together
> with the two inputs proved above: syntomic is a local complete intersection, so
> `Dualizing.isInvertible_relativeDualizingUnit_of_isLocalCompleteIntersection` supplies the
> invertibility of `ω^•_{B/A}` and
> `Dualizing.nonempty_upperShriekFunctor_obj_iso_derivedExtensionScalars_tensor_of_lci`
> the tensor formula.

```lean
theorem isDualizingComplex_iff_derivedExtensionScalars_of_syntomic_unconditional
    (f : A →+* B) (hsyn : letI := f.toAlgebra; Algebra.Syntomic A B)
    (hsurj : Function.Surjective (PrimeSpectrum.comap f))
    (K : DerivedCategory (ModuleCat.{u} A)) :
    IsDualizingComplex K ↔
      IsDualizingComplex ((derivedExtensionScalarsGeneral.{u, u, u} f).functor.obj K)
```

**`Dualizing.isDualizingComplex_iff_derivedExtensionScalars_of_faithfullyFlat_lci_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/SyntomicBaseChangeUnconditional.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/SyntomicBaseChangeUnconditional.lean#L344). The attribute's comment: “case (2): A → B faithfully flat and a local complete intersection”.

> **Stacks Project, Tag 0E4D, case (2).**  Let `φ : A → B` be a faithfully flat local complete
> intersection homomorphism of Noetherian rings.  Then `K` in `D(A)` is a dualizing complex for `A`
> if and only if `K ⊗_A^L B` is a dualizing complex for `B`.
>
> Descent is [Stacks, Tag 0E4A] at the given faithful flatness.  Ascent is [Stacks, Tag 0BZL] at a
> polynomial presentation of `φ`, which exists because a local complete intersection is of finite
> type, together with the two inputs proved above from `hlci`.

```lean
theorem isDualizingComplex_iff_derivedExtensionScalars_of_faithfullyFlat_lci_unconditional
    (f : A →+* B) (hff : f.FaithfullyFlat)
    (hlci : RingHom.IsLocalCompleteIntersection f) (K : DerivedCategory (ModuleCat.{u} A)) :
    IsDualizingComplex K ↔
      IsDualizingComplex ((derivedExtensionScalarsGeneral.{u, u, u} f).functor.obj K)
```

**`Dualizing.isDualizingComplex_iff_derivedExtensionScalars_of_gorensteinFibres_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/SyntomicBaseChangeUnconditional.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/SyntomicBaseChangeUnconditional.lean#L365). The attribute's comment: “case (3): A → B faithfully flat of finite type with Gorenstein fibres”.

> **Stacks Project, Tag 0E4D, case (3).**  Let `A → B` be a faithfully flat homomorphism of
> finite type of Noetherian rings and assume every fibre `B ⊗_A κ(q)` is Gorenstein.  Then `K` in
> `D(A)` is a dualizing complex for `A` if and only if `K ⊗_A^L B` is a dualizing complex for `B`.
>
> Descent is [Stacks, Tag 0E4A].  Ascent is [Stacks, Tag 0BZL] at a polynomial presentation `p`,
> which exists by finite type, together with two inputs: the invertibility of `ω^•_{B/A}`, which
> comes from the Gorenstein fibres by [Stacks, Tag 0E4C], and the tensor formula, whose only input
> is perfectness of `B` over the polynomial algebra of `p`, supplied by the flatness contained in
> `hff` through `Dualizing.PolynomialPresentation.isPerfectModule_of_flat`.

```lean
theorem isDualizingComplex_iff_derivedExtensionScalars_of_gorensteinFibres_unconditional
    [Algebra A B] (hff : (algebraMap A B).FaithfullyFlat) [Algebra.FiniteType A B]
    (hGor : ∀ (q : Ideal A) [q.IsPrime],
      letI := Algebra.FiniteType.isNoetherianRing q.ResidueField (q.Fiber B)
      IsGorensteinRing (q.Fiber B))
    (K : DerivedCategory (ModuleCat.{u} A)) :
    IsDualizingComplex K ↔
      IsDualizingComplex
        ((derivedExtensionScalarsGeneral.{u, u, u} (algebraMap A B)).functor.obj K)
```

## Tag 0E4E, a lemma

[Tag 0E4E](https://stacks.math.columbia.edu/tag/0E4E) in the Stacks Project.

**`Dualizing.exists_isInjectiveHull_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Complex/More.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Complex/More.lean#L730).

> Under a flat local homomorphism of Noetherian local rings whose target maximal ideal is
> extended from the source, the base change of an injective hull of the source residue field is an
> injective hull of the target residue field.

```lean
theorem exists_isInjectiveHull_tensorProduct
    (A B E : Type u) [CommRing A] [CommRing B]
    [IsLocalRing A] [IsLocalRing B] [IsNoetherianRing A] [IsNoetherianRing B]
    [Algebra A B] [IsLocalHom (algebraMap A B)] [Module.Flat A B]
    (hmax : Ideal.map (algebraMap A B) (IsLocalRing.maximalIdeal A) =
      IsLocalRing.maximalIdeal B)
    [AddCommGroup E] [Module A E]
    (i : ModuleCat.of A (IsLocalRing.ResidueField A) ⟶ ModuleCat.of A E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    ∃ j : ModuleCat.of B (IsLocalRing.ResidueField B) ⟶
        ModuleCat.of B (TensorProduct A B E),
      ∃ _ : Mono j, Module.IsInjectiveHull j
```

## Tag 0E4F, a lemma

[Tag 0E4F](https://stacks.math.columbia.edu/tag/0E4F) in the Stacks Project.

**`Module.tensorProduct_injective_of_flat_of_map_comap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualizingComplexes/InjectiveBaseChange.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualizingComplexes/InjectiveBaseChange.lean#L574).

> **Stacks Project, Tag 0E4F.** A flat map of Noetherian rings for which, locally at every
> prime of the target, that prime is generated by its contraction preserves injective modules
> under base change.

```lean
public theorem tensorProduct_injective_of_flat_of_map_comap_eq
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Algebra A B] [Module.Flat A B]
    (hprime : ∀ (q : Ideal B) [q.IsPrime],
      Ideal.map (algebraMap A (Localization.AtPrime q))
          (Ideal.comap (algebraMap A B) q) =
        Ideal.map (algebraMap B (Localization.AtPrime q)) q)
    (I : Type w) [AddCommGroup I] [Module A I] [Module.Injective A I] :
    Module.Injective B (TensorProduct A B I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.26, Tag 0E49](https://stacks.math.columbia.edu/tag/0E49)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
