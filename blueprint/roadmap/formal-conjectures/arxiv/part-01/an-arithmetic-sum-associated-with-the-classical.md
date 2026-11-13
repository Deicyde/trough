---
declaration: theorem
origin: cited
lean: Arxiv.«2501.03234».conjecture_1_1, Arxiv.«2501.03234».conjecture_4_1, Arxiv.«2501.03234».conjecture_4_2, Arxiv.«2501.03234».conjecture_4_3, Arxiv.«2501.03234».conjecture_4_4
statement: formalized
---

# An Arithmetic Sum Associated with the Classical Theta Function

> *Reference:* [arxiv/2501.03234](https://arxiv.org/abs/2501.03234)
> **An Arithmetic Sum Associated with the Classical Theta Function**
> by *Bruce C. Berndt, Raghavendra N. Bhat, Jeffrey L. Meyer, Likun Xie, Alexandru Zaharescu*

*Quoted from [FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 5 test statements, counted here but not shown.

## `Arxiv.«2501.03234».conjecture_1_1`

Open: stated without proof.

> **Conjecture 1.1**: For any odd prime $k$, the sum associated with the classical theta function $θ_3$,
> $S(k)$ is positive.

```lean
theorem conjecture_1_1 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) : 0 < S k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean#L65).

## `Arxiv.«2501.03234».conjecture_4_1`

Open: stated without proof.

> **Conjecture 4.1**: For any prime $k$ larger than $5$, $S(k) > k$.

```lean
theorem conjecture_4_1 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) (hgt : k > 5) : k < S k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean#L72).

## `Arxiv.«2501.03234».conjecture_4_2`

Open: stated without proof.

> **Conjecture 4.2**: For any prime $k$ larger than $233$, $S(k) > 2k$.

```lean
theorem conjecture_4_2 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) (hgt : k > 233) : 2 * k < S k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean#L79).

## `Arxiv.«2501.03234».conjecture_4_3`

Open: stated without proof.

> **Conjecture 4.3**: For any prime $k$ larger than $3119$, $S(k) > 3k$.

```lean
theorem conjecture_4_3 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) (hgt : k > 3119) : 3 * k < S k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean#L86).

## `Arxiv.«2501.03234».conjecture_4_4`

Open: stated without proof.

> **Conjecture 4.4**: Given a natural number $n ∈ ℕ$, for all large enough odd prime $k$ (depending on $n$),
> $nk < S(k)$.

```lean
theorem conjecture_4_4 (n : ℕ) : ∀ᶠ (k : ℕ) in Filter.atTop, k.Prime → Odd k → n * k < S k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2501.03234/ArithmeticSumS.lean)
- [arxiv/2501.03234](https://arxiv.org/abs/2501.03234)
