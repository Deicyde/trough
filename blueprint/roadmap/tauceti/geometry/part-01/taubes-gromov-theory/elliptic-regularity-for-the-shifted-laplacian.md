---
declaration: theorem
origin: cited
lean: TemperedDistribution.memSobolev_add_two_iff_neg_laplacian_add_smul
statement: formalized
proof: formalized
---

# Elliptic regularity for the shifted Laplacian

for `c > 0`, a tempered distribution `f`
lies in the Sobolev space `H^{s+2}` if and only if `-Δ f + c f` lies in `H^s`.

```lean
TemperedDistribution.memSobolev_add_two_iff_neg_laplacian_add_smul.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℂ F]
  [CompleteSpace F] {c s : ℝ} (hc : 0 < c) {f : TemperedDistribution E F} :
  TemperedDistribution.MemSobolev (s + 2) 2 f ↔
    TemperedDistribution.MemSobolev s 2 (-Laplacian.laplacian f + c • f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TemperedDistribution.laplacianResolvent](tempereddistribution-laplacianresolvent.md)

## Lean

Formalized in Tau Ceti as [`TemperedDistribution.memSobolev_add_two_iff_neg_laplacian_add_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.html#TemperedDistribution.memSobolev_add_two_iff_neg_laplacian_add_smul).

## Sources

- [Tau Ceti documentation: `TemperedDistribution.memSobolev_add_two_iff_neg_laplacian_add_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.html#TemperedDistribution.memSobolev_add_two_iff_neg_laplacian_add_smul)
- [Source of `TemperedDistribution.memSobolev_add_two_iff_neg_laplacian_add_smul` in TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.lean#L183)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
