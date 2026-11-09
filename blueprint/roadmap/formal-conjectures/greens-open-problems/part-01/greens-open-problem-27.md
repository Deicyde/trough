---
declaration: theorem
origin: cited
lean: Green27.green_27.equivalent, Green27.green_27.lower, Green27.green_27.upper, Green27.green_27.variants.lower_be23, Green27.green_27.variants.lower_cy26, Green27.green_27.variants.upper_be23, Green27.green_27.variants.previous_lower, Green27.green_27.variants.previous_upper
statement: formalized
---

# Green's Open Problem 27

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.27)
> - [Be23] Bedert, Benjamin. "On unique sums in Abelian groups." Combinatorica 44.2 (2024): 269-298.
> - [CY26] Cao, Jiao-Long, and Ye Yuan. "A Second-Logarithm Lower Bound for Sets with No Unique
>   Sums." arXiv preprint arXiv:2608.06728 (2026).
> - [St76] Straus, E. G. "Differences of residues (mod p)." Journal of Number Theory 8.1 (1976): 40-42.

*Quoted from [FormalConjectures/GreensOpenProblems/27.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 2 open and 6 solved.

## `Green27.green_27.equivalent`

Open: stated without proof.

> What is the size of the smallest set $A \subset \mathbb{Z} / p\mathbb{Z}$ (with at least two elements)
> for which no element in the sumset $A + A$ has a unique representation?

```lean
theorem green_27.equivalent :
  green_27.equivalent.answer ~[primesAtTop] m
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L63).

## `Green27.green_27.lower`

Solved: stated here without proof.

> Propose a better lower bound along primes.
>
> Cao and Yuan [CY26, Theorem 1.1] prove $m(p) \gg \log p \log \log p$. This beats `lowerBest`,
> since $\sqrt{\log \log \log p} / \log \log \log \log p = o(\log \log p)$. The exact order of
> $m(p)$ remains open.

```lean
theorem green_27.lower :
    (lowerBest =o[primesAtTop] green_27.lower.answer) ∧ (green_27.lower.answer =O[primesAtTop] m)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L75).

## `Green27.green_27.upper`

Open: stated without proof.

> Propose a better upper bound along primes.

```lean
theorem green_27.upper :
    (green_27.upper.answer =o[primesAtTop] upperBest) ∧ (m =O[primesAtTop] green_27.upper.answer)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L84).

## `Green27.green_27.variants.lower_be23`

Solved: stated here without proof.

> We have $m(p) \geq \omega(p) \log p$ for some function $\omega(p)$ tending to infinity [Be23, Theorem 3].

```lean
theorem green_27.variants.lower_be23 :
  ∃ ω : ℕ → ℝ, Tendsto ω primesAtTop atTop ∧
    ∀ᶠ p in primesAtTop,
      ω p * Real.log (p : ℝ) ≤ m p
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L93).

## `Green27.green_27.variants.lower_cy26`

Solved: stated here without proof.

> Lower bound: $\log p \log \log p \ll m(p)$ [CY26, Theorem 1.1].

```lean
theorem green_27.variants.lower_cy26 :
  (fun p ↦ Real.log (p : ℝ) * Real.log (Real.log (p : ℝ))) =O[primesAtTop] m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L101).

## `Green27.green_27.variants.upper_be23`

Solved: stated here; a Lean proof is at [https://github.com/mkwatson/unique-sums-notes/blob/d4383f93a52e3a916ccce78d5fb7739c3bf3dabc/Green27Upper/Theorem.lean#L26](https://github.com/mkwatson/unique-sums-notes/blob/d4383f93a52e3a916ccce78d5fb7739c3bf3dabc/Green27Upper/Theorem.lean#L26).

> Upper bound: $m(p) \ll (\log p)^2$ [Be23, Theorem 5].

```lean
theorem green_27.variants.upper_be23 :
  m =O[primesAtTop] upperBest
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L110).

## `Green27.green_27.variants.previous_lower`

Solved: stated here without proof.

> Previous best-known lower bound $\log p \ll m(p)$ from [St76].

```lean
theorem green_27.variants.previous_lower :
  (fun p ↦ Real.log (p : ℝ)) =O[primesAtTop] m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L116).

## `Green27.green_27.variants.previous_upper`

Solved: stated here without proof.

> Previous best-known upper bound $m(p) \ll \sqrt{p}$ from [Be23].

```lean
theorem green_27.variants.previous_upper :
  m =O[primesAtTop] (fun p ↦ Real.sqrt (p : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/27.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean#L122).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/27.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/27.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.27)
