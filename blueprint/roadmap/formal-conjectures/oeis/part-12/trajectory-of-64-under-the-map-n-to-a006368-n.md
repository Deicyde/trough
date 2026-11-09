---
declaration: theorem
origin: cited
lean: OeisA223086.conjecture
statement: formalized
---

# Trajectory of $64$ under the map $n \to \text{A006368}(n)$

> The map is given by
>
> $$f(n) = \begin{cases}
> 3n/2 & \text{if } n \equiv 0 \pmod 2, \\
> (3n+1)/4 & \text{if } n \equiv 1 \pmod 4, \\
> (3n-1)/4 & \text{if } n \equiv 3 \pmod 4.
> \end{cases}$$
>
> *References:*
> - [A223086](https://oeis.org/A223086)

*Quoted from [FormalConjectures/OEIS/223086.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/223086.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 7 test statements, counted here but not shown.

## `OeisA223086.conjecture`

Open: stated without proof.

> It is conjectured that this trajectory does not close on itself.

```lean
theorem conjecture (i j : ℕ) (hi : 0 < i) (hj : 0 < j) (h : a i = a j) : i = j
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/223086.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/223086.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/223086.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/223086.lean)
- [A223086](https://oeis.org/A223086)
