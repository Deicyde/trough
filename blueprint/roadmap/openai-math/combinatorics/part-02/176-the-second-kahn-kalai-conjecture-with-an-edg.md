---
declaration: section
origin: cited
lean: OAI.LeanBlast.SecondKahnKalai.secondKahnKalaiBounds
statement: formalized
proof: formalized
---

# 176. The second Kahn–Kalai conjecture with an edge-count bound

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the second Kahn–Kalai conjecture: for every finite simple graph *H* with *h* ≥ 1 edges and at most *n* vertices, its appearance threshold in $G(n,p)$ is at most $C p_{\mathrm E}(n,H)(1+\log_2 h)$, with universal *C*. Here $p_{\mathrm E}$ is the least density at which every subgraph of *H* has expected copy count at least 1/2.

## The second Kahn–Kalai conjecture

We prove the second Kahn–Kalai conjecture. For every finite simple graph *H* with *h* ≥ 1 edges and at most *n* vertices, the threshold for $G(n,p)$ to contain an ordinary copy of *H* is at most $C p_{\mathrm E}(n,H)(1+\log_2 h)$, where *C* is universal. Here $p_{\mathrm E}(n,H)$ is the least density at which every subgraph of *H* has expected copy count at least one half.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The second Kahn–Kalai conjecture compares the threshold for a random graph to contain a fixed graph with its expectation threshold. The formalized result proves the comparison up to a universal factor times $1+\log_2|E(H)|$, and hence up to a universal factor times $\log_2 n$, for every graph $H$ with at least one edge and at most $n$ vertices, $n\ge2$. The bounds use the actual containment and expectation thresholds.

## Lean: Second Kahn–Kalai threshold bounds

```lean
theorem secondKahnKalaiBounds (n : ℕ) (V : Type u) [Fintype V]
    (H : SimpleGraph V) (hn : 2 ≤ n) (hcard : Fintype.card V ≤ n)
    (hedge : 1 ≤ edgeCount H) : SecondKahnKalaiBounds n H
```

Stated in [SecondKahnKalai.lean, line 65](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SecondKahnKalai.lean#L65). Proved in [lean/OAI/Combinatorics/GraphThreshold/Main.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/GraphThreshold/Main.lean#L25). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/176.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/176.md)
