---
declaration: theorem
origin: cited
lean: PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound
statement: formalized
proof: formalized
---

# Quartic-over-logarithmic lower bound for rational permanent formulas

> Proves that every valid rational arithmetic formula over the complex numbers computing the n-by-n permanent, for n at least 32, has at least n^4 / (192 log_2 n) variable leaves. The development derives the bound through coefficient-field transcendence degree, Jacobian minors, matching-polynomial identities, and a cyclic block decomposition.

*Quoted from the card [LeanPool/projects/permanent-formula-lower-bound.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/permanent-formula-lower-bound.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/PermanentFormulaLowerBound.html#PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound) (theorem; a main declaration), declared in [LeanPool/PermanentFormulaLowerBound.lean, line 6243](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PermanentFormulaLowerBound.lean#L6243): “For n at least 32, every valid rational formula over the complex numbers that computes the n-by-n permanent has at least n^4 / (192 log_2 n) variable leaves.”
- [`PermanentFormulaLowerBound.permanent_rational_formula_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/PermanentFormulaLowerBound.html#PermanentFormulaLowerBound.permanent_rational_formula_lower_bound) (theorem), declared in [LeanPool/PermanentFormulaLowerBound.lean, line 6222](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PermanentFormulaLowerBound.lean#L6222): “The same quartic-over-logarithmic lower bound controls variable leaves, total leaves, and vertices, and half that bound controls internal gates.”

## Project

- Authors: OpenAI, Dean Cureton.
- Source: *Ten Advances in Mathematics and Theoretical Computer Science* by OpenAI.
- Project repository: [openai/ten-proofs](https://github.com/openai/ten-proofs), at commit [94bc0feb](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 68Q17, 68Q25, 15A15.
- In Lean Pool: [LeanPool/PermanentFormulaLowerBound](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PermanentFormulaLowerBound), from the card [LeanPool/projects/permanent-formula-lower-bound.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/permanent-formula-lower-bound.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/permanent-formula-lower-bound.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/permanent-formula-lower-bound.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PermanentFormulaLowerBound](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PermanentFormulaLowerBound)
