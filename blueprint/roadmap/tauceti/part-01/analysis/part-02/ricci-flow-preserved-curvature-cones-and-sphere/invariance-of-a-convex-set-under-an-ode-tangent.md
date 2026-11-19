---
declaration: theorem
origin: cited
lean: Convex.mapsTo_Icc_of_mem_posTangentConeAt
statement: formalized
proof: formalized
---

# Invariance of a convex set under an ODE, tangent cone form

A solution of `x' = v(t, x)`
on `[a, b]` which starts in a complete convex set `K` stays in `K`, provided `v t y` is a positive
tangent vector of `K` at every `y ∈ K` and the field is Lipschitz in space near the trajectory,
locally uniformly in later times.

```lean
Convex.mapsTo_Icc_of_mem_posTangentConeAt.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {K : Set E} (hKc : Convex ℝ K) (hK : IsComplete K) {v : ℝ → E → E}
  {x : ℝ → E} {a b : ℝ} (hx : ContinuousOn x (Set.Icc a b))
  (hx' : ∀ t ∈ Set.Ico a b, HasDerivWithinAt x (v t (x t)) (Set.Ici t) t)
  (hv :
    ∀ t ∈ Set.Ico a b,
      ∃ L, ∃ U ∈ nhds (x t), ∀ᶠ (τ : ℝ) in nhdsWithin t (Set.Ici t), LipschitzOnWith L (v τ) U)
  (hvK : ∀ t ∈ Set.Ico a b, ∀ y ∈ K, v t y ∈ posTangentConeAt K y) (ha : x a ∈ K) :
  Set.MapsTo x (Set.Icc a b) K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Convex.mapsTo_Icc_of_mem_posTangentConeAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/ConvexInvariance.html#Convex.mapsTo_Icc_of_mem_posTangentConeAt).

## Sources

- [Tau Ceti documentation: `Convex.mapsTo_Icc_of_mem_posTangentConeAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/ConvexInvariance.html#Convex.mapsTo_Icc_of_mem_posTangentConeAt)
- [Source of `Convex.mapsTo_Icc_of_mem_posTangentConeAt` in TauCeti/Analysis/ODE/ConvexInvariance.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/ODE/ConvexInvariance.lean#L171)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
