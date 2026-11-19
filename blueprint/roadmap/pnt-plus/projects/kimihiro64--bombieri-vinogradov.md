---
declaration: theorem
origin: cited
lean: BombieriVinogradov.PrimeCountingConversion.weighted_to_prime_counting
statement: formalized
proof: formalized
---

# Bombieri-Vinogradov in Lean

[kimihiro64/bombieri-vinogradov](https://github.com/kimihiro64/bombieri-vinogradov) at commit [7a174830](https://github.com/kimihiro64/bombieri-vinogradov/tree/7a1748306e026825ed6a5555516cc2f28989b2ac), 2026-09-05.

> A Lean 4 formalization of the Bombieri-Vinogradov theorem in the level-of-distribution form used by modern bounded-prime-gap arguments.

*Quoted from [README.md](https://github.com/kimihiro64/bombieri-vinogradov/blob/7a1748306e026825ed6a5555516cc2f28989b2ac/README.md), Apache-2.0.*

## Depends on

- [Robin1984](kimihiro64--robin1984.md)

## Proof depends on

- [Complex number](../../mathlib/overview/general-algebra/numbers/complex-number.md)
- [Real number](../../mathlib/overview/general-algebra/numbers/real-number.md)
- [Arithmetic functions](../../mathlib/overview/general-algebra/number-theory/arithmetic-functions.md)
- [Logarithm](../../mathlib/overview/analysis/special-functions/logarithm.md)
- [Bochner integral](../../mathlib/overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Finite](../../mathlib/overview/combinatorics/pigeonhole-principles/finite.md)
- [Fourier transform as an integral](../../mathlib/overview/analysis/fourier-analysis/fourier-transform-as-an-integral.md)
- [Natural number](../../mathlib/overview/general-algebra/numbers/natural-number.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`BombieriVinogradov.PrimeCountingConversion.weighted_to_prime_counting`](https://github.com/kimihiro64/bombieri-vinogradov/blob/7a1748306e026825ed6a5555516cc2f28989b2ac/BombieriVinogradov/Assembly/PrimeCountingConversion/Main.lean#L24) (theorem)

No file its headlines import, directly or not (819 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 852 .lean files; its Lean libraries `BombieriVinogradov`, `Challenge`, `Solution` hold 852, declaring 1,686 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/kimihiro64/bombieri-vinogradov/blob/7a1748306e026825ed6a5555516cc2f28989b2ac/LICENSE)).

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- [PrimeNumberTheoremAnd](../README.md) at `0f15a38c`, a GitHub fork of AlexKontorovich/PrimeNumberTheoremAnd.
- [Robin1984](kimihiro64--robin1984.md) at `bfa72aec`.

## Placement

Its Lake manifest requires `PrimeNumberTheoremAnd`, a GitHub fork of AlexKontorovich/PrimeNumberTheoremAnd, whose modules 77 files of the project import.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (599 of 2287 imports, 1.8×), General algebra (885 of 2287 imports, 1.1×), Analysis (667 of 2287 imports, 1.1×). *Proof depends on* lists 8 of the 38 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [kimihiro64/bombieri-vinogradov at 7a174830](https://github.com/kimihiro64/bombieri-vinogradov/tree/7a1748306e026825ed6a5555516cc2f28989b2ac)
