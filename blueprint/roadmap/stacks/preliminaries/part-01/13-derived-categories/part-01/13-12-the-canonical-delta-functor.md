---
declaration: section
origin: cited
lean: DerivedCategory.exists_deltaFunctorStructure_δ_eq, triangleOfSESIsoOfQuasiIsoHom, DerivedCategory.mapTriangle_triangleOfDegreewiseSplit_eq_triangleOfSES, DerivedCategory.exists_truncLESucc_triangle, DerivedCategory.exists_truncGESucc_triangle, CategoryTheory.Triangulated.TStructure.triangleLEGE_distinguished, main_covariant, main_contravariant
statement: formalized
proof: formalized
---

# 13.12 The canonical delta-functor

Section 13.12 of the Stacks Project, [Tag 014Z](https://stacks.math.columbia.edu/tag/014Z). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0152, a lemma

[Tag 0152](https://stacks.math.columbia.edu/tag/0152) in the Stacks Project.

**`DerivedCategory.exists_deltaFunctorStructure_δ_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L162). References: SGA 4½ Etat 0 (3.1.5), “partial”.

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

**`triangleOfSESIsoOfQuasiIsoHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L274).

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

**`DerivedCategory.mapTriangle_triangleOfDegreewiseSplit_eq_triangleOfSES`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L200).

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

**`DerivedCategory.exists_truncLESucc_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/TruncGESuccTriangle.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/TruncGESuccTriangle.lean#L91). The attribute's comment: “(2)”.

> **Stacks Project, Tag 08J5** (second triangle). Two successive truncations from above of an
> object of the derived category differ by its cohomology in the newly retained degree, placed in
> that degree: there is a distinguished triangle
> `τ^{≤a} E ⟶ τ^{≤a+1} E ⟶ H^{a+1}(E)[-a-1] ⟶ (τ^{≤a} E)[1]` whose first map is the canonical
> comparison of truncations.

```lean
public theorem exists_truncLESucc_triangle (E : DerivedCategory C) (a : ℤ) :
    ∃ (g : (TStructure.t.truncLE (a + 1)).obj E ⟶
        (singleFunctor C (a + 1)).obj ((homologyFunctor C (a + 1)).obj E))
      (δ : (singleFunctor C (a + 1)).obj ((homologyFunctor C (a + 1)).obj E) ⟶
        ((TStructure.t.truncLE a).obj E)⟦(1 : ℤ)⟧),
      Triangle.mk ((TStructure.t.natTransTruncLEOfLE a (a + 1) (by omega)).app E) g δ ∈
        distTriang (DerivedCategory C)
```

**`DerivedCategory.exists_truncGESucc_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/TruncGESuccTriangle.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/TruncGESuccTriangle.lean#L160). The attribute's comment: “(3)”.

> **Stacks Project, Tag 08J5** (third triangle).  Two successive truncations from below of an
> object of the derived category differ by its cohomology in the lower degree, placed in that
> degree: there is a distinguished triangle
> `H^a(E)[-a] ⟶ τ^{≥a} E ⟶ τ^{≥a+1} E ⟶ (H^a(E)[-a])[1]` whose second map is the canonical
> comparison of truncations.

```lean
public theorem exists_truncGESucc_triangle (E : DerivedCategory C) (a : ℤ) :
    ∃ (f : (singleFunctor C a).obj ((homologyFunctor C a).obj E) ⟶
        (TStructure.t.truncGE a).obj E)
      (δ : (TStructure.t.truncGE (a + 1)).obj E ⟶
        ((singleFunctor C a).obj ((homologyFunctor C a).obj E))⟦(1 : ℤ)⟧),
      Triangle.mk f ((TStructure.t.natTransTruncGEOfLE a (a + 1) (by omega)).app E) δ ∈
        distTriang (DerivedCategory C)
```

Declarations registered for the tag:

- [`CategoryTheory.Triangulated.TStructure.triangleLEGE_distinguished`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Triangulated.TStructure.triangleLEGE_distinguished#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Homology/DerivedCategory/TruncGESuccTriangle.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/TruncGESuccTriangle.lean#L73) (StacksFrontier): “(1)”.

## Tag 08Q2, a lemma

[Tag 08Q2](https://stacks.math.columbia.edu/tag/08Q2) in the Stacks Project.

**`main_covariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L710). The attribute's comment: “(1)”.

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

**`main_contravariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/CanonicalDeltaFunctor.lean#L742). The attribute's comment: “(2)”. References: SGA 4 XVIII (2.14.2), “partial”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
