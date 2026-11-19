---
declaration: theorem
origin: cited
lean: FormalGroup.frobeniusCurve_verschiebungCurve_of_coprime
statement: formalized
proof: formalized
---

# Cartier's coprime commutation law `f_m ∘ V_n = V_n ∘ f_m` whenever `gcd(m, n) = 1`, over any commutative ring

```lean
FormalGroup.frobeniusCurve_verschiebungCurve_of_coprime.{u_1} {R : Type u_1} [CommRing R]
  (F : FormalGroup R) [F.IsComm] {m n : ℕ} (hm : m ≠ 0) (hn : n ≠ 0) (hcop : m.Coprime n)
  (γ : F.Curve) :
  (F.frobeniusCurve m hm) ((F.verschiebungCurve n hn) γ) =
    (F.verschiebungCurve n hn) ((F.frobeniusCurve m hm) γ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lazard's theorem](../bordism-formal-groups-and-chromatic-operations/lazards-theorem.md)
- [Newton's formula for `evalTopEsymm` on power sums](../multivariate-polynomials/newtons-formula-for-evaltopesymm-on-power-sums.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.frobeniusCurve_verschiebungCurve_of_coprime`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Curve/Basic.html#FormalGroup.frobeniusCurve_verschiebungCurve_of_coprime).

## Sources

- [Tau Ceti documentation: `FormalGroup.frobeniusCurve_verschiebungCurve_of_coprime`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Curve/Basic.html#FormalGroup.frobeniusCurve_verschiebungCurve_of_coprime)
- [Source of `FormalGroup.frobeniusCurve_verschiebungCurve_of_coprime` in TauCeti/RingTheory/FormalGroup/Curve/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Curve/Basic.lean#L984)
