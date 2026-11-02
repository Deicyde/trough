---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.borelCaratheodory
mathlib_file: Mathlib/Analysis/Complex/BorelCaratheodory.lean
---

# Borel–Carathéodory theorem

**Borel-Carathéodory theorem**.

If `f` is analytic on the open ball `‖z‖ < R` and satisfies `(f z).re ≤ M` for all such `z`,
then `‖f z‖ ≤ 2 * M * ‖z‖ / (R - ‖z‖) + ‖f 0‖ * (R + ‖z‖) / (R - ‖z‖)` for all `‖z‖ < R`.

```lean
Complex.borelCaratheodory {f : ℂ → ℂ} {M R : ℝ} {z : ℂ} (hM : 0 < M)
  (hf : DifferentiableOn ℂ f (Metric.ball 0 R))
  (hf₁ : Set.MapsTo f (Metric.ball 0 R) {z | z.re ≤ M}) (hR : 0 < R) (hz : z ∈ Metric.ball 0 R) :
  ‖f z‖ ≤ 2 * M * ‖z‖ / (R - ‖z‖) + ‖f 0‖ * (R + ‖z‖) / (R - ‖z‖)
```

## Depends on

- [Ball](../../../../overview/topology/metric-spaces/ball.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)

## Proof depends on

- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Inner product space, over $R$ or $C$](../../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [List](../../../../overview/data-structures/list-like-structures/list.md)

## Sources

- [Mathlib documentation: `Complex.borelCaratheodory`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/BorelCaratheodory.html#Complex.borelCaratheodory)
- [Source of `Complex.borelCaratheodory` in Mathlib/Analysis/Complex/BorelCaratheodory.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/BorelCaratheodory.lean#L105)
- [1000+ theorems list: Q3229335](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2361)
- [1000+ theorems project: Q3229335](https://1000-plus.github.io/all.html?length=-1#Q3229335)
- [Wikipedia: Borel–Carathéodory theorem](https://en.wikipedia.org/wiki/Borel%E2%80%93Carath%C3%A9odory_theorem)
- [Wikidata: Q3229335](https://www.wikidata.org/wiki/Q3229335)
