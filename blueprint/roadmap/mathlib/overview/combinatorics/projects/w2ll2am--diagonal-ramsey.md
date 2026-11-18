---
declaration: theorem
origin: cited
lean: DiagRamsey.diagonal_le_3p4986238_pow, DiagRamsey.diagonal_le_exp_z
statement: formalized
---

# R(k,k) ≤ 3.4986238^k

[w2ll2am/diagonal-ramsey](https://github.com/w2ll2am/diagonal-ramsey) at commit [c2875f33](https://github.com/w2ll2am/diagonal-ramsey/tree/c2875f33a9d5c89f71c68f51b5767550570b5603), 2026-10-08.

> **R(k,k) ≤ 3.4986238^k** (an e^{1.2523697k} bound) for all sufficiently large k, formally verified in Lean 4 (Mathlib).

*Quoted from [README.md](https://github.com/w2ll2am/diagonal-ramsey/blob/c2875f33a9d5c89f71c68f51b5767550570b5603/README.md), MIT, Copyright (c) 2026 Zhipu Zhao, William Booth-Clibborn and Casper Schwahn.*

## Depends on

- [Exponential](../../analysis/special-functions/exponential.md)

## Proof depends on

- [List](../../data-structures/list-like-structures/list.md)
- [Simple graph](../graph-theory/simple-graph.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-02/squeeze-theorem.md)
- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Derivative at a point](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Real number](../../general-algebra/numbers/real-number.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`DiagRamsey.diagonal_le_3p4986238_pow`](https://github.com/w2ll2am/diagonal-ramsey/blob/c2875f33a9d5c89f71c68f51b5767550570b5603/SharpBound.lean#L34) (theorem)
- [`DiagRamsey.diagonal_le_exp_z`](https://github.com/w2ll2am/diagonal-ramsey/blob/c2875f33a9d5c89f71c68f51b5767550570b5603/SharpBound.lean#L12) (theorem)

## Project

- Lean v4.32.1, Mathlib at [520045ab](https://github.com/leanprover-community/mathlib4/tree/520045ab14e26149ee970e2e617ca04b09bde5d6).
- 82,192 .lean files; its Lean libraries `SharedDefinitions`, `Definitions`, `Bridge`, `BridgeLines`, `Lemmas`, `Solutions` and 2 more hold 5,000 (the first read), declaring 118,949 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: MIT ([LICENSE](https://github.com/w2ll2am/diagonal-ramsey/blob/c2875f33a9d5c89f71c68f51b5767550570b5603/LICENSE)).

## Builds on

- Mathlib, at [520045ab](https://github.com/leanprover-community/mathlib4/tree/520045ab14e26149ee970e2e617ca04b09bde5d6).
- `RamseyCurrent` (https://github.com/sichen-wang/diagonal-ramsey-numbers) at `5ec98f47`.

## Placement

Of its imports of Mathlib modules in an overview area, 15 of 64 are in Combinatorics, 5.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Combinatorics (15 of 64 imports, 5.4×), Analysis (28 of 64 imports, 1.6×), Data structures (7 of 64 imports, 0.8×). *Proof depends on* names 8 of the 14 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [w2ll2am/diagonal-ramsey at c2875f33](https://github.com/w2ll2am/diagonal-ramsey/tree/c2875f33a9d5c89f71c68f51b5767550570b5603)
