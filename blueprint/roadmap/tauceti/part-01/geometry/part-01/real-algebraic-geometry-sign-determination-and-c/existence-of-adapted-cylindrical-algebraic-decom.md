---
declaration: theorem
origin: cited
lean: TauCeti.exists_isCAD_signInvariant
statement: formalized
proof: formalized
---

# Existence of adapted cylindrical algebraic decompositions

For every finite set `F` of
real polynomials in `n` variables there is a cylindrical algebraic decomposition of `ℝ ^ n` on
each cell of which every member of `F` is sign-invariant.

```lean
TauCeti.exists_isCAD_signInvariant {n : ℕ} (F : Finset (MvPolynomial (Fin n) ℝ)) :
  ∃ 𝒞,
    TauCeti.IsCAD n 𝒞 ∧ ∀ f ∈ F, ∀ E ∈ 𝒞, TauCeti.SignInvariant (fun x => (MvPolynomial.eval x) f) E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy's bound on the symmetric power](../../../analysis/part-03/polynomial/cauchys-bound-on-the-symmetric-power.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_signInvariant`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Existence.html#TauCeti.exists_isCAD_signInvariant).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_signInvariant`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Existence.html#TauCeti.exists_isCAD_signInvariant)
- [Source of `TauCeti.exists_isCAD_signInvariant` in TauCeti/Geometry/RealAlgebraic/CAD/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/CAD/Existence.lean#L60)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RealAlgebraicGeometry/STATUS.md)
