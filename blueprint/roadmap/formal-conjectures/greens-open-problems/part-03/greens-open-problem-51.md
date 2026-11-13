---
declaration: theorem
origin: cited
lean: Green51.green_51, Green51.green_51.lower, Green51.green_51.upper, Green51.green_51.one_half, Green51.green_51.lower_ap, Green51.green_51.upper_ap
statement: formalized
---

# Green's Open Problem 51

> *References:*
> - [Gr24] [Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.51)
> - [Gr13] B. J. Green, Restriction and Kakeya phenomena, notes from a 2003 course.
>   Available at http://people.maths.ox.ac.uk/greenbj/papers/rkp.pdf
> - [Sa11] Sanders, Tom. "Green's sumset problem at density one half."
>   Acta Arithmetica 146.1 (2011): 91-101.
> - [Gr02] Green, Ben. "Arithmetic progressions in sumsets."
>   Geometric & Functional Analysis GAFA 12.3 (2002): 584-597.
> - [Ruz91] Ruzsa, Imre Z. "Arithmetic progressions in sumsets."
>   Acta Arithmetica 60.2 (1991): 191-202.

*Quoted from [FormalConjectures/GreensOpenProblems/51.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 2 open and 4 solved.

## `Green51.green_51`

Open: stated without proof.

> Suppose that $A \subset \mathbb{F}_2^n$ is a set of density $\alpha$. What is the largest size of coset
> guaranteed to be contained in $2A$?
>
> We phrase this by asking for the exact function $F(\alpha, n)$ giving the maximum dimension
> of a guaranteed coset.

```lean
theorem green_51 : green_51.answer = guaranteedMaxCosetDim
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/51.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean#L56).

## `Green51.green_51.lower`

Solved: stated here without proof.

> It is known that $A + A$ must contain a coset of dimension $\gg_\alpha n$ [Gr13].

```lean
theorem green_51.lower :
    ∀ (α : ℝ), 0 < α → α ≤ 1 →
    ∃ c > 0, ∀ᶠ (n : ℕ) in atTop, c * (n : ℝ) ≤ guaranteedMaxCosetDim n α
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/51.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean#L61).

## `Green51.green_51.upper`

Solved: stated here without proof.

> It is known that $A + A$ need not contain a coset of dimension $n - \sqrt{n}$ [Gr13].

```lean
theorem green_51.upper :
    ∃ α > 0, α ≤ 1 ∧ ∀ᶠ (n : ℕ) in atTop, (guaranteedMaxCosetDim n α : ℝ) < (n : ℝ) - sqrt n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/51.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean#L68).

## `Green51.green_51.one_half`

Open: stated without proof.

> Suppose that $A \subset \mathbb{F}_2^n$ has density $\alpha > 1/2 - C/\sqrt{n}$.
> Does $A + A$ contain a subspace of co-dimension $O_C(1)$? [Sa11, Question 5.1]

```lean
theorem green_51.one_half :
    ∀ (k : ℝ), 0 < k →
      ∃ (c : ℕ), ∀ᶠ (n : ℕ) in atTop,
        ∀ (α : ℝ), α > (1/2 : ℝ) - k / sqrt (n : ℝ) → α ≤ 1 →
          n ≤ guaranteedMaxCosetDim n α + c
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/51.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean#L77).

## `Green51.green_51.lower_ap`

Solved: stated here without proof.

> It is known that $A + A$ must contain an arithmetic progression of length $\sim \exp(c (\log N)^{1/2})$ [Gr02].

```lean
theorem green_51.lower_ap :
    ∀ (α : ℝ), 0 < α → α ≤ 1 →
      ∃ c > 0, ∀ᶠ (N : ℕ) in atTop,
        exp (c * log (N : ℝ) ^ (1/2 : ℝ)) ≤ guaranteedMaxAPLength N α
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/51.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean#L94).

## `Green51.green_51.upper_ap`

Solved: stated here without proof.

> It is known that $A + A$ need not contain an arithmetic progression of length
> $\sim \exp(c (\log N)^{2/3 + \varepsilon})$, for any $\varepsilon > 0$ [Ruz91].

```lean
theorem green_51.upper_ap :
    ∀ (α : ℝ), 0 < α → α < 1/2 → ∀ (ε : ℝ), 0 < ε →
      ∃ c > 0, ∀ᶠ (N : ℕ) in atTop,
        guaranteedMaxAPLength N α ≤ exp (c * log (N : ℝ) ^ (2/3 + ε : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/51.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/51.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/51.lean)
- [Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.51)
