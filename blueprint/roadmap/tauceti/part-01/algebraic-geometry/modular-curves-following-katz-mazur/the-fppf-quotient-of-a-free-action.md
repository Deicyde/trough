---
declaration: def
origin: cited
lean: TauCeti.InvariantQuotient.isColimitFppfYonedaCofork
statement: formalized
---

# The fppf quotient of a free action

For a free action, under the Yoneda embedding into fppf
sheaves, the quotient projection `X ⟶ X/G` is the coequalizer of the two maps `∐_g X ⇉ X` given by
the identity and by `σ g` on the component of `g`. Thus `X/G` represents the fppf quotient sheaf of
`X` by `G`.

```lean
TauCeti.InvariantQuotient.isColimitFppfYonedaCofork.{u, v} {X : AlgebraicGeometry.Scheme}
  {G : Type v} [Group G] [Finite G] {σ : G →* CategoryTheory.Aut X}
  (hσ : TauCeti.InvariantQuotient.HasInvariantAffineCover σ)
  (hG :
    ∀ (x : ↥X), ∃ U, x ∈ ↑U ∧ ∀ (g : G), g ≠ 1 → Ideal.span (Set.range fun a => g • a - a) = ⊤) :
  CategoryTheory.Limits.IsColimit
    (CategoryTheory.Limits.Cofork.ofπ
      (AlgebraicGeometry.Scheme.fppfTopology.yoneda.map (TauCeti.InvariantQuotient.projection σ hσ))
      ⋯)
```

## Depends on

- [TauCeti.InvariantQuotient.quotient](tauceti-invariantquotient-quotient.md)

## Proof depends on

- [Chase–Harrison–Rosenberg (`TauCeti.MulSemiringAction.tensorToPi_bijective`)](../../ring-theory/part-02/other-results/part-01/chase-harrison-rosenberg-tauceti-mulsemiringacti.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.InvariantQuotient.isColimitFppfYonedaCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Fppf.html#TauCeti.InvariantQuotient.isColimitFppfYonedaCofork).

## Sources

- [Tau Ceti documentation: `TauCeti.InvariantQuotient.isColimitFppfYonedaCofork`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Fppf.html#TauCeti.InvariantQuotient.isColimitFppfYonedaCofork)
- [Source of `TauCeti.InvariantQuotient.isColimitFppfYonedaCofork` in TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Fppf.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Quotient/FiniteGroup/Glued/Fppf.lean#L138)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
