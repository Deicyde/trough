---
declaration: theorem
origin: cited
lean: Erdos21.erdos_21, Erdos21.erdos_21.variants.lower, Erdos21.erdos_21.variants.three_n, Erdos21.erdos_21.variants.small_values
statement: formalized
---

# Erdős Problem 21

> *References:*
> - [erdosproblems.com/21](https://www.erdosproblems.com/21)
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42.
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er92b] Erdős, Paul, *Some of my favourite problems in various branches of combinatorics*.
>   Matematiche (Catania) (1992), 231-240.
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.
> - [ErLo75] Erdős, P. and Lovász, L., *Problems and results on $3$-chromatic hypergraphs and some
>   related questions*. (1975), 609--627.
> - [Ka92b] Kahn, Jeff, *On a problem of Erdős and Lovász: random lines in a projective plane*.
>   Combinatorica (1992), 417-423.
> - [Ka94] Kahn, Jeff, *On a problem of Erdős and Lovász. II. $n(r)=O(r)$*. J. Amer. Math. Soc.
>   (1994), 125-143.
> - [Tr14] A. Tripathi, *A result on intersecting families with maximum transversal size*.
>   arXiv:1409.4610 (2014).
> - [BaWa21] J. Barát and I. M. Wanless, *Intersecting and 2-intersecting hypergraphs with maximal
>   covering number: the Erdős-Lovász theme revisited*. J. Combin. Des. (2021), 260-286.

*Quoted from [FormalConjectures/ErdosProblems/21.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/21.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/21](https://www.erdosproblems.com/21).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos21.erdos_21`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos21.lean#L13036](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos21.lean#L13036).

> Let $f(n)$ be minimal such that there is an intersecting family $\mathcal{F}$ of sets of size $n$
> (so $A\cap B\neq\emptyset$ for all $A,B\in \mathcal{F}$) with $\lvert \mathcal{F}\rvert=f(n)$
> such that any set $S$ with $\lvert S\rvert \leq n-1$ is disjoint from at least one
> $A\in \mathcal{F}$.
>
> Is it true that
>
> $$f(n) \ll n?$$
>
> Conjectured by Erdős and Lovász [ErLo75], who proved that
>
> $$\frac{8}{3}n-3\leq f(n) \ll n^{3/2}\log n$$
>
> for all $n$. The upper bound was improved by Kahn [Ka92b] to $f(n) \ll n\log n$. (The upper
> bound constructions in both cases are formed by taking a random set of lines from a projective
> plane of order $n-1$, assuming $n-1$ is a prime power.)
>
> This problem was solved by Kahn [Ka94] who proved the upper bound $f(n) \ll n$. The Erdős-Lovász
> lower bound of $\frac{8}{3}n-O(1)$ has not been improved, and it has been speculated (see e.g.
> [Ka94]) that the correct answer is $3n+O(1)$.
>
> It is trivial that $f(1)=1$ and $f(2)=3$. The values $f(3)=6$ and $f(4)=9$ were established by
> Tripathi [Tr14]. Barát and Wanless [BaWa21] proved that $f(5)=13$, and that $13\leq f(6)\leq 18$.

```lean
theorem erdos_21 : ∃ C : ℕ, ∀ᶠ n : ℕ in atTop, f n ≤ C * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/21.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/21.lean#L86).

## `Erdos21.erdos_21.variants.lower`

Solved: stated here without proof.

> Erdős and Lovász [ErLo75] proved that $\frac{8}{3}n-3\leq f(n)$ for all $n$.

```lean
theorem erdos_21.variants.lower (n : ℕ) : (8 / 3 : ℝ) * n - 3 ≤ f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/21.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/21.lean#L91).

## `Erdos21.erdos_21.variants.three_n`

Open: stated without proof.

> It has been speculated (see e.g. [Ka94]) that the correct answer is $3n+O(1)$.

```lean
theorem erdos_21.variants.three_n : ∃ C : ℕ, ∀ᶠ n : ℕ in atTop,
    f n ≤ 3 * n + C ∧ 3 * n ≤ f n + C
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/21.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/21.lean#L96).

## `Erdos21.erdos_21.variants.small_values`

Solved: stated here without proof.

> $f(1)=1$, $f(2)=3$, $f(3)=6$ [Tr14], $f(4)=9$ [Tr14] and $f(5)=13$ [BaWa21].

```lean
theorem erdos_21.variants.small_values : f 1 = 1 ∧ f 2 = 3 ∧ f 3 = 6 ∧ f 4 = 9 ∧ f 5 = 13
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/21.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/21.lean#L102).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/21.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/21.lean)
- [erdosproblems.com/21](https://www.erdosproblems.com/21)
