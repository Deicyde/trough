# Principle of analytic continuation

The *identity principle* for analytic functions, global version: if two functions are
analytic on a connected set `U` and coincide at points which accumulate to a point `z₀ ∈ U`, then
they coincide globally in `U`.
For higher-dimensional versions requiring that the functions coincide in a neighborhood of `z₀`,
see `AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq`.

```lean
AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq.{u_1, u_2} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {f g : 𝕜 → E}
  {z₀ : 𝕜} {U : Set 𝕜} (hf : AnalyticOnNhd 𝕜 f U) (hg : AnalyticOnNhd 𝕜 g U) (hU : IsPreconnected U)
  (h₀ : z₀ ∈ U) (hfg : ∃ᶠ (z : 𝕜) in nhdsWithin z₀ {z₀}ᶜ, f z = g z) : Set.EqOn f g U
```

## Depends on

- [Analytic function](../differentiability/analytic-function.md)

## Proof depends on

- [Principle of isolated zeros](principle-of-isolated-zeros.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/IsolatedZeros.html#AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq)
- [Source of `AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq` in Mathlib/Analysis/Analytic/IsolatedZeros.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Analytic/IsolatedZeros.lean#L229)
- [Mathlib overview: Analysis › Complex analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L370)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L393)
- [1000+ theorems list: Q1038716](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1217)
- [1000+ theorems project: Q1038716](https://1000-plus.github.io/all.html?length=-1#Q1038716)
- [Wikipedia: Identity theorem](https://en.wikipedia.org/wiki/Identity_theorem)
- [Wikidata: Q1038716](https://www.wikidata.org/wiki/Q1038716)
