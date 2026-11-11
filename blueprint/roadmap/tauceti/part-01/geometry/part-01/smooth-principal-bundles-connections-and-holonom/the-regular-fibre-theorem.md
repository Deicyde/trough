---
declaration: theorem
origin: cited
lean: TauCeti.exists_regularFiber_smoothEmbedding
statement: formalized
proof: formalized
---

# The regular-fibre theorem

A regular fibre over an interior value of a `C^m` map,
`m ≥ 1`, from a finite-dimensional boundaryless real manifold to a finite-dimensional real
manifold admits a `C^m` manifold structure of dimension `dim M - dim N`, with its subspace
topology, for which the inclusion is a `C^m` smooth embedding and has tangent image `ker df`.
No separation or countability assumptions are needed, and an empty fibre is allowed.

```lean
TauCeti.exists_regularFiber_smoothEmbedding.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} {F : Type u_4} {G : Type u_5} {N : Type u_6} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [I.Boundaryless] {m : WithTop ℕ∞} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I m M]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] [TopologicalSpace G]
  {J : ModelWithCorners ℝ F G} [TopologicalSpace N] [ChartedSpace G N] [IsManifold J m N]
  {f : M → N} {c : N} (hm : 1 ≤ m) (hf : ContMDiff I J m f) (hc : J.IsInteriorPoint c)
  (hreg : TauCeti.IsRegularValue I J f c) :
  ∃ a,
    IsManifold (modelWithCornersSelf ℝ (Fin (Module.finrank ℝ E - Module.finrank ℝ F) → ℝ)) m
        { x // f x = c } ∧
      Manifold.IsSmoothEmbedding
          (modelWithCornersSelf ℝ (Fin (Module.finrank ℝ E - Module.finrank ℝ F) → ℝ)) I m
          Subtype.val ∧
        ∀ (z : { x // f x = c }), (↑(mfderiv% Subtype.val z)).range = (↑(mfderiv% f ↑z)).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_regularFiber_smoothEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/RegularValue/ManifoldLevel.html#TauCeti.exists_regularFiber_smoothEmbedding).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_regularFiber_smoothEmbedding`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/RegularValue/ManifoldLevel.html#TauCeti.exists_regularFiber_smoothEmbedding)
- [Source of `TauCeti.exists_regularFiber_smoothEmbedding` in TauCeti/Geometry/Manifold/RegularValue/ManifoldLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/RegularValue/ManifoldLevel.lean#L249)
- [Tau Ceti roadmap status: Smooth principal bundles, connections, and holonomy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SmoothBundlesConnections/STATUS.md)
