---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.fittingHeightBoundedByOrderAndCentralizer, MathlibExt.GroupTheory.FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.fittingHeightBoundedByOrderAndCentralizer_holds
statement: formalized
---

# Fitting height bounds from automorphisms

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/fitting-height-bounds-from-automorphisms/index.html).

## Kourovka Problem 19.43: Fitting height, automorphism order and centralizer size

The
statement that there is a function $f$ assigning a natural number $f(m, n)$ to every pair of
natural numbers $m$, $n$ such that every finite soluble group $G$ with an automorphism $\varphi$
has Fitting height at most $f(|\varphi|, |C_G(\varphi)|)$, where $|\varphi|$ is the order of
$\varphi$ and $|C_G(\varphi)|$ is the number of elements of $G$ fixed by $\varphi$.

The problem was posed by E. I. Khukhro.

Formalized by `MathlibExt.GroupTheory.FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.fittingHeightBoundedByOrderAndCentralizer`, a definition declared in [WantedExt/GroupTheory/FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/fitting-height-bounds-from-automorphisms/index.html#fitting-height-bounded-by-order-and-cent).

## Fitting height is bounded by the order of an automorphism and its centralizer

There is a
function $f$ assigning a natural number $f(m, n)$ to every pair of natural numbers $m$, $n$ such
that every finite soluble group $G$ with an automorphism $\varphi$ has Fitting height at most
$f(|\varphi|, |C_G(\varphi)|)$, where $|\varphi|$ is the order of $\varphi$ and $|C_G(\varphi)|$ is
the number of elements of $G$ fixed by $\varphi$.

This answers Kourovka Problem 19.43 (E. I. Khukhro) affirmatively: Khukhro proved the bound, and the
21st issue of the Kourovka Notebook marks 19.43 solved ("Yes, it is").

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.43 (E. I. Khukhro); resolution: E. Khukhro, Bull. London Math. Soc. 58 (2026), no. 1, Article ID e70206, the Kourovka Notebook (21st issue) marks 19.43 solved: Yes, it is, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.fittingHeightBoundedByOrderAndCentralizer_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FittingHeightAutomorphismCentralizerKourovka19Problem43Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/fitting-height-bounds-from-automorphisms/index.html#fitting-height-bounded-by-order-and-cent-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fitting height bounds from automorphisms](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/fitting-height-bounds-from-automorphisms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/fitting-height-bounds-from-automorphisms)
