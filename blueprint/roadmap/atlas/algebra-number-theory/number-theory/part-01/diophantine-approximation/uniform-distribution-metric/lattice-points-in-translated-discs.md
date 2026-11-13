---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DiophantineApproximation.ScottishBook152Wanted.DiscLatticeCount, MathlibExt.NumberTheory.DiophantineApproximation.ScottishBook152Wanted.steinhausDiscFrequenciesExist
statement: formalized
---

# Lattice points in translated discs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/lattice-points-in-translated-discs/index.html).

## Lattice points in a translated unit disc

For $w = (w_1, w_2) \in \mathbb{R}^2$ and a
natural number $n$, the disc lattice count is the number of integer points
$(p_1, p_2) \in \mathbb{Z}^2$ in the closed disc of radius $1$ centred at $n w$, that is, with
$(p_1 - n w_1)^2 + (p_2 - n w_2)^2 \le 1$.

Formalized by `MathlibExt.NumberTheory.DiophantineApproximation.ScottishBook152Wanted.DiscLatticeCount`, a definition declared in [WantedExt/NumberTheory/DiophantineApproximation/ScottishBook152Wanted.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/ScottishBook152Wanted.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/lattice-points-in-translated-discs/index.html#disc-lattice-count).

## Steinhaus's disc frequencies exist

Let $w = (w_1, w_2) \in \mathbb{R}^2$ be such that
$w_1$, $w_2$ and $w_1 / w_2$ are all irrational, and for each natural number $n$ let $c(n)$ be the
disc lattice count of $w$ and $n$, the number of integer lattice points in the closed disc of
radius $1$ centred at $n w$. Then for each $m$ equal to $2$, $3$ or $4$, the proportion of the
integers $n$ with $0 \le n < N$ and $c(n) = m$ converges to a real number as $N \to \infty$.

A closed disc of radius $1$ always covers at least two and at most five lattice points. The
frequency values themselves are not pinned down here: they are the measures of the corresponding
regions for the limiting distribution of $n w$ modulo the lattice, and in particular depend on
$w$.

## Sources

- H. Steinhaus, Problem 152 of the Scottish Book; J. Mycielski's commentary in Mauldin (ed.), The Scottish Book, 2nd ed. (2015) explains the solution using facts from Diophantine approximation, as reported in the 2026 survey "90+ years of the Scottish Book" (arXiv:2603.27867).

Stated but not proved: `MathlibExt.NumberTheory.DiophantineApproximation.ScottishBook152Wanted.steinhausDiscFrequenciesExist` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/ScottishBook152Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/ScottishBook152Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/lattice-points-in-translated-discs/index.html#steinhaus-disc-frequencies-exist).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lattice points in translated discs](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/lattice-points-in-translated-discs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/lattice-points-in-translated-discs)
