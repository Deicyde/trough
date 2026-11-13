---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Ewens.ewensProb, MathlibExt.Biology.PopulationGenetics.Ewens.sum_ewensProb, MathlibExt.Biology.PopulationGenetics.Ewens.ewensProb_nonneg, MathlibExt.Biology.PopulationGenetics.Ewens.sum_ewensProb_mul_card_parts, MathlibExt.Biology.PopulationGenetics.Ewens.hoppeStep, MathlibExt.Biology.PopulationGenetics.Ewens.hoppeLaw, MathlibExt.Biology.PopulationGenetics.Ewens.hoppeStep_nonneg, MathlibExt.Biology.PopulationGenetics.Ewens.sum_hoppeStep
statement: formalized
proof: formalized
---

# Ewens sampling formula and the Chinese restaurant process

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html).

## Ewens sampling formula

The **Ewens sampling formula**: the probability, under the neutral infinite-alleles model
with scaled mutation rate `θ = 4Nu`, that a sample of `n` genes has allelic partition `π`
(`π.parts.count j` alleles carried by exactly `j` genes each):
`n! * (∏ j, (θ / j) ^ (a j) / (a j)!) / θ^{(n)}` (Ewens 1972), for `θ > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.ewensProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#ewens-prob).

## The Ewens sampling formula is a probability distribution

**The Ewens sampling formula is a probability distribution** on the partitions of `n`
(Ewens 1972; equivalently, Cauchy's cycle-type formula `∑_{σ ∈ S_n} θ^{#cycles σ} = θ^{(n)}`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.sum_ewensProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#sum-ewens-prob).

## Nonnegativity of the Ewens sampling formula

The Ewens sampling formula is nonnegative for `θ > 0`; with `sum_ewensProb` it is a
probability distribution on the partitions of `n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.ewensProb_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#ewens-prob-nonneg).

## Expected number of alleles

**Expected number of alleles** in a sample of `n` genes under the Ewens sampling formula:
`E[K_n] = ∑_{i < n} θ / (θ + i)` (Ewens 1972).

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.sum_ewensProb_mul_card_parts`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#sum-ewens-prob-mul-card-parts).

## One step of Hoppe's urn

One step of **Hoppe's urn** on allelic partitions (Hoppe 1984): from a partition `π` of
`k`, the next gene carries a new allele with probability `θ / (θ + k)` (target parts
`1 ::ₘ π.parts`), and copies an allele carried by `j` genes with probability
`j * a j / (θ + k)`, where `a j = π.parts.count j` (target parts
`(j + 1) ::ₘ π.parts.erase j`). The value is the transition probability from `π` to `π'`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.hoppeStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#hoppe-step).

## Law of the allelic partition from Hoppe's urn

The law of the allelic partition after `n` draws from Hoppe's urn, started from the empty
sample: `hoppeLaw θ (n + 1) π' = ∑ π, hoppeLaw θ n π * hoppeStep θ π π'`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.hoppeLaw`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#hoppe-law).

## Hoppe urn transition probabilities are nonnegative

Hoppe-urn transition probabilities are nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.hoppeStep_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#hoppe-step-nonneg).

## Hoppe urn transition is stochastic

The Hoppe-urn transition is stochastic: from every partition of `k` the probabilities of
the partitions of `k + 1` sum to one.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.sum_hoppeStep`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#sum-hoppe-step).

## Hoppe's urn generates the Ewens sampling formula

**Hoppe's urn generates the Ewens sampling formula** (Hoppe 1984): after `n` draws, the
allelic partition has law `ewensProb θ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.hoppeLaw_eq_ewensProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#hoppe-law-eq-ewens-prob).

## Nonnegativity of the Hoppe urn law

The law of Hoppe's urn after `n` draws is nonnegative for `θ > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.hoppeLaw_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Ewens.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Ewens.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#hoppe-law-nonneg).

## Seating a customer at a new table

Seat customer `n` at a new table: the partition of `Fin (n + 1)` whose blocks are the
blocks of `π` (relabeled into `Fin (n + 1)`) together with the singleton `{n}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.newTable`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#new-table).

## Seating a customer at an occupied table

Seat customer `n` at the occupied table `B` of `π`: the block `B` becomes `B ∪ {n}` and
the other blocks are unchanged.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.joinTable`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#join-table).

## Blocks of the partition after opening a new table

The blocks of `newTable π`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.parts_newTable`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#parts-new-table).

## Blocks of the partition after joining a table

The blocks of `joinTable π B hB`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.parts_joinTable`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#parts-join-table).

## Seating a customer by a seating choice

Seat customer `n` according to the choice `c`: `none` opens a new table, `some B` joins
the occupied table `B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.seat`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#seat).

## Seating probabilities in the Chinese restaurant process

The probability of each seating choice for customer `n` given the partition `π` of the
first `n` customers: `θ / (n + θ)` for a new table, `|B| / (n + θ)` for the table `B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.seatWeight`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#seat-weight).

## Nonnegativity of seating probabilities

The seating probabilities are nonnegative for `θ > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.seatWeight_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#seat-weight-nonneg).

## Seating probabilities sum to one

The seating probabilities sum to one for `θ > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.sum_seatWeight`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#sum-seat-weight).

## Seating choice distribution of a customer

The seating choice of customer `n`, as a probability distribution.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.seatChoice`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#seat-choice).

## One step of the Chinese restaurant process

One step of the Chinese restaurant process: the law of the partition of `Fin (n + 1)`
given the partition `π` of the first `n` customers.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crpStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-step).

## Chinese restaurant process

The **Chinese restaurant process** with parameter `θ > 0`: the law of the random
partition of the customers `Fin n` into tables, built one customer at a time by `crpStep`
(Aldous 1985, §11; Pitman 2006, ch. 3).

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp).

## Closed-form law of the Chinese restaurant process

The closed-form law of the Chinese restaurant process,
`θ^{|π|} ∏_{B ∈ π} (|B| - 1)! / θ^{(n)}` (Pitman 2006, §3.1). Every block is nonempty,
so `|B| - 1` is never a truncated natural subtraction.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crpProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-prob).

## Removing the last customer undoes a seating

Removing the last customer undoes every seating: restricting `seat π c` to the first `n`
customers gives back `π`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.comap_castSucc_seat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#comap-cast-succ-seat).

## Injectivity of seating

Different seating choices give different partitions.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.seat_injective`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#seat-injective).

## Every partition arises from seating the last customer

Every partition of `Fin (n + 1)` arises by seating customer `n` into its restriction to
the first `n` customers.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.exists_seat_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#exists-seat-eq).

## Seating multiplies the closed-form law by the seating probability

One seating multiplies the closed-form law by the seating probability.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crpProb_seat`, a lemma declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-prob-seat).

## Law of the Chinese restaurant process

**Law of the Chinese restaurant process** (Pitman 2006, §3.1):
`P(π) = θ^{|π|} ∏_{B ∈ π} (|B| - 1)! / θ^{(n)}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-apply).

## Chinese restaurant process law as a real number

The law of the Chinese restaurant process as a real number.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_toReal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-to-real).

## Exchangeability

**Exchangeability**, pointwise: relabeling the customers by a permutation `σ` does not
change the probability of a partition.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_comap_perm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-comap-perm).

## Exchangeability of the Chinese restaurant process

**Exchangeability of the Chinese restaurant process** (Aldous 1985, §11): the law of the
partition relabeled by any permutation of the customers is the law of the partition.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_map_comap_perm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-map-comap-perm).

## Consistency of the Chinese restaurant process

Restricting the random partition of
`Fin (n + 1)` to the first `n` customers gives the process with `n` customers.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_map_restrict`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-map-restrict).

## Consistency for every sample size

Restricting the random partition of `Fin n` to the
first `m ≤ n` customers gives the process with `m` customers.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_map_restrict_castLE`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-map-restrict-cast-le).

## Allelic partition of a set partition

The allelic partition of a set partition of `Fin n`: the multiset of its block sizes, a
partition of the integer `n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.blockSizes`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#block-sizes).

## The block sizes follow Hoppe's urn

The law of the multiset of block sizes after `n`
customers is the law `Ewens.hoppeLaw` of Hoppe's urn on allelic partitions after `n` draws.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_map_blockSizes_eq_hoppeLaw`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-map-block-sizes-eq-hoppe-law).

## The allelic partition of the Chinese restaurant process follows the Ewens sampling formula

**The allelic partition of the Chinese restaurant process follows the Ewens sampling
formula** (Ewens 1972; Hoppe 1984): the multiset of block sizes after `n` customers has law
`Ewens.ewensProb θ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.crp_map_blockSizes`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 678](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#crp-map-block-sizes).

## Expected number of tables

**Expected number of tables** (expected number of alleles in a sample of `n` genes,
Ewens 1972): `E[|π|] = ∑_{i < n} θ / (θ + i)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ChineseRestaurant.sum_crp_toReal_mul_card_parts`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ChineseRestaurant.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html#sum-crp-to-real-mul-card-parts).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ewens sampling formula and the Chinese restaurant process](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/ewens-sampling-formula-and-the-chinese-restauran)
