---
declaration: theorem
origin: cited
lean: Ideal.IsRadical.colon
statement: formalized
proof: formalized
---

# Radical colons and pointwise annihilators

For a radical ideal `I` in a
commutative semiring `R` and an arbitrary subset `s : Set R`,
[`Ideal.IsRadical.colon`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Annihilator.lean)
proves `(I.colon s).IsRadical`; use it as `hI.colon s`.
Taking `I = ⊥` in a reduced commutative semiring shows that the ideal of
scalars `a` with `a * b = 0` for every `b ∈ s` is radical. No finiteness,
nonemptiness or nontriviality assumption is needed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.IsRadical.colon` (theorem), declared in [CoherentModules/RingTheory/Ideal/Annihilator.lean, line 137](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Annihilator.lean#L137).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Ideal.IsRadical.colon` in CoherentModules/RingTheory/Ideal/Annihilator.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Annihilator.lean#L137)
