---
declaration: theorem
origin: cited
lean: AlonSaksSeymourConjecture.alon_saks_seymour_conjecture, AlonSaksSeymourConjecture.alon_saks_seymour_conjecture.variants.graham_pollak, AlonSaksSeymourConjecture.alon_saks_seymour_conjecture.variants.huang_sudakov
statement: formalized
---

# The Alon–Saks–Seymour conjecture (disproved)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Graham%E2%80%93Pollak_theorem)
> * [GP71] Graham, R. L. and Pollak, H. O. (1971). "On the addressing problem for loop switching."
>   *Bell System Tech. J.* 50, pp. 2495--2519.
> * [Ka91] Kahn, J. (1991). "Recent results on some not-so-recent hypergraph matching and covering
>   problems." *Extremal problems for finite sets (Visegrád)*, Bolyai Soc. Math. Stud. 3,
>   pp. 305--353.
> * [HS12] Huang, H. and Sudakov, B. (2012). "A counterexample to the Alon–Saks–Seymour
>   conjecture and related problems." *Combinatorica* 32, pp. 205--219.
>   [arXiv:1002.4687](https://arxiv.org/abs/1002.4687)

*Quoted from [FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `AlonSaksSeymourConjecture.alon_saks_seymour_conjecture`

Solved: stated here without proof.

> **The Alon–Saks–Seymour conjecture — disproved.**
>
> It was conjectured (Alon, Saks and Seymour, c. 1991, see [Ka91]) that every graph whose edge
> set is partitioned into $k$ complete bipartite subgraphs is $(k+1)$-colourable, i.e.
> $\chi(G) \le \operatorname{bp}(G) + 1$ — the natural generalisation of the Graham–Pollak
> theorem, which is the case $G = K_n$.
>
> This is **false**: Huang and Sudakov [HS12] constructed graphs with
> $\chi(G) \ge c \operatorname{bp}(G)^{6/5}$.

```lean
theorem alon_saks_seymour_conjecture : ¬
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V),
      G.chromaticNumber ≤ bicliquePartitionNumber G + 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean#L73).

## `AlonSaksSeymourConjecture.alon_saks_seymour_conjecture.variants.graham_pollak`

Solved: stated here without proof.

> **The Graham–Pollak theorem (1971).**
>
> The edge set of $K_n$ cannot be partitioned into fewer than $n - 1$ complete bipartite
> subgraphs, and $n - 1$ suffice: $\operatorname{bp}(K_n) = n - 1$.
>
> *Reference:* [GP71].

```lean
theorem alon_saks_seymour_conjecture.variants.graham_pollak (n : ℕ) :
    bicliquePartitionNumber (completeGraph (Fin n)) = n - 1
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean#L87).

## `AlonSaksSeymourConjecture.alon_saks_seymour_conjecture.variants.huang_sudakov`

Solved: stated here without proof.

> **Huang–Sudakov (2012): a polynomial separation.**
>
> There is a constant $c > 0$ and, for every $k$, a graph $G$ with $\operatorname{bp}(G) \le k$
> and $\chi(G) \ge c\,k^{6/5}$.
>
> *Reference:* [HS12].

```lean
theorem alon_saks_seymour_conjecture.variants.huang_sudakov :
    ∃ c : ℝ, 0 < c ∧ ∀ k : ℕ, ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V)
      (G : SimpleGraph V), bicliquePartitionNumber G ≤ k ∧
        (c * (k : ℝ) ^ ((6 : ℝ) / 5) : ℝ) ≤ (G.chromaticNumber.toNat : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlonSaksSeymourConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Graham%E2%80%93Pollak_theorem)
