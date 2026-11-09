---
declaration: theorem
origin: cited
lean: Highlights.brill_noether_existence_through_five
statement: formalized
proof: formalized
---

# Brill–Noether theory and gonality of finite graphs

> Formalizes Brill–Noether existence through genus five, chains of marked banana graphs and loops, the treewidth lower bound for gonality, and a tricycle example whose gonality drops under regular subdivision. Includes divisor and transmission infrastructure and the Demazure-product support used by vertex gluing.

*Quoted from the card [LeanPool/projects/brill-noether-graphs.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brill-noether-graphs.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Highlights.brill_noether_existence_through_five`](https://leanpool.github.io/lean-pool/LeanPool/BrillNoetherGraphs/Highlights.html#Highlights.brill_noether_existence_through_five) (theorem; a main declaration), declared in [LeanPool/BrillNoetherGraphs/Highlights.lean, line 1242](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrillNoetherGraphs/Highlights.lean#L1242): “Every finite connected loopless multigraph of genus g at most five has, for integers r and d, a divisor of degree d and rank at least r whenever (r + 1) \* (g - d + r) ≤ g.”
- [`Highlights.treewidth_le_gonality`](https://leanpool.github.io/lean-pool/LeanPool/BrillNoetherGraphs/Highlights.html#Highlights.treewidth_le_gonality) (theorem), declared in [LeanPool/BrillNoetherGraphs/Highlights.lean, line 2052](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrillNoetherGraphs/Highlights.lean#L2052): “On a finite connected loopless multigraph, for every natural number k, any degree-k divisor of rank at least one bounds the treewidth by k; this is the witness formulation of the treewidth lower bound for divisorial gonality.”
- [`Highlights.gonality_drops_under_regular_subdivision`](https://leanpool.github.io/lean-pool/LeanPool/BrillNoetherGraphs/Highlights.html#Highlights.gonality_drops_under_regular_subdivision) (theorem), declared in [LeanPool/BrillNoetherGraphs/Highlights.lean, line 2003](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrillNoetherGraphs/Highlights.lean#L2003): “There is a graph whose divisorial gonality strictly decreases under a regular subdivision.”

## Project

- Authors: Nathan Pflueger.
- Project repository: [npflueger/brill-noether-graphs](https://github.com/npflueger/brill-noether-graphs), at commit [ce62dd82](https://github.com/npflueger/brill-noether-graphs/tree/ce62dd82fd499fcec9b5a4110a5312befd6e96e2).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 14T15, 05C50.
- In Lean Pool: [LeanPool/BrillNoetherGraphs](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrillNoetherGraphs), from the card [LeanPool/projects/brill-noether-graphs.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brill-noether-graphs.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/brill-noether-graphs.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brill-noether-graphs.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BrillNoetherGraphs](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrillNoetherGraphs)
