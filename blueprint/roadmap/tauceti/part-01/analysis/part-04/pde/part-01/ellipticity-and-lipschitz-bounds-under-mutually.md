---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_uniformlyEllipticOn_and_lipschitzOnWith_pullbackPrincipal
statement: formalized
proof: formalized
---

# Ellipticity and Lipschitz bounds under mutually inverse changes of variables

Let `Φ` and
`Ψ` be mutually inverse changes of variables, `Φ` of order one and `Ψ` of order two, with Jacobian
determinants at least one in absolute value, and let `Φ` map a nonempty subset `s` of a compact
convex subset of its domain into `t`. If `a` is uniformly elliptic and Lipschitz on `t`, the
pulled-back principal coefficient is uniformly elliptic and Lipschitz on `s`.

```lean
TauCeti.PDE.exists_uniformlyEllipticOn_and_lipschitzOnWith_pullbackPrincipal.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {U U' : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {Φ Ψ : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {L L' : ℝ} [Nonempty ι]
  (hΦ : TauCeti.Wkp.IsChangeOfVariables 1 U' U Φ L 1)
  (hΨ : TauCeti.Wkp.IsChangeOfVariables 2 U U' Ψ L' 1) (hΨΦ : Set.LeftInvOn Ψ Φ ↑U')
  (hΦΨ : Set.RightInvOn Ψ Φ ↑U) {B s t : Set (EuclideanSpace ℝ ι)} (hB : IsCompact B)
  (hBc : Convex ℝ B) (hBU : B ⊆ ↑U') (hs : s ⊆ B) (hsne : s.Nonempty) (hmaps : Set.MapsTo Φ s t)
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ} {K : NNReal}
  (ha : TauCeti.PDE.UniformlyEllipticOn t a lam Lam)
  (hK : LipschitzOnWith K (fun y => TauCeti.PDE.matrixBilinearForm (a y)) t) :
  ∃ lam' Lam' K',
    TauCeti.PDE.UniformlyEllipticOn s (TauCeti.PDE.pullbackPrincipal Φ a) lam' Lam' ∧
      LipschitzOnWith K'
        (fun x => TauCeti.PDE.matrixBilinearForm (TauCeti.PDE.pullbackPrincipal Φ a x)) s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_uniformlyEllipticOn_and_lipschitzOnWith_pullbackPrincipal`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/ChangeOfVariables.html#TauCeti.PDE.exists_uniformlyEllipticOn_and_lipschitzOnWith_pullbackPrincipal).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_uniformlyEllipticOn_and_lipschitzOnWith_pullbackPrincipal`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/ChangeOfVariables.html#TauCeti.PDE.exists_uniformlyEllipticOn_and_lipschitzOnWith_pullbackPrincipal)
- [Source of `TauCeti.PDE.exists_uniformlyEllipticOn_and_lipschitzOnWith_pullbackPrincipal` in TauCeti/Analysis/PDE/EnergyForm/ChangeOfVariables.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/EnergyForm/ChangeOfVariables.lean#L626)
