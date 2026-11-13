---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.CountQ, MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.discrep, MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.conjecture, MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.conjecture_refuted
statement: formalized
---

# Discrepancy of fractional parts

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/discrepancy-of-fractional-parts/index.html).

## Counting fractional parts in a rational interval

For a sequence of integers
$(x_n)_{n \ge 0}$, a real number $\alpha$, a natural number $N$ and rationals $p, q$, the number of
indices $n < N$ for which the fractional part $\{\alpha x_n\}$ lies in the closed interval
$[p, q]$.

Formalized by `MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.CountQ`, a definition declared in [WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/discrepancy-of-fractional-parts/index.html#count-q).

## Discrepancy of fractional parts over rational intervals

For a sequence of integers
$(x_n)_{n \ge 0}$, a real number $\alpha$ and a natural number $N$, the discrepancy $D(N)$ is the
supremum, over rationals $p, q$ with $0 \le p \le q \le 1$, of $\lvert A(p, q) - (q - p) N \rvert$,
where $A(p, q)$ is the number of indices $n < N$ for which the fractional part $\{\alpha x_n\}$
lies in the closed interval $[p, q]$.

Formalized by `MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.discrep`, a definition declared in [WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/discrepancy-of-fractional-parts/index.html#discrep).

## Erdős Problem 992 on the discrepancy of fractional parts

For a strictly increasing
sequence of integers $x_0 < x_1 < \cdots$, a real number $\alpha$ and a natural number $N$, let
$D(N)$ be the supremum, over rationals $p, q$ with $0 \le p \le q \le 1$, of
$\lvert A(p, q) - (q - p) N \rvert$, where $A(p, q)$ is the number of indices $n < N$ for which
the fractional part $\{\alpha x_n\}$ lies in $[p, q]$. The statement is that for every such
sequence, for almost every $\alpha \in [0, 1]$ (Lebesgue measure) and every $\varepsilon > 0$,
there is a real constant $C$ such that $D(N) \le C \sqrt{N} (\log N)^{\varepsilon}$ for all
sufficiently large $N$.

Formalized by `MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/discrepancy-of-fractional-parts/index.html#conjecture).

## Erdős Problem 992 has a negative answer

For a sequence of integers $(x_n)_{n \ge 0}$, a real
number $\alpha$ and a natural number $N$, let $D(N)$ be the supremum, over rationals $p, q$ with
$0 \le p \le q \le 1$, of $\lvert A(p, q) - (q - p) N \rvert$, where $A(p, q)$ is the number of
indices $n < N$ for which the fractional part $\{\alpha x_n\}$ lies in $[p, q]$. It is not true
that for every strictly increasing sequence of integers $x_0 < x_1 < \cdots$, for almost every
$\alpha \in [0, 1]$ and every $\varepsilon > 0$ there is a real constant $C$ with
$D(N) \le C \sqrt{N} (\log N)^{\varepsilon}$ for all sufficiently large $N$.

Berkes and Philipp construct an increasing integer sequence $(n_k)$ with
$\limsup_N \lvert \sum_{k \le N} \cos(2\pi n_k \alpha) \rvert / \sqrt{N \log N} = \infty$ for almost
every $\alpha$; by Koksma's inequality, $D(N)$ is then not $O(\sqrt{N} (\log N)^{\varepsilon})$ for
$\varepsilon < 1/2$.

## Sources

- C. Aistleitner, I. Berkes, R. Tichy, Lacunary sequences in analysis, probability and number theory, arXiv preprint (2023), arXiv:2301.05561 (reporting I. Berkes, W. Philipp, J. London Math. Soc. (2) 50 (1994), 454-464), https://arxiv.org/abs/2301.05561.

Stated but not proved: `MathlibExt.NumberTheory.ErdosSequenceDiscrepancyWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosSequenceDiscrepancyWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/discrepancy-of-fractional-parts/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrepancy of fractional parts](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/discrepancy-of-fractional-parts/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/discrepancy-of-fractional-parts)
