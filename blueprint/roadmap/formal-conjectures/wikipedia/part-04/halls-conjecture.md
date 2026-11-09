---
declaration: theorem
origin: cited
lean: Hall.hall_conjecture, Hall.danilov, Hall.weak_hall_conjecture
statement: formalized
---

# Hall's conjecture

> There exists a positive number $C$ such that for any integer $x, y$ with $y^2 \ne x^3$,
> $|y^2 - x^3| > C \sqrt{|x|}$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Hall%27s_conjecture)
> - L. Danilov, *The Diophantine equation $x^3 - y^2 = k$ and Hall's conjecture*, Mathematical notes of the Academy of Sciences of the USSR 32 (1982): 617-618

*Quoted from [FormalConjectures/Wikipedia/Hall.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hall.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Hall.hall_conjecture`

Open: stated without proof.

> Original Hall's conjecture with exponent $1/2$.

```lean
theorem hall_conjecture : HallConjectureExp 2⁻¹
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Hall.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hall.lean#L47).

## `Hall.danilov`

Solved: stated here without proof.

> Danilov proved that one cannot replace the exponent $1/2$ with larger number.
> In other words, for any $\delta > 0$, there is no positive constant $C$ such that
> $|y^2 - x^3| > C |x| ^ {1/2 + \delta}$ for all integers $x, y$ with $y^2 \ne x^3$.

```lean
theorem danilov (δ : ℝ) (h : δ > 0) : ¬ HallConjectureExp (2⁻¹ + δ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Hall.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hall.lean#L77).

## `Hall.weak_hall_conjecture`

Open: stated without proof.

> Weak form of Hall's conjecture: relax the exponent from $1/2$ to $1/2 - \varepsilon$.

```lean
theorem weak_hall_conjecture (ε : ℝ) (hε : ε > 0) : HallConjectureExp (2⁻¹ - ε)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Hall.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hall.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Hall.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Hall.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Hall%27s_conjecture)
