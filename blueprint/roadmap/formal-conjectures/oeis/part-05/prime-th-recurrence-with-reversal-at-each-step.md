---
declaration: theorem
origin: cited
lean: OeisA100475.conjecture_with_zero, OeisA100475.conjecture
statement: formalized
---

# Prime-th recurrence with reversal at each step

> $$a(n) = \operatorname{reversal}(p_{a(n-1)})$$
>
> with $a(0)=1$, where $p_k$ is the $k$-th prime number.
>
> *References:*
> - [A100475](https://oeis.org/A100475)

*Quoted from [FormalConjectures/OEIS/100475.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/100475.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 5 test statements and 2 API statements, counted here but not shown.

## `OeisA100475.conjecture_with_zero`

Proved here.

> If zero is admitted as a starting value, then a start other than $1$ does go into a loop: the
> sequence starting at zero is constant. This records the degenerate answer created by totalizing
> the one-based prime recurrence at index zero.

```lean
theorem conjecture_with_zero :
    ∃ x : ℕ, x ≠ 1 ∧ IsUltimatelyPeriodic (aStartAt x)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100475.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/100475.lean#L113).

## `OeisA100475.conjecture`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-11-000001](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-11-000001).

> Starting at a positive value other than $a(0) = 1$, does this sequence ever go into a loop?
>
> The positivity hypothesis is required because the source recurrence uses the one-based prime index
> `p₁ = 2`; the `x = 0` branch above is only an artifact of making `aStartAt` total on `ℕ`.
>
> The answer is no: no positive start, $1$ included, ever enters a loop, so the statement is the
> negation of the question. The number of decimal digits never decreases along an orbit (as $p_y > y$
> and a prime never ends in the digit $0$), which bounds the elements of a cycle by prime counts. A
> finite check of the starts below $1230$ and the bound "fewer than $10^{D-1}$ primes below $10^D$"
> for $D \geq 5$ (Legendre's sieve for $D = 5, \dots, 8$, Chebyshev's $\theta(x) \leq x \log 4$ for
> $D \geq 9$) then exclude every cycle.

```lean
theorem conjecture :
    ¬ ∃ x : ℕ, 0 < x ∧ x ≠ 1 ∧ IsUltimatelyPeriodic (aStartAt x)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100475.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/100475.lean#L134).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/100475.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/OEIS/100475.lean)
- [A100475](https://oeis.org/A100475)
