---
declaration: theorem
origin: cited
lean: Nat.DivisionGrowth.eventually_dominates
statement: formalized
proof: formalized
---

# `Nat.DivisionGrowth.eventually_dominates`

Under the same recurrence,
`0 < s`, `0 < b`, `s * b < n`, and the sufficient natural seed
`n * (s - 1) < (n - s) * u 0`, for **each** `K : ℕ` there is `M : ℕ`
such that **every** `m ≥ M` satisfies `K * b ^ m < u m`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/README.md#headline-results) of [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth) at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Nat.DivisionGrowth.eventually_dominates` (theorem), declared in [SequenceGrowth/Data/Nat/DivisionGrowth.lean, line 99](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/SequenceGrowth/Data/Nat/DivisionGrowth.lean#L99).

Read from the source at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), without running Lean.

## Sources

- [sequence-growth at ccf81c71: README, headline results](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/README.md#headline-results)
- [Source of `Nat.DivisionGrowth.eventually_dominates` in SequenceGrowth/Data/Nat/DivisionGrowth.lean](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/SequenceGrowth/Data/Nat/DivisionGrowth.lean#L99)
