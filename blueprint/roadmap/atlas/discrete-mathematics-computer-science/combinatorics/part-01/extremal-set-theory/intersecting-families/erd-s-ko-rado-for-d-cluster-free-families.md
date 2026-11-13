---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ClusterFreeErdosKoRadoOWR1386Problem011Wanted.IsKdFamily, MathlibExt.Combinatorics.ClusterFreeErdosKoRadoOWR1386Problem011Wanted.kdFamilyErdosKoRado, MathlibExt.Combinatorics.ClusterFreeErdosKoRadoOWR1386Problem011Wanted.kdFamilyErdosKoRado_holds
statement: formalized
---

# Erdős–Ko–Rado for d-cluster-free families

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/erd-s-ko-rado-for-d-cluster-free-families/index.html).

## $K(d)$-families

Let $n$, $k$ and $d$ be natural numbers and let
$[n] = \{0, 1, \dots, n - 1\}$. A family $G$ of subsets of $[n]$ is a $K(d)$-family of
$k$-subsets when every member of $G$ has exactly $k$ elements and any $d$ distinct members
$A_1, \dots, A_d$ of $G$ with $|A_1 \cup \dots \cup A_d| \le 2k$ have a common element.

Formalized by `MathlibExt.Combinatorics.ClusterFreeErdosKoRadoOWR1386Problem011Wanted.IsKdFamily`, a definition declared in [WantedExt/Combinatorics/ClusterFreeErdosKoRadoOWR1386Problem011Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ClusterFreeErdosKoRadoOWR1386Problem011Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/erd-s-ko-rado-for-d-cluster-free-families/index.html#is-kd-family).

## Mubayi's Erdős–Ko–Rado conjecture for $K(d)$-families

For all natural numbers $n$, $k$
and $d$ with $3 \le d \le k$ and $n \ge dk/(d - 1)$, every $K(d)$-family $G$ of $k$-subsets of
$[n] = \{0, 1, \dots, n - 1\}$ satisfies $|G| \le \binom{n-1}{k-1}$, and if
$|G| = \binom{n-1}{k-1}$ then some element of $[n]$ lies in every member of $G$.

## Sources

- D. Mubayi, Oberwolfach Report 48/2006, Conjecture 3.

Formalized by `MathlibExt.Combinatorics.ClusterFreeErdosKoRadoOWR1386Problem011Wanted.kdFamilyErdosKoRado`, a definition declared in [WantedExt/Combinatorics/ClusterFreeErdosKoRadoOWR1386Problem011Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ClusterFreeErdosKoRadoOWR1386Problem011Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/erd-s-ko-rado-for-d-cluster-free-families/index.html#kd-family-erdos-ko-rado).

## Mubayi's Erdős–Ko–Rado conjecture for $K(d)$-families holds

For all natural numbers $n$, $k$
and $d$ with $3 \le d \le k$ and $n \ge dk/(d - 1)$, every $K(d)$-family $G$ of $k$-subsets of
$[n] = \{0, 1, \dots, n - 1\}$ satisfies $|G| \le \binom{n-1}{k-1}$, and if
$|G| = \binom{n-1}{k-1}$ then some element of $[n]$ lies in every member of $G$.

Currier proved the bound for $2 \le d \le k$, with the equality case for $d \ge 3$.

## Sources

- D. Mubayi, in Combinatorics, Probability and Computing, Oberwolfach Reports 3 (2006), no. 48, p. 2922, Conjecture 3, DOI 10.4171/OWR/2006/48; resolution: G. Currier, On the d-cluster generalization of Erdős-Ko-Rado, J. Combin. Theory Ser. A 182 (2021), 105464, arXiv:1812.11153, abstract and Theorem 2: for 2 ≤ d ≤ k and n ≥ dk/(d - 1), a family of k-subsets of [n] with no d-cluster (d members with empty intersection and union of size at most 2k) has at most C(n - 1, k - 1) members, with equality only for a full star (d ≥ 3); this resolves Mubayi's conjecture, https://arxiv.org/abs/1812.11153.

Stated but not proved: `MathlibExt.Combinatorics.ClusterFreeErdosKoRadoOWR1386Problem011Wanted.kdFamilyErdosKoRado_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ClusterFreeErdosKoRadoOWR1386Problem011Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ClusterFreeErdosKoRadoOWR1386Problem011Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/erd-s-ko-rado-for-d-cluster-free-families/index.html#kd-family-erdos-ko-rado-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős–Ko–Rado for d-cluster-free families](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/erd-s-ko-rado-for-d-cluster-free-families/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/erd-s-ko-rado-for-d-cluster-free-families)
