---
declaration: theorem
origin: cited
lean: LeanPool.BalancedEdgeColourings.BklsPalomar.theorem1, LeanPool.BalancedEdgeColourings.BklsPalomar.theorem6, LeanPool.BalancedEdgeColourings.BklsPalomar.theorem10, LeanPool.BalancedEdgeColourings.BklsPalomar.corollary12
statement: formalized
proof: formalized
---

# Balanced and vertex-distinguishing edge colourings

> Formalizes Balister–Kostochka–Li–Schelp (2004), Theorems 1, 6, 10(2) and Corollary 12. Least-cost edge colourings balance palette multiplicities within two. Degree-count bounds then yield vertex-distinguishing colourings and the Burris–Schelp bound for graphs of large maximum degree and minimum degree at least five. Theorem 10(2) explicitly assumes k ≥ 3. Includes simultaneous Kempe exchanges, palette-counting and linear-programming dual bounds; does not formalize Theorem 10(1), Corollary 11 or the whole Burris–Schelp conjecture.

*Quoted from the card [LeanPool/projects/balanced-edge-colourings.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/balanced-edge-colourings.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.BalancedEdgeColourings.BklsPalomar.theorem1`](https://leanpool.github.io/lean-pool/LeanPool/BalancedEdgeColourings.html#LeanPool.BalancedEdgeColourings.BklsPalomar.theorem1) (theorem; a main declaration), declared in [LeanPool/BalancedEdgeColourings.lean, line 110](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BalancedEdgeColourings.lean#L110): “Every least-cost proper k-edge-colouring is balanced: for palettes P and Q of equal cardinality, the number of vertices seeing P is at most the number seeing Q plus two.” Its source, as the card gives it: “BKLS (2004), Theorem 1”
- [`LeanPool.BalancedEdgeColourings.BklsPalomar.theorem6`](https://leanpool.github.io/lean-pool/LeanPool/BalancedEdgeColourings.html#LeanPool.BalancedEdgeColourings.BklsPalomar.theorem6) (theorem; a main declaration), declared in [LeanPool/BalancedEdgeColourings.lean, line 125](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BalancedEdgeColourings.lean#L125): “A proper three-edge-colouring can be replaced by a four-edge-colouring that separates vertices with equal keys, under the paper's restrictions on repeated degree-three palettes and key classes.” Its source, as the card gives it: “BKLS (2004), Theorem 6”
- [`LeanPool.BalancedEdgeColourings.BklsPalomar.theorem10`](https://leanpool.github.io/lean-pool/LeanPool/BalancedEdgeColourings.html#LeanPool.BalancedEdgeColourings.BklsPalomar.theorem10) (theorem; a main declaration), declared in [LeanPool/BalancedEdgeColourings.lean, line 140](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BalancedEdgeColourings.lean#L140): “For k at least three and at least the maximum degree, the degree-count bounds in BKLS Theorem 10(2) guarantee a vertex-distinguishing proper edge-colouring with k+1 colours.” Its source, as the card gives it: “BKLS (2004), Theorem 10(2), with k ≥ 3”
- [`LeanPool.BalancedEdgeColourings.BklsPalomar.corollary12`](https://leanpool.github.io/lean-pool/LeanPool/BalancedEdgeColourings.html#LeanPool.BalancedEdgeColourings.BklsPalomar.corollary12) (theorem; a main declaration), declared in [LeanPool/BalancedEdgeColourings.lean, line 156](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BalancedEdgeColourings.lean#L156): “For a finite simple graph with minimum degree at least five and maximum degree at least sqrt(2|V|)+4, let k be the least integer with n_d at most binomial(k,d) for every d. A vertex-distinguishing proper edge-colouring exists with k+1 colours, and every such colouring uses at least k colours.” Its source, as the card gives it: “BKLS (2004), Corollary 12”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *Balanced edge colorings* by P. N. Balister, A. V. Kostochka, Hao Li, R. H. Schelp, [doi:10.1016/S0095-8956(03)00073-X](https://doi.org/10.1016/S0095-8956%2803%2900073-X).
- Project repository: [jtraverso/balanced-edge-colourings](https://github.com/jtraverso/balanced-edge-colourings), at commit [736c78e6](https://github.com/jtraverso/balanced-edge-colourings/tree/736c78e6addcdb77e95cd83e4e44c5c0700f13ef).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15.
- In Lean Pool: [LeanPool/BalancedEdgeColourings](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BalancedEdgeColourings), from the card [LeanPool/projects/balanced-edge-colourings.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/balanced-edge-colourings.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/balanced-edge-colourings.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/balanced-edge-colourings.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BalancedEdgeColourings](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BalancedEdgeColourings)
