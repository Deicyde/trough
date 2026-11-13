---
declaration: section
origin: cited
lean: Stacks.Chow.LocalizedSituation.localizedPowerSum_succ, Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedPowerSum, Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedChern, Stacks.Chow.LocalizedChernData.totalLocalizedChern, Stacks.Chow.LocalizedChernData.totalLocalizedChern_fst, Stacks.Chow.LocalizedChernData.totalLocalizedChern_snd, Stacks.Chow.LocalizedSituation.totalLocalizedChern, Stacks.Chow.LocalizedSituation.totalLocalizedChern_fst
statement: formalized
proof: formalized
---

# 42.52 Properties of localized Chern classes

Section 42.52 of the Stacks Project, [Tag 0FB9](https://stacks.math.columbia.edu/tag/0FB9). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FBA, a lemma

[Tag 0FBA](https://stacks.math.columbia.edu/tag/0FBA) in the Stacks Project.

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedNewton.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedNewton.lean#L125). The attribute's comment: “In Situation 0GUJ with E|\_\{X ∖ Z} zero: Newton's recursion P\_\{q+1} = ∑\_\{j`<`q} (-1)^j c\_\{j+1} P\_\{q-j} + (-1)^q (q+1) c\_\{q+1} for every q ≥ 0, products in the algebra A^\{(1)}(Z → X) of 0FA0; it gives P\_1 = c\_1, P\_2 = c\_1² - 2c\_2, P\_3 = c\_1³ - 3c\_1c\_2 + 3c\_3 and so on, the whole lemma”.

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

**`Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedPowerSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean#L570). The attribute's comment: “for P\_p(Z → X, E), when E|\_(X ∖ Z) is zero: P\_p(Z → X, E) ∘ c = c ∘ P\_p(Z → X, E) in A^*(Y ×\_X Z → X), for every c in A^*(Y → X)”.

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

**`Stacks.Chow.LocalizedSituation.nonhomogeneousBivariantTransport_compositeOfInvertible_localizedChern`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/Commutation.lean#L621). The attribute's comment: “for c\_p(Z → X, E), when E|\_(X ∖ Z) is finite locally free of rank < p in degree 0: c\_p(Z → X, E) ∘ c = c ∘ c\_p(Z → X, E) in A^*(Y ×\_X Z → X), for every c in A^*(Y → X)”.

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

**`Stacks.Chow.LocalizedChernData.totalLocalizedChern`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChern.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChern.lean#L103). The attribute's comment: “c^(p)(Z → X, E) for E whose Chern classes are defined, with the localized Chern classes of 0GUK; in Situation 0GUJ it is the class of the remark (LocalizedSituation.totalLocalizedChern\_toLocalizedChernData)”.

> **Stacks 0FBC for a perfect object: the total localized Chern class**
> `c⁽ᵖ⁾(Z ⟶ X, E) ∈ A⁽ᵖ⁾(Z ⟶ X)`. Its component in a degree `0 ≤ i < p` is the Chern class
> `c_i(E) ∈ Aⁱ(X)`, in a negative degree it is `0`, and in a degree `i ≥ p` it is the localized Chern
> class `c_i(Z ⟶ X, E) ∈ Aⁱ(Z ⟶ X)` of Remark 0GUK. In Situation 0GUJ it is the class of
> Remark 0FBC, built from the classes of Stacks 0FB2
> (`Stacks.Chow.LocalizedSituation.totalLocalizedChern_toLocalizedChernData`).

```lean
def totalLocalizedChern :
    localizedBivariantGrading D.base (gysinSystemOfInvertible D.base) (D.i ≫ D.a) D.a D.i rfl D.p
```

**`Stacks.Chow.LocalizedChernData.totalLocalizedChern_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChern.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChern.lean#L112). The attribute's comment: “the components c\_i(E) in the degrees i < p, for E whose Chern classes are defined”.

> The components of `c⁽ᵖ⁾(Z ⟶ X, E)` below the cutoff are the Chern classes of `E` (zero in the
> negative degrees).

```lean
theorem totalLocalizedChern_fst (i : {i : ℤ // i < (D.p : ℤ)}) :
    (totalLocalizedChern hE h).1 i =
      (perfectChernClass D.base D.a hE).intComponent D.base D.a i.1
```

**`Stacks.Chow.LocalizedChernData.totalLocalizedChern_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChern.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChern.lean#L123). The attribute's comment: “the components c\_i(Z → X, E) of 0GUK in the degrees i ≥ p, for E whose Chern classes are defined”.

> The components of `c⁽ᵖ⁾(Z ⟶ X, E)` from the cutoff on are the localized Chern classes.

```lean
theorem totalLocalizedChern_snd (i : {i : ℤ // (D.p : ℤ) ≤ i}) :
    (totalLocalizedChern hE h).2 i = localizedChernOfLe hE h i
```

**`Stacks.Chow.LocalizedSituation.totalLocalizedChern`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean#L72). The attribute's comment: “the total localized Chern class c^(p)(Z → X, E) in A^(p)(Z → X), in Situation 0GUJ, with the localized Chern classes of 0FB2”.

> **Stacks 0FBC: the total localized Chern class**
> `c⁽ᵖ⁾(Z ⟶ X, E) = 1 + c₁(E) + … + c_{p-1}(E) + c_p(Z ⟶ X, E) + c_{p+1}(Z ⟶ X, E) + …` in the
> algebra `A⁽ᵖ⁾(Z ⟶ X)` of Remark 0FA0, in Situation 0GUJ with `E|_{X ∖ Z}` finite locally free of
> rank `< p` in degree `0`. Its component in a degree `i < p` is the Chern class `c_i(E) ∈ Aⁱ(X)`
> (zero in the negative degrees, `1` in degree `0`), and in a degree `i ≥ p` it is the localized
> Chern class `c_i(Z ⟶ X, E) ∈ Aⁱ(Z ⟶ X)` of Stacks 0FB2.

```lean
def totalLocalizedChern :
    localizedBivariantGrading S.base (gysinSystemOfInvertible S.base) (S.i ≫ S.a) S.a S.i rfl S.p
```

**`Stacks.Chow.LocalizedSituation.totalLocalizedChern_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean#L80). The attribute's comment: “the components c\_i(E) in the degrees i < p”.

> The components of `c⁽ᵖ⁾(Z ⟶ X, E)` in the degrees `i < p` are the Chern classes `c_i(E)`
> (zero in the negative degrees).

```lean
theorem totalLocalizedChern_fst (i : {i : ℤ // i < (S.p : ℤ)}) :
    (totalLocalizedChern h).1 i =
      (perfectChernClass S.base S.a S.hasDefinedChernClasses_E).intComponent S.base S.a i.1
```

**`Stacks.Chow.LocalizedSituation.totalLocalizedChern_fst_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean#L88). The attribute's comment: “the leading term 1 = c\_0(E) when p > 0”.

> For `p > 0` the component of `c⁽ᵖ⁾(Z ⟶ X, E)` in degree `0` is `c₀(E) = 1`, the leading term
> `1` of the display of Remark 0FBC.

```lean
theorem totalLocalizedChern_fst_zero (hp : 0 < S.p) :
    (totalLocalizedChern h).1 ⟨0, by exact_mod_cast hp⟩ =
      (1 : TotalChowClass S.base S.a).intComponent S.base S.a 0
```

**`Stacks.Chow.LocalizedSituation.totalLocalizedChern_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/TotalLocalizedChernSituation.lean#L100). The attribute's comment: “the components c\_i(Z → X, E) of 0FB2 in the degrees i ≥ p”.

> The components of `c⁽ᵖ⁾(Z ⟶ X, E)` in the degrees `i ≥ p` are the localized Chern classes
> `c_i(Z ⟶ X, E)` of Stacks 0FB2.

```lean
theorem totalLocalizedChern_snd (i : {i : ℤ // (S.p : ℤ) ≤ i}) :
    (totalLocalizedChern h).2 i = localizedChernOfLe h i
```

## Tag 0FBD, a lemma

[Tag 0FBD](https://stacks.math.columbia.edu/tag/0FBD) in the Stacks Project.

**`Stacks.Chow.LocalizedChernData.totalLocalizedChern_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean, line 991](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean#L991).

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

**`Stacks.Chow.LocalizedChernData.localizedPowerSum_localizedChernChar_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean, line 1155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/WhitneyLocalized.lean#L1155).

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

**`Stacks.Chow.LocalizedSituation.localizedPowerSum_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L157). The attribute's comment: “the formula for P\_p(Z\_1 cap Z\_2 -> X, F\_1 tensor^L F\_2), with Z\_1 cap Z\_2 = Z\_1 x\_X Z\_2 and the products those of 0FE5 (supportedIntersectionMul). The source leaves implicit in which sense F\_1 tensor^L F\_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F\_1 tensor^L F\_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

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

**`Stacks.Chow.LocalizedSituation.localizedChern_one_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L187). The attribute's comment: “the formula for c\_1(Z\_1 cap Z\_2 -> X, F\_1 tensor^L F\_2), r\_i = P\_0(Z\_i -> X, F\_i); the product r\_2 c\_1(Z\_1 -> X, F\_1) is taken for Z\_1 cap Z\_2 presented as Z\_2 x\_X Z\_1 through the flipped square. The source leaves implicit in which sense F\_1 tensor^L F\_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F\_1 tensor^L F\_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

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

**`Stacks.Chow.LocalizedSituation.localizedChern_two_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L237). The attribute's comment: “the formula for c\_2(Z\_1 cap Z\_2 -> X, F\_1 tensor^L F\_2); the squares are the products res(c) o c of 0FA0 (supportedMul), C(r\_i, 2) is the class of x |-> C(chi\_\{F\_i}(x), 2) (LocalizedChernData.rankChoose), and (r\_1 r\_2 - 1) c c' is read as (r\_1 r\_2)(c c') - c c'. The source's 'and so on for higher Chern classes' is not formalized. The source leaves implicit in which sense F\_1 tensor^L F\_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F\_1 tensor^L F\_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

> **The second localized Chern class of a derived tensor product.** In the situation of
> `Stacks.Chow.LocalizedSituation.localizedPowerSum_derivedTensor`, with
> `r_i = P_0(Z_i ⟶ X, F_i)`, `γ_{i,p} = c_p(Z_i ⟶ X, F_i)` and `C(r_i, 2)` the class
> `Stacks.Chow.LocalizedChernData.rankChoose`,
>
>   `c\_2(Z₁ ∩ Z₂ ⟶ X, F₁ ⊗^L F₂) = r₁ γ\_\{2,2} + r₂ γ\_\{1,2} + C(r₁, 2) γ\_\{2,1}² +
>     ((r₁ r₂) (γ\_\{2,1} γ\_\{1,1}) - γ\_\{2,1} γ\_\{1,1}) + C(r₂, 2) γ\_\{1,1}²`
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

**`Stacks.Chow.LocalizedSituation.localizedChernChar_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/LocalizedChern/LocalizedDerivedTensor.lean#L328). The attribute's comment: “the formula ch(Z\_1 cap Z\_2 -> X, F\_1 tensor^L F\_2) = ch(Z\_1 -> X, F\_1) ch(Z\_2 -> X, F\_2), read degree by degree in prod\_p A^p(Z\_1 cap Z\_2 -> X) tensor Q. The source leaves implicit in which sense F\_1 tensor^L F\_2 satisfies (3) of 0GUJ in the mixed cases ((c) for one factor and (d) for the other, or (d) for both with different X'); the classes of F\_1 tensor^L F\_2 are those of Remark 0GUK, defined for every perfect object with defined Chern classes, which covers them.”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
