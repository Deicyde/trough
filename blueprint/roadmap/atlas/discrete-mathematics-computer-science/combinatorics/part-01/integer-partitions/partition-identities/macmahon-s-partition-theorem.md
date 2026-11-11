---
declaration: section
origin: cited
lean: MetaMathlibExt.andrews_macmahon_partition_identity, MetaMathlibExt.macmahon_multiplicity_one_free
statement: formalized
proof: formalized
---

# MacMahon's partition theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/macmahon-s-partition-theorem/index.html).

## Andrews' generalization of MacMahon's partition theorem

For all natural numbers $r$ and
$n$, the number of partitions of $n$ in which every part occurring an odd number of times occurs
at least $2r + 1$ times equals the number of partitions of $n$ in which every odd part is
congruent to $2r + 1$ modulo $4r + 2$.

For $r = 1$ this is MacMahon's partition theorem: the first condition says that no part occurs
exactly once, and the second that every part is even or congruent to $3$ modulo $6$.

The proof compares generating functions in $q$. Both sides factor through the product over the
even parts, and the remaining factors agree by Euler's theorem that partitions into odd parts and
partitions into distinct parts are equinumerous, applied with $q$ replaced by $q^{2r+1}$.

## Sources

- Beaullah Mugwangwavari and Darlison Nyirenda, "A Note on the Andrews-Ericksson-Petrov-Romick Bijection for MacMahon's Partition Theorem", Journal of Integer Sequences 24 (2021), Article 21.5.6, Theorem `andthm` (Andrews' generalization), source lines 113–115, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Nyirenda/nyir26.tex>. The paper attributes the result to Andrews.

Formalized by `MetaMathlibExt.andrews_macmahon_partition_identity`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/AndrewsMacMahonPartition.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/AndrewsMacMahonPartition.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/macmahon-s-partition-theorem/index.html#andrews-macmahon-partition-identity).

## MacMahon's partition theorem

For every natural number $n$, the number of partitions of
$n$ in which no part occurs exactly once equals the number of partitions of $n$ all of whose parts
are even or congruent to $3$ modulo $6$.

The source states the theorem for $n \ge 1$; for $n = 0$ both counts are $1$, counting the empty
partition.

## Sources

- Beaullah Mugwangwavari and Darlison Nyirenda, "A Note on the Andrews-Ericksson-Petrov-Romick Bijection for MacMahon's Partition Theorem", Journal of Integer Sequences 24 (2021), Article 21.5.6, Theorem `MacMahon`, source lines 88–97 with the displayed statement at lines 91–93, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Nyirenda/nyir26.tex>. The paper attributes the theorem to P. A. MacMahon, *Combinatory Analysis*, Vol. 2 (1916).

Formalized by `MetaMathlibExt.macmahon_multiplicity_one_free`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/MacMahonMultiplicityOneFree.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/MacMahonMultiplicityOneFree.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/macmahon-s-partition-theorem/index.html#macmahon-multiplicity-one-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: MacMahon's partition theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/macmahon-s-partition-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/partition-identities/macmahon-s-partition-theorem)
