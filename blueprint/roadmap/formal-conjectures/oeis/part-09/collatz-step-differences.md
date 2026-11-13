---
declaration: theorem
origin: cited
lean: OeisA153330.conjecture1, OeisA153330.conjecture2, OeisA153330.conjecture3, OeisA153330.conjecture4
statement: formalized
---

# Collatz step differences

> Differences in adjacent elements of the sequence quantifying the steps needed for $n$ to
> converge to 1 in the Collatz Conjecture.
>
> $$a(n) = \mathrm{A006577}(n+1) - \mathrm{A006577}(n)$$
>
> for $n > 0$.
>
> *References:*
> - [A153330](https://oeis.org/A153330)

*Quoted from [FormalConjectures/OEIS/153330.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/153330.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 5 test statements, counted here but not shown.

## `OeisA153330.conjecture1`

Open: stated without proof.

> Conjecture 1: More than half of the terms are 0.
> - _Ya-Ping Lu_, May 04 2024

```lean
theorem conjecture1 :
    1 / 2 < Filter.atTop.liminf (fun n : ℕ ↦
      (((Finset.Icc 1 n).filter (fun i ↦ a i = some 0)).card : ℝ) / (n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/153330.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/153330.lean#L145).

## `OeisA153330.conjecture2`

Open: stated without proof.

> Conjecture 2: 1, 6 and 16 appear only once and 3 appears twice in the sequence,
> i.e., $a(1) = 1$, $a(2) = 6$, $a(4) = a(5) = 3$, and $a(8) = 16$.
> - _Ya-Ping Lu_, May 04 2024

```lean
theorem conjecture2 :
    indices 1 = {1} ∧
    indices 6 = {2} ∧
    indices 16 = {8} ∧
    indices 3 = {4, 5}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/153330.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/153330.lean#L156).

## `OeisA153330.conjecture3`

Open: stated without proof.

> Conjecture 3 (Ya-Ping Lu, 2024):
> Except 1, 3 and 6, the absolute value of all terms can be written as $5x + 8y$ for $x, y \in \mathbb{N}$.
> (Note: in the OEIS comment, "x and y are integers" means $x$ and $y$ have the same sign,
> i.e., $|v| = 5x + 8y$ with $x, y \ge 0$, since every integer is a $\mathbb{Z}$-linear combination of 5 and 8).

```lean
theorem conjecture3 (n : ℕ) (v : ℤ) (hn : 0 < n) (ha : a n = some v)
    (hv : v ≠ 1 ∧ v ≠ 3 ∧ v ≠ 6) :
    ∃ x y : ℕ, v.natAbs = 5 * x + 8 * y
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/153330.lean, line 170](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/153330.lean#L170).

## `OeisA153330.conjecture4`

Open: stated without proof.

> Conjecture 4 (Ya-Ping Lu, 2024):
> For an $m$ that appears in the sequence, the ratio of the number of terms with value $m$ to that
> of $-m$ approaches 1 as $n \to \infty$, for any $|m| \notin \{1, 3, 6, 16\}$.

```lean
theorem conjecture4 (m : ℤ) (hm : m.natAbs ∉ ({1, 3, 6, 16} : Finset ℕ))
    (hocc : ∃ n, 0 < n ∧ a n = some m) :
    Filter.atTop.Tendsto
      (fun n : ℕ ↦
        (((Finset.Icc 1 n).filter (fun i ↦ a i = some m)).card : ℝ) /
        (((Finset.Icc 1 n).filter (fun i ↦ a i = some (-m))).card : ℝ))
      (nhds 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/153330.lean, line 181](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/153330.lean#L181).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/153330.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/153330.lean)
- [A153330](https://oeis.org/A153330)
