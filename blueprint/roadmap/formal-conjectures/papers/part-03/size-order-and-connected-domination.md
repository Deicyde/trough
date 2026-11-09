---
declaration: theorem
origin: cited
lean: SizeOrderConnectedDomination.mukwembi_theorem_2_1
statement: formalized
---

# Size, Order, and Connected Domination

> *References:*
> - [S. Mukwembi, _Size, order, and connected domination_,
>   Canad. Math. Bull. 57 (2014), no. 1, 141–144](https://doi.org/10.4153/CMB-2013-020-5)

*Quoted from [FormalConjectures/Paper/SizeOrderConnectedDomination.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/SizeOrderConnectedDomination.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `SizeOrderConnectedDomination.mukwembi_theorem_2_1`

Solved: stated here; a Lean proof is at [https://github.com/henrykmichalewski/formal-conjectures/blob/238fcea04077aee1d63c9201aa4b4b794f3a674d/FormalConjectures/Paper/SizeOrderConnectedDomination.lean#L156](https://github.com/henrykmichalewski/formal-conjectures/blob/238fcea04077aee1d63c9201aa4b4b794f3a674d/FormalConjectures/Paper/SizeOrderConnectedDomination.lean#L156).

> **Theorem 2.1** of [S. Mukwembi, _Size, order, and connected domination_,
> Canad. Math. Bull. 57 (2014), no. 1, 141–144](https://doi.org/10.4153/CMB-2013-020-5)
> claims: if $G$ is a connected triangle-free graph of order $n$ and size $m$ with
> connected domination number $\gamma_c$, then
> $$m \le \frac{(n - \gamma_c)^2}{4} + n - 1.$$
>
> The claim is **false**: the 3-dimensional hypercube $Q_3$ is a counterexample,
> with $n = 8$, $m = 12$ and $\gamma_c = 4$, so the asserted bound reads
> $12 \le (8-4)^2/4 + 8 - 1 = 11$. The gap in the paper's proof (p. 143) is the
> unjustified assertion that there is an edge $uv$ with
> $\gamma_c(G) \le \gamma_c(G - \{u, v\})$: in $Q_3$, removing any adjacent pair
> of vertices leaves a graph with connected domination number $2 < 4$.
>
> The corollaries of the paper (Corollary 2.2 and 2.3, on leaf numbers of
> triangle-free graphs) remain true; Corollary 2.2 is Graffiti.pc Conjecture 1.1,
> recorded as `WrittenOnTheWallII.GraphConjecture2.conjecture2`.

```lean
theorem mukwembi_theorem_2_1 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj],
      G.Connected → G.CliqueFree 3 →
      (G.edgeFinset.card : ℝ) ≤
        ((Fintype.card α : ℝ) - (G.connectedDominationNumber : ℝ)) ^ 2 / 4
          + (Fintype.card α : ℝ) - 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/SizeOrderConnectedDomination.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/SizeOrderConnectedDomination.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/SizeOrderConnectedDomination.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/SizeOrderConnectedDomination.lean)
- [S. Mukwembi, _Size, order, and connected domination_,
  Canad. Math. Bull. 57 (2014), no. 1, 141–144](https://doi.org/10.4153/CMB-2013-020-5)
