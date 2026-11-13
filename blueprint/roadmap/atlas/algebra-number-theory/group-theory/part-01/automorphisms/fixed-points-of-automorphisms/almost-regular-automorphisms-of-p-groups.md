---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.boundedIndexSubgroupOfBoundedDerivedLength, MathlibExt.GroupTheory.AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.boundedIndexSubgroupOfBoundedDerivedLength_holds, MathlibExt.GroupTheory.AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.boundedIndexBoundedClassSubgroup, MathlibExt.GroupTheory.AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.boundedIndexBoundedClassSubgroup_holds
statement: formalized
---

# Almost regular automorphisms of p-groups

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/almost-regular-automorphisms-of-p-groups/index.html).

## Bounded-index subgroups of bounded derived length (Kourovka 14.96)

The proposition that
there are functions $f \colon \mathbb{N}^3 \to \mathbb{N}$ and $g \colon \mathbb{N} \to \mathbb{N}$
such that for every prime $p$, all natural numbers $n$ and $m$, every finite $p$-group $P$ and
every automorphism $\varphi$ of $P$ of order $p^n$ with exactly $p^m$ fixed points, $P$ has a
subgroup of index at most $f(p, n, m)$ that is soluble of derived length at most $g(m)$.

This is the question posed by E. I. Khukhro as Kourovka Problem 14.96.

Formalized by `MathlibExt.GroupTheory.AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.boundedIndexSubgroupOfBoundedDerivedLength`, a definition declared in [WantedExt/GroupTheory/AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/almost-regular-automorphisms-of-p-groups/index.html#bounded-index-subgroup-of-bounded-derive).

## Almost regular automorphisms of finite $p$-groups and derived length (Kourovka 14.96)

There
are functions $f \colon \mathbb{N}^3 \to \mathbb{N}$ and $g \colon \mathbb{N} \to \mathbb{N}$ such
that for every prime $p$, all natural numbers $n$ and $m$, every finite $p$-group $P$ and every
automorphism $\varphi$ of $P$ of order $p^n$ with exactly $p^m$ fixed points, $P$ has a subgroup
of index at most $f(p, n, m)$ that is soluble of derived length at most $g(m)$. So Khukhro's
question of Kourovka Problem 14.96 has a positive answer.

This was proved by Jaikin-Zapirain.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.96 (E. I. Khukhro); resolution: A. Jaikin-Zapirain, On almost regular automorphisms of finite p-groups, Adv. Math. 153 (2000), no. 2, 391-402, main theorem (a subgroup of (p, n, m)-bounded index and m-bounded derived length); Kourovka Archive, Problem 14.96 (answer: Yes, it is true).

Stated but not proved: `MathlibExt.GroupTheory.AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.boundedIndexSubgroupOfBoundedDerivedLength_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlmostRegularAutomorphismDerivedLengthKourovka14Problem96Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/almost-regular-automorphisms-of-p-groups/index.html#bounded-index-subgroup-of-bounded-derive-2).

## Bounded index and bounded class under a $p$-automorphism (Kourovka 10.68)

The proposition
that there are functions $f(p, m)$ and $g(m)$ of natural numbers, with natural-number values, such
that for every prime $p$, every $m \in \mathbb{N}$, every finite $p$-group $G$ and every
automorphism $\varphi$ of $G$ of order $p$ with exactly $p^m$ fixed points, $G$ has a subgroup $H$
of index at most $f(p, m)$ and nilpotency class at most $g(m)$, that is, $\gamma_{g(m)+1}(H) = 1$,
where $\gamma_1(H) = H$ and $\gamma_{i+1}(H) = [\gamma_i(H), H]$.

Formalized by `MathlibExt.GroupTheory.AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.boundedIndexBoundedClassSubgroup`, a definition declared in [WantedExt/GroupTheory/AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/almost-regular-automorphisms-of-p-groups/index.html#bounded-index-bounded-class-subgroup).

## Medvedev's theorem on automorphisms of order $p$ with $p^m$ fixed points

There are functions
$f(p, m)$ and $g(m)$ of natural numbers, with natural-number values, such that for every prime $p$,
every $m \in \mathbb{N}$, every finite $p$-group $G$ and every automorphism $\varphi$ of $G$ of
order $p$ with exactly $p^m$ fixed points, $G$ has a subgroup $H$ of index at most $f(p, m)$ and
nilpotency class at most $g(m)$, that is, $\gamma_{g(m)+1}(H) = 1$, where $\gamma_1(H) = H$ and
$\gamma_{i+1}(H) = [\gamma_i(H), H]$.

This answers Kourovka Problem 10.68 (E. I. Khukhro) in the affirmative; the case $m = 1$ follows
from the theory of $p$-groups of maximal class.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.68 (E. I. Khukhro); resolution: Yu. Medvedev, J. London Math. Soc. (2) 59, no. 3 (1999), 787-798, Kourovka Archive, Problem 10.68 ("Yes, it is").

Stated but not proved: `MathlibExt.GroupTheory.AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.boundedIndexBoundedClassSubgroup_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismFewFixedPointsPGroupKourovka10Problem68Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/almost-regular-automorphisms-of-p-groups/index.html#bounded-index-bounded-class-subgroup-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Almost regular automorphisms of p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/almost-regular-automorphisms-of-p-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/almost-regular-automorphisms-of-p-groups)
