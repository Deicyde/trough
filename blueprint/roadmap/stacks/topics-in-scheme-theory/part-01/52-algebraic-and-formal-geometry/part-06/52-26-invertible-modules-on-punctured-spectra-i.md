---
declaration: section
origin: cited
lean: Stacks.Algebraization.picRestrictionInjOnTorsion, Stacks.Algebraization.puncturedClosedFibreRestriction_injOn_torsion, Stacks.Algebraization.kollar_picRestrictionInjective, Stacks.Serre.LocalizationDepth.two_le_ringDepth_localization_of_isDualizingComplex, Stacks.Algebraization.picRestrictionInjective_of_regularQuotient_of_depth, Stacks.Algebraization.hasDualizingComplexOfRegularQuotient, Stacks.Algebraization.twoLeDepthLocalization_of_four_le_depth, Stacks.Algebraization.three_le_depth_quotient_iff_four_le_depth
statement: formalized
proof: formalized
---

# 52.26 Invertible modules on punctured spectra, I

Section 52.26 of the Stacks Project, [Tag 0F29](https://stacks.math.columbia.edu/tag/0F29). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F2A, a lemma

[Tag 0F2A](https://stacks.math.columbia.edu/tag/0F2A) in the Stacks Project.

**`Stacks.Algebraization.picRestrictionInjOnTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardTorsion.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardTorsion.lean#L431). The attribute's comment: “conditional only on the polynomiality of the Euler characteristics of the twists (Tag 0F27), which this development does not prove”.

> **Stacks Project, Tag 0F2A.** Let `(A, 𝔪)` be a Noetherian local ring and let `f ∈ 𝔪` be a
> nonzerodivisor with `depth(A/fA) ≥ 2`. Let `U` be the punctured spectrum of `A` and `U₀` the
> punctured spectrum of `A/fA`. Then `Pic(U) → Pic(U₀)` is injective on torsion.
>
> Two classes of finite order with the same restriction have a difference of finite order
> restricting to zero, and such a difference is zero by
> `Stacks.Algebraization.eq_zero_of_schemePullbackClass_eq_zero_of_isOfFinAddOrder`.
>
> Beyond the tag's own hypotheses this carries one thing: `hpoly`, which is [Stacks, Tag 0F27] and
> which this development does not prove. It is a statement about Euler characteristics of twists of
> coherent triples; it mentions neither the Picard group nor any restriction map, so the conclusion
> is nowhere assumed. The `f`-torsion-freeness of `𝒪_U` that the rest of this section carries is
> *not* assumed here -- it is proved, from `f` being a nonzerodivisor, by
> `Stacks.Algebraization.isFTorsionFree_unitModule`.

```lean
public theorem picRestrictionInjOnTorsion (A : Type u) [CommRing A] [IsLocalRing A]
    [IsNoetherianRing A] (f : A) (hfm : f ∈ maximalIdeal A) (hreg : IsRegular f)
    (hb : 2 ≤ Module.depth A (maximalIdeal A) (A ⧸ Ideal.span {f}))
    (hpoly : IsCoherentTripleHilbertPolynomial.{u}) :
    Set.InjOn (Stacks.Picard.schemePullbackClass (puncturedClosedFibreRestriction A f))
      {x : Stacks.Picard.ofScheme (Stacks.Divisors.puncturedSpectrum A).toScheme |
        IsOfFinAddOrder x}
```

**`Stacks.Algebraization.puncturedClosedFibreRestriction_injOn_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardTorsionInjective.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardTorsionInjective.lean#L59).

> **Stacks Project, Tag 0F2A.** Let `(A, 𝔪)` be a Noetherian local ring and let `f ∈ 𝔪` be a
> nonzerodivisor with `depth(A/fA) ≥ 2`. Let `U` be the punctured spectrum of `A` and `U₀` the
> punctured spectrum of `A/fA`. Then `Pic(U) → Pic(U₀)` is injective on torsion.
>
> The map is pullback of invertible modules along the restriction `U₀ ⟶ U` of the closed immersion
> `Spec(A/fA) ⟶ Spec A`. This is `Stacks.Algebraization.picRestrictionInjOnTorsion` with its
> polynomiality argument supplied by `Stacks.Algebraization.isCoherentTripleHilbertPolynomial`.

```lean
public theorem puncturedClosedFibreRestriction_injOn_torsion (A : Type u) [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] (f : A) (hfm : f ∈ maximalIdeal A) (hreg : IsRegular f)
    (hb : 2 ≤ Module.depth A (maximalIdeal A) (A ⧸ Ideal.span {f})) :
    Set.InjOn (Stacks.Picard.schemePullbackClass (puncturedClosedFibreRestriction A f))
      {x : Stacks.Picard.ofScheme (Stacks.Divisors.puncturedSpectrum A).toScheme |
        IsOfFinAddOrder x}
```

## Tag 0F2B, a proposition

[Tag 0F2B](https://stacks.math.columbia.edu/tag/0F2B) in the Stacks Project.

**`Stacks.Algebraization.kollar_picRestrictionInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardKollar.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardKollar.lean#L290). The attribute's comment: “the proposition: Pic(U) → Pic(U₀) is injective”.

> **Stacks Project, Tag 0F2B** (Kollár). Let `(A, 𝔪)` be a Noetherian local ring and `f ∈ 𝔪`.
> Assume
>
> 1. `A` has a dualizing complex,
> 2. `f` is a nonzerodivisor,
> 3. `depth(A/fA) ≥ 2`, and
> 4. every prime `𝔭 ∋ f` with `dim(A/𝔭) = 2` has `depth(A_𝔭) ≥ 2`.
>
> Let `U`, resp. `U₀`, be the punctured spectrum of `A`, resp. of `A/fA`. Then `Pic(U) → Pic(U₀)`
> is injective. Finally, if (1), (2), (3) hold, `A` satisfies Serre's condition `(S₂)` and
> `dim(A) ≥ 4`, then (4) holds.
>
> This is the proposition's own conclusion, under the source's four hypotheses and nothing else:
> `Stacks.Algebraization.picRestrictionInjective_kollar`, after translating hypothesis (3) into
> `depth(A) ≥ 3` by `Stacks.Algebraization.le_depth_quotient_span_singleton_iff` and replacing the
> dualizing complex by the unique shift of it that is normalized
> (`Dualizing.exists_isNormalizedDualizingComplex_shift`).
>
> The source's closing sentence — that (1), (2), (3) together with `(S₂)` and `dim(A) ≥ 4` imply
> (4) — is the other half of the tag, and is
> `Stacks.Serre.LocalizationDepth.two_le_ringDepth_localization_of_isDualizingComplex`, which
> carries the tag's attribute for that assertion. The two attribute strings partition the
> proposition, so this one claims only the injectivity.

```lean
public theorem kollar_picRestrictionInjective (A : Type u) [CommRing A] [IsLocalRing A]
    [IsNoetherianRing A] (f : A) (hfm : f ∈ IsLocalRing.maximalIdeal A) :
    ∀ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K →
      IsSMulRegular A f →
      2 ≤ Module.depth A (IsLocalRing.maximalIdeal A) (A ⧸ Ideal.span {f}) →
      (∀ p : Ideal A, ∀ _ : p.IsPrime, f ∈ p → ringKrullDim (A ⧸ p) = 2 →
        2 ≤ Module.depth (Localization.AtPrime p)
          (IsLocalRing.maximalIdeal (Localization.AtPrime p)) (Localization.AtPrime p)) →
      Function.Injective
        (Stacks.Picard.schemePullbackClass (puncturedClosedFibreRestriction A f))
```

**`Stacks.Serre.LocalizationDepth.two_le_ringDepth_localization_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Serre/LocalizationDepthCodimension.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Serre/LocalizationDepthCodimension.lean#L165). The attribute's comment: “the last assertion: (S₂) and dimension at least four give hypothesis (4)”.

> **The last assertion of [Stacks, Tag 0F2B].** Let `A` be a Noetherian local ring admitting a
> dualizing complex, satisfying Serre's condition `(S₂)` and of dimension at least four. Then the
> localization of `A` at a prime whose quotient has dimension two has depth at least two, which is
> the fourth hypothesis of that source's proposition.
>
> A ring with a dualizing complex is universally catenary, hence catenary, so this is the
> preceding statement. The source restricts the primes to those containing an element `f` which it
> assumes to be a nonzerodivisor with `depth(A ⧸ fA) ≥ 2`; neither `f` nor those two hypotheses
> enter the argument.

```lean
theorem two_le_ringDepth_localization_of_isDualizingComplex (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] {K : DerivedCategory (ModuleCat.{u} A)}
    (hK : Dualizing.IsDualizingComplex K) (hS₂ : PropertySkRing A 2)
    (hdim : 4 ≤ ringKrullDim A) :
    ∀ p : PrimeSpectrum A, ringKrullDim (A ⧸ p.asIdeal) = 2 →
      2 ≤ ringDepth (Localization.AtPrime p.asIdeal)
```

## Tag 0FIX, a remark

[Tag 0FIX](https://stacks.math.columbia.edu/tag/0FIX) in the Stacks Project.

**`Stacks.Algebraization.picRestrictionInjective_of_regularQuotient_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivityDepthFour.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivityDepthFour.lean#L205). The attribute's comment: “the SGA2 lemma: for a Noetherian local ring that is a quotient of a regular ring and a nonzerodivisor `f` of the maximal ideal with `depth(A/fA) ≥ 3`, the map `Pic(U) → Pic(U₀)` from the punctured spectrum of `A` to that of `A/fA` is injective. The five hypotheses of the source are all demanded. The Euler characteristic of the invertible coherent triple completing a module trivial on `U₀` is shown to vanish in this depth, which by [Stacks, Tag 0F28] trivialises the module; the finiteness of `H^2` of its sections that this needs is [Stacks, Tag 0BPY]. The source's footnote that hypothesis (a) follows from hypothesis (b) is `twoLeDepthLocalization_of_dim_eq_one`, and the dualizing complex of a quotient of a regular ring is `hasDualizingComplexOfRegularQuotient`.”. References: SGA 2 XI (3.16), “more general”.

> [SGA2, Exposé XI, Lemma 3.16]. Let `(A, 𝔪)` be a Noetherian local ring and `f ∈ 𝔪`. Assume
> `A` is a quotient of a regular ring `R`, that `f` is a nonzerodivisor, and that (a)
> `depth(A_𝔭) ≥ 2` for every prime `𝔭` with `dim(A/𝔭) = 1` and (b) `depth(A/fA) ≥ 3`. Let `U`,
> resp. `U₀`, be the punctured spectrum of `A`, resp. `A/fA`. Then `Pic(U) → Pic(U₀)` is
> injective.

```lean
theorem picRestrictionInjective_of_regularQuotient_of_depth (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] (f : A) (hfm : f ∈ maximalIdeal A) (_R : Type u)
    [CommRing _R] [IsRegularRing _R] (_π : _R →+* A) (_hπ : Function.Surjective _π)
    (hf : IsRegular f)
    (_ha : ∀ p : Ideal A, ∀ _ : p.IsPrime, ringKrullDim (A ⧸ p) = 1 → TwoLeDepthLocalization A p)
    (hb : 3 ≤ Module.depth A (maximalIdeal A) (A ⧸ Ideal.span {f})) :
    PicRestrictionInjective A f
```

**`Stacks.Algebraization.hasDualizingComplexOfRegularQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean#L121). The attribute's comment: “item (1): a Noetherian local ring that is a quotient of a regular ring has a dualizing complex”.

> A Noetherian local ring that is a quotient of a regular ring has a dualizing complex.

```lean
theorem hasDualizingComplexOfRegularQuotient (A : Type u) [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] : HasDualizingComplexOfRegularQuotient A
```

**`Stacks.Algebraization.twoLeDepthLocalization_of_four_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean#L168). The attribute's comment: “item (2): for a Noetherian local ring with `depth(A) ≥ 4`, every prime `𝔭` with `dim(A/𝔭) = 2` (indeed `≤ 2`) has `depth(A_𝔭) ≥ 2`”.

> Let `A` be a Noetherian local ring. If `depth(A) ≥ 4` and `𝔭` is a prime with
> `dim(A/𝔭) ≤ 2` then `depth(A_𝔭) ≥ 2`.

```lean
theorem twoLeDepthLocalization_of_four_le_depth (A : Type u) [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] (hA : 4 ≤ Module.depth A (IsLocalRing.maximalIdeal A) A) (p : Ideal A)
    [p.IsPrime] (hdim : ringKrullDim (A ⧸ p) ≤ 2) :
    TwoLeDepthLocalization A p
```

**`Stacks.Algebraization.three_le_depth_quotient_iff_four_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean#L205). The attribute's comment: “hypothesis (b): for `f ∈ 𝔪` a nonzerodivisor of a Noetherian local ring, `depth(A/fA) ≥ 3` is equivalent to `depth(A) ≥ 4`”.

> Let `(A, 𝔪)` be a Noetherian local ring and `f ∈ 𝔪` a nonzerodivisor. Then
> `depth(A/fA) ≥ 3` if and only if `depth(A) ≥ 4`.

```lean
theorem three_le_depth_quotient_iff_four_le_depth (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] (f : A) (hfm : f ∈ IsLocalRing.maximalIdeal A)
    (hf : IsSMulRegular A f) :
    3 ≤ Module.depth A (IsLocalRing.maximalIdeal A) (A ⧸ Ideal.span {f}) ↔
      4 ≤ Module.depth A (IsLocalRing.maximalIdeal A) A
```

**`Stacks.Algebraization.twoLeDepthLocalization_of_dim_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean#L224). The attribute's comment: “footnote: (b) implies (a) -- for `f ∈ 𝔪` a nonzerodivisor of a Noetherian local ring with `depth(A/fA) ≥ 3`, every prime `𝔭` with `dim(A/𝔭) = 1` has `depth(A_𝔭) ≥ 2`”.

> Let `(A, 𝔪)` be a Noetherian local ring. If `f ∈ 𝔪` is a nonzerodivisor with
> `depth(A/fA) ≥ 3`, then every prime `𝔭` with `dim(A/𝔭) = 1` has `depth(A_𝔭) ≥ 2`.

```lean
theorem twoLeDepthLocalization_of_dim_eq_one (A : Type u) [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] (f : A) (hfm : f ∈ IsLocalRing.maximalIdeal A) (hf : IsSMulRegular A f)
    (hb : 3 ≤ Module.depth A (IsLocalRing.maximalIdeal A) (A ⧸ Ideal.span {f})) (p : Ideal A)
    [p.IsPrime] (hdim : ringKrullDim (A ⧸ p) = 1) :
    TwoLeDepthLocalization A p
```

**`Stacks.Algebraization.kollarHypotheses_of_regularQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumPicardInjectivitySGA2.lean#L244). The attribute's comment: “the deduction from 0F2B: the hypotheses of the SGA2 lemma (a Noetherian local ring that is a quotient of a regular ring, `f ∈ 𝔪` a nonzerodivisor, `depth(A/fA) ≥ 3`) give the four hypotheses of 0F2B -- a dualizing complex by item (1), `f` a nonzerodivisor, `depth(A/fA) ≥ 2`, and `depth(A_𝔭) ≥ 2` for every prime `𝔭 ∋ f` with `dim(A/𝔭) = 2` by item (2)”.

> The hypotheses of the SGA2 lemma give the four hypotheses of Kollár's proposition
> [Stacks, Tag 0F2B]. Let `(A, 𝔪)` be a Noetherian local ring, `f ∈ 𝔪`, and assume `A` is a
> quotient of a regular ring `R`, that `f` is a nonzerodivisor and that `depth(A/fA) ≥ 3`. Then
>
> 1. `A` has a dualizing complex,
> 2. `f` is a nonzerodivisor,
> 3. `depth(A/fA) ≥ 2`, and
> 4. every prime `𝔭 ∋ f` with `dim(A/𝔭) = 2` has `depth(A_𝔭) ≥ 2`.

```lean
theorem kollarHypotheses_of_regularQuotient (A : Type u) [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] (f : A) (hfm : f ∈ IsLocalRing.maximalIdeal A) (R : Type u) [CommRing R]
    [IsRegularRing R] (π : R →+* A) (hπ : Function.Surjective π) (hf : IsSMulRegular A f)
    (hb : 3 ≤ Module.depth A (IsLocalRing.maximalIdeal A) (A ⧸ Ideal.span {f})) :
    (∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K) ∧
      IsSMulRegular A f ∧
      2 ≤ Module.depth A (IsLocalRing.maximalIdeal A) (A ⧸ Ideal.span {f}) ∧
      ∀ p : Ideal A, ∀ _ : p.IsPrime, f ∈ p → ringKrullDim (A ⧸ p) = 2 →
        TwoLeDepthLocalization A p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.26, Tag 0F29](https://stacks.math.columbia.edu/tag/0F29)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
