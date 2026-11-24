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
- [NumberField.AdeleRing.baseChangeEquiv](../base-change/part-02/numberfield-adelering-basechangeequiv.md)

## Proof

We proceed as in the discreteness proof above, by reducing to $\mathbb{Q}$. As before, choosing a $\mathbb{Q}$-basis of $K$ gives us $\mathbb{A}_K/K\cong(\mathbb{A}_{\mathbb{Q}}/\mathbb{Q})^n$ so the result follows from the previous theorem.

## Lean

Stated as [`NumberField.AdeleRing.cocompact`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.cocompact); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 1031](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/AdeleMiniproject.tex#L1031)
