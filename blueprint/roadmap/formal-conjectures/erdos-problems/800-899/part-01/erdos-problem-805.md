---
declaration: theorem
origin: cited
lean: Erdos805.erdos_805.parts.i, Erdos805.erdos_805.parts.ii, Erdos805.erdos_805.variants.alon_sudakov, Erdos805.erdos_805.variants.alon_bucic_sudakov
statement: formalized
---

# Erdős Problem 805

> *References:*
> - [erdosproblems.com/805](https://www.erdosproblems.com/805)
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [AlSu07] Alon, N. and Sudakov, B., *On graphs with subgraphs having large independence
>   numbers*. J. Graph Theory 56 (2007), 149-157.
>   [arXiv:0706.4099](https://arxiv.org/abs/0706.4099)
> - [ABS21] Alon, N., Bucić, M. and Sudakov, B., *Large cliques and independent sets all over the
>   place*. Proc. Amer. Math. Soc. 149 (2021), 3145-3157.
>   [arXiv:2004.04718](https://arxiv.org/abs/2004.04718)

*Quoted from [FormalConjectures/ErdosProblems/805.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/805.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/805](https://www.erdosproblems.com/805).

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 1 API statement, counted here but not shown.

## `Erdos805.erdos_805.parts.i`

Open: stated without proof.

> For which functions $g(n)$ with $n>g(n)\geq (\log n)^2$ is there a graph on $n$ vertices in which
> every induced subgraph on $g(n)$ vertices contains a clique of size $\geq \log n$ and an
> independent set of size $\geq \log n$?
>
> In particular, is there such a graph for $g(n)=(\log n)^3$?
>
> This is the first part. A problem of Erdős and Hajnal [Er91]; see also
> [erdosproblems.com/804](https://www.erdosproblems.com/804). The inequalities
> on `g` are required for all large `n`, and a graph is required for all large `n`.

```lean
theorem erdos_805.parts.i :
    {g : ℕ → ℕ | (∀ᶠ n : ℕ in atTop, Real.log n ^ 2 ≤ g n ∧ g n < n) ∧ HasRamseyGraphs g} =
      erdos_805.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/805.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/805.lean#L82).

## `Erdos805.erdos_805.parts.ii`

Open: stated without proof.

> For which functions $g(n)$ with $n>g(n)\geq (\log n)^2$ is there a graph on $n$ vertices in which
> every induced subgraph on $g(n)$ vertices contains a clique of size $\geq \log n$ and an
> independent set of size $\geq \log n$?
>
> In particular, is there such a graph for $g(n)=(\log n)^3$?
>
> This is the second part. Erdős and Hajnal thought that there is no such graph for
> $g(n)=(\log n)^3$ [AlSu07]; we state the positive proposition, with $g(n)=\lfloor(\log n)^3\rfloor$
> and a graph required for all large $n$, as in the first part.

```lean
theorem erdos_805.parts.ii : HasRamseyGraphs (fun n ↦ ⌊Real.log n ^ 3⌋₊)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/805.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/805.lean#L99).

## `Erdos805.erdos_805.variants.alon_sudakov`

Solved: stated here without proof.

> Alon and Sudakov [AlSu07] proved that there is no such graph with
>
> $$g(n)=\frac{c}{\log\log n}(\log n)^3$$
>
> for some constant $c>0$.
>
> Here `log` is the natural logarithm, as in [AlSu07], and the statement is for all large `n`.

```lean
theorem erdos_805.variants.alon_sudakov :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop, ¬ ∃ G : SimpleGraph (Fin n),
      IsLocallyRamsey G ⌊c * Real.log n ^ 3 / Real.log (Real.log n)⌋₊ ⌈Real.log n⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/805.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/805.lean#L110).

## `Erdos805.erdos_805.variants.alon_bucic_sudakov`

Solved: stated here without proof.

> Alon, Bucić, and Sudakov [ABS21] construct such a graph with
>
> $$g(n)\leq 2^{2^{(\log\log n)^{1/2+o(1)}}}.$$
>
> Here all logarithms are to base $2$, as in [ABS21], so the cliques and independent sets have at
> least $\lceil\log_2 n\rceil$ vertices; this implies the natural-logarithm version of the problem.
> The $o(1)$ is expressed as: for every $0\lt \varepsilon<1/2$ and all large $n$ there is such a graph
> with $g(n)=\lceil 2^{2^{(\log_2\log_2 n)^{1/2+\varepsilon}}}\rceil$. This form, with the rounding,
> follows from [ABS21, Theorem 2].

```lean
theorem erdos_805.variants.alon_bucic_sudakov :
    ∀ ε : ℝ, 0 < ε → ε < 1 / 2 → ∀ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      IsLocallyRamsey G
        ⌈(2 : ℝ) ^ ((2 : ℝ) ^ (Real.logb 2 (Real.logb 2 n) ^ (1 / 2 + ε)))⌉₊
        ⌈Real.logb 2 n⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/805.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/805.lean#L126).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/805.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/805.lean)
- [erdosproblems.com/805](https://www.erdosproblems.com/805)
