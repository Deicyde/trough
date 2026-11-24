---
declaration: proposition
origin: cited
lean: HopfAlgebra.antipode_mul_antidistrib, HopfAlgebra.antipode_mul_distrib
statement: formalized
proof: formalized
---

# The antipode is a antihomomorphism

If $A$ is a $R$-Hopf algebra, then the antipode map $s : A \to A$ is anti-commutative, ie $s(a * b) = s(b) * s(a)$. If further $A$ is commutative, then $s(a * b) = s(a) * s(b)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Any standard reference will have a proof.

## Lean

Formalized as [`HopfAlgebra.antipode_mul_antidistrib`](https://yaeldillies.github.io/toric/docs/find/#doc/HopfAlgebra.antipode_mul_antidistrib), [`HopfAlgebra.antipode_mul_distrib`](https://yaeldillies.github.io/toric/docs/find/#doc/HopfAlgebra.antipode_mul_distrib).

## Sources

- [Toric varieties blueprint: chapters/2-3-hopf-algebras.tex, line 560](https://github.com/YaelDillies/toric/blob/97b1287db93f2eee84c8bb4e408058d9e721ce5b/blueprint/src/chapters/2-3-hopf-algebras.tex#L560)
