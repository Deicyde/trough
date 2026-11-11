---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_distTriang_blowUp, AlgebraicGeometry.exists_longExactSequence_blowUp, AlgebraicGeometry.exists_gluing_blowUp
statement: formalized
proof: formalized
---

# 59.105 Blow up squares and étale cohomology

Section 59.105 of the Stacks Project, [Tag 0EW4](https://stacks.math.columbia.edu/tag/0EW4). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EW5, a lemma

[Tag 0EW5](https://stacks.math.columbia.edu/tag/0EW5) in the Stacks Project.

**`AlgebraicGeometry.exists_distTriang_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/BlowUpTriangle.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/BlowUpTriangle.lean#L77).

> **Stacks Project, Tag 0EW5.** Let `X` be a scheme and `Z ⊆ X` the closed subscheme cut out by
> a quasi-coherent ideal `I` of finite type (finitely generated on every affine open), with blowup
> square
> ```
> E --j--> X'
> |π       |b
> v        v
> Z --i--> X
> ```
> (`X'` the blowup of `X` in `I`, `E = b⁻¹(Z)` the exceptional divisor) and `c = i ∘ π = b ∘ j`.
> For every `K` in `D⁺(X_étale)` (a complex of abelian sheaves on the small étale site, bounded
> below: `K.IsGE n`) with torsion cohomology sheaves there is a distinguished triangle
> `K ⟶ Ri_*(K|_Z) ⊕ Rb_*(K|_{X'}) ⟶ Rc_*(K|_E) ⟶ K[1]`
> in `D(X_étale)`, where `K|_Y` is the derived inverse image. Its first map is formed by the two
> adjunction units and its second map is the difference of the two comparison maps
> `Ri_*(K|_Z) ⟶ Rc_*(K|_E)` (along `c = i ∘ π`) and `Rb_*(K|_{X'}) ⟶ Rc_*(K|_E)` (along
> `c = b ∘ j`).

```lean
public theorem exists_distTriang_blowUp {X : Scheme.{u}} (I : X.IdealSheafData)
    (hI : ∀ U : X.affineOpens, (I.ideal U).FG)
    (K : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})) (n : ℤ)
    (hK : K.IsGE n)
    (hT : Stacks.Torsion.torsionCohomologyProperty.{u + 1} X.smallEtaleTopology K) :
    ∃ δ : (etaleAbelianDerivedDirectImage.{u, 0}
          ((exceptionalIdeal I).subschemeι ≫ blowUpToBase I)).obj
        ((etaleAbelianDerivedInverseImage.{u, 0}
          ((exceptionalIdeal I).subschemeι ≫ blowUpToBase I)).obj K) ⟶ K⟦(1 : ℤ)⟧,
      Triangle.mk (etaleAbelianDerivedSquareUnits.{u, 0} I.subschemeι (blowUpToBase I) K)
        (etaleAbelianDerivedSquareDifference.{u, 0} I.subschemeι (blowUpToBase I)
          (exceptionalIdeal I).subschemeι (exceptionalDivisorToCenter I)
          ((exceptionalIdeal I).subschemeι ≫ blowUpToBase I)
          (isPullback_exceptionalDivisor I).w rfl K) δ ∈
        distTriang (DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1}))
```

## Tag 0EW3, a lemma

[Tag 0EW3](https://stacks.math.columbia.edu/tag/0EW3) in the Stacks Project.

**`AlgebraicGeometry.exists_longExactSequence_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/BlowUpLongExactSequence.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/BlowUpLongExactSequence.lean#L72).

> **Stacks Project, Tag 0EW3.** Let `X` be a scheme, `K` an object of `D⁺(X_étale)` (a complex
> of abelian sheaves on the small étale site, bounded below: `K.IsGE n`) with torsion cohomology
> sheaves, and `Z ⊆ X` the closed subscheme cut out by a quasi-coherent ideal `I` of finite type
> (finitely generated on every affine open). In the blowup square
> ```
> E --j--> X'
> |π       |b
> v        v
> Z --i--> X
> ```
> (`X'` the blowup of `X` in `I`, `E = b⁻¹(Z)` the exceptional divisor) there is a long exact
> sequence
> `H^p(X, K) ⟶ H^p(X', K|_{X'}) × H^p(Z, K|_Z) ⟶ H^p(E, K|_E) ⟶ H^{p+1}(X, K) ⟶ ⋯`
> whose first map is `x ↦ (x|_{X'}, x|_Z)`, whose second map is `(x', z) ↦ x'|_E - z|_E` (the two
> restrictions read in `H^p(E, K|_E)`, `K|_E = (j ≫ b)⁻¹ K`, through
> `j⁻¹ b⁻¹ K ≅ K|_E ≅ π⁻¹ i⁻¹ K`), and whose third map is a connecting map `δ`, exact at all three
> places for every `p`. Here `H^p(Y, M) = Hom(ℤ_Y[-p], M)` in `D(Y_étale)`
> (`Stacks.EtaleCohomology.etaleDerivedCohomology`) and `K|_Y` is the derived inverse image.

```lean
public theorem exists_longExactSequence_blowUp {X : Scheme.{u}} (I : X.IdealSheafData)
    (hI : ∀ U : X.affineOpens, (I.ideal U).FG)
    (K : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})) (n : ℤ)
    (hK : K.IsGE n)
    (hT : Stacks.Torsion.torsionCohomologyProperty.{u + 1} X.smallEtaleTopology K) :
    ∃ δ : ∀ p : ℤ, etaleDerivedCohomology.{u, 0} (exceptionalDivisor I) p
        ((etaleAbelianDerivedInverseImage.{u, 0}
          ((exceptionalIdeal I).subschemeι ≫ blowUpToBase I)).obj K) →+
      etaleDerivedCohomology.{u, 0} X (p + 1) K,
    ∀ p : ℤ,
      Function.Exact
        (fun x : etaleDerivedCohomology.{u, 0} X p K ↦
          (etaleDerivedCohomologyRestriction.{u, 0} (blowUpToBase I) p K x,
            etaleDerivedCohomologyRestriction.{u, 0} I.subschemeι p K x))
        (fun y : etaleDerivedCohomology.{u, 0} (blowUp I) p
              ((etaleAbelianDerivedInverseImage.{u, 0} (blowUpToBase I)).obj K) ×
            etaleDerivedCohomology.{u, 0} I.subscheme p
              ((etaleAbelianDerivedInverseImage.{u, 0} I.subschemeι).obj K) ↦
          etaleDerivedCohomologyRestriction.{u, 0} (exceptionalIdeal I).subschemeι p _ y.1 ≫
              (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalIdeal I).subschemeι
                (blowUpToBase I) _ rfl).inv.app K -
            etaleDerivedCohomologyRestriction.{u, 0} (exceptionalDivisorToCenter I) p _ y.2 ≫
              (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalDivisorToCenter I)
                I.subschemeι _ (isPullback_exceptionalDivisor I).w).inv.app K) ∧
      Function.Exact
        (fun y : etaleDerivedCohomology.{u, 0} (blowUp I) p
              ((etaleAbelianDerivedInverseImage.{u, 0} (blowUpToBase I)).obj K) ×
            etaleDerivedCohomology.{u, 0} I.subscheme p
              ((etaleAbelianDerivedInverseImage.{u, 0} I.subschemeι).obj K) ↦
          etaleDerivedCohomologyRestriction.{u, 0} (exceptionalIdeal I).subschemeι p _ y.1 ≫
              (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalIdeal I).subschemeι
                (blowUpToBase I) _ rfl).inv.app K -
            etaleDerivedCohomologyRestriction.{u, 0} (exceptionalDivisorToCenter I) p _ y.2 ≫
              (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalDivisorToCenter I)
                I.subschemeι _ (isPullback_exceptionalDivisor I).w).inv.app K)
        (δ p) ∧
      Function.Exact (δ p)
        (fun x : etaleDerivedCohomology.{u, 0} X (p + 1) K ↦
          (etaleDerivedCohomologyRestriction.{u, 0} (blowUpToBase I) (p + 1) K x,
            etaleDerivedCohomologyRestriction.{u, 0} I.subschemeι (p + 1) K x))
```

## Tag 0EW6, a lemma

[Tag 0EW6](https://stacks.math.columbia.edu/tag/0EW6) in the Stacks Project.

**`AlgebraicGeometry.exists_gluing_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/BlowUpGluing.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/BlowUpGluing.lean#L92).

> **Stacks Project, Tag 0EW6.** Let `X` be a scheme and `Z ⊆ X` the closed subscheme cut out by
> a quasi-coherent ideal `I` of finite type (finitely generated on every affine open), with blowup
> square
> ```
> E --j--> X'
> |π       |b
> v        v
> Z --i--> X
> ```
> (`X'` the blowup of `X` in `I`, `E = b⁻¹(Z)` the exceptional divisor, `c = i ∘ π = b ∘ j`).
> Let `K'` be an object of `D⁺(X'_étale)` (bounded below: `K'.IsGE n₁`) with torsion cohomology
> sheaves, `L` an object of `D⁺(Z_étale)` (`L.IsGE n₂`), and `γ : K'|_E ≅ L|_E` an isomorphism,
> where `N|_Y` is the derived inverse image. Then there are an object `K` of `D⁺(X_étale)` and
> isomorphisms `f : K|_{X'} ≅ K'`, `g : K|_Z ≅ L` such that `γ = g|_E ∘ f⁻¹|_E` (both sides read
> through the canonical identifications `(K|_{X'})|_E ≅ K|_E ≅ (K|_Z)|_E`). Moreover, given an
> object `M` of `D⁺(X_étale)` with torsion cohomology sheaves and morphisms `α : K' ⟶ M|_{X'}`,
> `β : L ⟶ M|_Z` with `α|_E = β|_E ∘ γ` (read through `(M|_{X'})|_E ≅ M|_E ≅ (M|_Z)|_E`), there is a
> morphism `K ⟶ M` in `D(X_étale)` whose restriction to `X'` is `α ∘ f` and whose restriction to
> `Z` is `β ∘ g`.
>
> The source writes the last morphism as `M ⟶ K` with restrictions `a ∘ f`, `b ∘ g`; these are
> typos for `α ∘ f : K|_{X'} ⟶ M|_{X'}` and `β ∘ g : K|_Z ⟶ M|_Z`, which forces the direction
> `K ⟶ M`, the direction of the morphism of triangles in the source's proof. The source's
> hypothesis that `L` has torsion cohomology sheaves is not needed and is omitted.

```lean
public theorem exists_gluing_blowUp {X : Scheme.{u}} (I : X.IdealSheafData)
    (hI : ∀ U : X.affineOpens, (I.ideal U).FG)
    (K' : DerivedCategory (Sheaf (blowUp I).smallEtaleTopology AddCommGrpCat.{u + 1})) (n₁ : ℤ)
    (hK' : K'.IsGE n₁)
    (hK'T : Stacks.Torsion.torsionCohomologyProperty.{u + 1} (blowUp I).smallEtaleTopology K')
    (L : DerivedCategory (Sheaf I.subscheme.smallEtaleTopology AddCommGrpCat.{u + 1})) (n₂ : ℤ)
    (hL : L.IsGE n₂)
    (γ : (etaleAbelianDerivedInverseImage.{u, 0} (exceptionalIdeal I).subschemeι).obj K' ≅
      (etaleAbelianDerivedInverseImage.{u, 0} (exceptionalDivisorToCenter I)).obj L) :
    ∃ (K : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1}))
      (_ : K.IsGE (min n₁ n₂))
      (f : (etaleAbelianDerivedInverseImage.{u, 0} (blowUpToBase I)).obj K ≅ K')
      (g : (etaleAbelianDerivedInverseImage.{u, 0} I.subschemeι).obj K ≅ L),
      γ.hom = (etaleAbelianDerivedInverseImage.{u, 0} (exceptionalIdeal I).subschemeι).map f.inv ≫
          (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalIdeal I).subschemeι
            (blowUpToBase I) _ rfl).inv.app K ≫
          (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalDivisorToCenter I)
            I.subschemeι _ (isPullback_exceptionalDivisor I).w).hom.app K ≫
          (etaleAbelianDerivedInverseImage.{u, 0} (exceptionalDivisorToCenter I)).map g.hom ∧
      ∀ (M : DerivedCategory (Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})) (m : ℤ),
        M.IsGE m →
        Stacks.Torsion.torsionCohomologyProperty.{u + 1} X.smallEtaleTopology M →
        ∀ (α : K' ⟶ (etaleAbelianDerivedInverseImage.{u, 0} (blowUpToBase I)).obj M)
          (β : L ⟶ (etaleAbelianDerivedInverseImage.{u, 0} I.subschemeι).obj M),
          (etaleAbelianDerivedInverseImage.{u, 0} (exceptionalIdeal I).subschemeι).map α ≫
              (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalIdeal I).subschemeι
                (blowUpToBase I) _ rfl).inv.app M ≫
              (etaleAbelianDerivedInverseImageCompIso'.{u, 0} (exceptionalDivisorToCenter I)
                I.subschemeι _ (isPullback_exceptionalDivisor I).w).hom.app M =
            γ.hom ≫ (etaleAbelianDerivedInverseImage.{u, 0} (exceptionalDivisorToCenter I)).map β →
          ∃ φ : K ⟶ M, (etaleAbelianDerivedInverseImage.{u, 0} (blowUpToBase I)).map φ = f.hom ≫ α ∧
            (etaleAbelianDerivedInverseImage.{u, 0} I.subschemeι).map φ = g.hom ≫ β
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.105, Tag 0EW4](https://stacks.math.columbia.edu/tag/0EW4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
