---
declaration: theorem
origin: cited
lean: OeisA77408.conjecture
statement: formalized
---

# Trajectory of 103 under the Reverse and Add! operation in base 3

> The sequence $a(n)$ is the trajectory of $103$ under the Reverse and Add! operation carried out
> in base $3$, written in base $10$.
> $a(0) = 103$, and $a(n+1) = a(n) + \text{rev}_3(a(n))$.
>
> *References:*
> - [A077408](https://oeis.org/A077408)

*Quoted from [FormalConjectures/OEIS/77408.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/77408.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA77408.conjecture`

Open: stated without proof.

> $103$ is conjectured to be the smallest number such that the Reverse and Add! algorithm in base $3$
> does not lead to a palindrome. Its trajectory is conjectured to never reach a palindrome.

```lean
theorem conjecture (n : ℕ) : ¬ IsBasePalindrome 3 (a n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/77408.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/77408.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/77408.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/77408.lean)
- [A077408](https://oeis.org/A077408)
