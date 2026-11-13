---
declaration: section
origin: cited
lean: OAI.SmoothObstruction.main
statement: formalized
proof: formalized
---

# 152. Zero entropy does not guarantee a smooth positive-volume model

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a zero-entropy ergodic invertible transformation of a standard nonatomic probability space that is not measurably conjugate to any $C^{∞}$ diffeomorphism preserving a strictly positive smooth probability density on a compact finite-dimensional manifold. One example rules out every finite dimension.

## A zero-entropy system without a smooth positive-volume model

We construct an ergodic invertible transformation of a standard nonatomic probability space with zero Kolmogorov–Sinai entropy that has no smooth positive-volume model. More precisely, it is not measurably conjugate to any $C^{∞}$ diffeomorphism preserving a strictly positive smooth probability density on a compact finite-dimensional manifold. A single example excludes every finite dimension, including models on nonorientable manifolds and manifolds with smooth boundary.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper asks whether a measure-preserving system can be represented by a smooth diffeomorphism preserving positive smooth volume. The formalized supporting result constructs an ergodic invertible transformation of a standard nonatomic probability space with finite Kolmogorov–Sinai entropy that has no such model on any compact finite-dimensional manifold, including manifolds with smooth boundary. The comparison is measurable conjugacy after discarding null sets.

The linked statement gives finite entropy; the paper's stronger zero-entropy conclusion is outside this statement.

## Lean: Finite-entropy system without a smooth positive-volume model

```lean
theorem main :
    ∃ (X : Type) (_ : MeasurableSpace X) (μ : Measure X)
      (_ : IsProbabilityMeasure μ) (T : X ≃ᵐ X),
      StandardNonatomic μ ∧ Ergodic T μ ∧ FiniteKSEntropy μ T ∧
        ¬ HasSmoothPositiveVolumeModel μ T
```

Stated in [SmoothObstruction.lean, line 90](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SmoothObstruction.lean#L90). Proved in [lean/OAI/Dynamics/SmoothObstruction/Main.lean, line 124](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/SmoothObstruction/Main.lean#L124).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/152.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/152.md)
