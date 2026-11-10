---
declaration: theorem
origin: cited
lean: Order.krullDim_pi_eq_iSup_range_restrict
statement: formalized
proof: formalized
---

# Dimension from finite coordinate-restriction images

For arbitrary `ι : Type u` and independently universed given preorders
`β : ι → Type v`,
[`Order.krullDim_pi_eq_iSup_range_restrict`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)
states

```lean
Order.krullDim (∀ i, β i) =
  ⨆ J : Finset ι,
    Order.krullDim (Set.range
      (fun f : (∀ i, β i) => fun j : J => f j.1))
```

The equality is in `WithBot ℕ∞`. Every range has the inherited ordinary pointwise
subtype order, and every restriction starts from the original full product.
Thus an empty full product makes every image empty, even for `J = ∅`, giving
bottom on both sides. An empty ambient index instead gives dimension zero.
No nonemptiness, finite-index, finite-fibre, antisymmetry, finite-rank,
attainment or finite-support hypothesis is required; an infinite supremum need
not be attained by a finite image. These are not lexicographic or topological
products. The proof combines the point-height formulas above with Mathlib's
height transport, finite updates and surjective range reindexing.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Order.krullDim_pi_eq_iSup_range_restrict` (theorem), declared in [MinimalPrimes/Order/KrullDimension.lean, line 823](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L823).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Order.krullDim_pi_eq_iSup_range_restrict` in MinimalPrimes/Order/KrullDimension.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean#L823)
