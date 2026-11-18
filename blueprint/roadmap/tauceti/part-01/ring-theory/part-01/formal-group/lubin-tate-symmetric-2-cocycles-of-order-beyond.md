---
declaration: theorem
origin: cited
lean: FormalGroup.IsSymmetricCocycle.exists_eq_homDefect_𝔾ₐ
statement: formalized
proof: formalized
---

# Lubin–Tate: symmetric 2-cocycles of order beyond the degrees `pⁱ`, `0 < i < h`, are coboundaries

Let `p` be a prime with `p = 0` in `R`, and let `F` be a commutative formal group
law whose `p`-series has order at least `pʰ` and a unit coefficient of `X^(pʰ)`, for instance a
law of height `h` over a field of characteristic `p`. Let `Γ` be a symmetric 2-cocycle of `F`
without constant term that vanishes to order greater than `pⁱ` for every `0 < i < h`. Then
`Γ = g(F(X, Y)) - g(X) - g(Y)` for a power series `g` without constant term.

```lean
FormalGroup.IsSymmetricCocycle.exists_eq_homDefect_𝔾ₐ.{u_1} {R : Type u_1} [CommRing R]
  {F : FormalGroup R} {p h : ℕ} [F.IsComm] (hp : Nat.Prime p) (hpR : ↑p = 0)
  (hF : ↑(p ^ h) ≤ (F.nsmulSeries p).order)
  (hv : IsUnit ((PowerSeries.coeff (p ^ h)) (F.nsmulSeries p))) {Γ : MvPowerSeries (Fin 2) R}
  (hΓ : F.IsSymmetricCocycle Γ) (hΓ₀ : MvPowerSeries.constantCoeff Γ = 0)
  (hΓh : ∀ (i : ℕ), 0 < i → i < h → ↑(p ^ i) < Γ.order) :
  ∃ g, PowerSeries.constantCoeff g = 0 ∧ Γ = F.homDefect FormalGroup.𝔾ₐ g
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.IsSymmetricCocycle.exists_eq_homDefect_𝔾ₐ`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Height.html#FormalGroup.IsSymmetricCocycle.exists_eq_homDefect_%F0%9D%94%BE%E2%82%90).

## Sources

- [Tau Ceti documentation: `FormalGroup.IsSymmetricCocycle.exists_eq_homDefect_𝔾ₐ`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Height.html#FormalGroup.IsSymmetricCocycle.exists_eq_homDefect_%F0%9D%94%BE%E2%82%90)
- [Source of `FormalGroup.IsSymmetricCocycle.exists_eq_homDefect_𝔾ₐ` in TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Height.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/Height.lean#L245)
