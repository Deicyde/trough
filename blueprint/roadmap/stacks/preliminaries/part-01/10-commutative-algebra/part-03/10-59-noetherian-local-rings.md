---
declaration: section
origin: cited
lean: IsIdealOfDefinition, chi_bounds_of_quotient_finiteLength, additivity_of_characteristic_and_hilbert_functions, chi_change_ideal_of_definition, Ideal.exists_eventually_length_quotient_smul_pow_eq_sum_choose_mul, Ideal.hilbertPolynomial, Ideal.exists_degree_eq_of_eventually_eval_eq_length_quotient_smul_pow, Ideal.hilbertSamuelDegree
statement: formalized
proof: formalized
---

# 10.59 Noetherian local rings

Section 10.59 of the Stacks Project, [Tag 00K4](https://stacks.math.columbia.edu/tag/00K4). 10 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07DU, a definition

[Tag 07DU](https://stacks.math.columbia.edu/tag/07DU) in the Stacks Project.

**`IsIdealOfDefinition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Defs.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Defs.lean#L161). References: EGA 0 (16.2.1); EGA 0 (7.1.2), “special case”; EGA III (4.3.13); EGA IV (21.13.12.1); EGA IV (6.1.3); SGA 1 I (2.1).

> An ideal `I` of a Noetherian local ring `(R, m)` is an *ideal of definition* if its
> radical is the maximal ideal, i.e. `√I = m`.

```lean
def IsIdealOfDefinition {R : Type*} [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (I : Ideal R) : Prop
```

## Tag 00K5, a lemma

[Tag 00K5](https://stacks.math.columbia.edu/tag/00K5) in the Stacks Project.

**`chi_bounds_of_quotient_finiteLength`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Function.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Function.lean#L182).

> Let `(R, m, k)` be a Noetherian local ring, `I ⊆ R` an ideal of definition, and
> `M' ⊆ M` finite `R`-modules with `M / M'` of finite length. Then there are
> constants `c₁, c₂ ∈ ℕ` such that for all `n ≥ c₂`,
> `c₁ + χ_{I,M'}(n - c₂) ≤ χ_{I,M}(n) ≤ c₁ + χ_{I,M'}(n)`.

```lean
theorem chi_bounds_of_quotient_finiteLength
    {R : Type*} [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (I : Ideal R) (hI : IsIdealOfDefinition I)
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (M' : Submodule R M) (hlen : Module.length R (M ⧸ M') < ⊤) :
    ∃ c₁ c₂ : ℕ, ∀ n : ℕ, c₂ ≤ n →
      (c₁ : ℕ∞) + chi I M' (n - c₂) ≤ chi I M n ∧
      chi I M n ≤ (c₁ : ℕ∞) + chi I M' n
```

## Tag 00K6, a lemma

[Tag 00K6](https://stacks.math.columbia.edu/tag/00K6) in the Stacks Project.

**`additivity_of_characteristic_and_hilbert_functions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Function.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Function.lean#L404).

> Given a short exact sequence `0 → M' → M → M'' → 0` of finite `R`-modules over a
> Noetherian local ring `(R, m)` and an ideal `I` with `√I = m`, there are a submodule
> `N ⊆ M'` of finite colength `l = length_R (M'/N)` and an integer `c ≥ 0` such that for
> all `n ≥ c`
>   `χ_{I,M}(n) = χ_{I,M''}(n) + χ_{I,N}(n - c) + l`  and
>   `φ_{I,M}(n) = φ_{I,M''}(n) + φ_{I,N}(n - c)`.

```lean
theorem additivity_of_characteristic_and_hilbert_functions
    (R : Type*) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (I : Ideal R) (hI : I.radical = IsLocalRing.maximalIdeal R)
    (M' M M'' : Type*)
    [AddCommGroup M'] [Module R M'] [Module.Finite R M']
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    [AddCommGroup M''] [Module R M''] [Module.Finite R M'']
    (f : M' →ₗ[R] M) (g : M →ₗ[R] M'')
    (hf : Function.Injective f) (hg : Function.Surjective g)
    (hfg : Function.Exact f g) :
    ∃ (N : Submodule R M') (c : ℕ) (l : ℕ),
      Module.length R (M' ⧸ N) = (l : ℕ∞) ∧
      (∀ n ≥ c, charFn R I M n = charFn R I M'' n + charFn R I N (n - c) + (l : ℕ∞)) ∧
      (∀ n ≥ c, hilbertFn R I M n = hilbertFn R I M'' n + hilbertFn R I N (n - c))
```

## Tag 00K7, a lemma

[Tag 00K7](https://stacks.math.columbia.edu/tag/00K7) in the Stacks Project.

**`chi_change_ideal_of_definition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Defs.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Defs.lean#L124).

> Let `(R, m)` be a Noetherian local ring, let `I, I'` be two ideals of definition
> of `R`, and let `M` be a finite `R`-module. Then there exists a positive integer
> `a` such that
>   `χ_{I,M}(n) ≤ χ_{I',M}(a·n)` for all `n ≥ 1`.

```lean
theorem chi_change_ideal_of_definition
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (I I' : Ideal R) (hI : IsIdealOfDefinition' I) (hI' : IsIdealOfDefinition' I') :
    ∃ a : ℕ, 0 < a ∧ ∀ n : ℕ, 1 ≤ n → hilbertSamuel_chi I M n ≤ hilbertSamuel_chi I' M (a * n)
```

## Tag 00K8, a proposition

[Tag 00K8](https://stacks.math.columbia.edu/tag/00K8) in the Stacks Project.

**`Ideal.exists_eventually_length_quotient_smul_pow_eq_sum_choose_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertFunction/Numerical.lean, line 1207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertFunction/Numerical.lean#L1207). References: EGA 0 (16.2.1), “local case”.

> **Stacks 00K8.** Let `R` be a Noetherian local ring, let `I ⊆ R` be an ideal of definition
> (`I.radical` is the maximal ideal of `R`) and let `M` be a finite `R`-module. Then the Hilbert
> function `n ↦ length_R (I ^ n • M / I ^ (n + 1) • M)` and the function
> `n ↦ length_R (M / I ^ (n + 1) • M)` are numerical polynomials: each takes finite values which,
> for all `n ≫ 0`, are given by a `ℤ`-linear combination of the binomial coefficients
> `n choose 0, …, n choose r`.

```lean
public theorem Ideal.exists_eventually_length_quotient_smul_pow_eq_sum_choose_mul
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] (I : Ideal R)
    (hI : I.radical = IsLocalRing.maximalIdeal R)
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    ∃ (r : ℕ) (a b : ℕ → ℤ), ∀ᶠ n : ℕ in Filter.atTop,
      (∃ p : ℕ, Module.length R (↥(I ^ n • (⊤ : Submodule R M)) ⧸
            (I ^ (n + 1) • (⊤ : Submodule R M)).submoduleOf (I ^ n • ⊤)) = p ∧
          (p : ℤ) = ∑ i ∈ Finset.range (r + 1), (n.choose i : ℤ) * a i) ∧
      (∃ q : ℕ, Module.length R (M ⧸ (I ^ (n + 1) • (⊤ : Submodule R M))) = q ∧
          (q : ℤ) = ∑ i ∈ Finset.range (r + 1), (n.choose i : ℤ) * b i)
```

## Tag 09CA, a definition

[Tag 09CA](https://stacks.math.columbia.edu/tag/09CA) in the Stacks Project.

**`Ideal.hilbertPolynomial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertFunction/Defs.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertFunction/Defs.lean#L132). The attribute's comment: “Stated relative to an ideal `I ⊆ R`, as the rest of the section is (Tags 00K8, 00K9, 00KA); the Hilbert polynomial of Definition 09CA is the case `I = IsLocalRing.maximalIdeal R`, for `R` Noetherian local and `M` finite, where Proposition 00K8 makes the characterising property satisfiable. The property is what the definition consumes, and it determines the polynomial uniquely; the value is `0` where nothing has it.”.

> **Stacks 09CA.** The *Hilbert polynomial* of an `R`-module `M` relative to an ideal `I ⊆ R`:
> the polynomial `P ∈ ℚ[t]` such that `P(n) = φ_{I,M}(n) = length_R (I ^ n M / I ^ (n + 1) M)` for
> all `n ≫ 0`. At most one polynomial has this property, so this is a definition of that element;
> the value is `0` in the case that none has it. For `R` Noetherian local, `M` finite and `I` an
> ideal of definition — in particular for `I = m`, the Hilbert polynomial of `M` over `R` — such a
> `P` exists by Proposition 00K8.

```lean
public noncomputable def Ideal.hilbertPolynomial {R : Type*} [CommRing R] (I : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] : ℚ[X]
```

## Tag 00K9, a lemma

[Tag 00K9](https://stacks.math.columbia.edu/tag/00K9) in the Stacks Project.

**`Ideal.exists_degree_eq_of_eventually_eval_eq_length_quotient_smul_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/DegreeInvariance.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/DegreeInvariance.lean#L289). The attribute's comment: “The degree of a numerical polynomial is spelled as the degree of any rational polynomial computing it at all large `n`, and independence of `I` as the two degrees being quantified outside the ideal of definition. Part (1) of the tag is the first conjunct, part (2) the second.”. References: EGA 0 (16.2.3), “special case”.

> **Stacks 00K9.** Let `R` be a Noetherian local ring and let `M` be a finite `R`-module. Then
> there are `d e : WithBot ℕ`, depending on `R` and `M` only, such that for every ideal of
> definition `I ⊆ R` (that is, `I.radical = m`): every polynomial `P ∈ ℚ[t]` agreeing with the
> Hilbert function `φ_{I,M}(n) = length_R (I ^ n M / I ^ (n + 1) M)` for all `n ≫ 0` has degree
> `d`, and every polynomial `P ∈ ℚ[t]` agreeing with `χ_{I,M}(n) = length_R (M / I ^ (n + 1) M)`
> for all `n ≫ 0` has degree `e`. That is, the degrees of the numerical polynomials `φ_{I,M}` and
> `χ_{I,M}` are independent of the ideal of definition `I`.

```lean
public theorem Ideal.exists_degree_eq_of_eventually_eval_eq_length_quotient_smul_pow
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    ∃ d e : WithBot ℕ, ∀ I : Ideal R, I.radical = maximalIdeal R → ∀ P : ℚ[X],
      ((∀ᶠ n : ℕ in atTop, ∃ p : ℕ,
            Module.length R (↥(I ^ n • (⊤ : Submodule R M)) ⧸
              (I ^ (n + 1) • (⊤ : Submodule R M)).submoduleOf (I ^ n • ⊤)) = p ∧
            P.eval (n : ℚ) = (p : ℚ)) → P.degree = d) ∧
      ((∀ᶠ n : ℕ in atTop, ∃ q : ℕ,
            Module.length R (M ⧸ (I ^ (n + 1) • (⊤ : Submodule R M))) = q ∧
            P.eval (n : ℚ) = (q : ℚ)) → P.degree = e)
```

## Tag 00KA, a definition

[Tag 00KA](https://stacks.math.columbia.edu/tag/00KA) in the Stacks Project.

**`Ideal.hilbertSamuelDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Defs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Defs.lean#L79). The attribute's comment: “Definition 00KA is the case `I = maximalIdeal R`, spelled `Module.hilbertSamuelDegree`. The definition is stated for an arbitrary ideal because that is the generality of the surrounding section, and because Lemma 00K9(2) is the assertion that this value is the same for all ideals of definition.”. References: EGA 0 (16.2.3).

> The degree, an element of `{-∞, 0, 1, 2, …} = WithBot ℕ`, of the numerical polynomial
> `χ_{I,M}(n) = length_R (M / I ^ (n + 1) M)`: the degree of a polynomial `P ∈ ℚ[t]` with
> `P(n) = χ_{I,M}(n)` for all `n ≫ 0`, and `-∞` if there is no such polynomial.

```lean
public noncomputable def Ideal.hilbertSamuelDegree {R : Type*} [CommRing R] (I : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] : WithBot ℕ
```

**`Module.hilbertSamuelDegree`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Defs.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Defs.lean#L93). The attribute's comment: “The `d(M)` of the definition. Case (1) is not a separate branch: for `M = 0` the polynomial computing `χ_M` is `0`, whose degree is `-∞ = ⊥`, and conversely a computing polynomial of degree `-∞` forces `M = m ^ n M` for `n ≫ 0`, hence `M = 0` by Nakayama. See the module docstring.”. References: EGA 0 (16.2.3), “special case”.

> The invariant `d(M) ∈ {-∞, 0, 1, 2, …} = WithBot ℕ` of a module `M` over a local ring
> `(R, m)`: the degree of the numerical polynomial `χ_M(n) = length_R (M / m ^ (n + 1) M)`, that is
> `Ideal.hilbertSamuelDegree` at the maximal ideal.

```lean
public noncomputable abbrev Module.hilbertSamuelDegree (R : Type*) [CommRing R] [IsLocalRing R]
    (M : Type*) [AddCommGroup M] [Module R M] : WithBot ℕ
```

## Tag 00KB, a lemma

[Tag 00KB](https://stacks.math.columbia.edu/tag/00KB) in the Stacks Project.

**`HilbertSamuel.degree_sub_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Function.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Function.lean#L787). References: EGA 0 (16.2.2.2), “special case”.

> Let `(R, m)` be a Noetherian local ring, `I ⊆ R` an ideal of definition, and `M`
> a finite `R`-module which does not have finite length.  Let `M' ⊆ M` be a
> submodule with finite colength, and let `χ_{I,M}`, `χ_{I,M'} ∈ Q[t]` be the
> Hilbert–Samuel polynomials of `M` and `M'`.  Then the difference
> `χ_{I,M} - χ_{I,M'}` has degree strictly less than the degree of each of the two
> Hilbert–Samuel polynomials.

```lean
theorem degree_sub_lt
    [IsNoetherianRing R] [IsLocalRing R]
    (I : Ideal R) (hI : IsIdealOfDefinition I)
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (hM : ¬ HasFiniteLength R M)
    (M' : Submodule R M) (hM' : HasFiniteColength M')
    (χM χM' : ℚ[X])
    (hχM : IsHilbertSamuelPoly I M χM)
    (hχM' : IsHilbertSamuelPoly I (↥M') χM') :
    (χM - χM').degree < χM.degree ∧ (χM - χM').degree < χM'.degree
```

## Tag 00KC, a lemma

[Tag 00KC](https://stacks.math.columbia.edu/tag/00KC) in the Stacks Project.

**`Ideal.max_degree_eq_degree_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/ShortExact.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/ShortExact.lean#L549). The attribute's comment: “The first conjunct is parts (1) and (2) of the tag, for polynomials computing the three Hilbert–Samuel functions as in Tags 00K8 and 00K9, so `χ_{I,M} - χ_{I,M''} - χ_{I,M'}` is `P - P'' - P'`; that this is again a numerical polynomial is inherited from the hypotheses on the three polynomials, and the degree bound is the content. The second conjunct is part (2) for the invariant of Definition 00KA, and part (3) of the tag is its case `I = maximalIdeal R`. See the module docstring.”. References: EGA 0 (16.2.2.2), “(1) deg bound, (2)”.

> **Stacks 00KC.** Let `R` be a Noetherian local ring, let `I ⊆ R` be an ideal of definition
> (`I.radical` is the maximal ideal of `R`) and let `0 → M' → M → M'' → 0` be a short exact
> sequence of finite `R`-modules, given by `f : M' →ₗ[R] M` injective, `g : M →ₗ[R] M''`
> surjective and `Function.Exact f g`. Then
>
> 1. if `M'` does not have finite length, then `χ_{I,M} - χ_{I,M''} - χ_{I,M'}` is a numerical
>    polynomial of degree `<` the degree of `χ_{I,M'}`,
> 2. `max {deg χ_{I,M'}, deg χ_{I,M''}} = deg χ_{I,M}`, and
> 3. `max {d(M'), d(M'')} = d(M)`, for the invariant `d(-)` of Definition 00KA — the case
>    `I = m` of the last conjunct, since `d(N) = (maximalIdeal R).hilbertSamuelDegree N`.
>
> Here `P'`, `P`, `P''` are the numerical polynomials `χ_{I,M'}`, `χ_{I,M}`, `χ_{I,M''}`, that is,
> the polynomials with `P'(n) = length_R (M' / I ^ (n + 1) M')` for all `n ≫ 0` and likewise for
> `M` and `M''`, and `Ideal.hilbertSamuelDegree I N` is the degree of `χ_{I,N}`.

```lean
public theorem Ideal.max_degree_eq_degree_of_exact
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (I : Ideal R) (hI : I.radical = maximalIdeal R)
    {M' M M'' : Type*} [AddCommGroup M'] [Module R M'] [Module.Finite R M']
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    [AddCommGroup M''] [Module R M''] [Module.Finite R M'']
    {f : M' →ₗ[R] M} {g : M →ₗ[R] M''} (hfg : Function.Exact f g)
    (hf : Function.Injective f) (hg : Function.Surjective g) :
    (∀ P' P P'' : ℚ[X],
      (∀ᶠ n : ℕ in atTop, ∃ p : ℕ,
          Module.length R (M' ⧸ (I ^ (n + 1) • (⊤ : Submodule R M'))) = p ∧
            P'.eval (n : ℚ) = (p : ℚ)) →
        (∀ᶠ n : ℕ in atTop, ∃ p : ℕ,
          Module.length R (M ⧸ (I ^ (n + 1) • (⊤ : Submodule R M))) = p ∧
            P.eval (n : ℚ) = (p : ℚ)) →
        (∀ᶠ n : ℕ in atTop, ∃ p : ℕ,
          Module.length R (M'' ⧸ (I ^ (n + 1) • (⊤ : Submodule R M''))) = p ∧
            P''.eval (n : ℚ) = (p : ℚ)) →
        (¬ IsFiniteLength R M' → (P - P'' - P').degree < P'.degree) ∧
          max P'.degree P''.degree = P.degree) ∧
      max (I.hilbertSamuelDegree M') (I.hilbertSamuelDegree M'') =
        I.hilbertSamuelDegree M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.59, Tag 00K4](https://stacks.math.columbia.edu/tag/00K4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
