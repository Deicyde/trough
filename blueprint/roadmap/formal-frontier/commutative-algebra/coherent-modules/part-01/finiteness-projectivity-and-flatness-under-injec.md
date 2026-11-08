---
declaration: theorem
origin: cited
lean: Module.Finite.iff_finite_tensorProduct_of_injective, Module.FinitePresentation.iff_finitePresentation_tensorProduct_of_injective, Module.finite_projective_of_tensorProduct_of_injective, Module.Flat.of_flat_tensorProduct_of_injective, Module.Flat.iff_flat_tensorProduct_of_injective
statement: formalized
proof: formalized
---

# Finiteness, projectivity and flatness under injective tensor units

Let R be a commutative ring, S an R-algebra and M an additive commutative monoid with its given R-module structure. Assume the canonical unit N → S ⊗[R] N is injective for every additive commutative R-semimodule N in Type (max uR uM). For a possibly noncommutative semiring S, S ⊗[R] M is finitely generated over S if and only if M is finitely generated over R. For a possibly noncommutative ring S, the corresponding finite-presentation equivalence holds. If S ⊗[R] M is finite and projective over any possibly noncommutative semiring S, M is finite and projective over R; finite presentation of M is derived internally. For a commutative ring S, flatness is likewise equivalent. All three carrier universes are independent; S need not be flat over R, and M needs neither an S-action nor a supplied additive group structure.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.Finite.iff_finite_tensorProduct_of_injective` (theorem), declared in [CoherentModules/RingTheory/Finiteness/Pure.lean, line 50](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Finiteness/Pure.lean#L50).
- `Module.FinitePresentation.iff_finitePresentation_tensorProduct_of_injective` (theorem), declared in [CoherentModules/RingTheory/Finiteness/Pure.lean, line 116](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Finiteness/Pure.lean#L116).
- `Module.finite_projective_of_tensorProduct_of_injective` (theorem), declared in [CoherentModules/LinearAlgebra/Projective/Pure.lean, line 40](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Projective/Pure.lean#L40).
- `Module.Flat.of_flat_tensorProduct_of_injective` (theorem), declared in [CoherentModules/RingTheory/Flat/Pure.lean, line 193](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Pure.lean#L193).
- `Module.Flat.iff_flat_tensorProduct_of_injective` (theorem), declared in [CoherentModules/RingTheory/Flat/Pure.lean, line 215](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Pure.lean#L215).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml)
- [Source of `Module.Finite.iff_finite_tensorProduct_of_injective` in CoherentModules/RingTheory/Finiteness/Pure.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Finiteness/Pure.lean#L50)
- [Source of `Module.FinitePresentation.iff_finitePresentation_tensorProduct_of_injective` in CoherentModules/RingTheory/Finiteness/Pure.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Finiteness/Pure.lean#L116)
- [Source of `Module.finite_projective_of_tensorProduct_of_injective` in CoherentModules/LinearAlgebra/Projective/Pure.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Projective/Pure.lean#L40)
- [Source of `Module.Flat.of_flat_tensorProduct_of_injective` in CoherentModules/RingTheory/Flat/Pure.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Pure.lean#L193)
- [Source of `Module.Flat.iff_flat_tensorProduct_of_injective` in CoherentModules/RingTheory/Flat/Pure.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Pure.lean#L215)
