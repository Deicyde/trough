---
declaration: theorem
origin: cited
lean: OeisA217703.conjecture_1, OeisA217703.conjecture_2, OeisA217703.conjecture_3
statement: formalized
---

# Recurrence $a(n+1) = 2n(n+1)a(n) - n^4 a(n-1)$ and associated polynomials

> The sequence $a(n)$ is defined by $a(0) = 1$, $a(1) = 0$, and
> $a(n+1) = 2n(n+1)a(n) - n^4 a(n-1)$ for $n > 0$.
> The associated polynomials $S_n(x) \in \mathbb{Z}[x]$ satisfy $S_0(x) = 1$, $S_1(x) = x$, and
> $S_{n+1}(x) = (x + 2n(n+1)) S_n(x) - n^4 S_{n-1}(x)$ for $n > 0$.
>
> *References:*
> - [A217703](https://oeis.org/A217703)
> - [Sun-Conjectures-ii-iii-](https://github.com/anshM123/Sun-Conjectures-ii-iii-)
>   by *Ansh Mishra* and *Aryan Senthilkumar* (2026)

*Quoted from [FormalConjectures/OEIS/217703.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/217703.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 5 test statements, counted here but not shown.

## `OeisA217703.conjecture_1`

Open: stated without proof.

> Conjecture, (i): $S_n(x)$ is irreducible over the field of rational numbers
> for every $n = 1, 2, 3, \dots$
> - _Zhi-Wei Sun_, Mar 20 2013

```lean
theorem conjecture_1 (n : ℕ) (hn : 1 ≤ n) :
    Irreducible (Polynomial.map (Int.castRingHom ℚ) (polyS n))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/OEIS/217703.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/217703.lean#L78).

## `OeisA217703.conjecture_2`

Solved: stated here without proof.

> Conjecture, (ii): $a(n) = S_n(0)$ is negative if and only if
> $1 < n < 58$ or $n > 2177$.
> - _Zhi-Wei Sun_, Mar 20 2013
>
> Disproved by Ansh Mishra and Aryan Senthilkumar: $a(81935) > 0$.

```lean
theorem conjecture_2 :
    ¬ ∀ n : ℕ, (a n < 0 ↔ (1 < n ∧ n < 58) ∨ 2177 < n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/217703.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/217703.lean#L90).

## `OeisA217703.conjecture_3`

Solved: stated here; a Lean proof is at [https://github.com/anshM123/Sun-Conjectures-ii-iii-/blob/7016c789cbe3b36aff4a5bcaa3ece16ea9331f8e/lean/DMSolutions/OEIS_A217703/Solution.lean#L19-L23](https://github.com/anshM123/Sun-Conjectures-ii-iii-/blob/7016c789cbe3b36aff4a5bcaa3ece16ea9331f8e/lean/DMSolutions/OEIS_A217703/Solution.lean#L19-L23).

> Conjecture, (iii): $|a(n)|^{1/n} = o(n^2)$ as $n$ tends to infinity.
> - _Zhi-Wei Sun_, Mar 20 2013
>
> Disproved and formalized in Lean 4 by Ansh Mishra and Aryan Senthilkumar (with Claude).

```lean
theorem conjecture_3 :
    ¬ Filter.Tendsto (fun n : ℕ => |(a n : ℝ)| ^ (1 / (n : ℝ)) / (n : ℝ) ^ 2)
      Filter.atTop (nhds 0)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [26 Real functions](../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/OEIS/217703.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/217703.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/217703.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/217703.lean)
- [A217703](https://oeis.org/A217703)
