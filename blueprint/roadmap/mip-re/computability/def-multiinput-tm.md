---
declaration: definition
origin: cited
lean: Turing.MultiInputTM, Turing.MultiInputTM.ComputesInTimeAndSpace
statement: formalized
---

# Multi-input Turing machine

A *multi-input Turing machine* with $i$ input tapes and $w$ work tapes has $i$ two-way read-only input tapes (heads clamped one blank cell beyond either end of the input), $w$ bidirectional work tapes over an alphabet extended with a blank symbol, and a write-only output stream. A transition may write and move on every work tape, move every input head, emit at most one output symbol, and either continue or halt. Time is counted in steps, and space as the number of work-tape cells visited.

At $i = 1$ this is exactly the CSLib multi-tape model.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Turing.MultiInputTM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.MultiInputTM), [`Turing.MultiInputTM.ComputesInTimeAndSpace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.MultiInputTM.ComputesInTimeAndSpace).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 20](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L20)
