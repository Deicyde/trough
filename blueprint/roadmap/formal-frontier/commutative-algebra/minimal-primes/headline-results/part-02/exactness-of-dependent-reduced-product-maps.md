---
declaration: theorem
origin: cited
lean: Filter.Product.map_exact_iff
statement: formalized
proof: formalized
---

# Exactness of dependent reduced-product maps

For arbitrary functions `f i : X i → Y i` and `g i : Y i → Z i` in independent
universes, an arbitrary filter `F`, given `Zero (Z i)` records and
`Nonempty (∀ i, X i)`,
[`Filter.Product.map_exact_iff`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Exact.lean)
characterizes `Function.Exact` of the two existing `Product.map` functions by
`∀ᶠ i in F, Function.Exact (f i) (g i)`. This is one eventual locus of **whole
fibre exactness**, not exactness at every index or separately eventual tests on
fixed values. The selected target zero is exactly `Product.zeroPoint F Z`, the
represented section of the given fibre zeros; no global zero instance is added.
Neither function needs to preserve zero or any algebraic operation.

A total source section is essential: an empty source fibre outside the filter's
support still prevents all total source sections. No independent middle-section
hypothesis is needed, since the first map sends a source section to one.
`Filter.Product.map_exact_iff_of_addZeroClass` instead uses the existing named
additive product zero, still for arbitrary functions and only target
`AddZeroClass` records. `Product.zeroPoint_eq_zero_add` supplies this alignment.
In particular, given linear maps between semimodules over given, possibly
noncommutative, fibre semirings can be used as functions while retaining all the
given additive and module records. The target zero is inherited from
`Product.addCommMonoid F P`, and fibre source zeros discharge the section
condition. No bundled product linear map, finite basis, properness,
nontriviality, additive inverses or further inhabitation hypothesis is needed.
Bottom filters, empty indices and zero semirings remain included.

For constant families, `Product.map_const_eq_germ_map` and
`Product.zeroPoint_eq_germ_zero` identify these functions and the target zero
with Mathlib's germ maps and zero.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.map_exact_iff` (theorem), declared in [MinimalPrimes/Order/Filter/Product/Exact.lean, line 86](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Exact.lean#L86).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.map_exact_iff` in MinimalPrimes/Order/Filter/Product/Exact.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Exact.lean#L86)
