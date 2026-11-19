---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.IsEllipticAbove.memSobolev_smulLeftCLM
statement: formalized
proof: formalized
---

# Interior elliptic regularity

Let `p` be elliptic of order `m`, let `φ` be a compactly
supported Schwartz function, and let `a` be a symbol with compact spatial support that agrees with
`p` on a neighbourhood of `tsupport φ`. If `u ∈ H^t` and `Op(a) u ∈ H^{s - m}`, then `φ u ∈ H^s`,
for all real `s` and `t`.

```lean
TauCeti.Symbol.IsEllipticAbove.memSobolev_smulLeftCLM.{u_1, u_2} {n : ℕ} {V : Type u_1}
  {W : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℂ V] [CompleteSpace V]
  [NormedAddCommGroup W] [InnerProductSpace ℂ W] [CompleteSpace W] {m R : ℝ}
  {p a : TauCeti.Symbol n V W m} (hp : p.IsEllipticAbove R) (ha : a.HasCompactSpatialSupport)
  {φ : SchwartzMap (TauCeti.CoordinateSpace n) ℂ} (hφ : HasCompactSupport ⇑φ)
  (hap :
    ∀ᶠ (x : TauCeti.CoordinateSpace n) in nhdsSet (tsupport ⇑φ),
      ∀ (ξ : TauCeti.CoordinateSpace n), a.coefficient (x, ξ) = p.coefficient (x, ξ))
  {s t : ℝ} {u : BesselPotentialSpace (TauCeti.CoordinateSpace n) V t 2}
  (hu : TemperedDistribution.MemSobolev (s - m) 2 ↑((a.quantizeSobolev ha t) u)) :
  TemperedDistribution.MemSobolev s 2 ↑((BesselPotentialSpace.smulLeftCLM t φ) u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [An elliptic symbol has a two-sided parametrix symbol](an-elliptic-symbol-has-a-two-sided-parametrix-sy.md)
- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../part-04/special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)
- [Plancherel's theorem for the inverse Fourier transform of Schwartz functions](../../part-03/distribution/plancherels-theorem-for-the-inverse-fourier-tran.md)
- [The Sobolev estimate on Schwartz functions](../../part-04/pseudodifferential/the-sobolev-estimate-on-schwartz-functions.md)
- [The weighted Plancherel bound](../../part-03/distribution/the-weighted-plancherel-bound.md)
- [Young's convolution inequality](../../part-03/convolution/youngs-convolution-inequality.md)
- [Young's inequality for integral kernels](../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.IsEllipticAbove.memSobolev_smulLeftCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/EllipticRegularity.html#TauCeti.Symbol.IsEllipticAbove.memSobolev_smulLeftCLM).

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.IsEllipticAbove.memSobolev_smulLeftCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/EllipticRegularity.html#TauCeti.Symbol.IsEllipticAbove.memSobolev_smulLeftCLM)
- [Source of `TauCeti.Symbol.IsEllipticAbove.memSobolev_smulLeftCLM` in TauCeti/Analysis/Pseudodifferential/EllipticRegularity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Pseudodifferential/EllipticRegularity.lean#L106)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
