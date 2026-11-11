---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.existsUnique_framedGaugeGroup_smul_eq
statement: formalized
proof: formalized
---

# Uniqueness of framed plane vortices with prescribed zeros, modulo framed gauge

Let `x`
and `y` be smooth solutions of the vortex equation on the plane with the same end framing
`α (z) · phase (z) → 1`, where `|phase| → 1` at infinity; for example `phase` is the winding
phase `(z / |z|) ^ (-m)`. If `n` is a multiplicity function for both sections, meaning that each of
them factors near every `z` as `(w - z) ^ n z * v w` with `v` continuous and nonzero at `z`, then
exactly one smooth framed gauge `u` satisfies `u • y = x`.

```lean
TauCeti.Vortex.existsUnique_framedGaugeGroup_smul_eq {x y : ℂ → EuclideanSpace ℝ (Fin 4)}
  (hx : ContDiff ℝ (↑⊤) x) (hy : ContDiff ℝ (↑⊤) y)
  (hxsol : ∀ (z : ℂ), TauCeti.Vortex.equation x z = 0)
  (hysol : ∀ (z : ℂ), TauCeti.Vortex.equation y z = 0) {phase : ℂ → ℂ}
  (hphase : Filter.Tendsto (fun z => ‖phase z‖) (Filter.cocompact ℂ) (nhds 1))
  (hxfr :
    Filter.Tendsto (fun z => TauCeti.Vortex.sectionValue x z * phase z) (Filter.cocompact ℂ)
      (nhds 1))
  (hyfr :
    Filter.Tendsto (fun z => TauCeti.Vortex.sectionValue y z * phase z) (Filter.cocompact ℂ)
      (nhds 1))
  {n : ℂ → ℕ}
  (hnx :
    ∀ (z : ℂ),
      ∃ v,
        ContinuousAt v z ∧
          v z ≠ 0 ∧ ∀ᶠ (w : ℂ) in nhds z, TauCeti.Vortex.sectionValue x w = (w - z) ^ n z * v w)
  (hny :
    ∀ (z : ℂ),
      ∃ v,
        ContinuousAt v z ∧
          v z ≠ 0 ∧ ∀ᶠ (w : ℂ) in nhds z, TauCeti.Vortex.sectionValue y w = (w - z) ^ n z * v w) :
  ∃! u, u • y = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula for a compactly supported `C¹` map `u : ℂ → F`](../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/the-cauchy-pompeiu-formula-for-a-compactly-suppo.md)
- [Liouville theorem under the sign condition `f · Δ f ≥ 0`](../../part-03/inner-product-space/part-02/liouville-theorem-under-the-sign-condition-f-f-0.md)
- [TauCeti.cauchyTransform](../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-cauchytransform.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.existsUnique_framedGaugeGroup_smul_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Uniqueness.html#TauCeti.Vortex.existsUnique_framedGaugeGroup_smul_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.existsUnique_framedGaugeGroup_smul_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Uniqueness.html#TauCeti.Vortex.existsUnique_framedGaugeGroup_smul_eq)
- [Source of `TauCeti.Vortex.existsUnique_framedGaugeGroup_smul_eq` in TauCeti/Analysis/PDE/Vortex/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/Uniqueness.lean#L229)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
