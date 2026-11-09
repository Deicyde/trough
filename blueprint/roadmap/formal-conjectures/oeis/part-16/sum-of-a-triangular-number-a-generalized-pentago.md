---
declaration: theorem
origin: cited
lean: OeisA287616.conjecture
statement: formalized
---

# Sum of a triangular number, a generalized pentagonal number, and a generalized heptagonal number

> Any nonnegative integer can be written as $x(x+1)/2 + y(3y+1)/2 + z(5z+1)/2$ with $x, y, z$
> nonnegative integers.
>
> Zhi-Wei Sun offered a USD 135 prize for the first proof of this conjecture.
> Cao, Guo, Qiu, Feng and Gao proved it in [CGQFG26].
>
> *References:*
> - [A287616](https://oeis.org/A287616)
> - Zhi-Wei Sun, "Universal sums of three quadratic polynomials", arXiv:1502.03056 [math.NT]
> - [CGQFG26] Y. Cao, D. Guo, R. Qiu, R. Feng and X.-S. Gao, "Every Nonnegative Integer Is a Sum
>   of a Triangular, a Pentagonal, and a Heptagonal Number",
>   [arXiv:2606.26035](https://arxiv.org/abs/2606.26035)

*Quoted from [FormalConjectures/OEIS/287616.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/287616.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA287616.conjecture`

Solved: stated here without proof.

> **Zhi-Wei Sun's Conjecture (A287616)**: Any nonnegative integer can be written as the sum of
> a triangular number $x(x+1)/2$, a generalized pentagonal number $y(3y+1)/2$, and a generalized
> heptagonal number $z(5z+1)/2$, where $x, y, z$ are nonnegative integers.
>
> This was proved in [CGQFG26].

```lean
theorem conjecture (n : ℕ) : A n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/287616.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/287616.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/287616.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/287616.lean)
- [A287616](https://oeis.org/A287616)
