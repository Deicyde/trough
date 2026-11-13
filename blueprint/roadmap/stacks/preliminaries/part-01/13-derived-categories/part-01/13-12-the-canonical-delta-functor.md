---
declaration: section
origin: cited
lean: DerivedCategory.exists_deltaFunctorStructure_δ_eq_and_plus_minus_bounded, DerivedCategory.exists_deltaFunctorStructure_δ_eq, triangleOfSESIsoOfQuasiIsoHom, DerivedCategory.mapTriangle_triangleOfDegreewiseSplit_eq_triangleOfSES, DerivedCategory.triangleTruncLETruncGE_distinguished, DerivedCategory.triangleTruncLETruncLESucc_distinguished, DerivedCategory.triangleTruncGETruncGESucc_distinguished, main_covariant
statement: formalized
proof: formalized
---

# 13.12 The canonical delta-functor

Section 13.12 of the Stacks Project, [Tag 014Z](https://stacks.math.columbia.edu/tag/014Z). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0152, a lemma

[Tag 0152](https://stacks.math.columbia.edu/tag/0152) in the Stacks Project.

**`DerivedCategory.exists_deltaFunctorStructure_δ_eq_and_plus_minus_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDeltaFunctor.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/BoundedDeltaFunctor.lean#L248).

> **The canonical `δ`-functors** ([Stacks, Tag 0152]). Let `𝒜` be an abelian category. Each of
> the four functors `Q : Comp(𝒜) ⥤ D(𝒜)`, `Comp⁺(𝒜) ⥤ D⁺(𝒜)`, `Comp⁻(𝒜) ⥤ D⁻(𝒜)` and
> `Compᵇ(𝒜) ⥤ Dᵇ(𝒜)` has a `δ`-functor structure whose connecting morphism attached to a short exact
> sequence `0 → A^• → B^• → C^• → 0` is `δ = -p ∘ q⁻¹ = DerivedCategory.triangleOfSESδ` (for the
> three bounded variants: its image in `D(𝒜)` under the fully faithful inclusion is).

```lean
theorem exists_deltaFunctorStructure_δ_eq_and_plus_minus_bounded :
    (∃ h : Functor.DeltaFunctorStructure (CochainComplex C ℤ) (DerivedCategory C) Q,
      ∀ {S : ShortComplex (CochainComplex C ℤ)} (hS : S.ShortExact),
        h.δ hS = triangleOfSESδ hS) ∧
    (∃ h : Functor.DeltaFunctorStructure (CochainComplex.Plus C) (DerivedCategory.Plus C) Plus.Q,
      ∀ {S : ShortComplex (CochainComplex.Plus C)} (hS : S.ShortExact),
        Plus.ι.map (h.δ hS) ≫ (Plus.ι.commShiftIso (1 : ℤ)).hom.app (Plus.Q.obj S.X₁) =
          triangleOfSESδ (hS.map_of_exact (CochainComplex.Plus.ι C))) ∧
    (∃ h : Functor.DeltaFunctorStructure (CochainComplex.minus C).FullSubcategory
        (DerivedCategory.Minus C) Minus.Q,
      ∀ {S : ShortComplex (CochainComplex.minus C).FullSubcategory} (hS : S.ShortExact),
        Minus.ι.map (h.δ hS) ≫ (Minus.ι.commShiftIso (1 : ℤ)).hom.app (Minus.Q.obj S.X₁) =
          triangleOfSESδ (hS.map_of_exact (CochainComplex.minus C).ι)) ∧
    (∃ h : Functor.DeltaFunctorStructure
        (CochainComplex.plus C ⊓ CochainComplex.minus C).FullSubcategory
        (DerivedCategory.Bounded C) Bounded.Q,
      ∀ {S : ShortComplex (CochainComplex.plus C ⊓ CochainComplex.minus C).FullSubcategory}
        (hS : S.ShortExact),
        Bounded.ι.map (h.δ hS) ≫ (Bounded.ι.commShiftIso (1 : ℤ)).hom.app (Bounded.Q.obj S.X₁) =
          triangleOfSESδ (hS.map_of_exact (CochainComplex.plus C ⊓ CochainComplex.minus C).ι))
```

**`DerivedCategory.exists_deltaFunctorStructure_δ_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L163). The attribute's comment: “the functor Comp(𝒜) ⥤ D(𝒜)”. References: SGA 4½ Etat 0 (3.1.5), “partial”.

> **The canonical `δ`-functor.** Let `𝒜` be an abelian category. The localization functor
> `Q : CochainComplex 𝒜 ℤ ⥤ DerivedCategory 𝒜` has the structure of a `δ`-functor whose connecting
> morphism is `DerivedCategory.triangleOfSESδ = -p ∘ q⁻¹`: for every short exact sequence
> `0 ⟶ A^• ⟶ B^• ⟶ C^• ⟶ 0` of complexes the triangle
> `(Q A^•, Q B^•, Q C^•, Q a, Q b, triangleOfSESδ)` is distinguished, and `triangleOfSESδ` is
> natural in the short exact sequence.

```lean
public theorem exists_deltaFunctorStructure_δ_eq
    (C : Type u) [Category.{v} C] [Abelian C] [HasDerivedCategory.{w} C] :
    ∃ h : Functor.DeltaFunctorStructure (CochainComplex C ℤ) (DerivedCategory C) Q,
      ∀ {S : ShortComplex (CochainComplex C ℤ)} (hS : S.ShortExact),
        h.δ hS = triangleOfSESδ hS
```

## Tag 0153, a lemma

[Tag 0153](https://stacks.math.columbia.edu/tag/0153) in the Stacks Project.

**`triangleOfSESIsoOfQuasiIsoHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L275).

> The two distinguished triangles associated to `S₁` and `S₂` are isomorphic in
> `D(𝒜)`, via the canonical isomorphism with components `Q φ₁, Q φ₂, Q φ₃`.

```lean
noncomputable def triangleOfSESIsoOfQuasiIsoHom
    {S₁ S₂ : ShortComplex (CochainComplex 𝒜 ℤ)}
    (hS₁ : S₁.ShortExact) (hS₂ : S₂.ShortExact) (f : S₁ ⟶ S₂)
    (h₁ : QuasiIso f.τ₁) (h₂ : QuasiIso f.τ₂) (h₃ : QuasiIso f.τ₃) :
    DerivedCategory.triangleOfSES hS₁ ≅ DerivedCategory.triangleOfSES hS₂
```

## Tag 0154, a lemma

[Tag 0154](https://stacks.math.columbia.edu/tag/0154) in the Stacks Project.

**`DerivedCategory.mapTriangle_triangleOfDegreewiseSplit_eq_triangleOfSES`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L201).

> **The `δ`-functor on a termwise split short exact sequence.** Let `𝒜` be an abelian category
> and let `S` be a short exact sequence of cochain complexes in `𝒜` which is split in each degree,
> with splitting `σ`. Then the image under `Q : Comp(𝒜) ⥤ D(𝒜)` of the distinguished triangle
> `(S.X₁, S.X₂, S.X₃, S.f, S.g, CochainComplex.homOfDegreewiseSplit S σ)` attached to the splitting
> is the distinguished triangle that the canonical `δ`-functor attaches to `S`; in particular the
> connecting morphism `triangleOfSESδ hS` is the image of
> `CochainComplex.homOfDegreewiseSplit S σ`.

```lean
public theorem mapTriangle_triangleOfDegreewiseSplit_eq_triangleOfSES
    {C : Type u} [Category.{v} C] [Abelian C] [HasDerivedCategory.{w} C]
    {S : ShortComplex (CochainComplex C ℤ)} (hS : S.ShortExact)
    (σ : ∀ n, (S.map (HomologicalComplex.eval C (ComplexShape.up ℤ) n)).Splitting) :
    Q.mapTriangle.obj (CochainComplex.triangleOfDegreewiseSplit S σ) = triangleOfSES hS
```

## Tag 08J5, a remark

[Tag 08J5](https://stacks.math.columbia.edu/tag/08J5) in the Stacks Project.

**`DerivedCategory.triangleTruncLETruncGE_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/TruncationTriangles.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/TruncationTriangles.lean#L197). The attribute's comment: “(1) the triangle τ\_\{≤a}K → K → τ\_\{≥a+1}K → (τ\_\{≤a}K)[1] on the truncations of the complex K, with connecting map from the short exact sequence 0 → τ\_\{≤a}K → K → K/τ\_\{≤a}K → 0”.

> **Stacks Project, Tag 08J5** (1). For a complex `K` and an integer `a`, the triangle
> `τ_{≤a} K ⟶ K ⟶ τ_{≥a+1} K ⟶ (τ_{≤a} K)[1]` on the canonical truncations of `K`, with the
> canonical maps, is distinguished in `D(C)`.

```lean
theorem triangleTruncLETruncGE_distinguished (K : CochainComplex C ℤ) (a : ℤ) :
    triangleTruncLETruncGE K a ∈ distTriang (DerivedCategory C)
```

**`DerivedCategory.triangleTruncLETruncLESucc_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/TruncationTriangles.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/TruncationTriangles.lean#L265). The attribute's comment: “(2) the triangle τ\_\{≤a}K → τ\_\{≤a+1}K → H^\{a+1}(K)[-a-1] → (τ\_\{≤a}K)[1] on the truncations of the complex K, with the canonical maps”.

> **Stacks Project, Tag 08J5** (2). For a complex `K` and an integer `a`, the triangle
> `τ_{≤a} K ⟶ τ_{≤a+1} K ⟶ H^{a+1}(K)[-a-1] ⟶ (τ_{≤a} K)[1]`, whose first map is the canonical
> inclusion of truncations and whose second map is the canonical projection onto the cohomology in
> degree `a + 1`, is distinguished in `D(C)`.

```lean
theorem triangleTruncLETruncLESucc_distinguished (K : CochainComplex C ℤ) (a : ℤ) :
    triangleTruncLETruncLESucc K a ∈ distTriang (DerivedCategory C)
```

**`DerivedCategory.triangleTruncGETruncGESucc_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/TruncationTriangles.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/TruncationTriangles.lean#L313). The attribute's comment: “(3) the triangle H^a(K)[-a] → τ\_\{≥a}K → τ\_\{≥a+1}K → H^a(K)[-a+1] on the truncations of the complex K, with the canonical maps”.

> **Stacks Project, Tag 08J5** (3). For a complex `K` and an integer `a`, the triangle
> `H^a(K)[-a] ⟶ τ_{≥a} K ⟶ τ_{≥a+1} K ⟶ (H^a(K)[-a])[1]`, whose first map is the canonical
> inclusion of the cohomology in degree `a` and whose second map is the canonical projection of
> truncations, is distinguished in `D(C)`.

```lean
theorem triangleTruncGETruncGESucc_distinguished (K : CochainComplex C ℤ) (a : ℤ) :
    triangleTruncGETruncGESucc K a ∈ distTriang (DerivedCategory C)
```

## Tag 08Q2, a lemma

[Tag 08Q2](https://stacks.math.columbia.edu/tag/08Q2) in the Stacks Project.

**`main_covariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 711](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L711). The attribute's comment: “(1)”.

> Statement 1 (covariant case). If `H^i(K 0) = 0` for `i > 0` and the induced
> map `H^{-j}(f j)` vanishes for each `0 ≤ j ≤ n-1`, then the composite
> `K 0 ⟶ K n`, viewed in the derived category, factors through the canonical map
> `ι : τ_{≤ -n} (K n) ⟶ K n`.
>
> PROOF.  Induction on `n`.
> * `n = 0`: `chainComp K f 0 = 𝟙`, and `covariant_base` makes `Q(ιTruncLE 0)`
>   invertible, so `h = inv (Q(ιTruncLE 0))` works.
> * `n → n+1`: `chainComp K f (m+1) = chainComp K f m ≫ f m`.  The induction
>   hypothesis factors `Q(chainComp K f m)` through `Q(ιTruncLE (-m))`; apply
>   `covariant_step m (K m) (K (m+1)) (f m)` (its `H^{-m}(f m) = 0` hypothesis is
>   `h2 m`), then rewrite `-(↑m+1) = -(↑(m+1))` by `push_cast` to match.

```lean
theorem main_covariant
    (n : ℕ) (K : ℕ → CochainComplex A ℤ) (f : ∀ j, K j ⟶ K (j + 1))
    (h1 : ∀ i : ℤ, 0 < i → Limits.IsZero ((K 0).homology i))
    (h2 : ∀ j : ℕ, j < n → HomologicalComplex.homologyMap (f j) (-(j : ℤ)) = 0) :
    ∃ h : DerivedCategory.Q.obj (K 0) ⟶ DerivedCategory.Q.obj ((K n).truncLE (-(n : ℤ))),
      DerivedCategory.Q.map (chainComp K f n) =
        h ≫ DerivedCategory.Q.map ((K n).ιTruncLE (-(n : ℤ)))
```

**`main_contravariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 743](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L743). The attribute's comment: “(2)”. References: SGA 4 XVIII (2.14.2), “partial”.

> Statement 2 (contravariant / dual case). If `H^i(K 0) = 0` for `i < 0` and
> the induced map `H^{j}(g j)` vanishes for each `0 ≤ j ≤ n-1`, then the composite
> `K n ⟶ K 0`, viewed in the derived category, factors through the canonical map
> `π : K n ⟶ τ_{≥ n} (K n)`.
>
> PROOF.  Dual of `main_covariant`, by induction on `n` using `contravariant_base`
> (base) and `contravariant_step` (step).

```lean
theorem main_contravariant
    (n : ℕ) (K : ℕ → CochainComplex A ℤ) (g : ∀ j, K (j + 1) ⟶ K j)
    (h1 : ∀ i : ℤ, i < 0 → Limits.IsZero ((K 0).homology i))
    (h2 : ∀ j : ℕ, j < n → HomologicalComplex.homologyMap (g j) (j : ℤ) = 0) :
    ∃ h : DerivedCategory.Q.obj ((K n).truncGE (n : ℤ)) ⟶ DerivedCategory.Q.obj (K 0),
      DerivedCategory.Q.map (chainCompOp K g n) =
        DerivedCategory.Q.map ((K n).πTruncGE (n : ℤ)) ≫ h
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.12, Tag 014Z](https://stacks.math.columbia.edu/tag/014Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
