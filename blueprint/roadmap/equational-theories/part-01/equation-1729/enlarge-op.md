---
declaration: proposition
origin: cited
lean: Eq1729.enlarge_op
statement: formalized
proof: formalized
---

# Enlarging $\diamond$

Suppose one has a partial solution in which $x \diamond' y$ is undefined for some $x,y \in N$. Then one can extend the partial solution so that $x \diamond' y$ is now defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Enlarging $S'$](enlarge-s.md)

## Proof

By applying [Enlarging $S'$](enlarge-s.md) as needed, we may assume without loss of generality that $S'x$ and $S'y$ are already defined (among other things, this removes the possibility that $x \diamond' y$ is part of a pending identity). If this makes $x \diamond' y$ defined, then we are done, so we may assume that this is not the case.

Similarly, by using [Enlarging $L'_0$](enlarge-l0.md), we may assume without loss of generality that $L'_0 R'_0 R'_{S'x} y$ is defined.

We now divide into cases:

Case 1: $x=y$. In this case we set $x \diamond' y := S'x$. It is clear that this preserves axiom (v”), and no other axiom is impacted.

Case 2: If $x = R'_a y$ for some $a \in SM$, then we set $x \diamond' y := a - S'y$. This preserves axiom (vi”), and no other axiom is impacted.

Case 3: If $x$ is not equal to $y$ or $R'_a y$ for any $a \in SM$. Let $d_0 \in SM$ be a generator that does not appear as a component of any index of any of the generators $e_a$ appearing anywhere in the partial solution. We set $x \diamond' y := z$ with $z := e^2_{d_0}$.

This temporarily disrupts axiom (vii”). To recover it, we perform the following actions.

- Set $x' \diamond' y' = z'$, where $(x',y',z') := (z, x, (R'_{2S'x})^{-1} L_0 R'_0 R'_{Sx} y)$.
- Add $I[x',y',z']$ as a pending identity.

One can check that these definitions do not cause any collisions in the partial function $L'_0$, and that axioms (i'), (vii'), (P), (P') are preserved; the remaining axioms (S), (iii”), (iv”), (v”), (vi”) are unaffected by this extension.

## Lean

Formalized as [`Eq1729.enlarge_op`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.enlarge_op).

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 274](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1729.tex#L274)
