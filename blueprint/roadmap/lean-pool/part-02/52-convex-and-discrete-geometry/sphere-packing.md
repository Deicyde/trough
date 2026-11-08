---
declaration: theorem
origin: cited
lean: PackingBounds.sharpFullCohnElkiesManuscriptConclusions
statement: formalized
proof: formalized
---

# Sharp asymptotic upper bounds for sphere packing

> Formalizes the sharp high-dimensional asymptotics of the unrestricted Cohn--Elkies linear program and bridges them to sphere-packing density. The development constructs radial test functions through Mellin, saddle-point, and harmonic analysis, proves radialization preserves the unrestricted optimum, and certifies the exact natural- and base-two exponential rates.

*Quoted from the card [LeanPool/projects/sphere-packing.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sphere-packing.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`PackingBounds.FullMain.exact_limit`](https://leanpool.github.io/lean-pool/LeanPool/SpherePacking/Conclusion.html#PackingBounds.FullMain.exact_limit) (theorem), declared in [LeanPool/SpherePacking/Conclusion.lean, line 2030](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpherePacking/Conclusion.lean#L2030): “The d-th root of the unrestricted Cohn--Elkies linear-program bound converges to the sharp constant sqrt(e / (2 pi)).”
- [`PackingBounds.FullMain.exact_binary_exponent`](https://leanpool.github.io/lean-pool/LeanPool/SpherePacking/Conclusion.html#PackingBounds.FullMain.exact_binary_exponent) (theorem), declared in [LeanPool/SpherePacking/Conclusion.lean, line 2040](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpherePacking/Conclusion.lean#L2040): “The base-two logarithm of the unrestricted linear-program bound, divided by dimension, converges to -1/2 log_2(2 pi / e).”
- [`PackingBounds.PackingBridge.sphere_packing_sharp_asymptotic_upper`](https://leanpool.github.io/lean-pool/LeanPool/SpherePacking/Conclusion.html#PackingBounds.PackingBridge.sphere_packing_sharp_asymptotic_upper) (theorem), declared in [LeanPool/SpherePacking/Conclusion.lean, line 363](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpherePacking/Conclusion.lean#L363): “There is a vanishing error sequence such that, in every positive dimension, sphere-packing density is at most (sqrt(e / (2 pi)) plus that error) to the dimension.”
- [`PackingBounds.sharpFullCohnElkiesManuscriptConclusions`](https://leanpool.github.io/lean-pool/LeanPool/SpherePacking/Conclusion.html#PackingBounds.sharpFullCohnElkiesManuscriptConclusions) (theorem; a main declaration), declared in [LeanPool/SpherePacking/Conclusion.lean, line 2192](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpherePacking/Conclusion.lean#L2192): “Packages the complete sharp asymptotic conclusions for the unrestricted program, including quotient-root, natural-logarithmic, and base-two limits, vanishing-error formulas, a universal bound for all admissible functions, and a certified decimal exponent interval.”

## Project

- Authors: OpenAI, Sidharth Hariharan, Gareth Ma, Dean Cureton.
- Source: *Ten Advances in Mathematics and Theoretical Computer Science* by OpenAI, [https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Project repository: [openai/ten-proofs](https://github.com/openai/ten-proofs), at commit [94bc0feb](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 52C17, 41A60, 42A38.
- In Lean Pool: [LeanPool/SpherePacking](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpherePacking), from the card [LeanPool/projects/sphere-packing.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sphere-packing.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/sphere-packing.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sphere-packing.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SpherePacking](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SpherePacking)
