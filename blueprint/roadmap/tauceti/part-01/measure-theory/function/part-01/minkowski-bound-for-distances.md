---
declaration: theorem
origin: cited
lean: MeasureTheory.eLpNorm_edist_le_add
statement: formalized
proof: formalized
---

# Minkowski bound for distances

For maps `f g f' g' : α → Y` into a pseudo-emetric space
and `1 ≤ p`, the `Lᵖ(μ)` seminorm of `x ↦ edist (f' x) (g' x)` is at most that of
`x ↦ edist (f x) (g x)` plus those of the two displacements `x ↦ edist (f x) (f' x)` and
`x ↦ edist (g x) (g' x)`.

```lean
MeasureTheory.eLpNorm_edist_le_add.{u_1, u_2} {α : Type u_1} {Y : Type u_2} {m : MeasurableSpace α}
  [PseudoEMetricSpace Y] {p : ENNReal} {μ : MeasureTheory.Measure α} {f g f' g' : α → Y}
  (hp1 : 1 ≤ p) (hmeas : MeasureTheory.AEStronglyMeasurable (fun x => edist (f' x) (g' x)) μ) :
  MeasureTheory.eLpNorm (fun x => edist (f' x) (g' x)) p μ ≤
    MeasureTheory.eLpNorm (fun x => edist (f x) (g x)) p μ +
      (MeasureTheory.eLpNorm (fun x => edist (f x) (f' x)) p μ +
        MeasureTheory.eLpNorm (fun x => edist (g x) (g' x)) p μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.eLpNorm_edist_le_add`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSeminorm/EDist.html#MeasureTheory.eLpNorm_edist_le_add).

## Sources

- [Tau Ceti documentation: `MeasureTheory.eLpNorm_edist_le_add`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/LpSeminorm/EDist.html#MeasureTheory.eLpNorm_edist_le_add)
- [Source of `MeasureTheory.eLpNorm_edist_le_add` in TauCeti/MeasureTheory/Function/LpSeminorm/EDist.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/LpSeminorm/EDist.lean#L64)
