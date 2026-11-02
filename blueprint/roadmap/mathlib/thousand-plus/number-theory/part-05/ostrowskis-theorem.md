---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Rat.AbsoluteValue.equiv_real_or_padic, RatFunc.valuation_isEquiv_infty_or_adic
mathlib_file: Mathlib/NumberTheory/Ostrowski.lean
---

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

- [$A\[X\]$ has gcd and lcm if $A$ does](../../../overview/general-algebra/polynomials-and-power-series/a-x-has-gcd-and-lcm-if-a-does.md)
- [$K\[X\]$ is Euclidean](../../../overview/general-algebra/polynomials-and-power-series/k-x-is-euclidean.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Field of fractions of an integral domain](../../../overview/general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Noetherian module](../../../overview/linear-algebra/fundamentals/noetherian-module.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Prime ideal](../../../overview/general-algebra/ideals-and-quotients/prime-ideal.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Rational fraction fields with one indeterminate over a field](../../../undergraduate/ring-theory/field-theory/part-01/rational-fraction-fields-with-one-indeterminate.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Proof depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Bezout’s Theorem](../../../hundred-theorems/part-03/bezouts-theorem.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Cayley-Hamilton theorem](../../../overview/linear-algebra/endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Coprime element](../../../overview/general-algebra/divisibility-in-integral-domains/coprime-element.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Fractional ideal](../../../overview/general-algebra/ideals-and-quotients/fractional-ideal.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Integral root theorem](../../algebra/12-field-theory-and-polynomials/integral-root-theorem.md)
- [Intermediate value theorem](../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Power functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/power-functions.md)
- [Prime spectrum](../../../overview/geometry/algebraic-geometry/prime-spectrum.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Squeeze theorem](../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Subring](../../../overview/general-algebra/rings/subring.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Rat.AbsoluteValue.equiv_real_or_padic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Ostrowski.html#Rat.AbsoluteValue.equiv_real_or_padic)
- [Source of `Rat.AbsoluteValue.equiv_real_or_padic` in Mathlib/NumberTheory/Ostrowski.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Ostrowski.lean#L435)
- [Mathlib documentation: `RatFunc.valuation_isEquiv_infty_or_adic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/RatFunc/Ostrowski.html#RatFunc.valuation_isEquiv_infty_or_adic)
- [Source of `RatFunc.valuation_isEquiv_infty_or_adic` in Mathlib/NumberTheory/RatFunc/Ostrowski.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/RatFunc/Ostrowski.lean#L257)
- [1000+ theorems list: Q2919401](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2314)
- [1000+ theorems project: Q2919401](https://1000-plus.github.io/?length=-1#Q2919401)
- [Wikipedia: Ostrowski's theorem](https://en.wikipedia.org/wiki/Ostrowski's_theorem)
- [Wikidata: Q2919401](https://www.wikidata.org/wiki/Q2919401)
