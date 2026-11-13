---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.Truncated.exists_rightAdjoint_truncation, CategoryTheory.SimplicialObject.Truncated.existsUnique_iso_rightAdjoint_truncation, CategoryTheory.SimplicialObject.Truncated.coskConeIsLimit, CategoryTheory.SimplicialObject.Truncated.map_eq_coskConeIsLimit_lift, CategoryTheory.SimplicialObject.Truncated.coskAdjunction, CategoryTheory.SimplicialObject.bijective_app_zero_comp_π, CategoryTheory.SimplicialObject.Truncated.hasPointwiseRightKanExtension_of_hasFiniteLimits, CategoryTheory.SimplicialObject.Truncated.sliceCone_isLimit
statement: formalized
proof: formalized
---

# 14.19 Coskeleton functors

Section 14.19 of the Stacks Project, [Tag 0AMA](https://stacks.math.columbia.edu/tag/0AMA). 16 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AMA, the section

[Tag 0AMA](https://stacks.math.columbia.edu/tag/0AMA) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.exists_rightAdjoint_truncation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean#L82). The attribute's comment: “the section's assertion that `cosk_m` exists for every `m` over a category with finite limits, which is Lemma 0183 inside the section; the degreewise limit formula is `coskConeIsLimit` below”. References: SGA 4 V (7.1.0), “partial”; SGA 4 Vbis (3.0.1).

> **Stacks 0AMA**.
> If `C` has finite limits then for every `m` the skeleton functor `sk_m : Simp(C) ⥤ Simp_m(C)` has
> a right adjoint, so that the coskeleton functor `cosk_m` exists: morphisms `U ⟶ cosk_m V` of
> simplicial objects correspond naturally to morphisms `sk_m U ⟶ V` of `m`-truncated ones.

```lean
theorem exists_rightAdjoint_truncation [HasFiniteLimits C] (m : ℕ) :
    ∃ G : SimplicialObject.Truncated C m ⥤ SimplicialObject C,
      Nonempty (SimplicialObject.truncation (C := C) m ⊣ G)
```

**`CategoryTheory.SimplicialObject.Truncated.existsUnique_iso_rightAdjoint_truncation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean#L103). The attribute's comment: “the section's uniqueness assertion, that a representing object `cosk_m V` is unique up to unique isomorphism by the Yoneda lemma; `compatible with the counits` is the form the uniqueness takes for the adjunctions themselves”.

> **Stacks 0AMA**.
> A right adjoint of `sk_m` is unique up to unique isomorphism: if `G` and `G'` are both right
> adjoint to `sk_m`, there is exactly one isomorphism `G ≅ G'` compatible with the two counits.

```lean
theorem existsUnique_iso_rightAdjoint_truncation {m : ℕ}
    {G G' : SimplicialObject.Truncated C m ⥤ SimplicialObject C}
    (adj : SimplicialObject.truncation (C := C) m ⊣ G)
    (adj' : SimplicialObject.truncation (C := C) m ⊣ G') :
    ∃! e : G ≅ G',
      Functor.whiskerRight e.hom (SimplicialObject.truncation m) ≫ adj'.counit = adj.counit
```

**`CategoryTheory.SimplicialObject.Truncated.coskConeIsLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean#L161). The attribute's comment: “the degreewise limit formula”. References: SGA 4 Vbis (3.0.1), “partial”.

> **Stacks 0AMA**.
> The degreewise limit formula for the coskeleton: for an `m`-truncated simplicial object `U` of a
> category with finite limits the canonical cone over `U(n)` with apex `(cosk_m U)_n` is a limit
> cone, so `(cosk_m U)_n` is the limit of `U(n)` over `((Δ/[n])_{≤ m})ᵒᵖ`.

```lean
noncomputable def coskConeIsLimit (m : ℕ) (U : SimplicialObject.Truncated C m) (n : ℕ) :
    IsLimit (coskCone m U n)
```

**`CategoryTheory.SimplicialObject.Truncated.map_eq_coskConeIsLimit_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean#L188). The attribute's comment: “the second clause of the degreewise limit formula, that for `φ : [n] → [n']` the map `cosk_m U(φ)` comes from the identification of `U(n')` restricted along `φ` with `U(n)`”.

> **Stacks 0AMA**.
> The naturality half of the degreewise limit formula: `cosk_m U(φ)` is the morphism of limits
> induced by postcomposition with `φ : [n] → [n']`, the canonical cone in degree `n'` restricted
> along that functor being a cone over `U(n)`.

```lean
theorem map_eq_coskConeIsLimit_lift {m : ℕ} (U : SimplicialObject.Truncated C m) {n n' : ℕ}
    (φ : SimplexCategory.mk n ⟶ SimplexCategory.mk n') :
    ((Truncated.cosk m).obj U).map φ.op =
      (coskConeIsLimit m U n).lift
        ((coskCone m U n').whisker (CostructuredArrow.map φ).op)
```

## Tag 0181, an equation

[Tag 0181](https://stacks.math.columbia.edu/tag/0181) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.coskAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/LimitFormula.lean#L93). The attribute's comment: “the displayed bijection, for `cosk_m` itself”. References: SGA 4 V (7.1.0), “adjunction i\_n* ⊣ i\_\{n*}”; SGA 4 Vbis (3.0.1).

> **The bijection `Mor(U, cosk_m V) = Mor(sk_m U, V)`** of [Stacks, Equation 0181], over a
> category with finite limits: the coskeleton functor is right adjoint to the skeleton functor, an
> adjunction being exactly that bijection, natural in both variables.

```lean
noncomputable def coskAdjunction [HasFiniteLimits C] (m : ℕ) :
    SimplicialObject.truncation (C := C) m ⊣ Truncated.cosk m
```

## Tag 0182, an example

[Tag 0182](https://stacks.math.columbia.edu/tag/0182) in the Stacks Project.

**`CategoryTheory.SimplicialObject.bijective_app_zero_comp_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L170). The attribute's comment: “the self-product simplicial object is stated abstractly, by product cones on the terms of an arbitrary `U`, rather than by choosing a model of `X ^ (n + 1)`; the hom-set formula is reduced, as in the source, to `Mor(V, U) = Mor(V₀, X)`”.

> **Stacks 0182**.
> The `0`-coskeleton of an object `X` is the simplicial object `n ↦ X^{n + 1}`. Let `U` be a
> simplicial object of `C` whose term `U_n` is the product of `n + 1` copies of `X`, with projections
> `π n i : U_n ⟶ X` indexed by the vertices `i` of `⦋n⦌` (`hU`), the simplicial structure maps acting
> on coordinates by `(x_0, …, x_m) ↦ (x_{φ(0)}, …, x_{φ(n)})` (`hπ`). Then for every simplicial
> object `V` of `C`, a morphism `V ⟶ U` is determined by and determines a single morphism `V_0 ⟶ X`,
> namely the composite of its degree-`0` component with the projection `π 0 0`. In other words
> `Mor(V, U) = Mor(V_0, X)`, so that `U` is the coskeleton `cosk₀(X)`.

```lean
public theorem bijective_app_zero_comp_π {X : C} {U : SimplicialObject C}
    (π : ∀ n : ℕ, Fin (n + 1) → (U.obj (op ⦋n⦌) ⟶ X))
    (hU : ∀ n : ℕ, IsLimit (Fan.mk (U.obj (op ⦋n⦌)) (π n)))
    (hπ : ∀ {n m : ℕ} (φ : ⦋n⦌ ⟶ ⦋m⦌) (i : Fin (n + 1)),
      U.map φ.op ≫ π n i = π m (φ.toOrderHom i))
    (V : SimplicialObject C) :
    Function.Bijective (fun f : V ⟶ U => f.app (op ⦋0⦌) ≫ π 0 0)
```

## Tag 0183, a lemma

[Tag 0183](https://stacks.math.columbia.edu/tag/0183) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.hasPointwiseRightKanExtension_of_hasFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean, line 788](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean#L788). The attribute's comment: “existence and the displayed limit formula; the formula is the defining universal property of `HasPointwiseRightKanExtension` at each simplex”. References: SGA 4 Vbis (3.0.1).

> If `C` has finite limits, every truncated simplicial object has the pointwise right Kan
> extension along `( Δ_{≤ k} ⊆ Δ )ᵒᵖ` which defines its `k`-coskeleton. Pointwiseness says that its
> value at `[n]` is the limit over the finite structured-arrow category `((Δ/[n])_{≤ k})ᵒᵖ`, and
> functoriality supplies the maps induced by `[n] → [n']`.

```lean
public theorem hasPointwiseRightKanExtension_of_hasFiniteLimits [HasFiniteLimits C]
    (k : ℕ) (F : SimplicialObject.Truncated C k) :
    (SimplexCategory.Truncated.inclusion k).op.HasPointwiseRightKanExtension F
```

## Tag 0184, a lemma

[Tag 0184](https://stacks.math.columbia.edu/tag/0184) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.sliceCone_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 1000](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L1000).

> **Stacks 0184**.
> Let `C` be a category and let `U` be an `m`-truncated simplicial object of `C`. For `n ≤ m` the
> limit of the diagram `U(n)` exists in `C` and is canonically isomorphic to `U_n`: the canonical
> cone, with apex `U_n` and component `U(α) : U_n → U_k` at an object `α : [k] → [n]`, is a limit
> cone.

```lean
theorem sliceCone_isLimit {m : ℕ} (U : SimplicialObject.Truncated C m) {n : ℕ} (h : n ≤ m) :
    Nonempty (IsLimit (sliceCone U h))
```

## Tag 0185, a lemma

[Tag 0185](https://stacks.math.columbia.edu/tag/0185) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.isIso_ranAdjunction_counit_app_of_hasFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean, line 805](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean#L805). The attribute's comment: “`sk_n` is the truncation `truncation n` and the morphism is the counit at `U` of `ranAdjunction`, truncation ⊣ `cosk_n`, whose right Kan extensions exist by Lemma 0183”.

> Let `C` be a category with finite limits and let `U` be an `n`-truncated simplicial object
> of `C`. Then the morphism `sk_n cosk_n U → U` is an isomorphism. Here `sk_n` is the truncation
> functor `truncation n : SimplicialObject C ⥤ SimplicialObject.Truncated C n`, its right adjoint
> `cosk_n` is the right Kan extension along `(Δ_{≤n} ⊆ Δ)ᵒᵖ`, which exists by [Stacks, Lemma 0183]
> (`hasPointwiseRightKanExtension_of_hasFiniteLimits`), and the morphism is the counit at `U` of the
> adjunction `ranAdjunction` between them.

```lean
public theorem isIso_ranAdjunction_counit_app_of_hasFiniteLimits [HasFiniteLimits C] (n : ℕ)
    (U : SimplicialObject.Truncated C n) :
    haveI := hasPointwiseRightKanExtension_of_hasFiniteLimits (C := C) n
    IsIso (((SimplexCategory.Truncated.inclusion n).op.ranAdjunction C).counit.app U)
```

## Tag 0186, a lemma

[Tag 0186](https://stacks.math.columbia.edu/tag/0186) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.existsUnique_cone_app_δ_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L373). The attribute's comment: “the representing object of the functor of matching families is the limit over the truncated slice category, via restriction of a cone to its legs at the faces”.

> **Stacks 0186**.
> A matching family of morphisms into the top term of a truncated simplicial object is the same thing
> as a cone over the truncated slice category. Let `U` be an `(n + 1)`-truncated simplicial object of
> `C` and let `f i : T ⟶ U_{n + 1}`, `i = 0, …, n + 2`, be a family of morphisms. Then `f` extends,
> in exactly one way, to a cone over the diagram `(Δ/⦋n + 2⦌)^{opp}_{≤ n + 1} → C` defined by `U`
> whose leg at the face `δ_i : ⦋n + 1⦌ ⟶ ⦋n + 2⦌` is `f i`, if and only if `f` is a matching family:
> `f i ≫ d_j = f (j + 1) ≫ d_i` for all `i ≤ j`.
> Consequently, if the functor of matching families is represented by an object `U_{n + 2}`, then
> `U_{n + 2} = lim_{(Δ/⦋n + 2⦌)^{opp}_{≤ n + 1}} U`.

```lean
public theorem existsUnique_cone_app_δ_eq_iff (U : SimplicialObject.Truncated C (n + 1)) (T : C)
    (f : Fin (n + 3) →
      (T ⟶ U.obj (op (⟨⦋n + 1⦌, le_rfl⟩ : SimplexCategory.Truncated (n + 1))))) :
    (∃! π : (Functor.const (StructuredArrow (op ⦋n + 2⦌)
          (SimplexCategory.Truncated.inclusion (n + 1)).op)).obj T ⟶
        StructuredArrow.proj (op ⦋n + 2⦌)
          (SimplexCategory.Truncated.inclusion (n + 1)).op ⋙ U,
      ∀ i : Fin (n + 3), π.app (StructuredArrow.mk
        (Y := op (⟨⦋n + 1⦌, le_rfl⟩ : SimplexCategory.Truncated (n + 1)))
        (SimplexCategory.δ i).op) = f i) ↔
      ∀ i j : Fin (n + 2), i ≤ j →
        f i.castSucc ≫ U.map (SimplexCategory.Truncated.δ (n + 1) j n.le_succ le_rfl).op =
          f j.succ ≫ U.map (SimplexCategory.Truncated.δ (n + 1) i n.le_succ le_rfl).op
```

## Tag 0187, a lemma

[Tag 0187](https://stacks.math.columbia.edu/tag/0187) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.exists_isRightKanExtension_of_matchingFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L509). The attribute's comment: “the adjointness is stated as the universal property of a right Kan extension along the inclusion of the truncated simplex categories”.

> **Stacks 0187**.
> One-step extension of a truncated simplicial object, and its adjointness. Let `U` be an
> `(n + 1)`-truncated simplicial object of `C`, and suppose that the contravariant functor sending
> `T` to the set of families `(g_0, …, g_{n + 2})` of morphisms `T ⟶ U_{n + 1}` with
> `d_{j - 1} ∘ g_i = d_i ∘ g_j` for `i < j` is representable: it is represented by an object `Y`
> together with a universal such family `f`. Then `U` extends to an `(n + 2)`-truncated simplicial
> object `Ũ` whose `(n + 1)`-skeleton is identified with `U` by an isomorphism `α` and whose degree
> `n + 2` part is identified with `Y` compatibly with the faces, such that `(Ũ, α)` is a right Kan
> extension of `U` along the inclusion of truncated simplex categories; the latter is the adjointness
> `Mor(V, Ũ) = Mor(sk_{n + 1} V, U)`, natural in `V` and given by restricting along the skeleton.

```lean
public theorem exists_isRightKanExtension_of_matchingFamily {n : ℕ}
    (U : SimplicialObject.Truncated C (n + 1)) (Y : C)
    (f : Fin (n + 3) → (Y ⟶ U _⦋n + 1⦌ₙ₊₁))
    (hf : ∀ i j : Fin (n + 2), i ≤ j →
      f i.castSucc ≫ U.map (SimplexCategory.Truncated.δ (n + 1) j (by trunc) (by trunc)).op =
        f j.succ ≫ U.map (SimplexCategory.Truncated.δ (n + 1) i (by trunc) (by trunc)).op)
    (huniv : ∀ (T : C) (g : Fin (n + 3) → (T ⟶ U _⦋n + 1⦌ₙ₊₁)),
      (∀ i j : Fin (n + 2), i ≤ j →
        g i.castSucc ≫ U.map (SimplexCategory.Truncated.δ (n + 1) j (by trunc) (by trunc)).op =
          g j.succ ≫ U.map (SimplexCategory.Truncated.δ (n + 1) i (by trunc) (by trunc)).op) →
      ∃! h : T ⟶ Y, ∀ i, h ≫ f i = g i) :
    ∃ (Ũ : SimplicialObject.Truncated C (n + 2))
      (α : (SimplicialObject.Truncated.trunc C (n + 2) (n + 1)).obj Ũ ⟶ U),
      IsIso α ∧ Ũ.IsRightKanExtension α ∧
        ∃ e : Ũ _⦋n + 2⦌ₙ₊₂ ≅ Y, ∀ i : Fin (n + 3),
          e.hom ≫ f i =
            Ũ.map (SimplexCategory.Truncated.δ (n + 2) i (by trunc) (by trunc)).op ≫
              α.app (op ⦋n + 1⦌ₙ₊₁)
```

## Tag 0188, a remark

[Tag 0188](https://stacks.math.columbia.edu/tag/0188) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.eq_σ_comp_iff_of_matchingFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean#L252). The attribute's comment: “the description of the faces is the identification `he` of Lemma 0187; the description of the degeneracies is stated as a characterisation of them by their components, which the representability of the functor of matching families makes possible”.

> Let `U` be an `(n + 1)`-truncated simplicial object of `C` whose functor of matching families in
> degree `n + 2` is represented by `Y` with universal matching family `f` ([Stacks, Tag 0187]), let
> `Ũ` be an `(n + 2)`-truncated object with a comparison morphism `α : sk_{n + 1} Ũ ⟶ U` and an
> identification `e : Ũ_{n + 2} ≅ Y` under which the faces `d_i : Ũ_{n + 2} ⟶ Ũ_{n + 1}` become the
> projections `f_i`. Then a family `s` of morphisms `Ũ_{n + 1} ⟶ Y` records the degeneracies
> `s_j : Ũ_{n + 1} ⟶ Ũ_{n + 2}` of `Ũ` if and only if, componentwise, `s_j` sends `g` to
> `(s_{j - 1} d_0 g, …, s_{j - 1} d_{j - 1} g, g, g, s_j d_{j + 1} g, …, s_j d_{n + 1} g)`.

```lean
public theorem eq_σ_comp_iff_of_matchingFamily {n : ℕ}
    {U : SimplicialObject.Truncated C (n + 1)} {Ũ : SimplicialObject.Truncated C (n + 2)}
    (α : (SimplicialObject.Truncated.trunc C (n + 2) (n + 1)).obj Ũ ⟶ U) {Y : C}
    (f : Fin (n + 3) → (Y ⟶ U _⦋n + 1⦌ₙ₊₁))
    (hf : ∀ i j : Fin (n + 2), i ≤ j →
      f i.castSucc ≫ U.map (SimplexCategory.Truncated.δ (n + 1) j (by trunc) (by trunc)).op =
        f j.succ ≫ U.map (SimplexCategory.Truncated.δ (n + 1) i (by trunc) (by trunc)).op)
    (huniv : ∀ (T : C) (g : Fin (n + 3) → (T ⟶ U _⦋n + 1⦌ₙ₊₁)),
      (∀ i j : Fin (n + 2), i ≤ j →
        g i.castSucc ≫ U.map (SimplexCategory.Truncated.δ (n + 1) j (by trunc) (by trunc)).op =
          g j.succ ≫ U.map (SimplexCategory.Truncated.δ (n + 1) i (by trunc) (by trunc)).op) →
      ∃! h : T ⟶ Y, ∀ i, h ≫ f i = g i)
    (e : Ũ _⦋n + 2⦌ₙ₊₂ ≅ Y)
    (he : ∀ i : Fin (n + 3), e.hom ≫ f i =
      Ũ.map (SimplexCategory.Truncated.δ (n + 2) i (by trunc) (by trunc)).op ≫
        α.app (op ⦋n + 1⦌ₙ₊₁))
    (s : Fin (n + 2) → (Ũ _⦋n + 1⦌ₙ₊₂ ⟶ Y)) :
    (∀ j : Fin (n + 2),
        Ũ.map (SimplexCategory.Truncated.σ (n + 2) j (by trunc) (by trunc)).op = s j ≫ e.inv) ↔
      (∀ j : Fin (n + 2), s j ≫ f j.castSucc = α.app (op ⦋n + 1⦌ₙ₊₁)) ∧
      (∀ j : Fin (n + 2), s j ≫ f j.succ = α.app (op ⦋n + 1⦌ₙ₊₁)) ∧
      (∀ (i : Fin (n + 2)) (j : Fin (n + 1)), i ≤ j.castSucc →
        s j.succ ≫ f i.castSucc = α.app (op ⦋n + 1⦌ₙ₊₁) ≫
          U.map (SimplexCategory.Truncated.δ (n + 1) i (by trunc) (by trunc)).op ≫
            U.map (SimplexCategory.Truncated.σ (n + 1) j (by trunc) (by trunc)).op) ∧
      (∀ (i : Fin (n + 2)) (j : Fin (n + 1)), j.castSucc < i →
        s j.castSucc ≫ f i.succ = α.app (op ⦋n + 1⦌ₙ₊₁) ≫
          U.map (SimplexCategory.Truncated.δ (n + 1) i (by trunc) (by trunc)).op ≫
            U.map (SimplexCategory.Truncated.σ (n + 1) j (by trunc) (by trunc)).op)
```

## Tag 018A, a remark

[Tag 018A](https://stacks.math.columbia.edu/tag/018A) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.hasPointwiseRightKanExtension_of_incl_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean#L488). The attribute's comment: “the source's three displayed assertions, with each `Mor` formula stated as the universal property of the right Kan extension it is; the hypothesis is the one-degree step of Lemma 0187 rather than finite limits in the ambient category”.

> Let `C` be a category, let `m : ℕ` and let `F` be an `m`-truncated simplicial object of `C`.
> Assume that every `k`-truncated simplicial object of `C`, for `k ≥ m`, can be extended by one
> degree, i.e. admits a pointwise right Kan extension along the inclusion `(Δ_{≤k} ⊆ Δ_{≤k+1})ᵒᵖ` —
> the one-degree step of [Stacks, Tag 0187]. Then:
>
> * for every `n ≥ m` the `n`-truncated object `U^n` extending `F` exists, as a pointwise right Kan
>   extension of `F` along `(Δ_{≤m} ⊆ Δ_{≤n})ᵒᵖ`; its universal property is the source's
>   `Mor_{Simp_n(C)}(V, U^n) = Mor_{Simp_m(C)}(sk_m V, F)`;
> * the coskeleton `cosk_m F` exists, as a pointwise right Kan extension of `F` along
>   `(Δ_{≤m} ⊆ Δ)ᵒᵖ`; its universal property is the source's
>   `Mor_{Simp(C)}(V, cosk_m F) = Mor_{Simp_m(C)}(sk_m V, F)`;
> * the tower is compatible: the `n`-truncation of any right Kan extension `X` of `F` along
>   `(Δ_{≤m} ⊆ Δ)ᵒᵖ` is again a right Kan extension of `F` along `(Δ_{≤m} ⊆ Δ_{≤n})ᵒᵖ`, which is the
>   source's `(cosk_m F)_n = U^n_n`.

```lean
public theorem hasPointwiseRightKanExtension_of_incl_succ {m : ℕ}
    (H : ∀ (k : ℕ), m ≤ k → ∀ G : SimplicialObject.Truncated C k,
      (SimplexCategory.Truncated.incl k (k + 1)).op.HasPointwiseRightKanExtension G)
    (F : SimplicialObject.Truncated C m) :
    (∀ (n : ℕ) (h : m ≤ n),
        (SimplexCategory.Truncated.incl m n h).op.HasPointwiseRightKanExtension F) ∧
      (SimplexCategory.Truncated.inclusion m).op.HasPointwiseRightKanExtension F ∧
      ∀ (n : ℕ) (h : m ≤ n) (X : SimplicialObject C) (β : (truncation m).obj X ⟶ F),
        X.IsRightKanExtension β →
          ((truncation n).obj X).IsRightKanExtension
            (((truncationCompTrunc (C := C) h).app X).hom ≫ β)
```

## Tag 018B, a lemma

[Tag 018B](https://stacks.math.columbia.edu/tag/018B) in the Stacks Project.

**`CategoryTheory.SimplicialObject.nonempty_truncCoskAdj_and_isIso_coskAdj_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 727](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L727). The attribute's comment: “parts (2), (3) and (4); part (1) is the hypothesis that the coskeleta exist, i.e. Tag 0183 for a category with finite limits”. References: SGA 4 V (7.1.2), “1) cosk composition”.

> **Stacks 018B** (parts 2, 3 and 4).
> Coskeleta of different levels. Let `C` be a category, let `n ≤ m` and assume the `n`-th and `m`-th
> coskeleton functors of `C` exist. Then:
>
> * (2) the further truncation `sk_n : Simp_m(C) ⥤ Simp_n(C)` has a right adjoint, namely
>   `sk_m cosk_n`;
> * (3) for every `n`-truncated simplicial object `U` of `C` the canonical map
>   `cosk_n U ⟶ cosk_m sk_m cosk_n U` is an isomorphism, i.e. `cosk_m sk_m cosk_n U = cosk_n U`;
> * (4) if the canonical map `X ⟶ cosk_n sk_n X` is an isomorphism for a simplicial object `X` of
>   `C`, then so is the canonical map `X ⟶ cosk_m sk_m X`.

```lean
public theorem nonempty_truncCoskAdj_and_isIso_coskAdj_unit_app {n m : ℕ} (h : n ≤ m)
    [∀ F : (SimplexCategory.Truncated n)ᵒᵖ ⥤ C,
      (SimplexCategory.Truncated.inclusion n).op.HasPointwiseRightKanExtension F]
    [∀ F : (SimplexCategory.Truncated m)ᵒᵖ ⥤ C,
      (SimplexCategory.Truncated.inclusion m).op.HasPointwiseRightKanExtension F] :
    Nonempty (Truncated.trunc C m n h ⊣ Truncated.cosk n ⋙ truncation m) ∧
      (∀ U : SimplicialObject.Truncated C n,
        IsIso ((coskAdj m).unit.app ((Truncated.cosk n).obj U))) ∧
      (∀ X : SimplicialObject C,
        IsIso ((coskAdj n).unit.app X) → IsIso ((coskAdj m).unit.app X))
```

## Tag 09VS, a remark

[Tag 09VS](https://stacks.math.columbia.edu/tag/09VS) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.hasPointwiseRightKanExtension_of_hasBinaryProducts_or_hasFiniteConnectedLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean, line 769](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal/Existence.lean#L769). The attribute's comment: “the two items of the remark, as the two conjuncts; "cosk\_k exists" is spelled as the existence of the pointwise right Kan extensions along `(Δ_{≤k} ⊆ Δ)ᵒᵖ` that define `Truncated.cosk k`, and each hypothesis is an antecedent of its own item so that item (1) stays a claim about categories with products of pairs alone”. References: SGA 4 Vbis (3.0.1), “more general”.

> Let `C` be a category.
>
> * If `C` has products of pairs of objects, then every `0`-truncated simplicial object `F` of `C`
>   admits a pointwise right Kan extension along `(Δ_{≤0} ⊆ Δ)ᵒᵖ`; equivalently `cosk_0` exists, as
>   the right adjoint `Truncated.cosk 0` of `sk_0` ([Stacks, Example 0182]).
> * If `C` has finite connected limits, then for every `k ≥ 1` every `k`-truncated simplicial object
>   `F` of `C` admits a pointwise right Kan extension along `(Δ_{≤k} ⊆ Δ)ᵒᵖ`; equivalently `cosk_k`
>   exists.

```lean
public theorem hasPointwiseRightKanExtension_of_hasBinaryProducts_or_hasFiniteConnectedLimits :
    (HasBinaryProducts C → ∀ F : SimplicialObject.Truncated C 0,
        (SimplexCategory.Truncated.inclusion 0).op.HasPointwiseRightKanExtension F) ∧
      ((∀ (J : Type) [SmallCategory J] [FinCategory J] [IsConnected J], HasLimitsOfShape J C) →
        ∀ (k : ℕ), 0 < k → ∀ F : SimplicialObject.Truncated C k,
          (SimplexCategory.Truncated.inclusion k).op.HasPointwiseRightKanExtension F)
```

## Tag 018C, a lemma

[Tag 018C](https://stacks.math.columbia.edu/tag/018C) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.rightKanExtensionProdIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 1165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L1165). The attribute's comment: “the coskeleton of a single truncated simplicial object is its right Kan extension along the inclusion of truncated simplex categories; the equality is the canonical isomorphism, whose underlying morphism is the comparison morphism”.

> **Stacks 018C**.
> For `n`-truncated simplicial objects `U`, `V` of `C`, the canonical isomorphism
> `cosk_n (U ⨯ V) ≅ cosk_n U ⨯ cosk_n V`, whenever the coskeleta `cosk_n U`, `cosk_n V`,
> `cosk_n (U ⨯ V)` (right Kan extensions along `(Δ_{≤ n})ᵒᵖ ⥤ Δᵒᵖ`) and the products `U ⨯ V`,
> `cosk_n U ⨯ cosk_n V` exist. Its underlying morphism is the canonical comparison morphism
> (`rightKanExtensionProdIso_hom`).

```lean
noncomputable def rightKanExtensionProdIso :
    (SimplexCategory.Truncated.inclusion n).op.rightKanExtension (U ⨯ V) ≅
      (SimplexCategory.Truncated.inclusion n).op.rightKanExtension U ⨯
        (SimplexCategory.Truncated.inclusion n).op.rightKanExtension V
```

## Tag 018D, a lemma

[Tag 018D](https://stacks.math.columbia.edu/tag/018D) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.isIso_pullback_lift_coskMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 807](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L807). The attribute's comment: “the equality is the statement that the canonical comparison morphism is an isomorphism; the coskeleta are the right Kan extensions along `(Δ_{≤ n} ⊆ Δ)ᵒᵖ`, assumed to exist for `U`, `V`, `W` and `U ×_V W` only”.

> **Stacks 018D**.
> Let `C` be a category with fibre products, and let `f : U ⟶ V`, `g : W ⟶ V` be morphisms of
> `n`-truncated simplicial objects of `C`. Whenever the coskeleta `cosk_n U`, `cosk_n V`,
> `cosk_n W` and `cosk_n (U ×_V W)` exist (as right Kan extensions along `(Δ_{≤ n} ⊆ Δ)ᵒᵖ`, not
> assuming that the coskeleton functor exists), the canonical comparison morphism
> `cosk_n (U ×_V W) ⟶ cosk_n U ×_{cosk_n V} cosk_n W`, with components `cosk_n` of the two
> projections, is an isomorphism. The fibre product on the right exists since `C` has fibre
> products.

```lean
public theorem isIso_pullback_lift_coskMap [HasPullbacks C] {n : ℕ}
    {U V W : SimplicialObject.Truncated C n} (f : U ⟶ V) (g : W ⟶ V)
    [(SimplexCategory.Truncated.inclusion n).op.HasRightKanExtension U]
    [(SimplexCategory.Truncated.inclusion n).op.HasRightKanExtension V]
    [(SimplexCategory.Truncated.inclusion n).op.HasRightKanExtension W]
    [(SimplexCategory.Truncated.inclusion n).op.HasRightKanExtension (pullback f g)] :
    IsIso (pullback.lift (coskMap (pullback.fst f g)) (coskMap (pullback.snd f g))
      (by rw [← coskMap_comp, ← coskMap_comp, pullback.condition]) :
      (SimplexCategory.Truncated.inclusion n).op.rightKanExtension (pullback f g) ⟶
        pullback (coskMap f) (coskMap g))
```

## Tag 08NJ, a lemma

[Tag 08NJ](https://stacks.math.columbia.edu/tag/08NJ) in the Stacks Project.

**`CategoryTheory.Over.preservesPointwiseRightKanExtensions_forget_inclusion_succ_op`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean, line 877](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Coskeletal.lean#L877). The attribute's comment: “stated as preservation of the pointwise right Kan extensions along `(Δ_{≤m} ⊆ Δ)ᵒᵖ`, which is what "cosk\_m computed in C/X is computed in C" says with the comparison map pinned; the source's finite limits in `C` are not needed”.

> **Stacks 08NJ**.
> For a category `C` and an object `X : C`, the forgetful functor `Over.forget X : C/X ⥤ C` commutes
> with the coskeleton functors `cosk_m` for `m ≥ 1`: it carries a pointwise right Kan extension along
> `(Δ_{≤m} ⊆ Δ)ᵒᵖ` of an `m`-truncated simplicial object of `C/X`, with its structure map, to one of
> the underlying `m`-truncated simplicial object of `C`. Hence `cosk_m U` computed in `C/X` is
> computed in `C`, the comparison being the whiskering of the structure map.

```lean
public instance preservesPointwiseRightKanExtensions_forget_inclusion_succ_op (X : C) (k : ℕ) :
    (Over.forget X).PreservesPointwiseRightKanExtensions
      (SimplexCategory.Truncated.inclusion (k + 1)).op
```

## Tag 018E, a lemma

[Tag 018E](https://stacks.math.columbia.edu/tag/018E) in the Stacks Project.

**`SSet.canonicalMap_stdSimplex_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/Coskeletal.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/Coskeletal.lean#L245).

> **Stacks 018E**.
> For every `n`, the canonical map `c_{Δ[n]} : Δ[n] ⟶ cosk_1 sk_1 Δ[n]`, the unit of the adjunction
> `sk_1 ⊣ cosk_1` at the standard `n`-simplex, is an isomorphism of simplicial sets.

```lean
theorem canonicalMap_stdSimplex_isIso (n : ℕ) :
    IsIso (cosk1Unit (Δ[n]))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.19, Tag 0AMA](https://stacks.math.columbia.edu/tag/0AMA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
