---
declaration: theorem
origin: cited
lean: OeisA72200.conjecture
statement: formalized
---

# Smallest factorial containing exactly $n$ 6's

> The sequence $a(n)$ gives the smallest $k$ such that the decimal expansion of $k!$
> contains exactly $n$ occurrences of the digit '6', or $0$ if no such $k$ exists.
>
> *References:*
> - [A072200](https://oeis.org/A072200)

*Quoted from [FormalConjectures/OEIS/72200.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/72200.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA72200.conjecture`

Open: stated without proof.

> It is conjectured that $a(24) = 0$ since no factorial less than $10000$ contained just 24 sixes.

```lean
theorem conjecture : a 24 = 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/72200.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/72200.lean#L95).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/72200.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/72200.lean)
- [A072200](https://oeis.org/A072200)
