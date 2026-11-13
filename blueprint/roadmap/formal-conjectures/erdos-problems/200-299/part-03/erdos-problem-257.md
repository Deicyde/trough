---
declaration: theorem
origin: cited
lean: Erdos257.erdos_257, Erdos257.erdos_257.variants.tsum_top_eq, Erdos257.erdos_257.variants.tsum_top, Erdos257.erdos_257.variants.summable_reciprocal_support
statement: formalized
---

# Erdős Problem 257

> *Reference:* [erdosproblems.com/257](https://www.erdosproblems.com/257)

*Quoted from [FormalConjectures/ErdosProblems/257.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/257.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/257](https://www.erdosproblems.com/257).

The file states 4 research or textbook statements: 1 open, 2 solved and 1 textbook result.

## `Erdos257.erdos_257`

Open: stated without proof.

> Let $A\subseteq\mathbb{N}$ be an infinite set. Is
>
> $$
> \sum_{n\in A} \frac{1}{2^n - 1}
> $$
>
> irrational?

```lean
theorem erdos_257 : ∀ (A : Set ℕ), A.Infinite →
    Irrational (∑' n : A, (1 : ℝ) / (2 ^ n.1 - 1))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/257.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/257.lean#L38).

## `Erdos257.erdos_257.variants.tsum_top_eq`

Textbook result, proved here.

> Show that
>
> $$
> \sum_{n} \frac{1}{2^n - 1} = \sum_{n} \frac{d(n)}{2^n},
> $$
>
> where $d(n)$ is the number of divisors of $n$.

```lean
theorem erdos_257.variants.tsum_top_eq :
    ∑' n, 1 / (2 ^ n - 1 : ℝ) = ∑' n, n.divisors.card / (2 ^ n : ℝ)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/257.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/257.lean#L50).

## `Erdos257.erdos_257.variants.tsum_top`

Solved: stated here; a Lean proof is at [https://github.com/wcook04/plectis-erdos-lean/blob/c4eab2571b4692ee9c08d3ec138176f7fbfa09a9/verification/FCMergedIntegerAdapters/research/adapters/FormalConjecturesAdapter.lean#L121-L134](https://github.com/wcook04/plectis-erdos-lean/blob/c4eab2571b4692ee9c08d3ec138176f7fbfa09a9/verification/FCMergedIntegerAdapters/research/adapters/FormalConjecturesAdapter.lean#L121-L134).

> Show that
>
> $$
> \sum_{n} \frac{d(n)}{2^n}
> $$
>
> is irrational.
>
> [Er48] Erdős, P., _On arithmetical properties of Lambert series_. J. Indian Math. Soc. (N.S.) (1948), 63-66.

```lean
theorem erdos_257.variants.tsum_top :
    Irrational <| ∑' n, n.divisors.card / (2 ^ n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/257.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/257.lean#L101).

## `Erdos257.erdos_257.variants.summable_reciprocal_support`

Solved: stated here; a Lean proof is at [https://github.com/wcook04/plectis-erdos-lean/blob/ec92e5ce12c6117a24e4b532ea565ba332a1df7b/verification/FC257ReciprocalSupport/verification/Solutions/FC257Subtype.lean#L10-L17](https://github.com/wcook04/plectis-erdos-lean/blob/ec92e5ce12c6117a24e4b532ea565ba332a1df7b/verification/FC257ReciprocalSupport/verification/Solutions/FC257Subtype.lean#L10-L17).

> Let $A \subseteq \mathbb{N}$ be infinite with $\sum_{a \in A} 1/a < \infty$.
> For every integer base $b \ge 2$, the series
>
> $$
> \sum_{a \in A} \frac{1}{b^a - 1}
> $$
>
> is irrational. No pairwise coprimality assumption is needed. Exponent zero
> contributes zero under Lean's real-division convention.
>
> Erdős stated the coprimality-free result in *On the irrationality of certain
> series*, Math. Student 36 (1968), p. 222. A proof and formalisation appear in
> W. Cook,
> *Reciprocal Mersenne Subseries*:
> https://github.com/wcook04/plectis-erdos/blob/598cd7bac8b73dcfef3687f46922c1ef6da766ae/docs/papers/full-text/erdos257-mersenne-reasoning-surface.md

```lean
theorem erdos_257.variants.summable_reciprocal_support
    (b : ℕ) (A : Set ℕ) (hb : 2 ≤ b) (hA : A.Infinite)
    (hsum : Summable fun a : A => 1 / (a : ℝ)) :
    Irrational (∑' n : A, 1 / ((b : ℝ) ^ (n : ℕ) - 1))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/257.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/257.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/257.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/257.lean)
- [erdosproblems.com/257](https://www.erdosproblems.com/257)
