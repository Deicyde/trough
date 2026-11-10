---
declaration: theorem
origin: cited
lean: Module.FaithfullyFlat.annihilator_tensorProduct_eq
statement: formalized
proof: formalized
---

# Annihilator contraction under faithfully flat extension

Over a `CommRing R`,
[`Module.FaithfullyFlat.annihilator_tensorProduct_eq`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/TensorProduct.lean)
says tensoring an arbitrary `R`-module `M` with a faithfully flat module `P`
preserves its annihilator over `R`. Here `P` is only a module group, while `M`
needs only an additive commutative monoid structure. For a faithfully flat,
possibly noncommutative ring algebra `S`,
[`Module.comap_annihilator_tensorProduct_of_faithfullyFlat`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/BaseChange.lean)
identifies contraction of the annihilator of `S ⊗[R] M` with the original
annihilator. The tensor has its canonical left-factor action and `M` needs no
`S`-action. All three carrier universes are independent, with no finiteness,
flatness or faithfulness assumption on `M`. The
[module client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Flat/TensorProduct.lean) derives
preservation and reflection of faithful action over the coefficient ring;
this does not assert faithful action over a larger scalar algebra.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FaithfullyFlat.annihilator_tensorProduct_eq` (theorem), declared in [CoherentModules/RingTheory/Flat/TensorProduct.lean, line 47](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/TensorProduct.lean#L47).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FaithfullyFlat.annihilator_tensorProduct_eq` in CoherentModules/RingTheory/Flat/TensorProduct.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/TensorProduct.lean#L47)
