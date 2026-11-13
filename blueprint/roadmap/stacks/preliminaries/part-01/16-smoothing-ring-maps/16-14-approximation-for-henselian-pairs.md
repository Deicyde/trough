---
declaration: section
origin: cited
lean: Stacks.Smoothing.exists_solution_of_henselianPair_of_isRegularRingMap, Stacks.Smoothing.exists_solution_of_henselianPair_of_isGRing, Stacks.Smoothing.exists_solution_of_henselianPair_of_isGRing_henselization
statement: formalized
proof: formalized
---

# 16.14 Approximation for henselian pairs

Section 16.14 of the Stacks Project, [Tag 0AH4](https://stacks.math.columbia.edu/tag/0AH4). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AH5, a lemma

[Tag 0AH5](https://stacks.math.columbia.edu/tag/0AH5) in the Stacks Project.

**`Stacks.Smoothing.exists_solution_of_henselianPair_of_isRegularRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean#L165). The attribute's comment: “the conclusion under the source's FIRST alternative hypothesis, that `A → A^∧` is a regular ring map, with no other hypothesis: the appeal to Popescu's Theorem 07GC that the source makes here is `indSmooth_of_isRegularRingMap`, which is proved. Regularity is the Situation 07F2 spelling `IsRegularRingMap`, reached from the general `IsRegularRingHom` of 07BJ by the public `isRegularRingMap_of_regularRingHom`. The conclusion is the full one: a solution in `A` of the same system, congruent to the given one modulo the extension of `I ^ N` to `A^∧`, for every `N ≥ 1`. See also the two sibling wrappers for the source's other two alternatives.”.

> **Stacks 0AH5 under the source's first hypothesis.** Let `(A, I)` be a henselian pair with
> `A` Noetherian such that `A → A^∧` is a regular ring map. A system of polynomial equations over
> `A` with a solution in the completion has, for every `N ≥ 1`, a solution in `A` congruent to it
> modulo `I ^ N`.

```lean
theorem exists_solution_of_henselianPair_of_isRegularRingMap
    {A : Type u} [CommRing A] {I : Ideal A} [IsNoetherianRing A]
    (hAI : HenselianPair A I) (hreg : IsRegularRingMap A (AdicCompletion I A))
    {m n : ℕ} (f : Fin m → MvPolynomial (Fin n) A)
    (â : Fin n → AdicCompletion I A) (hâ : ∀ j, MvPolynomial.aeval â (f j) = 0)
    {N : ℕ} (hN : N ≠ 0) :
    ∃ a : Fin n → A,
      (∀ i, â i - algebraMap A (AdicCompletion I A) (a i) ∈
        (I ^ N).map (algebraMap A (AdicCompletion I A))) ∧
      ∀ j, MvPolynomial.aeval a (f j) = 0
```

**`Stacks.Smoothing.exists_solution_of_henselianPair_of_isGRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean#L187). The attribute's comment: “the conclusion under the source's SECOND alternative hypothesis, that `A` is a Noetherian G-ring (`IsGRing`, Tag 07GH, whose first component is Noetherianness), with no other hypothesis. The source's reduction (2) ⟹ (1) is Lemma 0AH2 (`isRegularRingHom_algebraMap_adicCompletion`), and the appeal to Popescu's Theorem 07GC is `indSmooth_of_isRegularRingMap`, which is proved. The conclusion is the full one, as in the sibling wrapper for alternative (1).”.

> **Stacks 0AH5 under the source's second hypothesis.** Let `(A, I)` be a henselian pair with
> `A` a Noetherian G-ring. A system of polynomial equations over `A` with a solution in the
> completion has, for every `N ≥ 1`, a solution in `A` congruent to it modulo `I ^ N`.

```lean
theorem exists_solution_of_henselianPair_of_isGRing
    {A : Type u} [CommRing A] {I : Ideal A} (hG : IsGRing A) (hAI : HenselianPair A I)
    {m n : ℕ} (f : Fin m → MvPolynomial (Fin n) A)
    (â : Fin n → AdicCompletion I A) (hâ : ∀ j, MvPolynomial.aeval â (f j) = 0)
    {N : ℕ} (hN : N ≠ 0) :
    ∃ a : Fin n → A,
      (∀ i, â i - algebraMap A (AdicCompletion I A) (a i) ∈
        (I ^ N).map (algebraMap A (AdicCompletion I A))) ∧
      ∀ j, MvPolynomial.aeval a (f j) = 0
```

**`Stacks.Smoothing.exists_solution_of_henselianPair_of_isGRing_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean#L211). The attribute's comment: “the conclusion under the source's THIRD alternative hypothesis, that `(A, I)` is the henselization of a pair `(C, J)` with `C` a Noetherian G-ring, with no other hypothesis. The henselization is described exactly as in Lemma 0AH3 (`isGRing_henselization`): the pair `(A, J A)` is henselian and `A` has the universal property of the henselization of `(C, J)`, which is the datum `exists_henselization` (Tag 0A02) produces. The source's reduction (3) ⟹ (2) is that lemma, (2) ⟹ (1) is Lemma 0AH2, and the appeal to Popescu's Theorem 07GC is `indSmooth_of_isRegularRingMap`, which is proved. The conclusion is the full one, as in the sibling wrappers for alternatives (1) and (2).”.

> **Stacks 0AH5 under the source's third hypothesis.** Let `C` be a Noetherian G-ring, let
> `J ⊂ C` be an ideal and let `A` be a henselization of the pair `(C, J)`. A system of polynomial
> equations over `A` with a solution in the `J A`-adic completion of `A` has, for every `N ≥ 1`, a
> solution in `A` congruent to it modulo `(J A) ^ N`.

```lean
theorem exists_solution_of_henselianPair_of_isGRing_henselization
    {C : Type u} [CommRing C] (hC : IsGRing C) (J : Ideal C)
    (A : Type u) [CommRing A] [Algebra C A]
    (hh : HenselianPair A (J.map (algebraMap C A)))
    (hι : ∀ (B : Type u) (_ : CommRing B) (K : Ideal B), HenselianPair B K →
      ∀ g : C →+* B, J ≤ K.comap g →
        ∃! t : A →+* B, t.comp (algebraMap C A) = g ∧ J.map (algebraMap C A) ≤ K.comap t)
    {m n : ℕ} (f : Fin m → MvPolynomial (Fin n) A)
    (â : Fin n → AdicCompletion (J.map (algebraMap C A)) A)
    (hâ : ∀ j, MvPolynomial.aeval â (f j) = 0) {N : ℕ} (hN : N ≠ 0) :
    ∃ a : Fin n → A,
      (∀ i, â i - algebraMap A (AdicCompletion (J.map (algebraMap C A)) A) (a i) ∈
        ((J.map (algebraMap C A)) ^ N).map
          (algebraMap A (AdicCompletion (J.map (algebraMap C A)) A))) ∧
      ∀ j, MvPolynomial.aeval a (f j) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.14, Tag 0AH4](https://stacks.math.columbia.edu/tag/0AH4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
