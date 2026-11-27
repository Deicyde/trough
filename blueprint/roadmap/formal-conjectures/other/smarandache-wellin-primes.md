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

*Quoted from [FormalConjectures/Other/SmarandacheWellinPrime.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Other/SmarandacheWellinPrime.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 10 test statements, counted here but not shown.

## `SmarandacheWellinPrime.conjecture`

Open: stated without proof.

> [Smarandache Problems](https://fs.unm.edu/S-PROBL.HTM) states: "There are infinitely many
> primes in the smarandache concatenated prime sequence."

```lean
theorem conjecture : {n : ℕ | (a n).Prime}.Infinite
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Other/SmarandacheWellinPrime.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Other/SmarandacheWellinPrime.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/SmarandacheWellinPrime.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Other/SmarandacheWellinPrime.lean)
- [Smarandache Problems](https://fs.unm.edu/S-PROBL.HTM)
