---
declaration: theorem
origin: cited
lean: SaxlCounterexamples.MainTheorems.mainTheorem
statement: formalized
proof: formalized
---

# Common-neighbour counterexamples for Saxl graphs

> Proves that for every base size B at least two and every prescribed degree bound, there is a finite faithful primitive permutation group of at least that degree and exact base size B whose generalized Saxl graph contains two nonadjacent vertices with no common neighbor. The supporting library constructs an explicit infinite family from binary deleted permutation modules over finite fields and proves the required base-size, irreducibility, primitivity, and graph-theoretic properties.

*Quoted from the card [LeanPool/projects/common-neighbour-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/common-neighbour-conjecture.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SaxlCounterexamples.MainTheorems.mainTheorem`](https://leanpool.github.io/lean-pool/LeanPool/CommonNeighbourConjecture/Examples/MainTheorems.html#SaxlCounterexamples.MainTheorems.mainTheorem) (theorem; a main declaration), declared in [LeanPool/CommonNeighbourConjecture/Examples/MainTheorems.lean, line 28](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CommonNeighbourConjecture/Examples/MainTheorems.lean#L28): “For every natural number B at least two and every degree bound, there exists a finite faithful primitive permutation group of degree at least the bound and base size exactly B whose generalized Saxl graph has two nonadjacent vertices with no common neighbor.”
- [`SaxlCounterexamples.EveryBase.hq_coreFamily`](https://leanpool.github.io/lean-pool/LeanPool/CommonNeighbourConjecture/Examples/EveryBase/Main.html#SaxlCounterexamples.EveryBase.hq_coreFamily) (theorem), declared in [LeanPool/CommonNeighbourConjecture/Examples/EveryBase/Main.lean, line 175](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CommonNeighbourConjecture/Examples/EveryBase/Main.lean#L175): “For every odd d with 3 ≤ d and every tail, the explicit affine wreath-product family has exact base size tail + 2, acts primitively, and its displayed pair has no common neighbor in the corresponding generalized Saxl graph.”

## Project

- Authors: Aluna Rizzoli, Adam R. Thomas.
- Source: *Common neighbour conjectures for Saxl graphs fail at every base size* by Aluna Rizzoli, Adam R. Thomas, [doi:10.5281/zenodo.22231393](https://doi.org/10.5281/zenodo.22231393).
- Project repository: [alunik/common-neighbour-conjecture](https://github.com/alunik/common-neighbour-conjecture), at commit [b2c0a8f9](https://github.com/alunik/common-neighbour-conjecture/tree/b2c0a8f95aa4dca76a034a0e769a8c8249f38ae2).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 20B15, 05C25.
- In Lean Pool: [LeanPool/CommonNeighbourConjecture](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CommonNeighbourConjecture), from the card [LeanPool/projects/common-neighbour-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/common-neighbour-conjecture.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/common-neighbour-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/common-neighbour-conjecture.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CommonNeighbourConjecture](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CommonNeighbourConjecture)
