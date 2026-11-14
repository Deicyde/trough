---
declaration: section
origin: cited
lean: OAI.DiscreteFree.real_l1_quantitative_renorming, OAI.DiscreteFree.source_endpoints
statement: formalized
proof: formalized
---

# 330. A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a countable uniformly discrete metric space whose real Lipschitz-free Banach space has the approximation property but not the bounded approximation property, answering Kalton's question negatively. Finite-rank operators approximate the identity on every compact set, but their norms cannot share a finite bound.

## A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces

We construct a countable uniformly discrete metric space whose real Lipschitz-free space has the approximation property but fails the bounded approximation property, answering Kalton's question negatively. The identity can be approximated on every compact set by finite-rank operators, but no uniform bound on their norms is possible.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

Kalton's question asks whether uniform discreteness of a metric space forces its Lipschitz-free space to have the bounded approximation property. The formalization constructs a countable metric space with all distinct points at distance at least one whose real Lipschitz-free space has the approximation property but fails every bounded approximation bound. The metric space is unbounded and not proper.

The earlier quantitative renorming result for real $\ell_1$ is retained: for each integer $p\ge1$, an equivalent complete norm has the $2B_p$-bounded approximation property but fails the $p$-bounded approximation property, where $B_p=300p^2+150p+5$.

## Lean: Quantitative renorming of real $\ell_1$

```lean
theorem real_l1_quantitative_renorming : RealL1RenormingStatement
```

Stated in [RealL1Renorming.lean, line 48](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RealL1Renorming.lean#L48). Proved in [lean/OAI/Analysis/LipschitzFree/Renorming.lean, line 41](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LipschitzFree/Renorming.lean#L41).

## Lean: Uniformly discrete Lipschitz-free space with AP but no BAP

```lean
theorem source_endpoints : BlockStatement ∧ MainStatement
```

Stated in [DiscreteLipschitzFree.lean, line 156](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DiscreteLipschitzFree.lean#L156). Proved in [lean/OAI/Analysis/LipschitzFree/Main.lean, line 92](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/LipschitzFree/Main.lean#L92).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/330.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/330.md)
