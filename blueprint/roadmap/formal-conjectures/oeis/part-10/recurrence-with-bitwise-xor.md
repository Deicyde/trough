---
declaration: theorem
origin: cited
lean: OeisA182510.conjecture1, OeisA182510.conjecture2
statement: formalized
---

# Recurrence with bitwise XOR

> The sequence is defined by $a(0) = 0$, $a(1) = 1$, and for $n \ge 0$,
> $$a(n+2) = (a(n+1) \mathbin{\mathrm{XOR}} (n+2)) - a(n),$$
> where $\mathrm{XOR}$ is the bitwise exclusive-or operator on integers.
>
> *References:*
> - [A182510](https://oeis.org/A182510)

*Quoted from [FormalConjectures/OEIS/182510.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182510.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 7 test statements, counted here but not shown.

## `OeisA182510.conjecture1`

Open: stated without proof.

> Conjecture: the sequence contains 8 zeros.

```lean
theorem conjecture1 : Set.ncard {n : ℕ | a n = 0} = 8
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/182510.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182510.lean#L64).

## `OeisA182510.conjecture2`

Open: stated without proof.

> Conjecture: more positive terms than negative.
>
> As $n \to \infty$, the count of positive terms is greater than the count of negative terms.
>
> The requirement that $n$ is large enough is needed, since the claim fails for $n = 100$.

```lean
theorem conjecture2 :
    ∀ᶠ n in Filter.atTop,
      ((Finset.range n).filter (fun k => a k < 0)).card <
        ((Finset.range n).filter (fun k => 0 < a k)).card
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/182510.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182510.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/182510.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/182510.lean)
- [A182510](https://oeis.org/A182510)
