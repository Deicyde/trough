---
declaration: theorem
origin: cited
lean: Erdos977.erdos_977, Erdos977.erdos_977.variants.schinzel, Erdos977.erdos_977.variants.stewart, Erdos977.erdos_977.variants.factorial, Erdos977.erdos_977.variants.lai
statement: formalized
---

# Erdős Problem 977

> *References:*
> - [erdosproblems.com/977](https://www.erdosproblems.com/977)
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Sc62] Schinzel, A., *On primitive prime factors of $a^n-b^n$*. Proc. Cambridge Philos. Soc.
>   (1962), 555-562.
> - [St74b] Stewart, C. L., *The greatest prime factor of $a^n-b^n$*. Acta Arith. (1974/75),
>   427-433.
> - [St13] Stewart, Cameron L., *On divisors of Lucas and Lehmer numbers*. Acta Math. (2013),
>   291-314.
> - [MuWo02] Murty, Ram and Wong, Siman, *The $ABC$ conjecture and prime divisors of the Lucas and
>   Lehmer sequences*. (2002), 43-54.
> - [La21] L. Lai, *On the largest prime divisor of $n!+1$*. arXiv:2103.14894 (2021).

*Quoted from [FormalConjectures/ErdosProblems/977.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/977.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/977](https://www.erdosproblems.com/977).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos977.erdos_977`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos977.lean#L4271](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos977.lean#L4271).

> If $P(m)$ is the greatest prime divisor of $m$, then is it true that
>
> $$\frac{P(2^n-1)}{n}\to \infty$$
>
> as $n\to \infty$?
>
> Schinzel [Sc62] proved that $P(2^n-1)>2n$ for $n>12$. In [Er65b] Erdős also asks about $P(n!+1)$.
> Stewart [St74b] proved that this conjecture is true if we restrict $n$ to those integers with
> $\lt \frac{1}{\log 2}\log\log n$ many prime factors.
>
> This was proved in the affirmative by Stewart [St13], who proved that
> $P(2^n-1)\gg n^{1+\frac{1}{104\log\log n}}$ for all large $n$.

```lean
theorem erdos_977 :
    Tendsto (fun n : ℕ ↦ (Nat.maxPrimeFac (2 ^ n - 1) : ℝ) / n) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/977.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/977.lean#L59).

## `Erdos977.erdos_977.variants.schinzel`

Solved: stated here without proof.

> Schinzel [Sc62] proved that $P(2^n-1)>2n$ for $n>12$.

```lean
theorem erdos_977.variants.schinzel :
    ∀ n : ℕ, 12 < n → 2 * n < Nat.maxPrimeFac (2 ^ n - 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/977.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/977.lean#L65).

## `Erdos977.erdos_977.variants.stewart`

Solved: stated here without proof.

> Stewart [St13] proved that $P(2^n-1)\gg n^{1+\frac{1}{104\log\log n}}$ for all large $n$.

```lean
theorem erdos_977.variants.stewart : ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
    c * (n : ℝ) ^ (1 + 1 / (104 * Real.log (Real.log n))) ≤ Nat.maxPrimeFac (2 ^ n - 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/977.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/977.lean#L71).

## `Erdos977.erdos_977.variants.factorial`

Open: stated without proof.

> In [Er65b] Erdős also asks about $P(n!+1)$: is it true that $P(n!+1)/n\to\infty$? This appears to
> be open still. Murty and Wong [MuWo02] proved that $P(n!+1)>(1+o(1))n\log n$ assuming the abc
> conjecture.

```lean
theorem erdos_977.variants.factorial :
    Tendsto (fun n : ℕ ↦ (Nat.maxPrimeFac (n.factorial + 1) : ℝ) / n) atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/977.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/977.lean#L81).

## `Erdos977.erdos_977.variants.lai`

Solved: stated here without proof.

> The best-known unconditional result, due to Lai [La21], is that
>
> $$\limsup \frac{P(n!+1)}{n} \geq 1+9\log 2\approx 7.238.$$

```lean
theorem erdos_977.variants.lai : ∀ C : ℝ, C < 1 + 9 * Real.log 2 →
    ∃ᶠ n : ℕ in atTop, C * n < Nat.maxPrimeFac (n.factorial + 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/977.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/977.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/977.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/977.lean)
- [erdosproblems.com/977](https://www.erdosproblems.com/977)
