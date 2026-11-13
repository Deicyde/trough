---
declaration: theorem
origin: cited
lean: Arxiv.«2507.17780».tx_graffiti_conjecture_1
statement: formalized
---

# TxGraffiti Conjecture 1: independence, annihilation, and residue

> *Reference:* [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
> **In Reverie Together: Ten Years of Mathematical Discovery with a Machine
> Collaborator** by *Randy Davila, Boris Brimkov, Ryan Pepper*
>
> Conjecture 1, the oldest of the four TxGraffiti conjectures in the cited
> collection (open since 2016), asserts that every nontrivial connected graph $G$
> with maximum degree $\Delta \ge 2$ satisfies
>
> $$\alpha(G) \ge \frac{a(G) + R(G)}{\Delta(G)},$$
>
> where $\alpha$ is the independence number, $a$ the annihilation number, $R$ the
> Havel–Hakimi residue, and $\Delta$ the maximum degree.
>
> This conjecture is **true**, proved in
> [arXiv:2606.29553](https://arxiv.org/abs/2606.29553) (C. Gupta).

*Quoted from [FormalConjectures/Arxiv/2507.17780/1.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2507.17780/1.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Arxiv.«2507.17780».tx_graffiti_conjecture_1`

Solved: stated here without proof.

> TxGraffiti [Conjecture 1](https://arxiv.org/abs/2507.17780):
> for every nontrivial connected graph $G$ with $\Delta(G) \ge 2$,
>
> $$\alpha(G) \ge \frac{a(G) + R(G)}{\Delta(G)}.$$
>
> This conjecture is **true**.
>
> **Proof sketch.** Substitute the Caro–Wei lower bound $\alpha \ge W$ for $\alpha$
> and reduce to $a \le (\Delta - 1) \alpha$. The case $\Delta = 2$ is trivial
> ($a = \alpha$). For $\Delta \ge 4$ an AM–HM argument with $m \le (n - a)\Delta$
> yields a quadratic whose discriminant is negative. For $\Delta = 3$ the
> annihilation number has a closed form in the degree counts $(n_1, n_2, n_3)$ and
> $a \le 2W$ is verified in three regimes. See
> [arXiv:2606.29553](https://arxiv.org/abs/2606.29553).

```lean
theorem tx_graffiti_conjecture_1 (V : Type) [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (_hConn : G.Connected)
    (_hDeg : 2 ≤ G.maxDegree) :
    (G.annihilationNumber + residue G : ℝ) / G.maxDegree ≤ G.indepNum
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2507.17780/1.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2507.17780/1.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2507.17780/1.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2507.17780/1.lean)
- [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
