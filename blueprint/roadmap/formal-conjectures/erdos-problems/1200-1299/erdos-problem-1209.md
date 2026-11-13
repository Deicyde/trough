---
declaration: theorem
origin: cited
lean: Erdos1209.erdos_1209.parts.i, Erdos1209.erdos_1209.parts.ii, Erdos1209.erdos_1209.parts.iii.a, Erdos1209.erdos_1209.parts.iii.b, Erdos1209.erdos_1209.parts.iii.c, Erdos1209.erdos_1209.parts.iii.d
statement: formalized
---

# Erdős Problem 1209

> *References:*
> - [erdosproblems.com/429](https://www.erdosproblems.com/429)
> - [erdosproblems.com/1102](https://www.erdosproblems.com/1102)
> - [erdosproblems.com/1209](https://www.erdosproblems.com/1209)
> - [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann. Discrete Math.
>   (1980), 89-115.

*Quoted from [FormalConjectures/ErdosProblems/1209.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1209](https://www.erdosproblems.com/1209).

The file states 6 research or textbook statements: 3 open and 3 solved. It also has 5 API statements, counted here but not shown.

## `Erdos1209.erdos_1209.parts.i`

Proved here.

> Let $A=\{a_1\lt a_2\lt \cdots\}$ be a sequence of integers which tends to infinity sufficiently fast.
> If there is an $n$ such that all $n+a_k$ are primes then must there exist infinitely many such $n$?
>
> Erdős [Er80] wrote 'unless I overlook a trivial way of getting a counterexample these questions
> are quite hopeless'. There is indeed a trivial counterexample (a variant of the construction in
> [erdosproblems.com/429]): define $a_1=2$ and for $k\geq 2$ let $a_k>a_{k-1}$ be a prime such that
> $a_k+k\equiv 0\pmod{q_k}$, where $q_k$ is some prime not dividing $k$. This sequence can be made to
> grow arbitrarily fast
>
> See also [erdosproblems.com/429] and [erdosproblems.com/1102].

```lean
theorem erdos_1209.parts.i :
    ¬ ∃ f : ℕ → ℕ, ∀ a : ℕ → ℕ, StrictMono a → (∀ k, f k ≤ a k) →
      (∃ n, ∀ k, (n + a k).Prime) →
      {n | ∀ k, (n + a k).Prime}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1209.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean#L89).

## `Erdos1209.erdos_1209.parts.ii`

Proved here.

> What if we ask for $n+a_k$ to be squarefree instead of prime?
>
> A similar construction provides a counterexample to the squarefree question.

```lean
theorem erdos_1209.parts.ii :
    ¬ ∃ f : ℕ → ℕ, ∀ a : ℕ → ℕ, StrictMono a → (∀ k, f k ≤ a k) →
      (∃ n, ∀ k, Squarefree (n + a k)) →
      {n | ∀ k, Squarefree (n + a k)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1209.lean, line 157](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean#L157).

## `Erdos1209.erdos_1209.parts.iii.a`

Solved: stated here; a Lean proof is at [https://github.com/ebarschkis/ErdosProblem/blob/main/Problem1209/Formalization.lean](https://github.com/ebarschkis/ErdosProblem/blob/main/Problem1209/Formalization.lean).

> Are there $n$ such that $n+2^{2^k}$ is always a prime?
>
> ebarschkis and GPT have proved that there are no $n$ such that $n+2^{2^k}$ is always prime: let
> $n\geq 3$ be any odd integer. If $k$ is chosen sufficiently large, and $p=n+2^{2^{k}}$ is prime,
> then the multiplicative order of $2^{2^k}\pmod{p}$, say $m$ is odd, and hence if $l$ is chosen such
> that $2^l\equiv 1\pmod{m}$ then $p\mid n+2^{2^{k+rl}}$ for all $r\geq 1$.
>
> This was formalized in Lean by Barschkis using ChatGPT.

```lean
theorem erdos_1209.parts.iii.a :
    ¬ ∃ n : ℕ, ∀ k : ℕ, (n + 2 ^ (2 ^ k)).Prime
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1209.lean, line 197](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean#L197).

## `Erdos1209.erdos_1209.parts.iii.b`

Open: stated without proof.

> Are there $n$ such that $n+2^{2^k}$ is always squarefree?

```lean
theorem erdos_1209.parts.iii.b :
    ∃ n : ℕ, ∀ k : ℕ, Squarefree (n + 2 ^ (2 ^ k))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1209.lean, line 205](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean#L205).

## `Erdos1209.erdos_1209.parts.iii.c`

Open: stated without proof.

> Are there $n$ such that $n+2^{2^k}$ is infinitely often a prime?

```lean
theorem erdos_1209.parts.iii.c :
    ∃ n : ℕ, {k | (n + 2 ^ (2 ^ k)).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1209.lean, line 213](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean#L213).

## `Erdos1209.erdos_1209.parts.iii.d`

Open: stated without proof.

> Are there $n$ such that $n+2^{2^k}$ is infinitely often squarefree?

```lean
theorem erdos_1209.parts.iii.d :
    ∃ n : ℕ, {k | Squarefree (n + 2 ^ (2 ^ k))}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1209.lean, line 221](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean#L221).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1209.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1209.lean)
- [erdosproblems.com/1209](https://www.erdosproblems.com/1209)
