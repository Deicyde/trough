---
declaration: theorem
origin: cited
lean: SmarandacheWellinPrime.conjecture
statement: formalized
---

# Smarandache–Wellin primes

> The Smarandache–Wellin numbers are formed by concatenating the decimal expansions of the
> successive primes: $2, 23, 235, 2357, \ldots$. It is conjectured that infinitely many members of
> this sequence are prime.
>
> *References:*
> * [Smarandache Problems](https://fs.unm.edu/S-PROBL.HTM)
> * [OEIS A019518](https://oeis.org/A019518)
> * [OEIS A069151](https://oeis.org/A069151)
> * [OEIS A046035](https://oeis.org/A046035)

*Quoted from [FormalConjectures/Other/SmarandacheWellinPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SmarandacheWellinPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 10 test statements, counted here but not shown.

## `SmarandacheWellinPrime.conjecture`

Open: stated without proof.

> [Smarandache Problems](https://fs.unm.edu/S-PROBL.HTM) states: "There are infinitely many
> primes in the smarandache concatenated prime sequence."

```lean
theorem conjecture : {n : ℕ | (a n).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Other/SmarandacheWellinPrime.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SmarandacheWellinPrime.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/SmarandacheWellinPrime.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SmarandacheWellinPrime.lean)
- [Smarandache Problems](https://fs.unm.edu/S-PROBL.HTM)
