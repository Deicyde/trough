---
declaration: theorem
origin: cited
lean: Nikodym.card_ge_pow_sub, Nikodym.exists_isNikodym_card_le
statement: formalized
proof: formalized
---

# The sharp finite-field Nikodym exponent

> Proves a lower bound for Nikodym sets over arbitrary finite fields and a matching exponent upper construction over sufficiently large prime fields, using interpolation, algebraic degree bounds, and multiquadratic constructions.

*Quoted from the card [LeanPool/projects/nikodym.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nikodym.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Nikodym.card_ge_pow_sub`](https://leanpool.github.io/lean-pool/LeanPool/Nikodym/Nikodym/Main.html#Nikodym.card_ge_pow_sub) (theorem; a main declaration), declared in [LeanPool/Nikodym/Nikodym/Main.lean, line 55](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Nikodym/Nikodym/Main.lean#L55): “Every Nikodym set in dimension d ≥ 2 over a finite field of size q has size at least q^d − (8d²+1)q^(d−2^(1−d)).”
- [`Nikodym.exists_isNikodym_card_le`](https://leanpool.github.io/lean-pool/LeanPool/Nikodym/Nikodym/Main.html#Nikodym.exists_isNikodym_card_le) (theorem; a main declaration), declared in [LeanPool/Nikodym/Nikodym/Main.lean, line 64](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Nikodym/Nikodym/Main.lean#L64): “For every positive ε and dimension d ≥ 2, sufficiently large prime fields admit a Nikodym set of size at most q^d − q^(d−2^(1−d)−ε).”

## Project

- Authors: Ting-Wei Chao, Zach Hunter, Cosmin Pohoata, Hung-Hsun Hans Yu, Shengtong Zhang.
- Project repository: [shengtongzhang-alt/nikodym](https://github.com/shengtongzhang-alt/nikodym), at commit [38d16dcd](https://github.com/shengtongzhang-alt/nikodym/tree/38d16dcdbaef04f6f85e5dee92905b7db2eba930).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05B25, 11T99.
- In Lean Pool: [LeanPool/Nikodym](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Nikodym), from the card [LeanPool/projects/nikodym.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nikodym.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/nikodym.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nikodym.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Nikodym](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Nikodym)
