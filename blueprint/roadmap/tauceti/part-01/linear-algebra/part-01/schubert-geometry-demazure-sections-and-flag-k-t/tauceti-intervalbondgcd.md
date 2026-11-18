---
declaration: def
origin: cited
lean: TauCeti.intervalBondGcd
statement: formalized
---

# TauCeti.intervalBondGcd

The **interval bond gcd** `d_λ(x, y)` of minimal coset representatives `y ≤ x` of the
stabilizer of `λ`: the bond gcd of any saturated chain of `W / W_λ` from `x` down to `y`. It does
not depend on the chain (`TauCeti.bondGcd_eq_intervalBondGcd`), and `d_λ(x, x) = 0`. It is `0`
unless `y ≤ x` are both minimal coset representatives of `W_λ`, that is when there is no saturated
chain from `x` down to `y`.

```lean
TauCeti.intervalBondGcd.{u, w, x} {ι : Type u} {M : Type w} {N : Type x} [AddCommGroup M]
  [AddCommGroup N] {P : RootPairing ι ℤ M N} (b : P.Base) [Finite ι] [P.IsReduced] (lam : M)
  (x y : ↥P.weylGroup) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.intervalBondGcd`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.html#TauCeti.intervalBondGcd).

## Sources

- [Tau Ceti documentation: `TauCeti.intervalBondGcd`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.html#TauCeti.intervalBondGcd)
- [Source of `TauCeti.intervalBondGcd` in TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Weyl/IntervalBondGcd.lean#L287)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SchubertGeometry/STATUS.md)
