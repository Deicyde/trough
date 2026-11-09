---
declaration: theorem
origin: cited
lean: CircuitComplexity.shannon_lower_bound_circuit
statement: formalized
proof: formalized
---

# Circuit Complexity in Lean 4

> A Lean 4 formalization of classical Boolean circuit complexity, including the Shannon counting lower bound, Schnorr's XOR gate lower bound, a gate-elimination lower bound, CNF/DNF lower bounds for parity, and nondeterministic quantification complexity bounds.

*Quoted from the card [LeanPool/projects/circuit-complexity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/circuit-complexity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CircuitComplexity.shannon_lower_bound_circuit`](https://leanpool.github.io/lean-pool/LeanPool/CircuitComplexity/Internal/Bridge.html#CircuitComplexity.shannon_lower_bound_circuit) (theorem; a main declaration), declared in [LeanPool/CircuitComplexity/Internal/Bridge.lean, line 217](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity/Internal/Bridge.lean#L217): “For N at least 6, there exists a Boolean function on N inputs that cannot be computed by any fan-in-2 AND/OR circuit of size at most 2^N / (5N).”
- [`CircuitComplexity.schnorr_lower_bound_circuit`](https://leanpool.github.io/lean-pool/LeanPool/CircuitComplexity/Internal/Bridge.html#CircuitComplexity.schnorr_lower_bound_circuit) (theorem), declared in [LeanPool/CircuitComplexity/Internal/Bridge.lean, line 235](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity/Internal/Bridge.lean#L235): “Any fan-in-2 AND/OR circuit computing the N-input XOR function (or its complement) has at least 2(N-1) internal gates.”
- [`CircuitComplexity.Circuit.gate_elimination_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/CircuitComplexity/Internal/LowerBound.html#CircuitComplexity.Circuit.gate_elimination_lower_bound) (theorem), declared in [LeanPool/CircuitComplexity/Internal/LowerBound.lean, line 167](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity/Internal/LowerBound.lean#L167): “Any circuit over bounded fan-in k AND/OR computing a function with n' essential inputs has size at least n' / k.”
- [`CircuitComplexity.DNF.xorBool_complexity_lb`](https://leanpool.github.io/lean-pool/LeanPool/CircuitComplexity/NF.html#CircuitComplexity.DNF.xorBool_complexity_lb) (theorem), declared in [LeanPool/CircuitComplexity/NF.lean, line 42](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity/NF.lean#L42): “Any DNF formula computing the N-input XOR function requires at least 2^(N-1) terms.”
- [`CircuitComplexity.CNF.xorBool_complexity_lb`](https://leanpool.github.io/lean-pool/LeanPool/CircuitComplexity/NF.html#CircuitComplexity.CNF.xorBool_complexity_lb) (theorem), declared in [LeanPool/CircuitComplexity/NF.lean, line 49](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity/NF.lean#L49): “Any CNF formula computing the N-input XOR function requires at least 2^(N-1) clauses.”
- [`CircuitComplexity.existQuantify_complexity_le`](https://leanpool.github.io/lean-pool/LeanPool/CircuitComplexity/Nondeterminism.html#CircuitComplexity.existQuantify_complexity_le) (theorem), declared in [LeanPool/CircuitComplexity/Nondeterminism.lean, line 160](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity/Nondeterminism.lean#L160): “If a function f has circuit complexity s, then the existential quantification of f over a k-bit block has circuit complexity at most 2^k \* (s + 1).”

## Project

- Authors: Samuel Schlesinger.
- Project repository: [SamuelSchlesinger/circuit-complexity](https://github.com/SamuelSchlesinger/circuit-complexity).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 68Q06, 94C11.
- In Lean Pool: [LeanPool/CircuitComplexity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity), from the card [LeanPool/projects/circuit-complexity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/circuit-complexity.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/circuit-complexity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/circuit-complexity.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CircuitComplexity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CircuitComplexity)
