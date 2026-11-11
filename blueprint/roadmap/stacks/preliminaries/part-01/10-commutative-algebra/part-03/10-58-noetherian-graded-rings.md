---
declaration: section
origin: cited
lean: generates_algebra_iff_generates_irrelevant, GradedRing.isNoetherianRing_iff_isNoetherianRing_gradeZero_and_irrelevant_fg, IsNumericalPolynomial, numerical_polynomial_functorial, main_00JZ, graded_module_pieces_finite, hilbertFun_isNumericalPolynomial, Stacks.HilbertFunction.PolynomialQuotient.hilbertFunction_degree_lt
statement: formalized
proof: formalized
---

# 10.58 Noetherian graded rings

Section 10.58 of the Stacks Project, [Tag 00JV](https://stacks.math.columbia.edu/tag/00JV). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07Z4, a lemma

[Tag 07Z4](https://stacks.math.columbia.edu/tag/07Z4) in the Stacks Project.

**`generates_algebra_iff_generates_irrelevant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/FinitelyGenerated.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedAlgebra/FinitelyGenerated.lean#L459). References: EGA II (2.1.3); EGA II (2.1.4), “partial”.

> Stacks Tag 07Z4: for a family `(f i)` of homogeneous elements of strictly
> positive degree in a graded ring `A` with grading `𝒜` (the `GradedRing 𝒜`
> hypothesis, together with the explicit `DirectSum.Decomposition 𝒜`, encodes the
> direct-sum decomposition `A = ⨁_d 𝒜 d`), the family generates `A` as an algebra
> over the degree-zero subring `𝒜 0` if and only if it generates the irrelevant
> ideal `S₊` as an ideal of `A`.

```lean
theorem generates_algebra_iff_generates_irrelevant
    {I : Type*} (f : I → A) (d : I → ℕ)
    (hd : ∀ i, 0 < d i) (hf : ∀ i, f i ∈ 𝒜 (d i)) :
    Algebra.adjoin ↥(𝒜 0) (Set.range f) = ⊤ ↔
    Ideal.span (Set.range f) = (HomogeneousIdeal.irrelevant 𝒜).toIdeal
```

## Tag 00JW, a lemma

[Tag 00JW](https://stacks.math.columbia.edu/tag/00JW) in the Stacks Project.

**`GradedRing.isNoetherianRing_iff_isNoetherianRing_gradeZero_and_irrelevant_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Noetherian.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedAlgebra/Noetherian.lean#L284). References: EGA II (2.1.5), “necessity”.

> A graded ring `A = ⨁_d 𝒜 d` is Noetherian if and only if its degree-zero subring `𝒜 0`
> is a Noetherian ring and its irrelevant ideal `⨁_{d > 0} 𝒜 d` is finitely generated as an
> ideal of `A`.

```lean
public theorem isNoetherianRing_iff_isNoetherianRing_gradeZero_and_irrelevant_fg
    (𝒜 : ℕ → σ) [GradedRing 𝒜] :
    IsNoetherianRing A ↔
      IsNoetherianRing (𝒜 0) ∧ (HomogeneousIdeal.irrelevant 𝒜).toIdeal.FG
```

## Tag 00JX, a definition

[Tag 00JX](https://stacks.math.columbia.edu/tag/00JX) in the Stacks Project.

**`IsNumericalPolynomial`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NumericalPolynomial.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NumericalPolynomial.lean#L68).

> A function `f : ℤ → A` (with `A` an additive abelian group) is a
> *numerical polynomial* if there exist `r : ℕ` and elements
> `a : Fin (r + 1) → A` such that
> `f n = ∑_{i = 0}^{r} (n choose i) • a i` holds for all sufficiently large
> integers `n`.

```lean
def IsNumericalPolynomial (f : ℤ → A) : Prop
```

## Tag 00JY, a lemma

[Tag 00JY](https://stacks.math.columbia.edu/tag/00JY) in the Stacks Project.

**`numerical_polynomial_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NumericalPolynomial.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NumericalPolynomial.lean#L113).

> Numerical polynomials are functorial: if `φ : A →+ A'` is a homomorphism of abelian groups
> and `f : ℤ → A` is a numerical polynomial, then `n ↦ φ (f n)` is a numerical polynomial valued in
> `A'`.

```lean
theorem numerical_polynomial_functorial
    {A A' : Type*} [AddCommGroup A] [AddCommGroup A']
    (φ : A →+ A') (f : ℤ → A) (hf : IsNumericalPolynomial f) :
    IsNumericalPolynomial (fun n => φ (f n))
```

## Tag 00JZ, a lemma

[Tag 00JZ](https://stacks.math.columbia.edu/tag/00JZ) in the Stacks Project.

**`main_00JZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NumericalPolynomial.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NumericalPolynomial.lean#L221).

> Let `A` be an abelian group and `f : ℤ → A`. If the backward difference
> `n ↦ f n - f (n - 1)` is a numerical polynomial, then so is `f`.

```lean
theorem main_00JZ {A : Type*} [AddCommGroup A] (f : ℤ → A)
    (hdiff : IsNumericalPolynomial (fun n => f n - f (n - 1))) :
    IsNumericalPolynomial f
```

## Tag 00K0, a lemma

[Tag 00K0](https://stacks.math.columbia.edu/tag/00K0) in the Stacks Project.

**`graded_module_pieces_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/FinitelyGenerated.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedAlgebra/FinitelyGenerated.lean#L266). References: EGA II (2.1.6), “(i)”.

> **Stacks 00K0**.
> Let `S = ⨁_{n ≥ 0} 𝒜 n` be a graded ring and `M = ⨁_{n ∈ ℤ} ℳ n` a graded `S`-module, with
> `S_d · M_e ⊆ M_{d+e}`. If `M` is finitely generated as an `S`-module and `S` is finitely
> generated as an `𝒜 0`-algebra, then every graded piece `ℳ n` is a finite `𝒜 0`-module.

```lean
theorem graded_module_pieces_finite (ℳ : ℤ → Submodule (𝒜 0) M) [DirectSum.Decomposition ℳ]
    (hsmul : ∀ (d : ℕ) (e : ℤ) (s : S), s ∈ 𝒜 d → ∀ m : M, m ∈ ℳ e → s • m ∈ ℳ ((d : ℤ) + e))
    (hM : Module.Finite S M)
    (hS : Algebra.FiniteType (𝒜 0) S) : ∀ n : ℤ, Module.Finite (𝒜 0) (ℳ n)
```

## Tag 00K1, a proposition

[Tag 00K1](https://stacks.math.columbia.edu/tag/00K1) in the Stacks Project.

**`hilbertFun_isNumericalPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertFunction/Polynomiality.lean, line 741](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertFunction/Polynomiality.lean#L741).

> **Main statement (Stacks Tag 00K1, Proposition 10.58.7).**
> Let `S` be a Noetherian graded ring with degree-zero ring `S_0 = ↥(𝒮 0)`, graded
> nonnegatively (`𝒮 d = 0` for `d < 0`), and let `M` be a finite graded `S`-module.
> Assume the irrelevant ideal `S_+` is generated by elements of degree `1`
> (`GeneratedInDegreeOne 𝒮`).  Then the Hilbert function
> `n ↦ [M_n] ∈ K'_0(S_0)` is a numerical polynomial.

```lean
theorem hilbertFun_isNumericalPolynomial (hneg : ∀ d : ℤ, d < 0 → 𝒮 d = ⊥)
    (hgen : GeneratedInDegreeOne 𝒮) : IsEventualNumericalPolynomial (hilbertFun 𝒮 ℳ hneg)
```

## Tag 00K3, a lemma

[Tag 00K3](https://stacks.math.columbia.edu/tag/00K3) in the Stacks Project.

**`Stacks.HilbertFunction.PolynomialQuotient.hilbertFunction_degree_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertFunction/DegreeBound.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertFunction/DegreeBound.lean#L605).

> **Main Theorem (Stacks Lemma 10.58.10, Tag 00K3).**
> Let `k` be a field, `d ≥ 1`, and `S = k[X_1, …, X_d]` with the standard grading.
> Let `I ⊆ S` be a *nonzero* graded ideal and set `M = S / I`. Then the Hilbert
> function `H_M(n) = dim_k(M_n)` is, for large `n`, given by a rational polynomial
> `P` whose degree is strictly less than `d - 1`.
>
> Concretely: there exist `P ∈ ℚ[T]` with `deg P < d - 1` and an integer `N` such
> that `dim_k(M_n) = P(n)` for all `n ≥ N`. The degree bound `deg P < d - 1` is
> expressed using `Polynomial.degree : ℚ[X] → WithBot ℕ`, which sends the zero
> polynomial to `⊥`; thus `deg P < d - 1` automatically allows `P = 0` (the case
> `-∞ < d - 1`), and when `d = 1` it forces `P = 0`.

```lean
theorem hilbertFunction_degree_lt (hd : 1 ≤ d) (I : Ideal (MvPolynomial (Fin d) k))
    (hI_hom : Ideal.IsHomogeneous (MvPolynomial.homogeneousSubmodule (Fin d) k) I)
    (hI_ne : I ≠ ⊥) :
    ∃ (P : Polynomial ℚ) (N : ℕ),
      P.degree < ((d - 1 : ℕ) : WithBot ℕ) ∧
        ∀ n : ℕ, N ≤ n → (hilbertFunction I n : ℚ) = P.eval (n : ℚ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.58, Tag 00JV](https://stacks.math.columbia.edu/tag/00JV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
