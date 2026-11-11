---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.exists_faithfullyFlat_ind_etale_algebra_splitting_etale, AlgebraicGeometry.ProEtale.mk_splittingAlgebra_le, AlgebraicGeometry.ProEtale.mk_iteratedSplittingColimit_le, AlgebraicGeometry.ProEtale.iteratedSplittingColimit_splits_etale, AlgebraicGeometry.ProEtale.exists_small_faithfullyFlat_ind_etale_algebra_splitting_etale, AlgebraicGeometry.ProEtale.etale_faithfullyFlat_retracts_quotient, AlgebraicGeometry.ProEtale.localizationAtPrime_strictlyHenselian_of_etale_faithfullyFlat_retracts, AlgebraicGeometry.ProEtale.etale_faithfullyFlat_retracts_localizationRing
statement: formalized
proof: formalized
---

# 61.8 Constructing ind-étale algebras

Section 61.8 of the Stacks Project, [Tag 097Q](https://stacks.math.columbia.edu/tag/097Q). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 097R, a lemma

[Tag 097R](https://stacks.math.columbia.edu/tag/097R) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_faithfullyFlat_ind_etale_algebra_splitting_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/Splitting.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/Splitting.lean#L42).

> There is a faithfully flat ind-étale `A`-algebra such that every faithfully flat étale
> algebra over it has a retraction.

```lean
theorem exists_faithfullyFlat_ind_etale_algebra_splitting_etale
    (A : Type u) [CommRing A] :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
      (algebraMap A C).FaithfullyFlat ∧
        ObjectProperty.ind.{u}
          (fun D : Under (CommRingCat.of A) ↦ D.hom.hom.Etale)
          (Under.mk (CommRingCat.ofHom (algebraMap A C))) ∧
        ∀ (B : Type u) [CommRing B] [Algebra C B],
          (algebraMap C B).FaithfullyFlat → Algebra.Etale C B →
            Nonempty (B →ₐ[C] C)
```

## Tag 097S, a remark

[Tag 097S](https://stacks.math.columbia.edu/tag/097S) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.mk_splittingAlgebra_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/Cardinality.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/Cardinality.lean#L110). The attribute's comment: “the bound on T(A)”.

> The cardinality of `T(A)` is at most every infinite cardinal which bounds the cardinality
> of `A`.

```lean
theorem mk_splittingAlgebra_le (A : Type u) [CommRing A]
    (k : Cardinal.{u}) (hk : ℵ₀ ≤ k) (hA : Cardinal.mk A ≤ k) :
    Cardinal.mk (splittingAlgebra A) ≤ k
```

**`AlgebraicGeometry.ProEtale.mk_iteratedSplittingColimit_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/Cardinality.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/Cardinality.lean#L131). The attribute's comment: “the bound on the iterated construction”.

> The colimit ring obtained by iterating `T` has the same cardinality bound as the ring it is
> built from.

```lean
theorem mk_iteratedSplittingColimit_le (A : CommRingCat.{u})
    (k : Cardinal.{u}) (hk : ℵ₀ ≤ k) (hA : Cardinal.mk A ≤ k) :
    Cardinal.mk (iteratedSplittingColimit A) ≤ k
```

**`AlgebraicGeometry.ProEtale.iteratedSplittingColimit_splits_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/IteratedColimit.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/IteratedColimit.lean#L297). The attribute's comment: “the properties of the iterated construction”.

> The sequential colimit of the iterated splitting rings is a faithfully flat ind-étale
> `A`-algebra over which every faithfully flat étale algebra admits a retraction. Its `A`-algebra
> structure is induced by the first coprojection into the colimit.

```lean
theorem iteratedSplittingColimit_splits_etale (A : Type u) [CommRing A] :
    letI : Algebra A (iteratedSplittingColimit (CommRingCat.of A)) :=
      (colimit.ι (iteratedSplittingDiagram (CommRingCat.of A)) (0 : ℕ)).hom.toAlgebra
    (algebraMap A (iteratedSplittingColimit (CommRingCat.of A))).FaithfullyFlat ∧
      ObjectProperty.ind.{u}
        (fun D : Under (CommRingCat.of A) ↦ D.hom.hom.Etale)
        (Under.mk (CommRingCat.ofHom
          (algebraMap A (iteratedSplittingColimit (CommRingCat.of A))))) ∧
      ∀ (B : Type u) [CommRing B]
        [Algebra (iteratedSplittingColimit (CommRingCat.of A)) B],
        (algebraMap (iteratedSplittingColimit (CommRingCat.of A)) B).FaithfullyFlat →
        Algebra.Etale (iteratedSplittingColimit (CommRingCat.of A)) B →
        Nonempty (B →ₐ[(iteratedSplittingColimit (CommRingCat.of A))]
          iteratedSplittingColimit (CommRingCat.of A))
```

**`AlgebraicGeometry.ProEtale.exists_small_faithfullyFlat_ind_etale_algebra_splitting_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/IteratedColimit.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/IteratedColimit.lean#L362). The attribute's comment: “the bounded form of the first construction”.

> The faithfully flat ind-étale `A`-algebra splitting all faithfully flat étale covers can be
> chosen of cardinality at most any infinite cardinal bounding the cardinality of `A`.

```lean
theorem exists_small_faithfullyFlat_ind_etale_algebra_splitting_etale
    (A : Type u) [CommRing A] (k : Cardinal.{u})
    (hk : ℵ₀ ≤ k) (hA : Cardinal.mk A ≤ k) :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
      Cardinal.mk C ≤ k ∧
        (algebraMap A C).FaithfullyFlat ∧
        ObjectProperty.ind.{u}
          (fun D : Under (CommRingCat.of A) ↦ D.hom.hom.Etale)
          (Under.mk (CommRingCat.ofHom (algebraMap A C))) ∧
        ∀ (B : Type u) [CommRing B] [Algebra C B],
          (algebraMap C B).FaithfullyFlat → Algebra.Etale C B →
            Nonempty (B →ₐ[C] C)
```

## Tag 097U, a lemma

[Tag 097U](https://stacks.math.columbia.edu/tag/097U) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.etale_faithfullyFlat_retracts_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/QuotientRetraction.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/QuotientRetraction.lean#L45).

> If every faithfully flat étale `A`-algebra `B` admits an `A`-algebra map `B → A`, then for
> every ideal `I` of `A`, every faithfully flat étale `A ⧸ I`-algebra admits an `A ⧸ I`-algebra map
> to `A ⧸ I`.

```lean
theorem etale_faithfullyFlat_retracts_quotient
    (A : Type u) [CommRing A]
    (h : ∀ (B : Type u) [CommRing B] [Algebra A B] [Algebra.Etale A B]
      [Module.FaithfullyFlat A B], Nonempty (B →ₐ[A] A))
    (I : Ideal A) :
    ∀ (B : Type u) [CommRing B] [Algebra (A ⧸ I) B]
      [Algebra.Etale (A ⧸ I) B] [Module.FaithfullyFlat (A ⧸ I) B],
      Nonempty (B →ₐ[A ⧸ I] A ⧸ I)
```

## Tag 097V, a lemma

[Tag 097V](https://stacks.math.columbia.edu/tag/097V) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.localizationAtPrime_strictlyHenselian_of_etale_faithfullyFlat_retracts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/StrictlyHenselianFromRetractions.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/StrictlyHenselianFromRetractions.lean#L433).

> If every faithfully flat étale algebra over `A` has a retraction, then the localization
> of `A` at any maximal ideal is strictly henselian.

```lean
theorem localizationAtPrime_strictlyHenselian_of_etale_faithfullyFlat_retracts
    (A : Type u) [CommRing A]
    (h : ∀ (B : Type u) [CommRing B] [Algebra A B] [Algebra.Etale A B]
      [Module.FaithfullyFlat A B], Nonempty (B →ₐ[A] A))
    (m : Ideal A) [m.IsMaximal] :
    StrictlyHenselianLocalRing (Localization.AtPrime m)
```

## Tag 097W, a lemma

[Tag 097W](https://stacks.math.columbia.edu/tag/097W) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.etale_faithfullyFlat_retracts_localizationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/LocalizationRetraction.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtaleConstruction/LocalizationRetraction.lean#L423).

> The property that every faithfully flat étale algebra admits a retraction
> passes to the canonical localization along any closed subscheme.

```lean
theorem etale_faithfullyFlat_retracts_localizationRing
    (A : Type u) [CommRing A]
    (h : ∀ (B : Type max u v) [CommRing B] [Algebra A B] [Algebra.Etale A B]
      [Module.FaithfullyFlat A B], Nonempty (B →ₐ[A] A))
    (I : Ideal A) :
    ∀ (C : Type v) [CommRing C]
      [Algebra (localizationRing I (1 : A)) C]
      [Algebra.Etale (localizationRing I (1 : A)) C]
      [Module.FaithfullyFlat (localizationRing I (1 : A)) C],
      Nonempty (C →ₐ[localizationRing I (1 : A)]
        localizationRing I (1 : A))
```

## Tag 097X, a lemma

[Tag 097X](https://stacks.math.columbia.edu/tag/097X) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_wLocal_faithfullyFlat_indEtale_extensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WLocalIndEtaleSquare.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/WLocalIndEtaleSquare.lean#L653).

> A ring map inducing algebraic extensions on residue fields admits a commutative square of
> faithfully flat ind-étale extensions with w-local spectra, compatible closed points, and strictly
> henselian local rings at the closed points of the lower-right ring.

```lean
theorem exists_wLocal_faithfullyFlat_indEtale_extensions
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (hres : let f : AlgebraicGeometry.Spec (.of B) ⟶ AlgebraicGeometry.Spec (.of A) :=
        Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op
      ∀ x,
        letI := (f.residueFieldMap x).hom.toAlgebra
        Algebra.IsAlgebraic
          ((AlgebraicGeometry.Spec (.of A)).residueField (f x))
          ((AlgebraicGeometry.Spec (.of B)).residueField x)) :
    ∃ (C D : Type u) (_ : CommRing C) (_ : CommRing D)
      (_ : Algebra A C) (_ : Algebra A D) (_ : Algebra B D) (_ : Algebra C D)
      (_ : IsScalarTower A B D) (_ : IsScalarTower A C D),
      (algebraMap A C).FaithfullyFlat ∧
      ObjectProperty.ind.{u}
        (fun E : Under (CommRingCat.of A) ↦ E.hom.hom.Etale)
        (Under.mk (CommRingCat.ofHom (algebraMap A C))) ∧
      (algebraMap B D).FaithfullyFlat ∧
      ObjectProperty.ind.{u}
        (fun E : Under (CommRingCat.of B) ↦ E.hom.hom.Etale)
        (Under.mk (CommRingCat.ofHom (algebraMap B D))) ∧
      WLocalSpace (PrimeSpectrum C) ∧
      WLocalSpace (PrimeSpectrum D) ∧
      IsWLocalMap (PrimeSpectrum.comap (algebraMap C D)) ∧
      closedPoints (PrimeSpectrum D) =
        (PrimeSpectrum.comap (algebraMap C D)) ⁻¹' closedPoints (PrimeSpectrum C) ∧
      (∀ x : PrimeSpectrum A, ∃ y : PrimeSpectrum C,
        y ∈ closedPoints (PrimeSpectrum C) ∧
          PrimeSpectrum.comap (algebraMap A C) y = x) ∧
      (∀ x : PrimeSpectrum B, ∃ y : PrimeSpectrum D,
        y ∈ closedPoints (PrimeSpectrum D) ∧
          PrimeSpectrum.comap (algebraMap B D) y = x) ∧
      ∀ (m : Ideal C) [m.IsMaximal],
        StrictlyHenselianLocalRing (Localization.AtPrime m)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.8, Tag 097Q](https://stacks.math.columbia.edu/tag/097Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
