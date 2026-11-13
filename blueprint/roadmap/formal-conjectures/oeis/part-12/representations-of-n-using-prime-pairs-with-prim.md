---
declaration: theorem
origin: cited
lean: OeisA219055.conjecture_1, OeisA219055.conjecture_2
statement: formalized
---

# Representations of $n$ using prime pairs with prime gaps of $6$

> Number of ways to write $n = p + q(3 - (-1)^n)/2$ with $p > q$ and $p, q, p - 6, q + 6$ all prime.
>
> *References:*
> - [A219055](https://oeis.org/A219055)

*Quoted from [FormalConjectures/OEIS/219055.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/219055.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA219055.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all even $n > 8012$ and odd $n > 15727$.

```lean
theorem conjecture_1 (n : ℕ) (hn : (Even n ∧ 8012 < n) ∨ (Odd n ∧ 15727 < n)) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219055.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/219055.lean#L63).

## `OeisA219055.conjecture_2`

Open: stated without proof.

> Conjecture: For any two multiples $d_1$ and $d_2$ of
> $6$, all sufficiently large integers $n$ can be written as $p + q(3 - (-1)^n)/2$ with $p > q$ and
> $p, q, p - d_1, q + d_2$ all prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (d₁ d₂ : ℤ) (hd₁ : 6 ∣ d₁) (hd₂ : 6 ∣ d₂) :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
      ∃ p q p' q' : ℕ, q < p ∧ p.Prime ∧ q.Prime ∧ p'.Prime ∧ q'.Prime ∧
        (p : ℤ) - d₁ = p' ∧ (q : ℤ) + d₂ = q' ∧ n = p + (1 + n % 2) * q
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/219055.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/219055.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/219055.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/219055.lean)
- [A219055](https://oeis.org/A219055)
