---
declaration: theorem
origin: cited
lean: TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center
statement: formalized
proof: formalized
---

# Iwasawa's theorem for the projective symplectic group

In positive rank, the quotient
`PSp_{2m}(K)` of the symplectic group by its centre is simple as soon as `Sp_{2m}(K)` is
perfect.

```lean
TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center.{u} {K : Type u} [Field K] {m : ℕ} [NeZero m]
  (h : commutator ↥(TauCeti.GLSymplecticFin m K) = ⊤) :
  IsSimpleGroup (↥(TauCeti.GLSymplecticFin m K) ⧸ Subgroup.center ↥(TauCeti.GLSymplecticFin m K))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Iwasawa's criterion for the derived central quotient](../../group-theory/finiteness-and-simplicity-of-the-groups-on-the-c/iwasawas-criterion-for-the-derived-central-quoti.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Symplectic/Simple.html#TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center).

## Sources

- [Tau Ceti documentation: `TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Symplectic/Simple.html#TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center)
- [Source of `TauCeti.GLSymplecticFin.isSimpleGroup_quotient_center` in TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Symplectic/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Symplectic/Simple.lean#L60)
