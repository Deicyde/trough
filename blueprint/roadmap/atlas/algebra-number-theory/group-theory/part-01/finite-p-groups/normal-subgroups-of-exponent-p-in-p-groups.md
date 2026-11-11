---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NormalExponentPSubgroupKourovka15Problem24Wanted.normalExponentPSubgroupOfLargePrime, MathlibExt.GroupTheory.NormalExponentPSubgroupKourovka15Problem24Wanted.normalExponentPSubgroupOfLargePrime_holds
statement: formalized
---

# Normal subgroups of exponent p in p-groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/normal-subgroups-of-exponent-p-in-p-groups/index.html).

## Berkovich's question on normal subgroups of exponent p, for p > n

For every prime $p$
and every natural number $n < p$, if a finite $p$-group $G$ has a subgroup of order $p^n$ all of
whose elements $x$ satisfy $x^p = 1$, then $G$ has a normal subgroup of order $p^n$ all of whose
elements $x$ satisfy $x^p = 1$.

Berkovich asked this for $p$ sufficiently large relative to $n$; the explicit bound $p > n$ is the
one of the resolution. For $n \ge 1$ the condition $x^p = 1$ on a group of order $p^n$ says that it
has exponent exactly $p$.

Formalized by `MathlibExt.GroupTheory.NormalExponentPSubgroupKourovka15Problem24Wanted.normalExponentPSubgroupOfLargePrime`, a definition declared in [WantedExt/GroupTheory/NormalExponentPSubgroupKourovka15Problem24Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NormalExponentPSubgroupKourovka15Problem24Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/normal-subgroups-of-exponent-p-in-p-groups/index.html#normal-exponent-psubgroup-of-large-prime).

## Normal subgroups of exponent p in p-groups when p > n

For every prime $p$ and every natural
number $n < p$, if a finite $p$-group $G$ has a subgroup $H$ of order $p^n$ with $x^p = 1$ for all
$x \in H$, then $G$ has a normal subgroup $N$ of order $p^n$ with $x^p = 1$ for all $x \in N$.

The Kourovka Archive answers "Yes, it is true if $p > n$" (A. Mann): by induction a subgroup $H$
of exponent $p$ and order $p^n$ may be taken normal in a maximal subgroup $M$; then $H$ lies in
the $(p-1)$-st term $\zeta_{p-1}(M)$ of the upper central series of $M$, and the elements of
order $p$ of $\zeta_{p-1}(M)$ form a normal subgroup of $G$ containing $H$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.24 (Ya. G. Berkovich); resolution: A. Mann, letter of 1 October 2002, as recorded in the Kourovka Archive, Problem 15.24, Archive answer: Yes if p > n (H of exponent p and order p^n normal in a maximal subgroup M lies in ζ_{p-1}(M), whose elements of order p form a normal subgroup of G), https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.NormalExponentPSubgroupKourovka15Problem24Wanted.normalExponentPSubgroupOfLargePrime_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/NormalExponentPSubgroupKourovka15Problem24Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NormalExponentPSubgroupKourovka15Problem24Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/normal-subgroups-of-exponent-p-in-p-groups/index.html#normal-exponent-psubgroup-of-large-prime-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal subgroups of exponent p in p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/normal-subgroups-of-exponent-p-in-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-p-groups/normal-subgroups-of-exponent-p-in-p-groups)
