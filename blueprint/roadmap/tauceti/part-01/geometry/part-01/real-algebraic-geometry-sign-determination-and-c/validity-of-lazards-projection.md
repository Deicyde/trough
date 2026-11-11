---
declaration: theorem
origin: cited
lean: TauCeti.exists_isCAD_lazardValuationReindex_eq
statement: formalized
proof: formalized
---

# Validity of Lazard's projection

Every finite family of real polynomials in `n`
variables has a cylindrical algebraic decomposition of `ℝ ^ n` into analytic submanifolds on
each cell of which every member has constant Lazard valuation, when the coordinates are read in
reverse order, from the coordinate added first by the cylindrical structure to the one added
last. Every member is also sign-invariant on each cell. No well-orientedness hypothesis is
imposed, and members may be nullified over base cells of positive dimension.

```lean
TauCeti.exists_isCAD_lazardValuationReindex_eq {n : ℕ} (F : Finset (MvPolynomial (Fin n) ℝ)) :
  ∃ 𝓒,
    TauCeti.IsCAD n 𝓒 ∧
      (∀ E ∈ 𝓒, ∃ d, TauCeti.IsAnalyticSubmanifold d E) ∧
        (∀ f ∈ F,
            ∀ E ∈ 𝓒,
              ∀ x ∈ E,
                ∀ y ∈ E,
                  f.lazardValuationReindex Fin.revPerm x = f.lazardValuationReindex Fin.revPerm y) ∧
          ∀ f ∈ F, ∀ E ∈ 𝓒, TauCeti.SignInvariant (fun x => (MvPolynomial.eval x) f) E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CAD lifting by Lazard delineations in a reordered base](cad-lifting-by-lazard-delineations-in-a-reordere.md)
- [Lazard lifting of a family](lazard-lifting-of-a-family.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCAD_lazardValuationReindex_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Existence.html#TauCeti.exists_isCAD_lazardValuationReindex_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCAD_lazardValuationReindex_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Existence.html#TauCeti.exists_isCAD_lazardValuationReindex_eq)
- [Source of `TauCeti.exists_isCAD_lazardValuationReindex_eq` in TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/CAD/Lazard/Existence.lean#L59)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RealAlgebraicGeometry/STATUS.md)
