---
declaration: theorem
origin: cited
lean: BrooksSubcubic.brooks_cubic
statement: formalized
proof: formalized
---

# Brooks' theorem for subcubic graphs

> Proves that every finite simple graph of maximum degree at most three with no four-clique admits a three-colouring, without a connectedness assumption. Includes controlled greedy colouring, colouring across cut vertices, and a good-triple argument for cubic components. This is the subcubic case of Brooks' theorem, not the general-degree theorem.

*Quoted from the card [LeanPool/projects/brooks-subcubic.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brooks-subcubic.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`BrooksSubcubic.brooks_cubic`](https://leanpool.github.io/lean-pool/LeanPool/BrooksSubcubic/Main.html#BrooksSubcubic.brooks_cubic) (theorem; a main declaration), declared in [LeanPool/BrooksSubcubic/Main.lean, line 28](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrooksSubcubic/Main.lean#L28): “Every finite simple graph with maximum degree at most three and no clique on four vertices is three-colourable. The graph may be disconnected.” Its source, as the card gives it: “The subcubic specialization of Brooks' 1941 colouring theorem; the linked Apache-2.0 Lean source proves exactly this specialization.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *On colouring the nodes of a network* by R. L. Brooks, [doi:10.1017/S030500410002168X](https://doi.org/10.1017/S030500410002168X), [https://github.com/jtraverso/lean-pool/blob/aced439fd4161d118bf167a1e8d10553f28913fe/LeanPool/BrooksSubcubic/Main.lean](https://github.com/jtraverso/lean-pool/blob/aced439fd4161d118bf167a1e8d10553f28913fe/LeanPool/BrooksSubcubic/Main.lean).
- Project repository: [jtraverso/lean-pool](https://github.com/jtraverso/lean-pool), at commit [aced439f](https://github.com/jtraverso/lean-pool/tree/aced439fd4161d118bf167a1e8d10553f28913fe).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15.
- In Lean Pool: [LeanPool/BrooksSubcubic](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrooksSubcubic), from the card [LeanPool/projects/brooks-subcubic.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brooks-subcubic.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/brooks-subcubic.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brooks-subcubic.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BrooksSubcubic](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrooksSubcubic)
