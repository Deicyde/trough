---
declaration: theorem
origin: cited
lean: QuantumInfo.knill_laflamme, QuantumInfo.knill_laflamme_sum, QuantumInfo.exists_recovery_channel_of_knillLaflamme
statement: formalized
proof: formalized
---

# Knill–Laflamme quantum error-correction conditions

> Characterizes correctability of arbitrary finite families of complex error matrices on a nonzero orthogonal code projector by the Knill–Laflamme matrix condition. Constructs a finite Kraus recovery channel, proves both the individual-error and combined-noise equivalences up to scalar factors, and proves exact recovery when the errors themselves form a trace-preserving channel.

*Quoted from the card [LeanPool/projects/knill-laflamme.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/knill-laflamme.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`QuantumInfo.knill_laflamme`](https://leanpool.github.io/lean-pool/LeanPool/KnillLaflamme/Basic.html#QuantumInfo.knill_laflamme) (theorem; a main declaration), declared in [LeanPool/KnillLaflamme/Basic.lean, line 88](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KnillLaflamme/Basic.lean#L88): “For a nonzero orthogonal code projector and arbitrary finite error family, the Knill–Laflamme condition is equivalent to the existence of a finite Kraus channel correcting each error up to a scalar on all supported matrices.”
- [`QuantumInfo.knill_laflamme_sum`](https://leanpool.github.io/lean-pool/LeanPool/KnillLaflamme/Basic.html#QuantumInfo.knill_laflamme_sum) (theorem; a main declaration), declared in [LeanPool/KnillLaflamme/Basic.lean, line 109](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KnillLaflamme/Basic.lean#L109): “The same condition is equivalent to a finite Kraus channel correcting the sum of all error actions up to a scalar on all code-supported matrices; the errors need not preserve trace.”
- [`QuantumInfo.exists_recovery_channel_of_knillLaflamme`](https://leanpool.github.io/lean-pool/LeanPool/KnillLaflamme/QuantumInfo/KnillLaflamme.html#QuantumInfo.exists_recovery_channel_of_knillLaflamme) (theorem; a main declaration), declared in [LeanPool/KnillLaflamme/QuantumInfo/KnillLaflamme.lean, line 516](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KnillLaflamme/QuantumInfo/KnillLaflamme.lean#L516): “A trace-preserving noise channel satisfying the Knill–Laflamme condition admits a recovery channel acting as the identity on every code-supported matrix.”

## Project

- Authors: Zayn Blore.
- Source: *Theory of quantum error-correcting codes*, [doi:10.1103/PhysRevA.55.900](https://doi.org/10.1103/PhysRevA.55.900).
- Project repository: [zblore/knill-laflamme-lean](https://github.com/zblore/knill-laflamme-lean), at commit [f680e2d5](https://github.com/zblore/knill-laflamme-lean/tree/f680e2d5f616bb423fb814f1471b07387729fffd).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 81P73, 81P47.
- In Lean Pool: [LeanPool/KnillLaflamme](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KnillLaflamme), from the card [LeanPool/projects/knill-laflamme.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/knill-laflamme.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/knill-laflamme.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/knill-laflamme.yaml)
- [Lean Pool at 307e3125: LeanPool/KnillLaflamme](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/KnillLaflamme)
