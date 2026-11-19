---
declaration: theorem
origin: cited
lean: Convex.forall_mem_posTangentConeAt_iff_forall_mapsTo_Icc
statement: formalized
proof: formalized
---

# Nagumo's criterion

For a closed convex set `K` in a real Hilbert space and an autonomous
locally Lipschitz field `v`, every solution of `x' = v(x)` which starts in `K` stays in `K` if and
only if `v y` is a positive tangent vector of `K` at every `y ∈ K`.

```lean
Convex.forall_mem_posTangentConeAt_iff_forall_mapsTo_Icc.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [CompleteSpace E] {K : Set E} (hKc : Convex ℝ K) (hK : IsClosed K)
  {v : E → E} (hv : LocallyLipschitz v) :
  (∀ y ∈ K, v y ∈ posTangentConeAt K y) ↔
    ∀ (x : ℝ → E) (a b : ℝ),
      ContinuousOn x (Set.Icc a b) →
        (∀ t ∈ Set.Ico a b, HasDerivWithinAt x (v (x t)) (Set.Ici t) t) →
          x a ∈ K → Set.MapsTo x (Set.Icc a b) K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Invariance of a convex set under an ODE, tangent cone form](invariance-of-a-convex-set-under-an-ode-tangent.md)
- [Picard–Lindelöf for a locally Lipschitz field](../../part-04/ode/picard-lindelof-for-a-locally-lipschitz-field.md)

## Lean

Formalized in Tau Ceti as [`Convex.forall_mem_posTangentConeAt_iff_forall_mapsTo_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/ConvexInvariance.html#Convex.forall_mem_posTangentConeAt_iff_forall_mapsTo_Icc).

## Sources

- [Tau Ceti documentation: `Convex.forall_mem_posTangentConeAt_iff_forall_mapsTo_Icc`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/ConvexInvariance.html#Convex.forall_mem_posTangentConeAt_iff_forall_mapsTo_Icc)
- [Source of `Convex.forall_mem_posTangentConeAt_iff_forall_mapsTo_Icc` in TauCeti/Analysis/ODE/ConvexInvariance.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/ODE/ConvexInvariance.lean#L185)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
