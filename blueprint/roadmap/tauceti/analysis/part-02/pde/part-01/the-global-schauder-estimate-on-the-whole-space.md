---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith, TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul
statement: formalized
proof: formalized
---

# The global Schauder estimate on the whole space

Let `0 < α < 1`, and let `λ`, `Λ` and
`L` be given. Then there is a constant `C`, depending only on `n`, `α`, `λ`, `Λ` and `L`, with the
following property. Let `a` be a matrix-valued coefficient on `ℝ^{n+1}` which is uniformly
elliptic and bounded with constants `0 < λ ≤ Λ` (`UniformlyEllipticOn univ a λ Λ`) and globally
`α`-Hölder entrywise with constant `L`, and put `L u = ∑ᵢⱼ aᵢⱼ ∂ᵢ∂ⱼu`. Let `u` be `C²` with
`|u| ≤ N`, and with `D²u` bounded and globally `α`-Hölder (with any constant). If `L u` is globally
`α`-Hölder with constant `K`, then `D²u` is globally `α`-Hölder with constant `C (K + N)`, and
`‖Du‖` and `‖D²u‖` are bounded by `C (K + N)`.

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (lam Lam : ℝ) (L : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K : NNReal},
            ContDiff ℝ 2 u →
              (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
                BddAbove (Set.range fun x => ‖iteratedFDeriv ℝ 2 u x‖) →
                  MemHolder α (iteratedFDeriv ℝ 2 u) →
                    (HolderWith K α fun x =>
                        ∑ i,
                          ∑ j,
                            a x i j •
                              ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                (EuclideanSpace.single j 1)) →
                      HolderWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u) ∧
                        (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖fderiv ℝ u x‖ ≤ ↑C * (↑K + ↑N)) ∧
                          ∀ (x : EuclideanSpace ℝ (Fin (n + 1))),
                            ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑C * (↑K + ↑N)
```

## Depends on

- [TauCeti.CkHolderSpace](../../../part-01/partial-differential-equations/tauceti-ckholderspace.md)

## Proof depends on

- [First-order Taylor bound for a Hölder derivative](../../other-results/first-order-taylor-bound-for-a-holder-derivative.md)
- [The interior Schauder estimate on small balls](the-interior-schauder-estimate-on-small-balls.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv).

## Other forms

**The global Schauder estimate in the `C_b^{2,α}` norm.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.html#TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv).

```lean
TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1)
  (lam Lam : ℝ) (L : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          ∀ (u : TauCeti.CkHolderSpace 2 α (EuclideanSpace ℝ (Fin (n + 1))) ℝ) {N K : NNReal},
            (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
              (HolderWith K α fun x =>
                  ∑ i,
                    ∑ j,
                      a x i j •
                        ((fderiv ℝ (fderiv ℝ ⇑u) x) (EuclideanSpace.single i 1))
                          (EuclideanSpace.single j 1)) →
                ‖u‖ ≤ ↑C * (↑K + ↑N)
```

**The global Schauder estimate with lower-order bounds.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith).

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (lam Lam : ℝ) (L : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K : NNReal},
            ContDiff ℝ 2 u →
              (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
                (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖fderiv ℝ u x‖ ≤ ↑N) →
                  (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
                    (∀ (S : Set (EuclideanSpace ℝ (Fin (n + 1)))),
                        IsCompact S → ∃ V, HolderOnWith V α (iteratedFDeriv ℝ 2 u) S) →
                      (HolderWith K α fun x =>
                          ∑ i,
                            ∑ j,
                              a x i j •
                                ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                  (EuclideanSpace.single j 1)) →
                        HolderWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u)
```

**The global Schauder estimate with lower-order terms on the whole space.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/LowerOrder.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul).

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul
  {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (lam Lam : ℝ) (L B : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
      {b : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))}
      {c : EuclideanSpace ℝ (Fin (n + 1)) → ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          HolderWith L α b →
            (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖b x‖ ≤ ↑B) →
              HolderWith L α c →
                (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |c x| ≤ ↑B) →
                  ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K : NNReal},
                    ContDiff ℝ 2 u →
                      (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
                        BddAbove (Set.range fun x => ‖iteratedFDeriv ℝ 2 u x‖) →
                          MemHolder α (iteratedFDeriv ℝ 2 u) →
                            (HolderWith K α fun x =>
                                ∑ i,
                                      ∑ j,
                                        a x i j •
                                          ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                            (EuclideanSpace.single j 1) +
                                    (fderiv ℝ u x) (b x) +
                                  c x * u x) →
                              HolderWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u) ∧
                                (∀ (x : EuclideanSpace ℝ (Fin (n + 1))),
                                    ‖fderiv ℝ u x‖ ≤ ↑C * (↑K + ↑N)) ∧
                                  ∀ (x : EuclideanSpace ℝ (Fin (n + 1))),
                                    ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑C * (↑K + ↑N)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv)
- [Source of `TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv` in TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.lean#L153)
