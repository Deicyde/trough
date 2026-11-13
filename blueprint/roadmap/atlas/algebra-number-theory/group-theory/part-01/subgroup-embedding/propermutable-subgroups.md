---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.Permutes, MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.IsPropermutable, MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.IsTwoNilpotent, MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableNotInIntermediate, MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableSylowSubgroupsTwoNilpotent, MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableNotInIntermediate_holds, MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableSylowSubgroupsTwoNilpotent_holds
statement: formalized
---

# Propermutable subgroups

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html).

## Permuting subgroups

Let $H$ and $X$ be subgroups of a group $G$. Then $H$ permutes
with $X$ when $HX = XH$ as subsets of $G$, where $HX = \{hx : h \in H, x \in X\}$ and
$XH = \{xh : x \in X, h \in H\}$.

Formalized by `MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.Permutes`, a definition declared in [WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html#permutes).

## Propermutable subgroups

A subgroup $H$ of a group $G$ is propermutable in $G$ when there
is a subgroup $B$ of $G$ with $G = N_G(H)B$ (every element of $G$ is a product $nb$ with $n$ in
the normalizer $N_G(H)$ of $H$ and $b \in B$) such that $H$ permutes with every subgroup $X$ of
$B$, that is, $HX = XH$.

Formalized by `MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.IsPropermutable`, a definition declared in [WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html#is-propermutable).

## 2-nilpotent groups

A group $G$ is $2$-nilpotent when it has a normal subgroup $N$ of
finite odd order whose index in $G$ is $2^k$ for some natural number $k$.

Formalized by `MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.IsTwoNilpotent`, a definition declared in [WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html#is-two-nilpotent).

## Kourovka Problem 18.91(a) (statement)

The statement of Kourovka Problem 18.91(a)
(A. N. Skiba): there exist a finite group $G$ and subgroups $A \le B \le G$ such that $A$ is
propermutable in $G$ but $A$, regarded as a subgroup of $B$, is not propermutable in $B$.

Formalized by `MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableNotInIntermediate`, a definition declared in [WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html#propermutable-not-in-intermediate).

## Kourovka Problem 18.91(b) (statement)

The statement of Kourovka Problem 18.91(b)
(A. N. Skiba), with the range $1 \le k < n$: let $G$ be a finite group and $P$ a non-abelian
Sylow $2$-subgroup of $G$, with $|P| = 2^n$, and let $k$ be a natural number with $1 \le k < n$.
If every subgroup of $P$ of order $2^k$ is propermutable in $G$, and, when $k = 1$, every cyclic
subgroup of $P$ of order $4$ is propermutable in $G$, then $G$ is $2$-nilpotent.

The printed problem has $1 < k < n$, which contradicts its clause for $k = 1$; the range
$1 \le k < n$ is the one of Al-Sharo's Corollary 1.3.

Formalized by `MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableSylowSubgroupsTwoNilpotent`, a definition declared in [WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html#propermutable-sylow-subgroups-two-nilpot).

## Propermutability is not inherited by intermediate subgroups

There exist a finite group $G$
and subgroups $A \le B \le G$ such that $A$ is propermutable in $G$ but $A$, regarded as a
subgroup of $B$, is not propermutable in $B$. This is the positive answer to
Kourovka Problem 18.91(a).

The Kourovka Archive answers 18.91(a) "Yes, there is" (A. A. Pypka and D. Yu. Storozhenko, 2017).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.91 (A. N. Skiba); resolution: (a) A. A. Pypka and D. Yu. Storozhenko, Dopov. Nac. Akad. Nauk Ukrain. 2017, no. 7, 18-20 (Ukrainian); (b) Kh. A. Al-Sharo, Finite groups with given systems of weakly S-propermutable subgroups, J. Group Theory 19 (2016), no. 5, 871-887, Kourovka Archive, Problem 18.91: a) Yes, there is; b) Yes, it is. Al-Sharo, Corollary 1.3: if X ⊴ G, P ∈ Syl_p(X), (p - 1, |X|) = 1, and for some 1 < D < P every subgroup of P of order |D| (and, when P is non-abelian and |D| = 2, every cyclic subgroup of order 4) is S-propermutable in G, then X is p-nilpotent, https://doi.org/10.1515/jgth-2016-0017.

Stated but not proved: `MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableNotInIntermediate_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html#propermutable-not-in-intermediate-holds).

## Propermutable subgroups of a non-abelian Sylow 2-subgroup force 2-nilpotency

Let $G$
be a finite group and $P$ a non-abelian Sylow $2$-subgroup of $G$, with $|P| = 2^n$, and let $k$
be a natural number with $1 \le k < n$. If every subgroup of $P$ of order $2^k$ is propermutable
in $G$, and, when $k = 1$, every cyclic subgroup of $P$ of order $4$ is propermutable in $G$, then
$G$ is $2$-nilpotent. This is the positive answer to Kourovka Problem 18.91(b).

The Kourovka Archive answers 18.91(b) "Yes, it is" (Kh. A. Al-Sharo, 2016). Al-Sharo's
Corollary 1.3 (quoted below), applied to the normal subgroup $X = G$ with $p = 2$ (where
$(p - 1, |G|) = 1$ holds), gives 2-nilpotency already when the subgroups in question are only
$S$-propermutable, a weaker condition than propermutability: a subgroup $H$ of $G$ is
$S$-propermutable in $G$ when there is a subgroup $B$ of $G$ with $G = N_G(H)B$ such that $H$
permutes with every Sylow subgroup of $B$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.91 (A. N. Skiba); resolution: (a) A. A. Pypka and D. Yu. Storozhenko, Dopov. Nac. Akad. Nauk Ukrain. 2017, no. 7, 18-20 (Ukrainian); (b) Kh. A. Al-Sharo, Finite groups with given systems of weakly S-propermutable subgroups, J. Group Theory 19 (2016), no. 5, 871-887, Kourovka Archive, Problem 18.91: a) Yes, there is; b) Yes, it is. Al-Sharo, Corollary 1.3: if X ⊴ G, P ∈ Syl_p(X), (p - 1, |X|) = 1, and for some 1 < D < P every subgroup of P of order |D| (and, when P is non-abelian and |D| = 2, every cyclic subgroup of order 4) is S-propermutable in G, then X is p-nilpotent, https://doi.org/10.1515/jgth-2016-0017.

Stated but not proved: `MathlibExt.GroupTheory.PropermutableSubgroupKourovka18Problem91Wanted.propermutableSylowSubgroupsTwoNilpotent_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PropermutableSubgroupKourovka18Problem91Wanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html#propermutable-sylow-subgroups-two-nilpot-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Propermutable subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/subgroup-embedding/propermutable-subgroups)
