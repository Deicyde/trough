---
declaration: theorem
origin: cited
lean: OeisA281976.conjecture
statement: formalized
---

# Sum of four squares with square conditions

> Any integer $n \geq 0$ can be written as $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative
> integers and $z \leq w$, such that both $x$ and $x + 24y$ are squares.
>
> Zhi-Wei Sun has offered a \$2,400 prize for the first proof.
>
> *References:*
> - [A281976](https://oeis.org/A281976)
> - Z.-W. Sun, "Refining Lagrange's four-square theorem," *J. Number Theory* **175** (2017), 167-190.
>   https://doi.org/10.1016/j.jnt.2016.11.008
> - Z.-W. Sun, "Restricted sums of four squares," *arXiv:1701.05868* [math.NT], 2017.
>   https://arxiv.org/abs/1701.05868

*Quoted from [FormalConjectures/OEIS/281976.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/281976.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 9 test statements, counted here but not shown.

## `OeisA281976.conjecture`

Open: stated without proof.

> **Zhi-Wei Sun's Conjecture (A281976)**: Any integer $n \geq 0$ can be written as $x^2 + y^2 + z^2 + w^2$
> with $x, y, z, w$ nonnegative integers and $z \leq w$, such that both $x$ and $x + 24y$ are squares.

```lean
theorem conjecture (n : ℕ) : A n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/281976.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/281976.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/281976.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/281976.lean)
- [A281976](https://oeis.org/A281976)
