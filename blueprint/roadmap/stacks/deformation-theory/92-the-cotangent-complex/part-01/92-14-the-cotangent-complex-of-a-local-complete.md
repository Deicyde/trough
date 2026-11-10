---
declaration: section
origin: cited
lean: CommAlgCat.nonempty_cotangentComplex_retraction_iso_single, CommAlgCat.nonempty_cotangentComplex_retraction_iso_single_unconditional, CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence, CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence_unconditional, CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular, CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_unconditional, CommAlgCat.isPerfect_and_hasTorAmplitude_cotangentComplexDerived_of_isLocalCompleteIntersection, CommAlgCat.isPerfect_and_hasTorAmplitude_cotangentComplexDerived_of_isLCI
statement: formalized
proof: formalized
---

# 92.14 The cotangent complex of a local complete intersection

Section 92.14 of the Stacks Project, [Tag 08SH](https://stacks.math.columbia.edu/tag/08SH). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08SI, a lemma

[Tag 08SI](https://stacks.math.columbia.edu/tag/08SI) in the Stacks Project.

**`CommAlgCat.nonempty_cotangentComplex_retraction_iso_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialRetraction.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialRetraction.lean#L267). The attribute's comment: “the lemma for a general base ring A and a general polynomial algebra B over it with an augmentation B → A, of which the source's A = Z[x_1,...,x_n] -> B = Z sending every x_i to 0 is the case A = Z; the source's ideal I = (x_1,...,x_n) is the kernel of the augmentation, and I/I^2 is its conormal module. ONE carried hypothesis: h08QX, Proposition 08QX for the tower A -> B -> A, which is the triangle the source's proof invokes and which is not proved in this library — the triangle the library carries, Tag 08SD, needs the middle map injective, whereas the augmentation B → A is surjective. The hypothesis is 08QX itself, for a general not-necessarily-injective map, and not the conclusion proved here”.

> **Stacks Project, Tag 08SI.** Let `A` be a commutative ring, let `B` be a polynomial algebra
> over `A`, and let `B → A` be a retraction of `A → B` — an augmentation. Let `I = ker(B → A)`.
> Then `L_{A/B}` is quasi-isomorphic to `I/I²[1]`, that is, isomorphic in `D(A)` to the conormal
> module `I/I²` placed in cohomological degree `-1`.
>
> The source states this for `A = ℤ`, `B = ℤ[x₁, …, xₙ]` and the augmentation sending every
> variable to `0`, whose kernel is the ideal `I = (x₁, …, xₙ)`; the statement here is that case
> with the base ring and the set of variables left general.

```lean
theorem nonempty_cotangentComplex_retraction_iso_single
    (hB : Algebra.IsPolynomialAlgebra A B) (h08QX : HasFundamentalTriangleAt A B A) :
    Nonempty (DerivedCategory.Q.obj (cotangentComplex B (CommAlgCat.of B A)) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} ↥(CommAlgCat.of B A)) (-1)).obj
        (ModuleCat.of ↥(CommAlgCat.of B A)
          (surjectionExtension B (CommAlgCat.of B A)
            (surjective_algebraMap_of_isScalarTower_self A B)).Cotangent))
```

**`CommAlgCat.nonempty_cotangentComplex_retraction_iso_single_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialRetractionUnconditional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialRetractionUnconditional.lean#L69). The attribute's comment: “the lemma for a general base ring A and a general polynomial algebra B over it with an augmentation B → A, of which the source's A = Z[x_1,...,x_n] -> B = Z sending every x_i to 0 is the case A = Z; the source's ideal I = (x_1,...,x_n) is the kernel of the augmentation, and I/I^2 is its conormal module. NOTHING is carried: the triangle the source's proof invokes is Proposition 08QX for the tower A -> B -> A, `CommAlgCat.productFundamentalTriangle_distinguished`, which holds for arbitrary ring maps — the triangle of Tag 08SD needs the middle map injective, whereas the augmentation B → A is surjective, so it is the proposition and not Tag 08SD that applies”.

> **Stacks Project, Tag 08SI.** Let `B` be a polynomial algebra over `A` with an augmentation
> `B → A`, and let `I` be its kernel. Then `L_{A/B}` is isomorphic in `D(A)` to `I/I²` placed in
> cohomological degree `-1`.
>
> This is `CommAlgCat.nonempty_cotangentComplex_retraction_iso_single` with the fundamental
> triangle of the tower `A → B → A` supplied by `CommAlgCat.hasFundamentalTriangleAt`.

```lean
theorem nonempty_cotangentComplex_retraction_iso_single_unconditional
    (hB : Algebra.IsPolynomialAlgebra A B) :
    Nonempty (DerivedCategory.Q.obj (cotangentComplex B (CommAlgCat.of B A)) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} ↥(CommAlgCat.of B A)) (-1)).obj
        (ModuleCat.of ↥(CommAlgCat.of B A)
          (surjectionExtension B (CommAlgCat.of B A)
            (surjective_algebraMap_of_isScalarTower_self A B)).Cotangent))
```

## Tag 08SJ, a lemma

[Tag 08SJ](https://stacks.math.columbia.edu/tag/08SJ) in the Stacks Project.

**`CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/KoszulRegularQuotient.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/KoszulRegularQuotient.lean#L338). The attribute's comment: “the lemma for a kernel generated by a Koszul-regular SEQUENCE f_1,...,f_r (the case Tag 08SK generalizes to a Koszul-regular ideal, which this does not prove: see the `No @[stacks 08SK]` section of the module docstring). I/I^2 is the conormal module of the surjection, as the cotangent module of the corresponding algebra extension. ONE carried hypothesis: h08QX, Proposition 08QX for the towers R -> P -> R with P a polynomial algebra over R carrying a retraction — exactly the hypothesis that Tag 08SI (`CommAlgCat.nonempty_cotangentComplex_retraction_iso_single`) carries, 08QX not being proved in this library because the triangle the library has, Tag 08SD, needs the middle map injective, whereas an augmentation is surjective. The hypothesis is 08QX itself and not the conclusion proved here”.

> **Stacks Project, Tag 08SJ.** Let `R → S` be a surjective map of commutative rings whose
> kernel `I` is generated by a Koszul-regular sequence `f₁, …, f_r ∈ R`. Then `L_{S/R}` is
> quasi-isomorphic to `I/I²[1]`, that is, isomorphic in `D(S)` to the conormal module `I/I²` placed
> in cohomological degree `-1`.
>
> The source's proof: the square of `P = R[x₁, …, x_r] → R`, `x_i ↦ f_i` over the augmentation
> `P → R`, `x_i ↦ 0` induces a quasi-isomorphism `R ⊗_P^𝐋 R = S`, so [Stacks, Tag 08QQ] reduces the
> computation to `L_{R/P}`, which [Stacks, Tag 08SI] gives as a projective module in degree `-1`.
> Hence `L_{S/R}` has no cohomology in the degrees `≤ -2`, and
> `CommAlgCat.nonempty_cotangentComplex_iso_single_of_isZero_homology_le_negTwo` concludes.

```lean
theorem nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence
    (h : Function.Surjective (algebraMap R (S : Type u)))
    {r : ℕ} (f : Fin r → R) (hf : Koszul.IsKoszulRegular f)
    (hI : RingHom.ker (algebraMap R (S : Type u)) = Ideal.span (Set.range f))
    (h08QX : ∀ (P : Type u) [CommRing P] [Algebra R P] [Algebra P R] [IsScalarTower R P R],
      Algebra.IsPolynomialAlgebra R P → HasFundamentalTriangleAt R P R) :
    Nonempty (DerivedCategory.Q.obj (cotangentComplex R S) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} (S : Type u)) (-1)).obj
        (ModuleCat.of (S : Type u) (surjectionExtension R S h).Cotangent))
```

**`CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/KoszulRegularQuotientUnconditional.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/KoszulRegularQuotientUnconditional.lean#L56). The attribute's comment: “the lemma for a kernel generated by a Koszul-regular SEQUENCE f_1,...,f_r. I/I^2 is the conormal module of the surjection, as the cotangent module of the corresponding algebra extension. NOTHING is carried: the fundamental triangle of the towers R -> P -> R with P a polynomial algebra over R carrying a retraction is Proposition 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`. The triangle of Tag 08SD does not apply, needing the middle map injective whereas an augmentation is surjective; the proposition does, assuming nothing”.

> **Stacks Project, Tag 08SJ.** Let `R → S` be a surjective map of commutative rings whose
> kernel `I` is generated by a Koszul-regular sequence `f₁, …, f_r ∈ R`. Then `L_{S/R}` is
> isomorphic in `D(S)` to the conormal module `I/I²` placed in cohomological degree `-1`.
>
> This is `CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence` with the
> fundamental triangles of the towers `R → P → R` supplied by
> `CommAlgCat.hasFundamentalTriangleAt`.

```lean
theorem nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence_unconditional
    (h : Function.Surjective (algebraMap R (S : Type u)))
    {r : ℕ} (f : Fin r → R) (hf : Koszul.IsKoszulRegular f)
    (hI : RingHom.ker (algebraMap R (S : Type u)) = Ideal.span (Set.range f)) :
    Nonempty (DerivedCategory.Q.obj (cotangentComplex R S) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} (S : Type u)) (-1)).obj
        (ModuleCat.of (S : Type u) (surjectionExtension R S h).Cotangent))
```

## Tag 08SK, a lemma

[Tag 08SK](https://stacks.math.columbia.edu/tag/08SK) in the Stacks Project.

**`CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/KoszulRegularIdealQuotient.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/KoszulRegularIdealQuotient.lean#L381). The attribute's comment: “the lemma for a Koszul-regular IDEAL (Tag 07CV (2), `Ideal.IsKoszulRegular`), generalizing the sequence case Tag 08SJ (`CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_sequence`). I/I^2 is the conormal module of the surjection, as the cotangent module of the corresponding algebra extension. TWO carried hypotheses, neither of them the conclusion. (1) h08SF: the localization lemma of Tag 08SF, `cotangent-lemma-localize`, which is not proved in this library and which no declaration here carries — it says L_{B_g/A_g} is isomorphic in D(B_g) to the degreewise extension of scalars of L_{B/A} along the flat map B -> B_g, an isomorphism of whole complexes for a DIFFERENT ring map A_g -> B_g, mentioning no homology in any degree, no single module and no conormal module; it is carried pointwise, only at the g at which the Koszul-regularity of the kernel produces a generating sequence. (2) h08QX: Proposition 08QX for the towers A_g -> P -> A_g with P a polynomial algebra over A_g carrying a retraction — verbatim the hypothesis that Tag 08SJ carries, inherited because Tag 08SJ is applied to the localized maps, 08QX not being proved in this library because the triangle the library has, Tag 08SD, needs the middle map injective whereas an augmentation is surjective. Everything else is proved outright: the Koszul cover generates the unit ideal, the localized map is surjective with kernel the localized ideal, Tag 08SJ at it, the flatness of B -> B_g, and the Zariski descent of the vanishing”.

> **Stacks Project, Tag 08SK.** Let `A → B` be a surjective map of commutative rings whose
> kernel `I` is a Koszul-regular ideal, Tag 07CV (2). Then `L_{B/A}` is quasi-isomorphic to
> `I/I²[1]`, that is, isomorphic in `D(B)` to the conormal module `I/I²` placed in cohomological
> degree `-1`.
>
> The source's proof: locally on `Spec(A)` the ideal `I` is generated by a Koszul-regular sequence,
> so [Stacks, Tag 08SJ] gives the vanishing of `H^i(L_{B_g/A_g})` for `i ≤ -2` over a cover, and
> [Stacks, Tag 08SF] turns that into the vanishing of the localizations of `H^i(L_{B/A})`, hence of
> `H^i(L_{B/A})` itself; then
> `CommAlgCat.nonempty_cotangentComplex_iso_single_of_isZero_homology_le_negTwo` concludes.
>
> See the module docstring for the two carried hypotheses.

```lean
theorem nonempty_cotangentComplex_iso_single_of_isKoszulRegular
    (h : Function.Surjective (algebraMap A (B : Type u)))
    (hI : Ideal.IsKoszulRegular (RingHom.ker (algebraMap A (B : Type u))))
    (h08SF : ∀ g : A, KernelKoszulRegularAway A B g → HasLocalizedCotangentComplexAt A B g)
    (h08QX : ∀ g : A, KernelKoszulRegularAway A B g →
      HasFundamentalTriangleAtPolynomialRetractions (Localization.Away g)) :
    Nonempty (DerivedCategory.Q.obj (cotangentComplex A B) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} (B : Type u)) (-1)).obj
        (ModuleCat.of (B : Type u) (surjectionExtension A B h).Cotangent))
```

**`CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/KoszulRegularIdealQuotientUnconditional.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/KoszulRegularIdealQuotientUnconditional.lean#L122). The attribute's comment: “the lemma for a Koszul-regular IDEAL (Tag 07CV (2), `Ideal.IsKoszulRegular`), generalizing the sequence case Tag 08SJ. I/I^2 is the conormal module of the surjection, as the cotangent module of the corresponding algebra extension. NOTHING is carried: the hypotheses are the source's two, that A -> B is surjective and that its kernel is a Koszul-regular ideal. Tag 08SF, `cotangent-lemma-localize`, is PROVED, not assumed: `CommAlgCat.hasLocalizedCotangentComplexAt` supplies it at every principal localization A_g -> B_g, from `CommAlgCat.nonempty_extendScalars_cotangentComplex_iso_localization`, the degreewise reading of Tag 08SF, whose `S maps into T` hypothesis is automatic for S the powers of g. Proposition 08QX is likewise NOT carried: the fundamental triangle of the towers A_g -> P -> A_g that Tag 08SJ consumes is `CommAlgCat.productFundamentalTriangle_distinguished`, through `CommAlgCat.hasFundamentalTriangleAt`. Everything else is proved outright: the Koszul cover generates the unit ideal, the localized map is surjective with kernel the localized ideal, Tag 08SJ at it, the flatness of B -> B_g, and the Zariski descent of the vanishing”.

> **Stacks Project, Tag 08SK.** Let `A → B` be a surjective map of commutative rings whose
> kernel `I` is a Koszul-regular ideal, Tag 07CV (2). Then `L_{B/A}` is quasi-isomorphic to
> `I/I²[1]`, that is, isomorphic in `D(B)` to the conormal module `I/I²` placed in cohomological
> degree `-1`.
>
> This is `CommAlgCat.nonempty_cotangentComplex_iso_single_of_isKoszulRegular` with its two inputs
> supplied by `CommAlgCat.hasLocalizedCotangentComplexAt` and
> `CommAlgCat.hasFundamentalTriangleAt`, so that the only hypotheses left are the source's own
> two.

```lean
theorem nonempty_cotangentComplex_iso_single_of_isKoszulRegular_unconditional
    (h : Function.Surjective (algebraMap A (B : Type u)))
    (hI : Ideal.IsKoszulRegular (RingHom.ker (algebraMap A (B : Type u)))) :
    Nonempty (DerivedCategory.Q.obj (cotangentComplex A B) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} (B : Type u)) (-1)).obj
        (ModuleCat.of (B : Type u) (surjectionExtension A B h).Cotangent))
```

## Tag 08SL, a proposition

[Tag 08SL](https://stacks.math.columbia.edu/tag/08SL) in the Stacks Project.

**`CommAlgCat.isPerfect_and_hasTorAmplitude_cotangentComplexDerived_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LocalCompleteIntersectionPerfect.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LocalCompleteIntersectionPerfect.lean#L208). The attribute's comment: “perfectness and Tor amplitude in [-1, 0] are both proved, conditionally on the hypothesis e that L_{B/A} is isomorphic in D(B) to the naive complex of the given finite polynomial presentation; that isomorphism is Tag 08RB (only its degree-zero clause is in this library) together with Tag 08SK (absent from this library). All the local complete intersection hypothesis is used for, finite projectivity of the two terms, is proved”.

> **Stacks 08SL.** Let `A → B` be a local complete intersection map. Then the cotangent complex
> `L_{B/A}` is a perfect object of `D(B)` with Tor amplitude in `[-1, 0]`.
>
> The quasi-isomorphism `L_{B/A} ≅ NL(P → B)` with the naive complex of a finite polynomial
> presentation `P` is taken as the hypothesis `e`: it is the conjunction of Tag 08RB and Tag 08SK,
> neither of which is available in this library (see the module documentation). What the local
> complete intersection hypothesis supplies, and what is proved here, is that the two terms of
> `NL(P → B)` are finite projective `B`-modules — the conormal module `J/J²` by Tag 08RK through
> Tags 07CZ and 062I, and `⨁ B dxᵢ` by the canonical basis of the cotangent space. Perfectness is
> then immediate from the definition and the Tor-amplitude bound follows by Tag 0654, a projective
> module being flat.

```lean
theorem isPerfect_and_hasTorAmplitude_cotangentComplexDerived_of_isLocalCompleteIntersection
    (A : Type u) [CommRing A] (B : CommAlgCat.{u} A) {ι : Type u} [Finite ι]
    (P : Algebra.Generators A ↥B ι)
    (hlci : RingHom.IsLocalCompleteIntersection (algebraMap A ↥B))
    (e : cotangentComplexDerived.{u, u} A B ≅
      DerivedCategory.Q.obj (Algebra.Extension.naiveComplex P.toExtension)) :
    StacksDraft.Perfect.IsPerfect (cotangentComplexDerived.{u, u} A B) ∧
      StacksDraft.TorAmplitude.HasTorAmplitudeCanonical ↥B
        (cotangentComplexDerived.{u, u} A B) (-1) 0
```

**`CommAlgCat.isPerfect_and_hasTorAmplitude_cotangentComplexDerived_of_isLCI`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LocalCompleteIntersectionPerfectUnconditional.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LocalCompleteIntersectionPerfectUnconditional.lean#L311). The attribute's comment: “the proposition, under the source's single hypothesis that A → B is a local complete intersection (RingHom.IsLocalCompleteIntersection, Tag 07D0). Perfect is Tag 0657 (1) and Tor amplitude is Tag 0652 (1) at the canonical derived tensor product. The isomorphism of L_{B/A} with the naive complex of a finite polynomial presentation is constructed here from Tag 08RB (Stacks.Cotangent.naiveComparisonIso), the fundamental triangle of A → P → B (Proposition 08QX), Tag 08QH and Tag 08SK”. References: SGA 6 0 (4.3), “special case”; SGA 6 VIII (2.4), “special case”; SGA 6 XIV (2.1), “special case”.

> If `A → B` is a local complete intersection map, then the cotangent complex `L_{B/A}` is a
> perfect object of `D(B)` with Tor amplitude in `[-1, 0]`.
>
> Choose a finite polynomial presentation `P = A[x₁, …, x_n] → B`. The
> naive complex `NL(P → B) = (J/J² → ⨁ B dxᵢ)` consists of finite projective modules, by Tag 08RK,
> `CommAlgCat.isPerfect_and_hasTorAmplitude_cotangentComplexDerived_of_isLocalCompleteIntersection`;
> and `L_{B/A}` is isomorphic to it in `D(B)`
> (`CommAlgCat.cotangentComplexDerivedIsoNaiveComplexOfIsLocalCompleteIntersection`): by Tag 08RB
> `NL(P → B) ≅ τ_{≥ -1} L_{B/A}`, and by the fundamental triangle 08QS of `A → P → B` together with
> Tags 08QH and 08SK, `H^i(L_{B/A}) = 0` for `i ≤ -2`.

```lean
theorem isPerfect_and_hasTorAmplitude_cotangentComplexDerived_of_isLCI
    (A : Type u) [CommRing A] (B : CommAlgCat.{u} A)
    (hlci : RingHom.IsLocalCompleteIntersection (algebraMap A ↥B)) :
    StacksDraft.Perfect.IsPerfect (cotangentComplexDerived.{u, u} A B) ∧
      StacksDraft.TorAmplitude.HasTorAmplitudeCanonical ↥B
        (cotangentComplexDerived.{u, u} A B) (-1) 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.14, Tag 08SH](https://stacks.math.columbia.edu/tag/08SH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
