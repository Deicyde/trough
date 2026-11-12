---
declaration: section
origin: cited
lean: OAI.Problem356.coulomb_counterexample_and_equal_infima
statement: formalized
proof: formalized
---

# 373. Nonattainment of the three-marginal Coulomb Monge problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

An optimal three-particle Coulomb configuration need not be a deterministic function of the first particle, even for smooth identical spatial densities. The Monge and Kantorovich infima agree, but the Monge infimum is not attained. The same phenomenon occurs for every inverse-power Riesz exponent in each dimension at least two, with a suitable density in each case.

## A counterexample to the Monge ansatz for the three-marginal Coulomb cost

We construct a smooth compactly supported probability density on ℝ$^{3}$, with a smooth compactly supported square root, for which the three-marginal Coulomb transport minimum is not attained by any pair of measure-preserving Borel maps. Nevertheless, the Monge and Kantorovich infima agree: we construct preserving maps whose costs approach the Kantorovich minimum. For every *d* ≥ 2 and *s* > 0, we also construct a smooth identical marginal with the same nonattainment and equality-of-infima properties for the inverse-power interaction $\sum_{i\lt j}|x_i-x_j|^{-s}$ on ℝ$^{d}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Monge ansatz asks whether an optimal multi-marginal transport plan can be induced by maps from one marginal. For the three-marginal Coulomb cost in $\mathbb R^3$, the formalization constructs a smooth compactly supported probability density, with smooth compactly supported square root, for which no pair of measure-preserving Borel maps attains the Kantorovich minimum.

Nevertheless, the Monge and Kantorovich infima are equal: preserving maps with finite costs approach the minimum. This is the three-dimensional Coulomb result; the paper's inverse-power extensions in every dimension are outside this statement.

## Lean: Coulomb Monge nonattainment with equality of infima

Stated in [CoulombCounterexample.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoulombCounterexample.lean).

```lean
theorem coulomb_counterexample_and_equal_infima :
    ∃ rho : E3 → ℝ, HasFullCoulombConclusion rho
```

Proved in [lean/OAI/Analysis/CoulombTransport/Conclusion.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/CoulombTransport/Conclusion.lean#L7).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/373.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/373.md)
