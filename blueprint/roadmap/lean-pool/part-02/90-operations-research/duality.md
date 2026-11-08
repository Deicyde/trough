---
declaration: theorem
origin: cited
lean: extendedFarkas, StandardLP.strongDuality
statement: formalized
proof: formalized
---

# Duality theory in linear optimization and its extensions

> Formalizes Farkas-like theorems and strong LP duality, including extensions to a linearly ordered field with bot and top.

*Quoted from the card [LeanPool/projects/duality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/duality.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`equalityFarkas`](https://leanpool.github.io/lean-pool/LeanPool/Duality/FarkasBasic.html#equalityFarkas) (theorem), declared in [LeanPool/Duality/FarkasBasic.lean, line 43](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Duality/FarkasBasic.lean#L43): “Farkas' lemma for linear equalities over nonnegative variables.”
- [`inequalityFarkas`](https://leanpool.github.io/lean-pool/LeanPool/Duality/FarkasBasic.html#inequalityFarkas) (theorem), declared in [LeanPool/Duality/FarkasBasic.lean, line 128](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Duality/FarkasBasic.lean#L128): “Farkas' lemma for linear inequalities over nonnegative variables.”
- [`extendedFarkas`](https://leanpool.github.io/lean-pool/LeanPool/Duality/FarkasSpecial.html#extendedFarkas) (theorem; a main declaration), declared in [LeanPool/Duality/FarkasSpecial.lean, line 572](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Duality/FarkasSpecial.lean#L572): “Extended Farkas theorem for matrices and vectors over a linearly ordered field with bot and top.”
- [`ValidELP.strongDuality`](https://leanpool.github.io/lean-pool/LeanPool/Duality/LinearProgramming.html#ValidELP.strongDuality) (theorem), declared in [LeanPool/Duality/LinearProgramming.lean, line 1151](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Duality/LinearProgramming.lean#L1151): “Strong duality theorem for extended linear programs.”
- [`StandardLP.strongDuality`](https://leanpool.github.io/lean-pool/LeanPool/Duality/LinearProgrammingB.html#StandardLP.strongDuality) (theorem; a main declaration), declared in [LeanPool/Duality/LinearProgrammingB.lean, line 242](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Duality/LinearProgrammingB.lean#L242): “Strong duality theorem for linear programs in standard form.”

## Project

- Authors: Martin Dvorak.
- Source: [doi:10.46298/afm.14253](https://doi.org/10.46298/afm.14253), [arXiv:2409.08119](https://arxiv.org/abs/2409.08119).
- Project repository: [madvorak/duality](https://github.com/madvorak/duality).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 90C05, 90C46.
- In Lean Pool: [LeanPool/Duality](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Duality), from the card [LeanPool/projects/duality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/duality.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/duality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/duality.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Duality](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Duality)
