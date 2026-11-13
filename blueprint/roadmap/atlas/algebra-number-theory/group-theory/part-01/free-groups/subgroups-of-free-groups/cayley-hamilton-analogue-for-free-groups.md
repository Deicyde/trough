---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeGroupCayleyHamiltonKourovka17Problem32Wanted.freeGroupCayleyHamilton, MathlibExt.GroupTheory.FreeGroupCayleyHamiltonKourovka17Problem32Wanted.freeGroupCayleyHamilton_refuted
statement: formalized
---

# Cayley–Hamilton analogue for free groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/cayley-hamilton-analogue-for-free-groups/index.html).

## Bogopolski's Cayley–Hamilton question for free groups (Kourovka 17.32)

The assertion
that for every natural number $n$, every element $w$ of the free group $F_n$ of rank $n$ and every
automorphism $\varphi$ of $F_n$, if $w, \varphi(w), \dots, \varphi^n(w)$ generate $F_n$, then
already $w, \varphi(w), \dots, \varphi^{n-1}(w)$ generate $F_n$.

Formalized by `MathlibExt.GroupTheory.FreeGroupCayleyHamiltonKourovka17Problem32Wanted.freeGroupCayleyHamilton`, a definition declared in [WantedExt/GroupTheory/FreeGroupCayleyHamiltonKourovka17Problem32Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupCayleyHamiltonKourovka17Problem32Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/cayley-hamilton-analogue-for-free-groups/index.html#free-group-cayley-hamilton).

## Bogopolski's Cayley–Hamilton analogue fails for free groups (Kourovka 17.32)

There are a
natural number $n$, an element $w$ of the free group $F_n$ of rank $n$ and an automorphism
$\varphi$ of $F_n$ such that $w, \varphi(w), \dots, \varphi^n(w)$ generate $F_n$ but
$w, \varphi(w), \dots, \varphi^{n-1}(w)$ do not.

Ionin and Semidetnov (Answer 8.2) give the example $n = 2$, $F_2 = \langle x, y \rangle$, $w = xy$
and $\varphi(x) = yx$, $\varphi(y) = x$. The Kourovka Notebook (21st issue) answers 17.32 "No, it
is not true", citing their preprint and a preprint of O. Kharlampovich.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 17.32 (O. V. Bogopolski); resolution: V. Ionin and A. Semidetnov, On some more problems from the Kourovka Notebook, preprint, arXiv:2608.29219 (2026; solutions found with the assistance of large language models and checked by the authors, per its abstract); O. Kharlampovich, preprint (2026), Ionin-Semidetnov, Answer 8.2 (the assertion fails for n = 2: w = xy, φ(x) = yx, φ(y) = x); the Kourovka Notebook (21st issue) marks 17.32 solved (No, it is not true), https://arxiv.org/abs/2608.29219.

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupCayleyHamiltonKourovka17Problem32Wanted.freeGroupCayleyHamilton_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupCayleyHamiltonKourovka17Problem32Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupCayleyHamiltonKourovka17Problem32Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/cayley-hamilton-analogue-for-free-groups/index.html#free-group-cayley-hamilton-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cayley–Hamilton analogue for free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/cayley-hamilton-analogue-for-free-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/cayley-hamilton-analogue-for-free-groups)
