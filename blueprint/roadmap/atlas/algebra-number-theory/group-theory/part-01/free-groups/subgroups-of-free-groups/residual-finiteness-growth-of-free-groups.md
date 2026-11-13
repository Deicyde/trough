---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeGroupLogIndexSeparationKourovka15Problem35Wanted.logIndexSeparation, MathlibExt.GroupTheory.FreeGroupLogIndexSeparationKourovka15Problem35Wanted.logIndexSeparation_refuted
statement: formalized
---

# Residual finiteness growth of free groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/residual-finiteness-growth-of-free-groups/index.html).

## Logarithmic-index separation in free groups (Kourovka 15.35)

The statement, posed by
O. V. Bogopolski, that for some integer $r \ge 2$ there is a real number $C$ such that every
element $w$ of the free group $F_r$ of rank $r$ whose reduced word length $n$ satisfies $n > 1$
lies outside some subgroup of $F_r$ of finite index at most $C \log n$, where $\log$ is the
natural logarithm.

Formalized by `MathlibExt.GroupTheory.FreeGroupLogIndexSeparationKourovka15Problem35Wanted.logIndexSeparation`, a definition declared in [WantedExt/GroupTheory/FreeGroupLogIndexSeparationKourovka15Problem35Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupLogIndexSeparationKourovka15Problem35Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/residual-finiteness-growth-of-free-groups/index.html#log-index-separation).

## Bogopolski's logarithmic-index separation fails in free groups of rank at least 2

For every
integer $r \ge 2$ and every real number $C$, there is an element $w$ of the free group $F_r$ of
rank $r$ whose reduced word length $n$ satisfies $n > 1$ and such that every subgroup of finite
index in $F_r$ that does not contain $w$ has index greater than $C \log n$, where $\log$ is the
natural logarithm. That is, the logarithmic-index separation property of Kourovka Problem 15.35
holds for no rank $r \ge 2$.

Bou-Rabee and McReynolds (Theorem 1.4) prove that for every rank $m > 1$ the maximal divisibility
function of $F_m$ on words of length at most $n$ is not $O(\log n)$, which rules out every $C$;
the Kourovka Archive answers 15.35 "No, it is not true".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.35 (O. V. Bogopolski); resolution: K. Bou-Rabee and D. B. McReynolds, Asymptotic growth and least common multiples in groups, Bull. London Math. Soc. 43 (2011), 1059-1068, arXiv:0907.3681, Theorem 1.4 (for m > 1, max D_{F_m}(n) is not bounded by O(log n)), https://arxiv.org/abs/0907.3681.

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupLogIndexSeparationKourovka15Problem35Wanted.logIndexSeparation_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupLogIndexSeparationKourovka15Problem35Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupLogIndexSeparationKourovka15Problem35Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/residual-finiteness-growth-of-free-groups/index.html#log-index-separation-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Residual finiteness growth of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/residual-finiteness-growth-of-free-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/residual-finiteness-growth-of-free-groups)
