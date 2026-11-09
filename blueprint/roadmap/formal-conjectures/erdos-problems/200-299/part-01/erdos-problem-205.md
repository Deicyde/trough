---
declaration: theorem
origin: cited
lean: Erdos205.erdos_205.parts.i, Erdos205.erdos_205.parts.ii, Erdos205.erdos_205.parts.iii, Erdos205.erdos_205.variants.many_prime_factors, Erdos205.erdos_205.variants.odd_counterexamples
statement: formalized
---

# Erdős Problem 205

> *References:*
> - [erdosproblems.com/205](https://www.erdosproblems.com/205)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115.
> - [Ro34] Romanoff, N. P., *Über einige Sätze der additiven Zahlentheorie*. Math. Ann. (1934),
>   668-678.

*Quoted from [FormalConjectures/ErdosProblems/205.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/205.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/205](https://www.erdosproblems.com/205).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos205.erdos_205.parts.i`

Solved: stated here without proof.

> Is it true that all sufficiently large $n$ can be written as $2^k+m$ for some $k\geq 0$, where
> $\Omega(m)\lt \log\log m$? (Here $\Omega(m)$ is the number of prime divisors of $m$ counted with
> multiplicity.)
>
> Barreto and Leeham, using ChatGPT and Aristotle, have proved a negative answer, which was
> quantified by Tao and Alexeev (see the comments): in fact there are infinitely many $n$ such that,
> for all $k$ with $2^k\lt n$, $n-2^k$ has at least
> $$\gg \left(\frac{\log n}{\log\log n}\right)^{1/2}$$
> many prime factors.

```lean
theorem erdos_205.parts.i :
    ¬ ∀ᶠ n : ℕ in atTop, IsRepresentable (fun m => Real.log (Real.log m)) n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/205.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/205.lean#L58).

## `Erdos205.erdos_205.parts.ii`

Solved: stated here without proof.

> Is it true that all sufficiently large $n$ can be written as $2^k+m$ for some $k\geq 0$, where
> $\Omega(m)\lt \log\log m$? (Here $\Omega(m)$ is the number of prime divisors of $m$ counted with
> multiplicity.) What about $\lt \epsilon \log\log m$?
>
> Barreto and Leeham, using ChatGPT and Aristotle, have proved a negative answer, which was
> quantified by Tao and Alexeev (see the comments).

```lean
theorem erdos_205.parts.ii :
    ¬ ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      IsRepresentable (fun m => ε * Real.log (Real.log m)) n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/205.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/205.lean#L71).

## `Erdos205.erdos_205.parts.iii`

Solved: stated here without proof.

> Is it true that all sufficiently large $n$ can be written as $2^k+m$ for some $k\geq 0$, where
> $\Omega(m)\lt \log\log m$? (Here $\Omega(m)$ is the number of prime divisors of $m$ counted with
> multiplicity.) Or some more slowly growing function?
>
> Barreto and Leeham, using ChatGPT and Aristotle, have proved a negative answer, which was
> quantified by Tao and Alexeev (see the comments).

```lean
theorem erdos_205.parts.iii :
    ¬ ∃ f : ℕ → ℝ, f =o[atTop] (fun m : ℕ => Real.log (Real.log m)) ∧
      ∀ᶠ n : ℕ in atTop, IsRepresentable f n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/205.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/205.lean#L85).

## `Erdos205.erdos_205.variants.many_prime_factors`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos205.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos205.lean).

> In fact there are infinitely many $n$ such that, for all $k$ with $2^k\lt n$, $n-2^k$ has at least
> $$\gg \left(\frac{\log n}{\log\log n}\right)^{1/2}$$
> many prime factors.

```lean
theorem erdos_205.variants.many_prime_factors : ∃ c > (0 : ℝ),
    {n : ℕ | ∀ k : ℕ, 2 ^ k < n →
      c * Real.sqrt (Real.log n / Real.log (Real.log n)) ≤ (Ω (n - 2 ^ k) : ℝ)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/205.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/205.lean#L97).

## `Erdos205.erdos_205.variants.odd_counterexamples`

Open: stated without proof.

> The $n$ constructed in this way are divisible by a large power of $2$. It remains open whether
> there exist arbitrarily large odd counterexamples.

```lean
theorem erdos_205.variants.odd_counterexamples :
    {n : ℕ | Odd n ∧ ¬ IsRepresentable (fun m => Real.log (Real.log m)) n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/205.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/205.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/205.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/205.lean)
- [erdosproblems.com/205](https://www.erdosproblems.com/205)
