---
declaration: theorem
origin: cited
lean: AlspachConjecture.alspach_conjecture, AlspachConjecture.alspach_conjecture.variants.even, AlspachConjecture.alspach_conjecture.variants.long_cycles, AlspachConjecture.alspach_conjecture.variants.oberwolfach
statement: formalized
---

# Alspach's conjecture on cycle decompositions of complete graphs (1981; proved 2014)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Alspach%27s_conjecture)
> * [Al81] Alspach, B. (1981). "Research problems, Problem 3." *Discrete Math.* 36, p. 333.
> * [BHP14] Bryant, D., Horsley, D. and Pettersson, W. (2014). "Cycle decompositions V:
>   Complete graphs into cycles of arbitrary lengths." *Proc. London Math. Soc.* 108,
>   pp. 1153--1192. [arXiv:1204.3709](https://arxiv.org/abs/1204.3709)
> * [GJKKO21] Glock, S., Joos, F., Kim, J., Kühn, D. and Osthus, D. (2021). "Resolution of the
>   Oberwolfach problem." *J. Eur. Math. Soc.* 23, pp. 2511--2547.
>   [arXiv:1806.04644](https://arxiv.org/abs/1806.04644)

*Quoted from [FormalConjectures/Wikipedia/AlspachConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlspachConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 2 test statements and 1 API statement, counted here but not shown.

## `AlspachConjecture.alspach_conjecture`

Solved: stated here without proof.

> **Alspach's conjecture (1981), proved by Bryant, Horsley and Pettersson (2014).**
>
> Let $n$ be odd and let $m_1, \dots, m_t$ be integers with $3 \le m_i \le n$ and
> $m_1 + \dots + m_t = \binom{n}{2}$. Then the complete graph $K_n$ decomposes into cycles of
> lengths $m_1, \dots, m_t$. (These conditions are clearly necessary: $K_n$ has all degrees even
> only for odd $n$, and its edges must be split exactly among the cycles.)

```lean
theorem alspach_conjecture :
    ∀ (n : ℕ), Odd n → ∀ m : Multiset ℕ, (∀ x ∈ m, 3 ≤ x ∧ x ≤ n) → m.sum = n.choose 2 →
      ∃ C : Multiset (Cycle (completeGraph (Fin n))),
        IsCycleDecomposition (completeGraph (Fin n)) C ∧ lengths C = m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/AlspachConjecture.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlspachConjecture.lean#L63).

## `AlspachConjecture.alspach_conjecture.variants.even`

Solved: stated here without proof.

> **The even case (Bryant–Horsley–Pettersson 2014).**
>
> For even $n$, the complete graph minus a perfect matching, $K_n - I$, decomposes into cycles of
> lengths $m_1, \dots, m_t$ whenever $3 \le m_i \le n$ and $\sum m_i = \binom{n}{2} - n/2$.
> Since Mathlib has no canonical perfect matching of $K_n$, we state this for any perfect
> matching `I`.
>
> *Reference:* [BHP14].

```lean
theorem alspach_conjecture.variants.even (n : ℕ) (hn : Even n)
    (I : (completeGraph (Fin n)).Subgraph) (hI : I.IsPerfectMatching)
    (m : Multiset ℕ) (hm : ∀ x ∈ m, 3 ≤ x ∧ x ≤ n) (hsum : m.sum = n.choose 2 - n / 2) :
    ∃ C : Multiset (Cycle (completeGraph (Fin n) \ I.spanningCoe)),
      IsCycleDecomposition (completeGraph (Fin n) \ I.spanningCoe) C ∧ lengths C = m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/AlspachConjecture.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlspachConjecture.lean#L81).

## `AlspachConjecture.alspach_conjecture.variants.long_cycles`

Solved: stated here without proof.

> A long-cycle corollary of the Alspach theorem (Bryant–Horsley–Pettersson 2014).
>
> For odd $n$, the conjecture holds whenever all the prescribed lengths $m_i$ are at least
> $\lceil(n+4)/2\rceil$. This follows from [BHP14, Theorem 1].

```lean
theorem alspach_conjecture.variants.long_cycles (n : ℕ) (hn : Odd n) (m : Multiset ℕ)
    (hm : ∀ x ∈ m, (n + 5) / 2 ≤ x ∧ x ≤ n) (hsum : m.sum = n.choose 2) :
    ∃ C : Multiset (Cycle (completeGraph (Fin n))),
      IsCycleDecomposition (completeGraph (Fin n)) C ∧ lengths C = m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/AlspachConjecture.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlspachConjecture.lean#L95).

## `AlspachConjecture.alspach_conjecture.variants.oberwolfach`

Open: stated without proof.

> **The Oberwolfach problem (Ringel 1967).**
>
> For odd $n$ and a $2$-regular graph $F$ on $n$ vertices, can $K_n$ be decomposed into
> $(n-1)/2$ spanning subgraphs isomorphic to $F$? The decomposition is known to be impossible for
> exactly two pairs with odd $n$ — $(9, C_4 + C_5)$ and $(11, C_3 + C_3 + C_5)$ — and is
> conjectured to exist in every other case. Known for all sufficiently large $n$ [GJKKO21].

```lean
theorem alspach_conjecture.variants.oberwolfach :
    ∀ (n : ℕ), Odd n → 3 ≤ n →
      ∀ (F : SimpleGraph (Fin n)) [DecidableRel F.Adj], (∀ v, F.degree v = 2) →
      IsEmpty (F ≃g oberwolfachException9) → IsEmpty (F ≃g oberwolfachException11) →
      ∃ D : Fin ((n - 1) / 2) → SimpleGraph (Fin n),
        (∀ i, Nonempty (D i ≃g F)) ∧
        ∀ u v, (completeGraph (Fin n)).Adj u v ↔ ∃! i, (D i).Adj u v
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/AlspachConjecture.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlspachConjecture.lean#L183).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/AlspachConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/AlspachConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Alspach%27s_conjecture)
