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
- [Euclidean domain](../../general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Freiman homomorphisms](freiman-homomorphisms.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [The Binomial Theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md)

## Sources

- [Mathlib documentation: `Behrend.roth_lower_bound`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/AP/Three/Behrend.html#Behrend.roth_lower_bound)
- [Source of `Behrend.roth_lower_bound` in Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean#L482)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L542)
