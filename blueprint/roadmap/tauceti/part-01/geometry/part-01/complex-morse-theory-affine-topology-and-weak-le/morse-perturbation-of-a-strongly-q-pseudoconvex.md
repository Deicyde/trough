---
declaration: theorem
origin: cited
lean: TauCeti.exists_isMorse_isProperMap_bddBelow_isManifoldStronglyPseudoconvexAt
statement: formalized
proof: formalized
---

# Morse perturbation of a strongly `q`-pseudoconvex exhaustion

A smooth proper bounded-below
globally strongly `q`-pseudoconvex function `f : M → ℝ` on a Hausdorff complex manifold is
approximated within `C⁰` distance `1` by a smooth proper bounded-below globally strongly
`q`-pseudoconvex Morse exhaustion whose critical points all have real Morse index at most
`dim_ℂ E + q`.

```lean
TauCeti.exists_isMorse_isProperMap_bddBelow_isManifoldStronglyPseudoconvexAt.{u, u_1} {E : Type u_1}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] [TopologicalSpace M]
  [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] [T2Space M] {q : ℕ} {f : M → ℝ}
  (hf : ContMDiff (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ ℝ) (↑⊤) f)
  (hf_prop : IsProperMap f) (hf_bdd : BddBelow (Set.range f))
  (hf_pos : ∀ (x : M), TauCeti.IsManifoldStronglyPseudoconvexAt E q f x) :
  ∃ g,
    TauCeti.IsMorse (modelWithCornersSelf ℝ E) ⇑g ∧
      IsProperMap ⇑g ∧
        BddBelow (Set.range ⇑g) ∧
          (∀ (x : M), TauCeti.IsManifoldStronglyPseudoconvexAt E q (⇑g) x) ∧
            (∀ x ∈ TauCeti.criticalPoints (modelWithCornersSelf ℝ E) ⇑g,
                TauCeti.manifoldMorseIndex (modelWithCornersSelf ℝ E) (⇑g) x ≤
                  Module.finrank ℂ E + q) ∧
              ∀ (x : M), |g x - f x| < 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [Sard's lemma in equal dimensions](../../../analysis/part-03/calculus/part-02/sards-lemma-in-equal-dimensions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isMorse_isProperMap_bddBelow_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Pseudoconvex/Morse.html#TauCeti.exists_isMorse_isProperMap_bddBelow_isManifoldStronglyPseudoconvexAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isMorse_isProperMap_bddBelow_isManifoldStronglyPseudoconvexAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Pseudoconvex/Morse.html#TauCeti.exists_isMorse_isProperMap_bddBelow_isManifoldStronglyPseudoconvexAt)
- [Source of `TauCeti.exists_isMorse_isProperMap_bddBelow_isManifoldStronglyPseudoconvexAt` in TauCeti/Geometry/Manifold/Complex/Pseudoconvex/Morse.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/Pseudoconvex/Morse.lean#L361)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
