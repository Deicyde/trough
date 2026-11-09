---
declaration: theorem
origin: cited
lean: Catalan.catalans_conjecture, Catalan.pillais_conjecture, LebesgueNagell.lebesgue_nagell
statement: formalized
---

# Catalan's conjecture and related Diophantine equations

> *References:*
> - [Wikipedia - Catalan's conjecture](https://en.wikipedia.org/wiki/Catalan%27s_conjecture)
> - [arXiv:2507.12397](https://arxiv.org/abs/2507.12397) (Lebesgue-Nagell equation)

*Quoted from [FormalConjectures/Wikipedia/Catalan.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Catalan.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `Catalan.catalans_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/cadamcat/catalan-lean4/blob/4bf1f742eb341decbdfc59ec56e1616f4d13e33b/Catalan/Final/Assembly.lean#L32](https://github.com/cadamcat/catalan-lean4/blob/4bf1f742eb341decbdfc59ec56e1616f4d13e33b/Catalan/Final/Assembly.lean#L32).

> The only natural number solution to the equation $x^a - y^b = 1$ such that $a, b > 1$ and
> $x, y > 0$ is given by $a = 2$, $b = 3$, $x = 3$, and $y = 2$.

```lean
theorem catalans_conjecture (a b x y : ℕ) (ha : 1 < a) (hb : 1 < b) (hx : 0 < x) (hy : 0 < y)
    (heq : x ^ a - y ^ b = 1) : a = 2 ∧ b = 3 ∧ x = 3 ∧ y = 2
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Catalan.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Catalan.lean#L39).

## `Catalan.pillais_conjecture`

Open: stated without proof.

> For positive integers a, b, and c, there are only finitely many positive solutions (x, y, m, n) to the
> equation $ax^n - by^m = c$ where $(m, n) \neq (2, 2)$ and $x, y > 1$.

```lean
theorem pillais_conjecture (a b c : ℕ) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    { (x, y, m, n) : (ℕ × ℕ × ℕ × ℕ) |
      1 < x ∧ 1 < y ∧ 1 < m ∧ 1 < n ∧ (m, n) ≠ (2, 2) ∧
      a * x^n - b * y^m = c }.Finite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Catalan.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Catalan.lean#L48).

## `LebesgueNagell.lebesgue_nagell`

Open: stated without proof.

> **Lebesgue-Nagell Equation Conjecture**
>
> For any odd prime $p$, the only integer solutions $(x, y)$ to the equation $x^2 - 2 = y^p$
> are $(x, y) = (\pm 1, -1)$.
>
> *Reference:* Ethan Katz and Kyle Pratt, "On the Lebesgue-Nagell equation $x^2 - 2 = y^p$",
> [arXiv:2507.12397](https://arxiv.org/abs/2507.12397)

```lean
theorem lebesgue_nagell (p : ℕ) (hp : p.Prime) (hodd : Odd p) (x y : ℤ) :
    x ^ 2 - 2 = y ^ p ↔ (x = 1 ∨ x = -1) ∧ y = -1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Catalan.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Catalan.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Catalan.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Catalan.lean)
- [Wikipedia - Catalan's conjecture](https://en.wikipedia.org/wiki/Catalan%27s_conjecture)
