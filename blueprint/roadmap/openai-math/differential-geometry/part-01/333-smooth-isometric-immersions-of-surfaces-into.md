---
declaration: section
origin: cited
lean: OAI.ClosedSurfaceR4.FiniteOrderSmoothing.smooth_isometric_immersion
statement: formalized
proof: formalized
---

# 333. Smooth isometric immersions of surfaces into ℝ$^{4}$

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Every closed smooth Riemannian surface admits a smooth isometric immersion into ℝ$^{4}$, resolving the closed-surface form of the four-dimensional isometric-immersion problem. This includes nonorientable surfaces and metrics of arbitrary Gaussian curvature.

## Smooth isometric immersions of closed surfaces into Euclidean four-space

Every closed smooth Riemannian surface admits a smooth isometric immersion into Euclidean four-space, without an orientability assumption. This resolves the closed-surface form of the classical four-dimensional isometric-immersion problem.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Smooth-isometric-immersions-of-closed-surfaces-into-Euclidean-four-space-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves that every closed smooth Riemannian surface admits a smooth isometric immersion into $\mathbb R^4$. The differential preserves the Riemannian inner product on every tangent space. No orientability assumption is imposed, and the statement asks for an immersion rather than an embedding.

## Lean: Smooth isometric immersion of every closed surface into four-space

```lean
theorem smooth_isometric_immersion (g : SmoothMetric M) :
    ∃ F : M → Space, IsSmoothIsometricImmersion M g F
```

Stated in [SurfaceImmersion.lean, line 40](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SurfaceImmersion.lean#L40). Proved in [lean/OAI/Geometry/SurfaceImmersion/Main.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/SurfaceImmersion/Main.lean#L16).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/333.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/333.md)
