---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.IsFrattiniChiefFactor, MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.IsComplementedChiefFactor, MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.coverAvoidTripleIntersectionCore, MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.coverAvoidTripleIntersectionCore_holds
statement: formalized
---

# Frattini and complemented chief factors

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/frattini-and-complemented-chief-factors/index.html).

## Frattini chief factor

For subgroups $A$ and $B$ of a group $G$, $A/B$ is a Frattini chief
factor of $G$ when $A/B$ is a chief factor of $G$ and $A$ is contained in every maximal subgroup
of $G$ that contains $B$; equivalently, $A/B \le \Phi(G/B)$, where $\Phi$ denotes the Frattini
subgroup.

Formalized by `MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.IsFrattiniChiefFactor`, a definition declared in [WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/frattini-and-complemented-chief-factors/index.html#is-frattini-chief-factor).

## Complemented chief factor

For subgroups $A$ and $B$ of a group $G$, $A/B$ is a
complemented chief factor of $G$ when $A/B$ is a chief factor of $G$ and some subgroup $M$ of $G$
satisfies $\langle M, A \rangle = G$ and $M \cap A = B$ (as $A$ is normal, the first condition
says $MA = G$).

Formalized by `MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.IsComplementedChiefFactor`, a definition declared in [WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/frattini-and-complemented-chief-factors/index.html#is-complemented-chief-factor).

## Kourovka Problem 19.38

The statement that for every finite soluble group $G$ and every
subgroup $H$ of $G$ that covers every Frattini chief factor $A/B$ of $G$, that is,
$A \le \langle H, B \rangle$ (which is $HB$, as $B$ is normal), and avoids every complemented
chief factor $A/B$ of $G$, that is, $H \cap A \le B$, there are $x, y \in G$ such that
$H \cap H^x \cap H^y = H_G$, where $H^x = xHx^{-1}$ and $H_G$ is the normal core of $H$, the
largest normal subgroup of $G$ contained in $H$.

Formalized by `MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.coverAvoidTripleIntersectionCore`, a definition declared in [WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/frattini-and-complemented-chief-factors/index.html#cover-avoid-triple-intersection-core).

## Kamornikov–Shemetkova theorem (Kourovka Problem 19.38)

Let $H$ be a subgroup of a
finite soluble group $G$. Suppose that $H$ covers every Frattini chief factor $A/B$ of $G$, that
is, $A \le \langle H, B \rangle$ (which is $HB$, as $B$ is normal), and avoids every complemented
chief factor $A/B$ of $G$, that is, $H \cap A \le B$. Then there are $x, y \in G$ such that
$H \cap H^x \cap H^y = H_G$, where $H^x = xHx^{-1}$ and $H_G$ is the normal core of $H$, the
largest normal subgroup of $G$ contained in $H$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.38 (S. F. Kamornikov); resolution: S. F. Kamornikov and O. L. Shemetkova, On a question concerning the intersection of Φ-isolators of finite soluble groups, J. Algebra 641 (2024), 1-8, doi:10.1016/j.jalgebra.2023.11.029, the Kourovka Notebook (21st issue) marks 19.38 solved: Yes, it is true, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.CoverAvoidIntersectionCoreKourovka19Problem38Wanted.coverAvoidTripleIntersectionCore_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CoverAvoidIntersectionCoreKourovka19Problem38Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/frattini-and-complemented-chief-factors/index.html#cover-avoid-triple-intersection-core-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frattini and complemented chief factors](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/frattini-and-complemented-chief-factors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/frattini-and-complemented-chief-factors)
