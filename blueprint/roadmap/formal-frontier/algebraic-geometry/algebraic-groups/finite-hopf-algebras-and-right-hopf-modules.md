---
declaration: theorem
origin: cited
lean: HopfAlgebra.exists_nondegenerate_mul, Coalgebra.RightComodule.coinvariantsTensorEquiv
statement: formalized
---

# Finite Hopf algebras and right Hopf modules

Every finite-dimensional Hopf algebra H over a field K admits a K-linear functional λ whose multiplication pairing (a, x) ↦ λ(a * x) is nondegenerate in both arguments. The Hopf algebra need not be commutative or cocommutative, and no restriction on the characteristic or assumption of antipode bijectivity is required. Over a commutative semiring, a specified right comodule over a possibly noncommutative semiring Hopf algebra with a given compatible right action and scalar tower is linearly equivalent to its coinvariants tensored with that Hopf algebra, without flatness or finiteness assumptions.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/formalization.yaml) of [FormalFrontier/algebraic-groups](https://github.com/FormalFrontier/algebraic-groups) at commit [cad2dc41](https://github.com/FormalFrontier/algebraic-groups/tree/cad2dc41da14fb003738f0a032601dfa4d203453), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `HopfAlgebra.exists_nondegenerate_mul` (theorem), declared in [AlgebraicGroups/Algebra/HopfAlgebra/Frobenius.lean, line 68](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/Frobenius.lean#L68).
- `Coalgebra.RightComodule.coinvariantsTensorEquiv` (def), declared in [AlgebraicGroups/Algebra/Coalgebra/RightComodule/HopfModule/Decomposition.lean, line 180](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/Coalgebra/RightComodule/HopfModule/Decomposition.lean#L180).

Read from the source at commit [cad2dc41](https://github.com/FormalFrontier/algebraic-groups/tree/cad2dc41da14fb003738f0a032601dfa4d203453), without running Lean.

## Sources

- [algebraic-groups at cad2dc41: formalization.yaml](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/formalization.yaml)
- [Source of `HopfAlgebra.exists_nondegenerate_mul` in AlgebraicGroups/Algebra/HopfAlgebra/Frobenius.lean](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/Frobenius.lean#L68)
- [Source of `Coalgebra.RightComodule.coinvariantsTensorEquiv` in AlgebraicGroups/Algebra/Coalgebra/RightComodule/HopfModule/Decomposition.lean](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/Coalgebra/RightComodule/HopfModule/Decomposition.lean#L180)
