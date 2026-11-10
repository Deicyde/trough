---
declaration: theorem
origin: cited
lean: RiemannZetaValues.irrational_five, RiemannZetaValues.irrational_seven, RiemannZetaValues.irrational_nine, RiemannZetaValues.irrational_eleven, RiemannZetaValues.irrational_odd, RiemannZetaValues.irrational_three, RiemannZetaValues.infinite_irrational_at_odd, RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven
statement: formalized
---

# Particular values of the Riemann zeta function

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Particular_values_of_the_Riemann_zeta_function)

*Quoted from [FormalConjectures/Wikipedia/RiemannZetaValues.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 4 open and 4 solved.

## `RiemannZetaValues.irrational_five`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a14b09f420e81b662b9b3e18d0b9b7ccefbdbeef/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L38](https://github.com/mo271/formal-conjectures/blob/a14b09f420e81b662b9b3e18d0b9b7ccefbdbeef/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L38); a Lean proof is at [https://github.com/mo271/Zeta5/blob/2c80b320d06b4395605edbd413649d19094507af/Apery/Main.lean#L26](https://github.com/mo271/Zeta5/blob/2c80b320d06b4395605edbd413649d19094507af/Apery/Main.lean#L26).

> $\zeta(5)$ is irrational.
>
> [Fa26] A. Fauzan (2026). [_$\zeta(5)$ is irrational_](https://zenodo.org/records/22826419).
> Preprint, 17 September 2026.

```lean
theorem irrational_five : ∃ x, Irrational x ∧ riemannZeta 5 = x
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L42).

## `RiemannZetaValues.irrational_seven`

Open: stated without proof.

> $\zeta(7)$ is irrational.

```lean
theorem irrational_seven : ∃ x, Irrational x ∧ riemannZeta 7 = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L49).

## `RiemannZetaValues.irrational_nine`

Open: stated without proof.

> $\zeta(9)$ is irrational.

```lean
theorem irrational_nine : ∃ x, Irrational x ∧ riemannZeta 9 = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L56).

## `RiemannZetaValues.irrational_eleven`

Open: stated without proof.

> $\zeta(11)$ is irrational.

```lean
theorem irrational_eleven : ∃ x, Irrational x ∧ riemannZeta 11 = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L63).

## `RiemannZetaValues.irrational_odd`

Open: stated without proof.

> $\zeta(2n + 1)$ is irrational for any $n\in\mathbb{N}^{+}$.

```lean
theorem irrational_odd (n : ℕ) (hn : 0 < n) :
    ∃ x, Irrational x ∧ riemannZeta (2 * n + 1) = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L70).

## `RiemannZetaValues.irrational_three`

Solved: stated here without proof.

> $\zeta(3)$ is irrational.
>
> [Ap79] Apéry, R. (1979). _Irrationalité de ζ(2) et ζ(3)_. Astérisque. 61: 11–13.

```lean
theorem irrational_three : ∃ x, Irrational x ∧ riemannZeta 3 = x
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L80).

## `RiemannZetaValues.infinite_irrational_at_odd`

Solved: stated here without proof.

> There are infinitely many $\zeta(2n + 1)$, $n \in \mathbb{N}$, that are irrational.
>
> [Ri00] Rivoal, T. (2000). _La fonction zeta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs_. Comptes Rendus de l'Académie des Sciences, Série I. 331 (4): 267–270.

```lean
theorem infinite_irrational_at_odd :
    { n : ℕ | ∃ x, Irrational x ∧ riemannZeta (2 * n + 1) = x }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L89).

## `RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven`

Solved: stated here without proof.

> At least one of $\zeta(5), \zeta(7), \zeta(9)$ or $\zeta(11)$ is irrational.
>
> [Zu01]  W. Zudilin (2001). _One of the numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational_. Russ. Math. Surv. 56 (4): 774–776.

```lean
theorem exists_irrational_of_five_seven_nine_eleven :
    {5, 7, 9, 11} ∩ { a | ∃ x, Irrational x ∧ riemannZeta a = x} |>.Nonempty
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RiemannZetaValues.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RiemannZetaValues.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Particular_values_of_the_Riemann_zeta_function)
