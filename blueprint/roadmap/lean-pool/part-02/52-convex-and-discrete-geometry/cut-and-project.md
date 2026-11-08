---
declaration: theorem
origin: cited
lean: CutAndProject.main_theorem_geometric_concrete
statement: formalized
proof: formalized
---

# Period Lengths of Rational Cut-and-Project Gap Sequences

> Formalizes the closed-form minimal periods of one-dimensional rational cut-and-project gap sequences at the level of the paper's residue model, plus a fully geometric aperiodicity theorem for irrational slopes. For coprime α, β ∈ ℕ and window parameter ω ≥ 0, write N = ⌊ωα⌋ + ⌊ωβ⌋ + 1 and D = α² + β². The strip-to-residue reduction of the paper — sorting the hits of the length-N progression twisted by the geometric multiplier −αβ⁻¹ (mod D) — is taken as the definition of the gap sequence rather than derived from the lattice; for it, the multiset convention has minimal period N/D when D ∣ N and N otherwise, and the set convention (multiplicities flattened to {0,1}) has minimal period 1 when N ≥ D and N otherwise. The irrational case is geometric from first principles: for positive irrational slope and ω > 0, the accepted points of ℤ² sorted by the physical projection have a gap sequence with no finite period, via injectivity of the projection and Kronecker density of the internal image.

*Quoted from the card [LeanPool/projects/cut-and-project.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/cut-and-project.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`CutAndProject.main_theorem_geometric_concrete`](https://leanpool.github.io/lean-pool/LeanPool/CutAndProject/Basic.html#CutAndProject.main_theorem_geometric_concrete) (theorem; a main declaration), declared in [LeanPool/CutAndProject/Basic.lean, line 2585](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CutAndProject/Basic.lean#L2585): “The gap sequence of the residue model of the rational cut-and-project multiset (sorted hits of the length-N progression under the multiplier −αβ⁻¹ mod D) has minimal period N/D if D divides N and N otherwise, where N = ⌊ωα⌋ + ⌊ωβ⌋ + 1 and D = α² + β².”
- [`CutAndProject.set_main_theorem_geometric_concrete`](https://leanpool.github.io/lean-pool/LeanPool/CutAndProject/Basic.html#CutAndProject.set_main_theorem_geometric_concrete) (theorem), declared in [LeanPool/CutAndProject/Basic.lean, line 2949](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CutAndProject/Basic.lean#L2949): “The set-convention residue-model gap sequence (multiplicities flattened to {0,1}) has minimal period 1 if N ≥ D and N otherwise.”
- [`CutAndProject.Irrational.prop_irrational`](https://leanpool.github.io/lean-pool/LeanPool/CutAndProject/Irrational.html#CutAndProject.Irrational.prop_irrational) (theorem), declared in [LeanPool/CutAndProject/Irrational.lean, line 891](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CutAndProject/Irrational.lean#L891): “For positive irrational slope and window parameter ω > 0, the projected gap sequence has no finite period.”

## Project

- Authors: Dirk Kunert.
- Source: *Period lengths of one-dimensional rational cut-and-project sequences* by Dirk Kunert, [https://github.com/dkunert/cut-and-project/blob/main/LaTeX/rational_cut_and_project_gap_periods.tex](https://github.com/dkunert/cut-and-project/blob/main/LaTeX/rational_cut_and_project_gap_periods.tex).
- Project repository: [dkunert/cut-and-project](https://github.com/dkunert/cut-and-project).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2026 Dirk Kunert”.
- MSC2020: 52C23, 11K06.
- In Lean Pool: [LeanPool/CutAndProject](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CutAndProject), from the card [LeanPool/projects/cut-and-project.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/cut-and-project.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/cut-and-project.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/cut-and-project.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CutAndProject](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CutAndProject)
