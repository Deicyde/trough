---
declaration: def
origin: cited
lean: Filter.Product.module
statement: formalized
---

# Semimodules, annihilators and faithful actions on dependent reduced products

For independent families `R i`, `M i` of semirings and additive commutative monoids,
with given `Module (R i) (M i)` records and an arbitrary filter `F`,
[`Filter.Product.module`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Module.lean) supplies
pointwise semimodule data on the existing `F.Product M` over the existing scalar
semiring `F.Product R`. The data are named rather than globally registered:
the given fibre actions stay fixed even when scalar and vector carriers coincide.
Representative equations characterize zero, addition, natural scaling and scalar
action. A represented scalar acts on every opaque vector by `Filter.Product.map`.
The additive record agrees with the existing semiring parent; constant records
recover Mathlib's two-germ module after identifying both base records.
The [torsion-free criterion](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Torsion.lean)
`Filter.Product.isTorsionFree_iff` identifies torsion-freeness of this semimodule
over `F.Product R` with eventual torsion-freeness of the given fibre semimodules.
Torsion-freeness uses full injectivity of the action of every two-sided regular
scalar. The represented-scalar readout reduces action injectivity to eventual
fibre injectivity, and regular-scalar sections give reflection. No additive
inverses, cancellation, domain, properness or nontriviality assumption is required.
The [varying-family client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/Module.lean)
applies the criterion to free semimodules of ranks `n + 1` over `ℕ × ZMod (n + 2)`
along the cofinite filter, and uses the faithfulness criterion for the same family.

The [annihilator and faithfulness criteria](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Faithful.lean)
retain these same given records. `Filter.Product.coe_mem_annihilator_iff` says that
a represented scalar annihilates the whole semimodule exactly when its values
annihilate the fibre semimodules eventually. `Filter.Product.faithfulSMul_iff`
says that the action is faithful exactly when the given fibre actions are faithful
eventually. Faithfulness compares **two scalars on all vectors**, unlike
represented-scalar injectivity; a zero annihilator does not characterize it at this
semiring floor. The weaker `faithfulSMul_smul_iff` needs only given fibre actions
and scalar/vector zeros, while `smul_coe_eq_smul_coe_iff` detects equality of two
represented actions using only vector zeros. These zeros provide total sections,
not zero-preservation laws. Bottom filters, empty indices and zero fibres remain
included, with independent scalar and vector universes.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.module` (def), declared in [MinimalPrimes/Order/Filter/Product/Module.lean, line 233](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Module.lean#L233).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.module` in MinimalPrimes/Order/Filter/Product/Module.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Module.lean#L233)
