# Lax-Milgram theorem

The Lax-Milgram equivalence of a coercive bounded bilinear operator:
for all `v : V`, `continuousLinearEquivOfBilin B v` is the unique element `V`
such that `continuousLinearEquivOfBilin B v, w⟫ = B v w`.
The Lax-Milgram theorem states that this is a continuous equivalence.

```lean
IsCoercive.continuousLinearEquivOfBilin.{u} {V : Type u} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [CompleteSpace V] {B : V →L[ℝ] V →L[ℝ] ℝ} (coercive : IsCoercive B) :
  V ≃L[ℝ] V
```

## Depends on

- [Fréchet-Riesz representation of the dual of a Hilbert space](frechet-riesz-representation-of-the-dual-of-a-hi.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `IsCoercive.continuousLinearEquivOfBilin`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/LaxMilgram.html#IsCoercive.continuousLinearEquivOfBilin)
- [Source of `IsCoercive.continuousLinearEquivOfBilin` in Mathlib/Analysis/InnerProductSpace/LaxMilgram.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/InnerProductSpace/LaxMilgram.lean#L100)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L304)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L449)
- [1000+ theorems list: Q9993851](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L4033)
- [1000+ theorems project: Q9993851](https://1000-plus.github.io/all.html?length=-1#Q9993851)
- [Wikipedia: Lax–Milgram theorem](https://en.wikipedia.org/wiki/Lax%E2%80%93Milgram_theorem)
- [Wikidata: Q9993851](https://www.wikidata.org/wiki/Q9993851)
