---
declaration: section
origin: cited
lean: OAI.StandardMapEntropy.main_components, OAI.StandardMapEntropy.main_entropy, OAI.StandardMapEntropy.main_entropy_complete
statement: formalized
proof: formalized
---

# 146. Positive metric entropy for the standard map

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the standard sine map on the two-dimensional torus has positive metric entropy with respect to area for every sufficiently large positive parameter. This establishes Sinai's positive-parameter-measure conjecture for the original family, with the stronger conclusion of a full parameter tail.

## Positive Metric Entropy for the Standard Map at Large Parameters

We prove that the standard sine map of the two-dimensional torus has positive metric entropy with respect to normalized area for every sufficiently large positive parameter. This gives a full parameter tail, and hence answers Sinai's positive-parameter-measure conjecture affirmatively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves Sinai's positive-entropy conjecture for the standard sine map on the two-dimensional torus in the stronger form of a full positive parameter tail. For every sufficiently large parameter, normalized area has positive metric entropy, and a positive-area set has positive largest Lyapunov exponent with the stated derivative-growth limit.

It also constructs a positive-area invariant ergodic hyperbolic component. That component splits into finitely many cyclic pieces on each of which the corresponding iterate is Bernoulli. No genericity assumption on the parameter is used.

## Lean: Positive-area hyperbolic Bernoulli component

Stated in [StandardMapComponents.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StandardMapComponents.lean).

```lean
theorem main_components : MainComponentsObligation
```

Proved in [lean/OAI/Dynamics/StandardMap/ComponentsMain.lean, line 51](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/StandardMap/ComponentsMain.lean#L51).

## Lean: Positive metric entropy for all sufficiently large parameters

Stated in [StandardMapEntropy.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StandardMapEntropy.lean).

```lean
theorem main_entropy : MainObligation
```

Proved in [lean/OAI/Dynamics/StandardMap/EntropyEndpoint.lean, line 56](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/StandardMap/EntropyEndpoint.lean#L56).

## Lean: Positive Lyapunov exponents and entropy

Stated in [StandardMapLyapunov.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StandardMapLyapunov.lean).

```lean
theorem main_entropy_complete :
    ∃ k₀ : ℝ, 0 < k₀ ∧ ∀ k : ℝ, k₀ ≤ k →
      0 < metricEntropy area (standardMap k) ∧
      PositiveLargestLyapunov k ∧
      (0 < metricEntropy area (standardMap k) ↔ PositiveLargestLyapunov k)
```

Proved in [lean/OAI/Dynamics/StandardMap/EntropyLyapunov.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/StandardMap/EntropyLyapunov.lean#L38).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/146.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/146.md)
