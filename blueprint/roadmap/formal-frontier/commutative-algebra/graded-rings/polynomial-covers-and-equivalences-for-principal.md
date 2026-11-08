---
declaration: def
origin: cited
lean: reesAlgebra.principalPolynomialHom
statement: formalized
---

# Polynomial covers and equivalences for principal ideals

For any
commutative ring `R` and `a : R`, evaluation at the class of `a t` defines a
surjective `R/(a)`-algebra map `(R/(a))[T] → C`, where `C` is the Rees algebra
modulo its coefficient ideal. If `a` is regular, this same map is an
`R/(a)`-algebra equivalence, including unit generators and the zero ring.
Composition with augmentation is evaluation at zero
([`reesAlgebra.principalPolynomialHom`](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/ReesAlgebra/PrincipalPolynomial.lean),
`surjective_principalPolynomialHom`,
`bijective_principalPolynomialHom`, `principalPolynomialEquiv`, and
`augmentation_comp_principalPolynomialEquiv`).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/README.md#headline-results) of [FormalFrontier/graded-rings](https://github.com/FormalFrontier/graded-rings) at commit [6a459e8e](https://github.com/FormalFrontier/graded-rings/tree/6a459e8e4d20392fe4f2a58191a621592f4788bb), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `reesAlgebra.principalPolynomialHom` (def), declared in [GradedRings/ReesAlgebra/PrincipalPolynomial.lean, line 31](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/ReesAlgebra/PrincipalPolynomial.lean#L31).

Read from the source at commit [6a459e8e](https://github.com/FormalFrontier/graded-rings/tree/6a459e8e4d20392fe4f2a58191a621592f4788bb), without running Lean.

## Sources

- [graded-rings at 6a459e8e: README, headline results](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/README.md#headline-results)
- [Source of `reesAlgebra.principalPolynomialHom` in GradedRings/ReesAlgebra/PrincipalPolynomial.lean](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/ReesAlgebra/PrincipalPolynomial.lean#L31)
