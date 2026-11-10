---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakLineDerivOn.integral_eq_sub
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus for a continuous representative

Let `u'` be the weak
derivative of `u` on `Ioo a b`, integrable on `Ioo a b`, and let `v` be continuous on `Icc a b`
and equal to `u` almost everywhere on `Ioo a b`. Then `∫ r in s..t, u' r = v t - v s` for all
`s, t ∈ Icc a b`.

```lean
TauCeti.HasWeakLineDerivOn.integral_eq_sub.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {a b : ℝ} {u u' v : ℝ → F}
  (h :
    TauCeti.HasWeakLineDerivOn MeasureTheory.volume { carrier := Set.Ioo a b, is_open' := ⋯ } u u'
      1)
  (hu' : MeasureTheory.IntegrableOn u' (Set.Ioo a b) MeasureTheory.volume)
  (hv : ContinuousOn v (Set.Icc a b)) (hae : u =ᵐ[MeasureTheory.volume.restrict (Set.Ioo a b)] v)
  {s t : ℝ} (hs : s ∈ Set.Icc a b) (ht : t ∈ Set.Icc a b) : ∫ (r : ℝ) in s..t, u' r = v t - v s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for weak derivatives](the-fundamental-theorem-of-calculus-for-weak-der.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakLineDerivOn.integral_eq_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.integral_eq_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakLineDerivOn.integral_eq_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.integral_eq_sub)
- [Source of `TauCeti.HasWeakLineDerivOn.integral_eq_sub` in TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean#L284)
