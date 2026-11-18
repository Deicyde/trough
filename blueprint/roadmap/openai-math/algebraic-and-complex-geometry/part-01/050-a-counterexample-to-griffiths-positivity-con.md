---
declaration: section
origin: cited
lean: OAI.QuadricCounterexample.main_theorem
statement: formalized
proof: formalized
---

# 050. A counterexample to Griffiths’ positivity conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs ample rank-two bundles on $\mathbb P^1\times\mathbb P^1$ with no smooth Hermitian metric of strictly Griffiths-positive curvature, disproving Griffiths' positivity conjecture already on the quadric surface.

## Ample rank-two bundles on the quadric surface without Griffiths-positive metrics

We give counterexamples to Griffiths' conjecture in rank two on the quadric surface $\mathbb P^1\times\mathbb P^1$. We construct an explicit bundle *G* whose coordinatewise power pullbacks, tensored with $\mathcal O(1,1)$, are ample for every positive power, but admit no smooth strictly Griffiths-positive Hermitian metric for all sufficiently large powers.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Griffiths' positivity conjecture predicts that every ample holomorphic vector bundle on a smooth complex projective variety admits a smooth Hermitian metric with strictly Griffiths-positive curvature. The formalized counterexample starts with a rank-two algebraic bundle $G$ on $\mathbb P^1\times\mathbb P^1$. Its coordinatewise power pullbacks, tensored with $\mathcal O(1,1)$, are ample for every positive power but admit no such metric for all sufficiently large powers.

The separate very-ampleness result for all admissible even exponents is not included.

## Lean: Ample bundles without Griffiths-positive metrics

```lean
theorem main_theorem : SourceMainTheorem
```

Stated in [QuadricBundles.lean, line 174](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/QuadricBundles.lean#L174). Proved in [lean/OAI/Geometry/QuadricBundles/Main.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/QuadricBundles/Main.lean#L10). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/050.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/050.md)
