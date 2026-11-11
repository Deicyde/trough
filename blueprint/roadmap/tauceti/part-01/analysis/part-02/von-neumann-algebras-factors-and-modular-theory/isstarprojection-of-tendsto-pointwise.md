---
declaration: theorem
origin: cited
lean: IsStarProjection.of_tendsto_pointwise
statement: formalized
proof: formalized
---

# IsStarProjection.of_tendsto_pointwise

A strong limit of orthogonal projections is an orthogonal projection, for arbitrary nets
and with no separability or dimension restriction.

```lean
IsStarProjection.of_tendsto_pointwise.{u_1, u_2, u_3} {𝕜 : Type u_1} {H : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H] {l : Filter ι}
  [l.NeBot] {P : ι → H →L[𝕜] H} {P₀ : H →L[𝕜] H} (hP : ∀ᶠ (i : ι) in l, IsStarProjection (P i))
  (hlim : ∀ (x : H), Filter.Tendsto (fun i => (P i) x) l (nhds (P₀ x))) : IsStarProjection P₀
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsStarProjection.of_tendsto_pointwise`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/StrongOperatorTopology.html#IsStarProjection.of_tendsto_pointwise).

## Sources

- [Tau Ceti documentation: `IsStarProjection.of_tendsto_pointwise`](https://taucetiproject.org/docs/TauCeti/Analysis/LocallyConvex/StrongOperatorTopology.html#IsStarProjection.of_tendsto_pointwise)
- [Source of `IsStarProjection.of_tendsto_pointwise` in TauCeti/Analysis/LocallyConvex/StrongOperatorTopology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/LocallyConvex/StrongOperatorTopology.lean#L100)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
