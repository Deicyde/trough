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

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_signInvariant`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Existence.html#TauCeti.exists_isCAD_signInvariant).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_signInvariant`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Existence.html#TauCeti.exists_isCAD_signInvariant)
- [Source of `TauCeti.exists_isCAD_signInvariant` in TauCeti/Geometry/RealAlgebraic/CAD/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/CAD/Existence.lean#L60)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RealAlgebraicGeometry/STATUS.md)
