---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleCohomology_rootsOfUnity_smoothProjectiveCurve_of_genus, Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod, Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod_curveKummerCoboundary, AlgebraicGeometry.baseRootsToEtaleH0_bijective_of_isCurve, Stacks.Kummer.subsingleton_sheafH_rootsOfUnitySheaf_of_isCurve, Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod_rootsOfUnityRestriction, AlgebraicGeometry.etaleCohomology_rootsOfUnity_affineSmoothCurve_of_compactification, AlgebraicGeometry.etaleH0EquivRootsOfUnitySections_val
statement: formalized
proof: formalized
---

# 59.69 Picard groups of curves

Section 59.69 of the Stacks Project, [Tag 03RN](https://stacks.math.columbia.edu/tag/03RN). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03RQ, a lemma

[Tag 03RQ](https://stacks.math.columbia.edu/tag/03RQ) in the Stacks Project.

**`AlgebraicGeometry.etaleCohomology_rootsOfUnity_smoothProjectiveCurve_of_genus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/RootsOfUnityCurvesFinal.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/RootsOfUnityCurvesFinal.lean#L91).

> **Stacks Project, Tag 03RQ.** Let `X` be a smooth projective curve of genus `g` over an
> algebraically closed field `k` and let `n ∈ k^*`. Then
> `H⁰_ét(X, μ_n) = μ_n(k)`, `H¹_ét(X, μ_n) = Pic⁰(X)[n] ≅ (𝐙/n𝐙)^{2g}`,
> `H²_ét(X, μ_n) ≅ 𝐙/n𝐙` (by the degree), `H^q_ét(X, μ_n) = 0` for `q ≥ 3`; and the same groups
> for the constant sheaf `𝐙/n𝐙`: `𝐙/n𝐙`, `(𝐙/n𝐙)^{2g}`, `𝐙/n𝐙` and `0` for `q ≥ 3`.

```lean
theorem etaleCohomology_rootsOfUnity_smoothProjectiveCurve_of_genus (hn : IsUnit (n : k)) :
    Function.Bijective (baseRootsToEtaleH0 E k X hX f n) ∧
      Function.Bijective (etaleH1RootsOfUnityToCurvePicardDegreeZeroTorsion k X f E hX n hn) ∧
      (∃ e : Sheaf.H (kummerSmallEtale E X hX n).X₁ 2 ≃+ ZMod n,
        ∀ x, e (etaleH2RootsOfUnityFromPicard k X f E hX n hn x) = picardDegreeZMod k X f n x) ∧
      (∀ q, 3 ≤ q → Subsingleton (Sheaf.H (kummerSmallEtale E X hX n).X₁ q)) ∧
      Nonempty (Sheaf.H (smallEtaleConstantZModSheaf E X hX n) 0 ≃+ ZMod n) ∧
      Nonempty (Sheaf.H (smallEtaleConstantZModSheaf E X hX n) 1 ≃+
        (Fin (2 * genus f) → ZMod n)) ∧
      Nonempty (Sheaf.H (smallEtaleConstantZModSheaf E X hX n) 2 ≃+ ZMod n) ∧
      ∀ q, 3 ≤ q → Subsingleton (Sheaf.H (smallEtaleConstantZModSheaf E X hX n) q)
```

**`Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/SecondCohomologyOfRootsOfUnity.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/SecondCohomologyOfRootsOfUnity.lean#L252). The attribute's comment: “the q = 2 clause, that H^2\_etale(X, mu\_n) of a smooth proper curve over an algebraically closed field is cyclic of order n, normalised by the degree through sheafHTwoRootsOfUnityAddEquivZMod\_curveKummerCoboundary; the q = 0 clause is AlgebraicGeometry.baseRootsToEtaleH0\_bijective\_of\_isCurve and the q > 2 clause is subsingleton\_sheafH\_rootsOfUnitySheaf\_of\_smoothCurve, while the q = 1 clause awaits Stacks 03P8 for the small etale site”. References: SGA 4½ Arcata (6.2.1), “partial”.

> **[Stacks, Tag 03RQ], the case `q = 2`.**  Let `X` be a smooth proper curve over an
> algebraically closed field `k` and let `n` be invertible in `k`.  Then `H²_étale(X, μ_n)` is
> cyclic of order `n`.
>
> The Kummer coboundary presents `H²_étale(X, μ_n)` as the quotient of `H¹_étale(X, 𝐆_m)` by its
> `n`-th multiples — it is onto because `H²_étale(X, 𝐆_m) = 0` ([Stacks, Tag 03RM]) and its kernel
> is the `n`-th multiples because the preceding map of the long exact sequence is multiplication by
> `n` — and the degree identifies that quotient with `𝐙/n𝐙`, by
> `Stacks.EtaleCohomology.ker_curveKummerCoboundary_eq_ker_sheafHOneMultiplicativeDegreeMod`.
>
> The normalisation of this isomorphism is
> `Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod_curveKummerCoboundary`.

```lean
def sheafHTwoRootsOfUnityAddEquivZMod :
    Sheaf.H.{u + 1} (rootsOfUnitySheaf.{u, u + 1} X n) 2 ≃+ ZMod n
```

**`Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod_curveKummerCoboundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/SecondCohomologyOfRootsOfUnity.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/SecondCohomologyOfRootsOfUnity.lean#L269). The attribute's comment: “the normalisation of the q = 2 clause by the degree: the coordinate of the Kummer coboundary of a class of H^1\_etale(X, G\_m) is the degree of the corresponding divisor class modulo n”.

> **The normalisation of `Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod`**: the
> coordinate of the Kummer coboundary of a class in `H¹_étale(X, 𝐆_m)` is the degree of that class
> modulo `n`.  Together with
> `Stacks.EtaleCohomology.exists_curveKummerCoboundary_eq`, which says that every class in
> `H²_étale(X, μ_n)` is a coboundary, this fixes the isomorphism and not merely its existence.

```lean
theorem sheafHTwoRootsOfUnityAddEquivZMod_curveKummerCoboundary
    (a : Sheaf.H.{u + 1} (multiplicativeSheaf.{u, u + 1} X) 1) :
    sheafHTwoRootsOfUnityAddEquivZMod g hn (curveKummerCoboundary g hn a) =
      sheafHOneMultiplicativeDegreeMod g n a
```

**`AlgebraicGeometry.baseRootsToEtaleH0_bijective_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnityCurve.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnityCurve.lean#L65). The attribute's comment: “the q = 0 clause, H^0\_etale(X, mu\_n) = mu\_n(k); all clauses together are etaleCohomology\_rootsOfUnity\_smoothProjectiveCurve\_of\_genus”.

> **Stacks Project, Tag 03RQ, the case `q = 0`.** Let `X` be a smooth projective curve over an
> algebraically closed field `k` and let `n` be invertible in `k`. Pullback along the structure
> morphism is a bijection from the `n`-th roots of unity of `k` onto `H⁰_étale(X, μ_n)`.

```lean
public theorem baseRootsToEtaleH0_bijective_of_isCurve
    (B : BigEtaleSite.{u}) (k : Type u) [Field k] [IsAlgClosed k]
    (X : Scheme.{u}) (hX : B.Contains X) (f : X ⟶ Spec (.of k))
    [IsCurve k f] [Smooth f] [IsProjectiveVariety k f] (n : ℕ) (hn : IsUnit (n : k))
    [HasSheafify (SmallEtale.topology B X hX) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u})] :
    Function.Bijective (baseRootsToEtaleH0 B k X hX f n)
```

**`Stacks.Kummer.subsingleton_sheafH_rootsOfUnitySheaf_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Picard/RootsOfUnitySecondCohomology.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Picard/RootsOfUnitySecondCohomology.lean#L164). The attribute's comment: “the clause q >= 3: H^q\_etale(X, mu\_n) = 0 for every q >= 3”. References: SGA 4½ Arcata (3.3.5), “partial”.

> **Stacks Project, Tag 03RQ, the clause `q ≥ 3`.** Let `X` be a smooth projective curve over
> an algebraically closed field `k` and let `n ≥ 1` be invertible in `k`. Then
> `H^q_étale(X, μ_n) = 0` for every `q ≥ 3`.
>
> The Kummer sequence places `H^q(X, μ_n)` between `H^{q-1}(X, 𝐆_m)` and `H^q(X, 𝐆_m)`, both zero
> by Stacks 03RM since `q - 1 ≥ 2`. Projectivity is not used.

```lean
theorem subsingleton_sheafH_rootsOfUnitySheaf_of_isCurve (q : ℕ) (hq : 3 ≤ q) :
    Subsingleton (Sheaf.H.{u + 1, u + 1} (rootsOfUnitySheaf.{u, u + 1} X n) q)
```

## Tag 0AMB, a lemma

[Tag 0AMB](https://stacks.math.columbia.edu/tag/0AMB) in the Stacks Project.

**`Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod_rootsOfUnityRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/SecondCohomologyPullbackDegree.lean, line 800](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/SecondCohomologyPullbackDegree.lean#L800). The attribute's comment: “for a nonconstant morphism pi : X -> Y of smooth proper curves over an algebraically closed field k and n invertible in k, the pullback pi^* : H^2\_etale(Y, mu\_n) -> H^2\_etale(X, mu\_n) is multiplication by the degree of pi, under the canonical identifications H^2\_etale(-, mu\_n) = Z/nZ of Stacks 03RQ (sheafHTwoRootsOfUnityAddEquivZMod), given by the Kummer coboundary of H^1\_etale(-, G\_m) = Cl(-) = Pic(-) followed by the degree”.

> **[Stacks, Tag 0AMB].**  Let `k` be an algebraically closed field, let `π : X ⟶ Y` be a
> nonconstant morphism of smooth proper curves over `k`, and let `n` be invertible in `k`.  In the
> coordinates of `Stacks.EtaleCohomology.sheafHTwoRootsOfUnityAddEquivZMod`, which identify both
> `H²_étale(Y, μ_n)` and `H²_étale(X, μ_n)` with `𝐙/n𝐙`, the pullback
>
> `π^* : H²_étale(Y, μ_n) ⟶ H²_étale(X, μ_n)`
>
> is multiplication by the degree `deg(X/Y) = [R(X) : R(Y)]` of the extension of function fields
> ([Stacks, Tag 02NY]).
>
> The proof is the source's.  Every class of `H²_étale(Y, μ_n)` is the Kummer coboundary of a class
> `a` of `H¹_étale(Y, 𝐆_m)` ([Stacks, Tag 03RM]), and the coordinate of that coboundary is the
> degree of `a` modulo `n`.  Restriction along `π` commutes with the Kummer coboundary
> (`Stacks.Kummer.etaleCohomologyRestrictionMap_kummerExtClass`), so the coordinate of the
> restricted class is the degree of the restriction of `a`, which is `deg(X/Y)` times the degree of
> `a` by `Stacks.EtaleCohomology.sheafHOneMultiplicativeDegreeMod_multiplicativeRestriction` —
> and that is where nonconstancy of `π` is used, through the rank-one case of [Stacks, Tag 0AYZ].

```lean
theorem sheafHTwoRootsOfUnityAddEquivZMod_rootsOfUnityRestriction
    (x : Sheaf.H.{u + 1} (Stacks.Kummer.rootsOfUnitySheaf.{u, u + 1} Y n) 2) :
    sheafHTwoRootsOfUnityAddEquivZMod gX hn
        (rootsOfUnityRestriction.{u, u + 1, u + 1} π n 2 x) =
      ((@degreeOver X Y π _ _ (locallyOfFiniteType_of_isCurve_comp k gX gY π hπ)
            (isDominant_of_not_constant k gX gY π hnc) : ℕ) : ZMod n) *
        sheafHTwoRootsOfUnityAddEquivZMod gY hn x
```

## Tag 03RR, a lemma

[Tag 03RR](https://stacks.math.columbia.edu/tag/03RR) in the Stacks Project.

**`AlgebraicGeometry.etaleCohomology_rootsOfUnity_affineSmoothCurve_of_compactification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/RootsOfUnityCurvesFinal.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/RootsOfUnityCurvesFinal.lean#L66).

> **Stacks Project, Tag 03RR.** Let `X` be an affine smooth curve over an algebraically closed
> field `k`, let `n ∈ k^*`, and let `j : X ⟶ X̄` be a smooth projective compactification, with `g`
> the genus of `X̄` and `r` the number of points of `X̄ ∖ X`. Then
> 1. `H⁰_ét(X, μ_n) = μ_n(k)`;
> 2. `H¹_ét(X, μ_n) ≅ (𝐙/n𝐙)^{2g + r - 1}`;
> 3. `H^q_ét(X, μ_n) = 0` for `q ≥ 2`.

```lean
theorem etaleCohomology_rootsOfUnity_affineSmoothCurve_of_compactification (hn : IsUnit (n : k))
    [IsAffine X] {Xbar : Scheme.{u}} (fbar : Xbar ⟶ Spec (.of k)) [IsCurve k fbar] [Smooth fbar]
    [IsProjectiveVariety k fbar] (j : X ⟶ Xbar) [IsOpenImmersion j] (hj : j ≫ fbar = f)
    (r : ℕ) (hr : Nat.card ↥(Set.range j.base)ᶜ = r) :
    Function.Bijective (baseRootsToEtaleH0 E k X hX f n) ∧
      Nonempty (Sheaf.H (kummerSmallEtale E X hX n).X₁ 1 ≃+
        (Fin (2 * genus fbar + r - 1) → ZMod n)) ∧
      ∀ q, 2 ≤ q → Subsingleton (Sheaf.H (kummerSmallEtale E X hX n).X₁ q)
```

**`AlgebraicGeometry.etaleH0EquivRootsOfUnitySections_val`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnity.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnity.lean#L189). The attribute's comment: “degree\_zero”.

> The comparison is the canonical evaluation of degree-zero cohomology at the final
> étale object, followed by the inclusion of the kernel into the units sheaf.

```lean
theorem etaleH0EquivRootsOfUnitySections_val
    (B : BigEtaleSite.{u}) (X : Scheme.{u}) (hX : B.Contains X)
    (n : ℕ)
    [HasSheafify (SmallEtale.topology B X hX) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u})]
    (x : Sheaf.H.{w, u}
      (rootsOfUnitySheaf (SmallEtale.topology B X hX)
        (SmallEtale.toScheme B X hX)
        (unitsPresheaf_isSheaf_smallEtale B X hX) n) 0) :
    (etaleH0EquivRootsOfUnitySections B X hX n x).1 =
      Additive.toMul
        ((Limits.kernel.ι
          (powerSheaf (SmallEtale.topology B X hX)
            (SmallEtale.toScheme B X hX)
            (unitsPresheaf_isSheaf_smallEtale B X hX) n)).hom.app
          (Opposite.op (SmallEtale.final B X hX))
          ((Sheaf.H.equiv₀
            (rootsOfUnitySheaf (SmallEtale.topology B X hX)
              (SmallEtale.toScheme B X hX)
              (unitsPresheaf_isSheaf_smallEtale B X hX) n)
            (SmallEtale.finalIsTerminal B X hX)) x))
```

**`AlgebraicGeometry.rootsOfUnitySections_bijective_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnity.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnity.lean#L230). The attribute's comment: “degree\_zero”.

> Roots of unity in global sections of an integral scheme over an algebraically
> closed field are precisely the constants.

```lean
theorem rootsOfUnitySections_bijective_of_isIntegral
    (k : Type u) [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} [IsIntegral X] (f : X ⟶ Spec (.of k))
    (n : ℕ) (hn : 0 < n) :
    Function.Bijective
      ((rootsOfUnitySections n).map f.op)
```

**`AlgebraicGeometry.baseRootsToEtaleH0_bijective_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnity.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DegreeZero/RootsOfUnity.lean#L270). The attribute's comment: “degree\_zero”.

> The canonical pullback from the field's roots of unity to degree-zero étale
> cohomology is bijective over an algebraically closed field.

```lean
theorem baseRootsToEtaleH0_bijective_of_isIntegral
    (B : BigEtaleSite.{u}) (k : Type u) [Field k] [IsAlgClosed k]
    (X : Scheme.{u}) [IsIntegral X] (hX : B.Contains X)
    (f : X ⟶ Spec (.of k)) (n : ℕ) (hn : 0 < n)
    [HasSheafify (SmallEtale.topology B X hX) AddCommGrpCat.{u}]
    [HasExt.{w} (Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u})] :
    Function.Bijective (baseRootsToEtaleH0 B k X hX f n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.69, Tag 03RN](https://stacks.math.columbia.edu/tag/03RN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
