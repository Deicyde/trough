---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.OneForm.sum_residue_preimage_support_pullback_sphere, TauCeti.RiemannSurface.OneForm.sum_residue_pullback_sphere
statement: formalized
proof: formalized
---

# The residue theorem for a pullback from the sphere

Let `F : X → ℙ¹` be a finite
holomorphic map from a compact Riemann surface and `η` a `1`-form meromorphic everywhere on the
sphere. Then the residues of `F^* η` over the preimage of the support of the divisor of `η` add
up to zero: over each fibre they add up to `deg F` times the residue of `η`
(`TauCeti.RiemannSurface.OneForm.sum_residue_pullback_eq_degree_mul`), and the residues of `η`
add up to zero (`TauCeti.RiemannSurface.OneForm.sum_residue_sphere`).

```lean
TauCeti.RiemannSurface.OneForm.sum_residue_preimage_support_pullback_sphere.{u_1} {X : Type u_1}
  [TopologicalSpace X] [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  [CompactSpace X] [T2Space X] {η : TauCeti.RiemannSurface.OneForm (OnePoint ℂ)}
  (F : TauCeti.RiemannSurface.FiniteHolomorphicMap X (OnePoint ℂ))
  (hη : ∀ (y : OnePoint ℂ), η.MeromorphicAt y) : ∑ x ∈ ⋯.toFinset, (η.pullback ↑F).residue x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The residue theorem on the Riemann sphere](the-residue-theorem-on-the-riemann-sphere.md)
- [Rouché's theorem for a disc, classical form](rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.OneForm.sum_residue_preimage_support_pullback_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.html#TauCeti.RiemannSurface.OneForm.sum_residue_preimage_support_pullback_sphere).

## Other forms

**The residue theorem for a pullback from the sphere, summed over the divisor of the pullback.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.OneForm.sum_residue_pullback_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.html#TauCeti.RiemannSurface.OneForm.sum_residue_pullback_sphere).

```lean
TauCeti.RiemannSurface.OneForm.sum_residue_pullback_sphere.{u_1} {X : Type u_1} [TopologicalSpace X]
  [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [CompactSpace X] [T2Space X]
  {η : TauCeti.RiemannSurface.OneForm (OnePoint ℂ)}
  (F : TauCeti.RiemannSurface.FiniteHolomorphicMap X (OnePoint ℂ))
  (hη : ∀ (y : OnePoint ℂ), η.MeromorphicAt y) :
  ∑ x ∈ (η.pullback ↑F).divisor.support, (η.pullback ↑F).residue x = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.OneForm.sum_residue_preimage_support_pullback_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.html#TauCeti.RiemannSurface.OneForm.sum_residue_preimage_support_pullback_sphere)
- [Source of `TauCeti.RiemannSurface.OneForm.sum_residue_preimage_support_pullback_sphere` in TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.lean#L141)
