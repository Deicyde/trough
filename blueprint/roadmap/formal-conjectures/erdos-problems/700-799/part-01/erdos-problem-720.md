---
declaration: theorem
origin: cited
lean: Erdos720.erdos_720.parts.i, Erdos720.erdos_720.parts.ii, Erdos720.erdos_720.parts.iii, Erdos720.erdos_720.variants.beck
statement: formalized
---

# Erdős Problem 720

> *References:*
> - [erdosproblems.com/720](https://www.erdosproblems.com/720)
> - [Er76c] Erdős, P., _Some recent problems and results in graph theory, combinatorics and number
>   theory_. Proceedings of the Seventh Southeastern Conference on Combinatorics, Graph Theory,
>   and Computing (Louisiana State Univ., Baton Rouge, La., 1976) (1976), 3-14.
> - [EFRS78b] Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., _The size Ramsey
>   number_. Period. Math. Hungar. (1978), 145-161.
> - [Er78] Erdős, Paul, _Problems and results in combinatorial analysis and combinatorial number
>   theory_. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
>   Computing (Florida Atlantic Univ., Boca Raton, Fla., 1978) (1978), 29-40.
> - [Er81] Erdős, P., _On the combinatorial problems which I would most like to see solved_.
>   Combinatorica (1981), 25-42.
> - [Er82e] Erdős, Paul, _Some of my favourite problems which recently have been solved_. (1982),
>   59--79.
> - [Be83b] Beck, József, _On size Ramsey number of paths, trees, and circuits. I_. J. Graph
>   Theory (1983), 115-129.

*Quoted from [FormalConjectures/ErdosProblems/720.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/720.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/720](https://www.erdosproblems.com/720).

The file states 4 research or textbook statements: 4 solved.

## `Erdos720.erdos_720.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39).

> Let $\hat{R}(G)$ denote the size Ramsey number, the minimal number of edges $m$ such that there
> is a graph $H$ with $m$ edges such that in any $2$-colouring of the edges of $H$ there is a
> monochromatic copy of $G$.
>
> Is it true that, if $P_n$ is the path of length $n$, then $\hat{R}(P_n)/n\to \infty$?
>
> The answer is no: Beck [Be83b] proved that in fact $\hat{R}(P_n)\ll n$.

```lean
theorem erdos_720.parts.i :
    ¬ Tendsto (fun n : ℕ ↦ (sizeRamseyNumber (pathGraph (n + 1)) : ℝ) / n) atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/720.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/720.lean#L64).

## `Erdos720.erdos_720.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39).

> Is it true that, if $P_n$ is the path of length $n$, then $\hat{R}(P_n)/n^2 \to 0$?
>
> The answer is yes: Beck [Be83b] proved that in fact $\hat{R}(P_n)\ll n$.

```lean
theorem erdos_720.parts.ii :
    Tendsto (fun n : ℕ ↦ (sizeRamseyNumber (pathGraph (n + 1)) : ℝ) / (n : ℝ) ^ 2) atTop
      (nhds 0)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/720.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/720.lean#L76).

## `Erdos720.erdos_720.parts.iii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39).

> Is it true that, if $C_n$ is the cycle with $n$ edges, then $\hat{R}(C_n) =o(n^2)$?
>
> The answer is yes: Beck [Be83b] proved that in fact $\hat{R}(C_n)\ll n$.

```lean
theorem erdos_720.parts.iii :
    Tendsto (fun n : ℕ ↦ (sizeRamseyNumber (cycleGraph n) : ℝ) / (n : ℝ) ^ 2) atTop
      (nhds 0)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/720.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/720.lean#L89).

## `Erdos720.erdos_720.variants.beck`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos720.lean#L39).

> Beck [Be83b] proved that $\hat{R}(P_n)\ll n$ and $\hat{R}(C_n)\ll n$.

```lean
theorem erdos_720.variants.beck :
    ∃ C : ℕ, ∀ᶠ n : ℕ in atTop,
      sizeRamseyNumber (pathGraph (n + 1)) ≤ C * n ∧
        sizeRamseyNumber (cycleGraph n) ≤ C * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/720.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/720.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/720.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/720.lean)
- [erdosproblems.com/720](https://www.erdosproblems.com/720)
