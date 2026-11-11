---
declaration: section
origin: cited
lean: RingHom.IsIntegralElemOverIdeal, isIntegralElem_of_isIntegralOverIdeal, isIntegralElem_of_isIntegralElemOverIdeal, zero_isIntegralElemOverIdeal, mul_left_isIntegralElemOverIdeal, Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_mem_map, minpoly.isIntegrallyClosed_eq_field_fractions
statement: formalized
proof: formalized
---

# 10.38 Going down for integral over normal

Section 10.38 of the Stacks Project, [Tag 037E](https://stacks.math.columbia.edu/tag/037E). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00H2, a definition

[Tag 00H2](https://stacks.math.columbia.edu/tag/00H2) in the Stacks Project.

**`RingHom.IsIntegralElemOverIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L67).

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

**`isIntegralElem_of_isIntegralOverIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L226). The attribute's comment: “Forward implication only: integral over I implies C s * X integral over reesAlgebra I. The converse half of the equivalence is not formalized.”.

> If `s : S` is integral over the ideal `I ⊂ R` (with respect to `φ : R →+* S`),
> then `C s · X ∈ S[X]` is integral over the Rees subalgebra `reesAlgebra I`
> viewed inside `S[X]` via the coefficient-wise extension of `φ`.

```lean
theorem isIntegralElem_of_isIntegralOverIdeal (φ : R →+* S) (I : Ideal R) (s : S)
    (h : IsIntegralOverIdeal φ I s) :
    (reesToPolyS φ I).IsIntegralElem (C s * X)
```

**`isIntegralElem_of_isIntegralElemOverIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdealIntegrallyClosed.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/OverIdealIntegrallyClosed.lean#L92). The attribute's comment: “Forward implication only: integral over I implies C s * X integral over reesAlgebra I. The converse half of the equivalence is not formalized.”.

> **[Stacks, Tag 00H3], the forward implication.** If `s : S` is integral over the ideal
> `I ⊆ R` with respect to `φ : R →+* S`, then `C s · X ∈ S[X]` is integral over the Rees
> subalgebra `reesAlgebra I`, viewed inside `S[X]` along the coefficientwise extension of `φ`.
>
> A monic witness of degree zero is `1`, whose vanishing at `s` makes `s = 0`, and then `C s · X`
> is zero and `X` is a witness; otherwise `forwardWitness` multiplies the `i`-th coefficient by
> `X ^ (n - i)` to land in the Rees algebra.

```lean
theorem isIntegralElem_of_isIntegralElemOverIdeal (φ : R →+* S) (I : Ideal R) (s : S)
    (h : φ.IsIntegralElemOverIdeal I s) :
    (reesToPolyS φ I).IsIntegralElem (C s * X)
```

## Tag 00H4, a lemma

[Tag 00H4](https://stacks.math.columbia.edu/tag/00H4) in the Stacks Project.

**`zero_isIntegralElemOverIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L264). The attribute's comment: “Partial: only that 0 is integral over I. Closure under addition, and hence the submodule conclusion of 00H4, is not formalized.”.

> The zero element of `S` is integral over any ideal `I ⊂ R`, witnessed by
> the polynomial `X`. (Partial component of Stacks `00H4`.)

```lean
theorem zero_isIntegralElemOverIdeal
    {R : Type*} {S : Type*} [CommRing R] [Ring S]
    (φ : R →+* S) (I : Ideal R) :
    RingHom.IsIntegralElemOverIdeal φ I (0 : S)
```

**`mul_left_isIntegralElemOverIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L290). The attribute's comment: “Partial: only closure under R-scalar multiplication. Closure under addition, and hence the submodule conclusion of 00H4, is not formalized.”.

> If `g ∈ S` is integral over the ideal `I` and `r ∈ R`, then `φ r * g` is
> integral over `I`. (Partial component of Stacks `00H4`: closure under
> `R`-scalar multiplication, with the action expressed through the ring map
> `φ`.)

```lean
theorem mul_left_isIntegralElemOverIdeal
    {R : Type*} {S : Type*} [CommRing R] [CommRing S]
    (φ : R →+* S) (I : Ideal R) (r : R) (g : S)
    (h : RingHom.IsIntegralElemOverIdeal φ I g) :
    RingHom.IsIntegralElemOverIdeal φ I (φ r * g)
```

## Tag 00H5, a lemma

[Tag 00H5](https://stacks.math.columbia.edu/tag/00H5) in the Stacks Project.

Declarations registered for the tag:

- [`Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_mem_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_mem_map#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/OverIdeal.lean#L322) (StacksFrontier).

## Tag 00H7, a lemma

[Tag 00H7](https://stacks.math.columbia.edu/tag/00H7) in the Stacks Project.

Declarations registered for the tag:

- [`minpoly.isIntegrallyClosed_eq_field_fractions`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=minpoly.isIntegrallyClosed_eq_field_fractions#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/GoingDown/Criteria.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/GoingDown/Criteria.lean#L21) (StacksFrontier): “the minimal polynomial over the fraction field is the base change of the minimal polynomial over the integrally closed base, so its coefficients lie in the base”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.38, Tag 037E](https://stacks.math.columbia.edu/tag/037E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
