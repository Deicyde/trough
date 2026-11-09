---
declaration: theorem
origin: cited
lean: Erdos11.erdos_11, Erdos11.erdos_11.variants.all_odd, Erdos11.erdos_11.variants.not_four_dvd, Erdos11.erdos_11.variants.two_pow_two, Erdos11.erdos_11.variants.finite_bound1, Erdos11.erdos_11.variants.finite_bound2, Erdos11.erdos_11.variants.granville_soundararajan
statement: formalized
---

# Erdős Problem 11

> *Reference:* [erdosproblems.com/11](https://www.erdosproblems.com/11)

*Quoted from [FormalConjectures/ErdosProblems/11.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/11](https://www.erdosproblems.com/11).

The file states 7 research or textbook statements: 4 open and 3 solved. It also has 1 test statement, counted here but not shown.

## `Erdos11.erdos_11`

Open: stated without proof.

> Is every large odd integer $n$ the sum of a squarefree number and a power of 2?

```lean
theorem erdos_11 :
    ∀ᶠ n : ℕ in atTop, Odd n → ∃ k l : ℕ, Squarefree k ∧ n = k + 2 ^ l
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/11.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean#L36).

## `Erdos11.erdos_11.variants.all_odd`

Open: stated without proof.

> Every odd $n > 1$ is the sum of a squarefree number and a power of 2. This is the form in
> earlier versions of erdosproblems.com/11 and the hypothesis of [GrSo98]. It is stronger than
> `erdos_11`, which asks only about large $n$: a single exception would refute it.

```lean
theorem erdos_11.variants.all_odd (n : ℕ) (hn : Odd n) (hn' : 1 < n) :
    ∃ k l : ℕ, Squarefree k ∧ n = k + 2 ^ l
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/11.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean#L46).

## `Erdos11.erdos_11.variants.not_four_dvd`

Open: stated without proof.

> Erdős often asked this under the weaker assumption that $n > 1$
> is not divisible by 4.

```lean
theorem erdos_11.variants.not_four_dvd (n : ℕ) (hn : ¬ 4 ∣ n) (hn' : 1 < n) :
    ∃ k l : ℕ , Squarefree k ∧ n = k + 2^l
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/11.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean#L61).

## `Erdos11.erdos_11.variants.two_pow_two`

Open: stated without proof.

> Is every odd $n > 1$ the sum of a squarefree number and two powers of 2?

```lean
theorem erdos_11.variants.two_pow_two (n : ℕ) (hn : Odd n) (hn' : 1 < n) :
    ∃ k l m : ℕ , Squarefree k ∧ n = k + 2^l + 2^m
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/11.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean#L69).

## `Erdos11.erdos_11.variants.finite_bound1`

Solved: stated here without proof.

> Every odd $1 < n < 10^7$ is the sum of a squarefree number and a power of 2.

```lean
theorem erdos_11.variants.finite_bound1 (n : ℕ) (hn : Odd n) (h : n < 10^7) (hn' : 1 < n) :
    ∃ k l : ℕ , Squarefree k ∧ n = k + 2^l
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/11.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean#L77).

## `Erdos11.erdos_11.variants.finite_bound2`

Solved: stated here without proof.

> Every odd $1 < n < 2^50$ is the sum of a squarefree number and a power of 2.

```lean
theorem erdos_11.variants.finite_bound2 (n : ℕ) (hn : Odd n) (h : n < 2^50) (hn' : 1 < n) :
    ∃ k l : ℕ , Squarefree k ∧ n = k + 2^l
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/11.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean#L85).

## `Erdos11.erdos_11.variants.granville_soundararajan`

Solved: stated here without proof.

> Suppose that every odd $n > 1$ is the sum of a squarefree number and a power of 2. Then the set of
> primes $p$ such that $2^p \not\equiv 2 \pmod{p^2}$ (the non-Wieferich primes) is infinite.
> This follows from Theorem 1 in [GrSo98].
> [GrSo98] Granville, A. and Soundararajan, K., A Binary Additive Problem of Erdős and the Order of $2$ mod $p^2$. The Ramanujan Journal (1998), 283-298.

```lean
theorem erdos_11.variants.granville_soundararajan (H : type_of% erdos_11.variants.all_odd) :
    {p : ℕ | p.Prime ∧ ¬ 2 ^ p ≡ 2 [MOD p ^ 2]}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/11.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/11.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/11.lean)
- [erdosproblems.com/11](https://www.erdosproblems.com/11)
