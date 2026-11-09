---
declaration: theorem
origin: cited
lean: Green24.green_24, Green24.variants.upper_trivial, Green24.variants.upper_HL, Green24.variants.lower_HL, Green24.variants.conjecture
statement: formalized
---

# Green's Open Problem 24

> References:
> - [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.24)
> - [Aa19] Aaronson, James. "Maximising the number of solutions to a linear equation in a set of integers."
>   Bulletin of the London Mathematical Society 51.4 (2019): 577-594.
> - [HaL28] Hardy, G. H., and J. E. Littlewood. "Notes on the theory of series (VIII): an inequality."
>   Journal of the London Mathematical Society 1.2 (1928): 105-110.

*Quoted from [FormalConjectures/GreensOpenProblems/24.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/24.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Green24.green_24`

Open: stated without proof.

> If $A$ is a set of $n$ integers, what is the maximum number of affine translates of the set
> $\lbrace 0,1,3 \rbrace$ that $A$ can contain?
>
> Conjectured in [Aa19] p.579: $\left(\frac{1}{3} + o(1)\right) n^2$.

```lean
theorem green_24 : ∀ n, max013AffineTranslates n = green_24.answer n
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/24.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/24.lean#L58).

## `Green24.variants.upper_trivial`

Proved here.

> From [Aa19] p.577: the trivial upper bound is $n^2$ (non asymptotic).

```lean
theorem upper_trivial {n : ℕ} : max013AffineTranslates n ≤ n ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/24.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/24.lean#L68).

## `Green24.variants.upper_HL`

Solved: stated here without proof.

> Asymptotic upper bound (1.2) in [Aa19]. Named after Hardy and Littlewood [HaL28].

```lean
theorem upper_HL : gamma ≤ 3/4
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/24.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/24.lean#L82).

## `Green24.variants.lower_HL`

Solved: stated here without proof.

> Asymptotic lower bound (1.2) in [Aa19]. Named after Hardy and Littlewood [HaL28].

```lean
theorem lower_HL : gamma ≥ 1/12
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/24.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/24.lean#L87).

## `Green24.variants.conjecture`

Open: stated without proof.

> Conjecture p.579 in [Aa19]: $\left(\frac{1}{3} + o(1)\right) n^2$.

```lean
theorem conjecture : gamma = 1/3
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/24.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/24.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/24.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/24.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.24)
