---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.IsSupersoluble, MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.MaximalFullPrimeSupersoluble, MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.HasChiefFactorRankGT, MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.PLengthLEOne, MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.everyNonabelianSimpleGroupOccurs, MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.fittingHeightUnbounded, MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.rankUnbounded, MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.pLengthAtMostOne
statement: formalized
---

# Supersoluble maximal subgroups

12 results, 8 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html).

## Supersoluble group (generator form)

A group $G$ is supersoluble when there are a natural
number $n$ and elements $g_0, \dots, g_{n-1}$ of $G$ that generate $G$ such that, for every
$i \le n$, the subgroup $G_i = \langle g_j : j < i \rangle$ is normal in $G$.

Then $1 = G_0 \le \dots \le G_n = G$ is a normal series with cyclic factors
$G_{i+1} / G_i = \langle G_i, g_i \rangle / G_i$.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.IsSupersoluble`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#is-supersoluble).

## Monakhov's condition

A group $G$ satisfies Monakhov's condition when every maximal
subgroup $M$ of $G$ with $\pi(M) = \pi(G)$ is supersoluble, where $\pi(X)$ is the set of prime
factors of the order of $X$ if $X$ is finite, and is empty if $X$ is infinite.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.MaximalFullPrimeSupersoluble`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#maximal-full-prime-supersoluble).

## Chief factor of rank above a bound

A group $G$ has a chief factor of rank greater than a
natural number $r$ when there are a chief factor $A / B$ of $G$, a prime $p$ and a natural number
$k > r$ such that the index $[A : B]$ equals $p^k$.

A chief factor of a finite soluble group is an elementary abelian $p$-group, of rank $k$ when its
order is $p^k$.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.HasChiefFactorRankGT`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#has-chief-factor-rank-gt).

## Groups of p-length at most one

For a natural number $p$, a group $G$ has $p$-length at
most $1$ when there are normal subgroups $N \le M$ of $G$ such that $N$ is finite of order not
divisible by $p$, the index $[M : N]$ equals $p^k$ for some natural number $k$ (an infinite index
counting as $0$), and the index $[G : M]$ is finite and not divisible by $p$.

For finite $G$ and prime $p$ this says that $N$ is a $p'$-group, $M / N$ is a $p$-group and $G / M$
is a $p'$-group.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.PLengthLEOne`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#plength-leone).

## Kourovka 19.55(a) (Monakhov): every non-abelian simple group occurs

The proposition that
for every finite non-abelian simple group $S$ there is a finite group $G$ such that $S$ is a
composition factor of $G$ and every maximal subgroup $M$ of $G$ with $\pi(M) = \pi(G)$ is
supersoluble, where $\pi(X)$ is the set of primes dividing the order of $X$.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.everyNonabelianSimpleGroupOccurs`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#every-nonabelian-simple-group-occurs).

## Kourovka 19.55(b) (Monakhov): unbounded Fitting height

The proposition that for every
natural number $h$ there is a finite soluble group $G$ whose Fitting height is greater than $h$ and
in which every maximal subgroup $M$ with $\pi(M) = \pi(G)$ is supersoluble, where $\pi(X)$ is the
set of primes dividing the order of $X$.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.fittingHeightUnbounded`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#fitting-height-unbounded).

## Unbounded chief-factor rank under Monakhov's condition (the claim)

The statement that for
every natural number $r$ there is a finite soluble group $G$ satisfying Monakhov's condition
(every maximal subgroup $M$ of $G$ with $\pi(M) = \pi(G)$ is supersoluble, where $\pi(X)$ is the
set of prime divisors of $|X|$) that has a chief factor $A/B$ of order $p^k$ for some prime $p$
and some $k > r$. This is the answer to Kourovka 19.55(b) for the rank.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.rankUnbounded`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#rank-unbounded).

## Kourovka 19.55(b) (Monakhov): p-length at most one

The proposition that for every finite
soluble group $G$ in which every maximal subgroup $H$ with $\pi(H) = \pi(G)$ is supersoluble,
where $\pi(X)$ is the set of primes dividing the order of $X$, and for every prime $p$, the group
$G$ has $p$-length at most $1$: there are normal subgroups $N \le M$ of $G$ such that $p$ does not
divide $|N|$, the index $[M : N]$ is a power of $p$, and $p$ does not divide $[G : M]$.

Formalized by `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.pLengthAtMostOne`, a definition declared in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#p-length-at-most-one).

## Moretó: every non-abelian simple group occurs in Kourovka 19.55(a)

For every finite
non-abelian simple group $S$ there is a finite group $G$ such that $S$ is a composition factor of
$G$ and every maximal subgroup $M$ of $G$ with $\pi(M) = \pi(G)$ is supersoluble, where $\pi(X)$ is
the set of primes dividing the order of $X$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.55 (V. S. Monakhov); resolution: A. Moretó, Finite groups whose maximal subgroups of order divisible by all the primes are supersolvable, Monatsh. Math. 195 (2021), no. 3, 497-500 (arXiv:2010.04808), Theorem A (every nonabelian simple group occurs as a composition factor), Theorem B (solvable examples of arbitrarily large nilpotency length and rank) and Theorem C (the p-length is 1 for every prime divisor p of |G|); Kourovka Archive, Problem 19.55, https://arxiv.org/abs/2010.04808.

Stated but not proved: `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.everyNonabelianSimpleGroupOccurs_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#every-nonabelian-simple-group-occurs-hol).

## Moretó: soluble groups in Kourovka 19.55 have unbounded Fitting height

For every natural
number $h$ there is a finite soluble group $G$ whose Fitting height is greater than $h$ and in
which every maximal subgroup $M$ with $\pi(M) = \pi(G)$ is supersoluble, where $\pi(X)$ is the set
of primes dividing the order of $X$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.55 (V. S. Monakhov); resolution: A. Moretó, Finite groups whose maximal subgroups of order divisible by all the primes are supersolvable, Monatsh. Math. 195 (2021), no. 3, 497-500 (arXiv:2010.04808), Theorem A (every nonabelian simple group occurs as a composition factor), Theorem B (solvable examples of arbitrarily large nilpotency length and rank) and Theorem C (the p-length is 1 for every prime divisor p of |G|); Kourovka Archive, Problem 19.55, https://arxiv.org/abs/2010.04808.

Stated but not proved: `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.fittingHeightUnbounded_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#fitting-height-unbounded-holds).

## Unbounded chief-factor rank under Monakhov's condition

For every natural number $r$ there is
a finite soluble group $G$ such that every maximal subgroup $M$ of $G$ with $\pi(M) = \pi(G)$ is
supersoluble, where $\pi(X)$ is the set of prime divisors of $|X|$, and $G$ has a chief factor
$A/B$ (normal subgroups $B < A$ of $G$ with no normal subgroup of $G$ strictly between them) of
order $p^k$ for some prime $p$ and some $k > r$.

Moretó's groups $G_n = V_1 \cdots V_n$ (Theorem B and its proof) are such examples: their minimal
normal subgroup $V_n$, an elementary abelian chief factor, has rank tending to infinity; the
Kourovka Archive records "there is not any bound for ... the rank".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.55 (V. S. Monakhov); resolution: A. Moretó, Finite groups whose maximal subgroups of order divisible by all the primes are supersolvable, Monatsh. Math. 195 (2021), no. 3, 497-500 (arXiv:2010.04808), Theorem A (every nonabelian simple group occurs as a composition factor), Theorem B (solvable examples of arbitrarily large nilpotency length and rank) and Theorem C (the p-length is 1 for every prime divisor p of |G|); Kourovka Archive, Problem 19.55, https://arxiv.org/abs/2010.04808.

Stated but not proved: `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.rankUnbounded_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#rank-unbounded-holds).

## Moretó: soluble groups in Kourovka 19.55 have p-length at most one

Let $G$ be a finite
soluble group in which every maximal subgroup $H$ with $\pi(H) = \pi(G)$ is supersoluble, where
$\pi(X)$ is the set of primes dividing the order of $X$. Then for every prime $p$ the group $G$ has
$p$-length at most $1$: there are normal subgroups $N \le M$ of $G$ such that $p$ does not divide
$|N|$, the index $[M : N]$ is a power of $p$, and $p$ does not divide $[G : M]$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.55 (V. S. Monakhov); resolution: A. Moretó, Finite groups whose maximal subgroups of order divisible by all the primes are supersolvable, Monatsh. Math. 195 (2021), no. 3, 497-500 (arXiv:2010.04808), Theorem A (every nonabelian simple group occurs as a composition factor), Theorem B (solvable examples of arbitrarily large nilpotency length and rank) and Theorem C (the p-length is 1 for every prime divisor p of |G|); Kourovka Archive, Problem 19.55, https://arxiv.org/abs/2010.04808.

Stated but not proved: `MathlibExt.GroupTheory.FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.pLengthAtMostOne_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FullPrimeMaximalSupersolubleKourovka19Problem55Wanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html#p-length-at-most-one-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Supersoluble maximal subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/supersoluble-maximal-subgroups)
