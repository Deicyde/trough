---
declaration: theorem
origin: cited
lean: RiemannZetaValues.irrational_five, RiemannZetaValues.irrational_seven, RiemannZetaValues.irrational_nine, RiemannZetaValues.irrational_eleven, RiemannZetaValues.irrational_odd, RiemannZetaValues.irrational_three, RiemannZetaValues.infinite_irrational_at_odd, RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven, RiemannZetaValues.transcendental_three, RiemannZetaValues.apery_central_binomial_series
statement: formalized
---

# Particular values of the Riemann zeta function

> *References:*
> - [Wikipedia: Particular values of the Riemann zeta function](https://en.wikipedia.org/wiki/Particular_values_of_the_Riemann_zeta_function)
> - [Wikipedia: Apéry's constant](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_constant)

*Quoted from [FormalConjectures/Wikipedia/RiemannZetaValues.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 10 research or textbook statements: 5 open, 4 solved and 1 textbook result.

## `RiemannZetaValues.irrational_five`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a14b09f420e81b662b9b3e18d0b9b7ccefbdbeef/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L38](https://github.com/mo271/formal-conjectures/blob/a14b09f420e81b662b9b3e18d0b9b7ccefbdbeef/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L38); a Lean proof is at [https://github.com/mo271/Zeta5/blob/2c80b320d06b4395605edbd413649d19094507af/Apery/Main.lean#L26](https://github.com/mo271/Zeta5/blob/2c80b320d06b4395605edbd413649d19094507af/Apery/Main.lean#L26).

> $\zeta(5)$ is irrational.
>
> [Fa26] A. Fauzan (2026). [_$\zeta(5)$ is irrational_](https://zenodo.org/records/22826419).
> Preprint, 17 September 2026.

```lean
theorem irrational_five : ∃ x, Irrational x ∧ riemannZeta 5 = x
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L44).

## `RiemannZetaValues.irrational_seven`

Open: stated without proof.

> $\zeta(7)$ is irrational.

```lean
theorem irrational_seven : ∃ x, Irrational x ∧ riemannZeta 7 = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L51).

## `RiemannZetaValues.irrational_nine`

Open: stated without proof.

> $\zeta(9)$ is irrational.

```lean
theorem irrational_nine : ∃ x, Irrational x ∧ riemannZeta 9 = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L58).

## `RiemannZetaValues.irrational_eleven`

Open: stated without proof.

> $\zeta(11)$ is irrational.

```lean
theorem irrational_eleven : ∃ x, Irrational x ∧ riemannZeta 11 = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L65).

## `RiemannZetaValues.irrational_odd`

Open: stated without proof.

> $\zeta(2n + 1)$ is irrational for any $n\in\mathbb{N}^{+}$.

```lean
theorem irrational_odd (n : ℕ) (hn : 0 < n) :
    ∃ x, Irrational x ∧ riemannZeta (2 * n + 1) = x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L72).

## `RiemannZetaValues.irrational_three`

Solved: stated here without proof.

> $\zeta(3)$ is irrational.
>
> [Ap79] Apéry, R. (1979). _Irrationalité de ζ(2) et ζ(3)_. Astérisque. 61: 11–13.

```lean
theorem irrational_three : ∃ x, Irrational x ∧ riemannZeta 3 = x
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L82).

## `RiemannZetaValues.infinite_irrational_at_odd`

Solved: stated here without proof.

> There are infinitely many $\zeta(2n + 1)$, $n \in \mathbb{N}$, that are irrational.
>
> [Ri00] Rivoal, T. (2000). _La fonction zeta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs_. Comptes Rendus de l'Académie des Sciences, Série I. 331 (4): 267–270.

```lean
theorem infinite_irrational_at_odd :
    { n : ℕ | ∃ x, Irrational x ∧ riemannZeta (2 * n + 1) = x }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L91).

## `RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven`

Solved: stated here without proof.

> At least one of $\zeta(5), \zeta(7), \zeta(9)$ or $\zeta(11)$ is irrational.
>
> [Zu01]  W. Zudilin (2001). _One of the numbers ζ(5), ζ(7), ζ(9), ζ(11) is irrational_. Russ. Math. Surv. 56 (4): 774–776.

```lean
theorem exists_irrational_of_five_seven_nine_eleven :
    {5, 7, 9, 11} ∩ { a | ∃ x, Irrational x ∧ riemannZeta a = x} |>.Nonempty
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L101).

## `RiemannZetaValues.transcendental_three`

Open: stated without proof.

> Apéry's constant $\zeta(3)$ is transcendental over $\mathbb{Q}$ (cf. `irrational_three` for
> Apéry's irrationality theorem [Ap79]).
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_constant)

```lean
theorem transcendental_three : Transcendental ℚ (riemannZeta 3)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L112).

## `RiemannZetaValues.apery_central_binomial_series`

Textbook result, stated without proof.

> Markov–Hjortnaes–Apéry central-binomial series identity [Ma1890, Hj53, Ap79]:
>
> $$\zeta(3) = \frac{5}{2} \sum_{n=0}^{\infty} \frac{(-1)^n}{(n + 1)^3 \binom{2(n + 1)}{n + 1}}.$$
>
> - [Ma1890] A. A. Markov (1890), Mém. Acad. Imp. Sci. St.-Pétersbourg (7) **37**, no. 9, 18 pp.
> - [Hj53] M. M. Hjortnaes (1953), Proc. 12th Scand. Math. Congr. (Lund), 211–213.
> - [Ap79] R. Apéry (1979), _Irrationalité de ζ(2) et ζ(3)_, Astérisque **61**, 11–13.

```lean
theorem apery_central_binomial_series :
    riemannZeta 3 =
      (5 / 2 : ℂ) * ∑' n : ℕ,
        (-1 : ℂ) ^ n / (((n : ℂ) + 1) ^ 3 * (Nat.centralBinom (n + 1) : ℂ))
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/RiemannZetaValues.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RiemannZetaValues.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/RiemannZetaValues.lean)
- [Wikipedia: Particular values of the Riemann zeta function](https://en.wikipedia.org/wiki/Particular_values_of_the_Riemann_zeta_function)
