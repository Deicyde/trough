---
declaration: section
origin: cited
lean: MetaMathlibExt.partitionsEvenPartsDistinct_mod24_progressions, MetaMathlibExt.partitionsEvenPartsDistinct_mod24_five_power
statement: formalized
---

# Partitions with distinct even parts

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-distinct-even-parts/index.html).

## Congruences modulo 24 for partitions with distinct even parts

Write $\mathrm{ped}(m)$ for the
number of partitions of $m$ in which the even parts are distinct (odd parts may repeat). For every
natural number $n$, each of $\mathrm{ped}(225n+43)$, $\mathrm{ped}(225n+88)$,
$\mathrm{ped}(225n+133)$ and $\mathrm{ped}(225n+223)$ is congruent to $0$ modulo $24$.

## Sources

- Hemjyoti Nath, *New Congruences for Partitions Where the Even Parts Are Distinct*, INTEGERS 24 (2024), Article A79, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.partitionsEvenPartsDistinct_mod24_progressions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PartitionsEvenPartsDistinctWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/PartitionsEvenPartsDistinctWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-distinct-even-parts/index.html#partitions-even-parts-distinct-mod24-pro).

## Power-of-five congruence modulo 24 for partitions with distinct even parts

Write
$\mathrm{ped}(m)$ for the number of partitions of $m$ in which the even parts are distinct (odd
parts may repeat). For all natural numbers $k \ge 1$ and $n$,

$$
\mathrm{ped}(9n+7) \equiv \mathrm{ped}\left(9 \cdot 5^{2k} n + \frac{57 \cdot 5^{2k} - 1}{8}\right)
  \pmod{24}.
$$

The quotient is exact, since $57 \cdot 5^{2k} - 1$ is divisible by $8$.

## Sources

- Hemjyoti Nath, *New Congruences for Partitions Where the Even Parts Are Distinct*, INTEGERS 24 (2024), Article A79, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.partitionsEvenPartsDistinct_mod24_five_power` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PartitionsEvenPartsDistinctWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/PartitionsEvenPartsDistinctWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-distinct-even-parts/index.html#partitions-even-parts-distinct-mod24-fiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partitions with distinct even parts](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-distinct-even-parts/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-distinct-even-parts)
