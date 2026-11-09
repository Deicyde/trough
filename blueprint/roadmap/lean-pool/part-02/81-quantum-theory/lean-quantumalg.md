---
declaration: theorem
origin: cited
lean: QuantumAlg.GroverSearch.main_success_probability
statement: formalized
proof: formalized
---

# Lean-QuantumAlg

> Provides a Mathlib-based library of formally verified quantum-algorithm definitions, primitives, and endpoints, including QFT, QSP, quantum kernels, amplitude amplification, Grover search, phase estimation, order finding, teleportation, and a Lie-algebraic barren-plateau witness.

*Quoted from the card [LeanPool/projects/lean-quantumalg.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-quantumalg.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`QuantumAlg.QuantumFourierTransform.main`](https://leanpool.github.io/lean-pool/LeanPool/LeanQuantumAlg/Primitives/QFT.html#QuantumAlg.QuantumFourierTransform.main) (theorem), declared in [LeanPool/LeanQuantumAlg/Primitives/QFT.lean, line 235](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg/Primitives/QFT.lean#L235): “Proves the QFT action on computational-basis states and records exact circuit counts.”
- [`QuantumAlg.ReflectionBasedQuantumSignalProcessing.main`](https://leanpool.github.io/lean-pool/LeanPool/LeanQuantumAlg/Primitives/QSP/Chebyshev.html#QuantumAlg.ReflectionBasedQuantumSignalProcessing.main) (theorem), declared in [LeanPool/LeanQuantumAlg/Primitives/QSP/Chebyshev.lean, line 590](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg/Primitives/QSP/Chebyshev.lean#L590): “Characterizes reflection-based single-qubit QSP transforms in the Chebyshev basis.”
- [`QuantumAlg.TrigonometricQuantumSignalProcessing.main`](https://leanpool.github.io/lean-pool/LeanPool/LeanQuantumAlg/Primitives/QSP/Fourier.html#QuantumAlg.TrigonometricQuantumSignalProcessing.main) (theorem), declared in [LeanPool/LeanQuantumAlg/Primitives/QSP/Fourier.lean, line 1001](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg/Primitives/QSP/Fourier.lean#L1001): “Characterizes trigonometric single-qubit QSP transforms in the YZZYZ form.”
- [`QuantumAlg.QuantumKernel.main`](https://leanpool.github.io/lean-pool/LeanPool/LeanQuantumAlg/Primitives/QKernel/Fidelity.html#QuantumAlg.QuantumKernel.main) (theorem), declared in [LeanPool/LeanQuantumAlg/Primitives/QKernel/Fidelity.lean, line 140](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg/Primitives/QKernel/Fidelity.lean#L140): “Proves that fidelity quantum-kernel Gram matrices are positive semidefinite.”
- [`QuantumAlg.QuantumKernelAdvantage.separation`](https://leanpool.github.io/lean-pool/LeanPool/LeanQuantumAlg/Primitives/QKernel/Advantage.html#QuantumAlg.QuantumKernelAdvantage.separation) (theorem), declared in [LeanPool/LeanQuantumAlg/Primitives/QKernel/Advantage.lean, line 92](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg/Primitives/QKernel/Advantage.lean#L92): “States the conditional quantum-kernel learning separation from discrete-log hardness.”
- [`QuantumAlg.fullControllability_hasBarrenPlateau`](https://leanpool.github.io/lean-pool/LeanPool/LeanQuantumAlg/Primitives/QNN/FullDLABasis.html#QuantumAlg.fullControllability_hasBarrenPlateau) (theorem), declared in [LeanPool/LeanQuantumAlg/Primitives/QNN/FullDLABasis.lean, line 174](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg/Primitives/QNN/FullDLABasis.lean#L174): “Exhibits an exponentially vanishing loss-variance family for a fully controllable dynamical Lie algebra, conditional on the assumed Ragone second-moment variance law (the Haar/Weingarten averaging identity Var = P_g(rho)\*P_g(O)/dim, taken as a hypothesis rather than derived from a circuit twirl).”
- [`QuantumAlg.GroverSearch.main_success_probability`](https://leanpool.github.io/lean-pool/LeanPool/LeanQuantumAlg/Algorithms/Grover.html#QuantumAlg.GroverSearch.main_success_probability) (theorem; a main declaration), declared in [LeanPool/LeanQuantumAlg/Algorithms/Grover.lean, line 106](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg/Algorithms/Grover.lean#L106): “Derives Grover search success probability from the amplitude-amplification closed form.”

## Project

- Authors: QudeLeap Team.
- Source: *Lean-QuantumAlg* by QudeLeap Team.
- Project repository: [QudeLeap/Lean-QuantumAlg](https://github.com/QudeLeap/Lean-QuantumAlg).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 81P68, 81P45, 68Q12.
- In Lean Pool: [LeanPool/LeanQuantumAlg](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg), from the card [LeanPool/projects/lean-quantumalg.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-quantumalg.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lean-quantumalg.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-quantumalg.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LeanQuantumAlg](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LeanQuantumAlg)
