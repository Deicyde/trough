---
declaration: section
origin: cited
---

# 136. A quasilinear PCP theorem for PPAD

1 manuscript, with no Lean, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the quasilinear PCP-for-PPAD conjecture. An End-of-Line instance of length *N* reduces to numerical circuit constraints of total length $N(\log N)^{O(1)}$ such that any polynomially encoded rational assignment satisfying all but a fixed fraction to fixed accuracy yields an endpoint solution. Such assignments always exist, giving robust local verification with only quasilinear size overhead.

## The PCP-for-PPAD conjecture: a quasilinear reduction

We prove the quasilinear-size PCP-for-PPAD conjecture of Babichenko, Papadimitriou, and Rubinstein. There are fixed positive rational constants *ε* and *δ* and a deterministic polynomial-time reduction that transforms an End-of-Line instance of binary length *N* into a generalized circuit of total binary length $N(\log N)^{O(1)}$. From any rational assignment of polynomial encoding length that *ε*-satisfies all but a *δ* fraction of the gates, a solution to the original End-of-Line instance can be recovered in polynomial time, regardless of which gates fail. Such assignments always exist, with one fixed polynomial bound on their encoding length.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/paper.pdf).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
