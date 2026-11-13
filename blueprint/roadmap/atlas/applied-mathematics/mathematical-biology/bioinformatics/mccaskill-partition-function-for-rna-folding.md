---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.RNA.PartitionFunction.CanPair, Cslib.Bioinformatics.RNA.PartitionFunction.inside, Cslib.Bioinformatics.RNA.PartitionFunction.outside, Cslib.Bioinformatics.RNA.PartitionFunction.structuresIn, Cslib.Bioinformatics.RNA.PartitionFunction.structures, Cslib.Bioinformatics.RNA.PartitionFunction.weight, Cslib.Bioinformatics.RNA.PartitionFunction.mem_structures, Cslib.Bioinformatics.RNA.PartitionFunction.inside_eq_sum
statement: formalized
proof: formalized
---

# McCaskill partition function for RNA folding

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html).

## Complementary base pairing of two positions

Positions `i` and `j` of `s` both lie in `s` and carry complementary bases.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.CanPair`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#can-pair).

## Inside recursion

**Inside recursion** over a commutative semiring `R`: `inside pair m s w i len` is the
weighted sum over the secondary structures supported in the interval `[i, i + len)` (proved in
`inside_eq_sum`). Base `i` is either unpaired, or paired with `i + 1 + k` for some `k ≥ m`
with `CanPair pair s i (i + 1 + k)`, which contributes `w i (i + 1 + k)` times the inside
values of the enclosed interval `[i + 1, i + 1 + k)` and of the outer interval
`[i + k + 2, i + len + 1)`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.inside`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#inside).

## Outside recursion

**Outside recursion** (McCaskill 1990) over a commutative semiring `R`, for a sequence of
length `n = s.length`: `outside pair m s w i j` is the weighted sum of the parts outside the
pair `(i, j)` of all structures containing it (proved in `outside_mul_eq_sum`). Either no pair
encloses `(i, j)`, leaving independent structures on `[0, i)` and `[j + 1, n)`, or there is a
unique innermost enclosing pair `(a, b)` (`a < i`, `j < b < n`), contributing the outside value
of `(a, b)`, its weight, and the inside values of `[a + 1, i)` and `[j + 1, b)`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.outside`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#outside).

## Secondary structures within an interval

The secondary structures on `s` (`IsStructure pair m s`) all of whose pairs lie in the
interval `[i, i + len)`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.structuresIn`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#structures-in).

## Set of all secondary structures of a sequence

All secondary structures on `s` with minimum hairpin `m` (see `mem_structures`).

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.structures`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#structures).

## Weight of a secondary structure

The weight of a structure: the product of the weights of its base pairs.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.weight`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#weight).

## Membership in the set of secondary structures

`structures` is exactly the set of secondary structures on `s`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.mem_structures`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#mem-structures).

## Inside algorithm

The inside recursion sums the weights of all secondary structures
supported in the interval `[i, i + len)`, over any commutative semiring.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.inside_eq_sum`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 614](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L614). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#inside-eq-sum).

## Inside value sums the weights of all secondary structures

The inside value of the whole sequence sums the weights of all its secondary structures.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.inside_eq_sum_structures`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#inside-eq-sum-structures).

## Outside algorithm

**Outside algorithm** (McCaskill 1990): for a candidate pair `(i, j)` (`i + m < j` and
`CanPair pair s i j`), the outside value times the pair's weight times the inside value of the
enclosed interval `[i + 1, j)` sums the weights of all secondary structures containing
`(i, j)`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.outside_mul_eq_sum`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#outside-mul-eq-sum).

## Tropical semiring

With every base pair weighted `-1` in the min-plus semiring
`MinTropical (WithTop ℤ)` (addition `min`, multiplication `+`), a structure with `k` pairs has
weight `-k`, so the inside value of the whole sequence is minus the Nussinov maximum number of
base pairs.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.inside_minTropical`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1464](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#inside-min-tropical).

## Waterman's recursion

**Waterman's recursion** for the number `S_m(n)` of secondary structures on `n` points
with minimum hairpin `m` when every pair is allowed: `S(0) = 1` and
`S(n + 1) = S(n) + ∑_{m ≤ k < n} S(k) S(n - 1 - k)` (Waterman 1978; Stein–Waterman 1979).
For `m = 0` these are the Motzkin numbers (`watermanNumber_zero_eq_motzkinNumber`); for `m = 1`
the Stein–Waterman numbers `1, 1, 1, 2, 4, 8, 17, 37, …` (OEIS A004148).

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.watermanNumber`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1497](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#waterman-number).

## Counting semiring

The number of secondary structures on `n` points with minimum
hairpin `m`, when every pair of positions may pair, is Waterman's number `S_m(n)`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.card_structures_eq_watermanNumber`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#card-structures-eq-waterman-number).

## Waterman numbers with no hairpin constraint are Motzkin numbers

For `m = 0` (no hairpin constraint) Waterman's numbers are the Motzkin numbers
`M(n) = ∑_k C(n, 2k) C(k)`: the number of non-crossing partial matchings on `n` points.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.watermanNumber_zero_eq_motzkinNumber`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1542](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1542). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#waterman-number-zero-eq-motzkin-number).

## Additive base-pair energy model

An **additive base-pair energy model**: the free energy of a structure is the sum of the
energies `e i j` of its base pairs (in the same units as `RT`).

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.energy`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#energy).

## McCaskill partition function of RNA secondary structures

The **partition function** `Z = ∑_S exp (-E(S) / RT)` over all secondary structures `S`
on `s` with minimum hairpin `m`, for the additive energy `e` at thermal energy `RT`
(physically `0 < RT`; the identities below hold for every real `RT`).

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.partitionFunction`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1568](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#partition-function).

## McCaskill's algorithm

**McCaskill's algorithm** (inside part): over the sum-product semiring `ℝ` with Boltzmann
weights `exp (-e i j / RT)`, the inside value of the whole sequence is the partition function.
This is an algebraic identity valid for every real `RT`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.inside_boltzmann_eq_partitionFunction`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1574](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1574). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#inside-boltzmann-eq-partition-function).

## Base-pair probability

The **base-pair probability** `P(i, j)`: the total weight of the structures containing the
pair `(i, j)`, divided by the total weight `Z` of all structures. For nonnegative weights `Z ≥ 1`
(the empty structure has weight `1`), so the denominator is positive; for Boltzmann weights this
is the probability of `(i, j)` under the Boltzmann distribution on structures.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.pairProb`, a definition declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1585](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#pair-prob).

## McCaskill's base-pair probabilities

For a candidate pair `(i, j)`,
`P(i, j) = outside(i, j) · w(i, j) · inside(i + 1, j) / inside(0, n)`.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.pairProb_eq_outside`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1591](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#pair-prob-eq-outside).

## Total structure weight is at least one

For nonnegative weights the total weight of all structures is at least `1`, the weight of
the empty structure; so the denominator of `pairProb` is positive.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.one_le_sum_weight`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#one-le-sum-weight).

## Nonnegativity of base-pair probabilities

Base-pair probabilities are nonnegative for nonnegative weights.

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.pairProb_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1610](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#pair-prob-nonneg).

## Each base pairs at most once

For nonnegative weights, the probabilities that base `i`
pairs with some later base `j` or some earlier base `j` sum to at most `1`
(`∑_j (P(i, j) + P(j, i)) ≤ 1`).

Formalized by `Cslib.Bioinformatics.RNA.PartitionFunction.sum_pairProb_le_one`, a theorem declared in [CSLibExt/Bioinformatics/RNA/PartitionFunction.lean, line 1618](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/RNA/PartitionFunction.lean#L1618). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html#sum-pair-prob-le-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: McCaskill partition function for RNA folding](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/mccaskill-partition-function-for-rna-folding)
