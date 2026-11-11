---
declaration: theorem
origin: cited
lean: TauCeti.PDE.UniformlyEllipticOn.exists_forall_energyFormH1_eq_iff
statement: formalized
proof: formalized
---

# The Fredholm compatibility condition for uniformly elliptic operators

On a bounded open
set, let `a` be uniformly elliptic and let `b` and `c` be bounded and measurable, with no sign
condition on `c` and no smallness of `b`. For `ℓ ∈ H⁻¹(Ω)` the weak problem `B(u, ·) = ℓ` for
`-∂ᵢ(aⁱʲ ∂ⱼu) + bⁱ ∂ᵢu + c u` has a solution `u ∈ H¹₀(Ω)` exactly when `ℓ` vanishes on the weak
adjoint kernel `{w | ∀ v, B(v, w) = 0}`.

```lean
TauCeti.PDE.UniformlyEllipticOn.exists_forall_energyFormH1_eq_iff.{u_1} {ι : Type u_1} [Fintype ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c : EuclideanSpace ℝ ι → ℝ} [DecidableEq ι]
  {lam Lam beta gamma : ℝ} (h : TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam)
  (ha : MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega))
  (hb : MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega))
  (hc : MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega))
  (hb_bound : ∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) (hc_bound : ∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma)
  (hOmega : Bornology.IsBounded ↑Omega) (ℓ : StrongDual ℝ ↥(TauCeti.W1p0 mu Omega 2)) :
  (∃ u, ∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a b c ↑u ↑v = ℓ v) ↔
    ∀ (w : ↥(TauCeti.W1p0 mu Omega 2)),
      (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a b c ↑v ↑w = 0) → ℓ w = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gårding's inequality on `H¹(Ω)`](../../part-03/pde/part-01/gardings-inequality-on-h1.md)
- [Rellich–Kondrachov on bounded Lipschitz domains](../../part-03/sobolev/part-02/rellich-kondrachov-on-bounded-lipschitz-domains.md)
- [Riesz--Schauder](../../part-03/fredholm/riesz-schauder.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.UniformlyEllipticOn.exists_forall_energyFormH1_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/FredholmAlternative.html#TauCeti.PDE.UniformlyEllipticOn.exists_forall_energyFormH1_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.UniformlyEllipticOn.exists_forall_energyFormH1_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/FredholmAlternative.html#TauCeti.PDE.UniformlyEllipticOn.exists_forall_energyFormH1_eq_iff)
- [Source of `TauCeti.PDE.UniformlyEllipticOn.exists_forall_energyFormH1_eq_iff` in TauCeti/Analysis/PDE/FredholmAlternative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/FredholmAlternative.lean#L328)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)
