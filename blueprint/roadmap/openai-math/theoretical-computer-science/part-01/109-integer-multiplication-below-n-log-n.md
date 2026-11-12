---
declaration: section
origin: cited
---

# 109. Integer multiplication below $n\log n$

1 manuscript, with no Lean, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Multiplies two *n*-bit integers exactly at every input length in deterministic worst-case time $O(n(\log n)^{1-\kappa})$, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with finitely many one-dimensional tapes. This disproves the Schönhage–Strassen $n\log n$ optimality conjecture in the ordinary multitape bit model.

## Integer multiplication below n log n

We give a deterministic algorithm that multiplies two *n*-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Schönhage and Strassen in this model.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Integer-multiplication-below-n-log-n-September-23-2026/paper.pdf).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
