---
declaration: theorem
origin: cited
lean: Perennial.goose_crash_adequacy, Perennial.github_com.mit_pdos.perennial.goose.testdata.examples.crashfs.crash_safety, Perennial.goose_dist_adequacy, Perennial.goose_dist_crash_adequacy, Perennial.github_com.mit_pdos.perennial.goose.testdata.examples.netfs.netfs_crash_safety, Perennial.TimeReceiptsTest.wp_clock_incr, Perennial.ThreadTokensTest.wp_counter_register, Perennial.strings.wp_Join
statement: formalized
---

# Perennial

[mit-pdos/perennial](https://github.com/mit-pdos/perennial) at commit [6d365ee1](https://github.com/mit-pdos/perennial/tree/6d365ee1aac396061ed93e644a7f5aa53228ced9), 2026-11-17.

## Depends on

- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Rational number](../../../mathlib/overview/general-algebra/numbers/rational-number.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Language](../../../mathlib/overview/logic-and-computation/formal-languages/language.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Prime numbers](../../../mathlib/undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Main results

Its Lean names are 8 of the 10 theorems its README names in code:

- [`Perennial.goose_crash_adequacy`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/GooseLang/CrashAdequacy.lean#L440) (theorem)
- [`Perennial.github_com.mit_pdos.perennial.goose.testdata.examples.crashfs.crash_safety`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/Proof/github_com/mit_pdos/perennial/goose/testdata/examples/crashfs/Results.lean#L143) (theorem)
- [`Perennial.goose_dist_adequacy`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/GooseLang/DistAdequacy.lean#L466) (theorem)
- [`Perennial.goose_dist_crash_adequacy`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/GooseLang/DistAdequacy.lean#L744) (theorem)
- [`Perennial.github_com.mit_pdos.perennial.goose.testdata.examples.netfs.netfs_crash_safety`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/Proof/github_com/mit_pdos/perennial/goose/testdata/examples/netfs/Results.lean#L329) (theorem)
- [`Perennial.TimeReceiptsTest.wp_clock_incr`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/ProgramLogic/TimeReceiptsTest.lean#L74) (theorem)
- [`Perennial.ThreadTokensTest.wp_counter_register`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/ProgramLogic/ThreadTokensTest.lean#L106) (theorem)
- [`Perennial.strings.wp_Join`](https://github.com/mit-pdos/perennial/blob/6d365ee1aac396061ed93e644a7f5aa53228ced9/Perennial/Proof/strings/Link.lean#L38) (theorem)

Of the files its headlines import, directly or not, `Perennial/GeneratedProof/strings.lean` hold `sorry` or `admit`.

## Project

- Lean v4.34.1.
- 1,682 .lean files; its Lean libraries `Perennial`, `PerennialMeta` hold 1,645, declaring 30,246 names, with `sorry` in 15 files and 3722 axioms, read without Lean.
- No license file; facts only.

## Builds on

- `iris` (https://github.com/leanprover-community/iris-lean) at `6d6544a4`.

## Placement

It requires neither Mathlib nor another library mapped here; 1 file of the project import Batteries modules.

## Mathlib use

*Proof depends on* names 6 of the 8 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [mit-pdos/perennial at 6d365ee1](https://github.com/mit-pdos/perennial/tree/6d365ee1aac396061ed93e644a7f5aa53228ced9)
