---
declaration: theorem
origin: cited
lean: TauCeti.HomologicalOrientation.abs_mul_simplicialVolume_le
statement: formalized
proof: formalized
---

# The degree inequality for the simplicial volume

If `f : M → N` carries the fundamental
class of `M` to `d` times the fundamental class of `N`, then `|d| * ‖N‖ ≤ ‖M‖`.

```lean
TauCeti.HomologicalOrientation.abs_mul_simplicialVolume_le {M E : Type} [TopologicalSpace M]
  [T2Space M] [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [ChartedSpace E M]
  {n : ℕ} (o : TauCeti.HomologicalOrientation M E n) (hn : Module.finrank ℝ E = n) [CompactSpace M]
  {N E' : Type} [TopologicalSpace N] [T2Space N] [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [FiniteDimensional ℝ E'] [ChartedSpace E' N] (o' : TauCeti.HomologicalOrientation N E' n)
  (hn' : Module.finrank ℝ E' = n) [CompactSpace N] (f : C(M, N)) {d : ℤ}
  (hf : o.mapFundamentalClass hn f = d • o'.fundamentalClass hn') :
  |↑d| * o'.simplicialVolume hn' ≤ o.simplicialVolume hn
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.abs_mul_simplicialVolume_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/LocalHomology/SimplicialVolume.html#TauCeti.HomologicalOrientation.abs_mul_simplicialVolume_le).

## Sources

- [Tau Ceti documentation: `TauCeti.HomologicalOrientation.abs_mul_simplicialVolume_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/LocalHomology/SimplicialVolume.html#TauCeti.HomologicalOrientation.abs_mul_simplicialVolume_le)
- [Source of `TauCeti.HomologicalOrientation.abs_mul_simplicialVolume_le` in TauCeti/AlgebraicTopology/Singular/LocalHomology/SimplicialVolume.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/LocalHomology/SimplicialVolume.lean#L124)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricTopology/STATUS.md)
