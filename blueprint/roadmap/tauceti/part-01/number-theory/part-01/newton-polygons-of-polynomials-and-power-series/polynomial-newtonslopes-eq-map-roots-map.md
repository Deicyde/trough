---
declaration: theorem
origin: cited
lean: Polynomial.newtonSlopes_eq_map_roots_map
statement: formalized
proof: formalized
---

# Polynomial.newtonSlopes_eq_map_roots_map

If `f` splits over a valued extension `L` whose valuation `w` restricts to `v`, and only
zero has infinite valuation in `L`, the finite slopes of `f` are the negated valuations `-w α`
of its nonzero roots `α` in `L`, with multiplicity.

```lean
Polynomial.newtonSlopes_eq_map_roots_map.{u_2, u_3} {K : Type u_2} {L : Type u_3} [Ring K]
  [CommRing L] [IsDomain L] [DecidableEq L] {v : AddValuation K (WithTop ℝ)}
  {w : AddValuation L (WithTop ℝ)} (hw : ∀ (x : L), w x = ⊤ → x = 0) (φ : K →+* L)
  (hφ : ∀ (x : K), w (φ x) = v x) {f : Polynomial K} (hf : (Polynomial.map φ f).Splits) :
  f.newtonSlopes v =
    Multiset.map (fun α => -(w α).untop₀)
      (Multiset.filter (fun x => x ≠ 0) (Polynomial.map φ f).roots)
```

## Depends on

- [TauCeti.lowerConvexEnvelope](tauceti-lowerconvexenvelope.md)

## Proof depends on

- [Polynomial.newtonPolygon_mul](polynomial-newtonpolygon-mul.md)
- [TauCeti.FiniteSlopeData](tauceti-finiteslopedata.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.newtonSlopes_eq_map_roots_map`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Roots.html#Polynomial.newtonSlopes_eq_map_roots_map).

## Sources

- [Tau Ceti documentation: `Polynomial.newtonSlopes_eq_map_roots_map`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Roots.html#Polynomial.newtonSlopes_eq_map_roots_map)
- [Source of `Polynomial.newtonSlopes_eq_map_roots_map` in TauCeti/NumberTheory/NewtonPolygon/Roots.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NewtonPolygon/Roots.lean#L138)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NewtonPolygons/STATUS.md)
