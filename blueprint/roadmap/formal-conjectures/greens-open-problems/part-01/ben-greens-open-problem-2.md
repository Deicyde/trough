---
declaration: theorem
origin: cited
lean: Green2.green_2, Green2.green_2_lower_bound_sanders, Green2.green_2_upper_bound_erdos, Green2.green_2_upper_bound_choi, Green2.green_2_upper_bound_ruzsa
statement: formalized
---

# Ben Green's Open Problem 2

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.2)
> - [Er65] P. Erdős. Extremal problems in number theory, In Proc. Sympos. Pure Math., Vol. VIII,
>   pages 181–189. Amer. Math. Soc., Providence, R.I., 1965.
> - [Sa21] Sanders, Tom. "The Erdős–Moser Sum-free Set Problem." Canadian Journal of Mathematics 73.1
>   (2021): 63-107.
> - [Ru05] I. Z. Ruzsa, Sum-avoiding subsets. Ramanujan J., 9 (2005) (1-2):77–82.
> - [Ch71] S. L. G. Choi. On a combinatorial problem in number theory. Proc. London Math. Soc. (3),
>   23:629–642, 1971. doi:10.1112/plms/s3-23.4.629.
> - [BSS00] A. Baltz, T. Schoen, and A. Srivastav. Probabilistic construction of small strongly
>   sum-free sets via large Sidon sets. Colloq. Math., 86(2):171–176, 2000.
>   doi:10.4064/cm-86-2-171-176.

*Quoted from [FormalConjectures/GreensOpenProblems/2.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/2.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Green2.green_2`

Open: stated without proof.

> Let $A \subset \mathbf{Z}$ be a set of $n$ integers. Is there a set $S \subset A$ of size
> $(\log n)^{100}$ such that the restricted sumset$S \hat{+} S$ is disjoint from $A$?

```lean
theorem green_2 :
    ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℤ, A.card = n →
      (maxRestrictedSumAvoidingSubsetSize A : ℝ) ≥ (Real.log n) ^ 100
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/2.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/2.lean#L58).

## `Green2.green_2_lower_bound_sanders`

Solved: stated here without proof.

> From [Sa21] it is known that there is always such an S with $|S| \gt (\log |A|)^{1+c}$.

```lean
theorem green_2_lower_bound_sanders :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ A : Finset ℤ, A.card = n →
      maxRestrictedSumAvoidingSubsetSize A ≥ Real.log n ^ (1 + c)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/2.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/2.lean#L67).

## `Green2.green_2_upper_bound_erdos`

Solved: stated here without proof.

> From [Er65] it is known that $M(A) \le \frac{1}{3}|A| + O(1)$.

```lean
theorem green_2_upper_bound_erdos :
    ∃ C : ℝ, ∀ᶠ n in atTop, ∃ A : Finset ℤ, A.card = n ∧
      (maxRestrictedSumAvoidingSubsetSize A : ℝ) ≤ A.card / 3 + C
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/2.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/2.lean#L76).

## `Green2.green_2_upper_bound_choi`

Solved: stated here without proof.

> From [Ch71] it is known that $M(A) \le |A|^{2/5 + o(1)}$.

```lean
theorem green_2_upper_bound_choi :
    ∃ (o : ℕ → ℝ) (_ : Tendsto o atTop (𝓝 0)), ∀ᶠ n in atTop, ∃ A : Finset ℤ, A.card = n ∧
      (maxRestrictedSumAvoidingSubsetSize A : ℝ) ≤ A.card ^ (2 / 5 + o A.card)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/2.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/2.lean#L90).

## `Green2.green_2_upper_bound_ruzsa`

Solved: stated here without proof.

> From [Ru05] the best-known upper bound is $|S| \lt e^{C \sqrt{\log |A|}}$.

```lean
theorem green_2_upper_bound_ruzsa :
    ∃ C > (0 : ℝ), ∀ᶠ n in atTop, ∃ A : Finset ℤ, A.card = n ∧
      (maxRestrictedSumAvoidingSubsetSize A : ℝ) < Real.exp (C * Real.sqrt (Real.log A.card))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/2.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/2.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/2.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/2.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.2)
