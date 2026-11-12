---
declaration: section
origin: cited
lean: OAI.SidorenkoCounterexample.main
statement: formalized
proof: formalized
---

# 161. Counterexamples to Sidorenko’s conjecture and the forcing conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves Sidorenko's conjecture with a connected bipartite pattern on 35 vertices and 66 edges that occurs less frequently than in a random graph of the same edge density. The same pattern disproves the forcing conjecture of Skokan and Thoma: matching its density and the edge density of a constant graphon need not force quasirandomness.

## A counterexample to Sidorenko's conjecture

We disprove Sidorenko's conjecture with a bipartite graph on 35 vertices and 66 edges: its homomorphism density in some finite simple graph is smaller than the conjectured lower bound. The same connected graph also disproves the forcing conjecture: at one fixed density, asymptotically matching the edge and pattern densities does not imply quasirandomness.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Sidorenko's conjecture predicts that every bipartite graph $H$ has homomorphism density at least the host graph's edge density raised to $|E(H)|$. The formalization disproves this for the paper's fixed bipartite graph with $35$ vertices and $66$ edges: it constructs a nonempty finite simple host graph with $t(H,G)<t(K_2,G)^{66}$. The separate forcing-conjecture consequence in the paper is outside this statement.

## Lean: Counterexample to Sidorenko's conjecture

Stated in [SidorenkoCounterexample.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SidorenkoCounterexample.lean).

```lean
theorem main : ∃ size : ℕ, 0 < size ∧ ∃ host : SimpleGraph (Fin size),
    (∃ left right, host.Adj left right) ∧ homDensity H host < (edgeDensity host) ^ 66
```

Proved in [lean/OAI/Combinatorics/Sidorenko/RandomHost.lean, line 319](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Sidorenko/RandomHost.lean#L319).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/161.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/161.md)
