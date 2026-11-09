---
declaration: theorem
origin: cited
lean: TauCeti.toeplitz_comp_sub_toeplitz_eq_neg_classicalHankel_comp_classicalHankel
statement: formalized
proof: formalized
---

# Classical Toeplitz product identity

The product defect is minus the product of
the classical Hankel operator of the left symbol and that of the reflected right symbol.

```lean
TauCeti.toeplitz_comp_sub_toeplitz_eq_neg_classicalHankel_comp_classicalHankel
  (a b : ↥(MeasureTheory.Lp ℂ ⊤ AddCircle.haarAddCircle)) :
  TauCeti.toeplitz a ∘SL TauCeti.toeplitz b - TauCeti.toeplitz (a * b) =
    -TauCeti.classicalHankel a ∘SL
        TauCeti.classicalHankel ((MeasureTheory.Lp.compMeasurePreserving (fun t => -t) ⋯) b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.toeplitz_comp_sub_toeplitz_eq_neg_classicalHankel_comp_classicalHankel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Hankel/Classical.html#TauCeti.toeplitz_comp_sub_toeplitz_eq_neg_classicalHankel_comp_classicalHankel).

## Sources

- [Tau Ceti documentation: `TauCeti.toeplitz_comp_sub_toeplitz_eq_neg_classicalHankel_comp_classicalHankel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Hankel/Classical.html#TauCeti.toeplitz_comp_sub_toeplitz_eq_neg_classicalHankel_comp_classicalHankel)
- [Source of `TauCeti.toeplitz_comp_sub_toeplitz_eq_neg_classicalHankel_comp_classicalHankel` in TauCeti/Analysis/Fourier/Hardy/Hankel/Classical.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/Hardy/Hankel/Classical.lean#L121)
