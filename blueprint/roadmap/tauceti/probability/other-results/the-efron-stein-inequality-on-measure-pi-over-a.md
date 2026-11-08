---
declaration: theorem
origin: cited
lean: TauCeti.Probability.efronStein
statement: formalized
proof: formalized
---

# The Efron–Stein inequality on `Measure.pi` over a finite index type

for a square
integrable measurable function `f` of independent coordinates, the variance of `f` is at most the
sum over `i` of the average variance of `f` in coordinate `i` with the other coordinates frozen.

```lean
TauCeti.Probability.efronStein.{u, u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι] {α : ι → Type u}
  [(i : ι) → MeasurableSpace (α i)] (μ : (i : ι) → MeasureTheory.Measure (α i))
  [∀ (i : ι), MeasureTheory.IsProbabilityMeasure (μ i)] {f : ((i : ι) → α i) → ℝ}
  (hf : Measurable f) (hL : MeasureTheory.MemLp f 2 (MeasureTheory.Measure.pi μ)) :
  ProbabilityTheory.evariance f (MeasureTheory.Measure.pi μ) ≤
    ∑ i,
      ∫⁻ (x : (i : ι) → α i),
        ProbabilityTheory.evariance (fun y => f (Function.update x i y))
          (μ i) ∂MeasureTheory.Measure.pi μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for Young's exponents](../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.efronStein`](https://taucetiproject.org/docs/TauCeti/Probability/Concentration/EfronStein.html#TauCeti.Probability.efronStein).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.efronStein`](https://taucetiproject.org/docs/TauCeti/Probability/Concentration/EfronStein.html#TauCeti.Probability.efronStein)
- [Source of `TauCeti.Probability.efronStein` in TauCeti/Probability/Concentration/EfronStein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Concentration/EfronStein.lean#L130)
