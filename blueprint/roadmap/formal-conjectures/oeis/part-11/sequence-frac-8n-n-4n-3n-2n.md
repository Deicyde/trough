---
declaration: theorem
origin: cited
lean: OeisA211420.conjecture_1, OeisA211420.conjecture_2, OeisA211420.conjecture_3, OeisA211420.conjecture_4, OeisA211420.conjecture_5, OeisA211420.conjecture_6
statement: formalized
---

# Sequence $\frac{(8n)! n!}{(4n)! (3n)! (2n)!}$

> The sequence $a(n) = \frac{(8n)! n!}{(4n)! (3n)! (2n)!}$, which is always an integer for $n \ge 0$.
>
> *References:*
> - [A211420](https://oeis.org/A211420)
> - T. Adamczewski, "OEIS Open: How many conjectures can language models turn into theorems?",
>   [arXiv:2608.11941](https://arxiv.org/abs/2608.11941) [cs.AI], 2026.
> - [OEIS-A211420](https://github.com/anshM123/OEIS-A211420)
>   by *Ansh Mishra* and *Aryan Senthilkumar* (2026)

*Quoted from [FormalConjectures/OEIS/211420.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 6 solved. It also has 5 test statements, counted here but not shown.

## `OeisA211420.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L25-L28](https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L25-L28).

> "It appears that $35 \cdot a(n)/(n + 1)$ is an integer for all $n$."
> - _Peter Bala_, Aug 26 2025
>
> Proved and formalized in Lean 4 by Ansh Mishra and Aryan Senthilkumar (with Claude).

```lean
theorem conjecture_1 (n : ℕ) : (n + 1) ∣ 35 * a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211420.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean#L70).

## `OeisA211420.conjecture_2`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L25-L28](https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L25-L28).

> "It appears that $3 \cdot a(n)/(2n + 1)$ is an integer for all $n$."
> - _Peter Bala_, Aug 26 2025
>
> Proved and formalized in Lean 4 by Ansh Mishra and Aryan Senthilkumar (with Claude).

```lean
theorem conjecture_2 (n : ℕ) : (2 * n + 1) ∣ 3 * a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211420.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean#L83).

## `OeisA211420.conjecture_3`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L25-L28](https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L25-L28).

> "It appears that $5 \cdot a(n)/(3n + 1)$ is an integer for all $n$."
> - _Peter Bala_, Aug 26 2025
>
> Follows from a result of Z.-W. Sun (2012), and formalized in Lean 4 by Ansh Mishra and Aryan
> Senthilkumar (with Claude).

```lean
theorem conjecture_3 (n : ℕ) : (3 * n + 1) ∣ 5 * a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211420.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean#L97).

## `OeisA211420.conjecture_4`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L30-L33](https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L30-L33).

> "More generally, we conjecture that there are constants $C(k, r) > 0$, $k = 1, 2$ or $3$, $r \ge 1$,
> such that $a(n) \cdot C(k, r)/((kn + 1)(kn + 2)\cdots(kn + r))$ is an integer for all $n$."
> - _Peter Bala_, Aug 26 2025
>
> Proved and formalized in Lean 4 by DannyExperiments (2026) and independently by Ansh Mishra and
> Aryan Senthilkumar (with Claude).

```lean
theorem conjecture_4 (k r : ℕ) (hk : k = 1 ∨ k = 2 ∨ k = 3) (hr : 1 ≤ r) :
    ∃ C : ℕ, 0 < C ∧ ∀ n : ℕ, (k * n + 1).ascFactorial r ∣ C * a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211420.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean#L112).

## `OeisA211420.conjecture_5`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L35-L38](https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L35-L38).

> "It also appears that $a(n)$ is divisible by $8n - 1$ for all $n$."
> - _Peter Bala_, Aug 26 2025
>
> Proved and formalized in Lean 4 by Ansh Mishra and Aryan Senthilkumar (with Claude).

```lean
theorem conjecture_5 (n : ℕ) :
    ((8 * n : ℤ) - 1) ∣ (a n : ℤ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211420.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean#L126).

## `OeisA211420.conjecture_6`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L40-L43](https://github.com/anshM123/OEIS-A211420/blob/2bd4dbf1185a9fa8edc2cb9a61d471583d018d08/lean/DMSolutions/OEIS_A211420/Solution.lean#L40-L43).

> "More generally, we conjecture that there are constants $K(r) > 0$, $r \ge 0$, such that
> $a(n) \cdot K(r)/((8n - 1)(8n - 3)\cdots(8n - (2r+1)))$ is an integer for all $n$."
> - _Peter Bala_, Aug 26 2025
>
> Proved in the OEIS Open project, see T. Adamczewski, OEIS Open: How many conjectures can
> language models turn into theorems?, [arXiv:2608.11941](https://arxiv.org/abs/2608.11941),
> and also by Ansh Mishra and Aryan Senthilkumar (with Claude).

```lean
theorem conjecture_6 (r : ℕ) :
    ∃ K : ℤ, 0 < K ∧ ∀ n : ℕ, oddDescendingProduct n r ∣ (a n : ℤ) * K
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/211420.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean#L143).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/211420.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/211420.lean)
- [A211420](https://oeis.org/A211420)
