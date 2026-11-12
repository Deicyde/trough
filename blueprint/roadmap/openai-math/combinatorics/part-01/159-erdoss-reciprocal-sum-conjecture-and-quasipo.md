---
declaration: section
origin: cited
---

# 159. Erdős’s reciprocal-sum conjecture and quasipolynomial Szemerédi bounds

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Erdős's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. Quantitatively, for each fixed *k* ≥ 3, every subset of $\{1,\ldots,N\}$ with no nonconstant *k*-term progression has size at most $C_kN\exp[-c_k(\log N)^{\varepsilon_k}]$, with positive constants depending only on *k*.

## Quasipolynomial Bounds for Arithmetic Progressions

We prove Erdős's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. More quantitatively, for every fixed *k* ≥ 3, we show

$\displaystyle r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr)$

with $C_k,c_k,\varepsilon_k\gt 0$, where $r_k(N)$ is the largest size of a subset of $\{1,\ldots,N\}$ with no nonconstant *k*-term arithmetic progression.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Erdős's reciprocal-sum conjecture asks whether every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. The formalization proves this statement: for every requested length, such a set contains a progression with positive common difference.

The selected theorem is the reciprocal-sum consequence. The paper's quantitative upper bound for the largest progression-free subset of $\{1,\ldots,N\}$ is outside this statement.

## Lean: Erdős's reciprocal-sum arithmetic-progression conjecture

Stated in [ErdosReciprocal.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ErdosReciprocal.lean).

```lean
theorem manuscriptReciprocalProgressionTheorem : ReciprocalProgressionTheorem
```

Its proof is in [lean/OAI/Combinatorics/Progressions/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Progressions/Main.lean) or a file it imports further down, which this chapter does not read.

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/159.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/159.md)
