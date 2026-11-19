---
declaration: theorem
origin: cited
lean: FormalGroup.frobeniusCurve_frobeniusCurve
statement: formalized
proof: formalized
---

# Cartier's composition law `f_m ∘ f_n = f_{m n}`

**Cartier's composition law `f_m ∘ f_n = f_{m n}`** on curves of a commutative formal group
law over any commutative ring.

```lean
FormalGroup.frobeniusCurve_frobeniusCurve.{u_1} {R : Type u_1} [CommRing R] (F : FormalGroup R)
  [F.IsComm] {m n : ℕ} (hm : m ≠ 0) (hn : n ≠ 0) (γ : F.Curve) :
  (F.frobeniusCurve m hm) ((F.frobeniusCurve n hn) γ) = (F.frobeniusCurve (m * n) ⋯) γ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lazard's theorem](../bordism-formal-groups-and-chromatic-operations/lazards-theorem.md)
- [Newton's formula for `evalTopEsymm` on power sums](../multivariate-polynomials/newtons-formula-for-evaltopesymm-on-power-sums.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.frobeniusCurve_frobeniusCurve`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Curve/Basic.html#FormalGroup.frobeniusCurve_frobeniusCurve).

## Sources

- [Tau Ceti documentation: `FormalGroup.frobeniusCurve_frobeniusCurve`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Curve/Basic.html#FormalGroup.frobeniusCurve_frobeniusCurve)
- [Source of `FormalGroup.frobeniusCurve_frobeniusCurve` in TauCeti/RingTheory/FormalGroup/Curve/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Curve/Basic.lean#L954)
