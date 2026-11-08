---
declaration: theorem
origin: cited
lean: isNoetherianRing_quotient_annihilator_of_finite
statement: formalized
proof: formalized
---

# Annihilator quotients with two scalar actions

Suppose a ring `A` and a
semiring `C` act on the same additive commutative monoid `M`, with commuting
given actions. If `M` is finitely generated over `C` and Noetherian over `A`,
then `A` modulo the annihilator of its original action is left Noetherian;
see
[`isNoetherianRing_quotient_annihilator_of_finite`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean).
If `M` is an additive commutative group, finite generation over `C` and
coherence over `A` instead give a coherent annihilator quotient, as a
regular left module over the quotient ring; see
[`isCoherentRing_quotient_annihilator_of_finite`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Quotient.lean).
The three universes are independent. Neither scalar type needs to be
Noetherian, and the `A`-action need not commute with itself.
Taking `C = A` in the Noetherian result recovers the self-commuting criterion:
for an additive commutative group with a self-commuting `A`-action, Noetherianity over `A`
is equivalent to finite generation over `A` and left Noetherianity of the
annihilator quotient. In particular, this applies over every commutative
ring. The sufficient direction holds over any ring for an additive
commutative monoid with its given module structure, without a commutation
hypothesis.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `isNoetherianRing_quotient_annihilator_of_finite` (theorem), declared in [CoherentModules/RingTheory/Noetherian.lean, line 247](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean#L247).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `isNoetherianRing_quotient_annihilator_of_finite` in CoherentModules/RingTheory/Noetherian.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Noetherian.lean#L247)
