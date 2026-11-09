---
declaration: theorem
origin: cited
lean: Erdos727.erdos_727, Erdos727.erdos_727.variants.k_2, Erdos727.erdos_727.variants.k_1, Erdos727.erdos_727.variants.k_1_2
statement: formalized
---

# Erdős Problem 727

> *Reference:* [erdosproblems.com/727](https://www.erdosproblems.com/727)

*Quoted from [FormalConjectures/ErdosProblems/727.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/727.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/727](https://www.erdosproblems.com/727).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos727.erdos_727`

Open: stated without proof.

> Let $k ≥ 2$. Does $((n+k)!)^2∣(2n)!$ hold for infinitely many $n$?

```lean
theorem erdos_727 : ∀ k ≥ 2,
    Set.Infinite {n : ℕ | (Nat.factorial (n + k)) ^ 2 ∣ Nat.factorial (2 * n)}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/727.lean, line 36](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/727.lean#L36).

## `Erdos727.erdos_727.variants.k_2`

Open: stated without proof.

> It is open even for $k = 2$.
> Let $k = 2$. Does $((n+k)!)^2∣(2n)!$ hold for infinitely many n?

```lean
theorem erdos_727.variants.k_2 :
    letI k := 2
    Set.Infinite {n : ℕ | (Nat.factorial (n + k)) ^ 2 ∣ Nat.factorial (2 * n)}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/727.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/727.lean#L45).

## `Erdos727.erdos_727.variants.k_1`

Solved: stated here without proof.

> Balakran proved this holds for $k = 1$.
>
> Let $k = 1$. Does $((n+k)!)^2∣(2n)!$ for infinitely many $n$?

```lean
theorem erdos_727.variants.k_1 :
    letI k := 1
    Set.Infinite {n : ℕ | (n + k)! ^ 2 ∣ (2 * n)!}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/727.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/727.lean#L56).

## `Erdos727.erdos_727.variants.k_1_2`

Solved: stated here without proof.

> Erdős, Graham, Ruzsa, and Straus observe that the method of Balakran can be further used to prove
> that there are infinitely many $n$ such that $(n+k)!(n+1)!∣(2n)!$

```lean
theorem erdos_727.variants.k_1_2 (k : ℕ) (hk : 2 ≤ k) :
    Set.Infinite {n : ℕ |
      (Nat.factorial (n + k)) * (Nat.factorial (n + 1)) ∣ Nat.factorial (2 * n)}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/727.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/727.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/727.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/727.lean)
- [erdosproblems.com/727](https://www.erdosproblems.com/727)
