---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BloomFilter, Cslib.Algorithms.Lean.BloomFilter.empty, Cslib.Algorithms.Lean.BloomFilter.insert, Cslib.Algorithms.Lean.BloomFilter.mayContain, Cslib.Algorithms.Lean.BloomFilter.bit_insert_iff, Cslib.Algorithms.Lean.BloomFilter.mayContain_iff, Cslib.Algorithms.Lean.BloomFilter.mayContain_insert_self, Cslib.Algorithms.Lean.BloomFilter.mayContain_insert_mono
statement: formalized
proof: formalized
---

# Bloom filter

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html).

## Bloom filter

A Bloom filter over a type $\alpha$ with $m$ bits consists of a finite list of
hash functions $\alpha \to \{0, \dots, m - 1\}$ and a bit vector of length $m$.

No false-positive rate is claimed because the model supplies no probability distribution.

Formalized by `Cslib.Algorithms.Lean.BloomFilter`, a structure declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#bloom-filter).

## Empty Bloom filter

Let $\alpha$ be a type and $m$ a natural number. Given a list of hash
functions $\alpha \to \{0, \dots, m - 1\}$, the empty Bloom filter with these hash functions has
all of its $m$ bits unset.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.empty`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#empty).

## Bloom filter insertion

Inserting an element $x$ into a Bloom filter keeps its hash functions
and sets bit $h(x)$ for every hash function $h$ of the filter, leaving all other bits unchanged.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.insert`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#insert).

## Bloom filter membership query

A Bloom filter reports that an element $x$ may be present
when bit $h(x)$ is set for every hash function $h$ of the filter, and reports $x$ absent
otherwise.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.mayContain`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#may-contain).

## Bits set by an insertion

Let $F$ be a Bloom filter over $\alpha$ with $m$ bits, let
$x \in \alpha$ and let $i \in \{0, \dots, m - 1\}$. Bit $i$ of the filter obtained by inserting
$x$ into $F$ is set if and only if bit $i$ of $F$ is set or some hash function $h$ of $F$
satisfies $h(x) = i$.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.bit_insert_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#bit-insert-iff).

## Membership query in terms of bits

For a Bloom filter $F$ and an element $x$, $F$ reports
that $x$ may be present if and only if bit $h(x)$ of $F$ is set for every hash function $h$ of
$F$.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.mayContain_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#may-contain-iff).

## An inserted element is reported present

For every Bloom filter $F$ and element $x$, the
filter obtained by inserting $x$ into $F$ reports that $x$ may be present.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.mayContain_insert_self`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#may-contain-insert-self).

## Insertion preserves positive answers

Let $F$ be a Bloom filter and let $x$, $y$ be elements.
If $F$ reports that $x$ may be present, then so does the filter obtained by inserting $y$ into $F$.

Insertion never clears a bit, so an element reported present stays reported present after any
later insertion; in particular there are no false negatives under further inserts.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.mayContain_insert_mono`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#may-contain-insert-mono).

## The empty Bloom filter reports every element absent

Let $\alpha$ be a type, $m$ a
natural number and $H$ a nonempty list of hash functions $\alpha \to \{0, \dots, m - 1\}$. For
every element $x \in \alpha$, the empty Bloom filter with hash functions $H$ reports $x$ absent.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.mayContain_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilter.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#may-contain-empty).

## Inserting a list of elements into a Bloom filter

Insert every element of a list, left to right.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.insertAll`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#insert-all).

## Bloom filter insertion keeps the hash functions

Insertion keeps the hash functions.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.hashes_insertAll`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#hashes-insert-all).

## Bits set after inserting a list into a Bloom filter

After inserting a list, bit `i` is set iff it was set before or some hash function sends
some inserted element to `i`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.bit_insertAll_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#bit-insert-all-iff).

## Characterization of the Bloom filter false-positive event

The false-positive event: after inserting `xs` into an empty filter, `y` is reported
present iff every bit selected by `y` is selected by some stored element.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.mayContain_insertAll_empty_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#may-contain-insert-all-empty-iff).

## Bits set by the stored hash values

The bits set by the stored hash values `H a j` (element `a`, hash function `j`).

Formalized by `Cslib.Algorithms.Lean.BloomFilter.setBits`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#set-bits).

## A Bloom filter bit is unset iff no stored hash selects it

A bit is unset iff no stored hash value selects it.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.notMem_setBits_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#not-mem-set-bits-iff).

## Exact Bloom filter false-positive rate under uniform hashing

The exact false-positive rate under uniform hashing: the fraction of outcomes (stored hash
values `H`, query hash values `q`) in which every query bit is set.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.falsePositiveProb`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#false-positive-prob).

## Number of hash outcomes leaving a given bit unset

Exactly `(m - 1) ^ (n * k)` outcomes of the stored hash values leave bit `i` unset.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.card_unset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#card-unset).

## Probability that a given Bloom filter bit is unset

A given bit is unset with probability `(1 - 1/m) ^ (n * k)`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.prob_unset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#prob-unset).

## Expected fraction of set bits in a Bloom filter

The expected fraction of set bits is `1 - (1 - 1/m) ^ (n * k)`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.expected_fraction_set`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#expected-fraction-set).

## False-positive rate as the expected k-th power of the set fraction

The exact false-positive rate is the expectation of `(fraction of set bits) ^ k`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.falsePositiveProb_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#false-positive-prob-eq).

## Bloom's formula is a lower bound

**Bloom's formula is a lower bound** on the exact false-positive rate (Jensen's
inequality for `t ↦ t ^ k`).

Formalized by `Cslib.Algorithms.Lean.BloomFilter.classical_le_falsePositiveProb`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#classical-le-false-positive-prob).

## Exponential approximation is a lower bound on the false-positive rate

The exponential approximation `(1 - exp (-(k n) / m)) ^ k` is also a lower bound.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.exp_approx_le_falsePositiveProb`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#exp-approx-le-false-positive-prob).

## Bound $\log t \cdot \log(1-t) \le (\log 2)^2$ on the unit interval

`log t * log (1 - t) ≤ (log 2) ^ 2` on `(0, 1)`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.log_mul_log_one_sub_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#log-mul-log-one-sub-le).

## Equality in the log-product bound holds only at $t = 1/2$

Equality holds only at `t = 1 / 2`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.log_mul_log_one_sub_eq_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#log-mul-log-one-sub-eq-iff).

## Exponential approximation of the Bloom filter false-positive rate

The exponential approximation `(1 - exp (-κ n / m)) ^ κ` of the false-positive rate, as a
function of a real number `κ` of hash functions.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.expApprox`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#exp-approx).

## Exponential approximation at the optimal number of hash functions

At `κ = (m / n) log 2` half of the bits are expected to be set and the approximation is
`(1 / 2) ^ κ`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.expApprox_at_optimum`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#exp-approx-at-optimum).

## The optimal number of hash functions

**The optimal number of hash functions** for the exponential approximation: on real
`κ > 0`, `(1 - exp (-κ n / m)) ^ κ` is minimal at `κ = (m / n) log 2`.

Formalized by `Cslib.Algorithms.Lean.BloomFilter.expApprox_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BloomFilterFalsePositive.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html#exp-approx-optimal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bloom filter](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/hashing/bloom-filter/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/hashing/bloom-filter)
