---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.IsPPrimeIsolated, MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.IsPSeparable, MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.isolatedFGSubgroupsPSeparable, MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.isolatedFGSubgroupsPSeparable_refuted
statement: formalized
---

# Separability of isolated subgroups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/separability-of-isolated-subgroups/index.html).

## $p'$-isolated subgroup

Let $p$ be a natural number and let $H$ be a subgroup of a group
$F$. Then $H$ is $p'$-isolated if, for every $x \in F$ and every natural number $n > 0$ that is not
divisible by $p$, $x^n \in H$ implies $x \in H$.

Formalized by `MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.IsPPrimeIsolated`, a definition declared in [WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/separability-of-isolated-subgroups/index.html#is-pprime-isolated).

## Separability in the class of finite $p$-groups

Let $p$ be a natural number and let $H$ be
a subgroup of a group $F$. Then $H$ is separable in the class of finite $p$-groups if for every
$x \in F$ with $x \notin H$ there are a finite $p$-group $Q$ (a finite group in which every element
$g$ satisfies $g^{p^k} = 1$ for some natural number $k$) and a group homomorphism
$f \colon F \to Q$ with $f(x) \notin f(H)$.

Formalized by `MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.IsPSeparable`, a definition declared in [WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/separability-of-isolated-subgroups/index.html#is-pseparable).

## Moldavanskiĭ's question on $p$-separability of isolated subgroups (Kourovka 15.60)

The
statement that there is a prime $p$ such that, for every set $\alpha$, every finitely generated
$p'$-isolated subgroup of the free group on $\alpha$ is separable in the class of finite
$p$-groups.

Formalized by `MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.isolatedFGSubgroupsPSeparable`, a definition declared in [WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/separability-of-isolated-subgroups/index.html#isolated-fgsubgroups-pseparable).

## Isolated subgroups of free groups need not be $p$-separable

For every prime $p$ there are a
set $\alpha$ and a finitely generated $p'$-isolated subgroup of the free group on $\alpha$ that is
not separable in the class of finite $p$-groups. That is, the statement of Kourovka Problem 15.60
fails for every prime $p$.

Bardakov proved that every nonabelian free group has a finitely generated isolated subgroup $H$
($x^n \in H$ with $n \ne 0$ implies $x \in H$) that is not separable in the class of nilpotent
groups; it is $p'$-isolated for every prime $p$, and finite $p$-groups are nilpotent. The Kourovka
Archive answers 15.60 "No, it is not".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.60 (D. I. Moldavanskiĭ); resolution: V. G. Bardakov, On D. I. Moldavanskii's question about p-separable subgroups of a free group, Siberian Math. J. 45 (2004), no. 3, 416-419, arXiv:math/0404292, abstract (every nonabelian free group has a finitely generated isolated subgroup that is not separable in the class of nilpotent groups); Kourovka Archive, Problem 15.60 (answer: No, it is not), https://arxiv.org/abs/math/0404292.

Stated but not proved: `MathlibExt.GroupTheory.IsolatedSubgroupPSeparableKourovka15Problem60Wanted.isolatedFGSubgroupsPSeparable_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IsolatedSubgroupPSeparableKourovka15Problem60Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/separability-of-isolated-subgroups/index.html#isolated-fgsubgroups-pseparable-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Separability of isolated subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/separability-of-isolated-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/separability-of-isolated-subgroups)
