---
declaration: theorem
origin: cited
lean: OeisA236566.conjecture_1, OeisA236566.conjecture_2
statement: formalized
---

# Ordered ways to write $2n = p + q$ with $p, q$ and $p_{p+2} + 2$ all prime

> Let $p_k$ denote the $k$-th prime number. The sequence $a(n)$ counts the number of ordered ways to
> write $2n = p + q$ with $p, q$, and $p_{p+2} + 2$ all prime.
>
> *References:*
> - [A236566](https://oeis.org/A236566)

*Quoted from [FormalConjectures/OEIS/236566.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236566.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA236566.conjecture_1`

Open: stated without proof.

> Conjecture: (i) $a(n) > 0$ for all $n > 2$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 2 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/236566.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236566.lean#L86).

## `OeisA236566.conjecture_2`

Open: stated without proof.

> Conjecture: (ii) If $n > 30$, then $2n + 1$ can be written as $2p + q$ with $p$, $q$ and
> $\operatorname{prime}(p + 2) + 2$ all prime.

```lean
theorem conjecture_2 (n : ℕ) (hn : 30 < n) :
    ∃ p q : ℕ, p.Prime ∧ q.Prime ∧ (Nat.nth Nat.Prime (p + 1) + 2).Prime ∧
      2 * n + 1 = 2 * p + q
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/236566.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236566.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/236566.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/236566.lean)
- [A236566](https://oeis.org/A236566)
