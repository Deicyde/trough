---
declaration: theorem
origin: cited
lean: Ideal.sup_pow_add_sub_one_le
statement: formalized
proof: formalized
---

# Sums of nilpotent left ideals

For arbitrary left ideals `I`, `J` of a
possibly noncommutative `Semiring R`,
[`Ideal.sup_pow_add_sub_one_le`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Operations.lean)
gives `(I ⊔ J) ^ (m + n - 1) ≤ I ^ m * ⊤ ⊔ J ^ n * ⊤` for all natural
`m`, `n`. Global witnesses `I ^ m = 0` and `J ^ n = 0` therefore give
`(I ⊔ J) ^ (m + n - 1) = 0`; `Ideal.isNilpotent_sup` makes the sum of two
globally nilpotent left ideals nilpotent. No commutativity, two-sidedness or
positivity of the exponents is required. The
[relative-generation client](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Ideal/Operations.lean)
combines this with nilpotent-ideal elimination to deduce `P ≤ N` from
`P ≤ N ⊔ (I ⊔ J) • P` in any additive commutative `R`-semimodule, with an
independent carrier universe.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.sup_pow_add_sub_one_le` (theorem), declared in [CoherentModules/RingTheory/Ideal/Operations.lean, line 136](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Operations.lean#L136).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.sup_pow_add_sub_one_le` in CoherentModules/RingTheory/Ideal/Operations.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Operations.lean#L136)
