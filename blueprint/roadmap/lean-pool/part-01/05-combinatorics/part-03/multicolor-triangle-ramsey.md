---
declaration: theorem
origin: cited
lean: ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit
statement: formalized
proof: formalized
---

# Superexponential lower bounds for multicolor triangle Ramsey numbers

> Resolves Erdős problem 183 by proving that the k-color triangle Ramsey number has a k-th root tending to infinity. The development constructs saturated palette families and recursive edge colorings, derives an explicit superexponential lower bound, and proves matching order-of-growth bounds for the logarithm of the Ramsey number.

*Quoted from the card [LeanPool/projects/multicolor-triangle-ramsey.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/multicolor-triangle-ramsey.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ErdosProblems.MulticolourTriangleRamsey.erdos_183`](https://leanpool.github.io/lean-pool/LeanPool/MulticolorTriangleRamsey.html#ErdosProblems.MulticolourTriangleRamsey.erdos_183) (theorem), declared in [LeanPool/MulticolorTriangleRamsey.lean, line 3106](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MulticolorTriangleRamsey.lean#L3106): “The k-th root of the k-color triangle Ramsey number tends to infinity, resolving Erdős problem 183.”
- [`ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit`](https://leanpool.github.io/lean-pool/LeanPool/MulticolorTriangleRamsey.html#ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit) (theorem; a main declaration), declared in [LeanPool/MulticolorTriangleRamsey.lean, line 3113](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MulticolorTriangleRamsey.lean#L3113): “For every k at least two, the k-color triangle Ramsey number is at least ((k^(1/3))/(6 exp(38) log k))^k, and its k-th root tends to infinity.”
- [`ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_isTheta`](https://leanpool.github.io/lean-pool/LeanPool/MulticolorTriangleRamsey.html#ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_isTheta) (theorem), declared in [LeanPool/MulticolorTriangleRamsey.lean, line 3037](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MulticolorTriangleRamsey.lean#L3037): “The logarithm of the k-color triangle Ramsey number has order k log k.”

## Project

- Authors: OpenAI.
- Source: *Ten Advances in Mathematics and Theoretical Computer Science* by OpenAI.
- Project repository: [openai/ten-proofs](https://github.com/openai/ten-proofs), at commit [94bc0feb](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05D10, 05C55.
- In Lean Pool: [LeanPool/MulticolorTriangleRamsey](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MulticolorTriangleRamsey), from the card [LeanPool/projects/multicolor-triangle-ramsey.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/multicolor-triangle-ramsey.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/multicolor-triangle-ramsey.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/multicolor-triangle-ramsey.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MulticolorTriangleRamsey](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MulticolorTriangleRamsey)
