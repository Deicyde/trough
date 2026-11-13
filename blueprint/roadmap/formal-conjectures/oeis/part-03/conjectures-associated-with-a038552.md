---
declaration: theorem
origin: cited
lean: OeisA38552.starkHeegner_classNumberOne, OeisA38552.mod_24_of_isA038552, OeisA38552.isA038552_eq_largestNegFundDisc, OeisA38552.largestEven_lt_largestOdd_negFundDisc
statement: formalized
---

# Conjectures associated with A038552

> A038552 lists the largest squarefree number $k$ such that the imaginary quadratic field
> $\mathbb{Q}(\sqrt{-k})$ has class number $n$.
>
> The conjectures state that:
> 1. All terms are congruent to $19 \pmod{24}$.
> 2. This is also the largest absolute value of negative fundamental discriminant $d$ for
>    class number $n$.
> 3. For even $n$, if $k$ is the largest odd number with $h(-k) = n$ and $k'$ is the largest
>    even number with $h(-k') = n$, then $k > k'$. Here $h(D)$ is the class number of the
>    quadratic field with discriminant $D$, so $k$ and $k'$ are absolute values of negative
>    fundamental discriminants, not radicands. The source states conjecture 2 in this form.
>
> The squarefree condition in the definition is needed for the maximum to exist, since
> $\mathbb{Q}(\sqrt{-k}) = \mathbb{Q}(\sqrt{-4k})$.
>
> Conjecture 2 is not a restatement of the definition. Both maxima range over the same imaginary
> quadratic fields, but they maximize different integers attached to those fields. A038552 uses
> the squarefree radicand $k$, whereas the discriminant of $\mathbb{Q}(\sqrt{-k})$ is $-k$ for
> $k \equiv 3 \pmod 4$ and $-4k$ otherwise. The map $k \mapsto |d|$ is not monotone: it sends $2$
> to $8$ and $3$ to $3$. So conjecture 2 says that the largest term $k$ satisfies
> $k \equiv 3 \pmod 4$, and that $4k' \le k$ for every $k' \equiv 1, 2 \pmod 4$ with class
> number $n$.
>
> *References:*
> - [Sta67] Stark, Harold M. "A complete determination of the complex quadratic fields of
>   class-number one." Michigan Mathematical Journal 14.1 (1967): 1-27.
> - [oeis.org/A038552](https://oeis.org/A038552)

*Quoted from [FormalConjectures/OEIS/38552.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38552.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 3 open and 1 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `OeisA38552.starkHeegner_classNumberOne`

Solved: stated here without proof.

> The Stark-Heegner theorem [Sta67] implies that the squarefree $k > 0$ such that
> $\mathbb{Q}(\sqrt{-k})$ has class number $1$ are exactly $\{1, 2, 3, 7, 11, 19, 43, 67, 163\}$.

```lean
theorem starkHeegner_classNumberOne :
    {k : ℕ | Squarefree k ∧ HasClassNumber k 1} = {1, 2, 3, 7, 11, 19, 43, 67, 163}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38552.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38552.lean#L86).

## `OeisA38552.mod_24_of_isA038552`

Open: stated without proof.

> All terms of A038552 are congruent to $19 \pmod{24}$.

```lean
theorem mod_24_of_isA038552 {n k : ℕ} (h : IsA038552 n k) : k % 24 = 19
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38552.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38552.lean#L117).

## `OeisA38552.isA038552_eq_largestNegFundDisc`

Open: stated without proof.

> A038552 also gives the largest absolute value of negative fundamental discriminant
> for each class number.

```lean
theorem isA038552_eq_largestNegFundDisc {n k : ℕ} (h : IsA038552 n k) :
    IsLargestNegFundDiscrForClassNumber (n := n) k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38552.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38552.lean#L123).

## `OeisA38552.largestEven_lt_largestOdd_negFundDisc`

Open: stated without proof.

> For even class number $n$, let $k$ be the largest odd number such that the quadratic field
> with discriminant $-k$ has class number $n$, and let $k'$ be the largest even such number, when
> they exist. Then $k > k'$.

```lean
theorem largestEven_lt_largestOdd_negFundDisc {n k k' : ℕ} (hn : Even n)
    (hk : IsGreatest {m : ℕ | Odd m ∧ IsFundamentalDiscr (-m : ℤ) ∧
      classNumberOfDiscriminant (-m : ℤ) = n} k)
    (hk' : IsGreatest {m : ℕ | Even m ∧ IsFundamentalDiscr (-m : ℤ) ∧
      classNumberOfDiscriminant (-m : ℤ) = n} k') : k' < k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38552.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38552.lean#L131).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/38552.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38552.lean)
- [oeis.org/A038552](https://oeis.org/A038552)
