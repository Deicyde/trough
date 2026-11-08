---
navigation: transparent
---

# Coherence via kernels of maps… to Inverse images with nilpotent…

## Highlights

- [Coherence via kernels of maps from finite free modules](coherence-via-kernels-of-maps-from-finite-free-m.md)
- [Finiteness, projectivity and flatness under injective tensor units](finiteness-projectivity-and-flatness-under-injec.md)
- [Internal Krull–Schmidt decompositions and cancellation](internal-krull-schmidt-decompositions-and-cancel.md)
- [Coherence of square-zero extensions and finite-support idealizations](coherence-of-square-zero-extensions-and-finite-s.md)

## Headline results

**Spans, kernels and coordinate faces.** For a linear map of semimodules over
any possibly noncommutative semiring, if its target has no nonzero additive
summands of zero and has no zero scalar divisors, then
`span R S ⊓ ker f = span R (S ∩ ↑(ker f))` for every set `S`.
Intersecting a finitely generated submodule with this kernel remains finitely
generated. The [image-only corollaries](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Span/Kernel.lean)
require these two properties only on `range f`, without changing the kernel.
For an arbitrary coefficient module `A` with those properties and arbitrary
index and support sets, the [coordinate-face formulas](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Finsupp/Supported.lean)
give the same conclusions for `Finsupp.supported A R J`, using the given
`R`-action. The [polynomial example](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesExamples/PolynomialFaces.lean)
exhibits a nonzero proper face of a two-generated semimodule over `ℕ[X]`.
If `R` is zero-sum-free and has no zero divisors, every
[uniformly degree-bounded coefficient face](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Polynomial/CoefficientFace.lean)
of a finitely generated submodule of `I →₀ R[X]` is finitely generated over
`R`. The allowed coefficient positions may correlate the index and degree;
neither `I` nor the allowed set needs to be finite. The whole polynomial
submodule need not be finitely generated over `R`, and `R` need not be
commutative.

**Polynomial intertwining.** For an arbitrary semiring `S`, additive commutative
monoids `M`, `N`, and coefficient representations `σ : S →+* AddMonoid.End M`,
`τ : S →+* AddMonoid.End N`, an additive map `h : M →+ N` that intertwines
every `σ s` with `τ s` and the selected endomorphisms `f` with `g` also
intertwines their plain polynomial evaluations. The
[semilinear version](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/LinearMap/Evaluation.lean)
uses the given module structures over independent semirings `R`, `R₂`, any
scalar homomorphism `η : R →+* R₂`, an `η`-semilinear map `h`, and representations
into the respective linear endomorphism semirings. The hypotheses
`(τ s).comp h = h.comp (σ s)` for every `s` and `g.comp h = h.comp f` imply
`(p.eval₂ τ g).comp h = h.comp (p.eval₂ σ f)`. All five carrier universes
are independent. No coefficient/end commutation, finiteness, or module
structure on the semilinear Hom is required.

**Stable kernels and ranges.** For an additive commutative group with its given
module structure over a possibly zero, noncommutative semiring, simultaneous
one-step stability at a natural bound, including zero, gives the specified
sum equivalence from the power kernel and range. The kernel restriction is
nilpotent and the range restriction is an automorphism. Canonical projections
are independent of the stable bound and natural for arbitrary linear
intertwiners. Noetherianity and Artinianity of the module give a common bound;
the separate Noetherian-surjective and Artinian-injective automorphism
criteria retain their asymmetric hypotheses. See
[`StableKernelRange`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/End/StableKernelRange.lean).
Over arbitrary ring scalars, a finite-length module that is categorically
indecomposable has a local endomorphism ring, and each endomorphism is
nilpotent or a unit. The indecomposable predicate already excludes the zero
module; see [`Local`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/End/Local.lean).
The classical ring-module antecedents are Fitting's lemma and its
indecomposable finite-length local-endomorphism consequence, as presented in
Wisbauer, *Foundations of Module and Ring Theory*, §§31.13 and 32.4(3)(iii).
The explicit-one-step semiring/additive-group decomposition above generalizes
the cited ring-module setting; the local-endomorphism theorem retains ring
scalars. See [references and credit](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#references-and-credit).

**Internal Krull–Schmidt decompositions and cancellation.** Over any ring, a
Noetherian module or an Artinian module is a finite internal direct sum of
nonzero indecomposable submodules; the two chain conditions are separate
existence hypotheses. Each existence witness includes `A i ≠ ⊥` alongside
categorical indecomposability. Two supplied finite internal decompositions of
linearly equivalent modules match up to an equivalence of index types and
linear equivalences of summands when all summands have local endomorphism
rings. Indecomposable summands and finite length of one total give the same
matching. Both matching conclusions include `∀ i, A i ≠ ⊥` and
`∀ j, B j ≠ ⊥`, derived from the given hypotheses. Arbitrary finite index
types use the caller's decidable equality instances and may be empty;
existence uses the stock equality instance on `Fin n`. The matching is
existential, not required to preserve the given coordinates. A common
finite-length module `P` cancels from `P × M ≃ₗ[R] P × N`, with no chain
condition on `M` or `N`; `P` may be zero. Zero modules, including those over
a zero ring, have the empty decomposition. See
[`KrullSchmidt`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean), which realizes
the categorical theorems of Homological Algebra through `ModuleCat`.

- [Additive intertwining by ranges](additive-intertwining-by-ranges.md)
- [Fibrewise additive intertwining](fibrewise-additive-intertwining.md)
- [Finite coarsening of complete orthogonal idempotents](finite-coarsening-of-complete-orthogonal-idempot.md)
- [Dual endomorphisms](dual-endomorphisms.md)
- [Tensor–dual Frobenius criterion](tensor-dual-frobenius-criterion.md)
- [Annihilator quotients with two scalar actions](annihilator-quotients-with-two-scalar-actions.md)
- [Noetherian semilinear Hom](noetherian-semilinear-hom.md)
- [Hom and End of matrix columns](hom-and-end-of-matrix-columns.md)
- [Projective matrix-column semimodules](projective-matrix-column-semimodules.md)
- [Left ideals of finite matrix semirings](left-ideals-of-finite-matrix-semirings.md)
- [Coherence of finite matrix rings](coherence-of-finite-matrix-rings.md)
- [Left-regular elements in left Artinian rings](left-regular-elements-in-left-artinian-rings.md)
- [Closed semimodule categories](closed-semimodule-categories.md)
- [Kernels over semirings](kernels-over-semirings.md)
- [Sums of nilpotent left ideals](sums-of-nilpotent-left-ideals.md)
- [Inverse images with nilpotent kernel](inverse-images-with-nilpotent-kernel.md)
