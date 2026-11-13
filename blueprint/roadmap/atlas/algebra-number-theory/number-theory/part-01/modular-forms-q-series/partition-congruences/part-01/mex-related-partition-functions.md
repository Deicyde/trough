---
declaration: section
origin: cited
lean: MetaMathlibExt.mesh_partition_congruence_lift, MetaMathlibExt.partitionMex, MetaMathlibExt.mexPartitionNumber, MetaMathlibExt.ramanujanDelta, MetaMathlibExt.ramanujan_mex_partition_congruences
statement: formalized
---

# Mex-related partition functions

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions/index.html).

## Lifting partition congruences to mex partition functions

For a partition $\lambda$, a
positive integer $A$ and a natural number $c$, let $\operatorname{mex}_{A,c}(\lambda)$ be the
smallest positive integer congruent to $c$ modulo $A$ that is not a part of $\lambda$, and let
$p_{A,c}(N)$ be the number of partitions $\lambda$ of $N$ with
$\operatorname{mex}_{A,c}(\lambda) \equiv c \pmod{2A}$. Let $p(N)$ be the number of partitions of
$N$. Let $m$, $a$ and $b$ be natural numbers with $m \ge 1$ and $b < a$, and suppose that $m$
divides $p(an + b)$ for every natural number $n$. Then for every integer $t \ge 1$ and every
natural number $n$, $m$ divides both $p_{at,at}(an + b)$ and $p_{2at,at}(an + b)$.

Because $b < a$, the hypothesis covers the whole residue class of $b$ modulo $a$; for $b \ge a$
the lift would need $p$ at arguments below $b$, which the hypothesis does not cover.

The proof follows the Andrews–Newman mex decomposition used by Barman and Singh: remove one copy
of every forced earlier mex candidate. The exact-mex fibers then telescope, while every removed
prefix sum remains a multiple of $a$.

## Sources

- Rupam Barman and Ajit Singh, "Mex-Related Partition Functions of Andrews and Newman," Journal of Integer Sequences 24 (2021), Article 21.6.3, Theorem, lines 172–182, https://cs.uwaterloo.ca/journals/JIS/VOL24/Barman/barman3.tex

Formalized by `MetaMathlibExt.mesh_partition_congruence_lift`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/MexPartitionCongruenceLift.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/MexPartitionCongruenceLift.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions/index.html#mesh-partition-congruence-lift).

## Mex of a partition in a residue class

For natural numbers $A$, $a$ and $n$ and a
partition $\lambda$ of $n$, $\operatorname{mex}_{A,a}(\lambda)$ is the smallest positive integer
congruent to $a$ modulo $A$ that is not a part of $\lambda$, and $0$ if there is no such integer
(which happens only when $A = 0$).

Formalized by `MetaMathlibExt.partitionMex`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions/index.html#partition-mex).

## Mex-related partition function of Andrews and Newman

For natural numbers $A$, $a$ and $n$,
$p_{A,a}(n)$ is the number of partitions $\lambda$ of $n$ such that
$\operatorname{mex}_{A,a}(\lambda) \equiv a \pmod{2A}$, where $\operatorname{mex}_{A,a}(\lambda)$
is the smallest positive integer congruent to $a$ modulo $A$ that is not a part of $\lambda$, and
$0$ if there is no such integer.

Formalized by `MetaMathlibExt.mexPartitionNumber`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions/index.html#mex-partition-number).

## Least inverse of 24 modulo a power

For natural numbers $p$ and $k$, $\delta_{p,k}$ is the
least natural number $\delta$ with $24\delta \equiv 1 \pmod{p^k}$, and $0$ if there is no such
$\delta$, which happens exactly when $p^k$ and $24$ have a common factor greater than $1$.

Formalized by `MetaMathlibExt.ramanujanDelta`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions/index.html#ramanujan-delta).

## Ramanujan congruences for mex-related partition functions

For a positive integer $A$, a
natural number $a$ and a partition $\lambda$, let $\operatorname{mex}_{A,a}(\lambda)$ be the
smallest positive integer congruent to $a$ modulo $A$ that is not a part of $\lambda$; let
$p_{A,a}(N)$ be the number of partitions $\lambda$ of $N$ with
$\operatorname{mex}_{A,a}(\lambda) \equiv a \pmod{2A}$; and let $\delta_{p,k}$ be the least
natural number $\delta$ with $24\delta \equiv 1 \pmod{p^k}$. Then for all natural numbers
$k \ge 1$, $t \ge 1$ and $n$, for each $p \in \{5, 7, 11\}$ and for both $A = p^k t$ and
$A = 2p^k t$,

$$p_{A,\,p^k t}(p^k n + \delta_{p,k}) \equiv 0 \pmod{p^{e}},$$

where $e = k$ for $p = 5$ and $p = 11$, and $e = \lfloor k/2 \rfloor + 1$ for $p = 7$.

## Sources

- Barman–Singh, JIS 24 (2021), Art. 21.6.3, corollary.

Stated but not proved: `MetaMathlibExt.ramanujan_mex_partition_congruences` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RamanujanMexPartitionCongruencesWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions/index.html#ramanujan-mex-partition-congruences).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mex-related partition functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/mex-related-partition-functions)
