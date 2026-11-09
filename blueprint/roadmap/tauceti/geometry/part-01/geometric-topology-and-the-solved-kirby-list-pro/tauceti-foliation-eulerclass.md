---
declaration: def
origin: cited
lean: TauCeti.Foliation.eulerClass
statement: formalized
---

# TauCeti.Foliation.eulerClass

The Euler class `Hᵏ(TF, TF₀) ⟶ Hᵏ(M)` of the tangent field of a foliation of rank `k`:
`TauCeti.eulerClass`, restriction to the total space followed by pullback along the zero
section, read in degree `k`.

```lean
TauCeti.Foliation.eulerClass.{w, v, u, u_1, u_2} {E : Type w} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_1} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {n : WithTop ℕ∞} {M : Type w} [TopologicalSpace M] [ChartedSpace H M] {k : ℕ}
  [IsManifold I (n + 1) M] (F : TauCeti.Foliation I n M k) {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Limits.HasCoproducts C]
  [CategoryTheory.Abelian C] (R : C) (K : Type u_2) [Ring K] [CategoryTheory.Linear K C] (N : C) :
  F.thomPair.singularCohomology R K N (Module.finrank ℝ (Fin k → ℝ)) ⟶
    TopCat.singularCohomology R K N (↧M) k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Foliation.eulerClass`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Foliation/EulerClass.html#TauCeti.Foliation.eulerClass).

## Sources

- [Tau Ceti documentation: `TauCeti.Foliation.eulerClass`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Foliation/EulerClass.html#TauCeti.Foliation.eulerClass)
- [Source of `TauCeti.Foliation.eulerClass` in TauCeti/Geometry/Manifold/Foliation/EulerClass.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Foliation/EulerClass.lean#L119)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
