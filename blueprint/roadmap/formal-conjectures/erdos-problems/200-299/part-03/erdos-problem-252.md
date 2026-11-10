---
declaration: theorem
origin: cited
lean: Erdos252.erdos_252, Erdos252.erdos_252.variants.k_eq_zero, Erdos252.erdos_252.variants.k_eq_one, Erdos252.erdos_252.variants.k_eq_two, Erdos252.erdos_252.variants.k_eq_three, Erdos252.erdos_252.variants.k_eq_four, Erdos252.erdos_252.variants.k_ge_five, Erdos252.erdos_252.variants.schinzel, Erdos252.erdos_252.variants.prime_tuples
statement: formalized
---

# Erdős Problem 252

> *References:*
>  - [erdosproblems.com/252](https://www.erdosproblems.com/252)
>  - [ErSt71] Erdös, P., and E. G. Straus. "Some number theoretic results." Pacific J. Math 36 (1971):
>     635-646.
>  - [ErSt74] Erdős, Paul, and Ernst Straus. "On the irrationality of certain series." Pacific journal
>     of mathematics 55.1 (1974): 85-92.
>  - [ErKa54] P. Erdős, M. Kac, Amer. Math. Monthly 61 (1954), Problem 4518.
>  - [ScPu06] Schlage-Puchta, J. C., The irrationality of a number theoretical series. Ramanujan J.
>     (2006), 455-460.
>  - [FLC07] Friedlander, J. B. and Luca, F. and Stoiciu, M., On the irrationality of a divisor
>     function series. Integers (2007).
>  - [Pr22] Pratt, K., The irrationality of a divisor function series of Erdős and Kac.
>     arXiv:2209.11124 (2022).

*Quoted from [FormalConjectures/ErdosProblems/252.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/252](https://www.erdosproblems.com/252).

The file states 9 research or textbook statements: 2 open and 7 solved.

## `Erdos252.erdos_252`

Open: stated without proof.

> Erdős Problem 252: irrationality of the sum for a given $k$.

```lean
theorem erdos_252 :
    ∀ k ≥ 1, Irrational (erdos_252_sum k)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L51).

## `Erdos252.erdos_252.variants.k_eq_zero`

Solved: stated here without proof.

> `∑ σ 0 n / n!` is irrational. This is proved in [ErSt71].

```lean
theorem erdos_252.variants.k_eq_zero : Irrational (erdos_252_sum 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L57).

## `Erdos252.erdos_252.variants.k_eq_one`

Solved: stated here without proof.

> `∑ σ 1 n / n!` is irrational. This is proved in [ErSt74].

```lean
theorem erdos_252.variants.k_eq_one : Irrational (erdos_252_sum 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L62).

## `Erdos252.erdos_252.variants.k_eq_two`

Solved: stated here without proof.

> `∑ σ 2 n / n!` is irrational. This is proved in [ErKa54].

```lean
theorem erdos_252.variants.k_eq_two : Irrational (erdos_252_sum 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L68).

## `Erdos252.erdos_252.variants.k_eq_three`

Solved: stated here without proof.

> `∑ σ 3 n / n!` is irrational. This is proved in [ScPu06] and [FLC07].

```lean
theorem erdos_252.variants.k_eq_three : Irrational (erdos_252_sum 3)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L73).

## `Erdos252.erdos_252.variants.k_eq_four`

Solved: stated here without proof.

> `∑ σ 4 n / n!` is irrational. This is proved in [Pr22].

```lean
theorem erdos_252.variants.k_eq_four : Irrational (erdos_252_sum 4)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L78).

## `Erdos252.erdos_252.variants.k_ge_five`

Open: stated without proof.

> For a fixed `k ≥ 5`, is `∑ σ k n / n!` irrational?.

```lean
theorem erdos_252.variants.k_ge_five :
    ∀ k ≥ 5, Irrational (erdos_252_sum k)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L83).

## `Erdos252.erdos_252.variants.schinzel`

Solved: stated here without proof.

> If Schinzel's conjecture is true, then `∑ σ k n / n!` is irrational for all `k`. This is proved
> in [ScPu06].

```lean
theorem erdos_252.variants.schinzel (hs : ∀ (fs : Finset (Polynomial ℤ)),
    (∀ f ∈ fs, BunyakovskyCondition f) → SchinzelCondition fs →
    Infinite ↑{n | ∀ f ∈ fs, Prime (Polynomial.eval (↑n) f).natAbs}) :
    ∀ k, Irrational (erdos_252_sum k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L90).

## `Erdos252.erdos_252.variants.prime_tuples`

Solved: stated here without proof.

> If the prime `k`-tuples conjecture is true, then `∑ σ k n / n!` is irrational. This is proved
> in [FLC07].

```lean
theorem erdos_252.variants.prime_tuples {k : ℕ} (hk : 4 ≤ k) (hp : ∀ (a : Fin k → ℕ+)
    (b : Fin k → ℕ) (hab : ∀ p, p.Prime → ∃ n, ¬ p ∣ ∏ i, (a i * n + b i)),
    Set.Infinite {n | ∀ i : Fin k, (a i * n + b i).Prime} ) :
    Irrational (erdos_252_sum k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/252.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/252.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/252.lean)
- [erdosproblems.com/252](https://www.erdosproblems.com/252)
