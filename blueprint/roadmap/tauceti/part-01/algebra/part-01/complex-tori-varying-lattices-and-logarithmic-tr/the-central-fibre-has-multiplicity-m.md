---
declaration: theorem
origin: cited
lean: TauCeti.analyticOrderAt_torusFamilyAffineQuotientLift_rootsOfUnityBall
statement: formalized
proof: formalized
---

# The central fibre has multiplicity `m`

Let `x` be a point of the central fibre of the
cyclic quotient `Q = X / C_m`, the fibre over `0` of the map `p_Q : Q → ℂ` induced by
`z ↦ z ^ m`, and let `e` be a chart of the quotient atlas at `x`. Along the transverse line
`u ↦ e.symm (u, v₀)` through `x`, where `v₀` is the fibre coordinate of `x`, the function `p_Q`
vanishes at `u = 0` to order exactly `m`.

```lean
TauCeti.analyticOrderAt_torusFamilyAffineQuotientLift_rootsOfUnityBall.{u_1, u_2} {m : ℕ} [NeZero m]
  {r : ℝ} {Λ : Type u_1} [AddCommGroup Λ] [Module.Free ℤ Λ] [Module.Finite ℤ Λ] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E]
  (P : ↥(TauCeti.rootsOfUnityBall m r) → Λ →ₗ[ℤ] E)
  [∀ (z : ↥(TauCeti.rootsOfUnityBall m r)), DiscreteTopology ↥(P z).range]
  [∀ (z : ↥(TauCeti.rootsOfUnityBall m r)), IsZLattice ℝ (P z).range]
  (hcont : ∀ (l : Λ), Continuous fun z => (P z) l)
  (hinj : ∀ (z : ↥(TauCeti.rootsOfUnityBall m r)), Function.Injective ⇑(P z))
  (R : ↥(rootsOfUnity m ℂ) → ↥(TauCeti.rootsOfUnityBall m r) → E →+ E)
  (ρ : Representation ℤ (↥(rootsOfUnity m ℂ)) Λ)
  (hequiv :
    ∀ (g : ↥(rootsOfUnity m ℂ)) (z : ↥(TauCeti.rootsOfUnityBall m r)) (l : Λ),
      (P (g • z)) ((ρ g) l) = (R g z) ((P z) l))
  (b :
    ↥(rootsOfUnity m ℂ) →
      ↥(TauCeti.rootsOfUnityBall m r) →
        AddAction.orbitRel.Quotient Λ (↥(TauCeti.rootsOfUnityBall m r) × E))
  (hb :
    ∀ (g : ↥(rootsOfUnity m ℂ)) (z : ↥(TauCeti.rootsOfUnityBall m r)),
      TauCeti.torusFamilyProjection P (b g z) = g • z)
  (hone : ∀ (z : ↥(TauCeti.rootsOfUnityBall m r)) (v : E), (R 1 z) v = v)
  (hmul :
    ∀ (g h : ↥(rootsOfUnity m ℂ)) (z : ↥(TauCeti.rootsOfUnityBall m r)) (v : E),
      (R (g * h) z) v = (R g (h • z)) ((R h z) v))
  (hbone : ∀ (z : ↥(TauCeti.rootsOfUnityBall m r)), b 1 z = ⟦(z, 0)⟧)
  (hbmul :
    ∀ (g h : ↥(rootsOfUnity m ℂ)) (z : ↥(TauCeti.rootsOfUnityBall m r)),
      b (g * h) z = TauCeti.torusFamilyAffineMap R P ρ hequiv b hb g (b h z))
  (hRc : ∀ (g : ↥(rootsOfUnity m ℂ)), Continuous fun p => (R g p.1) p.2)
  (hbc : ∀ (g : ↥(rootsOfUnity m ℂ)), Continuous (b g))
  (hfree :
    IsCancelSMul (↥(rootsOfUnity m ℂ))
      (AddAction.orbitRel.Quotient Λ (↥(TauCeti.rootsOfUnityBall m r) × E)))
  {e :
    OpenPartialHomeomorph
      (MulAction.orbitRel.Quotient (↥(rootsOfUnity m ℂ))
        (AddAction.orbitRel.Quotient Λ (↥(TauCeti.rootsOfUnityBall m r) × E)))
      (ModelProd ℂ E)}
  (he :
    e ∈
      atlas (ModelProd ℂ E)
        (MulAction.orbitRel.Quotient (↥(rootsOfUnity m ℂ))
          (AddAction.orbitRel.Quotient Λ (↥(TauCeti.rootsOfUnityBall m r) × E))))
  {x :
    MulAction.orbitRel.Quotient (↥(rootsOfUnity m ℂ))
      (AddAction.orbitRel.Quotient Λ (↥(TauCeti.rootsOfUnityBall m r) × E))}
  (hx : x ∈ e.source)
  (hx0 :
    TauCeti.torusFamilyAffineQuotientLift P R ρ hequiv b hb hone hmul hbone hbmul (fun z => ↑z ^ m)
        ⋯ x =
      0) :
  analyticOrderAt
      (fun u =>
        TauCeti.torusFamilyAffineQuotientLift P R ρ hequiv b hb hone hmul hbone hbmul
          (fun z => ↑z ^ m) ⋯ (↑e.symm (u, (↑e x).2)))
      0 =
    ↑m
```

## Depends on

- [The affine action](the-affine-action.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.analyticOrderAt_torusFamilyAffineQuotientLift_rootsOfUnityBall`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/RotatedDisc.html#TauCeti.analyticOrderAt_torusFamilyAffineQuotientLift_rootsOfUnityBall).

## Sources

- [Tau Ceti documentation: `TauCeti.analyticOrderAt_torusFamilyAffineQuotientLift_rootsOfUnityBall`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/RotatedDisc.html#TauCeti.analyticOrderAt_torusFamilyAffineQuotientLift_rootsOfUnityBall)
- [Source of `TauCeti.analyticOrderAt_torusFamilyAffineQuotientLift_rootsOfUnityBall` in TauCeti/Algebra/Module/ZLattice/Family/RotatedDisc.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/Family/RotatedDisc.lean#L404)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
