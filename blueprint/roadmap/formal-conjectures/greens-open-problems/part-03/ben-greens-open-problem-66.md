---
declaration: theorem
origin: cited
lean: Green66.green_66, Green66.green_66.variants.trivial_bound
statement: formalized
---

# Ben Green's Open Problem 66

> *Reference:* [Ben Green's Open Problem 66](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)

*Quoted from [FormalConjectures/GreensOpenProblems/66.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/66.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green66.green_66`

Open: stated without proof.

> Is there always a sum of two squares between $X - \frac{1}{10}X^{1/4}$ and $X$?
> We formalize this as an eventual statement for sufficiently large real $X$.

```lean
theorem green_66 :
    ∀ᶠ X : ℝ in atTop,
      ∃ n : ℕ, IsSumOfTwoSquares n ∧
        (n : ℝ) ∈ Set.Icc (X - (1 / 10 : ℝ) * X ^ (1 / 4 : ℝ)) X
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/66.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/66.lean#L41).

## `Green66.green_66.variants.trivial_bound`

Proved here.

> Green notes that a well-known, almost trivial argument gives an $O(X^{1/4})$ bound on the left.

```lean
theorem green_66.variants.trivial_bound :
    ∃ C > (0 : ℝ), ∀ᶠ X : ℝ in atTop,
      ∃ n : ℕ, IsSumOfTwoSquares n ∧
        (n : ℝ) ∈ Set.Icc (X - C * X ^ (1 / 4 : ℝ)) X
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/66.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/66.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/66.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/GreensOpenProblems/66.lean)
- [Ben Green's Open Problem 66](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)
