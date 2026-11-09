---
declaration: structure
origin: cited
lean: TauCeti.IsLiouvilleDomain
statement: formalized
---

# TauCeti.IsLiouvilleDomain

A subset `W` of a manifold `M` is a **Liouville domain** for the smooth two-form `ω`, with
primitive `α`, when `ω` is nondegenerate, `dα = ω`, `W` is compact and lies in the interior of
`M`, and the Liouville field of `α` points strictly outwards along the boundary of `W`: some smooth
vector field `Z` with `ι_Z ω = α` and some continuous function `f` and value `c` satisfy
`W = {f ≤ c}`, with `f` smooth and `df(Z) > 0` at every point of the level `f⁻¹(c)`. The
nondegeneracy of `ω` makes `Z` unique, and the condition along `f⁻¹(c)` makes `c` a regular value
of `f`, so that `W` is a compact domain with smooth boundary `f⁻¹(c)`.

```lean
TauCeti.IsLiouvilleDomain.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] (ω : TauCeti.SmoothTwoForm I M)
  (α : TauCeti.SmoothForm I M ℝ 1) (W : Set M) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLiouvilleDomain`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/Domain.html#TauCeti.IsLiouvilleDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLiouvilleDomain`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/Domain.html#TauCeti.IsLiouvilleDomain)
- [Source of `TauCeti.IsLiouvilleDomain` in TauCeti/Geometry/Symplectic/Liouville/Domain.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Liouville/Domain.lean#L79)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
