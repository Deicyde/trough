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

- [Ball](../../../overview/topology/metric-spaces/ball.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)

## Proof depends on

- [Removable singularity](../../../overview/analysis/complex-analysis/removable-singularity.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)

## Sources

- [Mathlib documentation: `Complex.borelCaratheodory`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/BorelCaratheodory.html#Complex.borelCaratheodory)
- [Source of `Complex.borelCaratheodory` in Mathlib/Analysis/Complex/BorelCaratheodory.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Complex/BorelCaratheodory.lean#L105)
- [1000+ theorems list: Q3229335](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2361)
- [1000+ theorems project: Q3229335](https://1000-plus.github.io/all.html?length=-1#Q3229335)
- [Wikipedia: Borel–Carathéodory theorem](https://en.wikipedia.org/wiki/Borel%E2%80%93Carath%C3%A9odory_theorem)
- [Wikidata: Q3229335](https://www.wikidata.org/wiki/Q3229335)
