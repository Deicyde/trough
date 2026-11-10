---
declaration: theorem
origin: cited
lean: Green64.green_64, Green64.green_64.variants.p_sub_one
statement: formalized
---

# Green's Open Problem 64

> *Reference:* [Ben Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.64)
>
> Do there exist infinitely many primes $p$ for which $p - 2$ has an odd number of prime factors,
> counted with multiplicity?

*Quoted from [FormalConjectures/GreensOpenProblems/64.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/64.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 3 test statements, counted here but not shown.

## `Green64.green_64`

Open: stated without proof.

> Do there exist infinitely many primes $p$ for which $p - 2$ has an odd number of prime factors,
> counted with multiplicity (i.e. $\Omega(p - 2)$ is odd)?

```lean
theorem green_64 :
    {p : ℕ | p.Prime ∧ Odd (Ω (p - 2))}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/64.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/64.lean#L42).

## `Green64.green_64.variants.p_sub_one`

Open: stated without proof.

> The same question as `green_64` but with $p - 1$ instead of $p - 2$.
> Green notes this is "probably more natural".

```lean
theorem green_64.variants.p_sub_one :
    {p : ℕ | p.Prime ∧ Odd (Ω (p - 1))}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/64.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/64.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/64.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/64.lean)
- [Ben Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.64)
