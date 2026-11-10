---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.WeilData.globalSections_criterion, Stacks.WeilCohomology.WeilData.exists_not_globalSections_criterion, Stacks.WeilCohomology.WeilCohomologyTheory, Stacks.WeilCohomology.WeilCohomologyTheory.factorwise_rank_one_of_geometricallyIrreducible, Stacks.WeilCohomology.WeilRealization.exists_globalSections_isoClassEquiv
statement: formalized
proof: formalized
---

# 45.11 Weil cohomology theories, II

Section 45.11 of the Stacks Project, [Tag 0FHY](https://stacks.math.columbia.edu/tag/0FHY). 5 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FI0, a lemma

[Tag 0FI0](https://stacks.math.columbia.edu/tag/0FI0) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.globalSections_criterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GlobalSectionsCriterion.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GlobalSectionsCriterion.lean#L418). The attribute's comment: “(1) ⇔ (2), the finite separability of H^0(X), and (1) ⇔ (3) for X equidimensional of dimension d, on the actual Weil data (D0)-(D3) satisfying (A), (B), (C) over the actual category of smooth projective k-schemes”.

> **Stacks Project, Tag 0FI0.** Assume given (D0), (D1), (D2) and (D3) satisfying (A), (B) and
> (C). Let `X` be a smooth projective scheme over `k` and `k' = Γ(X, 𝒪_X)`. Then the following are
> equivalent:
>
> 1. there exist finitely many closed points `x₁, …, x_r ∈ X` whose residue fields are separable
>    over `k` such that `H^0(X) → H^0(x₁) ⊕ … ⊕ H^0(x_r)` is injective
>    (`SeparablePointsDetectH0`),
> 2. the map `H^0(Spec(k')) → H^0(X)` is an isomorphism.
>
> If this is true, then `H^0(X)` is a finite separable algebra over `F`. If `X` is equidimensional
> of dimension `d`, then (1) and (2) are also equivalent to
>
> 3. the classes of closed points generate `H^{2d}(X)(d)` as a module over `H^0(X)`
>    (`PointClassesGenerate`).
>
> Here `Spec(k')` is the smooth projective `k`-scheme `specGlobalSections X` and the map in (2) is
> pullback along the canonical morphism `X ⟶ Spec(k')`; "equidimensional of dimension `d`" is
> `RelativeDimension X.obj.hom d`, which allows `X = ∅`.

```lean
theorem globalSections_criterion [CharZero F] (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) (X : (SmoothProjectiveScheme k).FullSubcategory) :
    (W.SeparablePointsDetectH0 X ↔ Function.Bijective (W.pullDeg (toSpecGlobalSections X) 0)) ∧
      (Function.Bijective (W.pullDeg (toSpecGlobalSections X) 0) →
        FiniteDimensional F (W.H0 X) ∧ Algebra.IsSeparable F (W.H0 X)) ∧
      ∀ d : ℕ, RelativeDimension X.obj.hom d →
        (W.SeparablePointsDetectH0 X ↔ W.PointClassesGenerate X d)
```

## Tag 0FI1, a lemma

[Tag 0FI1](https://stacks.math.columbia.edu/tag/0FI1) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.exists_not_globalSections_criterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GlobalSectionsNegativeDegree.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/GlobalSectionsNegativeDegree.lean#L128). The attribute's comment: “H^i(Y) ≠ 0 for some smooth projective Y and i < 0 gives a nonempty equidimensional smooth projective X for which conditions (1), (2), (3) of 0FI0 all fail, on the actual Weil data (D0)-(D3) satisfying (A), (B), (C) over the actual category of smooth projective k-schemes”.

> **Stacks Project, Tag 0FI1.** Assume given (D0), (D1), (D2) and (D3) satisfying (A), (B) and
> (C). If there exists a smooth projective scheme `Y` over `k` such that `H^i(Y)` is nonzero for
> some `i < 0`, then there exists an equidimensional smooth projective scheme `X` over `k` such
> that the equivalent conditions of Stacks 0FI0 fail for `X`: (1) no finite family of closed points
> with separable residue fields detects `H^0(X)` (`SeparablePointsDetectH0`), (2) the map
> `H^0(Spec Γ(X, 𝒪_X)) → H^0(X)` is not an isomorphism, and (3) the classes of closed points do not
> generate `H^{2d}(X)(d)` as an `H^0(X)`-module (`PointClassesGenerate`), `d` the dimension of `X`.
> The scheme `X` is moreover nonempty.

```lean
theorem exists_not_globalSections_criterion [CharZero F] (hA : W.PoincareDuality)
    (hB : W.Kunneth) (hC : W.CycleClassAxiom hA.perfectPairing)
    (hneg : ∃ (Y : (SmoothProjectiveScheme k).FullSubcategory) (i : ℤ), i < 0 ∧ W.grade Y i ≠ ⊥) :
    ∃ (X : (SmoothProjectiveScheme k).FullSubcategory) (d : ℕ), IsNonemptyEquidimensional X d ∧
      ¬ W.SeparablePointsDetectH0 X ∧
      ¬ Function.Bijective (W.pullDeg (toSpecGlobalSections X) 0) ∧
      ¬ W.PointClassesGenerate X d
```

## Tag 0FI2, a definition

[Tag 0FI2](https://stacks.math.columbia.edu/tag/0FI2) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.WeilCohomology.WeilCohomologyTheory`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilCohomologyTheory.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilCohomologyTheoryTag.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilCohomologyTheoryTag.lean#L37) (StacksFrontier): “Weil cohomology theory: data (D0)-(D3) on the smooth projective (01W8, not merely proper) k-schemes satisfying (A), (B), (C) of 0FHA and condition (2) of 0FI0 for every X, the equivalent condition (1) following by 0FI0. Generalized to any coefficient field F, with no [CharZero F]: with it, this is the source's notion. (B)(b) reads ∫_X ⊗ ∫_Y as zero off the top Künneth component H^{2d}(X)(d) ⊗ H^{2e}(Y)(e) of H^{2(d+e)}(X × Y)(d + e), the trace maps being extended by zero outside their degree as in 'Ad (A6)'”.

## Tag 0FI3, a remark

[Tag 0FI3](https://stacks.math.columbia.edu/tag/0FI3) in the Stacks Project.

**`Stacks.WeilCohomology.WeilCohomologyTheory.factorwise_rank_one_of_geometricallyIrreducible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProductOfFieldsFactors.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProductOfFieldsFactors.lean#L428). The attribute's comment: “for H^* a Weil cohomology theory (0FI2), X geometrically irreducible smooth projective of dimension d over a finite separable k'/k, viewed over k, and H^0(Spec k') → ∏ F_i bijective for fields F_i: H^*(X) and each H^n(X) are ∏_i of their base changes to the F_i by x ↦ (1 ⊗ x)_i; H^0(X) and H^{2d}(X) are free of rank 1 over H^0(Spec k'), with each factor of dimension 1 over F_i; M ⊗_{H^0(Spec k')} F_i is written F_i ⊗_{H^0(Spec k')} M; no CharZero F needed”.

> Let `H^*` be a Weil cohomology theory (Definition 0FI2). Let `X` be a geometrically
> irreducible smooth projective scheme of dimension `d` over `k'`, with `k'/k` a finite separable
> extension of fields. Suppose that `H^0(Spec(k')) = F_1 × ⋯ × F_r` for fields `F_i`. Then
>
> 1. `H^*(X) = ∏_i H^*(X) ⊗_{H^0(Spec k')} F_i`, by `x ↦ (x ⊗ 1)_i`, and likewise in each
>    degree;
> 2. `H^0(X)` is free of rank `1` over `∏_i F_i`, and each factor
>    `H^0(X) ⊗_{H^0(Spec k')} F_i` has dimension `1` over `F_i`;
> 3. the same is true in degree `2d`: `H^{2d}(X)` is free of rank `1` over `∏_i F_i`, and each
>    `H^{2d}(X) ⊗_{H^0(Spec k')} F_i` has dimension `1` over `F_i`.
>
> Here `X` is a scheme with a smooth projective, geometrically irreducible structure morphism
> `p : X ⟶ Spec k'`, viewed over `k` through `Spec k' ⟶ Spec k` (`ofOver k p hp`), `Spec k'` is
> the smooth projective `k`-scheme `spec k k'`, and "of dimension `d`" is
> `topologicalKrullDim X = d`. `H^*(X)` is an `H^0(Spec k')`-algebra by pullback
> along `X ⟶ Spec k'`, and `H^n(X)` is its degree `n` part (`WeilData.gradeOverSpec`).
> "`H^0(Spec(k')) = F_1 × ⋯ × F_r`" is a finite family of fields `F_i`, each an
> `H^0(Spec k')`-algebra, with `H^0(Spec k') → ∏_i F_i` bijective. The factor
> `M ⊗_{H^0(Spec k')} F_i` is written as the base change `F_i ⊗_{H^0(Spec k')} M`, which is the same
> module by the symmetry of the tensor product. The coefficient field `F` is not required to have
> characteristic zero.

```lean
theorem factorwise_rank_one_of_geometricallyIrreducible (W : WeilCohomologyTheory k F)
    {k' : Type u} [Field k'] [Algebra k k'] [FiniteDimensional k k'] [Algebra.IsSeparable k k']
    {X : Scheme.{u}} (p : X ⟶ Spec (.of k')) [Smooth p] [GeometricallyIrreducible p]
    (hp : IsProjectiveMorphism p) {d : ℕ} (hd : topologicalKrullDim X = d)
    {ι : Type*} [Fintype ι] [DecidableEq ι] (K : ι → Type*) [∀ i, Field (K i)]
    [∀ i, Algebra (W.H0 (spec k k')) (K i)]
    (hK : Function.Bijective (Pi.ringHom fun i ↦ algebraMap (W.H0 (spec k k')) (K i))) :
    Function.Bijective (fun (x : W.H (ofOver k p hp)) (i : ι) ↦
        (1 : K i) ⊗ₜ[W.H0 (spec k k')] x) ∧
      (∀ n : ℤ, Function.Bijective (fun (x : W.gradeOverSpec p hp n) (i : ι) ↦
        (1 : K i) ⊗ₜ[W.H0 (spec k k')] x)) ∧
      Nonempty (W.H0 (spec k k') ≃ₗ[W.H0 (spec k k')] W.gradeOverSpec p hp 0) ∧
      (∀ i, Module.finrank (K i) (K i ⊗[W.H0 (spec k k')] W.gradeOverSpec p hp 0) = 1) ∧
      Nonempty (W.H0 (spec k k') ≃ₗ[W.H0 (spec k k')] W.gradeOverSpec p hp (2 * d)) ∧
      (∀ i, Module.finrank (K i) (K i ⊗[W.H0 (spec k k')] W.gradeOverSpec p hp (2 * d)) = 1)
```

## Tag 0GIJ, a proposition

[Tag 0GIJ](https://stacks.math.columbia.edu/tag/0GIJ) in the Stacks Project.

**`Stacks.WeilCohomology.WeilRealization.exists_globalSections_isoClassEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilRealizationGlobalSections.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilRealizationGlobalSections.lean#L331). The attribute's comment: “a Weil cohomology theory is the same thing as a Q-linear symmetric monoidal functor G : M_k -> graded F-vector spaces with G(1(1)) nonzero only in degree -2 and G(h(Spec k')) -> G(h(X)) an isomorphism in degree 0 for k' = Gamma(X, O_X): a bijection of isomorphism classes, G corresponding to H^*(X) = G(h(X))”.

> **Stacks Project, Tag 0GIJ.** Let `k` be a field and `F` a field of characteristic `0`. A Weil
> cohomology theory (Definition 0FI2) is the same thing as a `ℚ`-linear symmetric monoidal functor
> `G : M_k ⥤ graded F-vector spaces` (`Stacks.WeilCohomology.WeilRealization`) such that
>
> 1. `G(𝟏(1))` is nonzero only in degree `-2`, and
> 2. for every smooth projective `X` over `k` with `k' = Γ(X, 𝒪_X)` the map
>    `G(h(Spec k')) → G(h(X))` is an isomorphism in degree `0`
>    (`Stacks.WeilCohomology.WeilRealization.GlobalSections`):
>
> there is a bijection between isomorphism classes of such functors and isomorphism classes of
> Weil cohomology theories, sending the class of `G` to the class of the Weil cohomology theory
> `H^*(X) = G(h(X))` of Stacks 0FHK.

```lean
theorem exists_globalSections_isoClassEquiv :
    ∃ e : Quotient ((isoSetoid k F).comap
          (Subtype.val : {G : WeilRealization k F // G.GlobalSections} → _)) ≃
        Quotient (WeilCohomologyTheory.isoSetoid k F),
      ∀ (G : {G : WeilRealization k F // G.GlobalSections}) (T : WeilCohomologyTheory k F),
        e (Quotient.mk _ G) = Quotient.mk _ T ↔
          (Quotient.mk (WeilDataAxioms.isoSetoid k F) G.1.toWeilDataAxioms =
            Quotient.mk _ T.toWeilDataAxioms)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.11, Tag 0FHY](https://stacks.math.columbia.edu/tag/0FHY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
