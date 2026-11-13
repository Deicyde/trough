---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.IsPSoluble, MathlibExt.GroupTheory.SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.sylowMaximalSupplementPSoluble, MathlibExt.GroupTheory.SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.sylowMaximalSupplementPSoluble_holds, MathlibExt.GroupTheory.SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.sylowMaximalSigmaNilpotentSupplement, MathlibExt.GroupTheory.SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.sylowMaximalSigmaNilpotentSupplement_holds, MathlibExt.GroupTheory.SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.sylowMaximalSigmaSolubleSupplement, MathlibExt.GroupTheory.SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.sylowMaximalSigmaSolubleSupplement_holds
statement: formalized
---

# Supplements of maximal subgroups of Sylow subgroups

7 results, 4 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html).

## $p$-soluble groups (series with $p$- and $p'$-factors)

A group $G$ is $p$-soluble when
it has a chain of subgroups $1 = H_0 \le H_1 \le \cdots \le H_n = G$, each normal in the next,
such that for every $i < n$ the relative index $|H_{i+1} : H_i|$ (taken to be $0$ when it is
infinite) is a power of $p$ or is coprime to $p$. For a finite group this says that every factor
$H_{i+1}/H_i$ is a $p$-group or a $p'$-group.

Formalized by `MathlibExt.GroupTheory.SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.IsPSoluble`, a definition declared in [WantedExt/GroupTheory/SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html#is-psoluble).

## Kourovka Problem 17.111 (supplements of maximal subgroups of Sylow subgroups)

The
statement, asked by A. N. Skiba, that for every prime $p$, every finite group $G$ whose order is
divisible by $p$ and every Sylow $p$-subgroup $P$ of $G$, if every maximal subgroup $M$ of $P$ has
a $p$-soluble supplement in $G$, that is, a $p$-soluble subgroup $K$ of $G$ with $MK = G$, then
$G$ is $p$-soluble.

Formalized by `MathlibExt.GroupTheory.SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.sylowMaximalSupplementPSoluble`, a definition declared in [WantedExt/GroupTheory/SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html#sylow-maximal-supplement-psoluble).

## $p$-soluble supplements of maximal subgroups of a Sylow subgroup force $p$-solubility

Let $p$ be a prime, $G$ a finite group whose order is divisible by $p$, and $P$ a Sylow
$p$-subgroup of $G$. If every maximal subgroup $M$ of $P$ has a $p$-soluble supplement in $G$,
that is, a $p$-soluble subgroup $K$ of $G$ with $MK = G$, then $G$ is $p$-soluble.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.111 (A. N. Skiba); resolution: GuoHua Qian, Science China Math. 56 (2013), 1015-1018, Kourovka Archive, Problem 17.111 (Yes, it must).

Stated but not proved: `MathlibExt.GroupTheory.SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.sylowMaximalSupplementPSoluble_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowMaximalPSolubleSupplementKourovka17Problem111Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html#sylow-maximal-supplement-psoluble-holds).

## Kourovka Problem 19.88 (statement)

The statement that for every partition $\sigma$ of the
set of all primes and every finite group $G$: if for every prime $p$, every Sylow $p$-subgroup $P$
of $G$ and every maximal subgroup $V$ of $P$ there is a $\sigma$-nilpotent subgroup $T$ of $G$ with
$VT = G$, that is, every element of $G$ is a product $vt$ with $v \in V$ and $t \in T$, then $G$ is
$\sigma$-nilpotent. Here a partition of the primes is a family of nonempty, pairwise disjoint sets
of primes whose union is the set of all primes, and a group is $\sigma$-nilpotent when it is the
internal direct product of finitely many normal subgroups, each of whose order has all its prime
divisors in a single block of $\sigma$.

Formalized by `MathlibExt.GroupTheory.SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.sylowMaximalSigmaNilpotentSupplement`, a definition declared in [WantedExt/GroupTheory/SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html#sylow-maximal-sigma-nilpotent-supplement).

## σ-nilpotent supplements to the maximal subgroups of Sylow subgroups (Kourovka 19.88)

Let
$\sigma$ be a partition of the set of all primes and let $G$ be a finite group. If for every prime
$p$, every Sylow $p$-subgroup $P$ of $G$ and every maximal subgroup $V$ of $P$ there is a
$\sigma$-nilpotent subgroup $T$ of $G$ with $VT = G$, that is, every element of $G$ is a product
$vt$ with $v \in V$ and $t \in T$, then $G$ is $\sigma$-nilpotent. Here a partition of the primes is
a family of nonempty, pairwise disjoint sets of primes whose union is the set of all primes, and a
group is $\sigma$-nilpotent when it is the internal direct product of finitely many normal
subgroups, each of whose order has all its prime divisors in a single block of $\sigma$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.88 (A. N. Skiba); resolution: A.-M. Liu, W. Guo, I. N. Safonova and A. N. Skiba, G-covering subgroup systems for some classes of σ-soluble groups, J. Algebra 585 (2021), 280-293; another solution using CFSG by S. F. Kamornikov and V. N. Tyutyanov, Trudy Inst. Mat. Mekh. UrO RAN 27 (2021), no. 1, 98-102, abstract: a set of subgroups of G containing a supplement to each maximal subgroup of every Sylow subgroup of G is a G-covering subgroup system for the classes of σ-soluble and of σ-nilpotent groups, which answers 19.87 and 19.88; Kourovka Archive, Problem 19.88: Yes, it is true, https://doi.org/10.1016/j.jalgebra.2021.06.010.

Stated but not proved: `MathlibExt.GroupTheory.SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.sylowMaximalSigmaNilpotentSupplement_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowMaximalSigmaNilpotentSupplementKourovka19Problem88Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html#sylow-maximal-sigma-nilpotent-supplement-2).

## Kourovka Problem 19.87 (statement)

The statement that for every partition $\sigma$ of the
set of all primes and every finite group $G$: if for every prime $p$, every Sylow $p$-subgroup $P$
of $G$ and every maximal subgroup $V$ of $P$ there is a $\sigma$-soluble subgroup $T$ of $G$ with
$VT = G$, that is, every element of $G$ is a product $vt$ with $v \in V$ and $t \in T$, then $G$ is
$\sigma$-soluble. Here a partition of the primes is a family of nonempty, pairwise disjoint sets of
primes whose union is the set of all primes, and a group is $\sigma$-soluble when for every chief
factor $A/B$ of it (normal subgroups $B < A$ with no normal subgroup strictly between them) all
prime divisors of the index $|A : B|$ lie in a single block of $\sigma$.

Formalized by `MathlibExt.GroupTheory.SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.sylowMaximalSigmaSolubleSupplement`, a definition declared in [WantedExt/GroupTheory/SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html#sylow-maximal-sigma-soluble-supplement).

## σ-soluble supplements to the maximal subgroups of Sylow subgroups (Kourovka 19.87)

Let $\sigma$
be a partition of the set of all primes and let $G$ be a finite group. If for every prime $p$, every
Sylow $p$-subgroup $P$ of $G$ and every maximal subgroup $V$ of $P$ there is a $\sigma$-soluble
subgroup $T$ of $G$ with $VT = G$, that is, every element of $G$ is a product $vt$ with $v \in V$
and $t \in T$, then $G$ is $\sigma$-soluble. Here a partition of the primes is a family of nonempty,
pairwise disjoint sets of primes whose union is the set of all primes, and a group is
$\sigma$-soluble when for every chief factor $A/B$ of it (normal subgroups $B < A$ with no normal
subgroup strictly between them) all prime divisors of the index $|A : B|$ lie in a single block of
$\sigma$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.87 (A. N. Skiba); resolution: A.-M. Liu, W. Guo, I. N. Safonova and A. N. Skiba, G-covering subgroup systems for some classes of σ-soluble groups, J. Algebra 585 (2021), 280-293; another solution using CFSG by S. F. Kamornikov and V. N. Tyutyanov, Trudy Inst. Mat. Mekh. UrO RAN 27 (2021), no. 1, 98-102, abstract: a set of subgroups of G containing a supplement to each maximal subgroup of every Sylow subgroup of G is a G-covering subgroup system for the classes of σ-soluble and of σ-nilpotent groups, which answers 19.87 and 19.88; Kourovka Archive, Problem 19.87: Yes, it is true, https://doi.org/10.1016/j.jalgebra.2021.06.010.

Stated but not proved: `MathlibExt.GroupTheory.SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.sylowMaximalSigmaSolubleSupplement_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowMaximalSigmaSolubleSupplementKourovka19Problem87Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html#sylow-maximal-sigma-soluble-supplement-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Supplements of maximal subgroups of Sylow subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/soluble-finite-groups/supplements-of-maximal-subgroups-of-sylow-subgro)
