---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Behrend.roth_lower_bound
mathlib_file: Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean
---

# Behrend's construction

Mathlib states this as `Behrend.roth_lower_bound`.

```lean
Behrend.roth_lower_bound {N : ℕ} : ↑N * Real.exp (-4 * √(Real.log ↑N)) ≤ ↑(rothNumberNat N)
```

## Depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Sets without arithmetic progressions](sets-without-arithmetic-progressions.md)

## Proof depends on

- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Euclidean domain](../../general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Freiman homomorphisms](freiman-homomorphisms.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)

## Sources

- [Mathlib documentation: `Behrend.roth_lower_bound`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/AP/Three/Behrend.html#Behrend.roth_lower_bound)
- [Source of `Behrend.roth_lower_bound` in Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean#L482)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L542)
