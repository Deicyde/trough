---
declaration: proposition
origin: cited
lean: Eq1729.enlarge_S'_induction_with_axioms
statement: formalized
proof: formalized
---

# Enlarging $S'$ with induction hypothesis and axioms

Suppose one has a partial solution in which $S'x$ is undefined for some $x \in N$, but $S'y$ is defined for all $y < x$. (This hypothesis is vacuous for $x=1$.) Let $y_0$ be the parent of $x$ (if $x \neq 1$), and assume the following additional axioms:

- (A) If $R'_a x = y_0$ for some $a \in SM$, then $L'_0 R'_{S' y_0} x$ is defined.
- (B) If $x = R'_a y_0$ for some $a \in SM$, then $L'_0 R'_{2(a-S'y_0)} x$ is defined.
- (C) If $I[x,y,z]$ for some $y,z \in N$, and $S'z$ is defined, then $L'_0 R'_0 R'_{S'z} x$ is defined.

Then one can extend the partial solution so that $S'x$ is now defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $d_0, d_1 \in SM$ be generators $E_{n_0}$ of $SM$ that do not appear in the index $a$ of any $e_a$ that currently appears in the partial solution (of which there are only finitely many). We also set some further distinct generators $d'_{y,z} \in SM$ for $y,z \in SM$ that are distinct from each other and all previous generators (this is possible as we have infinitely many generators). We set $S'x, x \diamond' x := d_0$; this preserves axiom (S) and (v”). We set

$$
L'_0 R'_{2d_0} x := e_{d_1}
$$

$$
L'_0 R'_{2d_0} (R'_{d_0})^{-1} e_{d_1} := R'_{d_0} x
$$

and then extend these choices using itero, itero-2 to recover axiom (i'), thus for instance

$$
L'_0 (R'_0)^n R'_{2d_0} x := (R'_0)^n e_{d_1}
$$

and

$$
L'_0 (R'_0)^n e_{d_1}  := (R'_0)^{n-1} R'_{2d_0} x
$$

for all $n \in \mathbb{Z}$.

To retain axiom (iii”), we perform the following actions:

- If $y_0$ is undefined, do nothing.
- If $R'_a x = y_0$ for some $a \in SM$ (so that $L'_0 R'_{S'y_0} x$ is defined, by hypothesis (A)), set $L'_0 R'_{2(a-d_0)} y_0 := R'_{a-d_0} (R'_{2S'y_0})^{-1} R'_0 L'_0 R'_{S'y_0} x$. Then extend using itero, itero-2.
- If $x = R'_a y_0$ for some $a \in SM$ (so that $L'_0 R'_{2(a-Sy_0)} x$ is already defined, by hypothesis (B)), set $L'_0 R'_{2d_0} (R'_{a-S'y_0})^{-1} L'_0 R'_{2(a-Sy_0)} x :=R'_{d_0} y_0$, and extend using itero, itero-2.

To retain axiom (P), we perform the following actions for each pending identity of the form $I[x,y,z]$ for some $y,z$, executed in some arbitrary order.

- Remove this identity $I[x,y,z]$ from the list of pending identities.
- Set $L'_0 R'_0 R'_{d_0} y := e_{d'_{y,z}}$, and $x' \diamond y' := z'$, where $(x',y',z') := (z, x, (R'_{2d_0})^{-1} e_{d'_{y,z}})$. Extend all the new definitions of $L'_0$ using itero, itero-2.
- If $S'x'$ is undefined, add $I[x',y',z']$ as a pending identity.
- If instead $S'x'$ is defined (which makes $L'_0 R'_0 R'_{S'x'} y'$ defined, by axiom (C)), set $x'' \diamond y'' = z''$, where $(x'',y'',z'') := (z', x', (R'_{2S'x'})^{-1} L'_0 R'_0 R'_{S'x'} y')$. Then add $I[x'',y'',z'']$ as a pending identity.

One can check that these definitions do not cause any collisions in the partial function $L'_0$, and that axioms (i'), (iii'), (iv”), (v”), (vii”), (P), (P'), (P”) are preserved; the remaining axiom (vi”) is unaffected by this extension. Axiom (L) can also be shown to be preserved after a tedious calculation.

## Lean

Formalized as [`Eq1729.enlarge_S'_induction_with_axioms`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.enlarge_S'_induction_with_axioms).

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 218](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1729.tex#L218)
