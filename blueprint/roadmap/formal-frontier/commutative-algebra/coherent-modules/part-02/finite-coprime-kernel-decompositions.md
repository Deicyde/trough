---
declaration: def
origin: cited
lean: RingHom.linearEquivPiKer
statement: formalized
---

# Finite coprime-kernel decompositions

Let a commutative semiring `A` act through
a representation `τ : A →+* Module.End R M`, where `R` is any semiring and `M` is
an additive commutative `R`-semimodule. For a finite labelled pairwise Bézout-coprime
family `a`, the sole annihilation premise `τ (∏ i, a i) = 0` gives
[`RingHom.linearEquivPiKer`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/Coprime/Kernel.lean),
an explicit equivalence with the product of the labelled kernels. Its inverse sums
the kernel inclusions, and its projectors are independent of the whole Bézout
partition used to compute them. Empty families, zero semirings and noncommutative
scalar semirings are allowed; no subtraction or additive cancellation is needed.
Polynomial evaluation and scalar torsion decompositions are specializations.
Given a second such decomposition from `υ : B →+* Module.End T N` and a finite
family `b : J → B`, an arbitrary map `q : I → J` regroups the fine labels. An
additive map `h : M →+ N` intertwining each represented fibre-product
`τ (∏ i with q i = j, a i)` with `υ (b j)` intertwines the corresponding sum of
fine canonical projectors with the target projector; each target coordinate is
the fibre-sum of mapped fine coordinates. Empty fibres are allowed. The
coefficient and scalar semirings may differ; neither scalar-linearity nor
compatibility with other represented elements is required. Same-label
naturality is the specialization `q = id`.
The exact projector criterion is
[`RingHom.semiconj_sum_kerProjector_iff_mapsTo_ker`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/Coprime/Kernel.lean):
`h` intertwines all fibre-sums of fine projectors with the target projectors if
and only if it maps `ker (τ (a i))` into `ker (υ (b (q i)))` for every `i`.
This criterion requires no scalar-linearity or intertwining of represented
elements; its only annihilation premises are that both represented products
vanish. The eight coefficient, scalar, module and index universes are
independent. Both label sets are finite here because the canonical families
are finite.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `RingHom.linearEquivPiKer` (def), declared in [CoherentModules/Algebra/Module/Coprime/Kernel.lean, line 188](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/Coprime/Kernel.lean#L188).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `RingHom.linearEquivPiKer` in CoherentModules/Algebra/Module/Coprime/Kernel.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/Coprime/Kernel.lean#L188)
