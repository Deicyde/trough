---
declaration: theorem
origin: cited
lean: Erdos163.erdos_163
statement: formalized
---

# Erdős Problem 163

> *References:*
> - [erdosproblems.com/163](https://www.erdosproblems.com/163)
> - [BuEr75] Burr, S. A. and Erdős, P., On the Ramsey number of graphs with small degree-ratio.
>   Colloq. Math. Soc. János Bolyai (1975).
> - [Le17] Lee, C., Ramsey numbers of degenerate graphs. Ann. of Math. (2) 185 (2017), 791-829.

*Quoted from [FormalConjectures/ErdosProblems/163.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/163.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/163](https://www.erdosproblems.com/163).

The file states 1 research or textbook statement: 1 solved.

## `Erdos163.erdos_163`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos163.lean#L53](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos163.lean#L53).

> The Burr-Erdős conjecture: For any $d\geq 1$ if $H$ is a graph such that every subgraph
> contains a vertex of degree at most $d$ then
>
> $$R(H)\ll_d n.$$
>
> Solved by Lee [Le17], who proved that $R(H) \leq 2^{2^{O(d)}}n$.
>
> This problem is #9 in Ramsey Theory in the graphs problem collection.
>
> The linked formal proof (Codex and GPT-5.6 Sol) gives, for graphs `H` on `Fin n`, a natural
> constant `C ≥ 1` with `RamseyFor H (C * n)` (every red/blue colouring of `K_{C n}` contains a
> monochromatic copy of `H`); transporting along `Fintype.equivFin` gives the statement below.

```lean
theorem erdos_163 :
    ∀ (d : ℕ), 1 ≤ d →
      ∃ C > (0 : ℝ), ∀ (V : Type) [Fintype V] (H : SimpleGraph V),
        H.IsDegenerate d →
        (SimpleGraph.diagonalGraphRamsey H : ℝ) ≤ C * Fintype.card V
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/163.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/163.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/163.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/163.lean)
- [erdosproblems.com/163](https://www.erdosproblems.com/163)
