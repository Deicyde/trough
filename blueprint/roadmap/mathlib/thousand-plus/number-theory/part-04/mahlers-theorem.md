---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: PadicInt.hasSum_mahler
mathlib_file: Mathlib/NumberTheory/Padics/MahlerBasis.lean
---

# Mahler's theorem

**Mahler's theorem**: for any continuous function `f` from `ℤ_[p]` to a `p`-adic Banach space, the
Mahler series with coefficients `n ↦ Δ_[1]^[n] f 0` converges to the original function `f`.

```lean
PadicInt.hasSum_mahler.{u_1} {p : ℕ} [hp : Fact (Nat.Prime p)] {E : Type u_1} [NormedAddCommGroup E]
  [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E] [IsUltrametricDist E] [CompleteSpace E]
  (f : C(ℤ_[p], E)) : HasSum (fun n => PadicInt.mahlerTerm ((fwdDiff 1)^[n] (⇑f) 0) n) f
```

## Depends on

- [$p$-adic integer](../../../overview/general-algebra/numbers/p-adic-integer.md)
- [Compact open topology](../../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Bezout’s Theorem](../../../hundred-theorems/part-03/bezouts-theorem.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Field $\Q$ of rational numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-q-of-rational-numbers.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Heine-Cantor theorem](../../../overview/topology/uniform-notions/heine-cantor-theorem.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `PadicInt.hasSum_mahler`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/MahlerBasis.html#PadicInt.hasSum_mahler)
- [Source of `PadicInt.hasSum_mahler` in Mathlib/NumberTheory/Padics/MahlerBasis.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Padics/MahlerBasis.lean#L331)
- [1000+ theorems list: Q3527118](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2495)
- [1000+ theorems project: Q3527118](https://1000-plus.github.io/all.html?length=-1#Q3527118)
- [Wikipedia: Mahler's theorem](https://en.wikipedia.org/wiki/Mahler's_theorem)
- [Wikidata: Q3527118](https://www.wikidata.org/wiki/Q3527118)
