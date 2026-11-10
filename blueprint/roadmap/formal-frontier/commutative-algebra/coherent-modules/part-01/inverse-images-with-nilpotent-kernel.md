---
declaration: theorem
origin: cited
lean: Ideal.pow_comap_eq_zero_of_ker_pow_eq_zero
statement: formalized
proof: formalized
---

# Inverse images with nilpotent kernel

For a unital semiring homomorphism `f`
and a target left ideal `J`,
[`Ideal.pow_comap_eq_zero_of_ker_pow_eq_zero`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Comap.lean)
gives `J.comap f ^ (m * n) = 0` from the global witnesses `J ^ m = 0` and
`(RingHom.ker f) ^ n = 0`. The companion `Ideal.isNilpotent_comap` gives global
nilpotence of the inverse image. Both semirings may be noncommutative, all natural
exponents including zero are allowed, and the source, target and generic
`RingHomClass` homomorphism family have independent universes. The same module
gives product and power inclusions for inverse images without nilpotence hypotheses.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.pow_comap_eq_zero_of_ker_pow_eq_zero` (theorem), declared in [CoherentModules/RingTheory/Ideal/Comap.lean, line 59](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Comap.lean#L59).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.pow_comap_eq_zero_of_ker_pow_eq_zero` in CoherentModules/RingTheory/Ideal/Comap.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Comap.lean#L59)
