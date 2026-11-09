---
declaration: theorem
origin: cited
lean: OeisA5132.conjecture
statement: formalized
---

# Recamán's sequence

> Start with $a(0)=0$. At step $n>0$, subtract $n$ from the preceding term when the result is
> nonnegative and has not appeared earlier; otherwise add $n$.
>
> *References:*
> - [OEIS A005132](https://oeis.org/A005132)

*Quoted from [FormalConjectures/OEIS/5132.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5132.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 10 test statements and 7 API statements, counted here but not shown.

## `OeisA5132.conjecture`

Open: stated without proof.

> “I conjecture that every number eventually appears” — N. J. A. Sloane,
> [OEIS A005132](https://oeis.org/A005132).
>
> Sloane later added that he was no longer sure every number appears. The coverage question remains
> open and is formalized here as surjectivity onto the natural numbers.

```lean
theorem conjecture : Function.Surjective a
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/5132.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5132.lean#L168).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/5132.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/5132.lean)
- [OEIS A005132](https://oeis.org/A005132)
