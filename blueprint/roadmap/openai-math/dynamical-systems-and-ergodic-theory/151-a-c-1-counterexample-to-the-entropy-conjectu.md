---
declaration: section
origin: cited
lean: OAI.Problem340.exists_C1_entropy_counterexample
statement: formalized
proof: formalized
---

# 151. A $C^{1}$ counterexample to the entropy conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a noninvertible $C^{1}$ self-map of a compact smooth manifold with zero topological entropy but eigenvalue 2 on second homology. This disproves the homological entropy lower bound for general $C^{1}$ self-maps: homological growth need not force positive orbit complexity.

## A C^1 Counterexample to the Entropy Conjecture

We disprove the general $C^{1}$ self-map formulation of Shub's entropy conjecture. We construct a noninvertible $C^{1}$ self-map of a compact smooth manifold without boundary whose topological entropy is zero, while its action on second real homology has eigenvalue 2. Thus the topological entropy is strictly smaller than the logarithm of the homological spectral radius.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

Shub's entropy conjecture predicts that a smooth self-map's topological entropy is at least the logarithm of the spectral radius of its action on real homology. The formalization gives a counterexample to the general $C^1$ self-map version: a noninvertible $C^1$ map on a compact smooth manifold without boundary has topological entropy zero, while its action on second real homology has a nonzero eigenvector with eigenvalue $2$. Thus the homological lower bound is strictly positive and fails for this map.

## Lean: A $C^1$ counterexample to the entropy conjecture

Stated in [C1EntropyCounterexample.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/C1EntropyCounterexample.lean).

```lean
theorem exists_C1_entropy_counterexample :
    ∃ q : ℕ, 0 < q ∧ ∃ f : CounterexampleManifold q → CounterexampleManifold q, ∃ hf : IsC1SelfMap q f, Dynamics.coverEntropy f (Set.univ : Set (CounterexampleManifold q)) = (0 : EReal) ∧ (∃ v : RealSingularHomology 2 (CounterexampleManifold q), v ≠ 0 ∧ realHomologyMap 2 f hf.1 v = (2 : ℝ) • v) ∧ 0 < Real.log (2 : ℝ) ∧ Real.log (2 : ℝ) ≤ Real.log (totalRealHomologySpectralRadius f hf.1) ∧ ¬ Function.Bijective f ∧ 5 ≤ 2 * q + 3
```

Proved in [lean/OAI/Dynamics/EntropyCounterexample/Counterexample.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/EntropyCounterexample/Counterexample.lean#L10).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/151.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/151.md)
