---
declaration: theorem
origin: cited
lean: Module.FaithfullyFlat.iff_flat_and_baseChange_of_map_maximal_ne_top
statement: formalized
proof: formalized
---

# Faithful flatness after base change covering maximal ideals

For commutative
rings `R` and `S` with an `R`-algebra structure on `S`, suppose every maximal
ideal `m` of `R` satisfies `m.map (algebraMap R S) ≠ ⊤`. For any additive
commutative group `M` with an `R`-module structure,
[`Module.FaithfullyFlat.iff_flat_and_baseChange_of_map_maximal_ne_top`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/FaithfullyFlat.lean)
characterizes faithful flatness over `R` by **original** flatness `Module.Flat R M`
and faithful flatness over `S` of `S ⊗[R] M`, with the canonical left tensor-factor
action. The three universes are independent. No flatness of `S` over `R`,
surjectivity, algebra structure on `M`, finiteness, Noetherianity, localness,
topology or completion is assumed. For `I ≤ Ideal.jacobson (⊥ : Ideal R)`,
[`Module.FaithfullyFlat.iff_flat_and_baseChange_of_le_jacobson`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/FaithfullyFlat.lean)
specializes this to the canonical quotient `R ⧸ I`. For commutative
`R`-algebras `S`,
[`Module.FaithfullyFlat.iff_flat_and_quotient_of_le_jacobson`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/FaithfullyFlat.lean)
gives the equivalent formulation using the canonical quotient algebra
`R ⧸ I → S ⧸ I.map (algebraMap R S)`. Conversely,
[`Algebra.map_maximal_ne_top_iff_forall_faithfullyFlat_baseChange`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/BaseChange.lean)
characterizes the maximal-ideal hypothesis itself: it holds **if and only if**
scalar extension preserves and reflects faithful flatness for every originally
flat `R`-module in `Type (max u w)`, where `R : Type u` and `w` is arbitrary.
The universe of `S` remains independent. The converse uses the direct sum of
principal localizations indexed by all elements of a maximal ideal, without
assuming that ideal is finitely generated. The
[quotient client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Flat/FaithfullyFlat.lean)
applies this corollary to the nonsurjective rank-two diagonal over `ZMod 4`
with the proper nonzero square-zero ideal `(2)`. Its inputs are obtained
independently from basis-derived faithful flatness.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FaithfullyFlat.iff_flat_and_baseChange_of_map_maximal_ne_top` (theorem), declared in [CoherentModules/RingTheory/Flat/FaithfullyFlat.lean, line 159](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/FaithfullyFlat.lean#L159).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FaithfullyFlat.iff_flat_and_baseChange_of_map_maximal_ne_top` in CoherentModules/RingTheory/Flat/FaithfullyFlat.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/FaithfullyFlat.lean#L159)
