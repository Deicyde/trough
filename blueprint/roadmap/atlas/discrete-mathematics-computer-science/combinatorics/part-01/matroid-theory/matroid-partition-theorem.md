---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Matroid.MatroidPartitionWanted.edmonds_matroid_partition', MathlibExt.Combinatorics.Matroid.MatroidPartitionWanted.edmonds_matroid_partition
statement: formalized
proof: formalized
---

# Matroid partition theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-partition-theorem/index.html).

## Edmonds' matroid partition theorem, arbitrary ground set

Let $E$ be a finite set, let $M$
be a matroid with ground set $E(M) \subseteq E$, let $S \subseteq E$ and let $k$ be a natural
number. Then $S = J_1 \cup \dots \cup J_k$ for some sets $J_1, \dots, J_k$ that are independent
in $M$ (not necessarily disjoint) if and only if $|X| \le k \, r_M(X)$ for every $X \subseteq S$,
where $r_M(X)$ denotes the rank in $M$ of $X \cap E(M)$.

Formalized by `MathlibExt.Combinatorics.Matroid.MatroidPartitionWanted.edmonds_matroid_partition'`, a theorem declared in [MathlibExt/Combinatorics/Matroid/MatroidPartition.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/MatroidPartition.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-partition-theorem/index.html#edmonds-matroid-partition).

## Edmonds' matroid partition theorem

Let $E$ be a finite set, let $M$ be a matroid whose
ground set is all of $E$, let $S \subseteq E$ and let $k$ be a natural number. Then
$S = J_1 \cup \dots \cup J_k$ for some sets $J_1, \dots, J_k$ that are independent in $M$ (not
necessarily disjoint) if and only if $|X| \le k \, r_M(X)$ for every $X \subseteq S$, where $r_M$
is the rank function of $M$.

## Sources

- J. Edmonds, Minimum partition of a matroid into independent subsets, J. Res. Natl. Bur. Standards Sect. B 69B (1965), 67-72, DOI 10.6028/jres.069B.004.

Formalized by `MathlibExt.Combinatorics.Matroid.MatroidPartitionWanted.edmonds_matroid_partition`, a theorem declared in [MathlibExt/Combinatorics/Matroid/MatroidPartition.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Matroid/MatroidPartition.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-partition-theorem/index.html#edmonds-matroid-partition-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matroid partition theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/matroid-partition-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/matroid-theory/matroid-partition-theorem)
