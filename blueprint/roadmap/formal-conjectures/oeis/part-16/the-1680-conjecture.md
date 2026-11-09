---
declaration: theorem
origin: cited
lean: OeisA280831.conjecture
statement: formalized
---

# The 1680-Conjecture

> Any nonnegative integer can be written as $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative
> integers such that $x^4 + 1680 y^3 z$ is a square.
>
> Zhi-Wei Sun has offered a prize of 1,680 RMB for the first proof.
>
> *References:*
> - [A280831](https://oeis.org/A280831)
> - Z.-W. Sun, "Refining Lagrange's four-square theorem," *J. Number Theory* **175** (2017), 167-190.
> - Z.-W. Sun, "Refining Lagrange's four-square theorem," arXiv:1604.06723 [math.NT], 2016.

*Quoted from [FormalConjectures/OEIS/280831.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/280831.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 7 test statements, counted here but not shown.

## `OeisA280831.conjecture`

Open: stated without proof.

> **Zhi-Wei Sun's 1680-Conjecture (A280831)**: Any nonnegative integer can be written as
> $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative integers such that $x^4 + 1680 y^3 z$ is a square.

```lean
theorem conjecture (n : ℕ) : A n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/280831.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/280831.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/280831.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/280831.lean)
- [A280831](https://oeis.org/A280831)
