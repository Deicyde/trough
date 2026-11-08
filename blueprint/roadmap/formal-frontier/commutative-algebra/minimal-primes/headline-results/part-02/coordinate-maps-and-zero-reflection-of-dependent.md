---
declaration: def
origin: cited
lean: Filter.Product.map
statement: formalized
---

# Coordinate maps and zero-reflection of dependent filter products

For any filter `D` and independently universed dependent type families `R` and `S`,
coordinate functions `φ i : R i → S i` induce the canonical
[`Filter.Product.map`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Map.lean)
from `D.Product R` to `D.Product S`. Its representative law uniquely characterizes
it, with identity and composition laws and agreement with the existing semiring
and constant-family germ maps. No algebra, points or proper-filter hypothesis is
needed for the coordinate map.

If the coordinate functions preserve selected total sections `a` and `b`
eventually, the induced map reflects the represented point `b` to `a` exactly
when the coordinate functions reflect these points eventually. For fibrewise
`ZeroHom`s this gives zero-reflection using only the **same selected fibre zeros**:
`Filter.Product.zeroPoint` is the class of that zero section, not a new Product
zero instance. No multiplication, addition or scalar zero is required.

`Filter.Product.map_surjective_iff` retains the exact global-section alternatives:
the total target section type is empty, or the total source section type is
nonempty and the coordinate maps are surjective eventually. An empty source fibre
ignored by the filter cannot be silently filled. The
[dependent controls](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/Map.lean) include varying
`Fin (n + 3) → Fin (n + 4)` maps that reflect zero but are neither injective nor
additive, and a frequent bad locus giving a genuine nonzero kernel class.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.map` (def), declared in [MinimalPrimes/Order/Filter/Product/Map.lean, line 36](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Map.lean#L36).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.map` in MinimalPrimes/Order/Filter/Product/Map.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Map.lean#L36)
