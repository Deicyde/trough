---
declaration: def
origin: cited
lean: Filter.Product.basis
statement: formalized
---

# Common finite bases of dependent reduced products

For the same given semiring and semimodule records, a family of given bases
`b i : Module.Basis J (R i) (M i)` with **one common finite index** `J` induces
[`Filter.Product.basis`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Basis.lean) of
`F.Product M` over the existing scalar semiring `F.Product R`. Its vector at `j`
is represented by `fun i => b i j`, and coefficients are the existing varying
maps of the fibre coefficients, on represented and opaque vectors alike.
For standard function bases on `J → R i`, the whole coordinate equivalence agrees
with `Filter.Product.piComparison`. All four carrier universes are independent;
empty `J`, bottom filters and zero semirings are included. No commutativity,
faithfulness, properness or nontriviality hypothesis is imposed. A family of
unbounded varying ranks is not an instance of this common finite-index construction.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.basis` (def), declared in [MinimalPrimes/Order/Filter/Product/Basis.lean, line 168](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Basis.lean#L168).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.basis` in MinimalPrimes/Order/Filter/Product/Basis.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Basis.lean#L168)
