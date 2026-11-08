---
declaration: theorem
origin: cited
lean: MiLAC.HybridCouplersPhaseShifters.implementable_dft
statement: formalized
proof: formalized
---

# Microwave network synthesis and power-of-two DFT implementation

> Characterizes the complex transmission matrices synthesized from phase shifters and permutations, with or without hybrid couplers, using series and parallel composition. Phase-only networks are permuted phase-diagonal matrices; networks with hybrid couplers are products of permutation and phase-parametrized block-diagonal layers. Proves that the normalized DFT of every power-of-two size is implementable, with reusable finite-type reindexing, independent row and column permutations, and block-diagonal composition infrastructure. Uses the reciprocal matched network matrix model of the source paper; no general scattering-physics theorem is claimed.

*Quoted from the card [LeanPool/projects/microwave-networks.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/microwave-networks.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`MiLAC.PhaseShifters.implementable_iff_permutedPhaseDiagonal`](https://leanpool.github.io/lean-pool/LeanPool/MicrowaveNetworks/PhaseShifters.html#MiLAC.PhaseShifters.implementable_iff_permutedPhaseDiagonal) (theorem), declared in [LeanPool/MicrowaveNetworks/PhaseShifters.lean, line 131](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MicrowaveNetworks/PhaseShifters.lean#L131): “A finite phase-only network is implementable exactly when its matrix is a permutation matrix times a diagonal matrix of complex phases.” Its source, as the card gives it: “Upstream PhaseShifters.lean.”
- [`MiLAC.HybridCouplersPhaseShifters.implementable_iff_layered`](https://leanpool.github.io/lean-pool/LeanPool/MicrowaveNetworks/HybridCouplersPhaseShifters.html#MiLAC.HybridCouplersPhaseShifters.implementable_iff_layered) (theorem), declared in [LeanPool/MicrowaveNetworks/HybridCouplersPhaseShifters.lean, line 581](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MicrowaveNetworks/HybridCouplersPhaseShifters.lean#L581): “A finite network is implementable with hybrid couplers and phase shifters exactly when its matrix is an initial permutation preceded by finitely many permutation and phase-parametrized block-diagonal layers.” Its source, as the card gives it: “Theorem 1 and Section IV of arXiv:2610.04774.”
- [`MiLAC.HybridCouplersPhaseShifters.implementable_dft`](https://leanpool.github.io/lean-pool/LeanPool/MicrowaveNetworks/HybridCouplersPhaseShifters.html#MiLAC.HybridCouplersPhaseShifters.implementable_dft) (theorem; a main declaration), declared in [LeanPool/MicrowaveNetworks/HybridCouplersPhaseShifters.lean, line 642](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MicrowaveNetworks/HybridCouplersPhaseShifters.lean#L642): “For every natural L, the normalized DFT matrix of size 2^L can be implemented by hybrid couplers, phase shifters, and permutation networks.” Its source, as the card gives it: “Section V of arXiv:2610.04774.”

## Project

- Authors: Matteo Nerini, Claude AI.
- Source: *Toward a Lean Formalization of Analog Computing with Microwaves*, [arXiv:2610.04774](https://arxiv.org/abs/2610.04774), [https://github.com/matteonerini/formalizing-analog-computing/tree/a89c1e9263658c20a29046f9ed1a8eeb867dd537](https://github.com/matteonerini/formalizing-analog-computing/tree/a89c1e9263658c20a29046f9ed1a8eeb867dd537).
- Project repository: [matteonerini/formalizing-analog-computing](https://github.com/matteonerini/formalizing-analog-computing), at commit [a89c1e92](https://github.com/matteonerini/formalizing-analog-computing/tree/a89c1e9263658c20a29046f9ed1a8eeb867dd537).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 94A12, 15A23, 42A38.
- In Lean Pool: [LeanPool/MicrowaveNetworks](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MicrowaveNetworks), from the card [LeanPool/projects/microwave-networks.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/microwave-networks.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/microwave-networks.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/microwave-networks.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MicrowaveNetworks](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MicrowaveNetworks)
