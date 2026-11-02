---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ax_grothendieck_zeroLocus
mathlib_file: Mathlib/FieldTheory/AxGrothendieck.lean
---

# Ax–Grothendieck theorem

The **Ax-Grothendieck** theorem

If `K` is an algebraically closed field, and `S : Set (ι → K)` is the `zeroLocus` of an ideal
of the multivariable polynomial ring, then any injective polynomial map `S → S`  is also
surjective on `S`.

```lean
ax_grothendieck_zeroLocus.{u_1, u_2} {K : Type u_1} {ι : Type u_2} [Field K] [IsAlgClosed K]
  [Finite ι] (I : Ideal (MvPolynomial ι K)) (p : ι → MvPolynomial ι K) :
  have S := MvPolynomial.zeroLocus K I;
  Set.MapsTo (fun v i => (MvPolynomial.eval v) (p i)) S S →
    Set.InjOn (fun v i => (MvPolynomial.eval v) (p i)) S →
      Set.SurjOn (fun v i => (MvPolynomial.eval v) (p i)) S S
```

## Depends on

- [Algebraically closed field](../../../../overview/general-algebra/field-theory/algebraically-closed-field.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Ideal of a commutative ring](../../../../overview/general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Polynomial in several indeterminates](../../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)

## Proof depends on

- [Algebraic extension](../../../../overview/general-algebra/field-theory/algebraic-extension.md)
- [Characteristic of a ring](../../../../overview/general-algebra/field-theory/characteristic-of-a-ring.md)
- [Definable set](../../../../overview/logic-and-computation/model-theory/definable-set.md)
- [Existence of algebraic closure of a field](../../../../overview/general-algebra/field-theory/existence-of-algebraic-closure-of-a-field.md)
- [Irreducible element](../../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Local ring](../../../../overview/general-algebra/rings/local-ring.md)
- [Noetherian ring](../../../../overview/general-algebra/rings/noetherian-ring.md)
- [Satisfiability](../../../../overview/logic-and-computation/model-theory/satisfiability.md)
- [Sum of subspaces](../../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `ax_grothendieck_zeroLocus`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AxGrothendieck.html#ax_grothendieck_zeroLocus)
- [Source of `ax_grothendieck_zeroLocus` in Mathlib/FieldTheory/AxGrothendieck.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/AxGrothendieck.lean#L219)
- [1000+ theorems list: Q4830725](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2848)
- [1000+ theorems project: Q4830725](https://1000-plus.github.io/all.html?length=-1#Q4830725)
- [Wikipedia: Ax–Grothendieck theorem](https://en.wikipedia.org/wiki/Ax%E2%80%93Grothendieck_theorem)
- [Wikidata: Q4830725](https://www.wikidata.org/wiki/Q4830725)
