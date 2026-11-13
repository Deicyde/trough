---
declaration: section
origin: cited
lean: OAI.Problem367.free_ising_factor_iff_threshold
statement: formalized
proof: formalized
---

# 236. The exact factor-of-IID threshold for free Ising spins on trees

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Determines when the free zero-field ferromagnetic Ising state on the infinite *d*-regular tree is a factor of independent vertex labels: exactly when $\tanh\beta\le(d-1)^{-1/2}$, including equality, for *d* ≥ 3 and *β* ≥ 0. The construction uses no root and is almost surely equivariant for each fixed tree automorphism, resolving the ferromagnetic case of Lyons's question.

## The sharp factor-of-IID threshold for the free Ising model on regular trees

For every integer *d* ≥ 3 and inverse temperature *β* ≥ 0, the free zero-field ferromagnetic Ising measure on the infinite *d*-regular tree is a factor of IID exactly when $\tanh\beta\le(d-1)^{-1/2}$. We prove the positive implication, including equality, resolving the conjecture of Nam, Sly and Zhang; the strict converse is known. The spin factor can be chosen to commute with every tree automorphism on every label input.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result determines the factor-of-IID threshold for the free zero-field Ising law on the infinite $d$-regular tree. For every $d\ge3$ and $\beta\ge0$, the law is a factor of IID exactly when $\tanh\beta\le1/\sqrt{d-1}$, including equality. The factor uses independent uniform vertex labels and is almost surely equivariant for each fixed tree automorphism. Finitary coding and coding-radius bounds are not included.

## Lean: Factor-of-IID threshold for the free Ising model

```lean
theorem free_ising_factor_iff_threshold :
    ∀ (d : ℕ) (beta : ℝ), 3 ≤ d → 0 ≤ beta → (IsFactorOfIID d (Real.tanh beta) ↔ Real.tanh beta ≤ 1 / Real.sqrt ((d : ℝ) - 1))
```

Stated in [FreeIsing.lean, line 87](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FreeIsing.lean#L87). Proved in [lean/OAI/Probability/FreeIsing/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/FreeIsing/Main.lean#L21). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/236.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/236.md)
