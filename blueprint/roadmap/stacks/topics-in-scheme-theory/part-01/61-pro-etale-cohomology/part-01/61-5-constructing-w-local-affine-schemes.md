---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.existsUnique_ringHom_comp_algebraMap, AlgebraicGeometry.ProEtale.range_comap_algebraMap, AlgebraicGeometry.ProEtale.homeomorphSetOfSpecializesTo, AlgebraicGeometry.ProEtale.nonvanishingSubmonoid_eq_of_basicLocallyClosed_eq, AlgebraicGeometry.ProEtale.algEquivOfBasicLocallyClosedEq, AlgebraicGeometry.ProEtale.basicLocallyClosed_eq_range_inter_zeroLocus, AlgebraicGeometry.ProEtale.surjective_quotientAwayLift, AlgebraicGeometry.ProEtale.localization_comap_range
statement: formalized
proof: formalized
---

# 61.5 Constructing w-local affine schemes

Section 61.5 of the Stacks Project, [Tag 096U](https://stacks.math.columbia.edu/tag/096U). 16 tags here are carried by 60 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 096V, a lemma

[Tag 096V](https://stacks.math.columbia.edu/tag/096V) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.existsUnique_ringHom_comp_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L140). The attribute's comment: “functoriality: the unique induced algebra map”.

> **Stacks Project, Tag 096V**, the final assertion. A ring map `A → A'` carrying a subset
> `Z' ⊆ Spec A'` into a subset `Z ⊆ Spec A` induces exactly one `A`-algebra map
> `A_Z^~ → (A')_{Z'}^~`.

```lean
theorem existsUnique_ringHom_comp_algebraMap {A' : Type u} [CommRing A'] (φ : A →+* A')
    {Z : Set (PrimeSpectrum A)} {Z' : Set (PrimeSpectrum A')}
    (h : PrimeSpectrum.comap φ '' Z' ⊆ Z) (B : Type u) [CommRing B] [Algebra A B]
    [IsLocalization (nonvanishingSubmonoid Z) B] (B' : Type u) [CommRing B'] [Algebra A' B']
    [IsLocalization (nonvanishingSubmonoid Z') B'] :
    ∃! ψ : B →+* B', ψ.comp (algebraMap A B) = (algebraMap A' B').comp φ
```

**`AlgebraicGeometry.ProEtale.range_comap_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L235). The attribute's comment: “part (1), the image of Spec of the localization”.

> **Stacks Project, Tag 096V**, assertion (1). The spectrum of `A_Z^~` maps onto the set of
> points of `Spec A` specializing to `Z = D(f) ∩ V(I)`.

```lean
theorem range_comap_algebraMap (f : A) (I : Ideal A) (B : Type u) [CommRing B] [Algebra A B]
    [IsLocalization (nonvanishingSubmonoid (basicLocallyClosed f I)) B] :
    Set.range (PrimeSpectrum.comap (algebraMap A B)) =
      {p : PrimeSpectrum A | ∃ q ∈ basicLocallyClosed f I, p ⤳ q}
```

**`AlgebraicGeometry.ProEtale.homeomorphSetOfSpecializesTo`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L247). The attribute's comment: “part (1), the homeomorphism onto the set of specializations”.

> **Stacks Project, Tag 096V**, assertion (1) as the homeomorphism it asserts:
> `Spec (A_Z^~)` is homeomorphic to the set of points of `Spec A` specializing to
> `Z = D(f) ∩ V(I)`.

```lean
noncomputable def homeomorphSetOfSpecializesTo (f : A) (I : Ideal A) (B : Type u) [CommRing B]
    [Algebra A B] [IsLocalization (nonvanishingSubmonoid (basicLocallyClosed f I)) B] :
    PrimeSpectrum B ≃ₜ {p : PrimeSpectrum A | ∃ q ∈ basicLocallyClosed f I, p ⤳ q}
```

**`AlgebraicGeometry.ProEtale.nonvanishingSubmonoid_eq_of_basicLocallyClosed_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L258). The attribute's comment: “part (2), dependence only on the underlying subset”.

> **Stacks Project, Tag 096V**, assertion (2). The source's multiplicative set — the elements
> whose image in `A/I` divides a power of the image of `f` — depends only on the underlying subset
> `D(f) ∩ V(I)`, and so therefore does `A_Z^~`.

```lean
theorem nonvanishingSubmonoid_eq_of_basicLocallyClosed_eq {f f' : A} {I I' : Ideal A}
    (h : basicLocallyClosed f I = basicLocallyClosed f' I') (a : A) :
    (∃ n : ℕ, ∃ b : A, f ^ n - a * b ∈ I) ↔ ∃ n : ℕ, ∃ b : A, f' ^ n - a * b ∈ I'
```

**`AlgebraicGeometry.ProEtale.algEquivOfBasicLocallyClosedEq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L274). The attribute's comment: “part (2), the algebra attached to the subset”.

> **Stacks Project, Tag 096V**, assertion (2) as the statement about the algebra: the algebras
> attached to two presentations of one locally closed subset are isomorphic as `A`-algebras.

```lean
noncomputable def algEquivOfBasicLocallyClosedEq {f f' : A} {I I' : Ideal A}
    (h : basicLocallyClosed f I = basicLocallyClosed f' I') (B B' : Type u) [CommRing B]
    [Algebra A B] [IsLocalization (nonvanishingSubmonoid (basicLocallyClosed f I)) B]
    [CommRing B'] [Algebra A B']
    [IsLocalization (nonvanishingSubmonoid (basicLocallyClosed f' I')) B'] : B ≃ₐ[A] B'
```

**`AlgebraicGeometry.ProEtale.basicLocallyClosed_eq_range_inter_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L287). The attribute's comment: “part (3), Z is closed in the image of Spec of the localization”.

> **Stacks Project, Tag 096V**, the topological half of assertion (3). Inside the image of
> `Spec (A_Z^~)` the subset `Z = D(f) ∩ V(I)` is cut out by `I` alone: a prime specializing into
> `Z` and containing `I` already avoids `f`, so `Z` is closed in that image.

```lean
theorem basicLocallyClosed_eq_range_inter_zeroLocus (f : A) (I : Ideal A) (B : Type u)
    [CommRing B] [Algebra A B]
    [IsLocalization (nonvanishingSubmonoid (basicLocallyClosed f I)) B] :
    basicLocallyClosed f I =
      Set.range (PrimeSpectrum.comap (algebraMap A B)) ∩ PrimeSpectrum.zeroLocus (I : Set A)
```

**`AlgebraicGeometry.ProEtale.surjective_quotientAwayLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L339). The attribute's comment: “part (3), Z is a closed subscheme of Spec of the localization”.

> **Stacks Project, Tag 096V**, assertion (3). The ring `A_Z^~` surjects onto
> `Γ(Z, 𝒪_Z) = (A/I)_f`, so `Z` is a closed subscheme of `Spec (A_Z^~)`.

```lean
theorem surjective_quotientAwayLift (f : A) (I : Ideal A) (B : Type u) [CommRing B] [Algebra A B]
    [IsLocalization (nonvanishingSubmonoid (basicLocallyClosed f I)) B] (C : Type u) [CommRing C]
    [Algebra (A ⧸ I) C] [IsLocalization.Away (Ideal.Quotient.mk I f) C] :
    Function.Surjective (quotientAwayLift f I B C)
```

**`AlgebraicGeometry.ProEtale.localization_comap_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean#L178). The attribute's comment: “part (1): image”.

> The points of the localization are precisely those specializing to
> `D(f) ∩ V(I)`.

```lean
theorem localization_comap_range (I : Ideal A) (f : A) :
    Set.range (PrimeSpectrum.comap (algebraMap A (localizationRing I f))) =
      {p | ∃ q ∈ locallyClosedPoints I f, p ⤳ q}
```

**`AlgebraicGeometry.ProEtale.localizationSubmonoid_eq_of_locallyClosedPoints_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean#L231). The attribute's comment: “part (2)”.

> The selected multiplicative subset, hence the localized `A`-algebra, depends only on the
> underlying locally closed subset.

```lean
theorem localizationSubmonoid_eq_of_locallyClosedPoints_eq
    (I J : Ideal A) (f g : A) (h : locallyClosedPoints I f = locallyClosedPoints J g) :
    localizationSubmonoid I f = localizationSubmonoid J g
```

**`AlgebraicGeometry.ProEtale.localizationToCoordinateRing_isClosedImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean#L240). The attribute's comment: “part (3)”.

> The locally closed subscheme is closed in the selected localization.

```lean
instance localizationToCoordinateRing_isClosedImmersion
    (I : Ideal A) (f : A) :
    IsClosedImmersion
      (Spec.map (CommRingCat.ofHom (localizationToCoordinateRing I f)))
```

**`AlgebraicGeometry.ProEtale.localizationSubmonoid_le_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean#L263). The attribute's comment: “naturality: selected multiplicative sets”.

> A map taking `D(g) ∩ V(J)` into `D(f) ∩ V(I)` preserves the selected multiplicative
> sets.

```lean
theorem localizationSubmonoid_le_comap
    (h : A →+* A') (I : Ideal A) (f : A) (J : Ideal A') (g : A')
    (hZ : ∀ q ∈ locallyClosedPoints J g,
      PrimeSpectrum.comap h q ∈ locallyClosedPoints I f) :
    localizationSubmonoid I f ≤ (localizationSubmonoid J g).comap h
```

**`AlgebraicGeometry.ProEtale.localizationMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean#L286). The attribute's comment: “naturality and uniqueness”.

> The canonical map is the unique map of `A`-algebras extending `h`.

```lean
theorem localizationMap_unique
    (h : A →+* A') (I : Ideal A) (f : A) (J : Ideal A') (g : A')
    (hZ : ∀ q ∈ locallyClosedPoints J g,
      PrimeSpectrum.comap h q ∈ locallyClosedPoints I f) :
    ∃! k : localizationRing I f →+* localizationRing J g,
      k.comp (algebraMap A (localizationRing I f)) =
        (algebraMap A' (localizationRing J g)).comp h
```

Declarations registered for the tag:

- [`PrimeSpectrum.localization_comap_isEmbedding`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.localization_comap_isEmbedding#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Localization.lean#L169) (StacksFrontier): “part (1): embedding”. References: EGA I (1.2.4), “localization R → M⁻¹R”; EGA I (1.6.2), “partial”; EGA I (2.4.2), “topological embedding”; EGA IV (10.7.3), “partial”.

## Tag 096W, an equation

[Tag 096W](https://stacks.math.columbia.edu/tag/096W) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.basicStratum_eq_basicLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L372).

> **Stacks Project, Tag 096W.** The stratum `Z(E', E'')` is the locally closed subset
> `D(∏_{f ∈ E'} f) ∩ V(∑_{f ∈ E''} f A)`, hence of the shape to which Tag 096V applies.

```lean
theorem basicStratum_eq_basicLocallyClosed (E' E'' : Finset A) :
    basicStratum E' E'' = basicLocallyClosed (∏ g ∈ E', g) (Ideal.span (E'' : Set A))
```

## Tag 096X, an equation

[Tag 096X](https://stacks.math.columbia.edu/tag/096X) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isConstructible_basicStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L389). The attribute's comment: “each stratum is constructible”.

> **Stacks Project, Tag 096X**, the observation that each stratum is constructible: a stratum
> is a finite intersection of basic opens and complements of basic opens.

```lean
theorem isConstructible_basicStratum (E' E'' : Finset A) :
    Topology.IsConstructible (basicStratum E' E'')
```

**`AlgebraicGeometry.ProEtale.exists_mem_vanishingPatternStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L464). The attribute's comment: “the strata cover the spectrum”.

> **Stacks Project, Tag 096X**, the covering half. Every point of `Spec A` lies in the stratum
> of its own vanishing pattern on `E`.

```lean
theorem exists_mem_vanishingPatternStratum (E : Finset A) (q : PrimeSpectrum A) :
    ∃ σ : A → Bool, q ∈ vanishingPatternStratum E σ
```

**`AlgebraicGeometry.ProEtale.vanishingPatternStratum_disjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/WLocalConstruction.lean#L481). The attribute's comment: “the strata are pairwise disjoint”.

> **Stacks Project, Tag 096X**, the disjointness half. Two vanishing patterns differing on `E`
> have disjoint strata.

```lean
theorem vanishingPatternStratum_disjoint {E : Finset A} {σ τ : A → Bool}
    (h : ∃ g ∈ E, σ g ≠ τ g) :
    Disjoint (vanishingPatternStratum E σ) (vanishingPatternStratum E τ)
```

## Tag 096Y, a lemma

[Tag 096Y](https://stacks.math.columbia.edu/tag/096Y) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_vanishingPatternStrata_refines`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ConstructibleStratification.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ConstructibleStratification.lean#L96).

> **Stacks Project, Tag 096Y.** Every finite constructible partition of an affine spectrum is
> refined by the stratification according to the vanishing pattern of finitely many elements.

```lean
lemma exists_vanishingPatternStrata_refines {A : Type u} [CommRing A]
    {P : Set (Set (PrimeSpectrum A))} (hP : Setoid.IsPartition P)
    (hP_finite : P.Finite) (hP_constructible : ∀ T ∈ P, Topology.IsConstructible T) :
    ∃ E : Finset A, local_Refines (vanishingPatternStrata E) P
```

## Tag 096Z, an equation

[Tag 096Z](https://stacks.math.columbia.edu/tag/096Z) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.stratificationRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean#L66).

> The ring `A_E`, formed as the product of the localizations attached to all
> vanishing-pattern strata of `Spec A`.

```lean
abbrev stratificationRing (E : Finset A) : Type u
```

## Tag 0970, an equation

[Tag 0970](https://stacks.math.columbia.edu/tag/0970) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.specStratificationRingIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationSpectrum.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationSpectrum.lean#L42).

> The spectrum `X_E = Spec(A_E)` of the stratification ring is the coproduct of the spectra
> `X_{E', E''} = Spec(A^~_{Z(E', E'')})` over all decompositions `E = E' ⨿ E''`.

```lean
def specStratificationRingIso (E : Finset A) :
    Spec (.of (stratificationRing E)) ≅
      ∐ fun E' : {E' : Finset A // E' ⊆ E} =>
        Spec (.of (localizationRing (stratumIdeal E E') (stratumOpenElement E'.val)))
```

## Tag 0971, an equation

[Tag 0971](https://stacks.math.columbia.edu/tag/0971) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.closedStrata`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean#L86). The attribute's comment: “the coproduct”.

> The coproduct `Z_E` of the coordinate schemes of all vanishing patterns.

```lean
def closedStrata (E : Finset A) : Scheme.{u}
```

**`AlgebraicGeometry.ProEtale.closedStrataMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean#L91). The attribute's comment: “the map”.

> The canonical map from the coproduct of strata to `X_E`.

```lean
def closedStrataMap (E : Finset A) :
    closedStrata E ⟶ Spec (.of (stratificationRing E))
```

**`AlgebraicGeometry.ProEtale.closedStrataMap_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean#L105). The attribute's comment: “closed immersion”.

> `Z_E` is a closed subscheme of `X_E`.

```lean
theorem closedStrataMap_isClosedImmersion (E : Finset A) :
    IsClosedImmersion (closedStrataMap E)
```

**`AlgebraicGeometry.ProEtale.closedPoints_mem_closedStrataMap_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Stratification.lean#L155). The attribute's comment: “closed points”.

> Every closed point of `X_E` belongs to `Z_E`.

```lean
theorem closedPoints_mem_closedStrataMap_range (E : Finset A)
    (x : Spec (.of (stratificationRing E))) (hx : IsClosed {x}) :
    x ∈ Set.range (closedStrataMap E)
```

## Tag 0972, an equation

[Tag 0972](https://stacks.math.columbia.edu/tag/0972) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.locallyClosedPoints_restrictStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean#L81). The attribute's comment: “inclusion of strata”.

> Restriction of a vanishing pattern carries its locally closed stratum
> into the corresponding stratum for the smaller finite set.

```lean
theorem locallyClosedPoints_restrictStratum (E₁ E₂ : Finset A)
    (h : E₁ ⊆ E₂) (i : {E' : Finset A // E' ⊆ E₂})
    (q : PrimeSpectrum A)
    (hq : q ∈ locallyClosedPoints
      (stratumIdeal E₂ i) (stratumOpenElement i.val)) :
    q ∈ locallyClosedPoints
      (stratumIdeal E₁ (restrictStratum E₁ E₂ h i))
      (stratumOpenElement (restrictStratum E₁ E₂ h i).val)
```

**`AlgebraicGeometry.ProEtale.stratificationRingMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean#L110). The attribute's comment: “the transition ring map”.

> The canonical transition map `A_{E₁} → A_{E₂}` for `E₁ ⊆ E₂`.

```lean
def stratificationRingMap (E₁ E₂ : Finset A) (h : E₁ ⊆ E₂) :
    stratificationRing E₁ →+* stratificationRing E₂
```

**`AlgebraicGeometry.ProEtale.stratificationRingMap_comp_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean#L292). The attribute's comment: “A-algebra compatibility”.

> The transition maps respect the structure maps from `A`.

```lean
theorem stratificationRingMap_comp_algebraMap (E₁ E₂ : Finset A) (h : E₁ ⊆ E₂) :
    (stratificationRingMap E₁ E₂ h).comp (stratificationAlgebraMap E₁) =
      stratificationAlgebraMap E₂
```

**`AlgebraicGeometry.ProEtale.stratificationRingMap_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean#L303). The attribute's comment: “identity transition”.

> The transition map for an identity inclusion is the identity.

```lean
theorem stratificationRingMap_id (E : Finset A) :
    stratificationRingMap E E (Finset.Subset.refl E) = RingHom.id _
```

**`AlgebraicGeometry.ProEtale.stratificationRingMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean#L319). The attribute's comment: “composition of transitions”.

> The transition maps compose for a chain of finite subsets.

```lean
theorem stratificationRingMap_comp (E₁ E₂ E₃ : Finset A)
    (h₁₂ : E₁ ⊆ E₂) (h₂₃ : E₂ ⊆ E₃) :
    (stratificationRingMap E₂ E₃ h₂₃).comp (stratificationRingMap E₁ E₂ h₁₂) =
      stratificationRingMap E₁ E₃ (h₁₂.trans h₂₃)
```

**`AlgebraicGeometry.ProEtale.stratificationSchemeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean#L348). The attribute's comment: “the scheme morphism”.

> The corresponding transition arrow `X_{E₂} → X_{E₁}`.

```lean
def stratificationSchemeMap (E₁ E₂ : Finset A) (h : E₁ ⊆ E₂) :
    Spec (.of (stratificationRing E₂)) ⟶ Spec (.of (stratificationRing E₁))
```

**`AlgebraicGeometry.ProEtale.closedStrataTransition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationTransition.lean#L355). The attribute's comment: “transition on closed strata”.

> The transition arrow restricts to a morphism `Z_{E₂} → Z_{E₁}` of
> closed subschemes, commuting with their inclusions into the affine schemes.

```lean
def closedStrataTransition (E₁ E₂ : Finset A) (h : E₁ ⊆ E₂) :
    {g : closedStrata E₂ ⟶ closedStrata E₁ //
      g ≫ closedStrataMap E₁ = closedStrataMap E₂ ≫ stratificationSchemeMap E₁ E₂ h}
```

## Tag 0973, an equation

[Tag 0973](https://stacks.math.columbia.edu/tag/0973) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.stratificationColimitRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimit.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimit.lean#L60).

> The colimit of the rings attached to all finite vanishing stratifications
> of `Spec A`, with the canonical transition maps for inclusion.

```lean
abbrev stratificationColimitRing : Type u
```

**`AlgebraicGeometry.ProEtale.stratificationColimitMap_comp_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimit.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimit.lean#L80). The attribute's comment: “compatibility with the finite stages”.

> The structure map from `A` agrees with the map through any finite stage.

```lean
theorem stratificationColimitMap_comp_algebraMap (E : Finset A) :
    (stratificationColimitMap (A := A) E).comp (stratificationAlgebraMap E) =
      stratificationColimitAlgebraMap (A := A)
```

## Tag 0974, an equation

[Tag 0974](https://stacks.math.columbia.edu/tag/0974) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.stratificationLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimit.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimit.lean#L382).

> **Stacks 0974.** The canonical closed subscheme `Z = lim Z_E` of
> `X_w = Spec A_w = lim X_E`.

```lean
def stratificationLimit : StratificationLimit A
```

## Tag 0975, a lemma

[Tag 0975](https://stacks.math.columbia.edu/tag/0975) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.stratificationColimit_isIndZariski_and_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitIndZariski.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitIndZariski.lean#L496). The attribute's comment: “ind_zariski_faithfully_flat”.

> **Stacks 0975**, part (1): the canonical map `A → A_w` from a commutative ring to its
> stratification colimit is ind-Zariski and faithfully flat.

```lean
theorem stratificationColimit_isIndZariski_and_faithfullyFlat :
    IsIndZariski.{u, u, u} A (stratificationColimitRing (A := A)) ∧
      (stratificationColimitAlgebraMap (A := A)).FaithfullyFlat
```

**`AlgebraicGeometry.ProEtale.stratificationLimit_closedScheme_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitBijection.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitBijection.lean#L38). The attribute's comment: “bijection_on_z”.

> The limiting closed subscheme `Z` of `X_w` maps bijectively onto `Spec A`.

```lean
theorem stratificationLimit_closedScheme_bijective (L : StratificationLimit A) :
    Function.Bijective (L.inclusion ≫
      Spec.map (CommRingCat.ofHom (stratificationColimitAlgebraMap (A := A)))).base
```

**`AlgebraicGeometry.ProEtale.bijective_stratificationLimitClosedScheme_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitBijection.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitBijection.lean#L132). The attribute's comment: “bijection_on_z”.

> The morphism `X_w → X` induces a bijection from the limiting closed subscheme `Z` onto
> `X = Spec A`.

```lean
theorem bijective_stratificationLimitClosedScheme_toBase :
    Function.Bijective (stratificationLimitInclusion (A := A) ≫
      Spec.map (CommRingCat.ofHom (stratificationColimitAlgebraMap (A := A)))).base
```

**`AlgebraicGeometry.ProEtale.range_inclusion_eq_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean#L57). The attribute's comment: “closed_points”.

> The limiting closed subscheme `Z` of `X_w` has as its underlying set exactly the closed
> points of `X_w`.

```lean
theorem range_inclusion_eq_closedPoints (L : StratificationLimit A) :
    Set.range L.inclusion.base = closedPoints (stratificationLimitScheme (A := A))
```

**`AlgebraicGeometry.ProEtale.existsUnique_specializes_closedScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean#L75). The attribute's comment: “unique_closed_specialization”.

> Every point of `X_w` specializes to exactly one point of its limiting closed subscheme
> `Z`.

```lean
theorem existsUnique_specializes_closedScheme (L : StratificationLimit A)
    (x : stratificationLimitScheme (A := A)) :
    ∃! z : L.closedScheme, x ⤳ L.inclusion.base z
```

**`AlgebraicGeometry.ProEtale.stratificationLimitScheme_wLocal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean#L84). The attribute's comment: “w_locality”.

> The limiting scheme `X_w` of the finite vanishing stratifications of `Spec A` is w-local.

```lean
instance stratificationLimitScheme_wLocal :
    WLocalSpace (stratificationLimitScheme (A := A))
```

**`AlgebraicGeometry.ProEtale.range_stratificationLimitInclusion_eq_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean#L102). The attribute's comment: “closed_points”.

> **Stacks 0975**, part (3): the limiting closed subscheme `Z` of `X_w` is exactly the set of
> closed points of `X_w`.

```lean
theorem range_stratificationLimitInclusion_eq_closedPoints :
    Set.range (stratificationLimitInclusion (A := A)).base =
      closedPoints (stratificationLimitScheme (A := A))
```

**`AlgebraicGeometry.ProEtale.existsUnique_specializes_stratificationLimitClosedScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitClosedPoints.lean#L110). The attribute's comment: “unique_closed_specialization”.

> **Stacks 0975**, part (5): every point of `X_w` specializes to exactly one point of the
> limiting closed subscheme `Z`.

```lean
theorem existsUnique_specializes_stratificationLimitClosedScheme
    (x : stratificationLimitScheme (A := A)) :
    ∃! z : stratificationLimitClosedScheme (A := A),
      x ⤳ (stratificationLimitInclusion (A := A)).base z
```

**`AlgebraicGeometry.ProEtale.stratificationLimit_closedScheme_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitReduced.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitReduced.lean#L343). The attribute's comment: “reduced_z”.

> **Stacks 0975**, part (4): the limiting closed subscheme `Z` of `X_w` is a reduced scheme.

```lean
theorem stratificationLimit_closedScheme_isReduced (L : StratificationLimit A) :
    IsReduced L.closedScheme
```

**`AlgebraicGeometry.ProEtale.stratificationLimitClosedScheme_isReduced`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitReduced.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationLimitReduced.lean#L358). The attribute's comment: “reduced_z”.

> **Stacks 0975**, part (4): the limiting closed subscheme `Z` of `X_w` is a reduced
> scheme.

```lean
instance stratificationLimitClosedScheme_isReduced :
    IsReduced (stratificationLimitClosedScheme (A := A))
```

## Tag 0976, a remark

[Tag 0976](https://stacks.math.columbia.edu/tag/0976) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.mk_finset_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitCardinality.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitCardinality.lean#L43). The attribute's comment: “finite subsets”.

> Finite subsets of a type of size at most an infinite cardinal themselves
> form a type of size at most that cardinal.

```lean
theorem mk_finset_le {A : Type u} (κ : Cardinal.{u})
    (hκ : ℵ₀ ≤ κ) (hA : Cardinal.mk A ≤ κ) :
    Cardinal.mk (Finset A) ≤ κ
```

**`AlgebraicGeometry.ProEtale.mk_stratificationRing_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitCardinality.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitCardinality.lean#L53). The attribute's comment: “finite stages”.

> Each finite stratification ring `A_E` has cardinality at most `κ`.

```lean
theorem mk_stratificationRing_le {A : Type u} [CommRing A]
    (κ : Cardinal.{u}) (hκ : ℵ₀ ≤ κ) (hA : Cardinal.mk A ≤ κ)
    (E : Finset A) :
    Cardinal.mk (stratificationRing E) ≤ κ
```

**`AlgebraicGeometry.ProEtale.mk_stratificationColimitRing_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitCardinality.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitCardinality.lean#L83).

> The ring `A_w` has cardinality at most every infinite cardinal bounding
> the cardinality of `A`.

```lean
theorem mk_stratificationColimitRing_le {A : Type u} [CommRing A]
    (κ : Cardinal.{u}) (hκ : ℵ₀ ≤ κ) (hA : Cardinal.mk A ≤ κ) :
    Cardinal.mk (stratificationColimitRing (A := A)) ≤ κ
```

## Tag 0977, a lemma

[Tag 0977](https://stacks.math.columbia.edu/tag/0977) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.existsUnique_wLocal_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitUniversal.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/StratificationColimitUniversal.lean#L603).

> **Stacks 0977.** A ring map `A → B` with `Spec B` w-local factors through `A → A_w` by
> exactly one ring map `A_w → B` whose induced map of spectra is w-local.

```lean
theorem existsUnique_wLocal_lift
    (A : Type u) (B : Type v) [CommRing A] [CommRing B]
    (f : A →+* B) [WLocalSpace (Spec (.of B))] :
    ∃! g : stratificationColimitRing (A := A) →+* B,
      g.comp (stratificationColimitAlgebraMap (A := A)) = f ∧
        IsWLocalMap (PrimeSpectrum.comap g)
```

## Tag 0978, a lemma

[Tag 0978](https://stacks.math.columbia.edu/tag/0978) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isProfiniteStacks_primeSpectrum_of_fiberwise_incomparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean#L67). The attribute's comment: “fiberwise_incomparable”.

> If the spectrum of `A` is profinite and distinct prime ideals of `B` lying over the same
> prime ideal of `A` are incomparable, then the spectrum of `B` is profinite.

```lean
theorem isProfiniteStacks_primeSpectrum_of_fiberwise_incomparable
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] (f : A →+* B)
    (hA : IsProfiniteStacks (PrimeSpectrum A))
    (hfiber : ∀ q q' : Ideal B, q.IsPrime → q'.IsPrime →
      Ideal.comap f q = Ideal.comap f q' → q ≤ q' → q = q') :
    IsProfiniteStacks (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.isProfiniteStacks_primeSpectrum_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean#L85). The attribute's comment: “quasi_finite”.

> A quasi-finite algebra over a ring with profinite prime spectrum has profinite prime
> spectrum.

```lean
theorem isProfiniteStacks_primeSpectrum_of_quasiFinite
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [Algebra.QuasiFinite A B] (hA : IsProfiniteStacks (PrimeSpectrum A)) :
    IsProfiniteStacks (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.isProfiniteStacks_primeSpectrum_of_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean#L96). The attribute's comment: “unramified”.

> An unramified algebra over a ring with profinite prime spectrum has profinite prime
> spectrum.

```lean
theorem isProfiniteStacks_primeSpectrum_of_unramified
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [Algebra.Unramified A B] (hA : IsProfiniteStacks (PrimeSpectrum A)) :
    IsProfiniteStacks (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.isProfiniteStacks_primeSpectrum_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreEtale/FiberwiseIncomparable/ProfiniteSpectra.lean#L104). The attribute's comment: “etale”.

> An étale algebra over a ring with profinite prime spectrum has profinite prime spectrum.

```lean
theorem isProfiniteStacks_primeSpectrum_of_etale
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [Algebra.Etale A B] (hA : IsProfiniteStacks (PrimeSpectrum A)) :
    IsProfiniteStacks (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.isProfiniteStacks_primeSpectrum_of_identifiesLocalRings'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WContractible/LocalRings.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WContractible/LocalRings.lean#L47). The attribute's comment: “identifies_local_rings”.

> A ring map identifying local rings preserves profiniteness of prime spectra.
>
> This is the form for an arbitrary ring homomorphism between commutative rings in possibly
> different universes.  The unprimed
> `isProfiniteStacks_primeSpectrum_of_identifiesLocalRings` is the form for an `Algebra`
> instance in a single universe.

```lean
theorem isProfiniteStacks_primeSpectrum_of_identifiesLocalRings'
    {A B : Type*} [CommRing A] [CommRing B] (f : A →+* B)
    (hA : IsProfiniteStacks (PrimeSpectrum A))
    (hf : letI := f.toAlgebra; Algebra.IdentifiesLocalRings A B) :
    IsProfiniteStacks (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.primeSpectrum_isProfinite_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean#L85). The attribute's comment: “algebraic_residue_fields”.

> A ring map inducing algebraic extensions on residue fields preserves profiniteness of
> prime spectra.

```lean
theorem primeSpectrum_isProfinite_of_isAlgebraic_residueField
    {A B : Type*} [CommRing A] [CommRing B] (f : A →+* B)
    (hA : CompactSpace (PrimeSpectrum A) ∧ T2Space (PrimeSpectrum A) ∧
      TotallyDisconnectedSpace (PrimeSpectrum A))
    (halg : ∀ q : Ideal B, ∀ [q.IsPrime],
      letI := (Ideal.ResidueField.map (q.comap f) q f rfl).toAlgebra
      Algebra.IsAlgebraic (q.comap f).ResidueField q.ResidueField) :
    CompactSpace (PrimeSpectrum B) ∧ T2Space (PrimeSpectrum B) ∧
      TotallyDisconnectedSpace (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.primeSpectrum_isProfinite_of_weaklyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean#L107). The attribute's comment: “weakly_etale”.

> A weakly étale algebra over a ring with profinite prime spectrum has profinite prime
> spectrum.

```lean
theorem primeSpectrum_isProfinite_of_weaklyEtale
    (A B : Type*) [CommRing A] [CommRing B] [Algebra A B]
    [Algebra.WeaklyEtale A B]
    (hA : CompactSpace (PrimeSpectrum A) ∧ T2Space (PrimeSpectrum A) ∧
      TotallyDisconnectedSpace (PrimeSpectrum A)) :
    CompactSpace (PrimeSpectrum B) ∧ T2Space (PrimeSpectrum B) ∧
    TotallyDisconnectedSpace (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.primeSpectrum_isProfinite_of_identifiesLocalRings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean#L176). The attribute's comment: “identifies_local_rings”.

> An algebra identifying local rings over a ring with profinite prime spectrum has profinite
> prime spectrum.

```lean
theorem primeSpectrum_isProfinite_of_identifiesLocalRings
    (A B : Type*) [CommRing A] [CommRing B] [Algebra A B]
    (hid : Algebra.IdentifiesLocalRings A B)
    (hA : CompactSpace (PrimeSpectrum A) ∧ T2Space (PrimeSpectrum A) ∧
      TotallyDisconnectedSpace (PrimeSpectrum A)) :
    CompactSpace (PrimeSpectrum B) ∧ T2Space (PrimeSpectrum B) ∧
      TotallyDisconnectedSpace (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.primeSpectrum_isProfinite_of_isLocalIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean#L189). The attribute's comment: “local_isomorphism”.

> A local isomorphism over a ring with profinite prime spectrum has target with profinite
> prime spectrum.

```lean
theorem primeSpectrum_isProfinite_of_isLocalIso
    (A B : Type*) [CommRing A] [CommRing B] [Algebra A B] [Algebra.IsLocalIso A B]
    (hA : CompactSpace (PrimeSpectrum A) ∧ T2Space (PrimeSpectrum A) ∧
      TotallyDisconnectedSpace (PrimeSpectrum A)) :
    CompactSpace (PrimeSpectrum B) ∧ T2Space (PrimeSpectrum B) ∧
      TotallyDisconnectedSpace (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.primeSpectrum_isProfinite_of_directLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteSpectrum.lean#L220). The attribute's comment: “filtered_colimit”.

> A filtered colimit of rings with profinite prime spectra has profinite prime spectrum: here
> the colimit is the direct limit of a directed system over a nonempty directed preorder, and the
> ring `B` is presented as that colimit by a ring isomorphism.

```lean
theorem primeSpectrum_isProfinite_of_directLimit
    {ι : Type*} [Preorder ι] [IsDirectedOrder ι] [Nonempty ι]
    (G : ι → Type*) [∀ i, CommRing (G i)] (f : ∀ i j, i ≤ j → G i →+* G j)
    [DirectedSystem G fun i j h => (f i j h : G i → G j)]
    (hG : ∀ i, CompactSpace (PrimeSpectrum (G i)) ∧ T2Space (PrimeSpectrum (G i)) ∧
      TotallyDisconnectedSpace (PrimeSpectrum (G i)))
    (B : Type*) [CommRing B]
    (e : B ≃+* Ring.DirectLimit G fun i j h => (f i j h : G i → G j)) :
    CompactSpace (PrimeSpectrum B) ∧ T2Space (PrimeSpectrum B) ∧
      TotallyDisconnectedSpace (PrimeSpectrum B)
```

## Tag 0979, a lemma

[Tag 0979](https://stacks.math.columbia.edu/tag/0979) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exists_isIndZariski_wLocal_of_isProfiniteStacks_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteClosedSubset.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteClosedSubset.lean#L571).

> **Stacks 0979.** Let `A` be a ring and `I` an ideal whose closed subset `V(I) ⊆ Spec A` is a
> profinite topological space. Then there is an ind-Zariski ring map `A → B` such that `Spec B` is
> w-local, the set of its closed points is `V(I·B)`, and `A ⧸ I → B ⧸ I·B` is an isomorphism.

```lean
theorem exists_isIndZariski_wLocal_of_isProfiniteStacks_zeroLocus (I : Ideal A)
    (hI : IsProfiniteStacks (PrimeSpectrum.zeroLocus (I : Set A))) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B),
      Algebra.IsIndZariski A B ∧ WLocalSpace (PrimeSpectrum B) ∧
        closedPoints (PrimeSpectrum B) =
          PrimeSpectrum.zeroLocus (I.map (algebraMap A B) : Set B) ∧
        Function.Bijective (algebraMap (A ⧸ I) (B ⧸ I.map (algebraMap A B)))
```

## Tag 097A, a lemma

[Tag 097A](https://stacks.math.columbia.edu/tag/097A) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.closedPoints_of_mem_zeroLocus_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/AlgebraicResidueExtension.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/AlgebraicResidueExtension.lean#L39). The attribute's comment: “part (1)”.

> **Stacks 097A, part (1).** Let `I` be an ideal of `A` whose zero locus is the set of closed
> points of `Spec A`, and let `f : A →+* B` induce algebraic extensions of residue fields. Then
> every prime of `B` containing the extended ideal `I B` is a closed point of `Spec B`.

```lean
theorem closedPoints_of_mem_zeroLocus_map
    {A : Type*} {B : Type*} [CommRing A] [CommRing B] (f : A →+* B) (I : Ideal A)
    (hzero : PrimeSpectrum.zeroLocus (I : Set A) = closedPoints (PrimeSpectrum A))
    (halg : ∀ q : Ideal B, ∀ [q.IsPrime],
      letI := (Ideal.ResidueField.map (q.comap f) q f rfl).toAlgebra
      Algebra.IsAlgebraic (q.comap f).ResidueField q.ResidueField) :
    PrimeSpectrum.zeroLocus (Ideal.map f I : Set B) ⊆ closedPoints (PrimeSpectrum B)
```

**`AlgebraicGeometry.ProEtale.exists_isIndZariski_wLocal_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/AlgebraicResidueExtensionWLocal.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/AlgebraicResidueExtensionWLocal.lean#L151). The attribute's comment: “part (2)”.

> **Stacks 097A, part (2).** Let `I` be an ideal of `A` whose zero locus is the set `X₀` of
> closed points of `X = Spec A`, and let `f : A →+* B` induce algebraic extensions of residue
> fields. Then there is an ind-Zariski ring map `B → C` such that `B ⧸ I·B → C ⧸ I·C` is an
> isomorphism, the space `Y = Spec C` is w-local, the induced map `p : Y → X` is w-local, and
> `p⁻¹(X₀)` is the set of closed points of `Y`.

```lean
theorem exists_isIndZariski_wLocal_of_isAlgebraic_residueField (f : A →+* B) (I : Ideal A)
    (hzero : PrimeSpectrum.zeroLocus (I : Set A) = closedPoints (PrimeSpectrum A))
    (halg : ∀ q : Ideal B, ∀ [q.IsPrime],
      letI := (Ideal.ResidueField.map (q.comap f) q f rfl).toAlgebra
      Algebra.IsAlgebraic (q.comap f).ResidueField q.ResidueField) :
    ∃ (C : Type v) (_ : CommRing C) (_ : Algebra B C),
      Algebra.IsIndZariski B C ∧
        Function.Bijective (algebraMap (B ⧸ Ideal.map f I)
          (C ⧸ (Ideal.map f I).map (algebraMap B C))) ∧
        WLocalSpace (PrimeSpectrum C) ∧
        IsWLocalMap (PrimeSpectrum.comap ((algebraMap B C).comp f)) ∧
        closedPoints (PrimeSpectrum C) =
          PrimeSpectrum.comap ((algebraMap B C).comp f) ⁻¹' closedPoints (PrimeSpectrum A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.5, Tag 096U](https://stacks.math.columbia.edu/tag/096U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
