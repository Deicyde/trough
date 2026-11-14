---
declaration: section
origin: cited
lean: OAI.Tingley.tingley_sphere_isometry_full
statement: formalized
proof: formalized
---

# 322. Tingley’s sphere-isometry problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves Tingley's problem: every surjective isometry between the unit spheres of nonzero real Banach spaces extends uniquely to a surjective real-linear isometry of the whole spaces. No dimension restriction is imposed, so the metric geometry of the unit sphere determines the Banach space up to linear isometry.

## A positive solution to Tingley’s problem

Every surjective isometry between the unit spheres of real Banach spaces extends uniquely to a surjective real-linear isometry, giving an affirmative solution to Tingley's problem. If distances between different radii are not preserved, we realize the positive maximal defect in a possibly enlarged pair of Banach spaces. We then align extremal chords using common supports and Darbo's fixed-point theorem and obtain a contradiction from support and convexity estimates.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Tingley's problem asks whether a surjective isometry between the unit spheres of Banach spaces extends to a linear isometry of the spaces. The formalized result gives a unique surjective real-linear isometric extension for arbitrary nonzero real Banach spaces, with no finite-dimensionality, separability, reflexivity, or convexity assumptions. For complex spaces viewed as real spaces, the conclusion is real linearity rather than complex linearity.

## Lean: Tingley's sphere-isometry extension

```lean
theorem tingley_sphere_isometry_full
    {X : Type u} {Y : Type v}
    [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
    [NormedAddCommGroup Y] [NormedSpace ℝ Y] [CompleteSpace Y]
    [Nontrivial X] [Nontrivial Y]
    (f : UnitSphere X → UnitSphere Y) (hf : Isometry f) (hs : Function.Surjective f) :
    ∃ T : X ≃ₗᵢ[ℝ] Y,
      (∀ u : UnitSphere X, T (u : X) = (f u : Y)) ∧
      T 0 = 0 ∧
      (∀ x : X, ∀ hx : x ≠ 0, T x = ‖x‖ • (f (normalize x hx) : Y)) ∧
      Function.Surjective T ∧
      (∀ L : X →ₗ[ℝ] Y, (∀ u : UnitSphere X, L (u : X) = (f u : Y)) →
        L = T.toLinearEquiv.toLinearMap)
```

Stated in [TingleySphereIsometry.lean, line 22](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TingleySphereIsometry.lean#L22). Proved in [lean/OAI/Analysis/SphereIsometry/Extension.lean, line 101](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/SphereIsometry/Extension.lean#L101). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/322.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/322.md)
