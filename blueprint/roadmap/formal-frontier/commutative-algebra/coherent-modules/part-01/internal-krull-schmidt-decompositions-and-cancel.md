---
declaration: theorem
origin: cited
lean: Submodule.exists_fin_isInternal_indecomposable_of_isNoetherian, Submodule.exists_fin_isInternal_indecomposable_of_isArtinian, DirectSum.IsInternal.exists_equiv_of_linearEquiv_of_isLocalRing_end, DirectSum.IsInternal.exists_equiv_of_linearEquiv_of_indecomposable_of_isFiniteLength, LinearEquiv.nonempty_of_prod_of_isFiniteLength
statement: formalized
proof: formalized
---

# Internal Krull–Schmidt decompositions and cancellation

Over any possibly noncommutative ring, a Noetherian module or an Artinian module is a finite internal direct sum of nonzero indecomposable submodules, with an explicit A i ≠ ⊥ fact paired with each summand's categorical indecomposability. Two supplied finite internal decompositions of linearly equivalent modules have matching summands up to linear equivalence when all summands have local endomorphism rings. Indecomposable summands and finite length of one total suffice instead. Both matching conclusions include explicit nonzero facts for each supplied family. Arbitrary finite index types use the caller's decidable equality instances and may be empty; existence uses stock equality on Fin n. Matching is existential; no preservation of the given coordinates or canonical choice is asserted. A common finite-length module P, possibly zero, cancels from P × M ≃ₗ[R] P × N with no chain condition on M or N. Zero modules, including those over a zero ring, have the empty decomposition.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Submodule.exists_fin_isInternal_indecomposable_of_isNoetherian` (theorem), declared in [CoherentModules/LinearAlgebra/KrullSchmidt.lean, line 122](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L122).
- `Submodule.exists_fin_isInternal_indecomposable_of_isArtinian` (theorem), declared in [CoherentModules/LinearAlgebra/KrullSchmidt.lean, line 139](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L139).
- `DirectSum.IsInternal.exists_equiv_of_linearEquiv_of_isLocalRing_end` (theorem), declared in [CoherentModules/LinearAlgebra/KrullSchmidt.lean, line 169](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L169).
- `DirectSum.IsInternal.exists_equiv_of_linearEquiv_of_indecomposable_of_isFiniteLength` (theorem), declared in [CoherentModules/LinearAlgebra/KrullSchmidt.lean, line 227](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L227).
- `LinearEquiv.nonempty_of_prod_of_isFiniteLength` (theorem), declared in [CoherentModules/LinearAlgebra/KrullSchmidt.lean, line 257](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L257).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml)
- [Source of `Submodule.exists_fin_isInternal_indecomposable_of_isNoetherian` in CoherentModules/LinearAlgebra/KrullSchmidt.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L122)
- [Source of `Submodule.exists_fin_isInternal_indecomposable_of_isArtinian` in CoherentModules/LinearAlgebra/KrullSchmidt.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L139)
- [Source of `DirectSum.IsInternal.exists_equiv_of_linearEquiv_of_isLocalRing_end` in CoherentModules/LinearAlgebra/KrullSchmidt.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L169)
- [Source of `DirectSum.IsInternal.exists_equiv_of_linearEquiv_of_indecomposable_of_isFiniteLength` in CoherentModules/LinearAlgebra/KrullSchmidt.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L227)
- [Source of `LinearEquiv.nonempty_of_prod_of_isFiniteLength` in CoherentModules/LinearAlgebra/KrullSchmidt.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/KrullSchmidt.lean#L257)
