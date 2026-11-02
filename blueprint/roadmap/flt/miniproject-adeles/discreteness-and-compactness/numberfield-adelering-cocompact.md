---
declaration: theorem
origin: cited
lean: NumberField.AdeleRing.cocompact
statement: formalized
---

# NumberField.AdeleRing.cocompact

The quotient $\mathbb{A}_K/K$ is compact.

## Depends on

- [Rat.AdeleRing.cocompact](rat-adelering-cocompact.md)
- [NumberField.AdeleRing.baseChangeEquiv](../base-change/part-03/numberfield-adelering-basechangeequiv.md)

## Proof

We proceed as in the discreteness proof above, by reducing to $\mathbb{Q}$. As before, choosing a $\mathbb{Q}$-basis of $K$ gives us $\mathbb{A}_K/K\cong(\mathbb{A}_{\mathbb{Q}}/\mathbb{Q})^n$ so the result follows from the previous theorem.

## Lean

Formalized as [`NumberField.AdeleRing.cocompact`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.cocompact).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 1031](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L1031)
