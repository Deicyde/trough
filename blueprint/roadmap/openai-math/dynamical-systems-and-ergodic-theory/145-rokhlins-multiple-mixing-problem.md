---
declaration: section
origin: cited
lean: OAI.Rokhlin.mixing_all_finite_orders
statement: formalized
proof: formalized
---

# 145. Rokhlin’s multiple-mixing problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every invertible mixing probability-preserving transformation is mixing of all finite orders, resolving Rokhlin's multiple-mixing problem for a single transformation. Correlations among any finite collection of measurable sets converge to the product of their measures whenever all pairwise time separations diverge.

## Rokhlin's multiple-mixing problem for one transformation

Every invertible mixing probability-preserving transformation is mixing of every finite order. Thus Rokhlin's multiple-mixing problem for a single transformation has an affirmative answer.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Rokhlin's multiple-mixing problem asks whether ordinary mixing of one invertible probability-preserving transformation implies mixing of every finite order. The formalization proves this implication. For each $k\ge3$ and every $k$ measurable sets, the measure of their translated intersection tends to the product of their measures as all successive time gaps tend to infinity.

## Lean: Mixing of every finite order for one mixing transformation

```lean
theorem mixing_all_finite_orders (μ : Measure Ω) [IsProbabilityMeasure μ]
    (T : Ω ≃ᵐ Ω) (h_pres : MeasurePreserving T μ μ) (h_mix : IsMixing μ T) :
    ∀ k : ℕ, 3 ≤ k → MixingOfOrder μ T k
```

Stated in [Rokhlin.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Rokhlin.lean#L30). Proved in [lean/OAI/Dynamics/MultipleMixing/Main.lean, line 317](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/MultipleMixing/Main.lean#L317).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/145.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/145.md)
