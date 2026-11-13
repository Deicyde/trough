---
declaration: section
origin: cited
lean: RingHom.IsIntegralElemOverIdeal, isIntegralElemOverIdeal_iff_isIntegralElem, Ideal.exists_submodule_and_mul_isIntegralElemOverIdeal, Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_mem_map, Polynomial.isIntegral_coeff_and_coeff_mem_radical_of_monic_dvd, minpoly.isIntegrallyClosed_eq_field_fractions
statement: formalized
proof: formalized
---

# 10.38 Going down for integral over normal

Section 10.38 of the Stacks Project, [Tag 037E](https://stacks.math.columbia.edu/tag/037E). 6 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00H2, a definition

[Tag 00H2](https://stacks.math.columbia.edu/tag/00H2) in the Stacks Project.

**`RingHom.IsIntegralElemOverIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L67).

> An element `g ∈ S` is *integral over the ideal `I ⊂ R`* with respect to the
> ring map `φ : R →+* S` if there exists a monic polynomial `P ∈ R[X]` of degree
> `d` such that every coefficient `P.coeff j` lies in `I ^ (d - j)`, and `P`
> evaluated at `g` via `φ` is zero in `S`.
>
> Since `P` is monic with `d = P.natDegree`, the leading coefficient `P.coeff d`
> equals `1 ∈ I ^ 0 = ⊤`, and the coefficients above the degree vanish, so the
> condition `∀ j, P.coeff j ∈ I ^ (d - j)` is exactly the Stacks requirement on
> the non-leading coefficients `a_j ∈ I ^ (d - j)` for `j < d`.

```lean
def IsIntegralElemOverIdeal {R S : Type*} [CommRing R] [Ring S]
    (φ : R →+* S) (I : Ideal R) (g : S) : Prop
```

## Tag 00H3, a lemma

[Tag 00H3](https://stacks.math.columbia.edu/tag/00H3) in the Stacks Project.

**`isIntegralElemOverIdeal_iff_isIntegralElem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L290).

> **[Stacks, Tag 00H3].** Let `φ : R →+* S` be a ring map and `I ⊆ R` an ideal, and let
> `A = reesAlgebra I = ∑ Iⁿ Xⁿ ⊆ R[X]`, mapped to `S[X]` along the coefficientwise extension of `φ`.
> An element `s : S` is integral over `I` if and only if `C s · X ∈ S[X]` is integral over `A`.
>
> Both directions are proved: `isIntegralElem_of_isIntegralOverIdeal` (forward) and
> `isIntegralElemOverIdeal_of_isIntegralElem` (converse, by taking the `X ^ d` coefficient).

```lean
theorem isIntegralElemOverIdeal_iff_isIntegralElem (φ : R →+* S) (I : Ideal R) (s : S) :
    φ.IsIntegralElemOverIdeal I s ↔ (reesToPolyS φ I).IsIntegralElem (C s * X)
```

## Tag 00H4, a lemma

[Tag 00H4](https://stacks.math.columbia.edu/tag/00H4) in the Stacks Project.

**`Ideal.exists_submodule_and_mul_isIntegralElemOverIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L423).

> **[Stacks, Tag 00H4].** Let `S` be an `R`-algebra and `I ⊆ R` an ideal. The elements of `S`
> integral over `I` form an `R`-submodule of `S`; furthermore, if `s ∈ S` is integral over `R` and
> `g ∈ S` is integral over `I`, then `s * g` is integral over `I`.

```lean
theorem Ideal.exists_submodule_and_mul_isIntegralElemOverIdeal (I : Ideal R) :
    (∃ M : Submodule R S, ∀ g, g ∈ M ↔ (algebraMap R S).IsIntegralElemOverIdeal I g) ∧
      ∀ s g : S, IsIntegral R s → (algebraMap R S).IsIntegralElemOverIdeal I g →
        (algebraMap R S).IsIntegralElemOverIdeal I (s * g)
```

## Tag 00H5, a lemma

[Tag 00H5](https://stacks.math.columbia.edu/tag/00H5) in the Stacks Project.

Declarations registered for the tag:

- [`Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_mem_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_mem_map#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L447) (StacksFrontier).

## Tag 00H6, a lemma

[Tag 00H6](https://stacks.math.columbia.edu/tag/00H6) in the Stacks Project.

**`Polynomial.isIntegral_coeff_and_coeff_mem_radical_of_monic_dvd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Polynomial/MonicDvdCoeff.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Polynomial/MonicDvdCoeff.lean#L129). The attribute's comment: “(1) is Mathlib's `Polynomial.isIntegral_coeff_of_dvd`; (2) proved here”.

> **Stacks 00H6.** Let `K` be a field, and let `g = xⁿ + aₙ₋₁xⁿ⁻¹ + ⋯ + a₀` divide
> `f = xᵐ + bₘ₋₁xᵐ⁻¹ + ⋯ + b₀` in `K[x]`. Then
> 1. the `aᵢ` are integral over any subring `R₀ ⊆ K` containing the `bⱼ`, and
> 2. each `aᵢ` lies in `√((b₀, …, bₘ₋₁)R)` for any subring `R ⊆ K` containing the `aᵢ` and the
>    `bⱼ`.

```lean
theorem isIntegral_coeff_and_coeff_mem_radical_of_monic_dvd {f g : K[X]} (hf : f.Monic)
    (hg : g.Monic) (hgf : g ∣ f) :
    (∀ R₀ : Subring K, (∀ j, f.coeff j ∈ R₀) → ∀ i, IsIntegral R₀ (g.coeff i)) ∧
    (∀ R : Subring K, (∀ j, f.coeff j ∈ R) → ∀ hgR : ∀ i, g.coeff i ∈ R,
      ∀ i < g.natDegree, (⟨g.coeff i, hgR i⟩ : R) ∈
        (Ideal.span {x : R | ∃ j < f.natDegree, (x : K) = f.coeff j}).radical)
```

## Tag 00H7, a lemma

[Tag 00H7](https://stacks.math.columbia.edu/tag/00H7) in the Stacks Project.

Declarations registered for the tag:

- [`minpoly.isIntegrallyClosed_eq_field_fractions`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=minpoly.isIntegrallyClosed_eq_field_fractions#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/GoingDown/Criteria.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/GoingDown/Criteria.lean#L21) (StacksFrontier): “the minimal polynomial over the fraction field is the base change of the minimal polynomial over the integrally closed base, so its coefficients lie in the base”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.38, Tag 037E](https://stacks.math.columbia.edu/tag/037E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
