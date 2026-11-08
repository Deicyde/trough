---
declaration: def
origin: cited
lean: TrivSqZeroExt.opEquiv
statement: formalized
---

# Opposites of square-zero extensions

[`TrivSqZeroExt.opEquiv`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Opposite.lean)
identifies `(TrivSqZeroExt R M)ᵐᵒᵖ` with `TrivSqZeroExt Rᵐᵒᵖ M` by
`op (r, m) ↦ (op r, m)`. The target uses the original right action on the
left and the original left action pulled back by double `unop` on the right.
The equivalence needs only `Add R`, `Mul R`, `AddCommMagma M`, and the two
given scalar actions. For a division ring `D` and an `AddCommGroup M` with
commuting bimodule actions, the double-opposite module is
`Module.compHom M (RingEquiv.opOp D).symm.toRingHom`. The preceding left
criterion and coherence transport then give the right-coherence criterion
`IsCoherentRing ((TrivSqZeroExt D M)ᵐᵒᵖ) ↔ Module.Finite Dᵐᵒᵖ M`,
with finiteness measured using the original right action, without centrality
or a comparison of left and right dimensions.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TrivSqZeroExt.opEquiv` (def), declared in [CoherentModules/Algebra/TrivSqZeroExt/Opposite.lean, line 46](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Opposite.lean#L46).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `TrivSqZeroExt.opEquiv` in CoherentModules/Algebra/TrivSqZeroExt/Opposite.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Opposite.lean#L46)
