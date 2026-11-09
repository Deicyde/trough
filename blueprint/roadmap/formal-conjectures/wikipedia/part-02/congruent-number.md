---
declaration: theorem
origin: cited
lean: CongruentNumber.not_congruentNumber_1, CongruentNumber.Tunnell_odd, CongruentNumber.Tunnell_even, CongruentNumber.Tunnell_odd_converse, CongruentNumber.Tunnell_even_converse
statement: formalized
---

# Congruent Number

> A natural number $n$ is called a congruent number if there exists a right triangle with rational
> sides $a$, $b$, and hypotenuse $c$ such that the area of the triangle is $\frac{1}{2}ab = n$.
>
> *References:*
> - [Wikipedia (Congruent number)](https://en.wikipedia.org/wiki/Congruent_number)
> - [Wikipedia (Tunnell's theorem)](https://en.wikipedia.org/wiki/Tunnell%27s_theorem)
> - [Keith Conrad's note](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/congnumber.pdf)

*Quoted from [FormalConjectures/Wikipedia/CongruentNumber.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CongruentNumber.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open, 2 solved and 1 textbook result. It also has 4 test statements, counted here but not shown.

## `CongruentNumber.not_congruentNumber_1`

Textbook result, stated without proof.

> 1 is not a congruent number, as proved by Fermat via infinite descent.

```lean
theorem not_congruentNumber_1 : ¬ congruentNumber 1
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CongruentNumber.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CongruentNumber.lean#L41).

## `CongruentNumber.Tunnell_odd`

Solved: stated here without proof.

> Tunnell's theorem (necessary condition) for odd squarefree congruent numbers.

```lean
theorem Tunnell_odd (n : ℕ) (hsqf : Squarefree n) (hodd : Odd n) :
    congruentNumber n → 2 * (A n).ncard = (B n).ncard
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CongruentNumber.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CongruentNumber.lean#L104).

## `CongruentNumber.Tunnell_even`

Solved: stated here without proof.

> Tunnell's theorem (necessary condition) for even squarefree congruent numbers.

```lean
theorem Tunnell_even (n : ℕ) (hsqf : Squarefree n) (heven : Even n) :
    congruentNumber n → 2 * (C n).ncard = (D n).ncard
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CongruentNumber.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CongruentNumber.lean#L110).

## `CongruentNumber.Tunnell_odd_converse`

Open: stated without proof.

> Tunnell's theorem (sufficient condition assuming BSD) for odd squarefree congruent numbers.

```lean
theorem Tunnell_odd_converse (n : ℕ) (hsqf : Squarefree n) (hodd : Odd n) :
    2 * (A n).ncard = (B n).ncard → congruentNumber n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CongruentNumber.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CongruentNumber.lean#L118).

## `CongruentNumber.Tunnell_even_converse`

Open: stated without proof.

> Tunnell's theorem (sufficient condition assuming BSD) for even squarefree congruent numbers.

```lean
theorem Tunnell_even_converse (n : ℕ) (hsqf : Squarefree n) (heven : Even n) :
    2 * (C n).ncard = (D n).ncard → congruentNumber n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/CongruentNumber.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CongruentNumber.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/CongruentNumber.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/CongruentNumber.lean)
- [Wikipedia (Congruent number)](https://en.wikipedia.org/wiki/Congruent_number)
