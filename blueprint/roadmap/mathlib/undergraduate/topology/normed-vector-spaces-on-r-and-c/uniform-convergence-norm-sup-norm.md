# Uniform convergence norm (sup-norm)

Expressing uniform convergence on a set using `edist`.

```lean
EMetric.tendstoUniformlyOn_iff.{u, v, u_2} {γ : Type u} {β : Type v} [PseudoEMetricSpace γ]
  {ι : Type u_2} {F : ι → β → γ} {f : β → γ} {p : Filter ι} {s : Set β} :
  TendstoUniformlyOn F f p s ↔ ∀ ε > 0, ∀ᶠ (n : ι) in p, ∀ x ∈ s, edist (f x) (F n x) < ε
```

## Depends on

- [Real number](../../../overview/general-algebra/numbers/real-number.md)

## Sources

- [Mathlib documentation: `EMetric.tendstoUniformlyOn_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/EMetricSpace/Basic.html#EMetric.tendstoUniformlyOn_iff)
- [Source of `EMetric.tendstoUniformlyOn_iff` in Mathlib/Topology/EMetricSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/EMetricSpace/Basic.lean#L123)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L431)
