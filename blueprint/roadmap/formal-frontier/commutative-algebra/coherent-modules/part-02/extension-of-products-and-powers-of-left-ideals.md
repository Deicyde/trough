---
declaration: theorem
origin: cited
lean: Ideal.map_mul_of_isTwoSided
statement: formalized
proof: formalized
---

# Extension of products and powers of left ideals

For any unital homomorphism
`f : A →+* B` between semirings in independent universes,
[`Ideal.map_mul_of_isTwoSided`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Maps.lean)
gives `(I * J).map f = I.map f * J.map f` whenever `I.map f` is two-sided.
The companion `Ideal.map_pow_of_isTwoSided` gives
`(I ^ n).map f = (I.map f) ^ n` for every natural exponent, including zero.
Neither semiring must be commutative, and `f` need not be surjective.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.map_mul_of_isTwoSided` (theorem), declared in [CoherentModules/RingTheory/Ideal/Maps.lean, line 39](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Maps.lean#L39).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.map_mul_of_isTwoSided` in CoherentModules/RingTheory/Ideal/Maps.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Maps.lean#L39)
