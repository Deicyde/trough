---
declaration: theorem
origin: cited
lean: SimpleGraph.IsChordal.exists_two_nonadj_isSimplicial
statement: formalized
proof: formalized
---

# Chordal graphs: minimal separators and simplicial vertices

> A reusable formalization byproduct accompanying Paper II: defines chordal graphs through the cycle-and-chord characterization, proves induced-subgraph heredity and the clique property for finite minimal separators of fixed vertex pairs, proves Dirac's simplicial-vertex theorem, and proves the connected non-complete case of the two-vertex conclusion.

*Quoted from the card [LeanPool/projects/erdos81-paper-ii-chordal-heredity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos81-paper-ii-chordal-heredity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`SimpleGraph.IsChordal.comap`](https://leanpool.github.io/lean-pool/LeanPool/Erdos81PaperIIContrib/Chordal.html#SimpleGraph.IsChordal.comap) (theorem), declared in [LeanPool/Erdos81PaperIIContrib/Chordal.lean, line 62](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIContrib/Chordal.lean#L62): “A graph that embeds as an induced subgraph of a chordal graph is itself chordal.”
- [`SimpleGraph.IsChordal.induce`](https://leanpool.github.io/lean-pool/LeanPool/Erdos81PaperIIContrib/Chordal.html#SimpleGraph.IsChordal.induce) (theorem), declared in [LeanPool/Erdos81PaperIIContrib/Chordal.lean, line 76](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIContrib/Chordal.lean#L76): “Every induced subgraph of a chordal graph is chordal.”
- [`SimpleGraph.IsChordal.minimalSeparator_isClique`](https://leanpool.github.io/lean-pool/LeanPool/Erdos81PaperIIContrib/Chordal.html#SimpleGraph.IsChordal.minimalSeparator_isClique) (theorem), declared in [LeanPool/Erdos81PaperIIContrib/Chordal.lean, line 904](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIContrib/Chordal.lean#L904): “Every finite minimal separator of two fixed vertices in a chordal graph is a clique.”
- [`SimpleGraph.IsChordal.exists_isSimplicial`](https://leanpool.github.io/lean-pool/LeanPool/Erdos81PaperIIContrib/Chordal.html#SimpleGraph.IsChordal.exists_isSimplicial) (theorem), declared in [LeanPool/Erdos81PaperIIContrib/Chordal.lean, line 910](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIContrib/Chordal.lean#L910): “Every nonempty finite chordal graph has a simplicial vertex.”
- [`SimpleGraph.IsChordal.exists_two_nonadj_isSimplicial`](https://leanpool.github.io/lean-pool/LeanPool/Erdos81PaperIIContrib/Chordal.html#SimpleGraph.IsChordal.exists_two_nonadj_isSimplicial) (theorem; a main declaration), declared in [LeanPool/Erdos81PaperIIContrib/Chordal.lean, line 926](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIContrib/Chordal.lean#L926): “Every connected non-complete finite chordal graph has two non-adjacent simplicial vertices.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *Complete-Split Extremizers for a Fractional Triangle-Cover Functional on Chordal Graphs* by Juan Pablo Traverso Gianini, [https://github.com/jtraverso/lean-pool/blob/822738f3089d92c5e65a6bfb8c88c992e4699167/LeanPool/Erdos81PaperIIContrib/Chordal.lean](https://github.com/jtraverso/lean-pool/blob/822738f3089d92c5e65a6bfb8c88c992e4699167/LeanPool/Erdos81PaperIIContrib/Chordal.lean).
- Project repository: [jtraverso/lean-pool](https://github.com/jtraverso/lean-pool).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C75.
- In Lean Pool: [LeanPool/Erdos81PaperIIContrib](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIContrib), from the card [LeanPool/projects/erdos81-paper-ii-chordal-heredity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos81-paper-ii-chordal-heredity.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos81-paper-ii-chordal-heredity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos81-paper-ii-chordal-heredity.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Erdos81PaperIIContrib](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIContrib)
