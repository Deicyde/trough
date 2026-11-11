---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.IAAutomorphismsLinearKourovka15Problem10Wanted.iaAut, MathlibExt.GroupTheory.IAAutomorphismsLinearKourovka15Problem10Wanted.iaAutLinear, MathlibExt.GroupTheory.IAAutomorphismsLinearKourovka15Problem10Wanted.iaAutLinear_refuted
statement: formalized
---

# Linearity of IA-automorphism groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/linearity-of-ia-automorphism-groups/index.html).

## IA-automorphisms of a free group

For a natural number $n$, let $F_n$ be the free group on
$n$ generators. $\mathrm{IA}(F_n)$ is the subgroup of the automorphism group of $F_n$ consisting of
the automorphisms $\varphi$ that act trivially on the abelianization $F_n/[F_n, F_n]$, that is,
such that $\varphi(x)$ and $x$ have the same image in $F_n/[F_n, F_n]$ for every $x \in F_n$.

Formalized by `MathlibExt.GroupTheory.IAAutomorphismsLinearKourovka15Problem10Wanted.iaAut`, a definition declared in [WantedExt/GroupTheory/IAAutomorphismsLinearKourovka15Problem10Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/IAAutomorphismsLinearKourovka15Problem10Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/linearity-of-ia-automorphism-groups/index.html#ia-aut).

## Kourovka Problem 15.10 (statement): linearity of IA-automorphism groups of free groups

The statement that for some $n \ge 3$ the group $\mathrm{IA}(F_n)$ of automorphisms of the free
group $F_n$ on $n$ generators that act trivially on its abelianization $F_n/[F_n, F_n]$ is linear,
that is, there are a field $K$, a natural number $m$ and an injective group homomorphism
$\mathrm{IA}(F_n) \to \mathrm{GL}_m(K)$.

Formalized by `MathlibExt.GroupTheory.IAAutomorphismsLinearKourovka15Problem10Wanted.iaAutLinear`, a definition declared in [WantedExt/GroupTheory/IAAutomorphismsLinearKourovka15Problem10Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/IAAutomorphismsLinearKourovka15Problem10Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/linearity-of-ia-automorphism-groups/index.html#ia-aut-linear).

## IA-automorphism group of a free group is not linear

Resolved false: the Kourovka Archive answers 15.10 No: `IA(Fₙ)` is not linear for `n ≥ 5` (Pettet)
and for every `n ≥ 3` (Bardakov and Mikhailov). Source: E. I. Khukhro and V. D. Mazurov (eds.),
Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026),
Archive of Solved Problems, Problem 15.10 (Yu. I. Merzlyakov; V. G. Bardakov); resolution: V. G.
Bardakov and R. Mikhailov, Commun. Algebra 36 (2008), no. 4, 1489-1499 (n ≥ 3); A. Pettet,
Cohomology of some subgroups of the automorphism group of a free group, Ph.D. thesis, 2006 (n ≥ 5),
Kourovka Archive, Problem 15.10.

Stated but not proved: `MathlibExt.GroupTheory.IAAutomorphismsLinearKourovka15Problem10Wanted.iaAutLinear_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/IAAutomorphismsLinearKourovka15Problem10Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/IAAutomorphismsLinearKourovka15Problem10Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/linearity-of-ia-automorphism-groups/index.html#ia-aut-linear-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linearity of IA-automorphism groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/linearity-of-ia-automorphism-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/linearity-of-ia-automorphism-groups)
