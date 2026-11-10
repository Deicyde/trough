---
declaration: def
origin: cited
lean: Filter.Product.piComparison
statement: formalized
---

# Small products of dependent filter products

For an arbitrary filter `D` and `R : ι → κ → Type w`, with independent row,
coordinate and fibre universes, [`Filter.Product.piComparison`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Pi.lean)
maps the class of a matrix to its family of column classes. It is surjective for
arbitrary `κ`. If `[CardinalInterFilter D c]` and `HasCardinalLT κ c`, with `c` in
the row universe, `Filter.Product.piEquivOfHasCardinalLT` makes this same comparison
an equivalence. The bound is strict: the filter must be closed under intersections
of fewer than `c` sets. Countable completeness and countable coordinates give
`Filter.Product.piEquivOfCountable`; finite coordinates give the original
`Filter.Product.piEquiv` for **every** filter. Both new equivalences agree with the
finite one as equivalence data when the coordinates are finite.

The inverse transposes supplied global column representatives. Generic equivalence
identities and the forward readouts give the inverse laws; existing comparison
naturality gives both naturality squares, with an independent target universe.
No quotient unfolding, algebra, inhabited fibres, properness, common-universe
assumption or chosen finite enumeration is required. The
[examples](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/Pi.lean) include infinite even
principal rows with `Fin (i+j+2)` fibres and proper nonprincipal cocountable rows
on `Set ℕ`, as well as empty indices and bottom with empty global sections.
The cofinite-Nat Boolean diagonal remains a failure of injectivity: countable
coordinates alone do not suffice.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.piComparison` (def), declared in [MinimalPrimes/Order/Filter/Product/Pi.lean, line 58](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Pi.lean#L58).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.piComparison` in MinimalPrimes/Order/Filter/Product/Pi.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Pi.lean#L58)
