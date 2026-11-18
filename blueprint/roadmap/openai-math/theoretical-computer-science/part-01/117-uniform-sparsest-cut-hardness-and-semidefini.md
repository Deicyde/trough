---
declaration: section
origin: cited
lean: OAI.UniformSparsestCut.mainGap
statement: formalized
proof: formalized
---

# 117. Uniform sparsest cut: hardness and semidefinite gaps

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that approximating Uniform Sparsest Cut within any fixed constant factor is NP-hard, even with nonnegative rational capacities and unit demands. The Goemans–Linial semidefinite relaxation also has integrality gaps of order at least $\sqrt{\log n}/(\log\log n)^3$, approaching the square-root-logarithmic upper bound.

## Constant-factor hardness of uniform sparsest cut

We prove that, for every fixed *C* > 1, approximating Uniform Sparsest Cut within factor *C* is NP-hard. The output graphs have nonnegative rational capacities and unit demand between every pair of distinct vertices.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026/Constant-factor-hardness-of-uniform-sparsest-cut-September-24-2026.pdf).

## Near-square-root logarithmic integrality gaps for uniform sparsest cut

We construct uniform sparsest-cut instances whose Goemans–Linial semidefinite integrality gap is at least $c\sqrt{\log n}/(\log\log n)^3$ along a sequence $n\to\infty$. The demand is one between every pair of distinct vertices, and the capacities are nonnegative real numbers. This matches the Arora–Rao–Vazirani upper bound up to a power of $\log\log n$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026/Near-square-root-logarithmic-integrality-gaps-for-uniform-sparsest-cut-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives integrality gaps for the Goemans–Linial relaxation of uniform sparsest cut. Along a sequence of instance sizes $n\to\infty$, the ratio of the integral optimum to the positive relaxation optimum is at least $c\sqrt{\log n}/(\log\log n)^3$ for one absolute $c>0$. Every unordered pair has unit demand, and the relaxation uses squared Euclidean distances satisfying the triangle inequalities. The result is an existential sequence, not a bound for every size or a computational hardness theorem.

## Lean: Uniform sparsest-cut integrality gaps

```lean
theorem mainGap :
    ∃ c : ℝ, 0 < c ∧
      ∃ n : ℕ → ℕ, ∃ C : (j : ℕ) → Capacity (n j),
        (∀ j, 2 ≤ n j) ∧
        Tendsto n atTop atTop ∧
        (∀ j, 0 < glValue (C j)) ∧
        ∀ᶠ j in atTop,
          c * Real.sqrt (Real.log (n j : ℝ)) / (Real.log (Real.log (n j : ℝ))) ^ 3 ≤
            OPT (C j) / glValue (C j)
```

Stated in [UniformSparsestCut.lean, line 40](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniformSparsestCut.lean#L40). Proved in [lean/OAI/Combinatorics/SparsestCut/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/SparsestCut/Main.lean#L14). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/117.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/117.md)
