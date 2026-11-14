---
declaration: section
origin: cited
lean: OAI.JointDickmanPaper.joint_law, OAI.JointDickmanPaper.increasing_order, OAI.JointDickmanPaper.decreasing_order
statement: formalized
proof: formalized
---

# 012. Independent largest prime factors of consecutive integers

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the Erdős–Pomerance joint Dickman conjecture: the logarithmic sizes of the largest prime factors of *n* and $n+1$ are asymptotically independent in ordinary natural density. In particular, the integers satisfying $P^+(n)\lt P^+(n+1)$ have density 1/2.

## The joint Dickman law for consecutive integers

Let $P^+(n)$ denote the largest prime factor of *n*. We prove that $\log P^+(n)/\log n$ and $\log P^+(n+1)/\log n$ are asymptotically independent in ordinary natural density, with Dickman marginals. This resolves the Erdős–Pomerance joint Dickman conjecture positively and implies that the ordering $P^+(n)\lt P^+(n+1)$ has natural density 1/2.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Let $P^+(n)$ be the largest prime factor of $n$. The formalization proves the joint Dickman law in ordinary natural density: for every $0<a,b<1$, the density of integers satisfying $P^+(n)\le n^a$ and $P^+(n+1)\le n^b$ tends to $\rho(1/a)\rho(1/b)$, where $\rho$ is the Dickman function.

It also proves that each of the orderings $P^+(n)<P^+(n+1)$ and $P^+(n+1)<P^+(n)$ has natural density $1/2$.

## Lean: Joint Dickman law and equal ordering densities for consecutive integers

```lean
theorem joint_law (a b : ℝ) (ha : 0 < a) (ha1 : a < 1) (hb : 0 < b) (hb1 : b < 1) :
    Tendsto (realDensity (fun n =>
      (n.maxPrimeFac : ℝ) ≤ (n : ℝ) ^ a ∧ ((n + 1).maxPrimeFac : ℝ) ≤ (n : ℝ) ^ b))
      atTop (𝓝 (Erdos970.NumberTheoryLean.Dickman.rho (1 / a) *
        Erdos970.NumberTheoryLean.Dickman.rho (1 / b)))
```

Stated in [JointDickman.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/JointDickman.lean#L44). Proved in [lean/OAI/NumberTheory/JointDickman/PaperMain.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/JointDickman/PaperMain.lean#L13).

```lean
theorem increasing_order :
    Tendsto (realDensity (fun n => n.maxPrimeFac < (n + 1).maxPrimeFac))
      atTop (𝓝 (1 / 2))
```

Stated in [JointDickman.lean, line 52](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/JointDickman.lean#L52). Proved in [lean/OAI/NumberTheory/JointDickman/PaperMain.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/JointDickman/PaperMain.lean#L21).

```lean
theorem decreasing_order :
    Tendsto (realDensity (fun n => (n + 1).maxPrimeFac < n.maxPrimeFac))
      atTop (𝓝 (1 / 2))
```

Stated in [JointDickman.lean, line 58](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/JointDickman.lean#L58). Proved in [lean/OAI/NumberTheory/JointDickman/PaperMain.lean, line 27](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/JointDickman/PaperMain.lean#L27).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/012.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/012.md)
