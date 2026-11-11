---
declaration: structure
origin: cited
lean: TauCeti.IsLiouvilleCompletion
statement: formalized
---

# TauCeti.IsLiouvilleCompletion

A manifold `M` is a **completion** of the Liouville domain `W ⊆ M`, for the form `ω` with
primitive `α`, when the Liouville field `Z` of `α`, the vector field with `ι_Z ω = α`, is complete
and its flow carries every point of `M` into `W` in some time. Then `M` is the union of `W` and of
the forward flow-out of its boundary, a cylindrical end
(`TauCeti.IsLiouvilleCompletion.existsUnique_flowOf_eq`).

```lean
TauCeti.IsLiouvilleCompletion.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] (ω : TauCeti.SmoothTwoForm I M)
  (α : TauCeti.SmoothForm I M ℝ 1) (W : Set M) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLiouvilleCompletion`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/Completion.html#TauCeti.IsLiouvilleCompletion).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLiouvilleCompletion`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/Completion.html#TauCeti.IsLiouvilleCompletion)
- [Source of `TauCeti.IsLiouvilleCompletion` in TauCeti/Geometry/Symplectic/Liouville/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Liouville/Completion.lean#L178)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)
