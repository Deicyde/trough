---
declaration: theorem
origin: cited
lean: FiveEighths.commProb_le_five_eighths
statement: formalized
proof: formalized
---

# The 5/8 theorem

> Proves Gustafson's 5/8 theorem — the Mathlib commuting probability of a nonabelian group is at most 5/8, with the infinite case immediate from commProb being zero — via the finite-group index bounds for the center and centralizers of noncentral elements.

*Quoted from the card [LeanPool/projects/five-eighths-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/five-eighths-theorem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`FiveEighths.commProb_le_five_eighths`](https://leanpool.github.io/lean-pool/LeanPool/FiveEighthsTheorem/Basic.html#FiveEighths.commProb_le_five_eighths) (theorem; a main declaration), declared in [LeanPool/FiveEighthsTheorem/Basic.lean, line 240](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiveEighthsTheorem/Basic.lean#L240): “The commuting probability of a nonabelian group is at most 5/8.”
- [`FiveEighths.centralFraction_le_quarter`](https://leanpool.github.io/lean-pool/LeanPool/FiveEighthsTheorem/Basic.html#FiveEighths.centralFraction_le_quarter) (theorem), declared in [LeanPool/FiveEighthsTheorem/Basic.lean, line 92](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiveEighthsTheorem/Basic.lean#L92): “The center of a finite nonabelian group contains at most a quarter of its elements.”
- [`FiveEighths.centralizerFraction_le_half`](https://leanpool.github.io/lean-pool/LeanPool/FiveEighthsTheorem/Basic.html#FiveEighths.centralizerFraction_le_half) (theorem), declared in [LeanPool/FiveEighthsTheorem/Basic.lean, line 114](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiveEighthsTheorem/Basic.lean#L114): “The centralizer of a noncentral element of a finite group contains at most half of its elements.”

## Project

- Authors: Xuanji Li.
- Source: *What is the probability that two group elements commute?* by W. H. Gustafson, [doi:10.2307/2317564](https://doi.org/10.2307/2317564).
- Project repository: [ldct/lean-monorepo](https://github.com/ldct/lean-monorepo).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 20P05.
- In Lean Pool: [LeanPool/FiveEighthsTheorem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiveEighthsTheorem), from the card [LeanPool/projects/five-eighths-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/five-eighths-theorem.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/five-eighths-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/five-eighths-theorem.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FiveEighthsTheorem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiveEighthsTheorem)
