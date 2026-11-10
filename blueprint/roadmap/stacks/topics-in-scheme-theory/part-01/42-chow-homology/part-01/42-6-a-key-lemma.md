---
declaration: section
origin: cited
lean: exists_finite_local_extension_with_prescribed_localizations, AlgebraicGeometry.sum_ord_heightOneSymbol_eq_zero, Stacks.Chow.finsum_fracTameSymbolOrderAt_canonical_eq_zero, Stacks.Chow.finsum_heightOneOrd_tameSymbol_totalFraction_eq_zero, AlgebraicGeometry.sum_ord_localTameSymbol_eq_zero, Stacks.Chow.dvrMilnorTameSymbol, Stacks.Chow.dvrMilnorTameSymbol', milnorKTheoryOneAddEquiv
statement: formalized
proof: formalized
---

# 42.6 A key lemma

Section 42.6 of the Stacks Project, [Tag 0EAU](https://stacks.math.columbia.edu/tag/0EAU). 4 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EAV, a lemma

[Tag 0EAV](https://stacks.math.columbia.edu/tag/0EAV) in the Stacks Project.

**`exists_finite_local_extension_with_prescribed_localizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/FiniteLocalExtension/PrescribedLocalizations.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/FiniteLocalExtension/PrescribedLocalizations.lean#L101).

> Finite modifications at the finitely many primes above a nonzerodivisor in a Noetherian local
> ring come from one finite local modification.

```lean
public theorem exists_finite_local_extension_with_prescribed_localizations
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {t : A} (_htm : t ∈ IsLocalRing.maximalIdeal A) (ht : IsSMulRegular A t)
    {ι : Type v} [Finite ι] (q : ι → Ideal A) (hq : ∀ i, (q i).IsPrime)
    (hq_ne : ∀ i, q i ≠ IsLocalRing.maximalIdeal A) (hq_inj : Function.Injective q)
    (hV : ∀ p : Ideal A, p.IsPrime →
      (t ∈ p ↔ p = IsLocalRing.maximalIdeal A ∨ ∃ i, p = q i))
    (Bᵢ : ι → Type w) [∀ i, CommRing (Bᵢ i)]
    [∀ i, Algebra (Localization.AtPrime (q i)) (Bᵢ i)]
    [∀ i, Algebra A (Bᵢ i)]
    [∀ i, IsScalarTower A (Localization.AtPrime (q i)) (Bᵢ i)]
    (hinj : ∀ i, Function.Injective
      (algebraMap (Localization.AtPrime (q i)) (Bᵢ i)))
    (hfinite : ∀ i, Module.Finite (Localization.AtPrime (q i)) (Bᵢ i))
    (htorsion : ∀ i, ∃ n : ℕ, ∀ b : Bᵢ i, ∃ a : Localization.AtPrime (q i),
      algebraMap (Localization.AtPrime (q i)) (Bᵢ i) a =
        algebraMap A (Bᵢ i) (t ^ n) * b) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B) (_ : IsLocalRing B)
      (_ : IsLocalHom (algebraMap A B)),
      Function.Injective (algebraMap A B) ∧
      Module.Finite A B ∧
      Function.Bijective (IsLocalRing.ResidueField.map (algebraMap A B)) ∧
      (∃ n : ℕ, ∀ b : B, ∃ a : A,
        algebraMap A B a = algebraMap A B (t ^ n) * b) ∧
      ∃ ℓ : ∀ i, B →ₐ[A] Bᵢ i, ∀ i,
        letI := (ℓ i).toRingHom.toAlgebra
        IsLocalization ((q i).primeCompl.map (algebraMap A B)) (Bᵢ i)
```

## Tag 0EAW, a lemma

[Tag 0EAW](https://stacks.math.columbia.edu/tag/0EAW) in the Stacks Project.

**`AlgebraicGeometry.sum_ord_heightOneSymbol_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/ReciprocityNonzerodivisors.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Symbols/ReciprocityNonzerodivisors.lean#L764).

> **Stacks Project, Tag 0EAW.** Let `A` be a two-dimensional Noetherian local ring and let
> `a, b` be nonzerodivisors of `A`. The orders of vanishing of the symbols `d_{A_𝔮}(a, b)` along
> `A / 𝔮`, summed over the height-one primes `𝔮` of `A`, give zero.

```lean
theorem sum_ord_heightOneSymbol_eq_zero
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hdim : ringKrullDim A = 2) {a b : A}
    (ha : a ∈ nonZeroDivisors A) (hb : b ∈ nonZeroDivisors A) :
    ∃ hquot : ∀ q : {q : Ideal A // q.IsPrime ∧ q.height = 1},
        Ring.KrullDimLE 1 (A ⧸ q.1),
    (∑ᶠ q : {q : Ideal A // q.IsPrime ∧ q.height = 1},
        letI : q.1.IsPrime := q.2.1
        letI := hquot q
        let d := heightOneSymbol q ha hb
        Multiplicative.toAdd (WithZero.unzero
          (x := Ring.ordFrac (A ⧸ q.1) (d : q.1.ResidueField))
          ((Units.isUnit d).map (Ring.ordFrac (A ⧸ q.1))).ne_zero)) = 0
```

## Tag 0EAX, a lemma

[Tag 0EAX](https://stacks.math.columbia.edu/tag/0EAX) in the Stacks Project.

**`Stacks.Chow.finsum_fracTameSymbolOrderAt_canonical_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityCanonical.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityCanonical.lean#L123).

> **Stacks Project, Tag 0EAX: the Key Lemma.** Let `A` be a two-dimensional Noetherian local
> domain with fraction field `K` and let `f, g ∈ K^*`. Then
>
> `∑_{height(𝔮) = 1} ord_{A/𝔮}(∂_{A_𝔮}(f, g)) = 0`,
>
> the sum being over the height-one primes of `A`, with `∂_{A_𝔮}` the tame symbol of Stacks 0EAH on
> the one-dimensional Noetherian local ring `A_𝔮`
> (`Stacks.Chow.canonicalHeightOneSymbol`). Only finitely many primes contribute, by
> `Stacks.Chow.finite_fracTameSymbolOrderAt_support`, which is the first form the source gives the
> statement in.
>
> The proof is the source's:
> `Stacks.Chow.fracTameSymbolOrderAt_finsum_eq_zero_of_forall_nonZeroDivisors` expands a pair of
> fractions into four pairs of nonzerodivisors of `A`, and Stacks 0EAW
> (`Stacks.Chow.finsum_tameSymbolOrderAt_canonical_eq_zero`) kills each of the four.

```lean
theorem finsum_fracTameSymbolOrderAt_canonical_eq_zero [IsDomain A] [IsLocalRing A]
    (hdim : ringKrullDim A = 2) (f g : (FractionRing A)ˣ) :
    ∑ᶠ p : HeightOnePrime A,
      fracTameSymbolOrderAt hdim p (canonicalHeightOneSymbol p) f g = 0
```

**`Stacks.Chow.finsum_heightOneOrd_tameSymbol_totalFraction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityTotalFraction.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/ReciprocityTotalFraction.lean#L205). The attribute's comment: “for every two-dimensional Noetherian local ring, on the total ring of fractions”.

> **Stacks Project, Tag 0EAX: the Key Lemma, for every two-dimensional Noetherian local
> ring.** Let `A` be a two-dimensional Noetherian local ring, not necessarily a domain, with total
> ring of fractions `Q(A)`, and let `f, g ∈ Q(A)^*`. Then
>
> `∑_{height(𝔮) = 1} ord_{A/𝔮}(∂_{A_𝔮}(f, g)) = 0`,
>
> the sum being over the height-one primes of `A`, with `∂_{A_𝔮}` the tame symbol of Stacks 0EAH on
> the one-dimensional Noetherian local ring `A_𝔮`, applied to the images of `f` and `g` under
> `Stacks.Chow.heightOneFractionMap`. Only finitely many terms are nonzero, by
> `Stacks.Chow.finite_heightOneOrd_tameSymbol_totalFraction_support`.
>
> The proof is the source's: writing `f = a / b`, `g = c / d` expands the sum into four reciprocity
> sums of Stacks 0EAW, each of which vanishes.

```lean
theorem finsum_heightOneOrd_tameSymbol_totalFraction_eq_zero [IsLocalRing A]
    (hdim : ringKrullDim A = 2) (f g : (FractionRing A)ˣ) :
    ∑ᶠ p : HeightOnePrime A, heightOneOrd hdim p
      (tameSymbolOfKrullDimOne (ringKrullDim_localization_heightOnePrime p)
        (FractionRing (Localization.AtPrime p.1.asIdeal))
        (Units.map (heightOneFractionMap p).toMonoidHom f)
        (Units.map (heightOneFractionMap p).toMonoidHom g)) = 0
```

**`AlgebraicGeometry.sum_ord_localTameSymbol_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Symbols/Reciprocity.lean, line 1220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Symbols/Reciprocity.lean#L1220). The attribute's comment: “the second displayed form, the sum over all height-one primes”.

> **Stacks Project, Tags 02QJ and 0EAX.** Let `A` be a two-dimensional Noetherian local domain
> with fraction field `K` and let `f, g` be units of `K`. The orders of vanishing of the tame
> symbols `∂_{A_𝔮}(f, g)` along `A / 𝔮`, summed over the height-one primes `𝔮` of `A`, give zero.

```lean
theorem sum_ord_localTameSymbol_eq_zero
    {A : Type u} {K : Type v} [CommRing A] [IsDomain A] [IsNoetherianRing A]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [IsLocalRing A] (hdim : ringKrullDim A = 2)
    (f g : Kˣ) :
    ∃ (hquot : ∀ q : {q : Ideal A // q.IsPrime ∧ q.height = 1},
        Ring.KrullDimLE 1 (A ⧸ q.1)),
    (∑ᶠ q : {q : Ideal A // q.IsPrime ∧ q.height = 1},
        letI : q.1.IsPrime := q.2.1
        letI := hquot q
        let d := localTameSymbol q f g
        Multiplicative.toAdd (WithZero.unzero
          (x := Ring.ordFrac (A ⧸ q.1) (d : q.1.ResidueField))
          ((Units.isUnit d).map (Ring.ordFrac (A ⧸ q.1))).ne_zero)) = 0
```

## Tag 0EAY, a remark

[Tag 0EAY](https://stacks.math.columbia.edu/tag/0EAY) in the Stacks Project.

**`Stacks.Chow.dvrMilnorTameSymbol`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DvrTameSymbol/MilnorTameSymbol.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DvrTameSymbol/MilnorTameSymbol.lean#L338). The attribute's comment: “the tame symbol ∂_A : K^M_{i+1}(F) → K^M_i(κ) of a discrete valuation ring A with fraction field F and residue field κ, constructed as in Section 42.5”.

> **The tame symbol of a discrete valuation ring in every degree.** For a discrete
> valuation ring `A` with fraction field `F` and residue field `κ`, and a uniformizer `ϖ`, the
> homomorphism
>
> `∂_A : K^M_{i+1}(F) ⟶ K^M_i(κ)`
>
> of the remark. It is the coefficient of `ξ` in the image of the ring homomorphism
> `Stacks.Chow.dvrMilnorShiftMap`, which sends a unit `f` of `F` to `{f ϖ ^ -v(f)} + v(f) ξ`; that
> coefficient drops the degree by one. In degree two it is the tame symbol of Section 42.5
> (`Stacks.Chow.dvrMilnorTameSymbol_degree_two`, the formula of Stacks 02Q6; and
> `Stacks.Chow.dvrMilnorTameSymbol_milnorKTwoPureSymbol`, the comparison with
> `Stacks.Chow.dvrRegularTameSymbol` itself), and it is characterized in general by
> `Stacks.Chow.dvrMilnorTameSymbol_eq_zero_of_units` and
> `Stacks.Chow.dvrMilnorTameSymbol_uniformizer`.
>
> Only the discrete valuation ring case is proved here. The source's extension of `∂_A` to an
> excellent local domain of dimension one is a citation to [Kato-Milnor-K], and its extension to an
> arbitrary Noetherian local domain of dimension one is flagged in the source itself as a
> conjecture ("presumably"); neither is formalized.

```lean
def dvrMilnorTameSymbol (hϖ : Irreducible ϖ) (i : ℕ) :
    MilnorKTheory F (i + 1) →+ MilnorKTheory (ResidueField A) i
```

**`Stacks.Chow.dvrMilnorTameSymbol'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DvrTameSymbol/MilnorTameSymbol.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DvrTameSymbol/MilnorTameSymbol.lean#L363). The attribute's comment: “the existence of the tame symbol ∂_A : K^M_{i+1}(F) → K^M_i(κ) for A a discrete valuation ring, with no choice of uniformizer in the statement”.

> **The tame symbol `∂_A` of a discrete valuation ring, in every degree.** The map
> of `Stacks.Chow.dvrMilnorTameSymbol` for an unspecified uniformizer, so that the statement names
> no choice — as in the source, which asserts that a tame symbol exists rather than that it is
> unique (Section 42.5: "We do not claim there is a unique map with these properties").

```lean
def dvrMilnorTameSymbol' (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (F : Type v) [Field F] [Algebra A F] [IsFractionRing A F] (i : ℕ) :
    MilnorKTheory F (i + 1) →+ MilnorKTheory (ResidueField A) i
```

**`milnorKTheoryOneAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKDegreeOne.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKDegreeOne.lean#L133). The attribute's comment: “milnor_k_one”.

> The degree-one Milnor K-group of a field is its multiplicative group.

```lean
public noncomputable def milnorKTheoryOneAddEquiv (k : Type u) [Field k] :
    MilnorKTheory k 1 ≃+ Additive kˣ
```

**`milnorKTwoEquivTensorProductQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKDegreeTwo.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKDegreeTwo.lean#L302). The attribute's comment: “milnor_k_two”.

> The second Milnor K-group is the tensor square of the group of units modulo the
> Steinberg relations.

```lean
noncomputable def milnorKTwoEquivTensorProductQuotient (k : Type u) [Field k] :
    MilnorKTheory k 2 ≃ₗ[ℤ]
      (TensorProduct ℤ (Additive kˣ) (Additive kˣ) ⧸
        milnorKTwoSteinbergSubmodule k)
```

**`milnorKTheoryZeroAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKDegreeZero.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKDegreeZero.lean#L108). The attribute's comment: “milnor_k_zero”.

> The degree-zero Milnor K-group of a field is additively isomorphic to `ℤ`.

```lean
noncomputable def milnorKTheoryZeroAddEquiv (k : Type u) [Field k] :
    MilnorKTheory k 0 ≃+ ℤ
```

**`MilnorKTheory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKTheory.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyLemma/MilnorKTheory.lean#L82). The attribute's comment: “milnor_k_theory_of_a_field”.

> The `n`th Milnor K-group of a field `k`, realized as the image of the degree-`n`
> homogeneous component of the tensor algebra in its quotient by the Steinberg ideal.

```lean
abbrev MilnorKTheory (k : Type u) [Field k] (n : ℕ) : Type u
```

**`Stacks.Chow.pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/MilnorChowGroupOne.lean#L161). The attribute's comment: “the remark's closing sentence: the composition of the two displayed arrows is zero when i = 1 and j is arbitrary. The remark says this follows from Lemma 0EAX, and the proof here does run through 0EAX's content: it reduces to AlgebraicGeometry.sum_localMilnorBoundaryOrder_eq_zero at the two-dimensional local ring 𝒪_{closure {x}, y}, which reduces to AlgebraicGeometry.sum_ord_localTameSymbol_eq_zero -- the declaration registered for 0EAX, the vanishing of the sum of ord_{A/𝔮}(∂_{A_𝔮}(f, g)) over the height-one primes. The remark's preceding sentence, that it is not clear the composition is zero in general, is not a claim; for excellent X the remark cites [Kato-Milnor-K], and that citation is not formalized”.

> **Stacks 0GU9.** The three locally finite direct sums of Milnor K-groups of the tag form a
> complex: the tame-symbol differential followed by the divisor differential of Stacks 0GU3 is the
> zero homomorphism.
>
> This is the assertion of the tag. By
> `Stacks.Chow.pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary_of_forall` it suffices to
> check it one point of relative dimension `k + 2` and one point of relative dimension `k` at a
> time, which is `Stacks.Chow.finsum_pointClosureOrdBoundaryTerm_eq_zero`.

```lean
theorem pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary (k : ℤ) :
    (pointwiseDivisorDifferential C p k).comp (pointwiseMilnorBoundary C p k) = 0
```

**`Stacks.Chow.pointwiseDivisorDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean#L465). The attribute's comment: “the second of the two arrows of the remark's displayed diagram, in the case i = 1: the map ⊕_{δ(x) = j} K^M_1(κ(x)) ⟶ ⊕_{δ(x) = j - 1} K^M_0(κ(x)), which on the identifications K^M_1(κ(x)) = κ(x)^* and K^M_0(κ(x)) = ℤ of the remark is the order of vanishing”.

> **Stacks 0GU3.** The divisor differential from pointwise Milnor K₁-chains at the points of
> relative dimension `k + 1` to pointwise Milnor K₀-chains at the points of relative dimension `k`:
> each Milnor K₁-class is read as a nonzero rational function on the closure of its point, and the
> differential is the locally finite sum of the pushed-forward principal divisors, transported to
> the pointwise description of cycles of Stacks 0GU2.

```lean
def pointwiseDivisorDifferential (k : ℤ) :
    PointwiseKOneGroup C p k →+ PointwiseCycleGroup C p k
```

**`Stacks.Chow.pointwiseMilnorBoundary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseMilnorBoundary.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseMilnorBoundary.lean#L433). The attribute's comment: “the first of the two arrows of the remark's displayed diagram, in the case i = 1: the map ⊕_{δ(x) = j + 1} K^M_2(κ(x)) ⟶ ⊕_{δ(x) = j} K^M_1(κ(x)) which the remark builds out of the tame symbols ∂_A, taken here at the one-dimensional local rings 𝒪_{closure {x}, x'} of the Noetherian scheme X carrying the dimension function δ. For i ≥ 2 the same arrow needs the tame symbol in higher degrees at those local rings, which the remark takes from [Kato-Milnor-K]”.

> **Stacks 0GU9.** The first differential of the complex of the tag: the homomorphism from the
> locally finite direct sum of the degree-two Milnor K-groups at the points of relative dimension
> `k + 2` to the locally finite direct sum of the degree-one Milnor K-groups at the points of
> relative dimension `k + 1` whose coefficient at `x'` is the sum, over the points `x` of relative
> dimension `k + 2` specializing to `x'`, of the tame-symbol boundaries
> `∂_{𝒪_{closure {x}, x'}}` of the classes of the chain.

```lean
def pointwiseMilnorBoundary (k : ℤ) :
    PointwiseKTwoGroup C p k →+ PointwiseKOneGroup C p k
```

**`Stacks.Chow.milnorChainBoundary_comp_milnorChainBoundary_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/Arrows.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/Arrows.lean#L319). The attribute's comment: “the remark's closing sentence for the displayed arrows built from the tame symbols ∂_A by normalization and norm: when i = 1 and j is arbitrary the composition ⊕_{δ(x) = j + 2} K^M_2(κ(x)) ⟶ ⊕_{δ(x) = j + 1} K^M_1(κ(x)) ⟶ ⊕_{δ(x) = j} K^M_0(κ(x)) of the two arrows Stacks.Chow.milnorChainBoundary is zero, and it follows from Lemma 0EAX. Stated for X locally of finite type over the base of chapter 42 with the induced dimension function, and for X whose local rings of dimension one at the closures of points have finite normalization -- the case of a Nagata, in particular an excellent, X, which is the setting in which the remark constructs ∂_A by normalization and norm maps. There ∂_A is the tame symbol d_A of Section 42.5 in degree two and ord_A in degree one, so the arrows are the differentials of Stacks 0GU9, whose composite vanishes by Lemma 0EAX”.

> **Stacks 0EAY, the case `i = 1`: the composition of the two displayed arrows is zero.** Let
> `X` be locally of finite type over the base `(S, δ)` of chapter 42, with the induced dimension
> function `δ_X` (the relative dimension, Stacks 02JW), and suppose the local rings of dimension
> one of the closures of the points of `X` have finite normalization (as for `X` Nagata, in
> particular excellent, which is the setting in which the remark constructs the tame symbols by
> normalization and norm). Then for every `j` the composite
>
> `⨁_{δ(x) = j + 2} K^M_2(κ(x)) ⟶ ⨁_{δ(x) = j + 1} K^M_1(κ(x)) ⟶ ⨁_{δ(x) = j} K^M_0(κ(x))`
>
> of the arrows `Stacks.Chow.milnorChainBoundary` is zero. As the remark says, this follows from
> Lemma 0EAX: the two arrows are the tame-symbol and divisor differentials of Stacks 0GU9
> (`Stacks.Chow.milnorChainBoundary_one_apply_eq`, `Stacks.Chow.milnorChainBoundary_zero_eq`),
> whose composite vanishes by the key lemma 0EAX
> (`Stacks.Chow.pointwiseDivisorDifferential_comp_pointwiseMilnorBoundary`).

```lean
theorem milnorChainBoundary_comp_milnorChainBoundary_eq_zero
    (hfin : HasFiniteNormalizationPointClosureStalks X) (j : ℤ) :
    haveI := LocallyOfFiniteType.isLocallyNoetherian p
    (milnorChainBoundary (relativeDimension C.dimensionFunction p)
        (relativeDimension_lt_of_specializes C p) 0 j).comp
      (milnorChainBoundary (relativeDimension C.dimensionFunction p)
        (relativeDimension_lt_of_specializes C p) 1 (j + 1)) = 0
```

**`Stacks.Chow.dvrMilnorTameSymbol_one_eq_milnorKTwoTameSymbol`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/DegreeTwo.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/DegreeTwo.lean#L632). The attribute's comment: “the tame symbol ∂_A : K^M_{i+1}(F) → K^M_i(κ) of a discrete valuation ring is defined as in Section 42.5: in degree i = 1 it is, as a map K^M_2(F) → K^M_1(κ) = κ^*, the tame symbol d_A of Section 42.5 (Stacks 02Q1) descended along the presentation of K^M_2, for every choice of uniformizer”.

> **Stacks 0EAY: in degree two the tame symbol of a discrete valuation ring is the tame symbol of
> Section 42.5.** For a discrete valuation ring `A` with fraction field `F` and any uniformizer `ϖ`,
> the tame symbol `∂_A : K^M_2(F) → K^M_1(κ)` of the remark is the tame symbol `d_A` of Stacks 02Q1
> descended to Milnor K-theory, as maps.

```lean
theorem dvrMilnorTameSymbol_one_eq_milnorKTwoTameSymbol {A : Type u} [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] {F : Type u} [Field F] [Algebra A F] [IsFractionRing A F]
    {ϖ : A} (hϖ : Irreducible ϖ) :
    dvrMilnorTameSymbol (F := F) hϖ 1 =
      milnorKTwoTameSymbol (A := A) (K := F) (IsDiscreteValuationRing.ringKrullDim_eq_one A)
```

**`Stacks.Chow.sectionTameArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/SectionArrows.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/SectionArrows.lean#L102). The attribute's comment: “the first displayed arrow in the case i = 1: for a Noetherian (here: locally Noetherian) scheme X with a dimension function δ, the map ⊕_{δ(x) = j + 1} K^M_2(κ(x)) ⟶ ⊕_{δ(x) = j} K^M_1(κ(x)) whose coefficient at x' is the sum over the points x specializing to x' of the tame symbol ∂_A of Section 42.5 of the one-dimensional local ring A = 𝒪_{closure {x}, x'}”.

> **The first displayed arrow of Stacks 0EAY at `i = 1`**, from the tame symbol of
> Section 42.5.

```lean
def sectionTameArrow (j : ℤ) :
    DimMilnorChainGroup X δ (j + 1) (1 + 1) →+ DimMilnorChainGroup X δ j 1
```

**`Stacks.Chow.sectionOrdArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/SectionArrows.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/SectionArrows.lean#L181). The attribute's comment: “the second displayed arrow in the case i = 1: for a Noetherian (here: locally Noetherian) scheme X with a dimension function δ, the map ⊕_{δ(x) = j + 1} K^M_1(κ(x)) ⟶ ⊕_{δ(x) = j} K^M_0(κ(x)) whose coefficient at x' is the sum over the points x specializing to x' of ∂_A = ord_A on κ(x)^* = K^M_1(κ(x)) for A = 𝒪_{closure {x}, x'}, with values in ℤ = K^M_0”.

> **The second displayed arrow of Stacks 0EAY at `i = 1`**, from the order of vanishing.

```lean
def sectionOrdArrow (j : ℤ) :
    DimMilnorChainGroup X δ (j + 1) (0 + 1) →+ DimMilnorChainGroup X δ j 0
```

**`Stacks.Chow.sectionOrdArrow_comp_sectionTameArrow_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/SectionComplex.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolComparison/SectionComplex.lean#L480). The attribute's comment: “the remark's closing sentence for the arrows of a Noetherian (here: locally Noetherian) scheme X with a dimension function δ: when i = 1 and j is arbitrary the composition ⊕_{δ(x) = j + 2} K^M_2(κ(x)) ⟶ ⊕_{δ(x) = j + 1} K^M_1(κ(x)) ⟶ ⊕_{δ(x) = j} K^M_0(κ(x)) of the two displayed arrows, built from the tame symbols ∂_A of Section 42.5 of the one-dimensional local rings A = 𝒪_{closure {x}, x'}, is zero; the proof runs through Lemma 0EAX at the two-dimensional local rings 𝒪_{closure {x}, y}. The remark's statement that it is not clear the composition is zero in general is not a claim, and the citation [Kato-Milnor-K] for excellent X is not formalized”.

> **Stacks 0EAY: at `i = 1` the composition of the two displayed arrows is zero.** For a
> locally Noetherian scheme `X` with a dimension function `δ` and every `j`, the arrow
> `⨁_{δ(x) = j + 2} K^M_2(κ(x)) → ⨁_{δ(x) = j + 1} K^M_1(κ(x))` built from the tame symbols of
> Section 42.5 of the one-dimensional local rings `𝒪_{closure {x}, x'}`, followed by the arrow
> `⨁_{δ(x) = j + 1} K^M_1(κ(x)) → ⨁_{δ(x) = j} K^M_0(κ(x))` built from their orders of vanishing, is
> zero. As the remark says, this follows from Lemma 0EAX
> (`AlgebraicGeometry.sum_localMilnorBoundaryOrder_eq_zero`).

```lean
theorem sectionOrdArrow_comp_sectionTameArrow_eq_zero (j : ℤ) :
    (sectionOrdArrow δ j).comp (sectionTameArrow δ (j + 1)) = 0
```

**`Stacks.Chow.oneDimTameSymbol`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolGeneral/MilnorNorm.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolGeneral/MilnorNorm.lean#L57). The attribute's comment: “the extension of the tame symbol ∂_A : K^M_{i+1}(F) → K^M_i(κ) from discrete valuation rings to one-dimensional local domains using normalization and norm maps on K^M_i: for a Noetherian local domain A of dimension 1 with fraction field F, ∂_A is the sum over the maximal ideals 𝔫 of the normalization A' of N_{κ(𝔫)/κ} ∘ ∂_{A'_𝔫}, where A'_𝔫 is a discrete valuation ring with fraction field F and κ(𝔫)/κ is finite (Krull-Akizuki). This covers every Noetherian local domain of dimension 1, so in particular the excellent ones of the remark”.

> **The tame symbol `∂_A : K^M_{i+1}(F) → K^M_i(κ(A))` of a one-dimensional Noetherian local
> domain `A` with fraction field `F`**, obtained from the tame symbols of the discrete valuation
> rings `A'_𝔫` of its normalization by the norm maps `N_{κ(𝔫)/κ(A)}`.

```lean
def oneDimTameSymbol (A : Type u) [CommRing A] [IsDomain A] [IsLocalRing A] [IsNoetherianRing A]
    (F : Type u) [Field F] [Algebra A F] [IsFractionRing A F] (hdim : ringKrullDim A = 1)
    (i : ℕ) : MilnorKTheory F (i + 1) →+ MilnorKTheory (ResidueField A) i
```

**`Stacks.Chow.oneDimTameSymbol_eq_dvrMilnorTameSymbol'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolGeneral/MilnorNorm.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolGeneral/MilnorNorm.lean#L66). The attribute's comment: “the general tame symbol extends the one of a discrete valuation ring: when A is a discrete valuation ring, the symbol obtained by normalization and norm is the tame symbol ∂_A : K^M_{i+1}(F) → K^M_i(κ) defined as in Section 42.5”.

> **For a discrete valuation ring, `∂_A` is the tame symbol of Section 42.5.**

```lean
theorem oneDimTameSymbol_eq_dvrMilnorTameSymbol' (A : Type u) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] (F : Type u) [Field F] [Algebra A F] [IsFractionRing A F]
    (i : ℕ) :
    oneDimTameSymbol A F (IsDiscreteValuationRing.ringKrullDim_eq_one A) i =
      dvrMilnorTameSymbol' A F i
```

**`Stacks.Chow.milnorChainBoundary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TameSymbolGeneral/MilnorNorm.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TameSymbolGeneral/MilnorNorm.lean#L87). The attribute's comment: “the arrows of the remark's display, in every degree i: for a Noetherian scheme X with a dimension function δ, the map ⊕_{δ(x) = j + 1} K^M_{i+1}(κ(x)) ⟶ ⊕_{δ(x) = j} K^M_i(κ(x)) whose coefficient at x' is the sum over the points x with δ(x) = j + 1 specializing to x' of the tame symbol ∂_A, A = 𝒪_{closure {x}, x'}, applied to the class at x. Proved for X locally Noetherian and δ strictly decreasing along proper specializations, which includes the remark's setting; the second arrow of the display is the same map at (i - 1, j - 1)”.

> **The arrow `⨁_{δ(x) = j + 1} K^M_{i+1}(κ(x)) → ⨁_{δ(x) = j} K^M_i(κ(x))`**, for a locally
> Noetherian scheme `X` and a function `δ` strictly decreasing along proper specializations. The
> coefficient at `x'` is the sum over the points `x` with `δ(x) = j + 1` specializing to `x'` of
> `∂_{𝒪_{closure {x}, x'}}` applied to the class at `x`. A dimension function is strictly decreasing
> along proper specializations (`DimensionFunction`, property (a)), and on a Noetherian scheme a
> locally finite family is a finitely supported one
> (`Stacks.Chow.mem_dimMilnorChainGroup_iff_finite`), so this is the arrow of the remark.

```lean
def milnorChainBoundary {X : Scheme.{u}} [IsLocallyNoetherian X] (δ : X → ℤ)
    (hδ : ∀ ⦃x y : X⦄, x ⤳ y → x ≠ y → δ y < δ x) (i : ℕ) (j : ℤ) :
    DimMilnorChainGroup X δ (j + 1) (i + 1) →+ DimMilnorChainGroup X δ j i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.6, Tag 0EAU](https://stacks.math.columbia.edu/tag/0EAU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
