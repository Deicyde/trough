---
declaration: theorem
origin: cited
lean: OeisA100474.conjecture, OeisA100474.next_semiprime
statement: formalized
---

# Conjectures associated with A100474

> $a(1) = 1$; $a(n)$ is the smallest integer such that $a(n) + a(n-1)$ has the first $n$ distinct
> prime factors not used before in this construction.
>
> *References:*
> - [A100474](https://oeis.org/A100474)

*Quoted from [FormalConjectures/OEIS/100474.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100474.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 5 test statements and 9 API statements, counted here but not shown.

## `OeisA100474.conjecture`

Open: stated without proof.

> After $a(2) = 5$, is there another prime?

```lean
theorem conjecture : ∃ n > 2, (a n).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100474.lean, line 147](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100474.lean#L147).

## `OeisA100474.next_semiprime`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a100474-next-semiprime/blob/d7781751918e63fd1268b15525bf9554c92fdd4d/lean/OeisA100474NextSemiprimeFC.lean#L1285-L1288](https://github.com/KitaKen1/oeis-a100474-next-semiprime/blob/d7781751918e63fd1268b15525bf9554c92fdd4d/lean/OeisA100474NextSemiprimeFC.lean#L1285-L1288).

> What is the next semiprime in the sequence after $a(11)$?

```lean
theorem next_semiprime :
    next_semiprime.answer =
      a (sInf {n : ℕ | 11 < n ∧ (a n).IsSemiprime})
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/100474.lean, line 160](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100474.lean#L160).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/100474.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/100474.lean)
- [A100474](https://oeis.org/A100474)
