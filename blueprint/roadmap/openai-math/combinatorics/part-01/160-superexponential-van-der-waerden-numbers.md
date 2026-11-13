---
declaration: section
origin: cited
lean: OAI.QuantitativeVanDerWaerden.uniform_lower_bound
statement: formalized
proof: formalized
---

# 160. Superexponential van der Waerden numbers

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves Erdős's superexponential-growth question for van der Waerden numbers. If $W_r(k)$ is the least interval length forcing a monochromatic *k*-term progression in every *r*-coloring, then $W_r(k)\gt k^{ck\lfloor\log_2 r\rfloor}$ for an absolute *c* > 0, all *r* ≥ 2 and sufficiently large *k*, uniformly in *r*. In particular, $W_r(k)^{1/k}\to\infty$ for each fixed *r*.

## Quantitative Superexponential Bounds for van der Waerden Numbers

We prove that there are absolute constants *c* > 0 and $K_{0}$ such that $W_r(k)\gt k^{ck\lfloor\log_2 r\rfloor}$ for every $k\ge K_0$ and *r* ≥ 2. Consequently $W_r(k)^{1/k}\to\infty$ for each fixed *r* ≥ 2, giving a quantitative positive resolution of Erdős's superexponential-growth question, including the two-color case.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Let $W(r,k)$ be the least interval length forcing a monochromatic $k$-term arithmetic progression in every coloring with at most $r$ colors. The formalized result gives an absolute threshold $K$ such that $W(r,k)>k^{k\lfloor\log_2 r\rfloor/100000}$ for all $k\ge K$ and $r\ge2$. It also establishes the associated growth limits, finiteness, and boundary values. The sharper intermediate estimates used in the paper are not part of the described formalization.

## Lean: Uniform van der Waerden lower bound

```lean
theorem uniform_lower_bound :
    ∃ K : ℕ, ∀ k ≥ K, ∀ r ≥ 2,
      (k : ℝ) ^ ((1 / 100000 : ℝ) * k * (Nat.log 2 r : ℝ)) < (W r k : ℝ)
```

Stated in [QuantitativeVanDerWaerden.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/QuantitativeVanDerWaerden.lean#L26). Proved in [lean/OAI/Combinatorics/ProgressionColoring/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ProgressionColoring/Main.lean#L12). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/160.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/160.md)
