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

Its statement uses no other node that has an article here.

## Proof

See ([McCune et al. 2002](https://doi.org/10.1023/A:1020542009983)). In fact this is the shortest law with this property.

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

are satisfied. A classical result of Sheffer ([Sheffer 1913](https://doi.org/10.2307/1988701)) then allows one to conclude.

## Lean

Formalized as [`Sheffer.Equation345169_is_Boolean`](https://teorth.github.io/equational_theories/docs/find/#doc/Sheffer.Equation345169_is_Boolean).

## Sources

- [Equational Theories blueprint: chapter/implications.tex, line 170](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/implications.tex#L170)
