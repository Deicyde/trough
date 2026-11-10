---
declaration: theorem
origin: cited
lean: not_ramaekersConjecture_ge_six, le_quality_nConjectureTuples
statement: formalized
proof: formalized
---

# Improved Lower Bounds for Strong n-Conjectures

> Formalizes the disproof of Ramaekers's conjecture, constructing tuple families whose abc-style quality stays bounded above 1, and proves Browkin-Brzezinski lower bounds on the quality of the n-conjecture tuples.

*Quoted from the card [LeanPool/projects/redhill.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/redhill.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RamaekersConjecture`](https://leanpool.github.io/lean-pool/LeanPool/Redhill/Common/Conjectures.html#RamaekersConjecture) (def), declared in [LeanPool/Redhill/Common/Conjectures.lean, line 49](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Redhill/Common/Conjectures.lean#L49): “Defines Ramaekers's conjecture for fixed n as the statement that the quality of the relevant tuple set equals 1.”
- [`not_ramaekersConjecture_ge_six`](https://leanpool.github.io/lean-pool/LeanPool/Redhill/General/Main.html#not_ramaekersConjecture_ge_six) (theorem; a main declaration), declared in [LeanPool/Redhill/General/Main.lean, line 131](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Redhill/General/Main.lean#L131): “Proves Ramaekers's conjecture fails for every n at least 6 (the general case, Theorem 1.14).”
- [`not_ramaekersConjecture_odd_ge_five`](https://leanpool.github.io/lean-pool/LeanPool/Redhill/Odd/Main.html#not_ramaekersConjecture_odd_ge_five) (theorem), declared in [LeanPool/Redhill/Odd/Main.lean, line 169](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Redhill/Odd/Main.lean#L169): “Proves Ramaekers's conjecture fails for every odd n at least 5 (the odd case via Pell equations, Theorem 1.13).”
- [`not_ramaekersConjecture_five`](https://leanpool.github.io/lean-pool/LeanPool/Redhill/KonyaginPrelude.html#not_ramaekersConjecture_five) (theorem), declared in [LeanPool/Redhill/KonyaginPrelude.lean, line 341](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Redhill/KonyaginPrelude.lean#L341): “Proves Ramaekers's conjecture fails for n equal to 5 (the Konyagin prelude bound).”
- [`le_quality_nConjectureTuples`](https://leanpool.github.io/lean-pool/LeanPool/Redhill/BB94.html#le_quality_nConjectureTuples) (theorem; a main declaration), declared in [LeanPool/Redhill/BB94.lean, line 291](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Redhill/BB94.lean#L291): “Proves the Browkin-Brzezinski 1994 lower bound 2n-5 on the quality of the n-conjecture tuples (Theorem 1.3).”

## Project

- Authors: Jeremy Tan.
- Source: *Improved Lower Bounds for Strong n-Conjectures* by Rupert Hölzl, Sören Kleine, Frank Stephan, [doi:10.1017/S1446788725000084](https://doi.org/10.1017/S1446788725000084).
- Project repository: [Parcly-Taxel/Redhill](https://github.com/Parcly-Taxel/Redhill).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2026 Jeremy Tan / Parcly Taxel”.
- MSC2020: 11A41, 11D75.
- In Lean Pool: [LeanPool/Redhill](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Redhill), from the card [LeanPool/projects/redhill.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/redhill.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/redhill.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/redhill.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Redhill](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Redhill)
