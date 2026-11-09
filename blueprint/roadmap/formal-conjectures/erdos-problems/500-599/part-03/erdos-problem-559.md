---
declaration: theorem
origin: cited
lean: Erdos559.erdos_559, Erdos559.erdos_559.variants.degree_three, Erdos559.erdos_559.variants.rodl_szemeredi, Erdos559.erdos_559.variants.tikhomirov, Erdos559.erdos_559.variants.trees, Erdos559.erdos_559.variants.draganic_petrova
statement: formalized
---

# Erdős Problem 559

> *References:*
> - [erdosproblems.com/559](https://www.erdosproblems.com/559)
> - [Be83b] Beck, József, _On size Ramsey number of paths, trees, and circuits. I_. J. Graph
>   Theory (1983), 115-129.
> - [FrPi87] Friedman, J. and Pippenger, N., _Expanding graphs contain all small trees_.
>   Combinatorica (1987), 71-76.
> - [HKL95] Haxell, P. E. and Kohayakawa, Y. and Łuczak, T., _The induced size-Ramsey number of
>   cycles_. Combin. Probab. Comput. (1995), 217-239.
> - [RoSz00] Rödl, Vojtěch and Szemerédi, Endre, _On size Ramsey numbers of graphs with bounded
>   degree_. Combinatorica (2000), 257-262.
> - [Ti22b] Tikhomirov, K., _On bounded degree graphs with large size-Ramsey numbers_.
>   arXiv:2210.05818 (2022).
> - [DrPe22] N. Draganić and K. Petrova, _Size-Ramsey numbers of graphs with maximum degree three_.
>   arXiv:2207.05048 (2022).

*Quoted from [FormalConjectures/ErdosProblems/559.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/559](https://www.erdosproblems.com/559).

The file states 6 research or textbook statements: 6 solved.

## `Erdos559.erdos_559`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos559.lean#L1275](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos559.lean#L1275).

> Let $\hat{R}(G)$ denote the size Ramsey number, the minimal number of edges $m$ such that there is
> a graph $H$ with $m$ edges that is Ramsey for $G$.
>
> If $G$ has $n$ vertices and maximum degree $d$ then prove that
>
> $$\hat{R}(G)\ll_d n.$$
>
> This was disproved for $d=3$ by Rödl and Szemerédi [RoSz00], who constructed a graph on $n$
> vertices with maximum degree $3$ such that $\hat{R}(G)\gg n(\log n)^{c}$ for some absolute
> constant $c>0$.

```lean
theorem erdos_559 :
    ¬ ∀ d : ℕ, ∃ C : ℝ, ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      G.maxDegree ≤ d → (sizeRamsey G G : ℝ) ≤ C * Fintype.card V
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/559.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean#L60).

## `Erdos559.erdos_559.variants.degree_three`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos559.lean#L1275](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos559.lean#L1275).

> Rödl and Szemerédi [RoSz00] disproved the linear bound already for maximum degree $3$.

```lean
theorem erdos_559.variants.degree_three :
    ¬ ∃ C : ℝ, ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      G.maxDegree ≤ 3 → (sizeRamsey G G : ℝ) ≤ C * Fintype.card V
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/559.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean#L70).

## `Erdos559.erdos_559.variants.rodl_szemeredi`

Solved: stated here without proof.

> Rödl and Szemerédi [RoSz00] constructed, for infinitely many $n$, a graph on $n$ vertices
> with maximum degree $3$ such that $\hat{R}(G)\gg n(\log n)^{c}$ for some absolute constant
> $c>0$.

```lean
theorem erdos_559.variants.rodl_szemeredi :
    ∃ c > (0 : ℝ), ∃ C > 0, ∃ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      G.maxDegree ≤ 3 ∧ C * n * (log n) ^ c ≤ sizeRamsey G G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/559.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean#L80).

## `Erdos559.erdos_559.variants.tikhomirov`

Solved: stated here without proof.

> Tikhomirov [Ti22b] improved this to $\hat{R}(G)\gg n\exp(c\sqrt{\log n})$.

```lean
theorem erdos_559.variants.tikhomirov :
    ∃ c > 0, ∃ C > 0, ∃ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      G.maxDegree ≤ 3 ∧ C * n * exp (c * √(log n)) ≤ sizeRamsey G G
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/559.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean#L88).

## `Erdos559.erdos_559.variants.trees`

Solved: stated here without proof.

> Friedman and Pippenger [FrPi87] proved the linear bound when $G$ is a tree.

```lean
theorem erdos_559.variants.trees (d : ℕ) :
    ∃ C : ℝ, ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      G.IsTree → G.maxDegree ≤ d → (sizeRamsey G G : ℝ) ≤ C * Fintype.card V
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/559.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean#L96).

## `Erdos559.erdos_559.variants.draganic_petrova`

Solved: stated here without proof.

> The best known upper bound for graphs of maximum degree $3$ is $\hat{R}(G)\leq n^{3/2+o(1)}$,
> due to Draganić and Petrova [DrPe22].

```lean
theorem erdos_559.variants.draganic_petrova (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      G.maxDegree ≤ 3 → (sizeRamsey G G : ℝ) ≤ (n : ℝ) ^ (3 / 2 + ε : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/559.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/559.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/559.lean)
- [erdosproblems.com/559](https://www.erdosproblems.com/559)
