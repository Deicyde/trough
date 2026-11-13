---
declaration: theorem
origin: cited
lean: Green3.green_3
statement: formalized
---

# Ben Green's Open Problem 3

> *References:*
> - [Ben Green's Open Problem 3](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.3 Problem 3)
> - [FGY26] Franchi, Leonardo and Gowers, W. T. and Yip, Fredy, *Product-free subsets of $(0,1)$*,
>   [arXiv:2607.06073](https://arxiv.org/abs/2607.06073), Theorem 1.1.

*Quoted from [FormalConjectures/GreensOpenProblems/3.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/3.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Green3.green_3`

Solved: stated here without proof.

> Suppose that $A \subset [0,1]$ is open and has measure greater than $\frac{1}{3}$. Is there a
> solution to $xy = z$ with $x, y, z \in A$?
>
> The answer is yes. [FGY26] prove that an open product-free subset of $(0,1)$ has measure strictly
> less than $\frac{1}{3}$.

```lean
theorem green_3 :
    ∀ A : Set ℝ,
      IsOpen A → A ⊆ Icc 0 1 → volume A > 1/3 →
        ∃ x y z, x ∈ A ∧ y ∈ A ∧ z ∈ A ∧ x * y = z
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/3.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/3.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/3.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/3.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.3](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.3)
