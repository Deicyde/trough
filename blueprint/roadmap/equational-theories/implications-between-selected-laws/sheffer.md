---
declaration: theorem
origin: cited
lean: Sheffer.Equation345169_is_Boolean
statement: formalized
proof: formalized
---

# Sheffer stroke axiom

Definition [E345169](https://teorth.github.io/equational_theories/implications/?345169) $({x = (y \diamond ((x \diamond y) \diamond y)) \diamond (x \diamond (z \diamond y))})$ axiomatizes the Sheffer stroke operation $x \diamond y = \overline{xy}$ in a Boolean algebra.

## Depends on

- [Equation 345169](../selected-laws/part-03/equations-of-order-greater-than-4/eq345169.md)

## Proof

See \[mccune\_et\_al\]. In fact this is the shortest law with this property.

A sketch of proof follows. One can easily verify that the Sheffer stroke operation satisfies this law. Conversely, if this law holds, then automated theorem provers can show that the three Sheffer axioms

$$
(x \diamond x) \diamond (x \diamond x)  = x
$$

$$
x \diamond (y \diamond (y \diamond y)) = x \diamond x
$$

$$
(x \diamond (y \diamond z)) \diamond (x \diamond (y \diamond z)) = ((y \diamond y) \diamond x) \diamond ((z \diamond z) \diamond x)
$$

are satisfied. A classical result of Sheffer \[sheffer\] then allows one to conclude.

## Lean

Formalized as [`Sheffer.Equation345169_is_Boolean`](https://teorth.github.io/equational_theories/docs/find/#doc/Sheffer.Equation345169_is_Boolean).

## Sources

- [Equational Theories blueprint: chapter/implications.tex, line 170](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/implications.tex#L170)
