---
declaration: theorem
origin: cited
lean: BialgHom.faithfullyFlat_of_injective_of_isReduced
statement: formalized
proof: formalized
---

# Surjectivity and faithfully flat coordinates

For homomorphisms of
given affine group schemes locally of finite type, dominance over an
algebraically closed field implies surjectivity on all scheme points;
over any field, schematic dominance suffices. Over any field with reduced
target `H`, dominance or injectivity of the compatible coordinate map
`A → B` gives `Module.FaithfullyFlat A B` for its given algebra structure.
The coordinate presentations may have independent universes.
For finite-type commutative Hopf algebras over any field, an injective
morphism `f : A →ₐc[K] B` with reduced source coordinate algebra `A` satisfies
`f.toAlgHom.toRingHom.FaithfullyFlat`, by
[`BialgHom.faithfullyFlat_of_injective_of_isReduced`](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/FaithfullyFlat/Reduced.lean).
This uses the given Hopf structures, in independent scalar and carrier universes.
See [surjectivity over algebraically closed fields](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/GroupScheme/Surjective.lean),
[schematic dominance over fields](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/GroupScheme/SurjectiveBaseChange.lean), and
[faithful flatness of coordinates](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/GroupScheme/FaithfullyFlatCoordinates.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/README.md#headline-results) of [FormalFrontier/algebraic-groups](https://github.com/FormalFrontier/algebraic-groups) at commit [cad2dc41](https://github.com/FormalFrontier/algebraic-groups/tree/cad2dc41da14fb003738f0a032601dfa4d203453), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `BialgHom.faithfullyFlat_of_injective_of_isReduced` (theorem), declared in [AlgebraicGroups/Algebra/HopfAlgebra/FaithfullyFlat/Reduced.lean, line 50](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/FaithfullyFlat/Reduced.lean#L50).

Read from the source at commit [cad2dc41](https://github.com/FormalFrontier/algebraic-groups/tree/cad2dc41da14fb003738f0a032601dfa4d203453), without running Lean.

## Sources

- [algebraic-groups at cad2dc41: README, headline results](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/README.md#headline-results)
- [Source of `BialgHom.faithfullyFlat_of_injective_of_isReduced` in AlgebraicGroups/Algebra/HopfAlgebra/FaithfullyFlat/Reduced.lean](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/FaithfullyFlat/Reduced.lean#L50)
