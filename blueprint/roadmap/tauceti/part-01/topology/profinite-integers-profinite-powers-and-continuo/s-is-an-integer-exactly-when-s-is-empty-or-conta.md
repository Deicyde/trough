---
declaration: theorem
origin: cited
lean: TauCeti.zHat.idemOfSet_mem_range_intCast_iff
statement: formalized
proof: formalized
---

# `ω_S` is an integer exactly when `S` is empty or contains every prime, that is, when `ω_S` is `0` or `1`

an idempotent integer is `0` or `1`.

```lean
TauCeti.zHat.idemOfSet_mem_range_intCast_iff.{u} {S : Set Nat.Primes} :
  TauCeti.zHat.idemOfSet S ∈ Set.range Int.cast ↔ S = ∅ ∨ S = Set.univ
```

## Depends on

- [The product decomposition of the profinite integers](the-product-decomposition-of-the-profinite-integ.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.idemOfSet_mem_range_intCast_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.html#TauCeti.zHat.idemOfSet_mem_range_intCast_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.idemOfSet_mem_range_intCast_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.html#TauCeti.zHat.idemOfSet_mem_range_intCast_iff)
- [Source of `TauCeti.zHat.idemOfSet_mem_range_intCast_iff` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.lean#L198)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteArithmetic/STATUS.md)
