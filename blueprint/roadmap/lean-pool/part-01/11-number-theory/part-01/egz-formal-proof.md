---
declaration: theorem
origin: cited
lean: EGZ.theorem_1_2, EGZ.main_upper_bound
statement: formalized
proof: formalized
---

# Convex geometry and the Erdős–Ginzburg–Ziv problem

> For every fixed positive dimension d, the Erdős–Ginzburg–Ziv constant of (ZMod p)^d equals p times its hollow-family constant plus o(p) as p tends to infinity through primes. Includes the convex-flag Helly and centerpoint theorems, flag decomposition, balanced combinations, relative expansion, and the polynomial hollow-family bound.

*Quoted from the card [LeanPool/projects/egz-formal-proof.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/egz-formal-proof.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`EGZ.theorem_1_2`](https://leanpool.github.io/lean-pool/LeanPool/ErdosGinzburgZiv/EGZ/MainTheorem.html#EGZ.theorem_1_2) (theorem; a main declaration), declared in [LeanPool/ErdosGinzburgZiv/EGZ/MainTheorem.lean, line 36](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosGinzburgZiv/EGZ/MainTheorem.lean#L36): “For each positive dimension d, s((F_p)^d) = p w((F_p)^d) + o(p) as p tends to infinity through primes.”
- [`EGZ.main_upper_bound`](https://leanpool.github.io/lean-pool/LeanPool/ErdosGinzburgZiv/EGZ/MainTheorem.html#EGZ.main_upper_bound) (theorem; a main declaration), declared in [LeanPool/ErdosGinzburgZiv/EGZ/MainTheorem.lean, line 23](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosGinzburgZiv/EGZ/MainTheorem.lean#L23): “For each positive d and ε > 0, sufficiently large primes satisfy s((F_p)^d) ≤ (w((F_p)^d) + ε) p.”

## Project

- Authors: Dmitrii Zakharov.
- Source: [doi:10.19086/da.165216](https://doi.org/10.19086/da.165216), [arXiv:2002.09892](https://arxiv.org/abs/2002.09892).
- Project repository: [zakharov2k/egz-formal-proof](https://github.com/zakharov2k/egz-formal-proof), at commit [7c82267c](https://github.com/zakharov2k/egz-formal-proof/tree/7c82267c43a51dd5cb3e440412780ff82aff7500).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 11B30, 11H06.
- In Lean Pool: [LeanPool/ErdosGinzburgZiv](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosGinzburgZiv), from the card [LeanPool/projects/egz-formal-proof.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/egz-formal-proof.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/egz-formal-proof.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/egz-formal-proof.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ErdosGinzburgZiv](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ErdosGinzburgZiv)
