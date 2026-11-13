---
declaration: theorem
origin: cited
lean: OeisA215926.conjecture_1, OeisA215926.conjecture_2
statement: formalized
---

# Smallest deficient multiplier for non-deficiency

> For $n \ge 2$, $a(n)$ is the smallest deficient number $k$ such that the product $k \cdot n$ is
> non-deficient (i.e., perfect or abundant).
>
> *References:*
> - [A215926](https://oeis.org/A215926)

*Quoted from [FormalConjectures/OEIS/215926.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/215926.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA215926.conjecture_1`

Open: stated without proof.

> Conjecture: For every $n \ge 2$, $a(n)$ is $1$, $3$, or a power of $2$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 2 ≤ n) :
    a n = 1 ∨ a n = 3 ∨ (a n).isPowerOfTwo
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/215926.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/215926.lean#L66).

## `OeisA215926.conjecture_2`

Open: stated without proof.

> Conjecture: The first occurrence of $2^m$ happens at [A014210](https://oeis.org/A014210)$(m)$.
>
> We require $m \ge 1$ because for $m = 0$, the first occurrence of $2^0 = 1$ is at $n = 6$, whereas
> $\mathrm{A014210}(0) = 2$ gives $a(2) = 3$.

```lean
theorem conjecture_2 (m : ℕ) (hm : 1 ≤ m) :
    IsLeast {n : ℕ | 2 ≤ n ∧ a n = 2 ^ m} (nextPrimeTwoPow m)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/215926.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/215926.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/215926.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/215926.lean)
- [A215926](https://oeis.org/A215926)
