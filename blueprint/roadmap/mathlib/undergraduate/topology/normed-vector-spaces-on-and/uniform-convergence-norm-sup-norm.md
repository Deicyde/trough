---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: EMetric.tendstoUniformlyOn_iff
mathlib_file: Mathlib/Topology/EMetricSpace/Basic.lean
---

# Uniform convergence norm (sup-norm)

Expressing uniform convergence on a set using `edist`.

```lean
EMetric.tendstoUniformlyOn_iff.{u, v, u_2} {γ : Type u} {β : Type v} [PseudoEMetricSpace γ]
  {ι : Type u_2} {F : ι → β → γ} {f : β → γ} {p : Filter ι} {s : Set β} :
  TendstoUniformlyOn F f p s ↔ ∀ ε > 0, ∀ᶠ (n : ι) in p, ∀ x ∈ s, edist (f x) (F n x) < ε
```

## Depends on

- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Real number](../../../overview/general-algebra/numbers/real-number.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Invertible elements](../../ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Order](../../single-variable-real-analysis/real-numbers/order.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../ring-theory/fundamentals/product-of-rings.md)
- [Ring morphism](../../../overview/general-algebra/rings/ring-morphism.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure.md)

## Sources

- [Mathlib documentation: `EMetric.tendstoUniformlyOn_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/EMetricSpace/Basic.html#EMetric.tendstoUniformlyOn_iff)
- [Source of `EMetric.tendstoUniformlyOn_iff` in Mathlib/Topology/EMetricSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/EMetricSpace/Basic.lean#L123)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L431)
