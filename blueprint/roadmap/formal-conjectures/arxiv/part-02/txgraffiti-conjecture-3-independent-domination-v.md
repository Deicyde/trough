---
declaration: theorem
origin: cited
lean: Arxiv.«2507.17780».tx_graffiti_conjecture_3
statement: formalized
---

# TxGraffiti Conjecture 3: independent domination versus saturation (regular)

> *Reference:* [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
> **In Reverie Together: Ten Years of Mathematical Discovery with a Machine
> Collaborator** by *Randy Davila, Boris Brimkov, Ryan Pepper*
>
> Conjecture 3 (open since 2020) asserts that for every $r$-regular graph $G$
> (every vertex has degree $r$),
>
> $$i(G) \le \mu^*(G),$$
>
> where $i(G)$ is the independent domination number and $\mu^*(G)$ the saturation
> number (minimum size of a maximal matching).

*Quoted from [FormalConjectures/Arxiv/2507.17780/3.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2507.17780/3.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Arxiv.«2507.17780».tx_graffiti_conjecture_3`

Open: stated without proof.

> TxGraffiti [Conjecture 3](https://arxiv.org/abs/2507.17780):
> for every $r$-regular graph $G$ ($r \ge 1$),
>
> $$i(G) \le \mu^*(G).$$
>
> This conjecture is **open**.

```lean
theorem tx_graffiti_conjecture_3 (V : Type) [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (r : ℕ) (_hReg : ∀ v, G.degree v = r) (_hr : 1 ≤ r) :
    G.indepDominationNumber ≤ G.saturationNumber
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2507.17780/3.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2507.17780/3.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2507.17780/3.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2507.17780/3.lean)
- [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
