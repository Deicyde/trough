---
declaration: theorem
origin: cited
lean: FanelliMoscardelli.stability_threshold_tight
statement: formalized
---

# Fanelli–Moscardelli conjecture on approximate roommates stability

> *Reference:* A. Fanelli and L. Moscardelli,
> [Approximately Stable Matching](https://doi.org/10.3233/FAIA251234), Section 5.
>
> For complete strict preferences on $N$ agents, let $K(N)$ be the least positive rank-improvement
> threshold that guarantees a stable matching for every profile. A pair blocks at threshold $k$
> when both agents gain at least $k$ positions. Singles have rank $N$.

*Quoted from [FormalConjectures/Paper/ApproximatelyStableMatching.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Paper/ApproximatelyStableMatching.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `FanelliMoscardelli.stability_threshold_tight`

Open: stated without proof.

> The universal rank-improvement threshold is $K(N)=\lceil N/2\rceil$ for every sufficiently
> large number of agents.

```lean
theorem stability_threshold_tight :
    ∃ N₀ : ℕ, 3 ≤ N₀ ∧
      ∀ N ≥ N₀, Roommates.stabilityThreshold N = (N + 1) / 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [68 Computer science](../../by-subject/part-02/68-computer-science/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Paper/ApproximatelyStableMatching.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Paper/ApproximatelyStableMatching.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/ApproximatelyStableMatching.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Paper/ApproximatelyStableMatching.lean)
- [Approximately Stable Matching](https://doi.org/10.3233/FAIA251234)
