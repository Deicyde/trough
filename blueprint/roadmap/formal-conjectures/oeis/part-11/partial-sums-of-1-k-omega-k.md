---
declaration: theorem
origin: cited
lean: OeisA212496.conjecture_1, OeisA212496.conjecture_2, OeisA212496.conjecture_3, OeisA212496.conjecture_4, OeisA212496.conjecture_5, OeisA212496.conjecture_6
statement: formalized
---

# Partial sums of $(-1)^{k - \Omega(k)}$

> The sequence $a(n) = \sum_{k=1}^n (-1)^{k - \Omega(k)}$, where $\Omega(k)$ is the total number of
> prime factors of $k$ counted with multiplicity.
>
> *References:*
> - [A212496](https://oeis.org/A212496)

*Quoted from [FormalConjectures/OEIS/212496.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 6 open. It also has 5 test statements, counted here but not shown.

## `OeisA212496.conjecture_1`

Open: stated without proof.

> "On May 16 2012, Zhi-Wei Sun conjectured that $a(n)$ is positive for each $n > 4$."
> - _Zhi-Wei Sun_, May 19 2012

```lean
theorem conjecture_1 (n : ℕ) (hn : 4 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212496.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean#L69).

## `OeisA212496.conjecture_2`

Open: stated without proof.

> "Moreover, he guessed that $a(n) > \sqrt{n}$ for any $n > 324$."
> - _Zhi-Wei Sun_, May 19 2012

```lean
theorem conjecture_2 (n : ℕ) (hn : 324 < n) :
    Real.sqrt (n : ℝ) < (a n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212496.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean#L77).

## `OeisA212496.conjecture_3`

Open: stated without proof.

> "He also guessed that $a(n) < \sqrt{n}\log(\log(n))$ for $n > 5892$."
> - _Zhi-Wei Sun_, May 19 2012

```lean
theorem conjecture_3 (n : ℕ) (hn : 5892 < n) :
    (a n : ℝ) < Real.sqrt (n : ℝ) * Real.log (Real.log (n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212496.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean#L86).

## `OeisA212496.conjecture_4`

Open: stated without proof.

> "Sun also conjectured that $b(n) = \sum_{k=1}^n (-1)^{k-\Omega(k)}/k < 0$ for all $n=1,2,3,\dots$"
> - _Zhi-Wei Sun_, May 19 2012

```lean
theorem conjecture_4 (n : ℕ) (hn : 0 < n) : b n < 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212496.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean#L95).

## `OeisA212496.conjecture_5`

Open: stated without proof.

> "Moreover, he guessed that $b(n) < -1/\sqrt{n}$ for all $n > 1$."
> - _Zhi-Wei Sun_, May 19 2012

```lean
theorem conjecture_5 (n : ℕ) (hn : 1 < n) :
    (b n : ℝ) < -1 / Real.sqrt (n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212496.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean#L103).

## `OeisA212496.conjecture_6`

Open: stated without proof.

> "He also guessed that $b(n) > -\log(\log(n))/\sqrt{n}$ for $n > 2008$."
> - _Zhi-Wei Sun_, May 19 2012

```lean
theorem conjecture_6 (n : ℕ) (hn : 2008 < n) :
    -Real.log (Real.log (n : ℝ)) / Real.sqrt (n : ℝ) < (b n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/212496.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean#L112).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/212496.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/212496.lean)
- [A212496](https://oeis.org/A212496)
