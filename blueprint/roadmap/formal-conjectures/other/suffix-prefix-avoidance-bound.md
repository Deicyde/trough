---
declaration: theorem
origin: cited
lean: SuffixPrefixAvoidance.suffix_prefix_avoidance_bound, SuffixPrefixAvoidance.suffix_prefix_avoidance_weaker_bound
statement: formalized
---

# Suffix-prefix avoidance bound

> Let $A$ and $B$ be sets of words of length $n$ over an alphabet with $q$ letters. If no
> (nonempty) suffix of any word in $A$ coincides with a prefix of any word in $B$, then
>
> $$|A| \cdot |B| \leq \frac{q^{2n}}{en}.$$
>
> *References:*
> - [X post by Dmitry Rybin](https://x.com/DmitryRybin1/status/2027278135847428577)
> - [Maximal sets of strings with no prefix-suffix overlap]
>   (https://mathoverflow.net/questions/508648/maximal-sets-of-strings-with-no-prefix-suffix-overlap)
>   by *Dmitry Rybin*, MathOverflow (2026)
> - [An isoperimetric inequality for word overlap](https://arxiv.org/abs/2602.20143)
>   by *Dmitrii Zakharov* (2026)

*Quoted from [FormalConjectures/Other/SuffixPrefixAvoidance.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SuffixPrefixAvoidance.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `SuffixPrefixAvoidance.suffix_prefix_avoidance_bound`

Solved: stated here without proof.

> $A$ and $B$ are sets of words of length $n$ over alphabet with $q \geq 1$ letters.
> No suffix of a word in $A$ coincides with a prefix of a word in $B$.
> Then $|A| \cdot |B|$ is at most $\frac{q^{2n}}{en}$.
>
> This problem is from *Maximal sets of strings with no prefix-suffix overlap* and was proved in
> *An isoperimetric inequality for word overlap*.

```lean
theorem suffix_prefix_avoidance_bound
    (A B : Finset (Fin n → Fin q))
    (hq : 0 < q) (hn : 0 < n)
    (h : IsSuffixPrefixAvoiding A B) :
    (A.card : ℝ) * B.card ≤ (q : ℝ) ^ (2 * n) / (exp 1 * n)
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Other/SuffixPrefixAvoidance.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SuffixPrefixAvoidance.lean#L76).

## `SuffixPrefixAvoidance.suffix_prefix_avoidance_weaker_bound`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/102e47fee802d461946e3a4e0b47fdbe7db4c1ed/FormalConjectures/Other/SuffixPrefixAvoidance.lean#L157](https://github.com/google-deepmind/formal-conjectures/blob/102e47fee802d461946e3a4e0b47fdbe7db4c1ed/FormalConjectures/Other/SuffixPrefixAvoidance.lean#L157).

> $A$ and $B$ are sets of words of length $n$ over alphabet with $q \geq 1$ letters.
> No suffix of a word in $A$ coincides with a prefix of a word in $B$.
> Then $|A| \cdot |B|$ is at most $\frac{q^{2n}}{n}$.

```lean
theorem suffix_prefix_avoidance_weaker_bound
    (A B : Finset (Fin n → Fin q))
    (_hq : 0 < q) (hn : 0 < n)
    (h : IsSuffixPrefixAvoiding A B) :
    (A.card : ℚ) * B.card ≤ (q : ℚ) ^ (2 * n) / n
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Other/SuffixPrefixAvoidance.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SuffixPrefixAvoidance.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/SuffixPrefixAvoidance.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SuffixPrefixAvoidance.lean)
- [X post by Dmitry Rybin](https://x.com/DmitryRybin1/status/2027278135847428577)
