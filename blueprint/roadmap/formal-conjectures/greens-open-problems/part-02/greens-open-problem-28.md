---
declaration: theorem
origin: cited
lean: Green28.green_28
statement: formalized
---

# Green's Open Problem 28

> References:
> - [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.28)
> - [Mathoverflow/339137](https://mathoverflow.net/questions/339137/why-do-polynomials-with-coefficients-0-1-like-to-have-only-factors-with-0-1) asked by user [Sil](https://mathoverflow.net/users/136794/sil)
> - [MathStackexchange/3325163](https://math.stackexchange.com/questions/3325163/) asked by user [Emmanuel Amiot](https://math.stackexchange.com/users/403309/emmanuel-amiot)

*Quoted from [FormalConjectures/GreensOpenProblems/28.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/28.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Green28.green_28`

Open: stated without proof.

> Suppose that $X, Y$ are two finitely-supported independent random variables taking integer values,
> and such that $X + Y$ is uniformly distributed on its range. Are $X$ and $Y$ themselves uniformly
> distributed on their ranges?

```lean
theorem green_28 :
  ∀ (X Y : PMF ℤ), -- marginals, independence is built into indepSum
    X.support.Finite ∧ Y.support.Finite ∧ IsUniformOnSupport (indepSum X Y) →
      IsUniformOnSupport X ∧ IsUniformOnSupport Y
```

Category `research open`; AMS [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/28.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/28.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/28.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/28.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.28)
