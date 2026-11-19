---
declaration: theorem
origin: cited
lean: TauCeti.MemWkpLoc.exists_contDiffOn_ae_eq
statement: formalized
proof: formalized
---

# Morrey's embedding `W^{k+1,p}_loc ⊆ Cᵏ` for `p > 2`

A map `u ∈ MemWkpLoc p Ω (k + 1)`
agrees almost everywhere on `Ω` with a map `g` that is `Cᵏ` on `Ω`. For `k ≥ 1` the classical
derivative of `g` is a weak derivative of `u`
(`TauCeti.MemWkpLoc.hasWeakFDerivOn_fderiv_of_contDiffOn`), and the `k`-th derivative of `g` is
Hölder continuous with exponent `1 - 2 / p` on compact subsets of `Ω`
(`TauCeti.MemWkpLoc.exists_holderOnWith_iteratedFDeriv_of_isCompact`).

```lean
TauCeti.MemWkpLoc.exists_contDiffOn_ae_eq.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ENNReal} {Ω : TopologicalSpace.Opens ℂ} {k : ℕ} {u : ℂ → F}
  [FiniteDimensional ℝ F] (hp : 2 < p) (hu : TauCeti.MemWkpLoc p (↑Ω) (k + 1) u) :
  ∃ g, ContDiffOn ℝ (↑k) g ↑Ω ∧ u =ᵐ[MeasureTheory.volume.restrict ↑Ω] g
```

## Depends on

- [TauCeti.MemWkpLoc](tauceti-memwkploc.md)

## Proof depends on

- [The local Morrey inequality](../../part-04/sobolev/part-01/the-local-morrey-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MemWkpLoc.exists_contDiffOn_ae_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Morrey/Higher.html#TauCeti.MemWkpLoc.exists_contDiffOn_ae_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.MemWkpLoc.exists_contDiffOn_ae_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Morrey/Higher.html#TauCeti.MemWkpLoc.exists_contDiffOn_ae_eq)
- [Source of `TauCeti.MemWkpLoc.exists_contDiffOn_ae_eq` in TauCeti/Analysis/Sobolev/Local/Morrey/Higher.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Local/Morrey/Higher.lean#L77)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
