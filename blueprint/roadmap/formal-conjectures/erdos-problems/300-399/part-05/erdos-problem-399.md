---
declaration: theorem
origin: cited
lean: Erdos399.erdos_399, Erdos399.erdos_399.variants.erdos_oblath, Erdos399.erdos_399.variants.pollack_shapiro, Erdos399.erdos_399.variants.cambie, Erdos399.erdos_399.variants.sum_two_squares
statement: formalized
---

# Erdős Problem 399

> Is it true that there are no solutions to $n! = x^k \pm y^k$ with $x,y,n \in \mathbb{N}$,
> with $xy > 1$ and $k > 2$?
>
> *References:*
>  - [erdosproblems.com/399](https://www.erdosproblems.com/399)
> - [Br32] Breusch, Robert, Zur Verallgemeinerung des Bertrandschen Postulates, da\ss zwischen $x$
>   und 2 $x$ stets Primzahlen liegen. Math. Z. (1932), 505--526.
> - [ErOb37] Erdős, P. and Obláth, R., \"Über diophantische Gleichungen der Form $n!=x^p+y^p$ und
>   $n!\pmd m!=x^p$. Acta Litt. ac Sci. Reg. Univ. Hung. Fr.-Jos., Sect. Sci. Math. (1937), 241-255.
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
> - [PoSh73] Pollack, Richard M. and Shapiro, Harold N., The next to last case of a factorial
>   diophantine equation. Comm. Pure Appl. Math. (1973), 313-325.

*Quoted from [FormalConjectures/ErdosProblems/399.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/399.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/399](https://www.erdosproblems.com/399).

The file states 5 research or textbook statements: 5 solved.

## `Erdos399.erdos_399`

Proved here.

> Is it true that there are no solutions to `n! = x^k ± y^k` with `x,y,n ∈ ℕ`, `x*y > 1`, and
> `k > 2`?
>
> The answer is no: Jonas Barfield found the counterexample `10! = 48^4 - 36^4` (equivalently,
> `10! + 36^4 = 48^4`).
>
> This is discussed in problem D2 of Guy's collection [Gu04].
>
> This was formalized in Lean by Lu using Codex.

```lean
theorem erdos_399 :
    ∃ (n x y k : ℕ), 1 < x * y ∧ 2 < k ∧ (n ! = x ^ k + y ^ k ∨ n ! + y ^ k = x ^ k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/399.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/399.lean#L55).

## `Erdos399.erdos_399.variants.erdos_oblath`

Solved: stated here without proof.

> Erdős and Obláth [ErOb37] proved this is true when $(x,y)=1$ and $k\neq 4$.

```lean
theorem erdos_399.variants.erdos_oblath {n x y k : ℕ} :
    x.Coprime y → 1 < x * y → 2 < k → k ≠ 4 →
      n ! ≠ x ^ k + y ^ k ∧ n ! + y ^ k ≠ x ^ k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/399.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/399.lean#L61).

## `Erdos399.erdos_399.variants.pollack_shapiro`

Solved: stated here without proof.

> Pollack and Shapiro [PoSh73] proved there are no solutions to $n!=x^4-1$.

```lean
theorem erdos_399.variants.pollack_shapiro (n x : ℕ) : n ! + 1 ≠ x ^ 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/399.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/399.lean#L68).

## `Erdos399.erdos_399.variants.cambie`

Proved here.

> Cambie has also observed that considerations modulo $8$ rule out any solutions to $n!=x^4+y^4$ with
> $(x,y)=1$ and $xy>1$.

```lean
theorem erdos_399.variants.cambie {n x y : ℕ} :
    x.Coprime y → 1 < x * y → n ! ≠ x ^ 4 + y ^ 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/399.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/399.lean#L76).

## `Erdos399.erdos_399.variants.sum_two_squares`

Solved: stated here without proof.

> Erdős and Obláth observed that the Bertrand-style fact (first proved by Breusch [Br32]) that, if
> $q_i$ is the sequence of primes congruent to $3\pmod{4}$ then $q_{i+1}<2q_i$ except for $q_1=3$,
> together with Fermat's theorem on the sums of two squares implies that the only solution to
> $n!=x^2+y^2$ is $6!=12^2+24^2$.

```lean
theorem erdos_399.variants.sum_two_squares :
    ∀ {n x y : ℕ}, 1 < x * y → n ! = x ^ 2 + y ^ 2 →
      n = 6 ∧ (x = 12 ∧ y = 24 ∨ x = 24 ∧ y = 12)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/399.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/399.lean#L130).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/399.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/399.lean)
- [erdosproblems.com/399](https://www.erdosproblems.com/399)
