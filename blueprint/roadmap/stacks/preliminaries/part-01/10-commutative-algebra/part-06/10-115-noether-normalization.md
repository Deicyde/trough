---
declaration: section
origin: cited
lean: eventuallyRapidlyDecreasing_snoc_dotProduct_eq_iff, eventuallyRapidlyDecreasing_dotProduct_eq_iff, eventuallyRapid_subst_constant_leadingCoeff_of_nonconstant, Stacks.RingTheory.NagataNormalization.exists_isIntegral_aeval, exists_finite_inj_aeval_ringKrullDim_eq_of_adjoin_eq_top, ringKrullDim_eq_of_aeval_injective_of_finite, noether_normalization_at_point_topologicalKrullDimAt, MvPolynomial.exists_finite_comap_eq_span_X_image_of_trdeg_eq
statement: formalized
proof: formalized
---

# 10.115 Noether normalization

Section 10.115 of the Stacks Project, [Tag 00OW](https://stacks.math.columbia.edu/tag/00OW). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 051M, a lemma

[Tag 051M](https://stacks.math.columbia.edu/tag/051M) in the Stacks Project.

**`eventuallyRapidlyDecreasing_snoc_dotProduct_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization/Basic.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization/Basic.lean#L276). The attribute's comment: “the last exponent `e_n` may be any positive integer; `N` need not be nonempty”.

> Stacks 051M with an arbitrary positive last exponent: for a finite set `N` of
> multi-indices in `ℕ^{n+1}` and any `c > 0`, for `e_1 ≫ ⋯ ≫ e_n ≫ e_{n+1} = c` the dot
> product with `e = (e_1, …, e_n, c)` separates `N`.

```lean
theorem eventuallyRapidlyDecreasing_snoc_dotProduct_eq_iff {n : ℕ}
    (N : Finset (Fin (n + 1) → ℕ)) {c : ℕ} (hc : 0 < c) :
    EventuallyRapidlyDecreasing n fun e => ∀ ν ∈ N, ∀ ν' ∈ N,
      ((Fin.snoc e c : Fin (n + 1) → ℕ) ⬝ᵥ ν = (Fin.snoc e c : Fin (n + 1) → ℕ) ⬝ᵥ ν' ↔
        ν = ν')
```

**`eventuallyRapidlyDecreasing_dotProduct_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization/Basic.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization/Basic.lean#L338). The attribute's comment: “nested quantifier `e_1 ≫ ⋯ ≫ e_n` as `EventuallyRapidlyDecreasing`; `N` need not be nonempty”.

> Stacks 051M: for a finite set `N` of multi-indices in `ℕ^n`, for all exponent vectors
> `e = (e_1, …, e_n)` with `e_1 ≫ e_2 ≫ ⋯ ≫ e_n` (in the nested sense of
> `EventuallyRapidlyDecreasing`) we have `e · ν = e · ν' ↔ ν = ν'` for all `ν, ν' ∈ N`.

```lean
theorem eventuallyRapidlyDecreasing_dotProduct_eq_iff {n : ℕ} (N : Finset (Fin n → ℕ)) :
    EventuallyRapidlyDecreasing n fun e => ∀ ν ∈ N, ∀ ν' ∈ N, (e ⬝ᵥ ν = e ⬝ᵥ ν' ↔ ν = ν')
```

## Tag 051N, a lemma

[Tag 051N](https://stacks.math.columbia.edu/tag/051N) in the Stacks Project.

**`eventuallyRapid_subst_constant_leadingCoeff_of_nonconstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization/Basic.lean, line 808](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization/Basic.lean#L808). The attribute's comment: “for all exponents e₁ ≫ ⋯ ≫ e\_\{N-1} ≫ e\_N = 1 in the nested sense of `EventuallyRapid`; X 0 is the distinguished variable x\_N”.

> **Stacks 051N.** Let `g ∈ R[x_1, …, x_N]` be nonconstant (here `N = n + 1`, the
> variable `X 0` plays the role of the distinguished variable `x_N`, and `X i` for `1 ≤ i ≤ n`
> plays the role of `x_{N-i}`). Then for all exponents `e_1 ≫ e_2 ≫ ⋯ ≫ e_{N-1} ≫ e_N = 1`,
> in the nested sense of `EventuallyRapid` (the tuple `e' : Fin n → ℕ` lists
> `e_{N-1}, …, e_1`, and the full exponent vector is `Fin.cons 1 e'`), the substituted
> polynomial `g(x_1 + x_N^{e_1}, …, x_{N-1} + x_N^{e_{N-1}}, x_N)`, viewed via `finSuccEquiv`
> as a polynomial in `x_N`, equals `a x_N^d + (lower order terms in x_N)` with `d > 0` and
> `a ∈ R` one of the nonzero coefficients of `g`: its degree is `d` and its leading
> coefficient is the constant `MvPolynomial.C a`.

```lean
theorem eventuallyRapid_subst_constant_leadingCoeff_of_nonconstant
    (n : ℕ) (g : MvPolynomial (Fin (n + 1)) R)
    (hg : ¬ ∃ r : R, g = MvPolynomial.C r) :
    EventuallyRapid n fun e' => ∃ (d : ℕ) (a : R),
      (∃ ν ∈ g.support, a = g.coeff ν) ∧
      0 < d ∧
      (finSuccEquiv R n (subst n (Fin.cons 1 e') g)).natDegree = d ∧
      (finSuccEquiv R n (subst n (Fin.cons 1 e') g)).leadingCoeff = MvPolynomial.C a
```

## Tag 00OX, a lemma

[Tag 00OX](https://stacks.math.columbia.edu/tag/00OX) in the Stacks Project.

**`Stacks.RingTheory.NagataNormalization.exists_isIntegral_aeval`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization.lean#L152).

> **Stacks 00OX**, in the form the induction uses. If the generators `x 0, …, x n` of a
> `k`-algebra `S` satisfy a nonzero polynomial relation `f`, then `S` is integral over the
> subalgebra generated by the `n` elements `y i = x (i + 1) - x 0 ^ D ^ (i + 1)`, where
> `D = f.totalDegree + 2`; these lie in the `ℤ`-subalgebra generated by the `x i`.

```lean
lemma exists_isIntegral_aeval {k : Type*} [Field k] {n : ℕ} {S : Type*} [CommRing S]
    [Algebra k S] (x : Fin (n + 1) → S) (hx : Algebra.adjoin k (Set.range x) = ⊤)
    {f : MvPolynomial (Fin (n + 1)) k} (hf : f ≠ 0) (hfx : MvPolynomial.aeval x f = 0) :
    ∃ y : Fin n → S, (∀ i, y i ∈ Algebra.adjoin ℤ (Set.range x)) ∧
      (MvPolynomial.aeval y : MvPolynomial (Fin n) k →ₐ[k] S).toRingHom.IsIntegral
```

## Tag 00OY, a lemma

[Tag 00OY](https://stacks.math.columbia.edu/tag/00OY) in the Stacks Project.

**`exists_finite_inj_aeval_ringKrullDim_eq_of_adjoin_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization.lean#L439). The attribute's comment: “Stated for a nonzero `k`-algebra with a finite generating set `s` rather than for a presentation `k[x_1, …, x_n]/I`, the source's `ℤ`-subalgebra being `Algebra.adjoin ℤ s`; the map `k[y_1, …, y_r] → S` is pinned as `MvPolynomial.aeval y`. See the module docstring.”.

> **Stacks 00OY** (Noether normalization). Let `k` be a field and let `S` be a nonzero
> commutative `k`-algebra generated by a finite set `s`. Then there are `r : ℕ` and `y : Fin r → S`
> with every `y i` in the `ℤ`-subalgebra of `S` generated by `s`, such that the `k`-algebra map
> `MvPolynomial (Fin r) k →ₐ[k] S` sending `X i` to `y i` is injective and finite; the number `r`
> is the Krull dimension of `S`.

```lean
public theorem exists_finite_inj_aeval_ringKrullDim_eq_of_adjoin_eq_top (k : Type*) {S : Type*}
    [Field k] [CommRing S] [Nontrivial S] [Algebra k S] {s : Set S} (hs : s.Finite)
    (hgen : Algebra.adjoin k s = ⊤) :
    ∃ (r : ℕ) (y : Fin r → S), (∀ i, y i ∈ Algebra.adjoin ℤ s) ∧
      Function.Injective (MvPolynomial.aeval y : MvPolynomial (Fin r) k →ₐ[k] S) ∧
      (MvPolynomial.aeval y : MvPolynomial (Fin r) k →ₐ[k] S).Finite ∧
      ringKrullDim S = r
```

**`ringKrullDim_eq_of_aeval_injective_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization.lean#L456). The attribute's comment: “The closing sentence of the lemma: any `r` and `y_1, …, y_r` with `k[y_1, …, y_r] → S` injective and finite satisfy `dim S = r`. Proved, as in the source, from Lemma 00OK (`Algebra.IsIntegral.ringKrullDim_eq`) and `MvPolynomial.ringKrullDim_of_isNoetherianRing`; no finite generation hypothesis is needed. The existence part is `exists_finite_inj_aeval_ringKrullDim_eq_of_adjoin_eq_top`.”.

> **Stacks 00OY**, the clause "in this case the integer `r` is the dimension of `S`": for a field
> `k`, a commutative `k`-algebra `S` and `y : Fin r → S` such that the `k`-algebra map
> `MvPolynomial (Fin r) k →ₐ[k] S` sending `X i` to `y i` is injective and finite, the Krull
> dimension of `S` is `r`. So every `r` produced by Noether normalization is `dim S`.

```lean
public theorem ringKrullDim_eq_of_aeval_injective_of_finite (k : Type*) {S : Type*}
    [Field k] [CommRing S] [Algebra k S] {r : ℕ} (y : Fin r → S)
    (hinj : Function.Injective (MvPolynomial.aeval y : MvPolynomial (Fin r) k →ₐ[k] S))
    (hfin : (MvPolynomial.aeval y : MvPolynomial (Fin r) k →ₐ[k] S).Finite) :
    ringKrullDim S = r
```

## Tag 00OZ, a lemma

[Tag 00OZ](https://stacks.math.columbia.edu/tag/00OZ) in the Stacks Project.

**`noether_normalization_at_point_topologicalKrullDimAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization/AtPoint.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization/AtPoint.lean#L73). The attribute's comment: “dim\_x(X) is topologicalKrullDimAt of 0055 (4); finite is ψ.toRingHom.Finite”.

> **Noether normalization at a point.** Let `k` be a field, `S` a finite type `k`-algebra,
> `X = Spec(S)`, `𝔮` a prime of `S` and `x ∈ X` the corresponding point. There exist `g ∈ S`,
> `g ∉ 𝔮`, such that `dim(S_g) = dim_x(X) =: d`, and a finite injective `k`-algebra map
> `k[y_1, …, y_d] → S_g`, where `k[y_1, …, y_d] = MvPolynomial (Fin d) k` and `dim_x(X)` is the
> Krull dimension of the topological space `X` at `x` (Stacks 0055 (4)),
> `topologicalKrullDimAt (PrimeSpectrum S) x`.

```lean
theorem noether_normalization_at_point_topologicalKrullDimAt
    {k S : Type*} [Field k] [CommRing S] [Algebra k S] [Algebra.FiniteType k S]
    (q : Ideal S) [q.IsPrime] :
    ∃ (g : S) (_ : g ∉ q) (d : ℕ)
      (ψ : MvPolynomial (Fin d) k →ₐ[k] Localization.Away g),
      (d : WithBot ℕ∞) = ringKrullDim (Localization.Away g) ∧
      (d : WithBot ℕ∞) = topologicalKrullDimAt (PrimeSpectrum S) ⟨q, ‹_›⟩ ∧
      Function.Injective ψ ∧
      ψ.toRingHom.Finite
```

## Tag 051P, a lemma

[Tag 051P](https://stacks.math.columbia.edu/tag/051P) in the Stacks Project.

**`MvPolynomial.exists_finite_comap_eq_span_X_image_of_trdeg_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MvPolynomial/PrimeStandardForm.lean, line 669](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/MvPolynomial/PrimeStandardForm.lean#L669). The attribute's comment: “The two polynomial rings are the one type `MvPolynomial (Fin n) k`, with `(y_{r + 1}, …, y_n)` spelled `Ideal.span (X '' {i | r ≤ (i : ℕ)})`; `φ` is a `k`-algebra map, as the source's construction gives, and `κ(q)` is the canonical `Ideal.ResidueField`. See the module docstring.”.

> Let `k` be a field, let `q ⊆ k[x_1, …, x_n]` be a prime ideal, and let `r` be the
> transcendence degree of the residue field `κ(q)` over `k`. Then there is a finite `k`-algebra map
> `φ : k[y_1, …, y_n] → k[x_1, …, x_n]` whose preimage of `q` is the ideal `(y_{r + 1}, …, y_n)`
> generated by the last `n - r` variables.

```lean
public theorem exists_finite_comap_eq_span_X_image_of_trdeg_eq {k : Type u} [Field k]
    {n : ℕ} (q : Ideal (MvPolynomial (Fin n) k)) [q.IsPrime] {r : ℕ}
    (hr : Algebra.trdeg k q.ResidueField = r) :
    ∃ φ : MvPolynomial (Fin n) k →ₐ[k] MvPolynomial (Fin n) k,
      φ.toRingHom.Finite ∧ q.comap φ = Ideal.span (X '' {i : Fin n | r ≤ (i : ℕ)})
```

## Tag 07NA, a lemma

[Tag 07NA](https://stacks.math.columbia.edu/tag/07NA) in the Stacks Project.

**`exists_subalgebra_finite_inj_aeval_pow_smul_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NoetherNormalization.lean, line 914](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/NoetherNormalization.lean#L914). The attribute's comment: “The chain `R → R[y_1, …, y_d] → S' → S` is realized with `S'` a `Subalgebra R S` and the middle map `MvPolynomial.aeval y`; `S'_f ≅ S_f` is stated in the elementary form `∀ x : S, ∃ n, f ^ n • x ∈ S'`. See the module docstring.”.

> **Stacks 07NA** (Noether normalization over a domain). Let `R` be a domain and let `S` be an
> `R`-algebra of finite type with `R → S` injective. Then there are an integer `d`, an `R`-subalgebra
> `S'` of `S`, elements `y_1, …, y_d ∈ S'` and a nonzero `f ∈ R` such that the `R`-algebra map
> `R[Y_1, …, Y_d] → S'`, `Y_i ↦ y_i`, is injective and makes `S'` a finite module over
> `R[Y_1, …, Y_d]`, and such that every element of `S` lies in `S'` after multiplication by a power
> of `f`; the last condition says precisely that `S'_f ≅ S_f`.

```lean
public theorem exists_subalgebra_finite_inj_aeval_pow_smul_mem (R S : Type*) [CommRing R]
    [IsDomain R] [CommRing S] [Algebra R S] [FaithfulSMul R S] [Algebra.FiniteType R S] :
    ∃ (d : ℕ) (S' : Subalgebra R S) (y : Fin d → S') (f : R), f ≠ 0 ∧
      Function.Injective (MvPolynomial.aeval y : MvPolynomial (Fin d) R →ₐ[R] S') ∧
      (MvPolynomial.aeval y : MvPolynomial (Fin d) R →ₐ[R] S').Finite ∧
      ∀ x : S, ∃ n : ℕ, f ^ n • x ∈ S'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.115, Tag 00OW](https://stacks.math.columbia.edu/tag/00OW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
