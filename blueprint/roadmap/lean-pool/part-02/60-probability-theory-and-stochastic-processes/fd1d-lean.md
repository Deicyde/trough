---
declaration: theorem
origin: cited
lean: FD1D.V5.Palomar.optimalDynamicMatchingUpperBound
statement: formalized
proof: formalized
---

# Optimal fully dynamic matching on the line

> Constructs a measurable hierarchical policy for fully dynamic matching of uniformly arriving demand and replenishment on the unit interval. Proves logarithmic-over-inventory bounds for long-run root-mean-square distance from every initial inventory and for initialized finite-horizon expected average cost.

*Quoted from the card [LeanPool/projects/fd1d-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fd1d-lean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FD1D.V5.Palomar.optimalDynamicMatchingUpperBound`](https://leanpool.github.io/lean-pool/LeanPool/FullyDynamicMatching/FD1D/V5/PaperStatements.html#FD1D.V5.Palomar.optimalDynamicMatchingUpperBound) (theorem; a main declaration), declared in [LeanPool/FullyDynamicMatching/FD1D/V5/PaperStatements.lean, line 136](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FullyDynamicMatching/FD1D/V5/PaperStatements.lean#L136): “For every inventory size m at least two, an online policy has long-run RMS cost at most (72000/log 2) log(m+1)/m from every initial inventory, and the same expected-average-cost bound after initialization for horizons at least 2m².”

## Project

- Authors: Yash Kanoria.
- Project repository: [ykanoria/fd1d-lean](https://github.com/ykanoria/fd1d-lean), at commit [26a5b4e2](https://github.com/ykanoria/fd1d-lean/tree/26a5b4e2fd83fa86053239e09e92af370c62f18c).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 60J20, 90B15.
- In Lean Pool: [LeanPool/FullyDynamicMatching](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FullyDynamicMatching), from the card [LeanPool/projects/fd1d-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fd1d-lean.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/fd1d-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fd1d-lean.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FullyDynamicMatching](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FullyDynamicMatching)
