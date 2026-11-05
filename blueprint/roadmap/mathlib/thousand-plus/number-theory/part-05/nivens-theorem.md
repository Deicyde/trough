---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: niven
mathlib_file: Mathlib/NumberTheory/Niven.lean
---

# Niven's theorem

**Niven's theorem**: The only rational values of `cos` that occur at rational multiples of π
are `{-1, -1/2, 0, 1/2, 1}`.

```lean
niven {θ : ℝ} (hθ : ∃ r, θ = ↑r * Real.pi) (hcos : ∃ q, Real.cos θ = ↑q) :
  Real.cos θ ∈ {-1, -1 / 2, 0, 1 / 2, 1}
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)

## Proof depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Integral root theorem](../../algebra/12-field-theory-and-polynomials/integral-root-theorem.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `niven`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Niven.html#niven)
- [Source of `niven` in Mathlib/NumberTheory/Niven.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Niven.lean#L105)
- [1000+ theorems list: Q4116459](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2668)
- [1000+ theorems project: Q4116459](https://1000-plus.github.io/all.html?length=-1#Q4116459)
- [Wikipedia: Niven's theorem](https://en.wikipedia.org/wiki/Niven's_theorem)
- [Wikidata: Q4116459](https://www.wikidata.org/wiki/Q4116459)
