---
declaration: theorem
origin: cited
lean: Arxiv.«2507.17780».tx_graffiti_conjecture_4
statement: formalized
proof: formalized
---

# TxGraffiti Conjecture 4: the saturation number versus the harmonic index

> *Reference:* [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
> **In Reverie Together: Ten Years of Mathematical Discovery with a Machine
> Collaborator** by *Randy Davila, Boris Brimkov, Ryan Pepper*
>
> TxGraffiti is an automated conjecturing program, a successor of Fajtlowicz's
> *Graffiti* and DeLaViña's *Graffiti.pc*. Conjecture 4 in the cited collection
> asserts a bound between two graph invariants:
>
> * the *saturation number* $\mu^*(G)$ (`SimpleGraph.saturationNumber`), the
>   minimum number of edges in a maximal matching of $G$;
> * the *harmonic index* $H(G)$ (`SimpleGraph.harmonicIndex`),
>   $\sum_{uv \in E(G)} 2 / (\deg u + \deg v)$.
>
> The conjecture is **false**. It was first refuted by Bıyıkoğlu, who exhibited a
> family of counterexamples — a disjoint union of edges joined to an independent
> set — with unbounded ratio $\mu^*/H$. That the smallest counterexample has
> order $9$, namely the friendship graph $F_4$ formalised below, and that the
> windmill family has an exact limiting ratio, are established in Gupta.
>
> *References:*
> - [A Note on the TxGraffiti Conjecture about Harmonic Index and Minimum Maximal
>   Matching Number](https://doi.org/10.46793/match.96-3.28425), Türker Bıyıkoğlu,
>   *MATCH Commun. Math. Comput. Chem.* **96** (2026), no. 3, 1097–1099 — the
>   first refutation.
> - [The saturation number is not bounded by the harmonic
>   index](https://arxiv.org/abs/2606.15761), C. Gupta — the order-$9$
>   minimality of $F_4$ (formalised below) and the exact windmill limit.

*Quoted from [FormalConjectures/Arxiv/2507.17780/4.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2507.17780/4.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Arxiv.«2507.17780».tx_graffiti_conjecture_4`

Proved here.

> TxGraffiti [Conjecture 4](https://arxiv.org/abs/2507.17780):
> for every nontrivial connected graph $G$, the saturation number is at most
> the harmonic index, $\mu^*(G) \le H(G)$.
>
> This conjecture is **FALSE**.
>
> **Counterexample.**
> The friendship graph $F_4$ (`friendshipF4`) is connected and nontrivial, with
> $\mu^*(F_4) = 4$ and $H(F_4) = 18/5$. Indeed the four rim edges
> $\{1,2\}, \{3,4\}, \{5,6\}, \{7,8\}$ form a maximal matching of size $4$, and
> no maximal matching is smaller, so $\mu^*(F_4) = 4$; the eight spokes
> contribute $2/(8+2) = 1/5$ each and the four rim edges contribute
> $2/(2+2) = 1/2$ each, giving $H(F_4) = 8 \cdot 1/5 + 4 \cdot 1/2 = 18/5$.
> Since $4 > 18/5$, the bound fails.
>
> More generally the friendship graphs $F_k$ satisfy $\mu^*(F_k) = k$ and
> $H(F_k) = 2k/(k+1) + k/2$, so the conjecture fails for every $k \ge 4$. An
> exhaustive search confirms that $F_4$ is the smallest counterexample
> (order $9$). The unbounded separation was first shown by Bıyıkoğlu, whose
> family of edges joined to an independent set makes $\mu^*/H$ arbitrarily
> large; the windmill generalisation and its exact limit appear in
> [arXiv:2606.15761](https://arxiv.org/abs/2606.15761).

```lean
theorem tx_graffiti_conjecture_4 :
    ¬ ∀ (V : Type) [Fintype V] [DecidableEq V] [Nontrivial V] (G : SimpleGraph V)
      [DecidableRel G.Adj] (_hConn : G.Connected),
      (G.saturationNumber : ℚ) ≤ G.harmonicIndex
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2507.17780/4.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2507.17780/4.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2507.17780/4.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2507.17780/4.lean)
- [arxiv/2507.17780](https://arxiv.org/abs/2507.17780)
