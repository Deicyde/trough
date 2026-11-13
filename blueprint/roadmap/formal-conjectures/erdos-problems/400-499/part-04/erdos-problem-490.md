---
declaration: theorem
origin: cited
lean: Erdos490.erdos_490, Erdos490.erdos_490.variants.limit
statement: formalized
---

# Erdős Problem 490

> *References:*
> - [erdosproblems.com/490](https://www.erdosproblems.com/490)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er69] Erdős, Paul, *Some applications of graph theory to number theory*. The Many Facets of
>   Graph Theory (Proc. Conf., Western Mich. Univ., Kalamazoo, Mich., 1968) (1969), 77-82.
> - [Er72] Erdős, Paul, *Extremal problems in number theory*. Proceedings of the 1972 Number Theory
>   Conference (Univ. Colorado, Boulder, Colo.) (1972), 80-86.
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [Sz76] Szemerédi, E., *On a problem of P. Erdős*. J. Number Theory (1976), 264-270.

*Quoted from [FormalConjectures/ErdosProblems/490.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/490.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/490](https://www.erdosproblems.com/490).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos490.erdos_490`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos490.lean#L38](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos490.lean#L38).

> Let $A,B\subseteq \{1,\ldots,N\}$ be such that all the products $ab$ with $a\in A$ and $b\in B$
> are distinct. Is it true that
>
> $$\lvert A\rvert \lvert B\rvert \ll \frac{N^2}{\log N}?$$
>
> This would be best possible, for example letting $A=[1,N/2]\cap \mathbb{N}$ and
> $B=\{ N/2\lt p\leq N: p\textrm{ prime}\}$. This is true, and was proved by Szemerédi [Sz76].
>
> In [Er72] Erdős goes on to ask whether
>
> $$\lim_{N\to \infty}\max_{A,B\subseteq [N]}\frac{\lvert A\rvert\lvert B\rvert\log N}{N^2}$$
>
> exists, where the maximum is over $A$ and $B$ with all the products $ab$ distinct, and to
> determine its value. As noted in the comments to [896](https://www.erdosproblems.com/896) by van
> Doorn, if the limit exists it must be $\geq 1$.
>
> See also [425](https://www.erdosproblems.com/425) and [896](https://www.erdosproblems.com/896).

```lean
theorem erdos_490 : ∃ C : ℝ, ∀ᶠ N : ℕ in atTop,
    ∀ A B : Finset ℕ, A ⊆ Finset.Icc 1 N → B ⊆ Finset.Icc 1 N →
      (∀ a₁ ∈ A, ∀ b₁ ∈ B, ∀ a₂ ∈ A, ∀ b₂ ∈ B, a₁ * b₁ = a₂ * b₂ → a₁ = a₂ ∧ b₁ = b₂) →
        (A.card * B.card : ℝ) ≤ C * N ^ 2 / Real.log N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/490.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/490.lean#L62).

## `Erdos490.erdos_490.variants.limit`

Open: stated without proof.

> Erdős [Er72] asks whether
>
> $$\lim_{N\to \infty}\max_{A,B\subseteq [N]}\frac{\lvert A\rvert\lvert B\rvert\log N}{N^2}$$
>
> exists, where the maximum is over $A$ and $B$ with all the products $ab$ distinct, and to
> determine its value.

```lean
theorem erdos_490.variants.limit : ∃ L : ℝ, Tendsto (fun N : ℕ =>
    (sSup {x : ℝ | ∃ A B : Finset ℕ, A ⊆ Finset.Icc 1 N ∧ B ⊆ Finset.Icc 1 N ∧
      (∀ a₁ ∈ A, ∀ b₁ ∈ B, ∀ a₂ ∈ A, ∀ b₂ ∈ B, a₁ * b₁ = a₂ * b₂ → a₁ = a₂ ∧ b₁ = b₂) ∧
      x = A.card * B.card}) * Real.log N / N ^ 2) atTop (nhds L)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/490.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/490.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/490.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/490.lean)
- [erdosproblems.com/490](https://www.erdosproblems.com/490)
