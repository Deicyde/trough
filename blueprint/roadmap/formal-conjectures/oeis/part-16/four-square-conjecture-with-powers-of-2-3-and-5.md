---
declaration: theorem
origin: cited
lean: OeisA308734.conjecture
statement: formalized
---

# Four-square conjecture with powers of 2, 3, and 5

> Any integer $n > 1$ can be written as $(2^a \cdot 3^b)^2 + (2^c \cdot 5^d)^2 + x^2 + y^2$
> where $a, b, c, d, x, y$ are nonnegative integers.
>
> Zhi-Wei Sun has offered a \$2,500 prize for the first proof.
>
> *References:*
> - [A308734](https://oeis.org/A308734)
> - Z.-W. Sun, "Refining Lagrange's four-square theorem," *J. Number Theory* **175** (2017), 167-190.
>   https://doi.org/10.1016/j.jnt.2016.11.008
> - Z.-W. Sun, "Restricted sums of four squares," *Int. J. Number Theory* **15** (2019), 1863-1893.
> - Z.-W. Sun, "Various Refinements of Lagrange's Four-Square Theorem," Westlake Number Theory
>   Symposium, Nanjing University, China, 2020.
> - S. Banerjee, "On a conjecture of Sun about sums of restricted squares," *J. Number Theory*
>   **256** (2024), 253-289.

*Quoted from [FormalConjectures/OEIS/308734.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/308734.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA308734.conjecture`

Open: stated without proof.

> **Zhi-Wei Sun's Four-Square Conjecture (A308734)**: Any integer $n > 1$ can be written as
> $(2^a \cdot 3^b)^2 + (2^c \cdot 5^d)^2 + x^2 + y^2$ for nonnegative integers $a, b, c, d, x, y$.

```lean
theorem conjecture (n : ℕ) (hn : 1 < n) : A n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/308734.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/308734.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/308734.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/308734.lean)
- [A308734](https://oeis.org/A308734)
