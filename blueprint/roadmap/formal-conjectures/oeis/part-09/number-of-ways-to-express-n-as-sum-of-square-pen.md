---
declaration: theorem
origin: cited
lean: OeisA160324.conjecture1, OeisA160324.conjecture2, OeisA160324.conjecture3, OeisA160324.conjecture4, OeisA160324.conjecture5
statement: formalized
---

# Number of ways to express $n$ as sum of square, pentagonal, and hexagonal numbers

> $$a(n) = |\{(x, y, z) \in \mathbb{N}^3 : x^2 + p_5(y) + p_6(z) = n\}|$$
>
> *References:*
> - [A160324](https://oeis.org/A160324)

*Quoted from [FormalConjectures/OEIS/160324.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/160324.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 4 test statements, counted here but not shown.

## `OeisA160324.conjecture1`

Open: stated without proof.

> In April 2009, _Zhi-Wei Sun_ conjectured that $a(n) > 0$ for every $n = 0, 1, 2, 3, \dots$.

```lean
theorem conjecture1 (n : ℕ) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/160324.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/160324.lean#L70).

## `OeisA160324.conjecture2`

Open: stated without proof.

> For each integer $m > 2$, any natural number $n$ can be written in the form
> $p_{m+1}(x_1) + \cdots + p_{2m}(x_m)$ with $x_1, \dots, x_m$ nonnegative integers, where
> $p_k(x) = (k-2)x(x-1)/2 + x$ ($x=0,1,2,\dots$) are $k$-gonal numbers.
> - _Zhi-Wei Sun_, Aug 15 2009

```lean
theorem conjecture2 (m : ℕ) (hm : m > 2) (n : ℕ) :
    ∃ x : Fin m → ℕ, n = ∑ i : Fin m, polygonalNumber (m + (i : ℕ) + 1) (x i)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/160324.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/160324.lean#L80).

## `OeisA160324.conjecture3`

Open: stated without proof.

> The sequence contains every positive integer.
> - _Zhi-Wei Sun_, Sep 04 2009

```lean
theorem conjecture3 (k : ℕ) (hk : 0 < k) : ∃ n : ℕ, a n = k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/160324.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/160324.lean#L89).

## `OeisA160324.conjecture4`

Open: stated without proof.

> Conjecture (Zhi-Wei Sun, Aug 21 2009):
> For any integer $m > 2$, each natural number $n$ can be expressed as
> $p_{m+1}(x_1) + p_{m+2}(x_2) + p_{m+3}(x_3) + r$ with $x_1, x_2, x_3 \in \mathbb{N}$ and
> $r \in \{0, \dots, m-3\}$.

```lean
theorem conjecture4 (m : ℕ) (hm : 2 < m) (n : ℕ) :
    ∃ x1 x2 x3 r : ℕ, r ≤ m - 3 ∧
      n = polygonalNumber (m + 1) x1 + polygonalNumber (m + 2) x2 + polygonalNumber (m + 3) x3 + r
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/160324.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/160324.lean#L99).

## `OeisA160324.conjecture5`

Open: stated without proof.

> Conjecture (Zhi-Wei Sun, Aug 21 2009):
> For each integer $m > 2$, all sufficiently large integers $n$ can be expressed in the form
> $p_{m+1}(x_1) + p_{m+2}(x_2) + p_{m+3}(x_3)$ with $x_1, x_2, x_3 \in \mathbb{N}$.

```lean
theorem conjecture5 (m : ℕ) (hm : 2 < m) :
    ∀ᶠ n in Filter.atTop,
      ∃ x1 x2 x3 : ℕ, n = polygonalNumber (m + 1) x1 + polygonalNumber (m + 2) x2 + polygonalNumber (m + 3) x3
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/160324.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/160324.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/160324.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/160324.lean)
- [A160324](https://oeis.org/A160324)
