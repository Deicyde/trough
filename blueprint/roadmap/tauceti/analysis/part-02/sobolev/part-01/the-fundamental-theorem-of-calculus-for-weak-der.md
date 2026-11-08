---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral, TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_left
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus for weak derivatives

If `u'` is the weak derivative
of `u` on `Ioo a b` and `t₀ ∈ Ioo a b`, then `u` is almost everywhere on `Ioo a b` equal to a
constant plus the primitive `t ↦ ∫ s in t₀..t, u' s`.

```lean
TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {a b t₀ : ℝ} {u u' : ℝ → F}
  (h :
    TauCeti.HasWeakLineDerivOn MeasureTheory.volume { carrier := Set.Ioo a b, is_open' := ⋯ } u u'
      1)
  (ht₀ : t₀ ∈ Set.Ioo a b) :
  ∃ c, u =ᵐ[MeasureTheory.volume.restrict (Set.Ioo a b)] fun t => c + ∫ (s : ℝ) in t₀..t, u' s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-01/integral-currents-geometric-homology-and-minimiz/the-du-bois-reymond-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral).

## Other forms

**The fundamental theorem of calculus for weak derivatives, from the left endpoint.** Formalized in Tau Ceti as [`TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_left`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_left).

```lean
TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral_left.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] {a b : ℝ} {u u' : ℝ → F}
  (h :
    TauCeti.HasWeakLineDerivOn MeasureTheory.volume { carrier := Set.Ioo a b, is_open' := ⋯ } u u'
      1)
  (hu' : MeasureTheory.IntegrableOn u' (Set.Ioo a b) MeasureTheory.volume) :
  ∃ c, u =ᵐ[MeasureTheory.volume.restrict (Set.Ioo a b)] fun t => c + ∫ (s : ℝ) in a..t, u' s
```

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral)
- [Source of `TauCeti.HasWeakLineDerivOn.exists_ae_eq_add_intervalIntegral` in TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean#L202)
