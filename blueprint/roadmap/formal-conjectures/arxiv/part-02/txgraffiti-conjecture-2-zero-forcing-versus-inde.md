---
declaration: theorem
origin: cited
lean: Arxiv.«2507.17780».tx_graffiti_conjecture_2
statement: formalized
---

# TxGraffiti Conjecture 2: zero forcing versus independence (cubic graphs)

> *Reference:* [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
> **In Reverie Together: Ten Years of Mathematical Discovery with a Machine
> Collaborator** by *Randy Davila, Boris Brimkov, Ryan Pepper*
>
> Conjecture 2 (open since 2017) asserts that for every connected graph $G$ with
> maximum degree at most $3$ and $G \ne K_4$,
> $$Z(G) \le \alpha(G) + 1,$$
> where $Z(G)$ is the zero forcing number and $\alpha(G)$ the independence number.

*Quoted from [FormalConjectures/Arxiv/2507.17780/2.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2507.17780/2.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Arxiv.«2507.17780».tx_graffiti_conjecture_2`

Solved: stated here without proof.

> TxGraffiti [Conjecture 2](https://arxiv.org/abs/2507.17780):
> for every connected graph $G$ with $\Delta(G) \le 3$ and $G \ne K_4$,
> $$Z(G) \le \alpha(G) + 1.$$
>
> This conjecture is **false**. Fischer gives a connected 24-vertex
> counterexample with maximum degree $3$; see
> [arXiv:2607.23664](https://arxiv.org/abs/2607.23664).

```lean
theorem tx_graffiti_conjecture_2 :
    ¬ ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
      [DecidableRel G.Adj] (_hConn : G.Connected)
      (_hDeg : G.maxDegree ≤ 3)
      (_hNotK4 : G = ⊤ → Fintype.card V ≠ 4),
      zeroForcingNumber G ≤ G.indepNum + 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2507.17780/2.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2507.17780/2.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2507.17780/2.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2507.17780/2.lean)
- [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
