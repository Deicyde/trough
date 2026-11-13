---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.freeByCyclicConjugacySeparable, MathlibExt.GroupTheory.FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.freeByCyclicConjugacySeparable_holds
statement: formalized
---

# Conjugacy separability

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/conjugacy-separability/index.html).

## Kapovich's conjugacy separability question (Kourovka 19.41)

The assertion that for every
natural number $n$ and every automorphism $\varphi$ of the free group $F_n$ of rank $n$, the
semidirect product $F_n \rtimes_\varphi \mathbb{Z}$, in which $k \in \mathbb{Z}$ acts on $F_n$ by
$\varphi^k$, is conjugacy separable.

Formalized by `MathlibExt.GroupTheory.FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.freeByCyclicConjugacySeparable`, a definition declared in [WantedExt/GroupTheory/FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/conjugacy-separability/index.html#free-by-cyclic-conjugacy-separable).

## Finite-rank free-by-cyclic groups are conjugacy separable

For every natural number $n$ and
every automorphism $\varphi$ of the free group $F_n$ of rank $n$, the semidirect product
$F_n \rtimes_\varphi \mathbb{Z}$, in which $k \in \mathbb{Z}$ acts on $F_n$ by $\varphi^k$, is
conjugacy separable: any two of its elements whose images are conjugate in every quotient by a
normal subgroup of finite index are conjugate.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.41 (I. Kapovich); resolution: F. Dahmani, S. Hughes, M. Kudlinska and N. Touikan, Free-by-cyclic groups are conjugacy separable, preprint, arXiv:2509.22346v2 (2026), abstract: all finitely generated free-by-cyclic groups are conjugacy separable, resolving Question 19.41; the Kourovka Notebook (21st issue) marks 19.41 solved: Yes, it is, https://arxiv.org/abs/2509.22346.

Stated but not proved: `MathlibExt.GroupTheory.FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.freeByCyclicConjugacySeparable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeByCyclicConjugacySeparableKourovka19Problem41Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/conjugacy-separability/index.html#free-by-cyclic-conjugacy-separable-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugacy separability](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/conjugacy-separability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/conjugacy-separability)
