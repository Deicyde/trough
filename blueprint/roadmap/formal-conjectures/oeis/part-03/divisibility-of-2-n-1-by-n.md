---
declaration: theorem
origin: cited
lean: OeisA56777.a_of_comesFromPrimeQuadruple, OeisA56777.comesFromPrimeQuadruple_of_a, OeisA56777.mod_72_of_comesFromPrimeQuadruple, OeisA56777.mod_100_of_comesFromPrimeQuadruple
statement: formalized
---

# Divisibility of $2^n + 1$ by $n$

> A56777 lists composite numbers $n$ satisfying both $\varphi(n+12) = \varphi(n) + 12$ and
> $\sigma(n+12) = \sigma(n) + 12$.
>
> The conjectures state identities connecting A56777 and prime quadruples (A7530), as
> well as congruences satisfied by the members of A56777.
>
> *References:*
> - [A56777](https://oeis.org/A56777)

*Quoted from [FormalConjectures/OEIS/56777.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/56777.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 textbook results. It also has 3 test statements, counted here but not shown.

## `OeisA56777.a_of_comesFromPrimeQuadruple`

Textbook result, proved here.

> Numbers coming from prime quadruples are in the sequence A56777.

```lean
theorem a_of_comesFromPrimeQuadruple {n : ℕ} (h : ComesFromPrimeQuadruple n) : A n
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/56777.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/56777.lean#L75).

## `OeisA56777.comesFromPrimeQuadruple_of_a`

Open: stated without proof.

> All members of the sequence A56777 come from prime quadruples.

```lean
theorem comesFromPrimeQuadruple_of_a {n : ℕ} (h : A n) : ComesFromPrimeQuadruple n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/56777.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/56777.lean#L124).

## `OeisA56777.mod_72_of_comesFromPrimeQuadruple`

Textbook result, proved here.

> Numbers coming from prime quadruples satisfy $n \equiv 65 \pmod{72}$.

```lean
theorem mod_72_of_comesFromPrimeQuadruple {n : ℕ} (h : ComesFromPrimeQuadruple n) :
    n % 72 = 65
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/56777.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/56777.lean#L129).

## `OeisA56777.mod_100_of_comesFromPrimeQuadruple`

Textbook result, proved here.

> Numbers coming from prime quadruples satisfy $n \equiv 9 \pmod{100}$,
> except the first value "65".

```lean
theorem mod_100_of_comesFromPrimeQuadruple {n : ℕ} (h65 : 65 < n) (h : ComesFromPrimeQuadruple n) :
    n % 100 = 9
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/56777.lean, line 163](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/56777.lean#L163).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/56777.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/56777.lean)
- [A56777](https://oeis.org/A56777)
