---
declaration: section
origin: cited
lean: OAI.ThreeManifold.main_theorem
statement: formalized
proof: formalized
---

# 358. A three-manifold without conjugate points or nonpositive curvature

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a closed connected orientable smooth three-manifold that admits a metric without conjugate points but no metric of nonpositive sectional curvature. This answers negatively, already in dimension three, whether the first metric-existence property implies the second.

## A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric

We construct a closed connected orientable smooth three-manifold that admits a smooth Riemannian metric without conjugate points but admits no smooth Riemannian metric of nonpositive sectional curvature.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result separates absence of conjugate points from nonpositive sectional curvature. It constructs a closed connected orientable smooth three-manifold with a smooth Riemannian metric having no conjugate points, while the same manifold admits no smooth metric of everywhere nonpositive sectional curvature. The no-conjugate-points assertion ranges over all geodesics and tangent-bundle Jacobi fields, including constant geodesics and unbounded time intervals. The separate no-focal-points and CAT(0) consequences are not included.

## Lean: No conjugate points without a nonpositively curved metric

Stated in [ConjugatePoints.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ConjugatePoints.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_theorem : MainStatement
```

Proved in [lean/OAI/Geometry/ConjugatePoints/ThreeManifold.lean, line 260](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/ConjugatePoints/ThreeManifold.lean#L260).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/358.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/358.md)
