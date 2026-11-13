---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.unsolvableEquationUnsolvableInFiniteQuotient, MathlibExt.GroupTheory.FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.unsolvableEquationUnsolvableInFiniteQuotient_refuted
statement: formalized
---

# Equations over free groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equations-over-free-groups/index.html).

## Kourovka Problem 14.48 (equations over free groups in finite quotients)

The statement
that for every free group $F$ on an arbitrary set of generators, every natural number $n$ and every
equation $w$ over $F$ in the unknowns $x_0, \dots, x_{n-1}$ (an element of the free product of $F$
with the free group on $x_0, \dots, x_{n-1}$): if no $g_0, \dots, g_{n-1} \in F$ are such that
substituting $g_i$ for $x_i$ sends $w$ to $1$, then there is a normal subgroup $N$ of finite index
in $F$ such that no $h_0, \dots, h_{n-1} \in F / N$ are such that substituting $h_i$ for $x_i$ and
mapping the coefficients of $w$ to their images in $F / N$ sends $w$ to $1$.

Formalized by `MathlibExt.GroupTheory.FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.unsolvableEquationUnsolvableInFiniteQuotient`, a definition declared in [WantedExt/GroupTheory/FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equations-over-free-groups/index.html#unsolvable-equation-unsolvable-in-finite).

## An unsolvable equation over a free group that is solvable in every finite quotient

There are
a free group $F$ on some set of generators, a natural number $n$ and an equation $w$ over $F$ in
the unknowns $x_0, \dots, x_{n-1}$, that is, an element $w$ of the free product of $F$ with the
free group on $x_0, \dots, x_{n-1}$, such that no $g_0, \dots, g_{n-1} \in F$ satisfy the equation
(substituting $g_i$ for $x_i$ never sends $w$ to $1$), but for every normal subgroup $N$ of finite
index in $F$ there are $h_0, \dots, h_{n-1} \in F / N$ such that substituting $h_i$ for $x_i$ and
mapping the coefficients of $w$ to their images in $F / N$ sends $w$ to $1$.

Resolved false: the Kourovka Archive answers 14.48 "No, not always", citing Coulbois and Khelif:
some equation over a free group has no solution in it but has a solution in every finite quotient.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.48 (L. Comerford); resolution: T. Coulbois and A. Khelif, Proc. Amer. Math. Soc. 127 (1999), no. 4, 963-965, Kourovka Archive, Problem 14.48 (answer: No, not always).

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.unsolvableEquationUnsolvableInFiniteQuotient_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeGroupEquationFiniteQuotientKourovka14Problem48Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equations-over-free-groups/index.html#unsolvable-equation-unsolvable-in-finite-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equations over free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/equations-over-free-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/varieties-and-equations/equations-over-free-groups)
