---
declaration: section
origin: cited
lean: Ideal.hilbertSamuelMultiplicity, Ideal.hilbertSamuelMultiplicityOfModule, Ideal.hilbertSamuelMultiplicity_additive_of_exact, Ideal.hilbertSamuelMultiplicity_eq_finsum_localizedLength_mul, Polynomial.fwdDiff_iter_degree_eq_factorial, fwdDiff_iter_eq_sum_shift, Ideal.hilbertSamuelMultiplicity_eq_alternatingSum_koszulHomology_length, Ideal.idealOfDefinition_support_length_tfae
statement: formalized
proof: formalized
---

# 43.15 Algebraic multiplicities

Section 43.15 of the Stacks Project, [Tag 0AZU](https://stacks.math.columbia.edu/tag/0AZU). 6 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AZV, a definition

[Tag 0AZV](https://stacks.math.columbia.edu/tag/0AZV) in the Stacks Project.

**`Ideal.hilbertSamuelMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Defs.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Defs.lean#L52). The attribute's comment: “the multiplicity `e_I(M, d)`”. References: SGA 7 X (2.6).

> The Hilbert–Samuel multiplicity `e_I(M, d)`: `d !` times the coefficient of degree `d`
> of the rational polynomial eventually computing `length_R (M / I ^ (n + 1) M)`.
>
> When `R` is Noetherian local, `M` is finite, `I` is an ideal of definition, and `d` is at
> least the dimension of the support of `M`, this is zero if the inequality is strict and is
> `d !` times the leading coefficient otherwise.

```lean
public noncomputable def Ideal.hilbertSamuelMultiplicity {R : Type*} [CommRing R]
    (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M] (d : ℕ) : ℚ
```

**`Ideal.hilbertSamuelMultiplicityOfModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Defs.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Defs.lean#L68). The attribute's comment: “the multiplicity `e_I(M)`”. References: SGA 7 X (2.6).

> The multiplicity `e_I(M)` of `M` for `I`, obtained by taking the coefficient in the
> Hilbert–Samuel degree of `M`. For a finite module over a Noetherian local ring that degree is the
> dimension of the support (`Module.hilbertSamuelDegree_eq_supportDim`), so this is
> `e_I(M, dim(Supp(M)))`. The zero module, of degree `-∞`, is read in degree zero, where its
> multiplicity is zero.

```lean
public noncomputable abbrev Ideal.hilbertSamuelMultiplicityOfModule {R : Type*} [CommRing R]
    [IsLocalRing R] (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M] : ℚ
```

## Tag 0AZW, a lemma

[Tag 0AZW](https://stacks.math.columbia.edu/tag/0AZW) in the Stacks Project.

**`Ideal.hilbertSamuelMultiplicity_additive_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Additivity.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Additivity.lean#L155).

> Hilbert–Samuel multiplicity in degree `d` is additive in a short exact sequence of
> finite modules, provided `d` is at least the dimension of the support of the middle term.

```lean
theorem hilbertSamuelMultiplicity_additive_of_exact
    {R M' M M'' : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M'] [Module R M'] [Module.Finite R M']
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    [AddCommGroup M''] [Module R M''] [Module.Finite R M'']
    (I : Ideal R) (hI : IsIdealOfDefinition I) (d : ℕ)
    {f : M' →ₗ[R] M} {g : M →ₗ[R] M''}
    (hf : Function.Injective f) (hfg : Function.Exact f g) (hg : Function.Surjective g)
    (hd : Module.supportDim R M ≤ (d : WithBot ℕ∞)) :
    I.hilbertSamuelMultiplicity M d =
      I.hilbertSamuelMultiplicity M' d + I.hilbertSamuelMultiplicity M'' d
```

## Tag 0AZX, a lemma

[Tag 0AZX](https://stacks.math.columbia.edu/tag/0AZX) in the Stacks Project.

**`Ideal.hilbertSamuelMultiplicity_eq_finsum_localizedLength_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/PrimeFiltration.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/PrimeFiltration.lean#L308).

> Let `I` be an ideal of definition in a Noetherian local ring `R`, and let `M` be a
> finite `R`-module. In every degree at least the dimension of the support of `M`, its
> Hilbert–Samuel multiplicity is the sum, over primes `p` with `dim(R / p)` equal to that
> degree, of the multiplicity of `R / p` weighted by `length_{R_p}(M_p)`.

```lean
theorem hilbertSamuelMultiplicity_eq_finsum_localizedLength_mul
    {R M : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (hI : IsIdealOfDefinition I) (d : ℕ)
    (hd : Module.supportDim R M ≤ d) :
    I.hilbertSamuelMultiplicity M d =
      ∑ᶠ p : {p : PrimeSpectrum R // ringKrullDim (R ⧸ p.asIdeal) = d},
        ((Module.length (Localization.AtPrime p.1.asIdeal)
          (LocalizedModule p.1.asIdeal.primeCompl M)).toNat : ℚ) *
          I.hilbertSamuelMultiplicity (R ⧸ p.1.asIdeal) d
```

## Tag 0AZY, a lemma

[Tag 0AZY](https://stacks.math.columbia.edu/tag/0AZY) in the Stacks Project.

Declarations registered for the tag:

- [`Polynomial.fwdDiff_iter_degree_eq_factorial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.fwdDiff_iter_degree_eq_factorial#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch43.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch43.lean#L16) (StacksFrontier): “the `r`-th forward difference of `P` is `r! a`”.
- [`fwdDiff_iter_eq_sum_shift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=fwdDiff_iter_eq_sum_shift#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch43.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch43.lean#L18) (StacksFrontier): “the `r`-th forward difference as the alternating sum, at `t - r`”.

## Tag 0AZZ, a theorem

[Tag 0AZZ](https://stacks.math.columbia.edu/tag/0AZZ) in the Stacks Project.

**`Ideal.hilbertSamuelMultiplicity_eq_alternatingSum_koszulHomology_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/KoszulEuler.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/KoszulEuler.lean#L603).

> If an ideal of definition `I` is generated by `f : Fin r → A`, then its Hilbert–Samuel
> multiplicity in degree `r` on a finite module is the Euler characteristic of the homology of
> the Koszul complex on `f` with coefficients in that module.

```lean
theorem hilbertSamuelMultiplicity_eq_alternatingSum_koszulHomology_length
    {A : Type*} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (I : Ideal A) (r : ℕ) (f : Fin r → A) (M : Type*)
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    (hI : IsIdealOfDefinition I) (hf : I = Ideal.span (Set.range f)) :
    I.hilbertSamuelMultiplicity M r =
      ∑ i : Fin (r + 1), (-1 : ℚ) ^ (i : ℕ) *
        ((Module.length A ((Koszul.seqComplexTensor f M).homology (i : ℕ))).toNat : ℚ)
```

## Tag 0B00, a remark

[Tag 0B00](https://stacks.math.columbia.edu/tag/0B00) in the Stacks Project.

**`Ideal.idealOfDefinition_support_length_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/FiniteLengthConditions.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/FiniteLengthConditions.lean#L97). The attribute's comment: “finite\_length\_conditions”.

> **Stacks Project, Tag 0B00, finite-length conditions.** Let `M` be a finite module over a
> Noetherian local ring and `I` an ideal. If `M / IM` is nonzero, then the following are
> equivalent: `I + Ann(M)` is an ideal of definition; the image of `I` in `R / Ann(M)` is an
> ideal of definition; the support of `M / IM` is contained in the closed point; that support
> has dimension at most zero; and `M / IM` has finite length.

```lean
theorem idealOfDefinition_support_length_tfae
    {R M : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R) (hMI : Nontrivial (M ⧸ I • (⊤ : Submodule R M))) :
    letI := hMI
    letI : Nontrivial M := (I • (⊤ : Submodule R M)).mkQ_surjective.nontrivial
    letI : Nontrivial (R ⧸ Module.annihilator R M) :=
      Ideal.Quotient.nontrivial_iff.mpr
        (mt Module.annihilator_eq_top_iff.mp (not_subsingleton M))
    letI : IsLocalRing (R ⧸ Module.annihilator R M) :=
      IsLocalRing.of_surjective' (Ideal.Quotient.mk (Module.annihilator R M))
        Ideal.Quotient.mk_surjective
    List.TFAE [
      IsIdealOfDefinition (I + Module.annihilator R M),
      IsIdealOfDefinition
        (Ideal.map (Ideal.Quotient.mk (Module.annihilator R M)) I),
      Module.support R (M ⧸ I • (⊤ : Submodule R M)) ⊆ {IsLocalRing.closedPoint R},
      Module.supportDim R (M ⧸ I • (⊤ : Submodule R M)) ≤ 0,
      Module.length R (M ⧸ I • (⊤ : Submodule R M)) < ⊤]
```

**`Ideal.generalizedHilbertFunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertFunction.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertFunction.lean#L143). The attribute's comment: “generalized\_hilbert\_function”.

> The generalized Hilbert function `χ_{I,M}(n) = length_R(M / I^n M)`.

```lean
noncomputable def generalizedHilbertFunction
    {R : Type*} [CommRing R] (I : Ideal R) (M : Type*)
    [AddCommGroup M] [Module R M] (n : ℕ) : ℕ∞
```

**`Ideal.generalizedHilbertFunction_lt_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertFunction.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertFunction.lean#L150). The attribute's comment: “generalized\_hilbert\_function”.

> If `M / IM` has finite length, then so does `M / I^n M` for every `n`.

```lean
theorem generalizedHilbertFunction_lt_top
    {R M : Type*} [CommRing R] [IsNoetherianRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I : Ideal R)
    (hIM : Module.length R (M ⧸ I • (⊤ : Submodule R M)) < ⊤)
    (n : ℕ) : Ideal.generalizedHilbertFunction I M n < ⊤
```

**`Ideal.generalizedHilbertFunction_eq_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertFunction.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertFunction.lean#L162). The attribute's comment: “generalized\_hilbert\_function”.

> The length of `M / I^n M` is the sum of the lengths of its successive `I`-adic layers,
> including the empty sum when `n = 0`.

```lean
theorem generalizedHilbertFunction_eq_sum
    {R : Type*} [CommRing R] (I : Ideal R) (M : Type*)
    [AddCommGroup M] [Module R M] (n : ℕ) :
    Ideal.generalizedHilbertFunction I M n =
      ∑ p ∈ Finset.range n,
        Module.length R
          (↥(I ^ p • (⊤ : Submodule R M)) ⧸
            (I ^ (p + 1) • (⊤ : Submodule R M)).submoduleOf
              (I ^ p • (⊤ : Submodule R M)))
```

**`Ideal.exists_computesGeneralizedHilbertPoly_degree_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertPolynomial.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertPolynomial.lean#L78). The attribute's comment: “eventual\_polynomiality”. References: EGA 0 (16.2.1), “partial”.

> **Stacks Project, Tag 0B00, eventual polynomiality.** Let `M` be a finite module over a
> Noetherian local ring and let `I` be an ideal with `M / IM` of finite length. For every
> `d ≥ dim(Supp(M))` there is a rational polynomial of degree at most `d` which computes
> `χ_{I, M}(n) = length(M / I ^ n M)` for all large `n`.

```lean
theorem exists_computesGeneralizedHilbertPoly_degree_le
    {A M : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M] (I : Ideal A)
    (hI : Module.length A (M ⧸ I • (⊤ : Submodule A M)) < ⊤)
    {d : ℕ} (hd : Module.supportDim A M ≤ (d : WithBot ℕ∞)) :
    ∃ P : ℚ[X], I.ComputesGeneralizedHilbertPoly M P ∧ P.degree ≤ (d : WithBot ℕ)
```

**`Ideal.exists_degree_lt_generalizedHilbertFunction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertPolynomial.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedHilbertPolynomial.lean#L109). The attribute's comment: “asymptotics”.

> **Stacks Project, Tag 0B00, asymptotics of the generalized Hilbert function.** Let `M` be
> a finite module over a Noetherian local ring and let `I` be an ideal with `M / IM` of finite
> length. For every `d ≥ dim(Supp(M))` there are lower order terms, a rational polynomial of
> degree `< d`, such that for all large `n` the length `χ_{I, M}(n) = length(M / I ^ n M)` is
> finite and equals `e_I(M, d) * n ^ d / d !` plus those terms.

```lean
theorem exists_degree_lt_generalizedHilbertFunction_eq
    {A M : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M] (I : Ideal A)
    (hI : Module.length A (M ⧸ I • (⊤ : Submodule A M)) < ⊤)
    {d : ℕ} (hd : Module.supportDim A M ≤ (d : WithBot ℕ∞)) :
    ∃ Q : ℚ[X], Q.degree < (d : WithBot ℕ) ∧
      ∀ᶠ n : ℕ in atTop, ∃ p : ℕ,
        I.generalizedHilbertFunction M n = (p : ℕ∞) ∧
          (p : ℚ) = I.generalizedHilbertSamuelMultiplicity M d * (n : ℚ) ^ d
            / (d.factorial : ℚ) + Q.eval (n : ℚ)
```

**`Ideal.generalizedHilbertSamuelMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedMultiplicity.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/GeneralizedMultiplicity.lean#L45). The attribute's comment: “generalized\_multiplicity”. References: SGA 7 X (2.6).

> The generalized Hilbert–Samuel multiplicity `e_I(M, d)`: `d !` times the coefficient of
> degree `d` in the rational polynomial eventually computing `length_R (M / I ^ n M)`.
>
> For a finite module over a Noetherian local ring, when `M / I M` is nonzero of finite length
> and `d` is at least the dimension of the support of `M`, this is the generalized multiplicity
> of Tag 0B00.

```lean
noncomputable def Ideal.generalizedHilbertSamuelMultiplicity {R : Type*} [CommRing R]
    (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M] (d : ℕ) : ℚ
```

**`Ideal.generalizedHilbertFunction_add_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Invariance.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Invariance.lean#L44). The attribute's comment: “invariance\_under\_adding\_annihilator”.

> Adding the annihilator of `M` to `I` does not change the length of `M / I^n M`.

```lean
theorem generalizedHilbertFunction_add_annihilator
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (I : Ideal R) (n : ℕ) :
    Ideal.generalizedHilbertFunction (I + Module.annihilator R M) M n =
      Ideal.generalizedHilbertFunction I M n
```

**`Ideal.generalizedHilbertFunction_add_annihilator_eq_map_quotientAnnihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Invariance.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Invariance.lean#L55). The attribute's comment: “invariance\_under\_quotient\_by\_annihilator”.

> The generalized Hilbert function is unchanged by passing from `I + Ann(M)` over `R` to the
> image of `I` over `R / Ann(M)`.

```lean
theorem generalizedHilbertFunction_add_annihilator_eq_map_quotientAnnihilator
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (I : Ideal R) (n : ℕ) :
    letI : Module (R ⧸ Module.annihilator R M) M := Module.quotientAnnihilator
    Ideal.generalizedHilbertFunction (I + Module.annihilator R M) M n =
      Ideal.generalizedHilbertFunction
        (Ideal.map (Ideal.Quotient.mk (Module.annihilator R M)) I) M n
```

**`Ideal.generalizedHilbertSamuelMultiplicity_add_annihilator_eq_map_quotientAnnihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Invariance.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/Invariance.lean#L77). The attribute's comment: “invariance\_under\_quotient\_by\_annihilator”.

> Generalized Hilbert–Samuel multiplicities are unchanged by passing to the quotient ring by
> the annihilator of the module.

```lean
theorem generalizedHilbertSamuelMultiplicity_add_annihilator_eq_map_quotientAnnihilator
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (I : Ideal R) (d : ℕ) :
    letI : Module (R ⧸ Module.annihilator R M) M := Module.quotientAnnihilator
    Ideal.generalizedHilbertSamuelMultiplicity (I + Module.annihilator R M) M d =
      Ideal.generalizedHilbertSamuelMultiplicity
        (Ideal.map (Ideal.Quotient.mk (Module.annihilator R M)) I) M d
```

**`Ideal.add_annihilator_pow_smul_top`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/QuotientAnnihilator.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/QuotientAnnihilator.lean#L40). The attribute's comment: “quotient\_power\_equalities”.

> **Stacks Project, Tag 0B00, quotient power equalities.** Adjoining the annihilator of a
> module to an ideal does not change the submodule generated by any power of that ideal.

```lean
lemma add_annihilator_pow_smul_top
    {R M : Type*} [CommSemiring R] [AddCommMonoid M] [Module R M]
    (I : Ideal R) (n : ℕ) :
    (I + Module.annihilator R M) ^ n • (⊤ : Submodule R M) =
      I ^ n • (⊤ : Submodule R M)
```

**`Ideal.map_quotientAnnihilator_pow_smul_top`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/QuotientAnnihilator.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Intersection/AlgebraicMultiplicities/QuotientAnnihilator.lean#L61). The attribute's comment: “quotient\_power\_equalities”.

> **Stacks Project, Tag 0B00, quotient power equalities.** If `M` is regarded as a module
> over `R / Ann(M)`, the image of a power of `I` generates the same submodule as that power of
> `I` does over `R`.

```lean
lemma map_quotientAnnihilator_pow_smul_top
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (I : Ideal R) (n : ℕ) :
    letI : Module (R ⧸ Module.annihilator R M) M := Module.quotientAnnihilator
    ((Ideal.map (Ideal.Quotient.mk (Module.annihilator R M)) I) ^ n •
        (⊤ : Submodule (R ⧸ Module.annihilator R M) M)).restrictScalars R =
      I ^ n • (⊤ : Submodule R M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.15, Tag 0AZU](https://stacks.math.columbia.edu/tag/0AZU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
