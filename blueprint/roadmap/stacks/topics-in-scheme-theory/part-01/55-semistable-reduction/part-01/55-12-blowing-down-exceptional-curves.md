---
declaration: section
origin: cited
lean: Stacks.Models.RegularProperModelSituation.contractedSituation, Stacks.Models.RegularProperModelSituation.exists_isContractionOfExceptionalCurve_specialFiberComponentIdeal, Stacks.Models.RegularProperModelSituation.exists_contractedComponentEquiv, Stacks.Models.RegularProperModelSituation.exists_contractedComponentMap, Stacks.Models.RegularProperModelSituation.contractedSpecialFiberIntersectionMatrix, Stacks.Models.RegularProperModelSituation.cast_specialFiberComponentGenus_contractedComponentEquiv, Stacks.Models.RegularProperModelSituation.associatedNumericalType_contraction_comparison, Stacks.Models.isProjectiveLineSpecialFiber_of_isMinimalModel
statement: formalized
proof: formalized
---

# 55.12 Blowing down exceptional curves

Section 55.12 of the Stacks Project, [Tag 0CEF](https://stacks.math.columbia.edu/tag/0CEF). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C6C, a lemma

[Tag 0C6C](https://stacks.math.columbia.edu/tag/0C6C) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.contractedSituation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponent.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponent.lean#L392). The attribute's comment: “X' is as in Situation 0C61: a regular proper model of the same curve”.

> **Stacks Project, Tag 0C6C, the contracted model.** Let `f : X ⟶ X'` contract an
> irreducible component `C_n` of the special fibre of a regular proper model `X` of `C`. Then `X'`,
> with the structure morphism through which `X ⟶ Spec R` factors, is again a regular proper model
> of `C` over the same discrete valuation ring: it is the standing situation of
> [Stacks, Tag 0C61] with `X'` in place of `X`.

```lean
public abbrev contractedSituation
    (hf : IsContractionOfExceptionalCurve (S.specialFiberComponentIdeal N) f) :
    RegularProperModelSituation.{u}
```

**`Stacks.Models.RegularProperModelSituation.exists_isContractionOfExceptionalCurve_specialFiberComponentIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentExists.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentExists.lean#L40). The attribute's comment: “the contraction f : X -> X' of the exceptional component C\_n exists”.

> **Stacks Project, Tag 0C6C, the contraction.** In Situation 0C61, an irreducible component
> `C_n` of the special fibre which is an exceptional curve of the first kind can be contracted:
> there is a contraction `f : X ⟶ X'` of `C_n`.

```lean
theorem exists_isContractionOfExceptionalCurve_specialFiberComponentIdeal
    (N : irreducibleComponents S.specialFiber) {κ : Type u} [Field κ]
    {e : projectiveLineProj κ ≅ (S.specialFiberComponentIdeal N).subscheme}
    (hN : (S.specialFiberComponentIdeal N).IsExceptionalCurveOfFirstKind κ e) :
    ∃ (X' : Scheme.{u}) (f : S.X ⟶ X'),
      IsContractionOfExceptionalCurve (S.specialFiberComponentIdeal N) f
```

**`Stacks.Models.RegularProperModelSituation.exists_contractedComponentEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentFibre.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentFibre.lean#L419). The attribute's comment: “the components C'\_i = f(C\_i), i < n, of X'\_k and their multiplicities m'\_i = m\_i”.

> **The components and multiplicities of the contracted model.** Let
> `f : X ⟶ X'` contract the component `C_n` of the special fibre of a regular proper model `X`,
> and let `X'` be the regular proper model of
> `Stacks.Models.RegularProperModelSituation.contractedSituation`. Then `f` lies over `Spec R` and
> over the identification of both generic fibres with `C`, and the images `C'_i = f(C_i)` of the
> components `C_i ≠ C_n` are exactly the `n - 1` irreducible components of `X'_k`, with
> multiplicities `m'_i = m_i`.

```lean
public theorem exists_contractedComponentEquiv
    (hf : IsContractionOfExceptionalCurve (S.specialFiberComponentIdeal N) f) :
    f ≫ (S.contractedSituation hf).X_to_R = S.X_to_R ∧
      (S.contractedSituation hf).genericFiberIso.hom ≫
          pullback.fst (S.contractedSituation hf).X_to_R
            (Spec.map (CommRingCat.ofHom (algebraMap S.R S.K))) =
        S.genericFiberIso.hom ≫ pullback.fst S.X_to_R _ ≫ f ∧
      Fintype.card (irreducibleComponents (S.contractedSituation hf).specialFiber) + 1 =
        Fintype.card (irreducibleComponents S.specialFiber) ∧
      ∃ σ : {Z : irreducibleComponents S.specialFiber // Z ≠ N} ≃
          irreducibleComponents (S.contractedSituation hf).specialFiber,
        ∀ Z, (S.contractedSituation hf).specialFiberι.base ''
              ((σ Z).1 : Set (S.contractedSituation hf).specialFiber) =
            f.base '' (S.specialFiberι.base '' (Z.1.1 : Set S.specialFiber)) ∧
          (S.contractedSituation hf).specialFiberMultiplicity (σ Z) =
            S.specialFiberMultiplicity Z.1
```

**`Stacks.Models.RegularProperModelSituation.exists_contractedComponentMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentFibre.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentFibre.lean#L501). The attribute's comment: “part (2): maps κ\_i ← κ'\_i → κ\_n when C\_i meets C\_n”.

> **The maps `κ_i ← κ'_i → κ_n`.** If `C_i` meets `C_n`, there are morphisms `C_i ⟶ C'_i` and
> `C_n ⟶ C'_i` compatible with the contraction and with the closed immersions into `X` and `X'`,
> and their maps of global sections are ring maps `κ_i ← κ'_i → κ_n`, where `κ_i`, `κ'_i`, `κ_n`
> are the rings of global functions on `C_i`, `C'_i`, `C_n`.

```lean
public theorem exists_contractedComponentMap
    (hf : IsContractionOfExceptionalCurve (S.specialFiberComponentIdeal N) f)
    (Z : {Z : irreducibleComponents S.specialFiber // Z ≠ N})
    (hmeet : ((Z.1.1 : Set S.specialFiber) ∩ N.1).Nonempty) :
    ∃ (φ : Γ(((S.contractedSituation hf).specialFiberComponentIdeal
          (S.contractedComponentEquiv hf Z)).subscheme, ⊤) ⟶
          Γ((S.specialFiberComponentIdeal Z.1).subscheme, ⊤))
      (ψ : Γ(((S.contractedSituation hf).specialFiberComponentIdeal
          (S.contractedComponentEquiv hf Z)).subscheme, ⊤) ⟶
          Γ((S.specialFiberComponentIdeal N).subscheme, ⊤))
      (g : (S.specialFiberComponentIdeal Z.1).subscheme ⟶
        ((S.contractedSituation hf).specialFiberComponentIdeal
          (S.contractedComponentEquiv hf Z)).subscheme)
      (h : (S.specialFiberComponentIdeal N).subscheme ⟶
        ((S.contractedSituation hf).specialFiberComponentIdeal
          (S.contractedComponentEquiv hf Z)).subscheme),
      g ≫ ((S.contractedSituation hf).specialFiberComponentIdeal
          (S.contractedComponentEquiv hf Z)).subschemeι =
          (S.specialFiberComponentIdeal Z.1).subschemeι ≫ f ∧
        h ≫ ((S.contractedSituation hf).specialFiberComponentIdeal
          (S.contractedComponentEquiv hf Z)).subschemeι =
          (S.specialFiberComponentIdeal N).subschemeι ≫ f ∧
        g.appTop = φ ∧ h.appTop = ψ
```

**`Stacks.Models.RegularProperModelSituation.contractedSpecialFiberIntersectionMatrix`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentIntersection.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentIntersection.lean#L453). The attribute's comment: “part (1): (C'\_i · C'\_j) = (C\_i · C\_j) - (C\_i · C\_n)(C\_j · C\_n)/(C\_n · C\_n)”.

> **Stacks Project, Tag 0C6C, part (1).** Let `f : X ⟶ X'` contract the component `C_n` of the
> special fibre of a regular proper model, and let `C'_i = f(C_i)`, `i < n`, be the components of
> the special fibre of the contracted model. Then for `i, j < n`
>
> `(C'_i · C'_j) = (C_i · C_j) - (C_i · C_n)(C_j · C_n) / (C_n · C_n)`.

```lean
public theorem contractedSpecialFiberIntersectionMatrix
    (hf : IsContractionOfExceptionalCurve (S.specialFiberComponentIdeal N) f)
    [DecidableEq (irreducibleComponents S.specialFiber)]
    [DecidableEq (irreducibleComponents (S.contractedSituation hf).specialFiber)]
    (Z W : {Z : irreducibleComponents S.specialFiber // Z ≠ N}) :
    ((S.contractedSituation hf).specialFiberIntersectionMatrix (S.contractedComponentEquiv hf Z)
        (S.contractedComponentEquiv hf W) : ℚ) =
      S.specialFiberIntersectionMatrix Z.1 W.1 -
        S.specialFiberIntersectionMatrix Z.1 N * S.specialFiberIntersectionMatrix W.1 N /
          S.specialFiberIntersectionMatrix N N
```

## Tag 0CA8, a remark

[Tag 0CA8](https://stacks.math.columbia.edu/tag/0CA8) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.cast_specialFiberComponentGenus_contractedComponentEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentGenus.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentGenus.lean#L446). The attribute's comment: “g'\_i = (w\_i/w'\_i)(g\_i - 1) + 1 + ((C\_i · C\_n)^2 - w\_n(C\_i · C\_n))/(2 w'\_i w\_n)”.

> **The genus of a component after contracting an exceptional curve** ([Stacks, Remark 0CA8]).
> In the situation of [Stacks, Tag 0C6C] — `X` a regular proper model of `C` over a discrete
> valuation ring with residue field `k`, `C_n` a component of the special fibre which is an
> exceptional curve of the first kind, `f : X ⟶ X'` its contraction, and `C'_i = f(C_i)` for
> `i ≠ n` — the genus `g'_i` of `C'_i` is
>
> `g'_i = (w_i/w'_i)(g_i - 1) + 1 + ((C_i · C_n)² - w_n(C_i · C_n)) / (2 w'_i w_n)`,
>
> where `w_i = [κ_i : k]`, `w_n = [κ_n : k]`, `w'_i = [κ'_i : k]` and `g_i` is the genus of `C_i`.
> Here `X'` is the regular proper model
> `Stacks.Models.RegularProperModelSituation.contractedSituation` and `C'_i` its component
> `Stacks.Models.RegularProperModelSituation.contractedComponentEquiv`. The components are indexed
> by `irreducibleComponents X_k`, the exceptional curve being presented as `𝐏¹_κ` by `ε`.

```lean
theorem cast_specialFiberComponentGenus_contractedComponentEquiv
    [DecidableEq (irreducibleComponents S.specialFiber)]
    (hf : IsContractionOfExceptionalCurve (S.specialFiberComponentIdeal N) f)
    (κ : Type u) [Field κ] {ε : projectiveLineProj κ ≅ (S.specialFiberComponentIdeal N).subscheme}
    (hE : (S.specialFiberComponentIdeal N).IsExceptionalCurveOfFirstKind κ ε)
    (Z : {Z : irreducibleComponents S.specialFiber // Z ≠ N}) :
    ((S.contractedSituation hf).specialFiberComponentGenus (S.contractedComponentEquiv hf Z) : ℚ) =
      (S.specialFiberComponentWeight Z.1 : ℚ) /
          ((S.contractedSituation hf).specialFiberComponentWeight
            (S.contractedComponentEquiv hf Z) : ℚ) *
          ((S.specialFiberComponentGenus Z.1 : ℚ) - 1) + 1 +
        ((S.specialFiberIntersectionMatrix Z.1 N : ℚ) ^ 2 -
            (S.specialFiberComponentWeight N : ℚ) * S.specialFiberIntersectionMatrix Z.1 N) /
          (2 * ((S.contractedSituation hf).specialFiberComponentWeight
            (S.contractedComponentEquiv hf Z) : ℚ) * (S.specialFiberComponentWeight N : ℚ))
```

## Tag 0CA9, a remark

[Tag 0CA9](https://stacks.math.columbia.edu/tag/0CA9) in the Stacks Project.

**`Stacks.Models.RegularProperModelSituation.associatedNumericalType_contraction_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentNumericalType.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/ContractExceptionalComponentNumericalType.lean#L68). The attribute's comment: “corrected: w'\_i | w\_n is stated for the components C\_i meeting C\_n, where 0C6C (2) gives the maps; a component missing C\_n keeps w'\_i = w\_i, which need not divide w\_n”.

> **Stacks Project, Tag 0CA9.** Let `f : X ⟶ X'` contract a component `C_n` of the special
> fibre of a regular proper model which is an exceptional curve of the first kind. Enumerate the
> components of `X_k` by `e`, with `C_n` last, and those of `X'_k` by `e'`, compatibly with
> `C'_i = f(C_i)`. Let `T` and `T'` be the numerical types associated to `X` and `X'`. Then
> * `n` is a `(-1)`-index of `T`, and `T'` agrees with the contraction of `T` of Tag 0C77 except
>   for the weights: `n' = n - 1`, `m'_i = m_i`, `a'_{ij} = a_{ij} - a_{in}a_{jn}/a_{nn}`, `g'_i` is
>   the genus formula at `w'_i`, and `w'_i` is a positive integer dividing `w_i`;
> * `w'_i` divides `w_n` when `a_{in} ≠ 0` (that is, when `C_i` meets `C_n`), and `w'_i = w_i`
>   when `a_{in} = 0`;
> * the numerical contraction `T''` of Tag 0C77 has the same `n'`, `m'_i` and `a'_{ij}` as `T'`, and
>   its weight `w''_i` is the largest positive integer dividing `w_i` for which the genus formula is
>   an integer; in particular `w'_i ≤ w''_i`;
> * for every numerical type which is a contraction of `T` up to weight (so with any weights
>   `w'_i ∣ w_i`, the geometric `T'` among them) the map `Pic(T) → Pic(T')` of Tag 0C7J is injective.
>
> The source asserts `w'_i ∣ w_n` for every `i`; for a component missing `C_n` the weight is `w_i`,
> which need not divide `w_n` (for the numerical datum, see
> `AlgebraicGeometry.NumericalType.exists_intersection_eq_zero_not_weight_dvd`), so that
> divisibility is stated for the components meeting `C_n`.

```lean
public theorem associatedNumericalType_contraction_comparison
    [DecidableEq (irreducibleComponents S.specialFiber)]
    (hf : IsContractionOfExceptionalCurve (S.specialFiberComponentIdeal N) f)
    [DecidableEq (irreducibleComponents (S.contractedSituation hf).specialFiber)]
    (κ : Type u) [Field κ] {ε : projectiveLineProj κ ≅ (S.specialFiberComponentIdeal N).subscheme}
    (hE : (S.specialFiberComponentIdeal N).IsExceptionalCurveOfFirstKind κ ε)
    (n : ℕ) (e : Fin n ≃ irreducibleComponents S.specialFiber)
    (e' : Fin (n - 1) ≃ irreducibleComponents (S.contractedSituation hf).specialFiber)
    (hN : e (lastIndex (S.associatedNumericalType n e)) = N)
    (he' : ∀ i, ((S.contractedComponentEquiv hf).symm (e' i)).1 =
      e (remainingIndex (S.associatedNumericalType n e) i)) :
    let T := S.associatedNumericalType n e
    let T' := (S.contractedSituation hf).associatedNumericalType (n - 1) e'
    ∃ h : IsMinusOneIndex T (lastIndex T), ∃ hT : IsContractionUpToWeight T T',
      -- the geometric weights
      (∀ i, T.intersection (remainingIndex T i) (lastIndex T) ≠ 0 →
          T'.weight (Fin.cast hT.componentCount_eq.symm i) ∣ T.weight (lastIndex T)) ∧
      (∀ i, T.intersection (remainingIndex T i) (lastIndex T) = 0 →
          T'.weight (Fin.cast hT.componentCount_eq.symm i) = T.weight (remainingIndex T i)) ∧
      -- comparison with the numerical contraction of Tag 0C77
      T'.componentCount = (contractLast T h).val.componentCount ∧
      (∀ i, T'.multiplicity (Fin.cast hT.componentCount_eq.symm i) =
          (contractLast T h).val.multiplicity
            (Fin.cast (contractLast T h).property.componentCount_eq.symm i)) ∧
      (∀ i j, T'.intersection (Fin.cast hT.componentCount_eq.symm i)
            (Fin.cast hT.componentCount_eq.symm j) =
          (contractLast T h).val.intersection
            (Fin.cast (contractLast T h).property.componentCount_eq.symm i)
            (Fin.cast (contractLast T h).property.componentCount_eq.symm j)) ∧
      (∀ i, T'.weight (Fin.cast hT.componentCount_eq.symm i) ≤
          (contractLast T h).val.weight
            (Fin.cast (contractLast T h).property.componentCount_eq.symm i)) ∧
      -- the numerical weight is the largest admissible one
      (∀ i, IsGreatest {d : ℤ | 0 < d ∧ d ∣ T.weight (remainingIndex T i) ∧
          ∃ G : ℤ, (G : ℚ) = (T.weight (remainingIndex T i) : ℚ) / d *
              ((T.componentGenus (remainingIndex T i) : ℚ) - 1) + 1 +
            ((T.intersection (remainingIndex T i) (lastIndex T) : ℚ) ^ 2 -
                T.weight (lastIndex T) * T.intersection (remainingIndex T i) (lastIndex T)) /
              (2 * d * T.weight (lastIndex T))}
        ((contractLast T h).val.weight
          (Fin.cast (contractLast T h).property.componentCount_eq.symm i))) ∧
      -- injectivity on Picard groups for smaller weights
      ∀ (T'' : NumericalType) (hT'' : IsContractionUpToWeight T T''),
        Function.Injective (hT''.picardMap h)
```

## Tag 0CDA, a lemma

[Tag 0CDA](https://stacks.math.columbia.edu/tag/0CDA) in the Stacks Project.

**`Stacks.Models.isProjectiveLineSpecialFiber_of_isMinimalModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelGenusZero.lean, line 619](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Models/MinimalModelGenusZero.lean#L619).

> **Stacks Project, Tag 0CDA.** Let `C` be a smooth projective curve over `K` with
> `H⁰(C, 𝒪_C) = K` and genus `0`. If there is more than one minimal model for `C` — two minimal
> models which are not isomorphic as models of `C` — then the special fibre of every minimal model
> is isomorphic to `𝐏¹_k` over the residue field `k`.

```lean
theorem isProjectiveLineSpecialFiber_of_isMinimalModel {C : Scheme.{u}} (c : C ⟶ Spec (.of K))
    [IsCurve K c] [Smooth c] (_hproj : Stacks.HProjective.IsHProjective c)
    (_hH0 : IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)) (_hg : genus c = 0)
    (hmore : ∃ (X₁ X₂ : Scheme.{u}) (p₁ : X₁ ⟶ Spec (.of R)) (p₂ : X₂ ⟶ Spec (.of R))
      (e₁ : C ≅ pullback p₁ (Spec.map (CommRingCat.ofHom (algebraMap R K))))
      (e₂ : C ≅ pullback p₂ (Spec.map (CommRingCat.ofHom (algebraMap R K)))),
      IsMinimalModel c p₁ e₁ ∧ IsMinimalModel c p₂ e₂ ∧
        ¬ ∃ φ : X₁ ≅ X₂, φ.hom ≫ p₂ = p₁ ∧
          e₁.hom ≫ pullback.fst p₁ (Spec.map (CommRingCat.ofHom (algebraMap R K))) ≫ φ.hom =
            e₂.hom ≫ pullback.fst p₂ (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    {X : Scheme.{u}} (p : X ⟶ Spec (.of R))
    (e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K))))
    (hX : IsMinimalModel c p e) : IsProjectiveLineSpecialFiber p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.12, Tag 0CEF](https://stacks.math.columbia.edu/tag/0CEF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
