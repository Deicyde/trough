---
declaration: theorem
origin: cited
lean: IsLeftRegular.isUnit_of_isArtinianRing
statement: formalized
proof: formalized
---

# Left-regular elements in left Artinian rings

For an arbitrary unital
`Ring A` with `[IsArtinianRing A]`,
[`IsLeftRegular.isUnit_of_isArtinianRing`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Artinian/Regular.lean)
makes every left-regular element a unit. Artinianity concerns the original
left regular module; no opposite-Artinian, commutativity or nontriviality
hypothesis is required, and the carrier universe is arbitrary. The reverse
implication is already available through Mathlib's `IsUnit.isRegular`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `IsLeftRegular.isUnit_of_isArtinianRing` (theorem), declared in [CoherentModules/RingTheory/Artinian/Regular.lean, line 35](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Artinian/Regular.lean#L35).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `IsLeftRegular.isUnit_of_isArtinianRing` in CoherentModules/RingTheory/Artinian/Regular.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Artinian/Regular.lean#L35)
