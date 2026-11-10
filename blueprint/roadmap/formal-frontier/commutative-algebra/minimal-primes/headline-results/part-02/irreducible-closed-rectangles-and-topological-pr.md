---
declaration: theorem
origin: cited
lean: topologicalKrullDim_prod
statement: formalized
proof: formalized
---

# Irreducible closed rectangles and topological product dimensions

For spaces `X : Type u` and `Y : Type v` with their given topologies,
[`topologicalKrullDim_prod`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Topology/KrullDimension/Product.lean) states

```lean
topologicalKrullDim (X × Y) = topologicalKrullDim X + topologicalKrullDim Y
```

For `ι : Type w`, `[Fintype ι]` and given topological fibres `Y : ι → Type u`,
`topologicalKrullDim_pi` gives
`topologicalKrullDim (∀ i, Y i) = ∑ i, topologicalKrullDim (Y i)`.
These use the canonical topological product and ordinary dependent product, with values
in `WithBot ℕ∞`. Empty factors give bottom, and empty index gives zero. No separation,
sobriety, Noetherianity, nonemptiness, finite dimension or attainment is assumed.
There is no arbitrary-infinite-index dimension sum, and these are not assertions about
scheme fibre-product Zariski topologies or lexicographic orders.

The [irreducible-closed product module](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Topology/IrreducibleCloseds.lean)
provides set-level product irreducibility and the arbitrary-index classification
`closure S = Set.pi Set.univ (fun i => closure (Function.eval i '' S))` for irreducible
`S`. The binary version needs only preirreducibility and includes empty `S`.
Its canonical irreducible closed products have the set-product and set-rectangle carriers.
`TopologicalSpace.IrreducibleCloseds.prodOrderIso` and `piOrderIso` send a closed
irreducible set to the closures of its projection images, with the canonical rectangles
as inverses. The dependent-product classification and order isomorphism allow arbitrary
index types, and nonemptiness for factor recovery comes from the factor sets themselves.
The dimension formulas reuse this library's pointwise product-order dimension formulas.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `topologicalKrullDim_prod` (theorem), declared in [MinimalPrimes/Topology/KrullDimension/Product.lean, line 42](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Topology/KrullDimension/Product.lean#L42).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `topologicalKrullDim_prod` in MinimalPrimes/Topology/KrullDimension/Product.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Topology/KrullDimension/Product.lean#L42)
