---
declaration: theorem
origin: cited
lean: TauCeti.montel
statement: formalized
proof: formalized
---

# Montel's selection theorem

A locally bounded sequence of holomorphic maps on an open
set `Ω ⊆ ℂ` into a proper complex normed space `E` has a subsequence converging locally uniformly
on `Ω` to a holomorphic map.

Over `ℂ`, properness of the target is equivalent to finite-dimensionality; in particular, the
result applies to scalar-valued holomorphic maps.

```lean
TauCeti.montel.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] {Ω : Set ℂ}
  {F : ℕ → ℂ → E} [ProperSpace E] (hΩ : IsOpen Ω) (hF : ∀ (n : ℕ), DifferentiableOn ℂ (F n) Ω)
  (hb : TauCeti.IsLocallyBoundedOn F Ω) :
  ∃ φ g,
    StrictMono φ ∧
      DifferentiableOn ℂ g Ω ∧ TendstoLocallyUniformlyOn (fun n => F (φ n)) g Filter.atTop Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Montel's theorem as an equivalence](montels-theorem-as-an-equivalence.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.montel`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Montel/Basic.html#TauCeti.montel).

## Sources

- [Tau Ceti documentation: `TauCeti.montel`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Montel/Basic.html#TauCeti.montel)
- [Source of `TauCeti.montel` in TauCeti/Analysis/Complex/Conformal/Montel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/Montel/Basic.lean#L52)
