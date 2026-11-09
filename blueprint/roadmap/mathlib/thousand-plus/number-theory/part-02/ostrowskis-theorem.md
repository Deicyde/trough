# Ostrowski's theorem

Mathlib records this with 2 declarations.

`Rat.AbsoluteValue.equiv_real_or_padic`: **Ostrowski's Theorem**: every absolute value (with values in `ℝ`) on `ℚ` is equivalent
to either the standard absolute value or a `p`-adic absolute value for a prime `p`.

```lean
Rat.AbsoluteValue.equiv_real_or_padic (f : AbsoluteValue ℚ ℝ) (hf_nontriv : f.IsNontrivial) :
  f ≈ Rat.AbsoluteValue.real ∨ ∃! p, ∃ (x : Fact (Nat.Prime p)), f ≈ Rat.AbsoluteValue.padic p
```

`RatFunc.valuation_isEquiv_infty_or_adic`: **Ostrowski's Theorem** for `K(X)` with `K` any field:
A valuation trivial on `K` is equivalent either to the valuation at infinity or to
the `p`-adic valuation for a unique maximal ideal `p` of `K[X]`.

```lean
RatFunc.valuation_isEquiv_infty_or_adic.{u_1, u_2} {K : Type u_1} {Γ : Type u_2} [Field K]
  [LinearOrderedCommGroupWithZero Γ] {v : Valuation (RatFunc K) Γ} [Valuation.IsTrivialOn K v]
  [v.IsNontrivial] [DecidableEq (RatFunc K)] :
  Xor (v.IsEquiv (RatFunc.inftyValuation K))
    (∃! u, v.IsEquiv (IsDedekindDomain.HeightOneSpectrum.valuation (RatFunc K) u))
```

## Depends on

- [$K\[X\]$ is Euclidean](../../../overview/general-algebra/polynomials-and-power-series/k-x-is-euclidean.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Field of fractions of an integral domain](../../../overview/general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Least common multiple](../../../overview/general-algebra/divisibility-in-integral-domains/least-common-multiple.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Noetherian module](../../../overview/linear-algebra/fundamentals/noetherian-module.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Prime ideal](../../../overview/general-algebra/ideals-and-quotients/prime-ideal.md)
- [Rational fraction fields with one indeterminate over a field](../../../undergraduate/ring-theory/field-theory/rational-fraction-fields-with-one-indeterminate.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Proof depends on

- [Array](../../../overview/data-structures/list-like-structures/array.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Coprime element](../../../overview/general-algebra/divisibility-in-integral-domains/coprime-element.md)
- [Field $\Q$ of rational numbers](../../../undergraduate/ring-theory/field-theory/field-q-of-rational-numbers.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Logarithm](../../../overview/analysis/special-functions/logarithm.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Rat.AbsoluteValue.equiv_real_or_padic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Ostrowski.html#Rat.AbsoluteValue.equiv_real_or_padic)
- [Source of `Rat.AbsoluteValue.equiv_real_or_padic` in Mathlib/NumberTheory/Ostrowski.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/Ostrowski.lean#L435)
- [Mathlib documentation: `RatFunc.valuation_isEquiv_infty_or_adic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/RatFunc/Ostrowski.html#RatFunc.valuation_isEquiv_infty_or_adic)
- [Source of `RatFunc.valuation_isEquiv_infty_or_adic` in Mathlib/NumberTheory/RatFunc/Ostrowski.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/RatFunc/Ostrowski.lean#L257)
- [1000+ theorems list: Q2919401](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2314)
- [1000+ theorems project: Q2919401](https://1000-plus.github.io/all.html?length=-1#Q2919401)
- [Wikipedia: Ostrowski's theorem](https://en.wikipedia.org/wiki/Ostrowski's_theorem)
- [Wikidata: Q2919401](https://www.wikidata.org/wiki/Q2919401)
