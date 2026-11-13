---
declaration: theorem
origin: cited
lean: CriticalPortraits.card_portraits, CriticalPortraits.Cycle.cycle_lemma
statement: formalized
proof: formalized
---

# Counting Critical Portraits

> Formalizes the census of degree-d critical portraits, modeled as level-canonical (d-1)-subsets of the cyclic group ZMod (d\*m), and proves that their number equals C(d\*m, d-1)/d for all d, via the Dvoretzky-Motzkin cycle lemma together with an explicit level-canonicalization bijection (injectivity and surjectivity of the delete-minimum map).

*Quoted from the card [LeanPool/projects/critical-portraits.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/critical-portraits.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CriticalPortraits.card_portraits`](https://leanpool.github.io/lean-pool/LeanPool/CriticalPortraits/Census.html#CriticalPortraits.card_portraits) (theorem; a main declaration), declared in [LeanPool/CriticalPortraits/Census.lean, line 61](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CriticalPortraits/Census.lean#L61): “The number of degree-d critical portraits at level m equals C(d\*m, d-1)/d.”
- [`CriticalPortraits.Cycle.cycle_lemma`](https://leanpool.github.io/lean-pool/LeanPool/CriticalPortraits/CycleLemma.html#CriticalPortraits.Cycle.cycle_lemma) (theorem; a main declaration), declared in [LeanPool/CriticalPortraits/CycleLemma.lean, line 69](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CriticalPortraits/CycleLemma.lean#L69): “The Dvoretzky-Motzkin cycle lemma: a period-n integer sequence with period-sum 1 has exactly one good cyclic shift.”
- [`CriticalPortraits.T_injOn`](https://leanpool.github.io/lean-pool/LeanPool/CriticalPortraits/Injectivity.html#CriticalPortraits.T_injOn) (theorem), declared in [LeanPool/CriticalPortraits/Injectivity.lean, line 1087](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CriticalPortraits/Injectivity.lean#L1087): “The delete-minimum map is injective on critical portraits.”
- [`CriticalPortraits.T_surjOn`](https://leanpool.github.io/lean-pool/LeanPool/CriticalPortraits/Surjectivity.html#CriticalPortraits.T_surjOn) (theorem), declared in [LeanPool/CriticalPortraits/Surjectivity.lean, line 1544](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CriticalPortraits/Surjectivity.lean#L1544): “The delete-minimum map surjects onto the level-canonical subsets.”

## Project

- Authors: Keston Aquino-Michaels.
- Source: *Counting critical portraits via the cycle lemma* by Keston Aquino-Michaels, [doi:10.5281/zenodo.20737896](https://doi.org/10.5281/zenodo.20737896).
- Project repository: [no-way-labs/lean-critical-portraits](https://github.com/no-way-labs/lean-critical-portraits).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05A15, 37F20.
- In Lean Pool: [LeanPool/CriticalPortraits](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CriticalPortraits), from the card [LeanPool/projects/critical-portraits.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/critical-portraits.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/critical-portraits.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/critical-portraits.yaml)
- [Lean Pool at 701389c0: LeanPool/CriticalPortraits](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CriticalPortraits)
