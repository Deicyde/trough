---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HighGirthSteinerTripleSystemErdosProblem207Wanted.highGirthSteinerTripleSystemsExist, MathlibExt.Combinatorics.HighGirthSteinerTripleSystemErdosProblem207Wanted.highGirthSteinerTripleSystemsExist_holds
statement: formalized
---

# High-girth Steiner triple systems

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/high-girth-steiner-triple-systems/index.html).

## Erdős Problem 207

The statement that for every integer $g \ge 2$ there is an $N$ such
that for every $n \ge N$ with $n \equiv 1$ or $n \equiv 3 \pmod 6$ there is a Steiner triple
system on the $n$ points $\{0, \dots, n-1\}$ (three-point blocks, every pair of distinct points
in exactly one block) in which every set of $j$ distinct blocks, with $2 \le j \le g$, covers at
least $j + 3$ points.

Formalized by `MathlibExt.Combinatorics.HighGirthSteinerTripleSystemErdosProblem207Wanted.highGirthSteinerTripleSystemsExist`, a definition declared in [WantedExt/Combinatorics/HighGirthSteinerTripleSystemErdosProblem207Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/HighGirthSteinerTripleSystemErdosProblem207Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/high-girth-steiner-triple-systems/index.html#high-girth-steiner-triple-systems-exist).

## High-girth Steiner triple systems exist

For every integer $g \ge 2$ there is an $N$
such that for every $n \ge N$ with $n \equiv 1$ or $n \equiv 3 \pmod 6$ there is a Steiner triple
system on the $n$ points $\{0, \dots, n-1\}$ in which every set of $j$ distinct blocks, with
$2 \le j \le g$, covers at least $j + 3$ points.

Kwan, Sah, Sawhney and Simkin proved this conjecture of Erdős; in their terms, the Steiner triple
system has girth greater than $g$ (for $j \le 3$ the condition holds in every Steiner triple
system).

## Sources

- T. F. Bloom, Erdős Problems, Problem #207, https://www.erdosproblems.com/207 (status PROVED); resolution: M. Kwan, A. Sah, M. Sawhney and M. Simkin, High-girth Steiner triple systems, Ann. of Math. (2) 200 (2024), 1059-1156, arXiv:2201.04554, main theorem: Erdős's 1973 conjecture, Steiner triple systems of girth greater than g on all large admissible n, https://doi.org/10.4007/annals.2024.200.3.4.

Stated but not proved: `MathlibExt.Combinatorics.HighGirthSteinerTripleSystemErdosProblem207Wanted.highGirthSteinerTripleSystemsExist_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/HighGirthSteinerTripleSystemErdosProblem207Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/HighGirthSteinerTripleSystemErdosProblem207Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/high-girth-steiner-triple-systems/index.html#high-girth-steiner-triple-systems-exist-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: High-girth Steiner triple systems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/high-girth-steiner-triple-systems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/designs-latin-squares/high-girth-steiner-triple-systems)
