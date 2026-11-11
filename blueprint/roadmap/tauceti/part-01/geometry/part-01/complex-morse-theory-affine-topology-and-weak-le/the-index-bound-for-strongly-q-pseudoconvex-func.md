---
declaration: theorem
origin: cited
lean: TauCeti.IsManifoldStronglyPseudoconvexAt.manifoldMorseIndex_le
statement: formalized
proof: formalized
---

# The index bound for strongly `q`-pseudoconvex functions on a complex manifold

At a
critical point `x` of a function `f` which is `C²` at `x` and strongly `q`-pseudoconvex at `x`, the
Morse index of `f` is at most `dim_ℂ E + q`.

```lean
TauCeti.IsManifoldStronglyPseudoconvexAt.manifoldMorseIndex_le.{u_1, u_2} {E : Type u_1}
  {M : Type u_2} [NormedAddCommGroup E] [NormedSpace ℂ E] [TopologicalSpace M] [ChartedSpace E M]
  {f : M → ℝ} {x : M} [FiniteDimensional ℂ E] [IsManifold (modelWithCornersSelf ℂ E) 2 M] {q : ℕ}
  (h : TauCeti.IsManifoldStronglyPseudoconvexAt E q f x)
  (hf : ContMDiffAt (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ ℝ) 2 f x)
  (hcrit : d% f x = 0) :
  TauCeti.manifoldMorseIndex (modelWithCornersSelf ℝ E) f x ≤ Module.finrank ℂ E + q
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [The Morse index bound `λ ≤ n`](../../../analysis/part-02/complex/part-03/the-morse-index-bound-n.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsManifoldStronglyPseudoconvexAt.manifoldMorseIndex_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/LeviForm.html#TauCeti.IsManifoldStronglyPseudoconvexAt.manifoldMorseIndex_le).

## Sources

- [Tau Ceti documentation: `TauCeti.IsManifoldStronglyPseudoconvexAt.manifoldMorseIndex_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/LeviForm.html#TauCeti.IsManifoldStronglyPseudoconvexAt.manifoldMorseIndex_le)
- [Source of `TauCeti.IsManifoldStronglyPseudoconvexAt.manifoldMorseIndex_le` in TauCeti/Geometry/Manifold/Complex/LeviForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/LeviForm.lean#L620)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
