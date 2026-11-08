---
declaration: def
origin: cited
lean: Filter.Product.centerEquiv
statement: formalized
---

# Centers of dependent filter products

For any filter and an independently universed family with multiplication, a section
represents an element of the full intrinsic center exactly when it is central
eventually. With a two-sided identity in each fibre,
[`Filter.Product.centerEquiv`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Center.lean)
identifies the product of the fibre centers with the center of the product.
Neither associativity nor a proper filter is required. The representative API
selects a total center-valued section agreeing eventually, not canonically at
ignored indices. The [varying-family client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Germ/Center.lean)
uses retained fibres of sizes four and sixteen with nonassociative multiplication;
the existing constant-germ API and its client remain available.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.centerEquiv` (def), declared in [MinimalPrimes/Order/Filter/Product/Center.lean, line 86](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Center.lean#L86).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.centerEquiv` in MinimalPrimes/Order/Filter/Product/Center.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Center.lean#L86)
