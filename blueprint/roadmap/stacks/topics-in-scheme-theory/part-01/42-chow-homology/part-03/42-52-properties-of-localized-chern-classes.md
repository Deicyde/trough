---
declaration: section
origin: cited
lean: Stacks.Chow.LocalizedSituation.localizedPowerSum_succ, Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedPowerSum, Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedChern, Stacks.Chow.totalLocalizedChernClass, Stacks.Chow.totalLocalizedChernClass_fst_of_nonneg, Stacks.Chow.totalLocalizedChernClass_fst_of_neg, Stacks.Chow.totalLocalizedChernClass_snd, Stacks.Chow.LocalizedChernData.totalLocalizedChernClass
statement: formalized
proof: formalized
---

# 42.52 Properties of localized Chern classes

Section 42.52 of the Stacks Project, [Tag 0FB9](https://stacks.math.columbia.edu/tag/0FB9). 6 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FBA, a lemma

[Tag 0FBA](https://stacks.math.columbia.edu/tag/0FBA) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedNewton.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedNewton.lean#L125). The attribute's comment: “In Situation 0GUJ with E|_{X ∖ Z} zero: Newton's recursion P_{q+1} = ∑_{j&lt;q} (-1)^j c_{j+1} P_{q-j} + (-1)^q (q+1) c_{q+1} for every q ≥ 0, products in the algebra A^{(1)}(Z → X) of 0FA0; it gives P_1 = c_1, P_2 = c_1² - 2c_2, P_3 = c_1³ - 3c_1c_2 + 3c_3 and so on, the whole lemma”.

> In Situation 0GUJ assume `E|_{X ∖ Z}` is zero. Then the
> localized classes `P_p(Z ⟶ X, E) ∈ A^p(Z ⟶ X)` of Stacks 0FB2 are Newton's polynomials in the
> localized Chern classes `c_i(Z ⟶ X, E)` (defined for every `i ≥ 1`, the zero module having
> rank `< i`), with the multiplication of the algebra `A^{(1)}(Z ⟶ X)` of Stacks 0FA0
> (`(c, c') ↦ res(c) ∘ c'`, `Stacks.Chow.supportedMul`):
>
>   `P_{q+1} = ∑_{j < q} (-1)^j c_{j+1} P_{q-j} + (-1)^q (q + 1) c_{q+1}`
>
> for every `q ≥ 0`. This is the recursion defining the universal power-sum polynomials, so
> `P_1 = c_1`, `P_2 = c_1² - 2c_2`, `P_3 = c_1³ - 3c_1c_2 + 3c_3`, and so on. The summand
> `c_{j+1} P_{q-j}` lies in `A^{(j+1)+(q-j)}(Z ⟶ X)`, read in degree `q + 1`.
>
> Here `P_p(Z ⟶ X, E)` is `Stacks.Chow.LocalizedSituation.localizedPowerSum` and `c_i(Z ⟶ X, E)` is
> `Stacks.Chow.LocalizedSituation.localizedChernClassOfIsZero`, the class
> `Stacks.Chow.LocalizedSituation.localizedChern` for the situation in degree `i`; both are formed
> in Situation 0GUJ, condition (3) making the Chern classes of the object `Q` of the graph
> construction defined (`Stacks.Chow.LocalizedSituation.hasDefinedChernClasses_graphObject`,
> Stacks 0GUE).

```lean
theorem localizedPowerSum_succ (q : ℕ) :
    S.localizedPowerSum h (q + 1) =
      ∑ j ∈ (Finset.range q).attach, ((-1 : ℤ) ^ (j : ℕ)) •
          bivariantClassDegreeCongr S.base _ (S.i ≫ S.a) S.a S.i rfl
            (newton_degree_eq (Finset.mem_range.mp j.2))
            (supportedMul S.base (S.i ≫ S.a) S.a S.i rfl
              (localizedChernClassOfIsZero h (Nat.succ_pos (j : ℕ)))
              (S.localizedPowerSum h (q - j))) +
        ((-1 : ℤ) ^ q * ((q : ℤ) + 1)) • localizedChernClassOfIsZero h (Nat.succ_pos q)
```

## Tag 0FBB, a lemma

[Tag 0FBB](https://stacks.math.columbia.edu/tag/0FBB) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean#L570). The attribute's comment: “for P_p(Z → X, E), when E|_(X ∖ Z) is zero: P_p(Z → X, E) ∘ c = c ∘ P_p(Z → X, E) in A^*(Y ×_X Z → X), for every c in A^*(Y → X)”.

> In Situation 0GUJ with `E|_{X ∖ Z}` zero, let `g : Y ⟶ X` be locally of finite type and let
> `c ∈ A^*(Y ⟶ X)`. Then
>
>   `P_p(Z ⟶ X, E) ∘ c = c ∘ P_p(Z ⟶ X, E)`   in   `A^*(Y ×_X Z ⟶ X)`,
>
> where `P_p(Z ⟶ X, E) ∘ c = res(P_p(Z ⟶ X, E)) ∘ c` is a class for `Z ×_X Y ⟶ X`, carried to
> `Y ×_X Z` along the symmetry of the fibre product, and `c ∘ P_p(Z ⟶ X, E)` is
> `res(c) ∘ P_p(Z ⟶ X, E)`. The class is `P'_p(Q)` of Stacks 0F9K for the graph construction, so
> this is `Stacks.Chow.nonhomogeneousBivariantTransport_compositeOfInvertible_modificationPowerSum`.

```lean
theorem nonhomogeneousBivariantTransport_compositeOfInvertible_localizedPowerSum
    (h : S.IsZeroOnComplement) (p : ℕ)
    (c : nonhomogeneousBivariantGroup S.base (gysinSystemOfInvertible S.base) (g ≫ S.a) S.a g
      rfl) :
    nonhomogeneousBivariantTransport S.base (gysinSystemOfInvertible S.base)
        (pullback.fst S.i g ≫ (S.i ≫ S.a)) (pullback.fst g S.i ≫ (g ≫ S.a)) S.a
        (pullback.snd S.i g ≫ g)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl g) rfl)
        (pullback.snd g S.i ≫ S.i)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq S.base (g ≫ S.a) S.a g rfl S.i) rfl)
        (pullbackSymmetry S.i g) (by simp [pullback.condition])
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base)
        (nonhomogeneousBivariantCompositeOfInvertible S.base (pullback.fst S.i g ≫ (S.i ≫ S.a))
          (g ≫ S.a) S.a (pullback.snd S.i g) g
          (pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl g) rfl
          (DirectSum.of _ (p : ℤ)
            (bivariantRestriction S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl
              g p (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base)
              (S.localizedPowerSum h p))) c) =
      nonhomogeneousBivariantCompositeOfInvertible S.base (pullback.fst g S.i ≫ (g ≫ S.a))
        (S.i ≫ S.a) S.a (pullback.snd g S.i) S.i
        (pullbackSnd_comp_structureMorphism_eq S.base (g ≫ S.a) S.a g rfl S.i) rfl
        (nonhomogeneousBivariantRestriction S.base (gysinSystemOfInvertible S.base) (g ≫ S.a) S.a
          g rfl S.i (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base) c)
        (DirectSum.of _ (p : ℤ) (S.localizedPowerSum h p))
```

**`Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedChern`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean#L621). The attribute's comment: “for c_p(Z → X, E), when E|_(X ∖ Z) is finite locally free of rank < p in degree 0: c_p(Z → X, E) ∘ c = c ∘ c_p(Z → X, E) in A^*(Y ×_X Z → X), for every c in A^*(Y → X)”.

> In Situation 0GUJ with `E|_{X ∖ Z}` finite locally free of rank `< p` in degree `0`, let
> `g : Y ⟶ X` be locally of finite type and let `c ∈ A^*(Y ⟶ X)`. Then
>
>   `c_p(Z ⟶ X, E) ∘ c = c ∘ c_p(Z ⟶ X, E)`   in   `A^*(Y ×_X Z ⟶ X)`,
>
> where `c_p(Z ⟶ X, E) ∘ c = res(c_p(Z ⟶ X, E)) ∘ c` is a class for `Z ×_X Y ⟶ X`, carried to
> `Y ×_X Z` along the symmetry of the fibre product, and `c ∘ c_p(Z ⟶ X, E)` is
> `res(c) ∘ c_p(Z ⟶ X, E)`. The class is `c'_p(Q)` of Stacks 0F9K for the graph construction, so
> this is
> `Stacks.Chow.nonhomogeneousBivariantTransport_compositeOfInvertible_modificationChernClass`.

```lean
theorem nonhomogeneousBivariantTransport_compositeOfInvertible_localizedChern
    (h : S.IsFiniteLocallyFreeOfRankLTOnComplement)
    (c : nonhomogeneousBivariantGroup S.base (gysinSystemOfInvertible S.base) (g ≫ S.a) S.a g
      rfl) :
    nonhomogeneousBivariantTransport S.base (gysinSystemOfInvertible S.base)
        (pullback.fst S.i g ≫ (S.i ≫ S.a)) (pullback.fst g S.i ≫ (g ≫ S.a)) S.a
        (pullback.snd S.i g ≫ g)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl g) rfl)
        (pullback.snd g S.i ≫ S.i)
        (comp_comp_structureMorphism_eq
          (pullbackSnd_comp_structureMorphism_eq S.base (g ≫ S.a) S.a g rfl S.i) rfl)
        (pullbackSymmetry S.i g) (by simp [pullback.condition])
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base)
        (nonhomogeneousBivariantCompositeOfInvertible S.base (pullback.fst S.i g ≫ (S.i ≫ S.a))
          (g ≫ S.a) S.a (pullback.snd S.i g) g
          (pullbackSnd_comp_structureMorphism_eq S.base (S.i ≫ S.a) S.a S.i rfl g) rfl
          (DirectSum.of _ (S.p : ℤ)
            (bivariantRestriction S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl
              g S.p (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base)
              (S.localizedChern h))) c) =
      nonhomogeneousBivariantCompositeOfInvertible S.base (pullback.fst g S.i ≫ (g ≫ S.a))
        (S.i ≫ S.a) S.a (pullback.snd g S.i) S.i
        (pullbackSnd_comp_structureMorphism_eq S.base (g ≫ S.a) S.a g rfl S.i) rfl
        (nonhomogeneousBivariantRestriction S.base (gysinSystemOfInvertible S.base) (g ≫ S.a) S.a
          g rfl S.i (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso S.base) c)
        (DirectSum.of _ (S.p : ℤ) (S.localizedChern h))
```

## Tag 0FBC, a remark

[Tag 0FBC](https://stacks.math.columbia.edu/tag/0FBC) in the Stacks Project.

**`Stacks.Chow.totalLocalizedChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean#L101).

> **Stacks 0FBC.** The total localized Chern class
>
>   `c⁽ᵖ⁾(Z ⟶ X, E) = 1 + c₁(E) + … + c_{p-1}(E) + c_p(Z ⟶ X, E) + c_{p+1}(Z ⟶ X, E) + …`
>
> of a situation for localized Chern classes: the element of `A⁽ᵖ⁾(Z ⟶ X)` whose component in a
> degree `0 ≤ i < p` is the ordinary Chern class `c i` of `E`, whose component in a degree `i ≥ p`
> is the localized Chern class `cloc i`, and whose components in the negative degrees vanish.

```lean
def totalLocalizedChernClass :
    localizedBivariantGrading T.base G (T.i ≫ T.a) T.a T.i rfl T.p
```

**`Stacks.Chow.totalLocalizedChernClass_fst_of_nonneg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean#L108). The attribute's comment: “the graded pieces in the degrees below the cutoff”.

> In a degree `0 ≤ i < p` the component of `c⁽ᵖ⁾(Z ⟶ X, E)` is the ordinary Chern class
> `c_i(E)` of `E`; in degree `0` that is `c₀(E) = 1`.

```lean
theorem totalLocalizedChernClass_fst_of_nonneg {i : ℤ} (hi : i < (T.p : ℤ)) (h0 : 0 ≤ i) :
    (totalLocalizedChernClass T G c cloc).1 ⟨i, hi⟩ = c ⟨i, h0⟩
```

**`Stacks.Chow.totalLocalizedChernClass_fst_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean#L115). The attribute's comment: “the vanishing of the graded pieces in the negative degrees”.

> In a negative degree the component of `c⁽ᵖ⁾(Z ⟶ X, E)` vanishes, the source's display having
> no term there.

```lean
theorem totalLocalizedChernClass_fst_of_neg {i : ℤ} (hi : i < (T.p : ℤ)) (h0 : i < 0) :
    (totalLocalizedChernClass T G c cloc).1 ⟨i, hi⟩ = 0
```

**`Stacks.Chow.totalLocalizedChernClass_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClass.lean#L122). The attribute's comment: “the graded pieces in the degrees from the cutoff onward”.

> In a degree `i ≥ p` the component of `c⁽ᵖ⁾(Z ⟶ X, E)` is the localized Chern class
> `c_i(Z ⟶ X, E)`.

```lean
theorem totalLocalizedChernClass_snd (i : {i : ℤ // (T.p : ℤ) ≤ i}) :
    (totalLocalizedChernClass T G c cloc).2 i = cloc i
```

**`Stacks.Chow.LocalizedChernData.totalLocalizedChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean#L60).

> The total localized Chern class
>
>   `c⁽ᵖ⁾(Z ⟶ X, E) = 1 + c₁(E) + … + c_{p-1}(E) + c_p(Z ⟶ X, E) + c_{p+1}(Z ⟶ X, E) + …`
>
> of the data of a localized Chern class: the element of `A⁽ᵖ⁾(Z ⟶ X)` whose component in a
> degree `0 ≤ i < p` is the ordinary Chern class `c i` of `E`, whose component in a degree `i ≥ p`
> is the localized Chern class `cloc i`, and whose components in the negative degrees vanish.

```lean
def LocalizedChernData.totalLocalizedChernClass (T : LocalizedChernData.{u})
    (G : GysinSystem T.base)
    (c : (i : {i : ℤ // 0 ≤ i}) →
      BivariantClass T.base G T.a T.a (𝟙 T.X) (Category.id_comp T.a) i.1)
    (cloc : (i : {i : ℤ // (T.p : ℤ) ≤ i}) →
      BivariantClass T.base G (T.i ≫ T.a) T.a T.i rfl i.1) :
    localizedBivariantGrading T.base G (T.i ≫ T.a) T.a T.i rfl T.p
```

**`Stacks.Chow.LocalizedChernData.totalLocalizedChernClass_fst_of_nonneg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean#L78). The attribute's comment: “the graded pieces in the degrees below the cutoff”.

> In a degree `0 ≤ i < p` the component of `c⁽ᵖ⁾(Z ⟶ X, E)` is the ordinary Chern class
> `c_i(E)` of `E`; in degree `0` that is `c₀(E) = 1`.

```lean
theorem LocalizedChernData.totalLocalizedChernClass_fst_of_nonneg {i : ℤ} (hi : i < (T.p : ℤ))
    (h0 : 0 ≤ i) :
    (LocalizedChernData.totalLocalizedChernClass T G c cloc).1 ⟨i, hi⟩ = c ⟨i, h0⟩
```

**`Stacks.Chow.LocalizedChernData.totalLocalizedChernClass_fst_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean#L85). The attribute's comment: “the vanishing of the graded pieces in the negative degrees”.

> In a negative degree the component of `c⁽ᵖ⁾(Z ⟶ X, E)` vanishes.

```lean
theorem LocalizedChernData.totalLocalizedChernClass_fst_of_neg {i : ℤ} (hi : i < (T.p : ℤ))
    (h0 : i < 0) :
    (LocalizedChernData.totalLocalizedChernClass T G c cloc).1 ⟨i, hi⟩ = 0
```

**`Stacks.Chow.LocalizedChernData.totalLocalizedChernClass_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/TotalLocalizedChernClassData.lean#L93). The attribute's comment: “the graded pieces in the degrees from the cutoff onward”.

> In a degree `i ≥ p` the component of `c⁽ᵖ⁾(Z ⟶ X, E)` is the localized Chern class
> `c_i(Z ⟶ X, E)`.

```lean
theorem LocalizedChernData.totalLocalizedChernClass_snd (i : {i : ℤ // (T.p : ℤ) ≤ i}) :
    (LocalizedChernData.totalLocalizedChernClass T G c cloc).2 i = cloc i
```

## Tag 0FBD, a lemma

[Tag 0FBD](https://stacks.math.columbia.edu/tag/0FBD) in the Stacks Project.

**`Stacks.Chow.LocalizedChernData.totalLocalizedChern_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean, line 991](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean#L991).

> **Stacks 0FBD.** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type
> over `S`, let `Z ⟶ X` be a closed immersion and let `E₁ ⟶ E₂ ⟶ E₃ ⟶ E₁[1]` be a distinguished
> triangle of perfect objects of `D(𝒪_X)`. Assume (1) `E₁|_{X ∖ Z}` and `E₃|_{X ∖ Z}` are finite
> locally free of rank `< p₁` and `< p₃` placed in degree `0`, and (2) one of: (a) `X` is
> quasi-compact, (b) `X` has quasi-compact irreducible components, (c) `E₃ ⟶ E₁[1]` is represented
> by a map of locally bounded complexes of finite locally free `𝒪_X`-modules, (d) the same holds for
> `Lf^*E₃ ⟶ Lf^*E₁[1]` after an envelope `f : Y ⟶ X`. These are stated as the hypothesis `hc`,
> in the source's order (a), (b), (c), (d). Then
>
>   `c⁽ᵖ¹⁺ᵖ³⁾(Z ⟶ X, E₂) = c⁽ᵖ¹⁾(Z ⟶ X, E₁) c⁽ᵖ³⁾(Z ⟶ X, E₃)`   in `A⁽ᵖ¹⁺ᵖ³⁾(Z ⟶ X)`,
>
> with the classes of Remark 0FBC (`Stacks.Chow.LocalizedChernData.totalLocalizedChern`) and the
> multiplication of Remark 0FA0 (`Stacks.Chow.localizedGradingMul`). That the statement makes
> sense, i.e. that `E₂|_{X ∖ Z}` is finite locally free of rank `< p₁ + p₃` in degree `0` and that
> the Chern classes of `E₁`, `E₂`, `E₃` are defined, is
> `Stacks.Chow.LocalizedChernData.exists_isFiniteLocallyFreeOfRankLT_restrict_obj₂` and
> `Stacks.Chow.hasDefinedChernClasses_triangle_of_mor₃`. This is the output cutoff `r = p₁ + p₃` of
> `Stacks.Chow.LocalizedChernData.totalLocalizedChern_triangle_eq_cutoffMul`.

```lean
theorem totalLocalizedChern_triangle
    (a : E₁ ⟶ E₂) (b : E₂ ⟶ E₃) (c : E₃ ⟶ E₁⟦(1 : ℤ)⟧) (hT : Triangle.mk a b c ∈ distTriang _)
    (r₁ : (∃ M : OXMod.{u, u, u} (D.X.toRingedSpace.restrict (⟨(Set.range D.i.base)ᶜ,
      D.i.isClosedEmbedding.isClosed_range.isOpen_compl⟩ : D.X.Opens).isOpenEmbedding),
      IsFiniteLocallyFreeOfRankLT M p₁ ∧
        Nonempty ((derivedPullback (D.X.toRingedSpace.ofRestrict (⟨(Set.range D.i.base)ᶜ,
          D.i.isClosedEmbedding.isClosed_range.isOpen_compl⟩ :
            D.X.Opens).isOpenEmbedding)).obj E₁ ≅ (DerivedCategory.singleFunctor _ 0).obj M)))
    (r₃ : (∃ M : OXMod.{u, u, u} (D.X.toRingedSpace.restrict (⟨(Set.range D.i.base)ᶜ,
      D.i.isClosedEmbedding.isClosed_range.isOpen_compl⟩ : D.X.Opens).isOpenEmbedding),
      IsFiniteLocallyFreeOfRankLT M p₃ ∧
        Nonempty ((derivedPullback (D.X.toRingedSpace.ofRestrict (⟨(Set.range D.i.base)ᶜ,
          D.i.isClosedEmbedding.isClosed_range.isOpen_compl⟩ :
            D.X.Opens).isOpenEmbedding)).obj E₃ ≅ (DerivedCategory.singleFunctor _ 0).obj M)))
    (hc : CompactSpace D.X ∨ (∀ T ∈ irreducibleComponents D.X, IsCompact T) ∨
      HasMapPresentation c ∨ HasEnvelopeMapPresentation c) :
    totalLocalizedChern (D := D.withObject E₂ (p₁ + p₃) h₂
        (D.exists_isFiniteLocallyFreeOfRankLT_restrict_obj₂ a b c hT (by omega) r₁ r₃))
        (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
          (hasTriangleChernCondition_of_conditions hc)).2.1
        (D.isFiniteLocallyFreeOfRankLTOnComplement_withObject _) =
      localizedGradingMul D.base (D.i ≫ D.a) D.a D.i rfl
        (totalLocalizedChern (D := D.withObject E₁ p₁ h₁ r₁)
          (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
            (hasTriangleChernCondition_of_conditions hc)).1
          (D.isFiniteLocallyFreeOfRankLTOnComplement_withObject r₁))
        (totalLocalizedChern (D := D.withObject E₃ p₃ h₃ r₃)
          (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
            (hasTriangleChernCondition_of_conditions hc)).2.2
          (D.isFiniteLocallyFreeOfRankLTOnComplement_withObject r₃))
```

## Tag 0FBE, a lemma

[Tag 0FBE](https://stacks.math.columbia.edu/tag/0FBE) in the Stacks Project.

**`Stacks.Chow.LocalizedChernData.localizedPowerSum_localizedChernChar_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean, line 1155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean#L1155).

> **Stacks 0FBE.** Let `(S, δ)` be as in Situation 02QL, let `X` be locally of finite type
> over `S`, let `Z ⟶ X` be a closed immersion and let `E₁ ⟶ E₂ ⟶ E₃ ⟶ E₁[1]` be a distinguished
> triangle of perfect objects of `D(𝒪_X)`. Assume (1) `E₁|_{X ∖ Z}` and `E₃|_{X ∖ Z}` are zero,
> and (2) one of the conditions (a)–(d) of Stacks 0FBD on `E₃ ⟶ E₁[1]`, stated as the hypothesis `hc`
> in the source's order: (a) `X` is quasi-compact, (b) `X` has quasi-compact irreducible components,
> (c) `E₃ ⟶ E₁[1]` is represented by a map of locally bounded complexes of finite locally free
> `𝒪_X`-modules, (d) the same holds for `Lf^*E₃ ⟶ Lf^*E₁[1]` after an envelope `f : Y ⟶ X`. Then
>
>   `P_p(Z ⟶ X, E₂) = P_p(Z ⟶ X, E₁) + P_p(Z ⟶ X, E₃)`   for all `p`,
>
> and consequently `ch(Z ⟶ X, E₂) = ch(Z ⟶ X, E₁) + ch(Z ⟶ X, E₃)`, in every degree `p`, for the
> classes of Remark 0GUK (`Stacks.Chow.LocalizedChernData.localizedPowerSum`,
> `Stacks.Chow.LocalizedChernData.localizedChernChar`). The case `p = 0` is included.
>
> The localized classes `P_p(Z ⟶ X, E)` are defined for `p ≥ 0` (Definition 0FB5); the source's
> `p ∈ 𝐙` ranges over those.

```lean
theorem localizedPowerSum_localizedChernChar_triangle
    (a : E₁ ⟶ E₂) (b : E₂ ⟶ E₃) (c : E₃ ⟶ E₁⟦(1 : ℤ)⟧) (hT : Triangle.mk a b c ∈ distTriang _)
    (z₁ : IsZero ((derivedPullback (D.X.toRingedSpace.ofRestrict (⟨(Set.range D.i.base)ᶜ,
      D.i.isClosedEmbedding.isClosed_range.isOpen_compl⟩ : D.X.Opens).isOpenEmbedding)).obj E₁))
    (z₃ : IsZero ((derivedPullback (D.X.toRingedSpace.ofRestrict (⟨(Set.range D.i.base)ᶜ,
      D.i.isClosedEmbedding.isClosed_range.isOpen_compl⟩ : D.X.Opens).isOpenEmbedding)).obj E₃))
    (hc : CompactSpace D.X ∨ (∀ T ∈ irreducibleComponents D.X, IsCompact T) ∨
      HasMapPresentation c ∨ HasEnvelopeMapPresentation c) :
    (∀ p : ℕ,
      (D.withZeroObject E₂ h₂ (D.isZero_restrict_obj₂ a b c hT z₁ z₃)).localizedPowerSum
          (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
            (hasTriangleChernCondition_of_conditions hc)).2.1
          (D.isZero_restrict_obj₂ a b c hT z₁ z₃) p =
        (D.withZeroObject E₁ h₁ z₁).localizedPowerSum
            (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
              (hasTriangleChernCondition_of_conditions hc)).1 z₁ p +
          (D.withZeroObject E₃ h₃ z₃).localizedPowerSum
            (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
              (hasTriangleChernCondition_of_conditions hc)).2.2 z₃ p) ∧
      ∀ p : ℕ,
        (D.withZeroObject E₂ h₂ (D.isZero_restrict_obj₂ a b c hT z₁ z₃)).localizedChernChar
            (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
              (hasTriangleChernCondition_of_conditions hc)).2.1
            (D.isZero_restrict_obj₂ a b c hT z₁ z₃) p =
          (D.withZeroObject E₁ h₁ z₁).localizedChernChar
              (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
                (hasTriangleChernCondition_of_conditions hc)).1 z₁ p +
            (D.withZeroObject E₃ h₃ z₃).localizedChernChar
              (hasDefinedChernClasses_triangle_of_mor₃ D.base D.a h₁ h₂ h₃ hT
                (hasTriangleChernCondition_of_conditions hc)).2.2 z₃ p
```

## Tag 0FBF, a lemma

[Tag 0FBF](https://stacks.math.columbia.edu/tag/0FBF) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L157). The attribute's comment: “the formula for P_p(Z_1 cap Z_2 -> X, F_1 tensor^L F_2), with Z_1 cap Z_2 = Z_1 x_X Z_2 and the products those of 0FE5 (supportedIntersectionMul). The source leaves implicit in which sense F_1 tensor^L F_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F_1 tensor^L F_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

> **The localized power sums of a derived tensor product.** In Situation 02QL let `X` be locally
> of finite type over `S`, let `Z₁, Z₂ ⊆ X` be closed subschemes and let `F₁, F₂ ∈ D(𝒪_X)` be perfect
> with `F_i|_{X ∖ Z_i}` zero and satisfying condition (3) of Situation 0GUJ. Then
>
>   `P_p(Z₁ ∩ Z₂ ⟶ X, F₁ ⊗^L F₂) = ∑_{p₁ + p₂ = p} C(p, p₁) P_{p₁}(Z₁ ⟶ X, F₁) P_{p₂}(Z₂ ⟶ X, F₂)`
>
> in `A^p(Z₁ ∩ Z₂ ⟶ X)`, the class of `F₁ ⊗^L F₂` being that of Remark 0GUK; the source leaves
> implicit in which sense `F₁ ⊗^L F₂` satisfies condition (3) in the mixed cases of alternatives
> (c) and (d), which the classes of Remark 0GUK cover.

```lean
theorem localizedPowerSum_derivedTensor (p : ℕ) :
    (LocalizedChernData.derivedTensorOfIsZero C a i₁ i₂ hF₁ hF₂ h₁ h₂ 0).localizedPowerSum
        (hasDefinedChernClasses_derivedTensor
          (ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).hasDefinedChernClasses_E
          (ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).hasDefinedChernClasses_E)
        (isZero_derivedTensor_compl_pullback i₁ i₂ hF₁ hF₂ h₁ h₂) p =
      ∑ q ∈ (antidiagonal p).attach, (p.choose q.1.1 : ℤ) •
        bivariantClassDegreeCongr C _ _ _ _ rfl (by have := mem_antidiagonal.1 q.2; omega)
          (supportedIntersectionMul C a i₁ i₂ (IsPullback.of_hasPullback i₁ i₂) _ rfl
            ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).localizedPowerSum h₁ q.1.1)
            ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).localizedPowerSum h₂ q.1.2))
```

**`Stacks.Chow.LocalizedSituation.localizedChern_one_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L187). The attribute's comment: “the formula for c_1(Z_1 cap Z_2 -> X, F_1 tensor^L F_2), r_i = P_0(Z_i -> X, F_i); the product r_2 c_1(Z_1 -> X, F_1) is taken for Z_1 cap Z_2 presented as Z_2 x_X Z_1 through the flipped square. The source leaves implicit in which sense F_1 tensor^L F_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F_1 tensor^L F_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

> **The first localized Chern class of a derived tensor product.** In the situation of
> `Stacks.Chow.LocalizedSituation.localizedPowerSum_derivedTensor`, with
> `r_i = P_0(Z_i ⟶ X, F_i)`,
>
>   `c_1(Z₁ ∩ Z₂ ⟶ X, F₁ ⊗^L F₂) = r₁ c_1(Z₂ ⟶ X, F₂) + r₂ c_1(Z₁ ⟶ X, F₁)`
>
> in `A^1(Z₁ ∩ Z₂ ⟶ X)`, the class of `F₁ ⊗^L F₂` being that of Remark 0GUK.

```lean
theorem localizedChern_one_derivedTensor :
    (LocalizedChernData.derivedTensorOfIsZero C a i₁ i₂ hF₁ hF₂ h₁ h₂ 1).localizedChern
        (hasDefinedChernClasses_derivedTensor
          (ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).hasDefinedChernClasses_E
          (ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).hasDefinedChernClasses_E)
        (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _
          (isZero_derivedTensor_compl_pullback i₁ i₂ hF₁ hF₂ h₁ h₂) one_pos) =
      bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
          (supportedIntersectionMul C a i₁ i₂ (IsPullback.of_hasPullback i₁ i₂) _ rfl
            ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).localizedPowerSum h₁ 0)
            ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₂
                one_pos))) +
        bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
          (supportedIntersectionMul C a i₂ i₁ (IsPullback.of_hasPullback i₁ i₂).flip _
            pullback.condition
            ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).localizedPowerSum h₂ 0)
            ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₁
                one_pos)))
```

**`Stacks.Chow.LocalizedSituation.localizedChern_two_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L237). The attribute's comment: “the formula for c_2(Z_1 cap Z_2 -> X, F_1 tensor^L F_2); the squares are the products res(c) o c of 0FA0 (supportedMul), C(r_i, 2) is the class of x |-> C(chi_{F_i}(x), 2) (LocalizedChernData.rankChoose), and (r_1 r_2 - 1) c c' is read as (r_1 r_2)(c c') - c c'. The source's 'and so on for higher Chern classes' is not formalized. The source leaves implicit in which sense F_1 tensor^L F_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F_1 tensor^L F_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

> **The second localized Chern class of a derived tensor product.** In the situation of
> `Stacks.Chow.LocalizedSituation.localizedPowerSum_derivedTensor`, with
> `r_i = P_0(Z_i ⟶ X, F_i)`, `γ_{i,p} = c_p(Z_i ⟶ X, F_i)` and `C(r_i, 2)` the class
> `Stacks.Chow.LocalizedChernData.rankChoose`,
>
>   `c_2(Z₁ ∩ Z₂ ⟶ X, F₁ ⊗^L F₂) = r₁ γ_{2,2} + r₂ γ_{1,2} + C(r₁, 2) γ_{2,1}² +
>     ((r₁ r₂) (γ_{2,1} γ_{1,1}) - γ_{2,1} γ_{1,1}) + C(r₂, 2) γ_{1,1}²`
>
> in `A^2(Z₁ ∩ Z₂ ⟶ X)`, the class of `F₁ ⊗^L F₂` being that of Remark 0GUK. The products of a
> class supported on `Z₂` with one supported on `Z₁` are taken for `Z₁ ∩ Z₂` presented as
> `Z₂ ×_X Z₁` through the flipped square, and the squares are the products of
> `Stacks.Chow.supportedMul`.

```lean
theorem localizedChern_two_derivedTensor :
    (LocalizedChernData.derivedTensorOfIsZero C a i₁ i₂ hF₁ hF₂ h₁ h₂ 2).localizedChern
        (hasDefinedChernClasses_derivedTensor
          (ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).hasDefinedChernClasses_E
          (ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).hasDefinedChernClasses_E)
        (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _
          (isZero_derivedTensor_compl_pullback i₁ i₂ hF₁ hF₂ h₁ h₂) two_pos) =
      bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
          (supportedIntersectionMul C a i₁ i₂ (IsPullback.of_hasPullback i₁ i₂) _ rfl
            ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).localizedPowerSum h₁ 0)
            ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 2).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₂
                two_pos))) +
        bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
          (supportedIntersectionMul C a i₂ i₁ (IsPullback.of_hasPullback i₁ i₂).flip _
            pullback.condition
            ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).localizedPowerSum h₂ 0)
            ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 2).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₁
                two_pos))) +
        bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
          (supportedIntersectionMul C a i₁ i₂ (IsPullback.of_hasPullback i₁ i₂) _ rfl
            ((LocalizedChernData.ofIsZero C a i₁ F₁ hF₁ h₁ 0).rankChoose h₁ 2 two_pos)
            (supportedMul C (i₂ ≫ a) a i₂ rfl ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₂
                one_pos))
              ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₂
                one_pos)))) +
        (bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
            (supportedMul C ((pullback.snd i₁ i₂ ≫ i₂) ≫ a) a (pullback.snd i₁ i₂ ≫ i₂) rfl
              (supportedIntersectionMul C a i₁ i₂ (IsPullback.of_hasPullback i₁ i₂) _ rfl
                ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).localizedPowerSum h₁ 0)
                ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).localizedPowerSum h₂ 0))
              (supportedIntersectionMul C a i₂ i₁ (IsPullback.of_hasPullback i₁ i₂).flip _
            pullback.condition
                ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₂
                one_pos))
                ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₁
                one_pos)))) -
          bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
            (supportedIntersectionMul C a i₂ i₁ (IsPullback.of_hasPullback i₁ i₂).flip _
            pullback.condition
              ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₂
                one_pos))
              ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₁
                one_pos)))) +
        bivariantClassDegreeCongr C _ _ _ _ rfl (by norm_num)
          (supportedIntersectionMul C a i₂ i₁ (IsPullback.of_hasPullback i₁ i₂).flip _
            pullback.condition
            ((LocalizedChernData.ofIsZero C a i₂ F₂ hF₂ h₂ 0).rankChoose h₂ 2 two_pos)
            (supportedMul C (i₁ ≫ a) a i₁ rfl ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₁
                one_pos))
              ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 1).localizedChern
              (LocalizedChernData.isFiniteLocallyFreeOfRankLTOnComplement_ofIsZero C a _ _ _ h₁
                one_pos))))
```

**`Stacks.Chow.LocalizedSituation.localizedChernChar_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L328). The attribute's comment: “the formula ch(Z_1 cap Z_2 -> X, F_1 tensor^L F_2) = ch(Z_1 -> X, F_1) ch(Z_2 -> X, F_2), read degree by degree in prod_p A^p(Z_1 cap Z_2 -> X) tensor Q. The source leaves implicit in which sense F_1 tensor^L F_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F_1 tensor^L F_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

> **The localized Chern character of a derived tensor product.** In the situation of
> `Stacks.Chow.LocalizedSituation.localizedPowerSum_derivedTensor`,
>
>   `ch(Z₁ ∩ Z₂ ⟶ X, F₁ ⊗^L F₂) = ch(Z₁ ⟶ X, F₁) ch(Z₂ ⟶ X, F₂)`
>
> in `∏_p A^p(Z₁ ∩ Z₂ ⟶ X) ⊗ 𝐐`, read in each degree `p`: the component of degree `p` of the left
> side is `∑_{p₁ + p₂ = p} ch_{p₁}(Z₁ ⟶ X, F₁) ch_{p₂}(Z₂ ⟶ X, F₂)`, the degree `p` component of the
> product, with the products of `Stacks.Chow.rationalSupportedIntersectionMul`. The Chern character
> of `F₁ ⊗^L F₂` is that of Remark 0GUK.

```lean
theorem localizedChernChar_derivedTensor (p : ℕ) :
    (LocalizedChernData.derivedTensorOfIsZero C a i₁ i₂ hF₁ hF₂ h₁ h₂ 0).localizedChernChar
        (hasDefinedChernClasses_derivedTensor
          (ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).hasDefinedChernClasses_E
          (ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).hasDefinedChernClasses_E)
        (isZero_derivedTensor_compl_pullback i₁ i₂ hF₁ hF₂ h₁ h₂) p =
      ∑ q ∈ (antidiagonal p).attach,
        rationalBivariantClassDegreeCongr C _ _ _ _ rfl (by have := mem_antidiagonal.1 q.2; omega)
          (rationalSupportedIntersectionMul C a i₁ i₂ (IsPullback.of_hasPullback i₁ i₂) _ rfl
            ((ofIsZero C a i₁ F₁ hF₁ h₁ hfin₁ 0).localizedChernChar h₁ q.1.1)
            ((ofIsZero C a i₂ F₂ hF₂ h₂ hfin₂ 0).localizedChernChar h₂ q.1.2))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.52, Tag 0FB9](https://stacks.math.columbia.edu/tag/0FB9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
