---
navigation: transparent
---

# Faithfully flat dependent… to Finite-type ideal/module…

- [Faithfully flat dependent direct sums](faithfully-flat-dependent-direct-sums.md)
- [Finitely generated ideals and dependent products](finitely-generated-ideals-and-dependent-products.md)
- [Faithful flatness after base change covering maximal ideals](faithful-flatness-after-base-change-covering-max.md)
- [Faithful flatness of unital algebras](faithful-flatness-of-unital-algebras.md)
- [Faithfully flat products of algebras](faithfully-flat-products-of-algebras.md)
- [Products of localizations at submonoids](products-of-localizations-at-submonoids.md)
- [Families of principal localizations](families-of-principal-localizations.md)
- [Faithfully flat coherence descent](faithfully-flat-coherence-descent.md)
- [Universal coherence](universal-coherence.md)
- [Associative square-zero multiplication](associative-square-zero-multiplication.md)
- [Commutativity of square-zero extensions](commutativity-of-square-zero-extensions.md)
- [Square-zero kernels and projection base change](square-zero-kernels-and-projection-base-change.md)
- [Full left-ideal lattice of square-zero extensions](full-left-ideal-lattice-of-square-zero-extension.md)
- [Module length and square-zero extensions](module-length-and-square-zero-extensions.md)
- [Coherent square-zero extensions](../part-01/coherence-of-square-zero-extensions-and-finite-s.md)
- [Opposites of square-zero extensions](opposites-of-square-zero-extensions.md)
- [Left Noetherian square-zero extensions](left-noetherian-square-zero-extensions.md)
- [Finite-type ideal/module transfer](finite-type-ideal-module-transfer.md)

The foundation, finite-presentation and coherent-module category results allow
arbitrary `Ring`. Coherent semilinear Hom allows arbitrary source and target
scalar `Semiring`s with a commuting `Ring` action on the target. Localization
of coherent modules and universal coherence use `CommRing`. Coherent tensor closure
uses a `CommRing` base but allows an independent, possibly noncommutative `Ring`
acting on the coherent factor.
The square-zero commutativity criterion uses only `Mul`, `AddZeroClass`,
`IsAddCommutative` and the two given `SMulZeroClass` actions. The square-zero
kernel and base-change results use `CommSemiring` and `AddCommMonoid`; the
full left-ideal classification uses `DivisionSemiring` and `AddCommGroup` with
both given commuting module actions. The square-zero Noetherian criterion allows
`Ring` and `AddCommMonoid` with commuting bimodule actions. The coherent-extension
sufficiency and injective-vector necessity use `Ring` and `AddCommGroup`, without
centrality. The finite-generation
biconditional uses an arbitrary division ring and the given compatible bimodule
with `AddCommGroup`; its canonical-field specialization gives finite dimensionality.
The predicate transfer uses `CommRing` and `AddCommGroup`.
The ideal/product identity and semilinear mono-flatness invariance use
`CommSemiring` and `AddCommMonoid`; the faithful-flatness criteria use `CommRing`
and require no coherence or projectivity assumption. Module carrier universes are independent where stated.
Zero rings/modules, empty indexing sets and rank-zero finite free
modules are not excluded. Consult the linked source statements and
[guide](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/docs/Guide.md) for exact hypotheses. This is not a coherent-sheaf theory
or a claim to formalize an entire source.
