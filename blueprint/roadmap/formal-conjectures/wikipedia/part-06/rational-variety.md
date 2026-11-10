---
declaration: theorem
origin: cited
lean: NoetherProblem.noether_problem, NoetherProblem.noether_problem.variants.two, NoetherProblem.noether_problem.variants.three, NoetherProblem.noether_problem.variants.four, NoetherProblem.noether_problem.variants.forty_seven
statement: formalized
---

# Rational_variety

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Rational_variety)

*Quoted from [FormalConjectures/Wikipedia/NoetherProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/NoetherProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 solved. It also has 1 test statement, counted here but not shown.

## `NoetherProblem.noether_problem`

Solved: stated here without proof.

> The **Noether Problem**: let `L` be the field of rational functions in `n`
> indeterminates over `K`, and let `G` be a finite group permuting these indeterminates.
> Is the fixed field `L^G` a rational extension of `K`, i.e. does `L/K` have the Noether property?
>
> Solution: False.

```lean
theorem noether_problem : ¬ ∀ (K L ι : Type)
    [Field K] [Field L] [Fintype ι] [Algebra K L] [IsRationalExtension K L ι],
    HasNoetherProperty K L ι
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/NoetherProblem.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/NoetherProblem.lean#L73).

## `NoetherProblem.noether_problem.variants.two`

Solved: stated here without proof.

> The Noether problem has a positive solution for groups permuting two indeterminates.

```lean
theorem noether_problem.variants.two {K L ι : Type}
    [Field K] [Field L] [Fintype ι] [Algebra K L]
    [IsRationalExtension K L ι] (hι : Fintype.card ι = 2) :
    HasNoetherProperty K L ι
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/NoetherProblem.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/NoetherProblem.lean#L82).

## `NoetherProblem.noether_problem.variants.three`

Solved: stated here without proof.

> The Noether problem has a positive solution for groups permuting three indeterminates.

```lean
theorem noether_problem.variants.three {K L ι : Type}
    [Field K] [Field L] [Fintype ι] [Algebra K L]
    [IsRationalExtension K L ι] (hι : Fintype.card ι = 3) :
    HasNoetherProperty K L ι
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/NoetherProblem.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/NoetherProblem.lean#L92).

## `NoetherProblem.noether_problem.variants.four`

Solved: stated here without proof.

> The Noether problem has a positive solution for groups permuting four indeterminates.

```lean
theorem noether_problem.variants.four {K L ι : Type}
    [Field K] [Field L] [Fintype ι] [Algebra K L]
    [IsRationalExtension K L ι] (hι : Fintype.card ι = 4) :
    HasNoetherProperty K L ι
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/NoetherProblem.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/NoetherProblem.lean#L102).

## `NoetherProblem.noether_problem.variants.forty_seven`

Solved: stated here without proof.

> One can find a counterexample to the Noether Problem's claim by considering a
> group permuting the 47 indeterminates of a rational function field.

```lean
theorem noether_problem.variants.forty_seven :
    ∃ (K L ι : Type)
    (_ :  Field K) (_ : Field L) (_ : Fintype ι) (_ : Algebra K L)
    (_ : IsRationalExtension K L ι),
    Fintype.card ι = 47 ∧ ¬ HasNoetherProperty K L ι
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/NoetherProblem.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/NoetherProblem.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/NoetherProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/NoetherProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Rational_variety)
