---
declaration: theorem
origin: cited
lean: TauCeti.isSubmersion_fst_transverseFiberProduct
statement: formalized
proof: formalized
---

# TauCeti.isSubmersion_fst_transverseFiberProduct

Base change preserves submersions: the first projection of the transverse fibre product
is a submersion if the map from the second factor is a submersion.

```lean
TauCeti.isSubmersion_fst_transverseFiberProduct.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9}
  {EX : Type u_1} {HX : Type u_2} {X : Type u_3} {EY : Type u_4} {HY : Type u_5} {Y : Type u_6}
  {EN : Type u_7} {HN : Type u_8} {N : Type u_9} [NormedAddCommGroup EX] [NormedSpace ℝ EX]
  [TopologicalSpace HX] [NormedAddCommGroup EY] [NormedSpace ℝ EY] [TopologicalSpace HY]
  [NormedAddCommGroup EN] [NormedSpace ℝ EN] [TopologicalSpace HN] {IX : ModelWithCorners ℝ EX HX}
  {IY : ModelWithCorners ℝ EY HY} {IN : ModelWithCorners ℝ EN HN} [TopologicalSpace X]
  [ChartedSpace HX X] [TopologicalSpace Y] [ChartedSpace HY Y] [TopologicalSpace N]
  [ChartedSpace HN N] {n : WithTop ℕ∞} [IsManifold IX n X] [IsManifold IY n Y] [IsManifold IN n N]
  [IX.Boundaryless] [IY.Boundaryless] [IN.Boundaryless] [FiniteDimensional ℝ EX]
  [FiniteDimensional ℝ EY] [FiniteDimensional ℝ EN] {f : X → N} {g : Y → N} (hn : 1 ≤ n)
  (hf : ContMDiff IX IN n f) (hg : ContMDiff IY IN n g)
  (htrans :
    ∀ (p : X × Y),
      f p.1 = g p.2 →
        (↑(mfderiv% f p.1)).range ⊔
            (↑(↑(tangentSpaceCast IN (g p.2) (f p.1)) ∘SL mfderiv% g p.2)).range =
          ⊤)
  (hgs : Manifold.IsSubmersion IY IN n g) :
  Manifold.IsSubmersion
    (modelWithCornersSelf ℝ
      (Fin (Module.finrank ℝ EX + Module.finrank ℝ EY - Module.finrank ℝ EN) → ℝ))
    IX n fun p => (↑p).1
```

## Depends on

- [The transverse fibre-product theorem](the-transverse-fibre-product-theorem.md)

## Proof depends on

- [The inverse function theorem for manifolds](../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isSubmersion_fst_transverseFiberProduct`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberProduct/Submersion.html#TauCeti.isSubmersion_fst_transverseFiberProduct).

## Sources

- [Tau Ceti documentation: `TauCeti.isSubmersion_fst_transverseFiberProduct`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberProduct/Submersion.html#TauCeti.isSubmersion_fst_transverseFiberProduct)
- [Source of `TauCeti.isSubmersion_fst_transverseFiberProduct` in TauCeti/Geometry/Manifold/FiberProduct/Submersion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/FiberProduct/Submersion.lean#L122)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
