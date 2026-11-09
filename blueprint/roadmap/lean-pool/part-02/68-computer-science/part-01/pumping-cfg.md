---
declaration: theorem
origin: cited
lean: Language.IsContextFree.pumping, ChomskyNormalFormGrammar.pumping
statement: formalized
proof: formalized
---

# Pumping Lemma for Context-Free Grammars

> Formalizes the pumping lemma for context-free languages via parse trees of Chomsky-normal-form grammars and a pigeonhole argument.

*Quoted from the card [LeanPool/projects/pumping-cfg.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pumping-cfg.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Language.IsContextFree.pumping`](https://leanpool.github.io/lean-pool/LeanPool/PumpingCfg/Pumping.html#Language.IsContextFree.pumping) (theorem; a main declaration), declared in [LeanPool/PumpingCfg/Pumping.lean, line 343](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PumpingCfg/Pumping.lean#L343): “Every context-free language admits a pumping length p such that any word of length at least p decomposes as u v x y z with vy nonempty, vxy of length at most p, and u vⁱ x yⁱ z in the language for every i.”
- [`ChomskyNormalFormGrammar.pumping`](https://leanpool.github.io/lean-pool/LeanPool/PumpingCfg/Pumping.html#ChomskyNormalFormGrammar.pumping) (lemma; a main declaration), declared in [LeanPool/PumpingCfg/Pumping.lean, line 314](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PumpingCfg/Pumping.lean#L314): “The pumping lemma at the level of a Chomsky-normal-form grammar, obtained from a sufficiently tall parse tree with a repeated nonterminal.”

## Project

- Authors: Alexander Loitzl, Martin Dvorak.
- Project repository: [AlexLoitzl/pumping_cfg](https://github.com/AlexLoitzl/pumping_cfg).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 68Q45.
- In Lean Pool: [LeanPool/PumpingCfg](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PumpingCfg), from the card [LeanPool/projects/pumping-cfg.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pumping-cfg.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/pumping-cfg.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pumping-cfg.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PumpingCfg](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PumpingCfg)
