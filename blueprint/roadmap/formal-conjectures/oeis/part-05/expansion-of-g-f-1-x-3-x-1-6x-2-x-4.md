---
declaration: theorem
origin: cited
lean: OeisA100434.a_even, OeisA100434.a_odd, OeisA100434.conjecture1, OeisA100434.conjecture2, OeisA100434.conjecture3
statement: formalized
---

# Expansion of g.f. $(1+x)(3+x)/(1+6x^2+x^4)$

> This sequence is defined by the linear recurrence relation
> $a(n) = -6 a(n-2) - a(n-4)$ for $n \ge 4$,
> with initial values $a(0)=3$, $a(1)=4$, $a(2)=-17$, $a(3)=-24$.
>
> *References:*
> - [A100434](https://oeis.org/A100434)

*Quoted from [FormalConjectures/OEIS/100434.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100434.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 solved and 2 textbook results. It also has 5 test statements, counted here but not shown.

## `OeisA100434.a_even`

Textbook result, proved here.

> For all $n \ge 0$, we have $a(2n) = - c(2n+1)$.

```lean
theorem a_even (n : ℕ) : a (2 * n) = - c (2 * n + 1)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100434.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100434.lean#L109).

## `OeisA100434.a_odd`

Textbook result, proved here.

> For all $n \ge 0$, we have $a(2n+1) = d(2n+1)$.

```lean
theorem a_odd (n : ℕ) : a (2 * n + 1) = d (2 * n + 1)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100434.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100434.lean#L134).

## `OeisA100434.conjecture1`

Solved: stated here; a Lean proof is at [https://github.com/chy4pro/formal-conjectures/blob/32f88077a444b83741f1db6734390eebd3678ecf/FormalConjectures/OEIS/100434.lean#L287](https://github.com/chy4pro/formal-conjectures/blob/32f88077a444b83741f1db6734390eebd3678ecf/FormalConjectures/OEIS/100434.lean#L287).

> **Conjecture from Creighton Dement (A100434)**:
> Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
> Then for all $n \ge 0$, $c(n) + d(n) = b(n)$.
>
> **Proof outline**:
> strong two-step induction on the paired recurrences. The even/odd cases are coupled
> through closed identities between consecutive terms of the relevant pair of sequences
> (here $c, d$), and the induction step is discharged by `rfl`-level unfolding of the definitions
> plus linear arithmetic. (Numerically verified for $n < 600$ before formalization.)

```lean
theorem conjecture1 (n : ℕ) : c n + d n = b n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100434.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100434.lean#L166).

## `OeisA100434.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/chy4pro/formal-conjectures/blob/32f88077a444b83741f1db6734390eebd3678ecf/FormalConjectures/OEIS/100434.lean#L306](https://github.com/chy4pro/formal-conjectures/blob/32f88077a444b83741f1db6734390eebd3678ecf/FormalConjectures/OEIS/100434.lean#L306).

> **Conjecture from Creighton Dement (A100434)**:
> Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
> Then for all $n \ge 0$, $e(n) + f(n) = b(n)$.
>
> **Proof outline**:
> strong two-step induction on the paired recurrences. The even/odd cases are coupled
> through closed identities between consecutive terms of the relevant pair of sequences
> (here $e, f$), and the induction step is discharged by `rfl`-level unfolding of the definitions
> plus linear arithmetic. (Numerically verified for $n < 600$ before formalization.)

```lean
theorem conjecture2 (n : ℕ) : e n + f n = b n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100434.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100434.lean#L183).

## `OeisA100434.conjecture3`

Solved: stated here; a Lean proof is at [https://github.com/chy4pro/formal-conjectures/blob/32f88077a444b83741f1db6734390eebd3678ecf/FormalConjectures/OEIS/100434.lean#L335](https://github.com/chy4pro/formal-conjectures/blob/32f88077a444b83741f1db6734390eebd3678ecf/FormalConjectures/OEIS/100434.lean#L335).

> **Conjecture from Creighton Dement (A100434)**:
> Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
> Then for all $n \ge 0$, $g(n) + a(n) = b(n)$.
>
> **Proof outline**:
> strong two-step induction on the paired recurrences. The even/odd cases are coupled
> through closed identities between consecutive terms of the relevant pair of sequences
> (here $g, a$), and the induction step is discharged by `rfl`-level unfolding of the definitions
> plus linear arithmetic. (Numerically verified for $n < 600$ before formalization.)

```lean
theorem conjecture3 (n : ℕ) : g n + a n = b n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100434.lean, line 200](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100434.lean#L200).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/100434.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100434.lean)
- [A100434](https://oeis.org/A100434)
