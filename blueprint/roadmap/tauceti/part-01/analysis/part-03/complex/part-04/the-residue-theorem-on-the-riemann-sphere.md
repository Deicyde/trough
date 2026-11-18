---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.OneForm.sum_residue_sphere
statement: formalized
proof: formalized
---

# The residue theorem on the Riemann sphere

The residues of a `1`-form meromorphic
everywhere on `OnePoint ℂ` add up to zero; the residue at `∞` is read in the inverted chart.

```lean
TauCeti.RiemannSurface.OneForm.sum_residue_sphere {ω : TauCeti.RiemannSurface.OneForm (OnePoint ℂ)}
  (hω : ∀ (x : OnePoint ℂ), ω.MeromorphicAt x) : ∑ x ∈ ω.divisor.support, ω.residue x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The classical residue theorem for a null-homologous contour cycle](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-classical-residue-theorem-for-a-null-homolog.md)
- [Rouché's theorem for a disc, classical form](rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.OneForm.sum_residue_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.html#TauCeti.RiemannSurface.OneForm.sum_residue_sphere).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.OneForm.sum_residue_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.html#TauCeti.RiemannSurface.OneForm.sum_residue_sphere)
- [Source of `TauCeti.RiemannSurface.OneForm.sum_residue_sphere` in TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Sphere.lean#L77)
