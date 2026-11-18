---
declaration: theorem
origin: cited
lean: TauCeti.DualGraph.nonempty_iso_of_reflTransGen_of_isStable
statement: formalized
proof: formalized
---

# Stabilization is independent of the order of contractions

Any two stable graphs reached
from the same graph by stabilization steps are isomorphic. The starting graph is then in the stable
range `2g - 2 + n > 0`, since the steps preserve `g` and `n`.

```lean
TauCeti.DualGraph.nonempty_iso_of_reflTransGen_of_isStable.{u, v} {ι : Type v}
  {G : TauCeti.DualGraph ι} [Fintype ι] {H₁ H₂ : TauCeti.DualGraph ι}
  (h₁ : Relation.ReflTransGen TauCeti.DualGraph.StabilizationStep G H₁)
  (h₂ : Relation.ReflTransGen TauCeti.DualGraph.StabilizationStep G H₂) (hH₁ : H₁.IsStable)
  (hH₂ : H₂.IsStable) : Nonempty (H₁.Iso H₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DualGraph.nonempty_iso_of_reflTransGen_of_isStable`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Stabilization.html#TauCeti.DualGraph.nonempty_iso_of_reflTransGen_of_isStable).

## Sources

- [Tau Ceti documentation: `TauCeti.DualGraph.nonempty_iso_of_reflTransGen_of_isStable`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Stabilization.html#TauCeti.DualGraph.nonempty_iso_of_reflTransGen_of_isStable)
- [Source of `TauCeti.DualGraph.nonempty_iso_of_reflTransGen_of_isStable` in TauCeti/AlgebraicGeometry/Curves/DualGraph/Stabilization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Curves/DualGraph/Stabilization.lean#L613)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StableReduction/STATUS.md)
