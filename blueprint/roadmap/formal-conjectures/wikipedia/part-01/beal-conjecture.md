---
declaration: theorem
origin: cited
lean: BealConjecture.beal_conjecture, BealConjecture.flt_of_beal_conjecture
statement: formalized
---

# Beal conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Beal_conjecture)

*Quoted from [FormalConjectures/Wikipedia/BealConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BealConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 textbook result.

## `BealConjecture.beal_conjecture`

Open: stated without proof.

> The **Beal Conjecture**: if we are given positive integers $A, B, C, x, y, z$ such that
> $x, y, z > 2$ and $A^x + B^y = C^z$ then $A, B, C$ have a common divisor.

```lean
theorem beal_conjecture : bealConjecture
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BealConjecture.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BealConjecture.lean#L39).

## `BealConjecture.flt_of_beal_conjecture`

Textbook result, proved here.

> The Beal Conjecture implies Fermat's last theorem

```lean
theorem flt_of_beal_conjecture (H : bealConjecture) :
    FermatLastTheorem
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/BealConjecture.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BealConjecture.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BealConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/BealConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Beal_conjecture)
