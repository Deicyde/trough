---
declaration: theorem
origin: cited
lean: Green23.green_23
statement: formalized
---

# Green's Open Problem 23

> References:
> - [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.23)
> - [FrKlMo25] Frantzikinakis, N., O. Klurman, and J. Moreira. "Partition regularity of Pythagorean pairs." Forum of Mathematics, Pi 13. Cambridge University Press (2025).

*Quoted from [FormalConjectures/GreensOpenProblems/23.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/23.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Green23.green_23`

Solved: stated here without proof.

> Suppose that $\mathbb{N}$ is finitely coloured. Are there $x,y$ of the same colour such that $x^2 +
>  y^2$ is a square?
>
> Solved in [FrKlMo25].

```lean
theorem green_23 :
    -- For every finite colouring of the natural numbers
    ∀ (k : ℕ) (c : ℕ → Fin k),
    -- there exist two numbers of the same colour whose squares sum to a square
    ∃ x y : ℕ,
      0 < x ∧ 0 < y ∧  -- Exclude trivial x^2 + 0^2 = x^2 solution
      c x = c y ∧      -- Same colour
      IsSquare (x^2 + y^2)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/23.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/23.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/23.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/23.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.23)
