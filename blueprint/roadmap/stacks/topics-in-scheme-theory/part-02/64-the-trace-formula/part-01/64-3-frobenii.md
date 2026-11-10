---
declaration: section
origin: cited
lean: cohomologyPullbackMap_eq_id_of_preimageEq, Stacks.EtaleCohomology.etaleCohomologyPullbackMap_comp_comparison, Stacks.EtaleCohomology.absoluteFrobeniusCohomologyFunctorIso, Stacks.EtaleCohomology.absoluteFrobenius_etaleCohomologyRestrictionMap_eq_id, Stacks.Frobenius.geometricFrobenius, Stacks.EtaleCohomology.geometricFrobeniusPushforwardIso, Stacks.EtaleCohomology.geometricFrobeniusInverseImageIso, Stacks.EtaleCohomology.geometricFrobeniusDescentIsos
statement: formalized
proof: formalized
---

# 64.3 Frobenii

Section 64.3 of the Stacks Project, [Tag 03SL](https://stacks.math.columbia.edu/tag/03SL). 10 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03SO, an exercise

[Tag 03SO](https://stacks.math.columbia.edu/tag/03SO) in the Stacks Project.

**`cohomologyPullbackMap_eq_id_of_preimageEq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pullback/IdOfPreimageEq.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/IdOfPreimageEq.lean#L99). The attribute's comment: “g induces the identity on cohomology, for any coefficients”.

> **Stacks tag 03SO.** Let `X` be a topological space and `g : X ⟶ X` a continuous map such
> that `g ⁻¹' U = U` for every open `U` of `X`. Then the map `g` induces on sheaf cohomology,
> followed by the canonical comparison of the pullback sheaf with the original one, is the
> identity, in every degree `n` and for every abelian sheaf `F`: `g` induces the identity on
> cohomology, for any coefficients.
>
> See [Stacks Project, Tag 03SO](https://stacks.math.columbia.edu/tag/03SO).

```lean
theorem cohomologyPullbackMap_eq_id_of_preimageEq
    [HasExt.{w} (Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u})]
    (F : Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{u}) (n : ℕ) :
    (Sheaf.H.map ((Adjunction.leftAdjointIdIso (sheafAdjunctionOpensMap g)
          (sheafPushforwardIdOfPreimageEq g h)).hom.app F) n).comp
        (Stacks.Cohomology.cohomologyPullbackMap.{w} (sheafAdjunctionOpensMap g)
          (sheafPushforwardIdOfPreimageEq g h) F n) =
      AddMonoidHom.id (Sheaf.H.{w} F n)
```

## Tag 03SP, a lemma

[Tag 03SP](https://stacks.math.columbia.edu/tag/03SP) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleCohomologyPullbackMap_comp_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BafflingTheorem.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BafflingTheorem.lean#L207). The attribute's comment: “g induces the identity on cohomology, for any sheaf”.

> **Stacks Project, Tag 03SP.** Let `X` be a scheme and `g : X ⟶ X` a morphism such that every
> étale `X`-scheme `U` is isomorphic over `X` to its base change `U ×_{g} X`, functorially in `U`.
> Then `g` induces the identity on cohomology, for any abelian sheaf `F` and in every degree `n`:
> the map `H^n(X, F) ⟶ H^n(X, g^{-1}F)` induced by `g`, followed by the canonical comparison
> `H^n(X, g^{-1}F) ≅ H^n(X, F)`, is the identity of `H^n(X, F)`.
>
> See [Stacks Project, Tag 03SP](https://stacks.math.columbia.edu/tag/03SP).

```lean
public theorem etaleCohomologyPullbackMap_comp_comparison (X : Scheme.{u}) (g : X ⟶ X)
    (e : 𝟭 X.Etale ≅ smallEtaleBaseChange g)
    [HasWeakSheafify (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v}]
    [∀ F : X.Etaleᵒᵖ ⥤ AddCommGrpCat.{max (u + 1) v},
      (smallEtaleBaseChange g).op.HasLeftKanExtension F]
    [HasSheafify (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v}]
    [HasExt.{w} (Sheaf (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v})]
    (F : Sheaf (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v}) (n : ℕ) :
    (Sheaf.H.map ((etaleSheafPullbackComparison.{u, v} X g e).hom.app F) n).comp
        (etaleCohomologyPullbackMap.{u, v, w} X g e F n) =
      AddMonoidHom.id (Sheaf.H.{w} F n)
```

## Tag 03SN, a theorem

[Tag 03SN](https://stacks.math.columbia.edu/tag/03SN) in the Stacks Project.

**`Stacks.EtaleCohomology.absoluteFrobeniusCohomologyFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BafflingTheorem.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BafflingTheorem.lean#L302). The attribute's comment: “pullback along the absolute Frobenius is identified with the identity functor”.

> On a scheme `X` of characteristic `p`, pullback along the absolute Frobenius is identified
> with the identity functor on abelian étale sheaves, so composing it with cohomology in degree `j`
> gives back cohomology in degree `j`, naturally in the sheaf.
>
> See [Stacks Project, Tag 03SN](https://stacks.math.columbia.edu/tag/03SN).

```lean
public def absoluteFrobeniusCohomologyFunctorIso
    [HasWeakSheafify (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v}]
    [∀ F : X.Etaleᵒᵖ ⥤ AddCommGrpCat.{max (u + 1) v},
      (smallEtaleBaseChange (absoluteFrobenius X p hX)).op.HasLeftKanExtension F]
    [HasSheafify (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v}]
    [HasExt.{w} (Sheaf (smallEtaleTopology X) AddCommGrpCat.{max (u + 1) v})] (j : ℕ) :
    Functor.sheafPullbackConstruction.sheafPullback
          (smallEtaleBaseChange (absoluteFrobenius X p hX)) AddCommGrpCat.{max (u + 1) v}
          (smallEtaleTopology X) (smallEtaleTopology X) ⋙
        Sheaf.functorH (smallEtaleTopology X) j ≅
      Sheaf.functorH (smallEtaleTopology X) j
```

**`Stacks.EtaleCohomology.absoluteFrobenius_etaleCohomologyRestrictionMap_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BafflingTheoremIdentity.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BafflingTheoremIdentity.lean#L110). The attribute's comment: “the induced map on H^j(X, Z/nZ) is the identity”. References: SGA 5 XV (2.Proposition2), “special case”.

> **The Baffling Theorem**: on a scheme `X` of characteristic `p` the absolute Frobenius induces
> the identity on `H^j(X, ℤ/nℤ)`. The canonical pullback map on étale cohomology, followed by the
> canonical identification of the inverse image of the constant sheaf `ℤ/nℤ` with `ℤ/nℤ`, sends
> every class to itself, in every degree `j`.

```lean
public theorem absoluteFrobenius_etaleCohomologyRestrictionMap_eq_id
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})] (n j : ℕ)
    (x : Sheaf.H.{w}
      ((constantSheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj
        (AddCommGrpCat.of (ULift.{max (u + 1) v} (ZMod n)))) j) :
    Sheaf.H.map
        ((etaleAbelianInverseImageConstantIso.{u, v} (absoluteFrobenius X p hX)).hom.app
          (AddCommGrpCat.of (ULift.{max (u + 1) v} (ZMod n)))) j
        (etaleCohomologyRestrictionMap.{u, v, w} (absoluteFrobenius X p hX)
          ((constantSheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj
            (AddCommGrpCat.of (ULift.{max (u + 1) v} (ZMod n)))) j x) = x
```

## Tag 03SQ, a definition

[Tag 03SQ](https://stacks.math.columbia.edu/tag/03SQ) in the Stacks Project.

**`Stacks.Frobenius.geometricFrobenius`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Frobenius.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Frobenius.lean#L276). References: SGA 4½ Rapport (1.1).

> **Stacks Project, Tag 03SQ.** The geometric Frobenius of a scheme over a finite field of
> characteristic `p` and cardinality `p ^ f`. It is the `f`-fold absolute Frobenius, bundled with
> its canonical structure as a morphism over the field.

```lean
noncomputable def geometricFrobenius {k : Type u} [Field k] [Fintype k]
    (X : Over (Spec (.of k))) (p f : ℕ) [Fact p.Prime] [CharP k p]
    (hcard : Fintype.card k = p ^ f) : X ⟶ X
```

## Tag 03SR, a lemma

[Tag 03SR](https://stacks.math.columbia.edu/tag/03SR) in the Stacks Project.

**`Stacks.EtaleCohomology.geometricFrobeniusPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusDescent.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusDescent.lean#L305). The attribute's comment: “direct image”. References: SGA 5 XII (7.3), “more general”.

> Let `k` be a finite field with `p ^ f` elements, let `X` be a scheme over `k` and let `π_X` be
> the geometric Frobenius of `X`. Then a sheaf `ℱ` on the small étale site of `X` is canonically
> isomorphic to its direct image `(π_X)_* ℱ`, naturally in `ℱ`.
> On sections over an étale `φ : U ⟶ X` the isomorphism
> `ℱ(U) ⟶ (π_X)_* ℱ(U) = ℱ(U ×_{φ, X, π_X} X)` is restriction along the inverse of
> `γ_U = (F_U^f, φ)`.

```lean
public def geometricFrobeniusPushforwardIso :
    𝟭 (Sheaf (smallEtaleTopology X.left) A) ≅
      (smallEtaleBaseChange
          (Stacks.Frobenius.geometricFrobenius X p f hcard).left).sheafPushforwardContinuous A
        (smallEtaleTopology X.left) (smallEtaleTopology X.left)
```

**`Stacks.EtaleCohomology.geometricFrobeniusInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusDescent.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusDescent.lean#L330). The attribute's comment: “inverse image, for coefficients admitting sheafification and left Kan extensions”.

> Let `k` be a finite field with `p ^ f` elements, let `X` be a scheme over `k` and let `π_X` be
> the geometric Frobenius of `X`. Then the inverse image `π_X^{-1} ℱ` of a sheaf `ℱ` on the small
> étale site of `X` is canonically isomorphic to `ℱ`, naturally in `ℱ`. The isomorphism is the
> left-adjoint mate of `geometricFrobeniusPushforwardIso`.

```lean
public def geometricFrobeniusInverseImageIso
    [HasWeakSheafify (smallEtaleTopology X.left) A]
    [∀ F : X.left.Etaleᵒᵖ ⥤ A,
      (smallEtaleBaseChange
        (Stacks.Frobenius.geometricFrobenius X p f hcard).left).op.HasLeftKanExtension F] :
    Functor.sheafPullbackConstruction.sheafPullback
        (smallEtaleBaseChange (Stacks.Frobenius.geometricFrobenius X p f hcard).left) A
        (smallEtaleTopology X.left) (smallEtaleTopology X.left) ≅
      𝟭 (Sheaf (smallEtaleTopology X.left) A)
```

**`Stacks.EtaleCohomology.geometricFrobeniusDescentIsos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusInverseImage.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FrobeniusInverseImage.lean#L157). References: SGA 4½ Rapport (1.2); SGA 5 XII (7.3), “more general”.

> **Stacks Project, Tag 03SR.** Let `k` be a finite field with `q = p ^ f` elements, let `X` be
> a scheme over `k` with geometric Frobenius `π_X = F_X^f`, and let `ℱ` be a sheaf on the small
> étale site `X_étale`, with values in any category (sets, abelian groups, `Λ`-modules, ...).
> Then there are canonical isomorphisms `π_X^{-1} ℱ ≅ ℱ` and `ℱ ≅ (π_X)_* ℱ`, natural in `ℱ`.
>
> Here `(π_X)_*` is precomposition with base change along `π_X`, and the inverse image `π_X^{-1}`
> is the left adjoint of `(π_X)_*`; its existence is proved, not assumed, since `(π_X)_*` is an
> equivalence. Where the coefficients admit sheafification it agrees with the sheafified left Kan
> extension (`CategoryTheory.Functor.sheafPullbackConstruction.sheafPullbackIso`), whose Kan
> extensions exist by `hasLeftKanExtension_smallEtaleBaseChange_geometricFrobenius_op`. On
> sections over an étale `φ : U ⟶ X` the second isomorphism is restriction along the inverse of
> `γ_U = (F_U^f, φ) : U ⟶ U ×_{φ, X, π_X} X` (`geometricFrobeniusPushforwardIso_hom_app_hom_app`),
> and the first is its left-adjoint mate
> (`sheafAdjunctionContinuous_unit_comp_geometricFrobeniusSheafPullbackIso`).

```lean
public def geometricFrobeniusDescentIsos :
    (Functor.sheafPullback
        (smallEtaleBaseChange (Stacks.Frobenius.geometricFrobenius X p f hcard).left) A
        (smallEtaleTopology X.left) (smallEtaleTopology X.left) ≅
      𝟭 (Sheaf (smallEtaleTopology X.left) A)) ×
    (𝟭 (Sheaf (smallEtaleTopology X.left) A) ≅
      (smallEtaleBaseChange
          (Stacks.Frobenius.geometricFrobenius X p f hcard).left).sheafPushforwardContinuous A
        (smallEtaleTopology X.left) (smallEtaleTopology X.left))
```

## Tag 03SS, a remark

[Tag 03SS](https://stacks.math.columbia.edu/tag/03SS) in the Stacks Project.

**`Stacks.Frobenius.geometricFrobenius_left_eq_absoluteFrobenius_pow_and_exists_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Frobenius.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Frobenius.lean#L382).

> **Stacks Project, Tag 03SS.** The geometric Frobenius of a scheme over a finite field with
> `p ^ f` elements is the `f`-fold absolute Frobenius. The exponent is read off from the base
> field, so a scheme over two finite fields `k` and `k'` can have two distinct geometric Frobenius
> endomorphisms, as does the spectrum of a field with `p ^ 2` elements over the prime field and
> over itself.

```lean
theorem geometricFrobenius_left_eq_absoluteFrobenius_pow_and_exists_ne :
    (∀ (k : Type u) [Field k] [Fintype k] (p f : ℕ) [Fact p.Prime] [CharP k p]
        (hcard : Fintype.card k = p ^ f) (U : Over (Spec (.of k))),
        (geometricFrobenius U p f hcard).left =
          End.asHom (End.of (absoluteFrobenius U.left p (isInCharacteristic_of_over U)) ^ f)) ∧
      ∃ (p f f' : ℕ) (_ : Fact p.Prime) (k k' : Type u) (_ : Field k) (_ : Fintype k)
        (_ : CharP k p) (_ : Field k') (_ : Fintype k') (_ : CharP k' p)
        (hcard : Fintype.card k = p ^ f) (hcard' : Fintype.card k' = p ^ f') (U : Scheme.{u})
        (g : U ⟶ Spec (.of k)) (g' : U ⟶ Spec (.of k')),
        (geometricFrobenius (Over.mk g) p f hcard).left ≠
          (geometricFrobenius (Over.mk g') p f' hcard').left
```

## Tag 03ST, a lemma

[Tag 03ST](https://stacks.math.columbia.edu/tag/03ST) in the Stacks Project.

**`Stacks.Frobenius.fibreComparison_galoisStalkAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GaloisActionFibreCohomology.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GaloisActionFibreCohomology.lean#L395). The attribute's comment: “Galois equivariance of the Theorem 03Q9 comparison in degree zero: unconditional in `α`, in the sheaf and in the algebraically closed extension, stated on the germ at an arbitrary étale neighbourhood of the geometric point. That the comparison is an isomorphism is Tag 03Q9, available in this library only over a strictly henselian base, and the equivariance in degree j > 0 needs transitivity of restriction of sections in the scheme over the base; neither is assumed here”.

> **Stacks Project, Tag 03ST, Galois equivariance in degree zero.** The comparison of Étale
> Cohomology, Theorem 03Q9 carries the Galois action of Étale Cohomology Section 03QW on the stalk
> `(α_* ℱ)_{Spec k̄}` to restriction along the automorphism `id_X × Spec σ` of the geometric fibre
> `X_{k̄}`: on the germ at an étale neighbourhood `W` of the geometric point, acting by `σ` and
> then comparing is restricting along `(id_X × Spec σ) ∘ (X_{k̄} ⟶ X_W)`.
>
> Since the germs are jointly surjective onto the stalk, this determines the induced map on the
> whole stalk, and it is the statement that the identification of Tag 03Q9 is a map of
> `G_k`-modules.

```lean
public theorem fibreComparison_galoisStalkAction (σ : K ≃ₐ[k] K)
    (W : (Spec (.of k)).Etale)
    (u : (Scheme.pointSmallEtale (specAlgebraMap k K)).fiber.obj W) :
    (Scheme.pointSmallEtale (specAlgebraMap k K)).toPresheafFiber W u
          ((sheafToPresheaf _ _).obj ((smallEtalePushforwardAb X.hom).obj F)) ≫
        (galoisStalkAction Ab.{u + 1} K σ (𝟙 (Spec (.of k)))).app
          ((smallEtalePushforwardAb X.hom).obj F) ≫
        fibreComparison K X F =
      (smallEtaleSectionsPullbackAb (pullback.fst X.hom (specAlgebraMap k K))
        ((smallEtaleBaseChange X.hom).obj W)
        (galoisBaseChange X K σ ≫ fibreLift K X W u)
        ((congrArg (fun z => z ≫ ((smallEtaleBaseChange X.hom).obj W).hom)
            (galoisBaseChange_comp_fibreLift K X σ W u).symm).trans
          (fibreLift_comp_hom K X W (galoisLift K σ W u)))).app F
```

**`Stacks.Frobenius.higherDirectImageFibreMap_isIso_galoisEquivariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GaloisModuleHigherDirectImageStalk.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GaloisModuleHigherDirectImageStalk.lean#L245). References: SGA 4½ Arcata (2.3.3), “special case”; SGA 4½ Rapport (1.4), “special case”; SGA 7 XXII (2.2), “more general”.

> **Stacks Project, Tag 03ST.** Let `k` be a finite field, `K` an algebraic closure of `k`,
> `G_k = Gal(K/k)`, `α : X ⟶ Spec k` quasi-compact and quasi-separated, and `ℱ` an abelian sheaf on
> `X_étale`. For every `j`, the identification `(R^j α_* ℱ)_{Spec K} ≅ H^j(X_K, ℱ|_{X_K})` of
> Étale Cohomology, Theorem 03Q9 is an isomorphism of `G_k`-modules:
>
> * it is an isomorphism;
> * it carries the Galois action of Étale Cohomology Section 03QW on the stalk at `Spec K` of the
>   `j`-th higher direct image (`Stacks.Frobenius.fieldGaloisStalkAction`, which is the base's
>   `Stacks.Frobenius.galoisStalkAction` at the rational point `𝟙 (Spec k)`) to the action
>   `σ ↦ (Spec σ × id_X)^*` on cohomology (`Stacks.Frobenius.galoisCohomologyAction`);
> * the latter is a left action of `G_k`, as the former is (`fieldGaloisStalkAction_one`,
>   `fieldGaloisStalkAction_mul`).
>
> The identification is `Stacks.Frobenius.higherDirectImageFibreMap`: the degree-zero comparison of
> 03Q9 — restriction of the germ of a section of `α_* ℱ` over an étale neighbourhood of `Spec K` to
> the geometric fibre `X_K` — passed to right derived functors; the strict henselization of `Spec k`
> at `Spec K` is `Spec K`, the finite field `k` being perfect. The hypothesis on `α` is that of
> Theorem 03Q9, whose identification exists only then; see the module docstring.
>
> In the language of modules: `Stacks.Frobenius.higherDirectImageFibreAddEquiv` is an additive
> equivalence which is `G_k`-equivariant (`Stacks.Frobenius.higherDirectImageFibreAddEquiv_smul`) for
> the `G_k`-module structures `Stacks.Frobenius.galoisHigherDirectImageStalkDistribMulAction` and
> `Stacks.Frobenius.galoisCohomologyDistribMulAction`.

```lean
theorem higherDirectImageFibreMap_isIso_galoisEquivariant [Finite k] [Algebra.IsAlgebraic k K]
    [QuasiCompact X.hom] [QuasiSeparated X.hom] (j : ℕ)
    (F : Sheaf (smallEtaleTopology X.left) Ab.{u + 1}) :
    IsIso (higherDirectImageFibreMap K X (acyclic_fieldBaseChangePullbackAb_of_injective K X) j F) ∧
      (∀ σ : K ≃ₐ[k] K,
        (fieldGaloisStalkAction K σ).app (((smallEtalePushforwardAb X.hom).rightDerived j).obj F) ≫
            higherDirectImageFibreMap K X (acyclic_fieldBaseChangePullbackAb_of_injective K X) j F =
          higherDirectImageFibreMap K X (acyclic_fieldBaseChangePullbackAb_of_injective K X) j F ≫
            galoisCohomologyAction K X σ j F) ∧
      galoisCohomologyAction K X (1 : K ≃ₐ[k] K) j F = 𝟙 _ ∧
      ∀ σ τ : K ≃ₐ[k] K, galoisCohomologyAction K X (σ * τ) j F =
        galoisCohomologyAction K X τ j F ≫ galoisCohomologyAction K X σ j F
```

## Tag 03SU, a definition

[Tag 03SU](https://stacks.math.columbia.edu/tag/03SU) in the Stacks Project.

**`Stacks.Frobenius.arithmeticFrobenius`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Frobenius.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Frobenius.lean#L304). References: SGA 7 XXI (5.0).

> **Stacks Project, Tag 03SU.** The arithmetic Frobenius `x ↦ x ^ q` of a finite field `k`
> with `q = p ^ f` elements, acting on a perfect extension field `K` of exponential
> characteristic `p`. It is the `f`-fold Frobenius automorphism of `K`, and it fixes `k`
> pointwise because every element of a field with `q` elements satisfies `x ^ q = x`.

```lean
noncomputable def arithmeticFrobenius (hcard : Fintype.card k = p ^ f) : K ≃ₐ[k] K
```

## Tag 03SV, a theorem

[Tag 03SV](https://stacks.math.columbia.edu/tag/03SV) in the Stacks Project.

**`Stacks.Frobenius.galoisRestrictionEndo_comp_geometricFrobeniusRestrictionEndo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ArithmeticFrobeniusInverse.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ArithmeticFrobeniusInverse.lean#L434). The attribute's comment: “the Galois action of frob\_k after the map induced by the geometric Frobenius is the identity”.

> Let `k` be a finite field with `q = p ^ f` elements, let `X` be a scheme over `k`, let
> `K/k` be an extension and let `σ` be the arithmetic Frobenius `x ↦ x ^ q` of `K`. For an
> abelian sheaf `ℱ` on `X_étale` and every degree `j`, the endomorphism of `H^j(X_K, ℱ|_{X_K})`
> induced by the Galois action `id_X × Spec(σ)` undoes the one induced by `π_X × id`: the
> arithmetic Frobenius acts as the inverse of `π_X^*`.
>
> Each endomorphism restricts along the morphism of `X_K` and then identifies the coefficients
> again: along `X` for the Galois action (`galoisRestrictionCoeff`), and through the Frobenius
> descent on `X` for the geometric Frobenius (`geometricFrobeniusRestrictionCoeff`).

```lean
public theorem galoisRestrictionEndo_comp_geometricFrobeniusRestrictionEndo (n : ℕ)
    (F : Sheaf X.left.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    (etaleCohomologyEndo.{u, v, w} (galoisBaseChange X K σ)
          ((etaleAbelianInverseImage.{u, v} (fieldBaseChangeProj X K)).obj F)
          (galoisRestrictionCoeff.{u, v} X K σ F) n).comp
        (etaleCohomologyEndo.{u, v, w} (geometricFrobeniusBaseChange X K p f hcard)
          ((etaleAbelianInverseImage.{u, v} (fieldBaseChangeProj X K)).obj F)
          (geometricFrobeniusRestrictionCoeff.{u, v} X K p f hcard F) n) =
      AddMonoidHom.id (Sheaf.H.{w}
        ((etaleAbelianInverseImage.{u, v} (fieldBaseChangeProj X K)).obj F) n)
```

**`Stacks.Frobenius.geometricFrobeniusRestrictionEndo_comp_galoisRestrictionEndo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ArithmeticFrobeniusInverse.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ArithmeticFrobeniusInverse.lean#L471). The attribute's comment: “the map induced by the geometric Frobenius after the Galois action of frob\_k is the identity”.

> With the data of `galoisRestrictionEndo_comp_geometricFrobeniusRestrictionEndo`, the
> endomorphism of `H^j(X_K, ℱ|_{X_K})` induced by `π_X × id` undoes the one induced by the Galois
> action `id_X × Spec(σ)`; so the two endomorphisms are mutually inverse.

```lean
public theorem geometricFrobeniusRestrictionEndo_comp_galoisRestrictionEndo (n : ℕ)
    (F : Sheaf X.left.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) :
    (etaleCohomologyEndo.{u, v, w} (geometricFrobeniusBaseChange X K p f hcard)
          ((etaleAbelianInverseImage.{u, v} (fieldBaseChangeProj X K)).obj F)
          (geometricFrobeniusRestrictionCoeff.{u, v} X K p f hcard F) n).comp
        (etaleCohomologyEndo.{u, v, w} (galoisBaseChange X K σ)
          ((etaleAbelianInverseImage.{u, v} (fieldBaseChangeProj X K)).obj F)
          (galoisRestrictionCoeff.{u, v} X K σ F) n) =
      AddMonoidHom.id (Sheaf.H.{w}
        ((etaleAbelianInverseImage.{u, v} (fieldBaseChangeProj X K)).obj F) n)
```

## Tag 03SW, a definition

[Tag 03SW](https://stacks.math.columbia.edu/tag/03SW) in the Stacks Project.

**`Stacks.Frobenius.geometricFrobeniusStalkFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricFrobeniusStalk.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricFrobeniusStalk.lean#L183). The attribute's comment: “on the stalk functor”. References: SGA 7 XXI (5.0), “F\_x acts on G\_x̄”; SGA 7 I (6.3); SGA 7 XXII (2.2.4), “The element φ\_q”.

> **Stacks Project, Tag 03SW.** The geometric Frobenius at a rational point `x` of a scheme
> over a finite field `k` with `p ^ f` elements, as an endomorphism of the étale stalk functor at
> the geometric point over `x`: it is the action of the inverse of the arithmetic Frobenius.

```lean
def geometricFrobeniusStalkFunctor (hcard : Fintype.card k = p ^ f) (x : Spec (.of k) ⟶ X) :
    (Scheme.pointSmallEtale (rationalGeometricPoint K x).hom).sheafFiber (A := A) ⟶
      (Scheme.pointSmallEtale (rationalGeometricPoint K x).hom).sheafFiber
```

**`Stacks.Frobenius.geometricFrobeniusStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricFrobeniusStalk.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricFrobeniusStalk.lean#L191). References: SGA 7 XXI (5.0), “F\_x acts on G\_x̄”.

> **Stacks Project, Tag 03SW.** The geometric Frobenius at a rational point `x`, acting on
> the étale stalk of a sheaf `F` at the geometric point over `x`.

```lean
def geometricFrobeniusStalk (hcard : Fintype.card k = p ^ f) (x : Spec (.of k) ⟶ X)
    (F : Sheaf X.smallEtaleTopology A) :
    (Scheme.pointSmallEtale (rationalGeometricPoint K x).hom).sheafFiber.obj F ⟶
      (Scheme.pointSmallEtale (rationalGeometricPoint K x).hom).sheafFiber.obj F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.3, Tag 03SL](https://stacks.math.columbia.edu/tag/03SL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
