---
declaration: theorem
origin: cited
lean: Submodule.FG.ideal_smul_eq_self_iff_sup_annihilator_eq_top
statement: formalized
proof: formalized
---

# Ideal action on finite coefficients

For an FG submodule `N` of an arbitrary
additive commutative module over a `CommRing R`,
[`Submodule.FG.ideal_smul_eq_self_iff_sup_annihilator_eq_top`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Nakayama.lean)
says `I • N = N ↔ I ⊔ N.annihilator = ⊤` for every ideal `I`. For finite `P`,
[`Module.forall_maximal_smul_top_ne_top_iff_annihilator_le_jacobson`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Nakayama.lean)
characterizes proper image under every maximal ideal by
`Module.annihilator R P ≤ Ideal.jacobson ⊥`, with no flatness or faithful-action
assumption. The [clients](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Nakayama.lean) recover
relative Jacobson properness and supply the finite tensor-detection input.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Submodule.FG.ideal_smul_eq_self_iff_sup_annihilator_eq_top` (theorem), declared in [CoherentModules/RingTheory/Nakayama.lean, line 40](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Nakayama.lean#L40).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Submodule.FG.ideal_smul_eq_self_iff_sup_annihilator_eq_top` in CoherentModules/RingTheory/Nakayama.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Nakayama.lean#L40)
