---
declaration: theorem
origin: cited
lean: Submodule.restrictedFamilyMkQ_surjective
statement: formalized
proof: formalized
---

# Submodule.restrictedFamilyMkQ_surjective

Closed coefficient quotients induce surjections of algebraic restricted families, without
any positivity assumption on the radii.

```lean
Submodule.restrictedFamilyMkQ_surjective.{u_1, u_2, u_3} {σ : Type u_1} {R : Type u_2}
  {E : Type u_3} [SeminormedRing R] [SeminormedAddCommGroup E] [_root_.Module R E]
  [IsBoundedSMul R E] {c : σ → ℝ} (N : Submodule R E) [IsClosed ↑N] :
  Function.Surjective ⇑N.restrictedFamilyMkQ
```

## Depends on

- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)

## Lean

Formalized in Tau Ceti as [`Submodule.restrictedFamilyMkQ_surjective`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Quotient.html#Submodule.restrictedFamilyMkQ_surjective).

## Sources

- [Tau Ceti documentation: `Submodule.restrictedFamilyMkQ_surjective`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Quotient.html#Submodule.restrictedFamilyMkQ_surjective)
- [Source of `Submodule.restrictedFamilyMkQ_surjective` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Quotient.lean#L101)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
