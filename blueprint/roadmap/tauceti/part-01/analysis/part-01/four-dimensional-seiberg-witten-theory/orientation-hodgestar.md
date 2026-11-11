---
declaration: def
origin: cited
lean: Orientation.hodgeStar
statement: formalized
---

# Orientation.hodgeStar

The Hodge star `⋀ᵏ V ≃ ⋀ˡ V`, `k + l = finrank ℝ V`, of an oriented real inner product space:
Mathlib's `exteriorPower.hodgeStar` for the inner product and `Orientation.volumeEquiv`. It is
characterized by `⟪⋆x, y⟫ = vol (x ∧ y)` (`Orientation.inner_hodgeStar_apply`).

```lean
Orientation.hodgeStar.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] {n : ℕ} [_i : Fact (Module.finrank ℝ V = n)] (o : Orientation ℝ V (Fin n))
  {k l : ℕ} (hkl : k + l = Module.finrank ℝ V) : ↥(⋀[ℝ]^k V) ≃ₗ[ℝ] ↥(⋀[ℝ]^l V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Orientation.hodgeStar`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HodgeStar/Basic.html#Orientation.hodgeStar).

## Sources

- [Tau Ceti documentation: `Orientation.hodgeStar`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HodgeStar/Basic.html#Orientation.hodgeStar)
- [Source of `Orientation.hodgeStar` in TauCeti/Analysis/InnerProductSpace/HodgeStar/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/HodgeStar/Basic.lean#L173)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
