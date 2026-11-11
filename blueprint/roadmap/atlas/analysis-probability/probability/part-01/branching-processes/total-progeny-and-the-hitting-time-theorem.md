---
declaration: section
origin: cited
lean: MathlibExt.Probability.GaltonWatson.IsFirstPassage, MathlibExt.Probability.GaltonWatson.rotate, MathlibExt.Probability.GaltonWatson.card_filter_isFirstPassage_rotate, MathlibExt.Probability.GaltonWatson.walkWeight, MathlibExt.Probability.GaltonWatson.hittingWeight, MathlibExt.Probability.GaltonWatson.natCast_mul_hittingWeight, MathlibExt.Probability.GaltonWatson.measure_firstPassage, MathlibExt.Probability.GaltonWatson.measure_walk
statement: formalized
proof: formalized
---

# Total progeny and the hitting-time theorem

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html).

## First passage of the exploration walk

The exploration walk started at `k` with steps `x_i - 1` stays positive at every time
`j < n`: `j < k + ∑_{i < j} x_i`. Together with `∑ x_i + k = n` this says that the walk first
hits `0` at time `n`.

Formalized by `MathlibExt.Probability.GaltonWatson.IsFirstPassage`, a definition declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#is-first-passage).

## Cyclic shift of a tuple

The cyclic shift `i ↦ x_{(i + r) mod n}` of a tuple.

Formalized by `MathlibExt.Probability.GaltonWatson.rotate`, a definition declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#rotate).

## Cycle lemma

**Cycle lemma** (Dvoretzky–Motzkin 1947). If `x : Fin n → ℕ` satisfies `∑ x_i + k = n` with
`1 ≤ k`, then exactly `k` of the `n` cyclic shifts of `x` (counted by shift `r < n`) are
first-passage sequences.

Formalized by `MathlibExt.Probability.GaltonWatson.card_filter_isFirstPassage_rotate`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#card-filter-is-first-passage-rotate).

## Walk weight of step sequences ending at zero

The weight `W_p(k, n) = ∑ ∏_i p(x_i)` over the step sequences `x : Fin n → ℕ` with
`∑ x_i + k = n` (the walk from `k` is at `0` at time `n`). For `p(j) = P(ξ = j)` this is
`P(ξ_1 + ⋯ + ξ_n = n - k)` when `k ≤ n`, and `0` when `k > n`.

Formalized by `MathlibExt.Probability.GaltonWatson.walkWeight`, a definition declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#walk-weight).

## Hitting weight of first-passage step sequences

The weight `H_p(k, n) = ∑ ∏_i p(x_i)` over the step sequences with `∑ x_i + k = n` along
which the walk from `k` first hits `0` at time `n`. For `p(j) = P(ξ = j)` this is the
probability `P(T = n)` that the total progeny of `k` ancestors is `n`.

Formalized by `MathlibExt.Probability.GaltonWatson.hittingWeight`, a definition declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#hitting-weight).

## Hitting-time theorem

**Hitting-time theorem**, weighted form: `n · H_p(k, n) = k · W_p(k, n)` for every weight
`p` with values in a commutative semiring and all `k, n`. For probability weights this is the
hitting-time theorem of van der Hofstad–Keane (2008); the proof double counts cyclic shifts
with the cycle lemma.

Formalized by `MathlibExt.Probability.GaltonWatson.natCast_mul_hittingWeight`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#nat-cast-mul-hitting-weight).

## Probability of first passage at time n

Under `ν^{⊗n}`, the event that the walk from `k` first hits `0` at time `n` has
measure `H_p(k, n)` with `p(j) = ν{j}`. When `ν` is a probability measure this is the
probability `P(T = n)`.

Formalized by `MathlibExt.Probability.GaltonWatson.measure_firstPassage`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#measure-first-passage).

## Probability of the offspring walk event as a walk weight

Under `ν^{⊗n}`, the event `ξ_1 + ⋯ + ξ_n + k = n` has measure `W_p(k, n)` with
`p(j) = ν{j}`. When `ν` is a probability measure this is the probability
`P(ξ_1 + ⋯ + ξ_n = n - k)`.

Formalized by `MathlibExt.Probability.GaltonWatson.measure_walk`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#measure-walk).

## Otter–Dwass formula

For i.i.d. offspring numbers with law `ν` and `k` ancestors,
the finite-measure identity
`n · P(T = n) = k · P(ξ_1 + ⋯ + ξ_n = n - k)` holds as an identity of event masses
(Otter 1949; Dwass 1969); the two sides are probabilities when `ν` is a probability
measure.

Formalized by `MathlibExt.Probability.GaltonWatson.natCast_mul_measure_firstPassage`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#nat-cast-mul-measure-first-passage).

## Walk weights for Poisson offspring

For Poisson(`r`) step weights, `W_p(k, n) = e^{-rn} (rn)^{n-k} / (n-k)!` when `k ≤ n`:
the sum of `n` independent Poisson(`r`) variables is Poisson(`rn`).

Formalized by `MathlibExt.Probability.GaltonWatson.walkWeight_poisson`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#walk-weight-poisson).

## Borel–Tanner law

For Poisson(`r`) offspring and `k ≤ n` ancestors,
`n · P(T = n) = k e^{-rn} (rn)^{n-k} / (n-k)!` (Tanner 1961; Haight–Breuer 1960).

Formalized by `MathlibExt.Probability.GaltonWatson.natCast_mul_hittingWeight_poisson`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#nat-cast-mul-hitting-weight-poisson).

## Borel law

For Poisson(`r`) offspring and one ancestor, the total progeny satisfies
`P(T = n) = e^{-rn} (rn)^{n-1} / n!` for `n ≥ 1` (Borel 1942).

Formalized by `MathlibExt.Probability.GaltonWatson.hittingWeight_poisson_one`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#hitting-weight-poisson-one).

## Mean total progeny of a Galton–Watson process

The mean total progeny `∑_n E Z_n` of the Galton–Watson process started from one individual.
By Tonelli this is `E ∑_n Z_n` for any process with the generation laws `law ν n`.

Formalized by `MathlibExt.Probability.GaltonWatson.meanTotalProgeny`, a definition declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#mean-total-progeny).

## Mean total progeny equals $1/(1-m)$

The mean total progeny is `(1 - m)⁻¹` in `[0, ∞]`: it is `1 / (1 - m)` for `m < 1` and `∞`
for `m ≥ 1` (`m` the mean offspring number).

Formalized by `MathlibExt.Probability.GaltonWatson.meanTotalProgeny_eq`, a theorem declared in [MathlibExt/Probability/BranchingProcess/TotalProgeny.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/TotalProgeny.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html#mean-total-progeny-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Total progeny and the hitting-time theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/branching-processes/total-progeny-and-the-hitting-time-theorem)
