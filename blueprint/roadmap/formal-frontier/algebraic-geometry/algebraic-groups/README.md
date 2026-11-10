# Algebraic groups

> Reusable Lean formalization of matrix point groups, finite algebraic group schemes and their coordinate algebras. The library covers unitriangular and upper-triangular groups, diagonal products, split kernels, closed unitriangular stages and their underlying affine-space presentations, finite additive products and positive-stage underlying projections and sections, unitriangular scalar base change and coherence, and selected dimension and geometric results. Coalgebra APIs include field subcoalgebras and finite-dimensional containment, right comodules and finitely generated subcomodule containment, coefficient matrix units, counit ranges and idempotent principal ideal constructors; split free presentations give finite tensor coordinates. Precise hypotheses and exclusions are documented in README.md and the focused mathematical guides. This is not a complete formalization of any cited source.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/formalization.yaml) of [FormalFrontier/algebraic-groups](https://github.com/FormalFrontier/algebraic-groups) at commit [cad2dc41](https://github.com/FormalFrontier/algebraic-groups/tree/cad2dc41da14fb003738f0a032601dfa4d203453), Apache-2.0.*

6 articles: 5 for highlights of its formalization.yaml whose declarations the scan finds and 1 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/algebraic-groups](https://github.com/FormalFrontier/algebraic-groups), read at commit [cad2dc41](https://github.com/FormalFrontier/algebraic-groups/tree/cad2dc41da14fb003738f0a032601dfa4d203453) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “AI-assisted development with independent agent review of individual contributions; no human mathematical review is claimed.”.
- Review notes: “Mathematical scope and third-party credit appear in README.md and CREDITS.md; this metadata does not assert complete source coverage.”
- Automation: agent; tool setup “Formal Frontier AI agents used Lean and Lake with pinned dependencies.”
- Automation notes: “AI agents developed mathematical proofs and ordinary-import clients.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Hopf Algebras*, Moss E. Sweedler, W. A. Benjamin, 1969 (book; background).
- *Algebraic Groups*, James S. Milne, 2017 edition (book; background).
- *Original algebraic-group and affine-localization constructions*, Formal Frontier Agents (original project proofs and earlier project research; adapts).

## Builds on

- [Coherent modules](../../commutative-algebra/coherent-modules/README.md) (a Lake dependency, pinned at 28c82dc8)
- [General linear groups](../../group-theory/general-linear-groups/README.md) (a Lake dependency, pinned at a9b20bb1)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 29001ecd)
- [Minimal primes](../../commutative-algebra/minimal-primes/README.md) (a Lake dependency, pinned at 44b23fb5)
- [Multivariate polynomials](../../commutative-algebra/multivariate-polynomials/README.md) (a Lake dependency, pinned at 58f7a9d7)
- [Projective modules](../../ring-theory/projective-modules/README.md) (a Lake dependency, pinned at 031aeecd)
- [Scheme properties](../scheme-properties/README.md) (a Lake dependency, pinned at 6391288b)
- [Smooth regularity](../../commutative-algebra/smooth-regularity/README.md) (a Lake dependency, pinned at 8e054f1f)

## Used by

- [Norm forms](../../number-theory/norm-forms/README.md)

## Highlights

- [Closed linear embeddings of affine algebraic groups](closed-linear-embeddings-of-affine-algebraic-gro.md)
- [Point representations and comodules](point-representations-and-comodules.md)
- [Finite-dimensional subcoalgebra containment](finite-dimensional-subcoalgebra-containment.md)
- [Finite Hopf algebras and right Hopf modules](finite-hopf-algebras-and-right-hopf-modules.md)
- [Bidual coactions and the antipode square](bidual-coactions-and-the-antipode-square.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/README.md#headline-results) of [FormalFrontier/algebraic-groups](https://github.com/FormalFrontier/algebraic-groups) at commit [cad2dc41](https://github.com/FormalFrontier/algebraic-groups/tree/cad2dc41da14fb003738f0a032601dfa4d203453), Apache-2.0.*

**Cartier's theorem.** Every commutative Hopf algebra over a characteristic-zero
field is reduced, and is smooth if it is finite type, for its given coefficient algebra
structure and with independent scalar and carrier universes. See
[Hopf algebra smoothness](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/Smooth.lean).

**Linear embeddings of affine algebraic groups.** Every affine group scheme
locally of finite type over a field `K` admits a group-scheme morphism
`G → GLₙ` for some `n : ℕ` whose underlying scheme morphism is a closed
immersion. No basis or representation is supplied, and nonreduced group
schemes are included.
See the [closed linear embedding theorem](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/GroupScheme/ComoduleGeneralLinear.lean).

- [Surjectivity and faithfully flat coordinates](surjectivity-and-faithfully-flat-coordinates.md)

**Hopf tensor–quotient equivalences.** For a central bialgebra map from a
commutative bialgebra `A` over a commutative ring `R` to a possibly
noncommutative Hopf algebra `B`, comultiplication gives a first-factor
`B`-linear equivalence `B ⊗[A] B ≃ₗ[B] B ⊗[R] (B / (ker ε_A)B)`.
In this generality the quotient is only a module quotient, and `A` need
not have an antipode. When `B` is commutative,
`HopfAlgebra.tensorQuotientAlgEquiv` refines the same map to a `B`-algebra
equivalence on the canonical tensor and quotient algebras. The simp equality
`tensorQuotientAlgEquiv_toLinearEquiv` recovers `tensorQuotientEquiv`, so its
finite-comultiplication formulas compute both directions. For a group-like
`c`, the inverse sends `(b c) ⊗ [c]` to `b ⊗ c`. Mixed scalar extension is
the composition of inverse tensor cancellation, congruence with this
refinement, and tensor cancellation. Compatible ordinary algebra maps
and scalar towers suffice; the commutative coefficient algebra needs no
Hopf structure.
See [`HopfAlgebra/TensorQuotient`](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/TensorQuotient.lean).

**Finite Hopf algebras and Hopf modules.** Every finite-dimensional Hopf
algebra over a field has a linear functional `λ` such that `λ (a * x)`
is nondegenerate in both arguments. Its left regular module is injective
(`HopfAlgebra.injective_self`). The algebra need not be commutative or
cocommutative, and the field may have any characteristic.
See [the Frobenius and self-injectivity theorems](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/HopfAlgebra/Frobenius.lean).
For decomposition over a commutative semiring `R`, let
`H` be a possibly noncommutative semiring with full Hopf algebra structure, and
`X` a specified right comodule on an additive-commutative-monoid `R`-module `M`.
For its given right action with `IsScalarTower R Hᵐᵒᵖ M`, an explicit
`hX : X.IsHopfModule` gives
`X.coinvariantsTensorEquiv hX : (X.weightSpace (1 : H)) ⊗[R] H ≃ₗ[R] M`.
The forward map is the given action. The inverse `X.toCoinvariantsTensor hX`
corestricts the antipode contraction to coinvariants before tensoring it with
`H` and composing with the coaction. Both inverse identities hold, including
the tensor-side identity inside coinvariants tensored with `H` itself. Both
maps intertwine the given right action with right multiplication on the `H`
factor. Universes are independent; no flatness, finiteness or inverse antipode
is required.
See [the decomposition and its API](https://github.com/FormalFrontier/algebraic-groups/blob/cad2dc41da14fb003738f0a032601dfa4d203453/AlgebraicGroups/Algebra/Coalgebra/RightComodule/HopfModule/Decomposition.lean).

## Main results

Its formalization.yaml lists 328 main results, and the scan finds 328 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
