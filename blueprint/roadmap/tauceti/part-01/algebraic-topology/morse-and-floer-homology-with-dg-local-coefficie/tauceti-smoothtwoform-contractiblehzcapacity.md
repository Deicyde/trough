---
declaration: def
origin: cited
lean: TauCeti.SmoothTwoForm.contractibleHZCapacity
statement: formalized
---

# TauCeti.SmoothTwoForm.contractibleHZCapacity

The **`π₁`-sensitive Hofer–Zehnder capacity** `c°_HZ(W)` of a subset `W` of a manifold with a
two-form `σ`: the supremum, in `[0, ∞]`, of the maxima of the `HZ°`-admissible Hamiltonians
(`TauCeti.SmoothTwoForm.IsContractibleHZAdmissible`).

```lean
TauCeti.SmoothTwoForm.contractibleHZCapacity.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] (W : Set M)
  [IsManifold I (↑⊤) M] (σ : TauCeti.SmoothTwoForm I M) : ENNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.contractibleHZCapacity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Capacity/HoferZehnder.html#TauCeti.SmoothTwoForm.contractibleHZCapacity).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.contractibleHZCapacity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Capacity/HoferZehnder.html#TauCeti.SmoothTwoForm.contractibleHZCapacity)
- [Source of `TauCeti.SmoothTwoForm.contractibleHZCapacity` in TauCeti/Geometry/Symplectic/Capacity/HoferZehnder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Capacity/HoferZehnder.lean#L190)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
