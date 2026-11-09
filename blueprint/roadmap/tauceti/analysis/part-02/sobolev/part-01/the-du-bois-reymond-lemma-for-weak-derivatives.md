---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakLineDerivOn.exists_ae_eq_const
statement: formalized
proof: formalized
---

# The du Bois-Reymond lemma for weak derivatives

A function whose weak derivative on
`Ioo a b` is `0` is almost everywhere equal to a constant on `Ioo a b`.

```lean
TauCeti.HasWeakLineDerivOn.exists_ae_eq_const.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {a b : ℝ} {u : ℝ → F}
  (h :
    TauCeti.HasWeakLineDerivOn MeasureTheory.volume { carrier := Set.Ioo a b, is_open' := ⋯ } u 0
      1) :
  ∃ c, u =ᵐ[MeasureTheory.volume.restrict (Set.Ioo a b)] fun x => c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../distribution/the-du-bois-reymond-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakLineDerivOn.exists_ae_eq_const`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.exists_ae_eq_const).

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakLineDerivOn.exists_ae_eq_const`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.html#TauCeti.HasWeakLineDerivOn.exists_ae_eq_const)
- [Source of `TauCeti.HasWeakLineDerivOn.exists_ae_eq_const` in TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/WeakDeriv/Interval.lean#L190)
