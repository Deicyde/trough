---
declaration: theorem
origin: cited
lean: TauCeti.zHat.isIdempotentElem_iff_exists_idemOfSet
statement: formalized
proof: formalized
---

# The idempotents of `ℤ̂` are the `ω_S`

A profinite integer is idempotent exactly when it is
`ω_S` for some set `S` of primes, necessarily the set of primes at which its component is `1`: under
the product decomposition each component of an idempotent is an idempotent of the domain `ℤ_ℓ`
(`Pi.isIdempotentElem_iff`), hence `0` or `1`.

```lean
TauCeti.zHat.isIdempotentElem_iff_exists_idemOfSet.{u}
  {a : Additive ↑TauCeti.zHat.toProfinite.toTop} :
  IsIdempotentElem a ↔ ∃ S, TauCeti.zHat.idemOfSet S = a
```

## Depends on

- [The product decomposition of the profinite integers](the-product-decomposition-of-the-profinite-integ.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.zHat.isIdempotentElem_iff_exists_idemOfSet`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.html#TauCeti.zHat.isIdempotentElem_iff_exists_idemOfSet).

## Sources

- [Tau Ceti documentation: `TauCeti.zHat.isIdempotentElem_iff_exists_idemOfSet`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.html#TauCeti.zHat.isIdempotentElem_iff_exists_idemOfSet)
- [Source of `TauCeti.zHat.isIdempotentElem_iff_exists_idemOfSet` in TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ZHat/Idempotent.lean#L185)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteArithmetic/STATUS.md)
