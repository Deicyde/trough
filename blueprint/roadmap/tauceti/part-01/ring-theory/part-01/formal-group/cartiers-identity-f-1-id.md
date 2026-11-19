---
declaration: theorem
origin: cited
lean: FormalGroup.frobeniusCurve_one, FormalGroup.frobeniusCurve_verschiebungCurve_self
statement: formalized
proof: formalized
---

# Cartier's identity `f_1 = id`

the first Frobenius operator is the identity on curves.

```lean
FormalGroup.frobeniusCurve_one.{u_1} {R : Type u_1} [CommRing R] (F : FormalGroup R) [F.IsComm]
  (γ : F.Curve) : (F.frobeniusCurve 1 ⋯) γ = γ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lazard's theorem](../bordism-formal-groups-and-chromatic-operations/lazards-theorem.md)
- [Newton's formula for `evalTopEsymm` on power sums](../multivariate-polynomials/newtons-formula-for-evaltopesymm-on-power-sums.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.frobeniusCurve_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Curve/Basic.html#FormalGroup.frobeniusCurve_one).

## Other forms

**Cartier's identity `f_n ∘ V_n = [n]_F`.** Formalized in Tau Ceti as [`FormalGroup.frobeniusCurve_verschiebungCurve_self`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Curve/Basic.html#FormalGroup.frobeniusCurve_verschiebungCurve_self).

```lean
FormalGroup.frobeniusCurve_verschiebungCurve_self.{u_1} {R : Type u_1} [CommRing R]
  (F : FormalGroup R) [F.IsComm] (n : ℕ) (hn : n ≠ 0) (γ : F.Curve) :
  (F.frobeniusCurve n hn) ((F.verschiebungCurve n hn) γ) = n • γ
```

## Sources

- [Tau Ceti documentation: `FormalGroup.frobeniusCurve_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Curve/Basic.html#FormalGroup.frobeniusCurve_one)
- [Source of `FormalGroup.frobeniusCurve_one` in TauCeti/RingTheory/FormalGroup/Curve/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Curve/Basic.lean#L944)
