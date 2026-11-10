---
declaration: instance
origin: cited
lean: Matrix.instIsCoherentRing
statement: formalized
---

# Coherence of finite matrix rings

For an arbitrary, possibly noncommutative
or zero `Ring R`, a finite type `I` with its given decidable equality, and the
canonical regular left modules,
[`Matrix.instIsCoherentRing`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/CoherentRing.lean)
gives coherence of `Matrix I I R` from coherence of `R`, including empty `I`.
For nonempty `I`, `IsCoherentRing.of_matrix` reflects coherence and
`Matrix.isCoherentRing_iff` gives the equivalence. The ring and index universes
are independent. The supporting
[`Matrix.entrywiseLinearMap`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/Entrywise.lean)
applies a coefficient-linear map `(κ → R) →ₗ[R] R` entrywise to a family of
matrices, linearly for regular left matrix multiplication, over any semiring
and arbitrary family index `κ`. Its scalar-restricted kernel has a split
entry projection onto the coefficient kernel. Reflection needs nonempty `I`:
the empty matrix ring has one element and is coherent for every `R`.
More generally, for any additive commutative monoid `M` with its given
`R`-module structure,
[`Matrix.Module.instIsCoherent`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/CoherentModule.lean)
preserves coherence under the canonical finite-sum action of `Matrix I I R`
on `I → M`, including empty `I`. For nonempty `I`,
`Module.IsCoherent.of_matrixModule` reflects coherence and
`Matrix.Module.isCoherent_iff` gives the equivalence with `Module.IsCoherent R M`.
No coherence of `R`, Noetherianity, or extra finite-generation premise is
required. The index, coefficient and module universes are independent, and
`R` may be zero. With empty `I`, every column module is a subsingleton and
hence coherent, so nonemptiness is essential for reflection.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Matrix.instIsCoherentRing` (instance), declared in [CoherentModules/LinearAlgebra/Matrix/CoherentRing.lean, line 48](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/CoherentRing.lean#L48).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Matrix.instIsCoherentRing` in CoherentModules/LinearAlgebra/Matrix/CoherentRing.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/CoherentRing.lean#L48)
