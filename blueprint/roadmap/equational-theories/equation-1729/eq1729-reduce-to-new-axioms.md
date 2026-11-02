---
declaration: lemma
origin: cited
---

# Reduction to new axioms

Suppose we can find a function $S': N \to SM$, a bijection $L'_0: N \to N$, and an operation $\diamond': N \times N \to SM \uplus N$ satisfying axioms (i'), (iii'), (iv'), (v), (vi'), (vii'). Then there exists a magma satisfying 1729 but not 817.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Using $L'_0$ to construct $L'_a$](l0-la.md)
- [Basic properties of $R'_a$](ra-prop.md)
- [Extending a 1729 magma](mag.md)

## Proof

Construct the $L'_a$ using [Using $L'_0$ to construct $L'_a$](l0-la.md). By [Basic properties of $R'_a$](ra-prop.md) and direct verification we can noe verify axioms (i)-(vii), and then the claim follows from [Extending a 1729 magma](mag.md).

## Lean

The blueprint marks this formalized but names no Lean declaration.

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 134](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1729.tex#L134)
