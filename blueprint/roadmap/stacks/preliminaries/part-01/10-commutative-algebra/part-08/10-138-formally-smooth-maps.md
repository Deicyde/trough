---
declaration: section
origin: cited
lean: Algebra.FormallySmooth.instTensorProduct, Algebra.FormallySmooth.comp, Algebra.instFormallySmoothMvPolynomial, Algebra.FormallySmooth.iff_split_surjection, Algebra.FormallySmooth.tfae_lifting_of_surjective, KaehlerDifferential.exists_retraction_mapBaseChange, KaehlerDifferential.exists_retraction_kerCotangentToTensor, Algebra.FormallySmooth.exists_retraction_mapCotangent
statement: formalized
proof: formalized
---

# 10.138 Formally smooth maps

Section 10.138 of the Stacks Project, [Tag 00TH](https://stacks.math.columbia.edu/tag/00TH). 12 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00TJ, a lemma

[Tag 00TJ](https://stacks.math.columbia.edu/tag/00TJ) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallySmooth.instTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallySmooth.instTensorProduct#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Smooth/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/Basic.lean#L92) (StacksFrontier): “formal smoothness is stable under base change”. References: EGA 0 (19.3.5), “(iii), special case”; EGA 0 (19.4.2), “Necessity, special case”; EGA 0 (19.4.6), “special case”; EGA 0 (19.9.3), “discrete topology”.

## Tag 031H, a lemma

[Tag 031H](https://stacks.math.columbia.edu/tag/031H) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallySmooth.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallySmooth.comp#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Smooth/Basic.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/Basic.lean#L103) (StacksFrontier): “formal smoothness is stable under composition”. References: EGA 0 (19.3.5), “(ii), special case”; EGA 0 (19.5.4.4), “partial”; EGA IV (17.1.3), “(ii), special case”.

## Tag 00TK, a lemma

[Tag 00TK](https://stacks.math.columbia.edu/tag/00TK) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.instFormallySmoothMvPolynomial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.instFormallySmoothMvPolynomial#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L250) (StacksFrontier). References: EGA 0 (19.3.2), “special case”; EGA 0 (19.3.3); EGA 0 (19.5.4.4), “special case”; EGA 0 (19.10.3); EGA 0 (21.2.7), “special case”; SGA 6 0 (4.4), “partial”.

## Tag 00TL, a lemma

[Tag 00TL](https://stacks.math.columbia.edu/tag/00TL) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.FormallySmooth.iff_split_surjection`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FormallySmooth.iff_split_surjection#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L252) (StacksFrontier).

## Tag 031J, a proposition

[Tag 031J](https://stacks.math.columbia.edu/tag/031J) in the Stacks Project.

**`Algebra.FormallySmooth.tfae_lifting_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/Presentation.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/Presentation.lean#L162). The attribute's comment: “The presentation `P` is a variable, so conditions 2 and 3 hold for some `P` iff they hold for every `P` (each is equivalent to condition 1); Stacks' conditions (2)/(3) are item 2, (4)/(5) are item 3 and (6) is item 4. Item 5 is Mathlib's `Algebra.FormallySmooth`, which is (6) by definition.”.

> **Stacks 031J.** Let `R → S` be a ring map, let `P` be a formally smooth `R`-algebra and let
> `P → S` be a surjection with kernel `J`. The following are equivalent:
>
> 1. `S` is formally smooth over `R` in the sense of Stacks 00TI: for every `R`-algebra `B` and every
>    ideal `I ⊆ B` of square zero, every `R`-algebra map `S → B ⧸ I` lifts to an `R`-algebra map
>    `S → B`;
> 2. the surjection `P ⧸ J² → S` admits an `R`-algebra section;
> 3. the sequence `0 → J/J² → S ⊗[P] Ω[P⁄R] → Ω[S⁄R] → 0` is split short exact, i.e. its first map
>    is injective and its second map admits an `S`-linear section;
> 4. `Ω[S⁄R]` is a projective `S`-module and `H₁(NL_{S/R}) = 0`;
> 5. `S` is an `Algebra.FormallySmooth R`-algebra (Mathlib's definition, which is condition 4).
>
> The lifting condition quantifies over `R`-algebras `B` in the universe `max u v`, where `R : Type u`
> and `S : Type v`, the universe in which Mathlib proves the lifting criterion.

```lean
public theorem Algebra.FormallySmooth.tfae_lifting_of_surjective.{u, v, w}
    {R : Type u} {S : Type v} {P : Type w} [CommRing R] [CommRing S] [CommRing P]
    [Algebra R S] [Algebra R P] [Algebra P S] [IsScalarTower R P S]
    [Algebra.FormallySmooth R P] (hf : Function.Surjective (algebraMap P S)) :
    List.TFAE
      [ ∀ ⦃B : Type (max u v)⦄ [CommRing B] [Algebra R B] (I : Ideal B), I ^ 2 = ⊥ →
          Function.Surjective ((Ideal.Quotient.mkₐ R I).comp : (S →ₐ[R] B) → S →ₐ[R] B ⧸ I),
        ∃ g, (IsScalarTower.toAlgHom R P S).kerSquareLift.comp g = AlgHom.id R S,
        Function.Injective (kerCotangentToTensor R P S) ∧
          ∃ σ : Ω[S⁄R] →ₗ[S] S ⊗[P] Ω[P⁄R], mapBaseChange R P S ∘ₗ σ = LinearMap.id,
        Module.Projective S Ω[S⁄R] ∧ Subsingleton (Algebra.H1Cotangent R S),
        Algebra.FormallySmooth R S ]
```

## Tag 031K, a lemma

[Tag 031K](https://stacks.math.columbia.edu/tag/031K) in the Stacks Project.

**`KaehlerDifferential.exists_retraction_mapBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Kaehler/BaseChange.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Kaehler/BaseChange.lean#L199). The attribute's comment: “Split short exactness, i.e. the two assertions of the tag that are not already in Mathlib (exactness at `Ω_{C/A}` is `KaehlerDifferential.exact_mapBaseChange_map` and surjectivity is `KaehlerDifferential.map_surjective`), stated as the existence of a retraction of the injection: that is at once its injectivity and the splitting. See the module docstring.”. References: EGA 0 (20.5.7), “(ii), sufficiency”; EGA IV (17.2.3), “(ii), affine case”; EGA 0 (20.7.3), “discrete case, necessity”; EGA 0 (20.7.2), “sufficiency”; SGA 1 II (4.3), “(i) inj., affine case”; SGA 1 II (4.4), “special case”; SGA 6 VIII (2.6), “partial”.

> **The sequence of differentials of a tower is split short exact.** Let `R → A → B` be ring
> maps with `A → B` formally smooth. Then the canonical injection `B ⊗_A Ω_{A/R} → Ω_{B/R}` admits
> a `B`-linear retraction, so that `0 → B ⊗_A Ω_{A/R} → Ω_{B/R} → Ω_{B/A} → 0` is a split short
> exact sequence.

```lean
public theorem KaehlerDifferential.exists_retraction_mapBaseChange (R : Type*) [CommRing R]
    (A B : Type*) [CommRing A] [CommRing B] [Algebra R A] [Algebra A B] [Algebra R B]
    [IsScalarTower R A B] [Algebra.FormallySmooth A B] :
    ∃ r : Ω[B⁄R] →ₗ[B] B ⊗[A] Ω[A⁄R],
      r ∘ₗ KaehlerDifferential.mapBaseChange R A B = LinearMap.id
```

## Tag 06A6, a lemma

[Tag 06A6](https://stacks.math.columbia.edu/tag/06A6) in the Stacks Project.

**`KaehlerDifferential.exists_retraction_kerCotangentToTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Conormal.lean, line 1110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/Conormal.lean#L1110). The attribute's comment: “Split exactness, i.e. the two assertions of the tag that are not already in Mathlib (exactness at `Ω_{B/A} ⊗_B C` is `KaehlerDifferential.exact_kerCotangentToTensor_mapBaseChange` and surjectivity on the right is `KaehlerDifferential.mapBaseChange_surjective`), stated as the existence of a retraction of the injection `J/J² → Ω_{B/A} ⊗_B C`: that single datum is at once its injectivity and the splitting. See the module docstring.”. References: EGA 0 (20.5.14), “injectivity, splitting”; EGA IV (17.2.5), “injectivity, affine”; EGA 0 (22.4.6), “(22.4.6.1)”; EGA 0 (22.4.4.2), “partial”; SGA 3 III (4.25), “(ii) inj. + splitting”.

> **Stacks 06A6.** If `S` is a formally smooth `R`-algebra and `P → S` is surjective with kernel
> `J`, then the canonical map `J/J² → S ⊗[P] Ω[P⁄R]` of Stacks 00RU admits a retraction, so that the
> sequence `0 → J/J² → S ⊗[P] Ω[P⁄R] → Ω[S⁄R] → 0` is split exact. Nothing is required of `P`.

```lean
public theorem KaehlerDifferential.exists_retraction_kerCotangentToTensor (R P S : Type*)
    [CommRing R] [CommRing P] [CommRing S] [Algebra R P] [Algebra P S] [Algebra R S]
    [IsScalarTower R P S] [Algebra.FormallySmooth R S]
    (hf : Function.Surjective (algebraMap P S)) :
    ∃ l : S ⊗[P] Ω[P⁄R] →ₗ[P] (RingHom.ker (algebraMap P S)).Cotangent,
      l ∘ₗ kerCotangentToTensor R P S = LinearMap.id
```

## Tag 06A7, a lemma

[Tag 06A7](https://stacks.math.columbia.edu/tag/06A7) in the Stacks Project.

**`Algebra.FormallySmooth.exists_retraction_mapCotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Conormal.lean, line 1602](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/Conormal.lean#L1602). The attribute's comment: “Split exactness, i.e. the part of the tag that is not already the neighbouring tag 065V, stated as the existence of a retraction of the injection `I/I² → J/J²`: given 065V's exactness that single datum is at once its injectivity and the splitting. Exactness at `J/J²` and surjectivity of `KaehlerDifferential.kerCotangentToTensor A B C` are 065V, hold with no hypothesis on `A → B`, and are not restated. See the module docstring.”.

> **Stacks 06A7.** Let `A → B → C` be ring maps with `A → C` surjective and `A → B` formally
> smooth, and put `I = ker (A → C)` and `J = ker (B → C)`. Then the map `ι : I/I² → J/J²` of
> Stacks 065V admits a retraction; in particular `ι` is injective, so that the sequence
> `0 → I/I² → J/J² → Ω[B⁄A] ⊗[B] B/J → 0` of Stacks 065V is split short exact.

```lean
public theorem Algebra.FormallySmooth.exists_retraction_mapCotangent
    (A B C : Type*) [CommRing A] [CommRing B] [CommRing C] [Algebra A B] [Algebra B C]
    [Algebra A C] [IsScalarTower A B C] [Algebra.FormallySmooth A B]
    (h : Function.Surjective (algebraMap A C)) :
    ∃ ρ : (RingHom.ker (algebraMap B C)).Cotangent →ₗ[A]
        (RingHom.ker (algebraMap A C)).Cotangent,
      ρ ∘ₗ Ideal.mapCotangent (RingHom.ker (algebraMap A C))
        (RingHom.ker (algebraMap B C)) (Algebra.ofId A B)
        (((RingHom.comap_ker (algebraMap B C) (algebraMap A B)).trans
          (congrArg RingHom.ker (IsScalarTower.algebraMap_eq A B C).symm)).ge) =
        LinearMap.id
```

## Tag 00TN, a proposition

[Tag 00TN](https://stacks.math.columbia.edu/tag/00TN) in the Stacks Project.

**`Algebra.finitePresentation_and_lifting_iff_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Basic.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/Basic.lean#L146). The attribute's comment: “The lifting property (Definition 00TI) is spelled out, not Mathlib's `FormallySmooth`, which is defined by the cotangent condition. The test rings `B` range over `Type (max u w)` for an arbitrary universe `w`, with `R : Type u`: every universe containing `R`'s. `Algebra.Smooth` is Definition 00T2: finite presentation, `Ω[S⁄R]` projective (finite by finite presentation) and `H¹(L_{S/R}) = 0`.”.

> **Stacks 00TN.** Let `R → S` be a ring map. Then `R → S` is of finite presentation and formally
> smooth in the sense of Stacks 00TI (every `R`-algebra map `S → B ⧸ I`, for `I` an ideal of square
> zero in an `R`-algebra `B`, lifts to an `R`-algebra map `S → B`) if and only if `R → S` is smooth
> in the sense of Stacks 00T2.

```lean
theorem finitePresentation_and_lifting_iff_smooth {R : Type u} {S : Type v} [CommRing R]
    [CommRing S] [Algebra R S] :
    (FinitePresentation R S ∧ ∀ (B : Type (max u w)) [CommRing B] [Algebra R B] (I : Ideal B),
      I ^ 2 = ⊥ → ∀ g : S →ₐ[R] B ⧸ I, ∃ f : S →ₐ[R] B, (Ideal.Quotient.mkₐ R I).comp f = g) ↔
      Smooth R S
```

## Tag 0CAQ, a lemma

[Tag 0CAQ](https://stacks.math.columbia.edu/tag/0CAQ) in the Stacks Project.

**`smooth_descends_to_filtered_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/SpreadingOut/Smooth.lean, line 1346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/SpreadingOut/Smooth.lean#L1346).

> **Stacks Tag 0CAQ (Lemma 10.138.15).** Let `I` be a filtered category and
> `F : I ⥤ CommRingCat` a filtered system of commutative rings with colimit
> `A = colimit F` and structure maps `ψ_i = colimit.ι F i`. If `A → B` (given by a
> morphism `f : colimit F ⟶ B`) is a smooth ring map, then there exist an index `i`,
> a commutative ring `B_i`, and a smooth ring map `g : A_i → B_i`, such that `B` is
> isomorphic, as an `A`-algebra, to the base change `B_i ⊗_{A_i} A` of `B_i` along
> the structure map `ψ_i : A_i → A`.

```lean
theorem smooth_descends_to_filtered_colimit
    {I : Type u} [SmallCategory I] [IsFiltered I] (F : I ⥤ CommRingCat.{u})
    (B : CommRingCat.{u}) (f : colimit F ⟶ B) :
    letI : Algebra (↑(colimit F) : Type u) (↑B : Type u) := f.hom.toAlgebra
    RingHom.Smooth f.hom →
    ∃ (i : I) (Bi : CommRingCat.{u}) (g : F.obj i ⟶ Bi),
      letI : Algebra (↑(F.obj i) : Type u) (↑Bi : Type u) := g.hom.toAlgebra
      letI : Algebra (↑(F.obj i) : Type u) (↑(colimit F) : Type u) :=
        (colimit.ι F i).hom.toAlgebra
      RingHom.Smooth g.hom ∧
      (letI : Algebra (↑(colimit F) : Type u) (↑B : Type u) := f.hom.toAlgebra
       letI := Algebra.TensorProduct.rightAlgebra
         (R := (↑(F.obj i) : Type u)) (A := (↑Bi : Type u)) (B := (↑(colimit F) : Type u))
       Nonempty ((↑B : Type u) ≃ₐ[(↑(colimit F) : Type u)]
         TensorProduct (↑(F.obj i) : Type u) (↑Bi : Type u) (↑(colimit F) : Type u)))
```

## Tag 06CM, a lemma

[Tag 06CM](https://stacks.math.columbia.edu/tag/06CM) in the Stacks Project.

**`Algebra.FormallySmooth.iff_tensorProduct_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/FaithfullyFlatDescent.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/FaithfullyFlatDescent.lean#L39). The attribute's comment: “The source's `S' = S ⊗_R R'` is written `R' ⊗[R] S`, Mathlib's order for a base change.”. References: EGA 0 (19.3.5), “(iii), special case”; EGA 0 (19.4.6), “special case”; SGA 3 XIX (2.1), “special case”.

> Let `R → R'` be faithfully flat. Then `S` is formally smooth over `R` if and only if the
> base change `R' ⊗_R S` is formally smooth over `R'`.

```lean
theorem iff_tensorProduct_of_faithfullyFlat [Module.FaithfullyFlat R R'] :
    FormallySmooth R S ↔ FormallySmooth R' (R' ⊗[R] S)
```

## Tag 07K4, a lemma

[Tag 07K4](https://stacks.math.columbia.edu/tag/07K4) in the Stacks Project.

**`Stacks.Smooth.strongLifting_specMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/StrongLifting.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/StrongLifting.lean#L144). The attribute's comment: “the geometric form for the spectrum of a smooth ring map”.

> **The ring dictionary for the strong lifting property.** The spectrum of a smooth ring map
> has the strong lifting property; the lift is the one produced by Algebra, Lemma 10.138.17.

```lean
theorem strongLifting_specMap {R A : CommRingCat.{u}} {ψ : R ⟶ A} (hψ : RingHom.Smooth ψ.hom) :
    StrongLifting (Spec.map ψ)
```

**`Stacks.Smooth.strongLifting_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/StrongLifting.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/StrongLifting.lean#L174). The attribute's comment: “the geometric form for a smooth morphism of affine schemes”.

> **A smooth morphism of affine schemes has the strong lifting property.**

```lean
theorem strongLifting_of_isAffine {X S : Scheme.{u}} (f : X ⟶ S) [IsAffine X] [IsAffine S]
    [AlgebraicGeometry.Smooth f] : StrongLifting f
```

**`Stacks.Smooth.exists_lift_of_isClosedImmersion_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/StrongLifting.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/StrongLifting.lean#L193). The attribute's comment: “the lifting problem along a thickening of affine schemes”. References: SGA 3 III (2.5), “(a), special case”; SGA 3 IX (3.3), “special case”.

> **Lifting along a thickening for a smooth morphism of affine schemes.** Let `f : X ⟶ S` be a
> smooth morphism of affine schemes, let `i : T ⟶ T'` be a closed immersion of schemes with `T'`
> affine which is surjective on points, and let `a : T ⟶ X` and `h : T' ⟶ S` present a lifting
> problem for `f` along `i`. Then there is a morphism `b : T' ⟶ X` with `b ≫ f = h` and
> `i ≫ b = a`.
>
> The thickening is the spectrum of the surjection `i.appTop` on global sections, whose kernel is
> locally nilpotent by
> `AlgebraicGeometry.isLocallyNilpotent_ker_appTop_of_surjective`, so
> `Stacks.Smooth.strongLifting_of_isAffine` applies.

```lean
theorem exists_lift_of_isClosedImmersion_of_surjective {X S T T' : Scheme.{u}} (f : X ⟶ S)
    [IsAffine X] [IsAffine S] [AlgebraicGeometry.Smooth f] [IsAffine T'] {i : T ⟶ T'}
    [IsClosedImmersion i] (hi : Function.Surjective i.base) (a : T ⟶ X) (h : T' ⟶ S)
    (hcomm : a ≫ f = i ≫ h) :
    ∃ b : T' ⟶ X, b ≫ f = h ∧ i ≫ b = a
```

**`main_theorem07K4`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smooth/Lifting.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smooth/Lifting.lean#L130). References: EGA 0 (19.0.1), “special case”; EGA 0 (19.3.10.1), “special case”; EGA 0 (19.5.6.4), “special case”; EGA IV (17.14.2), “partial”; SGA 1 III (5.2), “special case”; SGA 3 III (0.17), “special case”; SGA 3 III (2.3), “(a), special case”; SGA 3 III (2.5), “(a), special case”; SGA 3 IX (3.3), “special case”; SGA 3 XI (1.5), “partial”.

> **Smooth strong lifting**: a smooth ring map `R → S` has the lifting
> property with respect to locally nilpotent ideals. For any commutative
> `R`-algebra `A` with a locally nilpotent ideal `I`, every `R`-algebra map
> `S → A ⧸ I` lifts to an `R`-algebra map `S → A`.

```lean
theorem main_theorem07K4
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Algebra.Smooth R S]
    (A : Type*) [CommRing A] [Algebra R A] (I : Ideal A)
    (hI : Ideal.IsLocallyNilpotent I)
    (g : S →ₐ[R] A ⧸ I) :
    ∃ f : S →ₐ[R] A, (Ideal.Quotient.mkₐ R I).comp f = g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.138, Tag 00TH](https://stacks.math.columbia.edu/tag/00TH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
