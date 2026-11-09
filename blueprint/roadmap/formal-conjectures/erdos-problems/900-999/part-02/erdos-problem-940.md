---
declaration: theorem
origin: cited
lean: Erdos940.erdos_940, Erdos940.erdos_940.variants.two, Erdos940.erdos_940.variants.three_cubes, Erdos940.erdos_940.variants.large_integers, Erdos940.erdos_940.variants.three_powerful
statement: formalized
---

# Erdős Problem 940

> *References:*
> - [erdosproblems.com/940](https://www.erdosproblems.com/940)
> - [BaBr94] Baker, R. C. and Brüdern, J., _On sums of two squarefull numbers_. Math. Proc.
>   Cambridge Philos. Soc. (1994), 1-5.
> - [He88] Heath-Brown, D. R., _Ternary quadratic forms and sums of three square-full numbers_.
>   (1988), 137-163.

*Quoted from [FormalConjectures/ErdosProblems/940.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/940.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/940](https://www.erdosproblems.com/940).

The file states 5 research or textbook statements: 3 open and 2 solved.

## `Erdos940.erdos_940`

Open: stated without proof.

> Let $r \ge 3$. Is it true that the set of integers which are the sum of at most $r$ $r$-powerful numbers
> has density $0$?

```lean
theorem erdos_940 :
    ∀ r ≥ 3,
      {n : ℕ | ∃ (S : Multiset ℕ), S.card ≤ r ∧ (∀ s ∈ S, r.Full s) ∧ n = S.sum}.HasDensity 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/940.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/940.lean#L42).

## `Erdos940.erdos_940.variants.two`

Solved: stated here without proof.

> The set of integers which are the sum of at most two $2$-powerful numbers has density $0$.
>
> Erdős called this 'easy'. Baker and Brüdern [BaBr94] gave the first proof in the literature.

```lean
theorem erdos_940.variants.two :
    {n : ℕ | ∃ (S : Multiset ℕ),
      S.card ≤ 2 ∧ (∀ s ∈ S, (2).Full s) ∧ n = S.sum}.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/940.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/940.lean#L53).

## `Erdos940.erdos_940.variants.three_cubes`

Open: stated without proof.

> Is it true that the set of integers which are the sum of at most three cubes has density $0$?
>
> The cubes are those of non-negative integers, which is what `Multiset ℕ` gives. This choice
> decides the question: over `ℤ` a sum of three cubes is conjectured to represent every integer
> that is not $\pm 4 \bmod 9$, which is density $7/9$.

```lean
theorem erdos_940.variants.three_cubes :
    {n : ℕ | ∃ (S : Multiset ℕ), S.card ≤ 3 ∧ n = (Multiset.map (· ^ 3) S).sum}.HasDensity 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/940.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/940.lean#L66).

## `Erdos940.erdos_940.variants.large_integers`

Open: stated without proof.

> Let $r \ge 3$. Are there infinitely many integers which are not the sum of at most $r$-many
> $r$-powerful numbers?

```lean
theorem erdos_940.variants.large_integers :
    ∀ r ≥ 3, ¬ (∀ᶠ x in atTop, ∃ (S : Multiset ℕ), S.card ≤ r ∧ (∀ s ∈ S, r.Full s) ∧ x = S.sum)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/940.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/940.lean#L76).

## `Erdos940.erdos_940.variants.three_powerful`

Solved: stated here without proof.

> Heath-Brown [He88] has proved that all large numbers are the sum of at most three
> $2$-powerful numbers.
>
> This is the case $r = 2$ of `Erdos1107.erdos_1107`, which asks the same question with $r + 1$
> summands, and it is stated there as `Erdos1107.erdos_1107.variants.two`.

```lean
theorem erdos_940.variants.three_powerful :
    ∀ᶠ x in atTop, ∃ (S : Multiset ℕ), S.card ≤ 3 ∧ (∀ s ∈ S, (2).Full s) ∧ x = S.sum
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/940.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/940.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/940.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/940.lean)
- [erdosproblems.com/940](https://www.erdosproblems.com/940)
