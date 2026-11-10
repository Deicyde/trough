---
declaration: theorem
origin: cited
lean: OeisA108306.a_is_invert_transform_case, OeisA108306.conjecture
statement: formalized
---

# A108306: Expansion of $(3x+1)/(1-3x-3x^2)$

> This sequence satisfies the linear recurrence relation $a(0)=1$, $a(1)=6$,
> and $a(n) = 3a(n-1) + 3a(n-2)$ for $n \ge 2$.
>
> *References:*
> - [A108306](https://oeis.org/A108306)

*Quoted from [FormalConjectures/OEIS/108306.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108306.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 solved and 1 textbook result. It also has 5 test statements, counted here but not shown.

## `OeisA108306.a_is_invert_transform_case`

Textbook result, proved here.

> The sequence is the INVERT transform of (1, 5, 10, 20, 40, 80, 160, ...) and can be obtained
> by extracting the upper left terms of matrix powers of [(1,5); (1,2)].
> These results are a case (a=5, b=2) of the general conjecture below.

```lean
theorem a_is_invert_transform_case (n : ℕ) :
    a n = (m ^ (n + 1)) 0 0
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108306.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108306.lean#L76).

## `OeisA108306.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-108306/blob/2e01e81b20a56880993e174ee4af0f0d7af37bdd/lean/OeisA108306FC.lean#L101-L106](https://github.com/KitaKen1/oeis-108306/blob/2e01e81b20a56880993e174ee4af0f0d7af37bdd/lean/OeisA108306FC.lean#L101-L106).

> The conjecture: The INVERT transform of a sequence starting
> $(1, a, ab, ab^2, ab^3, \ldots)$ is equivalent to extracting the upper left terms
> of powers of the 2x2 matrix [(1,a); (1,b)].

```lean
theorem conjecture (a_val b_val n : ℕ) :
    invertSeqD a_val b_val n = (genMatrix a_val b_val ^ n) 0 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108306.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108306.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108306.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108306.lean)
- [A108306](https://oeis.org/A108306)
