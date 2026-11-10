---
declaration: theorem
origin: cited
lean: Nat.DivisionGrowth.affine_lower_bound
statement: formalized
proof: formalized
---

# `Nat.DivisionGrowth.affine_lower_bound`

[`Nat.DivisionGrowth.affine_lower_bound`](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/SequenceGrowth/Data/Nat/DivisionGrowth.lean): if `0 < s < n` and
`∀ m, n * (u m / s) ≤ u (m + 1)`, then for every `m : ℕ`, with
`λ = (n : ℚ) / s` and `C = (n : ℚ) * ((s - 1 : ℕ) : ℚ) / ((n : ℚ) - s)`,
`λ ^ m * ((u 0 : ℚ) - C) + C ≤ (u m : ℚ)`. There is **no** seed condition.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/README.md#headline-results) of [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth) at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Nat.DivisionGrowth.affine_lower_bound` (theorem), declared in [SequenceGrowth/Data/Nat/DivisionGrowth.lean, line 71](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/SequenceGrowth/Data/Nat/DivisionGrowth.lean#L71).

Read from the source at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), without running Lean.

## Sources

- [sequence-growth at ccf81c71: README, headline results](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/README.md#headline-results)
- [Source of `Nat.DivisionGrowth.affine_lower_bound` in SequenceGrowth/Data/Nat/DivisionGrowth.lean](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/SequenceGrowth/Data/Nat/DivisionGrowth.lean#L71)
