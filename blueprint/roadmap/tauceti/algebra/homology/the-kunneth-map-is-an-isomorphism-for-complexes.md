---
declaration: theorem
origin: cited
lean: HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero, HomologicalComplex.isIso_homologyKunneth_of_homotopyEquiv_of_d_eq_zero
statement: formalized
proof: formalized
---

# The Künneth map is an isomorphism for complexes with zero differentials

then
`Hₙ(K ⊗ L) = (K ⊗ L)ₙ` is the direct sum of the `K.X p ⊗ L.X q = Hₚ(K) ⊗ H_q(L)` with
`p + q = n`.

```lean
HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero.{v_1, u_1, u_2} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C] {I : Type u_2}
  [AddMonoid I] {c : ComplexShape I} [c.TensorSigns] [DecidableEq I] {K L : HomologicalComplex C c}
  [K.HasTensor L] (n : I) [∀ (p : I), K.HasHomology p] [∀ (q : I), L.HasHomology q]
  [(K.tensorObj L).HasHomology n]
  [∀ (p : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorLeft (K.homology p))]
  [∀ (q : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorRight (L.cycles q))]
  [∀ (q : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorRight (L.X (c.prev q)))]
  [CategoryTheory.GradedObject.HasTensor (fun p => K.homology p) fun q => L.homology q]
  (hK : ∀ (i j : I), K.d i j = 0) (hL : ∀ (i j : I), L.d i j = 0) :
  CategoryTheory.IsIso (K.homologyKunneth L n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.html#HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero).

## Other forms

**The Künneth map is an isomorphism for complexes homotopy equivalent to complexes with zero differentials.** Formalized in Tau Ceti as [`HomologicalComplex.isIso_homologyKunneth_of_homotopyEquiv_of_d_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.html#HomologicalComplex.isIso_homologyKunneth_of_homotopyEquiv_of_d_eq_zero).

```lean
HomologicalComplex.isIso_homologyKunneth_of_homotopyEquiv_of_d_eq_zero.{v_1, u_1, u_2}
  {C : Type u_1} [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C] {I : Type u_2}
  [AddMonoid I] {c : ComplexShape I} [c.TensorSigns] [DecidableEq I]
  {K L K' L' : HomologicalComplex C c} [K.HasTensor L] [K'.HasTensor L'] (n : I)
  [∀ (p : I), K.HasHomology p] [∀ (q : I), L.HasHomology q] [(K.tensorObj L).HasHomology n]
  [∀ (p : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorLeft (K.homology p))]
  [∀ (q : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorRight (L.cycles q))]
  [∀ (q : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorRight (L.X (c.prev q)))]
  [CategoryTheory.GradedObject.HasTensor (fun p => K.homology p) fun q => L.homology q]
  [∀ (p : I), K'.HasHomology p] [∀ (q : I), L'.HasHomology q] [(K'.tensorObj L').HasHomology n]
  [∀ (p : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorLeft (K'.homology p))]
  [∀ (q : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorRight (L'.cycles q))]
  [∀ (q : I),
      CategoryTheory.Limits.PreservesColimitsOfShape CategoryTheory.Limits.WalkingParallelPair
        (CategoryTheory.MonoidalCategory.tensorRight (L'.X (c.prev q)))]
  [CategoryTheory.GradedObject.HasTensor (fun p => K'.homology p) fun q => L'.homology q]
  (eK : HomotopyEquiv K K') (eL : HomotopyEquiv L L') (hK' : ∀ (i j : I), K'.d i j = 0)
  (hL' : ∀ (i j : I), L'.d i j = 0) : CategoryTheory.IsIso (K.homologyKunneth L n)
```

## Sources

- [Tau Ceti documentation: `HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.html#HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero)
- [Source of `HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero` in TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.lean#L209)
