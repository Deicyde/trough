---
declaration: theorem
origin: cited
lean: HardyLittlewood.first_hardy_littlewood_conjecture, HardyLittlewood.second_hardy_littlewood_conjecture, HardyLittlewood.not_first_and_secondHardyLittlewoodConjecture
statement: formalized
---

# First Hardy–Littlewood conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/First_Hardy%E2%80%93Littlewood_conjecture)

*Quoted from [FormalConjectures/Wikipedia/HardyLittlewood.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HardyLittlewood.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved.

## `HardyLittlewood.first_hardy_littlewood_conjecture`

Open: stated without proof.

> Let $P = (m_1, \dots, m_k)$ be a tuple of distinct positive even integers. Let
> $\pi_P(n)$ denote the number of primes $p\leq n$ such that $(p, p + m_1, \dots, p + m_k)$
> forms an admissible prime constellation. Let $w(q; m_1, \dots, m_k)$ denote the
> number of distinct residues of $0, m_1, \dots, m_k$ modulo $q$, and let
>
> $$
>   C_P = 2 ^ k\prod_{\substack{q\ \text{prime} \\ q\geq 3}}
>     \frac{1 - \frac{w(q; m_1, \dots, m_k)}{q}}{\left(1 - \frac{1}{q}\right)^{k+1}}.
> $$
>
> Then
>
> $$
>   \pi_P(n)\sim C_P\int_2^n\frac{dt}{\log^{k+1}t}.
> $$

```lean
theorem first_hardy_littlewood_conjecture {k : ℕ} (m : Fin k.succ → ℕ) :
    FirstHardyLittlewoodConjectureFor m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/HardyLittlewood.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HardyLittlewood.lean#L94).

## `HardyLittlewood.second_hardy_littlewood_conjecture`

Open: stated without proof.

> For integers $x, y \geq 2$,
>
> $$
>   \pi(x + y) \leq \pi(x) + \pi(y),
> $$
>
> where $\pi(z)$ denotes the prime-counting function, giving the number of primes up to
> and including $z$.

```lean
theorem second_hardy_littlewood_conjecture {x y : ℕ} (hx : 2 ≤ x) (hy : 2 ≤ y) :
    SecondHardyLittlewoodConjectureFor x y
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/HardyLittlewood.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HardyLittlewood.lean#L112).

## `HardyLittlewood.not_first_and_secondHardyLittlewoodConjecture`

Solved: stated here without proof.

> Richards [Ri74] showed that only one of the two Hardy-Littlewood conjectures can be true.
>
> [Ri74] Richards, Ian (1974). _On the Incompatibility of Two Conjectures Concerning Primes_. Bull. Amer. Math. Soc. 80: 419–438.

```lean
theorem not_first_and_secondHardyLittlewoodConjecture :
    (∀ {k : ℕ} (m : Fin k.succ → ℕ), FirstHardyLittlewoodConjectureFor m) →
      ¬(∀ {x y : ℕ} (hx : 2 ≤ x) (hy : 2 ≤ y), SecondHardyLittlewoodConjectureFor x y)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/HardyLittlewood.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HardyLittlewood.lean#L121).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/HardyLittlewood.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HardyLittlewood.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/First_Hardy%E2%80%93Littlewood_conjecture)
