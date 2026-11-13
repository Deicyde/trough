---
declaration: theorem
origin: cited
lean: Erdos703.erdos_703, Erdos703.erdos_703.variants.zero, Erdos703.erdos_703.variants.frankl_furedi
statement: formalized
---

# Erdős Problem 703

> *References:*
> - [erdosproblems.com/703](https://www.erdosproblems.com/703)
> - [Er75f] Erdős, Paul, _On some problems of elementary and combinatorial geometry_. Ann. Mat.
>   Pura Appl. (4) (1975), 99-108.
> - [Er76b] Erdős, P., _Problems and results in graph theory and combinatorial analysis_.
>   Proceedings of the Fifth British Combinatorial Conference (Univ. Aberdeen, Aberdeen, 1975)
>   (1976), 169-192.
> - [Er81] Erdős, P., _On the combinatorial problems which I would most like to see solved_.
>   Combinatorica (1981), 25-42.
> - [Er82e] Erdős, Paul, _Some of my favourite problems which recently have been solved_. (1982),
>   59--79.
> - [FrFu84b] Frankl, P. and Füredi, Z., _On hypergraphs without two edges intersecting in a given
>   number of vertices_. J. Combin. Theory Ser. A (1984), 230-236.
> - [Fr77b] Frankl, P., _An intersection problem for finite sets_. Acta Math. Acad. Sci. Hungar.
>   (1977), 371-373.
> - [FrRo87] Frankl, Peter and Rödl, Vojtech, _Forbidden intersections_. Trans. Amer. Math. Soc.
>   (1987), 259-286.

*Quoted from [FormalConjectures/ErdosProblems/703.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/703.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/703](https://www.erdosproblems.com/703).

The file states 3 research or textbook statements: 2 solved and 1 textbook result.

## `Erdos703.erdos_703`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos703.lean#L331](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos703.lean#L331).

> Let $r\geq 1$ and define $T(n,r)$ to be maximal such that there exists a family $\mathcal{F}$ of
> subsets of $\{1,\ldots,n\}$ of size $T(n,r)$ such that $\lvert A\cap B\rvert\neq r$ for all
> $A,B\in \mathcal{F}$.
>
> Estimate $T(n,r)$ for $r\geq 2$. In particular, is it true that for every $\epsilon>0$ there
> exists $\delta>0$ such that for all $\epsilon n\lt r<(1/2-\epsilon) n$ we have
>
> $$T(n,r)<(2-\delta)^n?$$
>
> The answer is yes, proved by Frankl and Rödl [FrRo87].

```lean
theorem erdos_703 :
    ∀ ε : ℝ, 0 < ε → ∃ δ : ℝ, 0 < δ ∧
      ∀ (n r : ℕ), ε * n < r → r < (1 / 2 - ε) * n → (T n r : ℝ) < (2 - δ) ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/703.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/703.lean#L69).

## `Erdos703.erdos_703.variants.zero`

Textbook result, proved here.

> It is trivial that $T(n,0)=2^{n-1}$.

```lean
theorem erdos_703.variants.zero (n : ℕ) (hn : 1 ≤ n) : T n 0 = 2 ^ (n - 1)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/703.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/703.lean#L76).

## `Erdos703.erdos_703.variants.frankl_furedi`

Solved: stated here without proof.

> Frankl and Füredi [FrFu84b] proved that, for fixed $r$ and $n$ sufficiently large in terms of
> $r$, the maximal $T(n,r)$ is achieved by taking
>
> $$\mathcal{F} = \left\{ A\subseteq \{1,\ldots,n\} : \lvert A\rvert> \frac{n+r}{2}\textrm{ or }
> \lvert A\rvert < r\right\}$$
>
> when $n+r$ is odd, and
>
> $$\mathcal{F} = \left\{ A\subseteq \{1,\ldots,n\} : \lvert A\backslash \{1\}\rvert\geq
> \frac{n+r}{2}\textrm{ or }\lvert A\rvert < r\right\}$$
>
> when $n+r$ is even.

```lean
theorem erdos_703.variants.frankl_furedi (r : ℕ) : ∀ᶠ n : ℕ in Filter.atTop,
    T n r = if (n + r) % 2 = 1 then
      ((univ : Finset (Finset (Fin n))).filter fun A ↦
        (n + r : ℝ) / 2 < A.card ∨ A.card < r).card
    else
      ((univ : Finset (Finset (Fin n))).filter fun A ↦
        (n + r : ℝ) / 2 ≤ (A.filter fun i : Fin n ↦ (i : ℕ) ≠ 0).card ∨
          A.card < r).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/703.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/703.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/703.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/703.lean)
- [erdosproblems.com/703](https://www.erdosproblems.com/703)
