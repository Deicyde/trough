---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPartialParkingFunction, MetaMathlibExt.IsParkingFunction, MetaMathlibExt.isParkingFunction_iff_card_filter_le, MetaMathlibExt.PollakPartialParking.pollak_partial_parking_functions_card
statement: formalized
proof: formalized
---

# Parking functions: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/index.html).

Parking functions and their variants (partial, weakly increasing, k-Naples, metered) and statistics on them: lucky cars, descents, displacement, and lucky statistics of Stirling permutations read as parking preferences.

## Partial parking function

Let $s, t \in \mathbb{N}$ and number the $t$ spots
$0, \dots, t-1$. A map $f : \{0, \dots, s-1\} \to \{0, \dots, t-1\}$, giving the preferred spot
of each of $s$ cars, is a partial parking function if for every spot $k \in \{0, \dots, t-1\}$,
at most $t - k$ cars $i$ satisfy $f(i) \ge k$.

Formalized by `MetaMathlibExt.IsPartialParkingFunction`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ParkingFunction.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ParkingFunction.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/index.html#is-partial-parking-function).

## Parking function

Let $n \in \mathbb{N}$ and number the $n$ spots $0, \dots, n-1$.
A map $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$, giving the preferred spot of each of
$n$ cars, is a parking function if it is a partial parking function with $n$ cars and $n$
spots, that is, if for every spot $k$, at most $n - k$ cars $i$ satisfy $f(i) \ge k$.

Formalized by `MetaMathlibExt.IsParkingFunction`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ParkingFunction.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ParkingFunction.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/index.html#is-parking-function).

## Lower-tail characterization of parking functions

Let $n \in \mathbb{N}$, number
the $n$ spots $0, \dots, n-1$, and let $f : \{0, \dots, n-1\} \to \{0, \dots, n-1\}$ give the
preferred spot of each of $n$ cars. Then $f$ is a parking function if and only if, for every
spot $k \in \{0, \dots, n-1\}$, at least $k + 1$ cars $i$ satisfy $f(i) \le k$.

Formalized by `MetaMathlibExt.isParkingFunction_iff_card_filter_le`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/ParkingFunction.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/ParkingFunction.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/index.html#is-parking-function-iff-card-filter-le).

## Number of partial parking functions

Let $s$ and $t$ be natural numbers with
$0 < s \le t$. A partial parking function with $s$ cars and $t$ spots is a map
$f : \{0, \dots, s - 1\} \to \{0, \dots, t - 1\}$ such that for every spot
$k \in \{0, \dots, t - 1\}$ at most $t - k$ cars $i$ have $f(i) \ge k$. The number of partial
parking functions with $s$ cars and $t$ spots is $(t + 1 - s)(t + 1)^{s - 1}$.

The proof is Pollak's circle argument.

## Sources

- Steve Butler, Kimberly Hadaway, Victoria Lenius, Preston Martens, and Marshall Moats, “Lucky Cars and Lucky Spots in Parking Functions”, Journal of Integer Sequences 29 (2026), Article 26.1.1, proposition at lines 330–332 of https://cs.uwaterloo.ca/journals/JIS/VOL29/Hadaway/had3.tex.

Formalized by `MetaMathlibExt.PollakPartialParking.pollak_partial_parking_functions_card`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PollakPartialParkingFunctions.lean, line 1308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PollakPartialParkingFunctions.lean#L1308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/index.html#pollak-partial-parking-functions-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parking functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/parking-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/parking-functions)
