---
declaration: theorem
origin: cited
lean: OeisA135508.conjecture
statement: formalized
---

# Recurrence involving LCM: $a(n) = x(n+1)/x(n) - 2$

> $a(n) = x(n+1)/x(n) - 2$ where $x(1)=1$ and $x(n) = 2 x(n-1) + \operatorname{lcm}(x(n-1),n)$
> for $n > 1$.
>
> *References:*
> - [A135508](https://oeis.org/A135508)

*Quoted from [FormalConjectures/OEIS/135508.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/135508.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA135508.conjecture`

Open: stated without proof.

> Conjecture: For prime $p$ such that $p-2$ is not a prime, $a(p-1) = p$.
> - _Bill McEachen_, Sep 26 2025

```lean
theorem conjecture (p : ℕ) (hp : p.Prime) (hp_twin : ¬ (p - 2).Prime) : a (p - 1) = p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/135508.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/135508.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/135508.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/135508.lean)
- [A135508](https://oeis.org/A135508)
