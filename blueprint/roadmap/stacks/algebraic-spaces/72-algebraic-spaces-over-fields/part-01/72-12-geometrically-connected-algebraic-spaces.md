---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsGeometricallyConnected, AlgebraicGeometry.Space.isGeometricallyConnected_iff_relocalizeRestrict, AlgebraicGeometry.Space.bijective_connectedComponents_pullback_of_isGeometricallyConnected, AlgebraicGeometry.Space.bijective_connectedComponents_relocalizeRestrict_of_isSepClosed, AlgebraicGeometry.Space.isGeometricallyConnected_iff_connectedSpace_of_isSepClosed, AlgebraicGeometry.Space.isGeometricallyConnected_iff_connectedSpace_sepClosure, AlgebraicGeometry.Space.galoisActionOnBaseChange, AlgebraicGeometry.Space.galoisActionOnBaseChange_ρ_app_fst
statement: formalized
proof: formalized
---

# 72.12 Geometrically connected algebraic spaces

Section 72.12 of the Stacks Project, [Tag 0A0Y](https://stacks.math.columbia.edu/tag/0A0Y). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A0Z, a definition

[Tag 0A0Z](https://stacks.math.columbia.edu/tag/0A0Z) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGeometricallyConnected`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L492).

> **Stacks 0A0Z.** A presheaf on the big fppf site over a field `k` — in particular an
> algebraic space over `k` — is *geometrically connected* when for every field extension `K/k`
> whose spectrum lies in the chosen big fppf site the base change `X_K` has a connected space
> of points.

```lean
def IsGeometricallyConnected (B : BigFppfSite.{u}) (k : Type u) [Field k]
    (hk : B.Contains (Spec (.of k)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u) : Prop
```

## Tag 0A10, a lemma

[Tag 0A10](https://stacks.math.columbia.edu/tag/0A10) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyConnected_iff_relocalizeRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 797](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L797).

> **Stacks 0A10.** A presheaf on the big fppf site over a field `k` — in particular an
> algebraic space over `k` — is geometrically connected over `k` if and only if its base change
> to a field extension `k'` of `k` is geometrically connected over `k'`.

```lean
theorem isGeometricallyConnected_iff_relocalizeRestrict (B : BigFppfSite.{u})
    (k k' : Type u) [Field k] [Field k'] [Algebra k k']
    (hk : B.Contains (Spec (.of k))) (hk' : B.Contains (Spec (.of k')))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsGeometricallyConnected B k hk X ↔
      IsGeometricallyConnected B k' hk'
        ((OverShriek.relocalizeRestrict (fieldExtensionMap B k k' hk hk')).obj X)
```

## Tag 0A11, a lemma

[Tag 0A11](https://stacks.math.columbia.edu/tag/0A11) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_connectedComponents_pullback_of_isGeometricallyConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 1005](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L1005).

> **Stacks 0A11.** Let `k` be a field, let `X` and `Y` be algebraic spaces over `k` and
> assume `X` is geometrically connected over `k`. The projection `X ×_k Y ⟶ Y` induces a
> bijection between the sets of connected components of the two point spaces.
>
> The projection is open on points because `X ⟶ Spec k` is universally open (Stacks 06DN), and
> its fibre over the point represented by a field-valued point `Spec K ⟶ Y` is the image of
> `|X_K ×_k Spec K|`; that fibre product is the base change `X_K` of `X` to `K` viewed again over
> `k`, whose point space is homeomorphic to `|X_K|` and so is connected. Stacks 0378 then gives
> the bijection.

```lean
theorem bijective_connectedComponents_pullback_of_isGeometricallyConnected
    {X Y : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (hY : IsAlgebraicSpace B (Spec (.of k)) hk Y)
    (hXconn : IsGeometricallyConnected B k hk X)
    (f : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hk))))
    (g : Y ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hk)))) :
    Function.Bijective
      (continuous_pointsMap B (Spec (.of k)) hk
        (pullback.snd f g)).connectedComponentsMap
```

## Tag 0A12, a lemma

[Tag 0A12](https://stacks.math.columbia.edu/tag/0A12) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_connectedComponents_relocalizeRestrict_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 1188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L1188). The attribute's comment: “bijection on connected components”. References: EGA IV (4.4.6), “more general”.

> **Stacks 0A12, the bijection on connected components.** Let `k` be a separably closed
> field, let `K/k` be a field extension whose spectrum lies in the chosen big fppf site and let
> `X` be an algebraic space over `k`. The map `|X_K| → |X|` induced by the base change is a
> bijection between the sets of connected components.
>
> Viewed again over `k`, the base change `X_K` is the product `Spec K ×_k X`
> (`CategoryTheory.OverShriek.isPullback_relocalizeRestrictCounit`), and `Spec K` is
> geometrically connected over `k`, so Stacks 0A11 applies to the projection to `X`.

```lean
theorem bijective_connectedComponents_relocalizeRestrict_of_isSepClosed [IsSepClosed k]
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    Function.Bijective
      (continuous_pointsOfRelocalizeRestrict B (Spec (.of K)) (Spec (.of k)) hK hk
        (fieldExtensionMap B k K hk hK) X
        (isAlgebraicSpace_relocalizeRestrict B (Spec (.of K)) (Spec (.of k)) hK hk
          (fieldExtensionMap B k K hk hK) X hX)).connectedComponentsMap
```

**`AlgebraicGeometry.Space.isGeometricallyConnected_iff_connectedSpace_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 1259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L1259). The attribute's comment: “geometric connectedness”.

> **Stacks 0A12, geometric connectedness.** Over a separably closed field an algebraic space
> is geometrically connected exactly when its space of points is connected.

```lean
theorem isGeometricallyConnected_iff_connectedSpace_of_isSepClosed [IsSepClosed k]
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsGeometricallyConnected B k hk X ↔ ConnectedSpace (points B (Spec (.of k)) hk X)
```

## Tag 0A13, a lemma

[Tag 0A13](https://stacks.math.columbia.edu/tag/0A13) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyConnected_iff_connectedSpace_sepClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 1291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L1291).

> **Stacks 0A13.** Let `k` be a field, let `K` be a separable algebraic closure of `k` whose
> spectrum lies in the chosen big fppf site and let `X` be an algebraic space over `k`. Then `X`
> is geometrically connected over `k` if and only if the base change `X_K` has a connected space
> of points.
>
> Geometric connectedness over `k` is geometric connectedness of `X_K` over `K` by Stacks 0A10,
> and over the separably closed field `K` that is connectedness by Stacks 0A12.

```lean
theorem isGeometricallyConnected_iff_connectedSpace_sepClosure (B : BigFppfSite.{u})
    (k K : Type u) [Field k] [Field K] [Algebra k K] [IsSepClosure k K]
    (hk : B.Contains (Spec (.of k))) (hK : B.Contains (Spec (.of K)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsGeometricallyConnected B k hk X ↔
      ConnectedSpace (points B (Spec (.of K)) hK
        ((OverShriek.relocalizeRestrict (fieldExtensionMap B k K hk hK)).obj X))
```

## Tag 0A14, an equation

[Tag 0A14](https://stacks.math.columbia.edu/tag/0A14) in the Stacks Project.

**`AlgebraicGeometry.Space.galoisActionOnBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 917](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L917). The attribute's comment: “the action”.

> **Stacks 0A14, the action.** The canonical action of the opposite group of `k`-algebra
> automorphisms of `K` on the base change `X_K`, viewed again as a presheaf over `k`. For a
> Galois extension `K/k` this is the Galois action on `X_{\overline{k}}`.
>
> The action is over `k`, not over `K`: an automorphism changes only the `K`-coordinate of a
> section.

```lean
noncomputable def galoisActionOnBaseChange :
    Action ((BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u) (MulOpposite (K ≃ₐ[k] K))
```

**`AlgebraicGeometry.Space.galoisActionOnBaseChange_ρ_app_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 948](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L948). The attribute's comment: “the action on the K-coordinate of a section”.

> **Stacks 0A14, the action on the `K`-coordinate.** An automorphism `σ` acts on a section
> of `X_K` over a `k`-scheme by composing its morphism to `Spec K` with the automorphism of
> `Spec K` induced by `σ`.

```lean
theorem galoisActionOnBaseChange_ρ_app_fst (σ : MulOpposite (K ≃ₐ[k] K))
    (W : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ)
    (x : ((OverShriek.relocalizePresheafFunctor (fieldExtensionMap B k K hk hK)).obj
      ((OverShriek.relocalizeRestrict (fieldExtensionMap B k K hk hK)).obj X)).obj W) :
    (((galoisActionOnBaseChange B k K hk hK X).ρ σ).asHom.app W x).val.1 =
      x.val.1 ≫ siteMapAlgAut B k K hK σ.unop
```

**`AlgebraicGeometry.Space.galoisActionOnBaseChange_ρ_app_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean, line 960](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnected.lean#L960). The attribute's comment: “the action on the section”.

> **Stacks 0A14, the action on the section.** An automorphism leaves the section of `X`
> itself untouched. The equality is heterogeneous because the type of the section is indexed by
> the morphism to `Spec K`, which the action does change.

```lean
theorem galoisActionOnBaseChange_ρ_app_snd (σ : MulOpposite (K ≃ₐ[k] K))
    (W : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ)
    (x : ((OverShriek.relocalizePresheafFunctor (fieldExtensionMap B k K hk hK)).obj
      ((OverShriek.relocalizeRestrict (fieldExtensionMap B k K hk hK)).obj X)).obj W) :
    HEq (((galoisActionOnBaseChange B k K hk hK X).ρ σ).asHom.app W x).val.2 x.val.2
```

## Tag 0A15, a lemma

[Tag 0A15](https://stacks.math.columbia.edu/tag/0A15) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finite_subextension_descending_isQuasiCompact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenGaloisDescent.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenGaloisDescent.lean#L616). The attribute's comment: “part (1)”.

> Let `X` be an algebraic space over a field `k` and let `K/k` be an algebraic field extension. A
> quasi-compact open subspace of the base change of `X` to `K` is the base change of a quasi-compact
> open subspace of the base change of `X` to a finite subextension of `K/k`.

```lean
theorem exists_finite_subextension_descending_isQuasiCompact_open (B : BigFppfSite.{u})
    (k K : Type u) [Field k] [Field K] [Algebra k K] [Algebra.IsAlgebraic k K]
    (hk : B.Contains (Spec (.of k))) (hK : B.Contains (Spec (.of K)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (V : Subfunctor ((OverShriek.relocalizeRestrict (fieldExtensionMap B k K hk hK)).obj X))
    (hV : IsOpenSubspace B (Spec (.of K)) hK V)
    (hVqc : IsQuasiCompactSpace B (Spec (.of K)) hK V.toFunctor) :
    ∃ (E : IntermediateField k K) (_ : FiniteDimensional k E)
      (hE : B.Contains (Spec (.of E)))
      (V' : Subfunctor
        ((OverShriek.relocalizeRestrict (fieldExtensionMap B k E hk hE)).obj X)),
      IsOpenSubspace B (Spec (.of E)) hE V' ∧
        IsQuasiCompactSpace B (Spec (.of E)) hE V'.toFunctor ∧
        Subfunctor.preimage V
            (eqToHom (relocalizeRestrict_fieldExtensionMap_comp B k E K hk hE hK X)) =
          OverShriek.relocalizeRestrictSubfunctor (fieldExtensionMap B E K hE hK) V'
```

**`AlgebraicGeometry.Space.exists_open_subgroup_fixing_isQuasiCompact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenGaloisDescent.lean, line 798](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOpenGaloisDescent.lean#L798). The attribute's comment: “part (2)”.

> Let `X` be an algebraic space over a field `k` and let `K/k` be a Galois extension. A
> quasi-compact open subspace of the base change of `X` to `K` is fixed by an open subgroup of
> `Gal(K/k)`.

```lean
theorem exists_open_subgroup_fixing_isQuasiCompact_open [IsGalois k K]
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (V : Subfunctor ((OverShriek.relocalizeRestrict (fieldExtensionMap B k K hk hK)).obj X))
    (hV : IsOpenSubspace B (Spec (.of K)) hK V)
    (hVqc : IsQuasiCompactSpace B (Spec (.of K)) hK V.toFunctor) :
    ∃ H : Subgroup Gal(K/k), IsOpen (H : Set Gal(K/k)) ∧
      ∀ σ : Gal(K/k), σ ∈ H →
        Subfunctor.preimage (galoisOpenSubfunctor B k K hk hK X V)
            ((galoisActionOnBaseChange B k K hk hK X).ρ (MulOpposite.op σ)).asHom =
          galoisOpenSubfunctor B k K hk hK X V
```

## Tag 0A16, a lemma

[Tag 0A16](https://stacks.math.columbia.edu/tag/0A16) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_closed_subset_with_preimage_eq_of_galois_invariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GaloisInvariantClosedSubspace.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GaloisInvariantClosedSubspace.lean#L721).

> **Stacks 0A16.** Let `K/k` be a Galois extension whose spectra lie in the chosen big fppf
> site, and let `X` be an algebraic space over `k`. A closed subset of the points of the base
> change `X_K` which is invariant under the action of every `k`-algebra automorphism of `K` is the
> inverse image of a closed subset of the points of `X`.

```lean
theorem exists_closed_subset_with_preimage_eq_of_galois_invariant (B : BigFppfSite.{u})
    (k K : Type u) [Field k] [Field K] [Algebra k K] [IsGalois k K]
    (hk : B.Contains (Spec (.of k))) (hK : B.Contains (Spec (.of K)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X)
    (Tbar : Set (points B (Spec (.of K)) hK
      ((OverShriek.relocalizeRestrict (fieldExtensionMap B k K hk hK)).obj X)))
    (hTbar : @IsClosed _ (pointTopology B (Spec (.of K)) hK _) Tbar)
    (hstable : ∀ σ : K ≃ₐ[k] K, galoisPointsAction B k K hk hK X σ ⁻¹' Tbar = Tbar) :
    ∃ T : Set (points B (Spec (.of k)) hk X),
      @IsClosed _ (pointTopology B (Spec (.of k)) hk X) T ∧
      pointsOfRelocalizeRestrict B (Spec (.of K)) (Spec (.of k)) hK hk
          (fieldExtensionMap B k K hk hK) X ⁻¹' T = Tbar
```

## Tag 0A17, a lemma

[Tag 0A17](https://stacks.math.columbia.edu/tag/0A17) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyConnected_iff_connectedSpace_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnectedFiniteSeparable.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyConnectedFiniteSeparable.lean#L378). References: EGA IV (8.4.5); EGA IV (4.5.18), “more general”.

> Let `k` be a field and let `X` be an algebraic space over `k`. Then `X` is
> geometrically connected over `k` if and only if the base change `X_{k'}` has a connected space of
> points for every finite separable field extension `k'/k` whose spectrum lies in the chosen big
> fppf site.

```lean
theorem isGeometricallyConnected_iff_connectedSpace_finite_separable (B : BigFppfSite.{u})
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
    (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of k)) hk X) :
    IsGeometricallyConnected B k hk X ↔
      ∀ (K : Type u) [Field K] [Algebra k K] [FiniteDimensional k K]
        [Algebra.IsSeparable k K] (hK : B.Contains (Spec (.of K))),
        ConnectedSpace (points B (Spec (.of K)) hK
          ((OverShriek.relocalizeRestrict (fieldExtensionMap B k K hk hK)).obj X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.12, Tag 0A0Y](https://stacks.math.columbia.edu/tag/0A0Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
