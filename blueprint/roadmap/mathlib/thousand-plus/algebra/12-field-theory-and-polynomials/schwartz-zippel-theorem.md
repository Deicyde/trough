# Schwartz–Zippel theorem

The **Schwartz-Zippel lemma**

For a nonzero multivariable polynomial `p` over an integral domain, the probability that `p`
evaluates to zero at points drawn at random from a product of finite subsets `S i` of the integral
domain is bounded by the supremum of `∑ i, degᵢ s / #(S i)` ranging over monomials `s` of `p`.

```lean
MvPolynomial.schwartz_zippel_sup_sum.{u_1} {R : Type u_1} [CommRing R] [IsDomain R] [DecidableEq R]
  {n : ℕ} {p : MvPolynomial (Fin n) R} (hp : p ≠ 0) (S : Fin n → Finset R) :
  ↑{x ∈ Fintype.piFinset fun i => S i | (MvPolynomial.eval x) p = 0}.card / ∏ i, ↑(S i).card ≤
    p.support.sup fun s => ∑ i, ↑(s i) / ↑(S i).card
```

## Depends on

- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Roots of a polynomial](../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)

## Sources

- [Mathlib documentation: `MvPolynomial.schwartz_zippel_sup_sum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/SchwartzZippel.html#MvPolynomial.schwartz_zippel_sup_sum)
- [Source of `MvPolynomial.schwartz_zippel_sup_sum` in Mathlib/Algebra/MvPolynomial/SchwartzZippel.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/MvPolynomial/SchwartzZippel.lean#L67)
- [1000+ theorems list: Q7433182](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3789)
- [1000+ theorems project: Q7433182](https://1000-plus.github.io/all.html?length=-1#Q7433182)
- [Wikipedia: Schwartz–Zippel theorem](https://en.wikipedia.org/wiki/Schwartz%E2%80%93Zippel_theorem)
- [Wikidata: Q7433182](https://www.wikidata.org/wiki/Q7433182)
