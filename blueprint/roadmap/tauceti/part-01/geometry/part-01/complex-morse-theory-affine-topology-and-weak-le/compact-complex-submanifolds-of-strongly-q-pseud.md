---
declaration: theorem
origin: cited
lean: TauCeti.finrank_le_of_isManifoldStronglyPseudoconvexAt
statement: formalized
proof: formalized
---

# Compact complex submanifolds of strongly `q`-pseudoconvex manifolds

A nonempty compact
complex manifold admitting a holomorphic `C²` immersion into a complex manifold that carries a real
function, `C²` and strongly `q`-pseudoconvex at every point of the image, has complex dimension at
most `q`. No properness or exhaustion hypothesis on the function is needed.

```lean
TauCeti.finrank_le_of_isManifoldStronglyPseudoconvexAt.{u_1, u_2, u_3, u_5, u_7} {E : Type u_1}
  {F : Type u_2} {H : Type u_3} {M : Type u_5} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [NormedAddCommGroup F] [NormedSpace ℂ F] [TopologicalSpace H] {I : ModelWithCorners ℂ E H}
  [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] {P : Type u_7} [TopologicalSpace P]
  [ChartedSpace F P] {u : P → ℝ} {i : M → P} [CompactSpace M] [Nonempty M] [FiniteDimensional ℂ F]
  {q : ℕ} (hpos : ∀ (x : M), TauCeti.IsManifoldStronglyPseudoconvexAt F q u (i x))
  (hu : ∀ (x : M), ContMDiffAt (modelWithCornersSelf ℝ F) (modelWithCornersSelf ℝ ℝ) 2 u (i x))
  (hi : Manifold.IsImmersion I (modelWithCornersSelf ℂ F) 2 i) : Module.finrank ℂ E ≤ q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_le_of_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/MaximumPrinciple.html#TauCeti.finrank_le_of_isManifoldStronglyPseudoconvexAt).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_le_of_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/MaximumPrinciple.html#TauCeti.finrank_le_of_isManifoldStronglyPseudoconvexAt)
- [Source of `TauCeti.finrank_le_of_isManifoldStronglyPseudoconvexAt` in TauCeti/Geometry/Manifold/Complex/MaximumPrinciple.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/MaximumPrinciple.lean#L191)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
