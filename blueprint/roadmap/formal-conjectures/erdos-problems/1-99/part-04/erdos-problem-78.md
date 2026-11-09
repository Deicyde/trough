---
declaration: theorem
origin: cited
lean: Erdos78.erdos_78, Erdos78.erdos_78.variants.nonconstructive, Erdos78.erdos_78.variants.little_o_sqrt, Erdos78.erdos_78.variants.cohen, Erdos78.erdos_78.variants.li, Erdos78.erdos_78.variants.strongly_explicit, Erdos78.erdos_78.variants.li_strongly_explicit
statement: formalized
---

# Erdős Problem 78

> *References:*
> - [erdosproblems.com/78](https://www.erdosproblems.com/78)
> - [Co15] Cohen, Gil, *Two-source dispersers for polylogarithmic entropy and improved Ramsey
>   graphs*. arXiv:1506.04428 (2015).
> - [Er47] Erdős, P., *Some remarks on the theory of graphs*. Bull. Amer. Math. Soc. (1947),
>   292-294.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Er88] Erdős, P, Problems and results in combinatorial analysis and graph theory. Discrete Math.
>   (1988), 81-92.
> - [Er93] Erdős, Paul, Some of my favorite solved and unsolved problems in graph theory. Quaestiones
>   Math. (1993), 333-350.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul
>   Erdős, I (1997), 47-67.
> - [Li23b] Li, Xin, *Two source extractors for asymptotically optimal entropy, and (many) more*.
>   arXiv:2303.06802 (2023).
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference "Paul
>   Erdős and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/78.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/78](https://www.erdosproblems.com/78).

The file states 7 research or textbook statements: 2 open and 5 solved.

## `Erdos78.erdos_78`

Open: stated without proof.

> Let $R(k)$ be the Ramsey number for $K_k$. Give a constructive proof that $R(k) > C^k$ for some
> constant $C > 1$.
>
> Equivalently, give an explicit construction of graphs on $n$ vertices which contain no clique
> and no independent set of size $\geq c \log n$, for some constant $c > 0$.
>
> We formalise "explicit" as: the adjacency relation of the graph on $n$ vertices is decided by a
> single algorithm that runs in time polynomial in $n$ (see `explicitGraph`). This is the weakest
> reasonable notion ("weakly explicit"); even this is open. The strongly explicit version, with time
> polynomial in $\log n$, is `erdos_78.variants.strongly_explicit`.
>
> This problem is #4 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_78 :
    ∃ c > (0 : ℝ), ∃ adj : List Bool × ℕ × ℕ → Bool, IsPolyTime adj ∧
      ∀ᶠ n in atTop, NoHomogeneousSet (explicitGraph adj n) ⌈c * log n⌉₊
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [68 Computer science](../../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/ErdosProblems/78.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean#L96).

## `Erdos78.erdos_78.variants.nonconstructive`

Solved: stated here without proof.

> Erdős [Er47] gave a simple probabilistic, non-constructive proof that $R(k) > C^k$ for some
> constant $C > 1$. In fact $R(k) > 2^{k/2}$ for all $k \geq 3$.

```lean
theorem erdos_78.variants.nonconstructive :
    ∃ C > (1 : ℝ), ∀ᶠ k in atTop, C ^ k < (SimpleGraph.diagonalRamsey k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/78.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean#L106).

## `Erdos78.erdos_78.variants.little_o_sqrt`

Solved: stated here without proof.

> Erdős also asked for an explicit construction of graphs on $n$ vertices whose largest clique and
> independent set have size $o(n^{1/2})$. Such constructions are now known; see [Co15] for the
> history.

```lean
theorem erdos_78.variants.little_o_sqrt :
    ∃ f : ℕ → ℝ, f =o[atTop] (fun n ↦ √(n : ℝ)) ∧
      ∃ adj : List Bool × ℕ × ℕ → Bool, IsPolyTime adj ∧
        ∀ᶠ n in atTop, NoHomogeneousSet (explicitGraph adj n) ⌈f n⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [68 Computer science](../../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/ErdosProblems/78.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean#L116).

## `Erdos78.erdos_78.variants.cohen`

Solved: stated here without proof.

> Cohen [Co15] constructed explicit graphs on $n$ vertices with no clique and no independent set
> of size $2^{(\log \log n)^C}$, for some constant $C > 0$.

```lean
theorem erdos_78.variants.cohen :
    ∃ C > (0 : ℝ), ∃ adj : List Bool × ℕ × ℕ → Bool, IsPolyTime adj ∧
      ∀ᶠ n in atTop,
        NoHomogeneousSet (explicitGraph adj n) ⌈(2 : ℝ) ^ (log (log n)) ^ C⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [68 Computer science](../../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/ErdosProblems/78.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean#L127).

## `Erdos78.erdos_78.variants.li`

Solved: stated here without proof.

> Li [Li23b] improved this to explicit graphs on $n$ vertices with no clique and no independent set
> of size $(\log n)^C$, for some constant $C > 0$.

```lean
theorem erdos_78.variants.li :
    ∃ C > (0 : ℝ), ∃ adj : List Bool × ℕ × ℕ → Bool, IsPolyTime adj ∧
      ∀ᶠ n in atTop, NoHomogeneousSet (explicitGraph adj n) ⌈(log n) ^ C⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [68 Computer science](../../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/ErdosProblems/78.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean#L138).

## `Erdos78.erdos_78.variants.strongly_explicit`

Open: stated without proof.

> The strongly explicit version of `erdos_78`: an explicit family of graphs on $n$ vertices with no
> clique and no independent set of size $\geq c \log n$, where each adjacency query is answered in
> time polynomial in $\log n$ (see `stronglyExplicitGraph`).

```lean
theorem erdos_78.variants.strongly_explicit :
    ∃ c > (0 : ℝ), ∃ adj : ℕ × ℕ × ℕ → Bool, IsPolyTime adj ∧
      ∀ᶠ n in atTop, NoHomogeneousSet (stronglyExplicitGraph adj n) ⌈c * log n⌉₊
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [68 Computer science](../../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/ErdosProblems/78.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean#L149).

## `Erdos78.erdos_78.variants.li_strongly_explicit`

Solved: stated here without proof.

> The construction of Li [Li23b] is strongly explicit: there are graphs on $n$ vertices with no
> clique and no independent set of size $(\log n)^C$, for some constant $C > 0$, whose adjacency
> queries are answered in time polynomial in $\log n$.

```lean
theorem erdos_78.variants.li_strongly_explicit :
    ∃ C > (0 : ℝ), ∃ adj : ℕ × ℕ × ℕ → Bool, IsPolyTime adj ∧
      ∀ᶠ n in atTop, NoHomogeneousSet (stronglyExplicitGraph adj n) ⌈(log n) ^ C⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [68 Computer science](../../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/ErdosProblems/78.lean, line 160](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean#L160).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/78.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/78.lean)
- [erdosproblems.com/78](https://www.erdosproblems.com/78)
