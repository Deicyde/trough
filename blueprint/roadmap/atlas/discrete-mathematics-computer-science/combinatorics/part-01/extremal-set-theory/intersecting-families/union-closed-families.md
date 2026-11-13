---
declaration: section
origin: cited
lean: MetaMathlibExt.binRep, MetaMathlibExt.setLT, MetaMathlibExt.setKey, MetaMathlibExt.famString, MetaMathlibExt.permImage, MetaMathlibExt.IsUnionClosed, MetaMathlibExt.IsCanonical, MetaMathlibExt.setLT_iff_setKey_lt
statement: formalized
proof: formalized
---

# Union-closed families

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html).

## Binary code of a subset

For a natural number $n$ and a subset $A$ of
$\{0, 1, \dots, n-1\}$, the binary code of $A$ is the natural number
$b(A) = \sum_{i \in A} 2^i$.

Formalized by `MetaMathlibExt.binRep`, a definition declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#bin-rep).

## Set order

For subsets $A$ and $B$ of $\{0, \dots, n-1\}$, $A$ precedes $B$ in the set
order, written $A < B$, if $|A| > |B|$, or $|A| = |B|$ and $b(A) < b(B)$, where
$b(A) = \sum_{i \in A} 2^i$ is the binary code of $A$.

Formalized by `MetaMathlibExt.setLT`, a definition declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#set-lt).

## Sort key of a subset

For a subset $A$ of $\{0, \dots, n-1\}$, the sort key of $A$ is
the natural number $(n - |A|) \cdot 2^n + b(A)$, where $b(A) = \sum_{i \in A} 2^i$ is the
binary code of $A$.

Since $b(A) < 2^n$, comparing sort keys as numbers agrees with the set order: larger sets come
first, and sets of the same size are ordered by binary code.

Formalized by `MetaMathlibExt.setKey`, a definition declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#set-key).

## String of a family

For a family $U$ of subsets of $\{0, \dots, n-1\}$, the string
$s(U)$ is the list of the sort keys of the nonempty members of $U$, in increasing order.

Formalized by `MetaMathlibExt.famString`, a definition declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#fam-string).

## Permuted image of a family

For a permutation $\sigma$ of $\{0, \dots, n-1\}$ and a
family $U$ of subsets of $\{0, \dots, n-1\}$, the permuted image $\sigma(U)$ is the family
$\{\sigma(A) : A \in U\}$, where $\sigma(A) = \{\sigma(a) : a \in A\}$.

Formalized by `MetaMathlibExt.permImage`, a definition declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#perm-image).

## Union-closed family

A family $U$ of subsets of $\{0, \dots, n-1\}$ is union-closed if
$A \cup B \in U$ for all $A, B \in U$.

Formalized by `MetaMathlibExt.IsUnionClosed`, a definition declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#is-union-closed).

## Canonical family

A family $U$ of subsets of $\{0, \dots, n-1\}$ is canonical, the
canonical representative of its isomorphism class, if for every permutation $\sigma$ of
$\{0, \dots, n-1\}$ the string $s(U)$ is lexicographically at most the string $s(\sigma(U))$
of the permuted family $\sigma(U)$.

Formalized by `MetaMathlibExt.IsCanonical`, a definition declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#is-canonical).

## The sort key encodes the set order

For all subsets $A$ and $B$ of $\{0, \dots, n-1\}$,
$A < B$ in the set order if and only if the sort key of $A$ is less than the sort key of $B$.

Formalized by `MetaMathlibExt.setLT_iff_setKey_lt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#set-lt-iff-set-key-lt).

## Prefixes of a sorted canonical family are canonical

Let $A_1, \dots, A_k$ be nonempty
subsets of $\{0, \dots, n-1\}$ with $A_i < A_j$ in the set order whenever $i < j$, and suppose
the family $U = \{\emptyset, A_1, \dots, A_k\}$ is canonical. Then for every $m \le k$, including
$m = 0$, the family $\{\emptyset, A_1, \dots, A_m\}$ is canonical.

Neither union closure nor coverage of the universe is needed.

Formalized by `MetaMathlibExt.orderly_canonical_prefix_of_sorted`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#orderly-canonical-prefix-of-sorted).

## Orderly generation of union-closed families

Let $n$, $k$ and $m$ be natural numbers with
$1 \le m \le k$, and let $A_1, \dots, A_k$ be nonempty subsets of $\Omega_n = \{0, \dots, n-1\}$
with $A_i < A_j$ in the set order whenever $i < j$. Suppose the family
$U = \{\emptyset, A_1, \dots, A_k\}$ is union-closed, every element of $\Omega_n$ lies in some
member of $U$, $U \ne \{\Omega_n, \emptyset\}$, and $U$ is canonical. Then the prefix family
$\{\emptyset, A_1, \dots, A_m\}$ is canonical.

The hypotheses that $U$ is union-closed, covers $\Omega_n$ and differs from
$\{\Omega_n, \emptyset\}$ are not used in the proof. The string of $U$ lists the sort keys of
$A_1, \dots, A_k$ in order, so the string of the prefix family is a prefix of it, and a
permutation that made the prefix family's string smaller would make the string of $U$ smaller.

## Sources

- Gunnar Brinkmann and Robin Deklerck, "Generation of Union-Closed Sets and Moore Families", Journal of Integer Sequences 21 (2018), Article 18.1.7, Theorem `thm:orderly`, source lines 275–281, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Brinkmann/brink6.tex>.

Formalized by `MetaMathlibExt.orderly_canonical_prefix`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/UnionClosedOrderly.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html#orderly-canonical-prefix).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Union-closed families](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-closed-families)
