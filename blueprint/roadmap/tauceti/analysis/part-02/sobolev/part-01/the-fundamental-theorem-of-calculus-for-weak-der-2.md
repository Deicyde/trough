---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_top
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus for weak derivatives on the line

If `u'` is the weak
derivative of `u` on all of `ℝ`, then `u` is almost everywhere equal to a constant plus the
primitive `t ↦ ∫ s in t₀..t, u' s`, for any base point `t₀`.

```lean
TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_top.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {u u' : ℝ → F}
  (h : TauCeti.HasWeakLineDerivOn MeasureTheory.volume ⊤ u u' 1) (t₀ : ℝ) :
  ∃ c, u =ᵐ[MeasureTheory.volume] fun t => c + ∫ (s : ℝ) in t₀..t, u' s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for weak derivatives](the-fundamental-theorem-of-calculus-for-weak-der.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_top`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_top).

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_top`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_top)
- [Source of `TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_top` in TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean#L241)
