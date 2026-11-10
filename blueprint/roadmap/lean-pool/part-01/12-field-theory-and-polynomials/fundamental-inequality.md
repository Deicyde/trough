---
declaration: def
origin: cited
lean: Valuation.ramificationIndex, Valuation.fundamentalInequality
statement: formalized
---

# The Fundamental Inequality of Valued Fields

> Defines the ramification index and residue degree of an extension of valued fields and proves the fundamental inequality e \* f ≤ finrank K L for finite extensions, via the valuation independence of products of coset representatives and residue-field basis lifts.

*Quoted from the card [LeanPool/projects/fundamental-inequality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fundamental-inequality.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Valuation.ramificationIndex`](https://leanpool.github.io/lean-pool/LeanPool/FundamentalInequality.html#Valuation.ramificationIndex) (def; a main declaration), declared in [LeanPool/FundamentalInequality.lean, line 74](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FundamentalInequality.lean#L74): “Defines the ramification index e(w/v) as the relative index of the value group of the restricted valuation inside the value group of the extension.”
- [`Valuation.residueDegree`](https://leanpool.github.io/lean-pool/LeanPool/FundamentalInequality.html#Valuation.residueDegree) (def), declared in [LeanPool/FundamentalInequality.lean, line 59](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FundamentalInequality.lean#L59): “Defines the residue degree f(w/v) as the rank of the residue field extension.”
- [`Valuation.valuation_independence`](https://leanpool.github.io/lean-pool/LeanPool/FundamentalInequality.html#Valuation.valuation_independence) (lemma), declared in [LeanPool/FundamentalInequality.lean, line 206](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FundamentalInequality.lean#L206): “Elements with valuations in distinct cosets and residues that are linearly independent give products that are linearly independent over the base field.”
- [`Valuation.fundamentalInequality`](https://leanpool.github.io/lean-pool/LeanPool/FundamentalInequality.html#Valuation.fundamentalInequality) (theorem; a main declaration), declared in [LeanPool/FundamentalInequality.lean, line 476](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FundamentalInequality.lean#L476): “The fundamental inequality e(w/v) \* f(w/v) ≤ finrank K L for finite extensions of valued fields.” Its source, as the card gives it: “F.-V. Kuhlmann, Valued Fields, Chapter 4, §4.4.”

## Project

- Authors: Alessandro Linzi.
- Source: *Valued Fields* by Franz-Viktor Kuhlmann.
- Project repository: [linzialessandro/FundamentalInequality](https://github.com/linzialessandro/FundamentalInequality).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 12J20.
- In Lean Pool: [LeanPool/FundamentalInequality](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FundamentalInequality), from the card [LeanPool/projects/fundamental-inequality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fundamental-inequality.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/fundamental-inequality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fundamental-inequality.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FundamentalInequality](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FundamentalInequality)
