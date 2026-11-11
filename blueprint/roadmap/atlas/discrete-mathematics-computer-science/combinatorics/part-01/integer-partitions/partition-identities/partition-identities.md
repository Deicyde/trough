---
declaration: section
origin: cited
lean: MetaMathlibExt.card_odd_countRestricted_four_eq_card_mod_four_pair_excluding, MetaMathlibExt.partitions_two_distant_eq_polarized, MathlibExt.Combinatorics.Enumerative.Partition.RogersRamanujanWanted.rogers_ramanujan_difference_two_vs_one_four
statement: formalized
proof: formalized
---

# Partition identities: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/index.html).

Theorems equating counts of two classes of partitions: Euler, MacMahon, Andrews, Andrews–Lewis, Rogers–Ramanujan, Stanley and Elder theorems, polarized and 2-distant partitions, colored Euler-type identities and Merca's sums of different parts.

## Andrews–Lewis identity

For every natural number $n$, the number of partitions of $n$ into
odd parts in which each part occurs at most three times equals the number of partitions of $n$
into parts congruent to $1$ or $3$ modulo $4$ such that for no natural number $j \le n$ are both
$4j + 1$ and $4j + 3$ parts.

## Sources

- the Andrews–Lewis identity (G. E. Andrews and R. P. Lewis, "An algebraic identity of F. H. Jackson and its implications for partitions," Discrete Math. 232 (2001), 77–83) as quoted in Michael D. Hirschhorn and James A. Sellers, "A Congruence Modulo 3 for Partitions into Distinct Non-Multiples of Four," Journal of Integer Sequences 17 (2014), Article 14.9.6, Theorem, lines 99–102. <https://cs.uwaterloo.ca/journals/JIS/VOL17/Sellers/sellers32.tex>

Formalized by `MetaMathlibExt.card_odd_countRestricted_four_eq_card_mod_four_pair_excluding`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/OddBoundedMultiplicity.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/OddBoundedMultiplicity.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/index.html#card-odd-count-restricted-four-eq-card-m).

## Partitions with 2-distant parts and polarized partitions

For every natural number $n$, the
number of partitions of $n$ into distinct parts any two of which differ by at least $2$ equals the
number of polarized partitions of $n$, that is, partitions of $n$ into distinct parts in which
every even part is greater than twice the number of odd parts.

## Sources

- Ivica Martinjak and Dragutin Svrtan, "New Identities for the Polarized Partitions and Partitions with d-Distant Parts," Journal of Integer Sequences 17 (2014), Article 14.11.4, Theorem 1, lines 150–155, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Martinjak/mart3.tex>.

Formalized by `MetaMathlibExt.partitions_two_distant_eq_polarized`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/TwoDistantPolarized.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/TwoDistantPolarized.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/index.html#partitions-two-distant-eq-polarized).

## Rogers–Ramanujan identity (first form)

For every natural number $n$, the number of
partitions of $n$ into distinct parts, any two of which differ by at least $2$, equals the number
of partitions of $n$ all of whose parts are congruent to $1$ or $4$ modulo $5$.

## Sources

- George E. Andrews and David Newman, "The Minimal Excludant in Integer Partitions," Journal of Integer Sequences 23 (2020), Article 20.2.3, quoted Rogers–Ramanujan theorem at lines 173–178. Public TeX URL: <https://cs.uwaterloo.ca/journals/JIS/VOL23/Andrews/andrews5.tex>

Formalized by `MathlibExt.Combinatorics.Enumerative.Partition.RogersRamanujanWanted.rogers_ramanujan_difference_two_vs_one_four`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RogersRamanujan.lean, line 2645](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/RogersRamanujan.lean#L2645). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/index.html#rogers-ramanujan-difference-two-vs-one-f).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition identities](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/partition-identities)
