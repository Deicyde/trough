---
declaration: theorem
origin: cited
lean: TauCeti.exists_isManifold_transverseFiberProduct_isSmoothEmbedding
statement: formalized
proof: formalized
---

# The transverse fibre-product theorem

The actual equal-value subtype of two transverse
`C^n` maps, `n ≥ 1`, is a `C^n` manifold of dimension `dim X + dim Y - dim N` with its
subspace topology. Its inclusion is a smooth embedding, and its tangent image consists of
pairs whose images under the two differentials agree. Empty fibre products are allowed;
no separation or countability hypotheses are needed.

```lean
TauCeti.exists_isManifold_transverseFiberProduct_isSmoothEmbedding.{u_1, u_2, u_3, u_4, u_5, u_6,
    u_7, u_8, u_9}
  {EX : Type u_1} {HX : Type u_2} {X : Type u_3} {EY : Type u_4} {HY : Type u_5} {Y : Type u_6}
  {EN : Type u_7} {HN : Type u_8} {N : Type u_9} [NormedAddCommGroup EX] [NormedSpace ℝ EX]
  [TopologicalSpace HX] [NormedAddCommGroup EY] [NormedSpace ℝ EY] [TopologicalSpace HY]
  [NormedAddCommGroup EN] [NormedSpace ℝ EN] [TopologicalSpace HN] {IX : ModelWithCorners ℝ EX HX}
  {IY : ModelWithCorners ℝ EY HY} {IN : ModelWithCorners ℝ EN HN} [TopologicalSpace X]
  [ChartedSpace HX X] [TopologicalSpace Y] [ChartedSpace HY Y] [TopologicalSpace N]
  [ChartedSpace HN N] {n : WithTop ℕ∞} [IsManifold IN n N] {f : X → N} {g : Y → N}
  [IsManifold IX n X] [IsManifold IY n Y] [IX.Boundaryless] [IY.Boundaryless] [IN.Boundaryless]
  [FiniteDimensional ℝ EX] [FiniteDimensional ℝ EY] [FiniteDimensional ℝ EN] (hn : 1 ≤ n)
  (hf : ContMDiff IX IN n f) (hg : ContMDiff IY IN n g)
  (htrans :
    ∀ (p : X × Y),
      f p.1 = g p.2 →
        (↑(mfderiv% f p.1)).range ⊔
            (↑(↑(tangentSpaceCast IN (g p.2) (f p.1)) ∘SL mfderiv% g p.2)).range =
          ⊤) :
  ∃ cs,
    IsManifold
        (modelWithCornersSelf ℝ
          (Fin (Module.finrank ℝ EX + Module.finrank ℝ EY - Module.finrank ℝ EN) → ℝ))
        n { p // f p.1 = g p.2 } ∧
      Manifold.IsSmoothEmbedding
          (modelWithCornersSelf ℝ
            (Fin (Module.finrank ℝ EX + Module.finrank ℝ EY - Module.finrank ℝ EN) → ℝ))
          (IX.prod IY) n Subtype.val ∧
        ∀ (p : { p // f p.1 = g p.2 }) (v : TangentSpace (IX.prod IY) ↑p),
          v ∈ (↑(mfderiv% Subtype.val p)).range ↔
            (mfderiv% f (↑p).1) v.1 =
              (tangentSpaceCast IN (g (↑p).2) (f (↑p).1)) ((mfderiv% g (↑p).2) v.2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Homeomorph.pullbackChartedSpace](../../complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackchartedspace.md)
- [Homeomorph.pullbackDiffeomorph](../../complex-manifolds-transport-quotients-bundles-an/homeomorph-pullbackdiffeomorph.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isManifold_transverseFiberProduct_isSmoothEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberProduct/Manifold.html#TauCeti.exists_isManifold_transverseFiberProduct_isSmoothEmbedding).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isManifold_transverseFiberProduct_isSmoothEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/FiberProduct/Manifold.html#TauCeti.exists_isManifold_transverseFiberProduct_isSmoothEmbedding)
- [Source of `TauCeti.exists_isManifold_transverseFiberProduct_isSmoothEmbedding` in TauCeti/Geometry/Manifold/FiberProduct/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/FiberProduct/Manifold.lean#L82)
