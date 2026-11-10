---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.IsInvertible, AlgebraicGeometry.SheafOfModules.IsTrivial, Stacks.SheafOfModules.Invertible.tensorInverseIsoDualSheaf, Stacks.SheafOfModules.isInvertible_iff_exists_tensor_iso_unit, Stacks.SheafOfModules.Invertible.isInvertible_iff_exists_tensor_iso_unit, Stacks.SheafOfModules.LocallyFiniteFree.isLocallyFiniteFreeSummand_of_isInvertible, Stacks.RingedSpace.modulePullback_isInvertible, AlgebraicGeometry.Scheme.isInvertibleModule_pushforward_of_isIso
statement: formalized
proof: formalized
---

# 17.25 Invertible modules

Section 17.25 of the Stacks Project, [Tag 01CR](https://stacks.math.columbia.edu/tag/01CR). 11 tags here are carried by 78 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01CS, a definition

[Tag 01CS](https://stacks.math.columbia.edu/tag/01CS) in the Stacks Project.

**`Stacks.SheafOfModules.IsInvertible`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean#L130). The attribute's comment: “invertible”.

> **Stacks Project, Tag 01CS**, equivalently **Tag 0409 (2)**. A sheaf of `O`-modules is
> *invertible* when its tensor functor is an equivalence. The universal property specifies that
> tensor functor independently of any chosen construction of sheafification, hence on every
> site; so the ringed-space form of the definition and the ringed-site form coincide here.

```lean
class IsInvertible
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)) : Prop
```

**`AlgebraicGeometry.SheafOfModules.IsTrivial`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Invertible.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Invertible.lean#L137). The attribute's comment: “trivial”.

> An `O`-module sheaf is trivial when it is isomorphic, as an `O`-module, to `O`
> itself.

```lean
noncomputable abbrev IsTrivial
    (L : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
      : Prop
```

## Tag 0B8K, a lemma

[Tag 0B8K](https://stacks.math.columbia.edu/tag/0B8K) in the Stacks Project.

**`Stacks.SheafOfModules.Invertible.tensorInverseIsoDualSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L307). The attribute's comment: “the tensor inverse is the dual”. References: SGA 6 VIII (3.5), “partial”.

> **Stacks Project, Tag 0B8N (c).** A sheaf of `𝒪`-modules `N` whose tensor product with `L` is
> isomorphic to the structure sheaf is isomorphic to `SheafHom(L, 𝒪)`.
>
> The hypothesis is clause (2) of the tag, so `L` is invertible and the evaluation pairing
> `SheafHom(L, 𝒪) ⊗_𝒪 L ⟶ 𝒪` is an isomorphism by `isIso_evaluation`. That exhibits
> `SheafHom(L, 𝒪)` as a two-sided tensor inverse of `L`, the braiding supplying the other order,
> while the given isomorphism exhibits `N` as one; a two-sided tensor inverse in a monoidal
> category is unique up to isomorphism
> (`CategoryTheory.MonoidalCategory.HasInverse.inv_iso`).

```lean
noncomputable def tensorInverseIsoDualSheaf
    (N : SheafOfModules.{max u v} (TensorSheafification.structureSheaf 𝒪 h𝒪))
    (e : ((Tensor.sheafTensor
      ⟨𝒪, Presheaf.isSheaf_of_isSheaf_comp _ 𝒪 (forget₂ CommRingCat RingCat) h𝒪⟩).obj L).obj N ≅
      SheafOfModules.unit (TensorSheafification.structureSheaf 𝒪 h𝒪)) :
    N ≅ dualSheaf 𝒪 h𝒪 L
```

**`Stacks.SheafOfModules.isInvertible_iff_exists_tensor_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRankOne.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRankOne.lean#L298). The attribute's comment: “(1) ⟺ (2)”.

> **Stacks Project, Tag 0B8K and Tag 0B8N, (1) ⟺ (2).** A sheaf of `O`-modules `L` is invertible
> if and only if there is a sheaf of `O`-modules `N` whose tensor product with `L` is isomorphic
> to `O`.
>
> For the forward implication the tensor functor of `L` is an equivalence, so `O` has a preimage `N`
> under it, and the universal property identifies the image of that preimage with `L ⊗_O N`. For the
> converse the isomorphism `L ⊗_O N ≅ O` is turned into a pairing of presheaves of modules by
> composing with the sheafification unit, and `isInvertible_of_pairing` applies.
>
> Tag 0B8K states this for a ringed space and Tag 0B8N for an arbitrary ringed site; the statement
> here is the one on a ringed site, so it carries both.

```lean
theorem isInvertible_iff_exists_tensor_iso_unit
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)) :
    IsInvertible O hO L ↔ ∃ N : SheafOfModules.{w}
      (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO),
      Nonempty (((Tensor.sheafTensor.{u, v, w, w, w}
        ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat) hO⟩).obj L).obj N ≅
        SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
```

**`Stacks.SheafOfModules.Invertible.isInvertible_iff_exists_tensor_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Ample/DescentStep.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Ample/DescentStep.lean#L200). The attribute's comment: “tensor_inverse_characterization”.

> **Stacks Project, Tag 0B8K.** A sheaf of modules is invertible if and only if it has a
> tensor inverse, that is, if and only if some `N` satisfies `L ⊗ N ≅ 𝒪`.

```lean
theorem isInvertible_iff_exists_tensor_iso_unit
    (L : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
      :
    IsInvertible O hO L ↔
      ∃ N : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O
        hO),
        Nonempty (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w}
          ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat) hO⟩).obj L).obj N ≅
          _root_.SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf O
            hO))
```

**`Stacks.SheafOfModules.LocallyFiniteFree.isLocallyFiniteFreeSummand_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Ample/LocallyFiniteFreeSummand.lean, line 1191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Ample/LocallyFiniteFreeSummand.lean#L1191). The attribute's comment: “locally_finite_free_summand”.

> **Stacks Project, Tag 0B8K.** An invertible sheaf of modules is locally a direct
> summand of a finite free sheaf.

```lean
theorem isLocallyFiniteFreeSummand_of_isInvertible
    (X : RingedSpace.{u, w}) (L : _root_.SheafOfModules.{u} (ringSheaf X))
    [HasWeakSheafify (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}]
    [(Opens.grothendieckTopology X.carrier).WEqualsLocallyBijective AddCommGrpCat.{u}]
    [∀ U : Opens X,
      HasWeakSheafify (Opens.grothendieckTopology (X.restrict U.isOpenEmbedding).carrier)
        AddCommGrpCat.{u}]
    [∀ U : Opens X,
      (Opens.grothendieckTopology
        (X.restrict U.isOpenEmbedding).carrier).WEqualsLocallyBijective
        AddCommGrpCat.{u}]
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ X.presheaf
        (forget₂ CommRingCat.{u} RingCat.{u}) X.IsSheaf) L) :
    ∀ x : X, ∃ (U : Opens X) (_ : x ∈ U) (n : ℕ),
      Nonempty (Retract ((modulePullback (X.ofRestrict U.isOpenEmbedding)).obj L)
        (_root_.SheafOfModules.free (ULift.{u} (Fin n))))
```

## Tag 0B8L, a lemma

[Tag 0B8L](https://stacks.math.columbia.edu/tag/0B8L) in the Stacks Project.

**`Stacks.RingedSpace.modulePullback_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackInvertible/Basic.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackInvertible/Basic.lean#L56).

> **Stacks Project, Tag 0B8L.** The pullback of an invertible module along a
> morphism of ringed spaces is invertible.

```lean
theorem modulePullback_isInvertible {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (L : SheafOfModules.{u} (structureSheafRing Y))
    [Stacks.SheafOfModules.IsInvertible Y.presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) Y.IsSheaf) L] :
    Stacks.SheafOfModules.IsInvertible X.presheaf
      (Presheaf.isSheaf_comp_of_isSheaf _ _ (forget₂ CommRingCat RingCat) X.IsSheaf)
      ((modulePullback f).obj L)
```

**`AlgebraicGeometry.Scheme.isInvertibleModule_pushforward_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/NonAlgebraizableLevelKernel.lean#L143). The attribute's comment: “the direct image of an invertible module along an isomorphism”.

> **The direct image of an invertible module along an isomorphism of schemes is invertible.**
> The direct image along the inverse of an isomorphism is its inverse image
> (`AlgebraicGeometry.Scheme.Modules.pushforwardInvIsoPullback`), and the inverse image of an
> invertible module is invertible (`Stacks.Modules.isInvertible_pullback`).

```lean
public theorem isInvertibleModule_pushforward_of_isIso {X Y : Scheme.{u}} (e : X ≅ Y)
    (L : Y.Modules) (hL : Stacks.Ample.IsInvertibleModule Y L) :
    Stacks.Ample.IsInvertibleModule X ((Scheme.Modules.pushforward e.inv).obj L)
```

**`Stacks.InvertiblePullback.isInvertible_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertiblePullback/Basic.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertiblePullback/Basic.lean#L126).

> **Stacks Tag 0B8L.** The pullback of an invertible sheaf of modules along a morphism of
> ringed spaces is invertible.
>
> A tensor inverse `N` of `L`, which Tag 0B8K produces from invertibility, is carried by `f^*` to a
> tensor inverse of `f^*L`: Tag 01CD turns `f^*(L ⊗ N)` into `f^*L ⊗ f^*N`, and
> `RingedSpaceModuleAdjunction.modulePullbackObjUnitIso` turns `f^* 𝒪_Y` into `𝒪_X`.

```lean
theorem isInvertible_pullback (L : SheafOfModules.{u} (structureRingSheaf Y))
    [Stacks.SheafOfModules.IsInvertible Y.sheaf.obj (structureRingSheaf Y).property L] :
    Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureRingSheaf X).property
      ((pullbackFunctor f).obj L)
```

**`Stacks.RingedSpace.isInvertible_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PullbackInvertible/RingedSpace.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PullbackInvertible/RingedSpace.lean#L88).

> **Stacks Project, Tag 0B8L.** The pullback `f^*L` of an invertible `𝒪_Y`-module along a
> morphism of ringed spaces `f : X ⟶ Y` is an invertible `𝒪_X`-module.
>
> The proof is the one the Stacks Project gives. Tag 0B8K produces an `𝒪_Y`-module `N` with
> `L ⊗_{𝒪_Y} N ≅ 𝒪_Y`; `Stacks.RingedSpace.tensorIsoUnitPullback` pulls that pairing back, which
> is where Tag 01CD enters; and Tag 0B8K read in the other direction concludes.

```lean
theorem isInvertible_modulePullback (f : X ⟶ Y)
    (L : SheafOfModules.{u} (structureSheafRing Y))
    [Stacks.SheafOfModules.IsInvertible Y.sheaf.obj (structureSheafRing Y).property L] :
    Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheafRing X).property
      ((modulePullback f).obj L)
```

**`RingedSpaceModuleAdjunction.modulePullback_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackInvertible.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/RingedSpace/ModulePullbackInvertible.lean#L43).

> The pullback of an invertible module is invertible: if tensoring by `L` is an
> autoequivalence of `Mod(𝒪_Y)`, then tensoring by `f^* L` is an autoequivalence of `Mod(𝒪_X)`.

```lean
theorem modulePullback_isInvertible {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (L : SheafOfModules.{u}
      (Stacks.SheafOfModules.TensorSheafification.structureSheaf Y.presheaf (structureSheafRing
        Y).property))
    [IsInvertible Y.presheaf (structureSheafRing Y).property L] :
    IsInvertible X.presheaf (structureSheafRing X).property
      ((RingedSpaceModuleAdjunction.modulePullback f).obj L)
```

## Tag 0B8M, a lemma

[Tag 0B8M](https://stacks.math.columbia.edu/tag/0B8M) in the Stacks Project.

**`Stacks.SheafOfModules.Invertible.isInvertible_of_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRankOneLocal.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRankOneLocal.lean#L285). The attribute's comment: “locally free of rank one implies invertible”.

> **Stacks Project, Tag 0B8M.** A finite locally free sheaf of modules of rank one is
> invertible.
>
> This is the statement for `Stacks.SheafOfModules.Invertible.IsFiniteLocallyFreeOfRank`, and it
> lives in that predicate's namespace;
> `Stacks.SheafOfModules.isInvertible_of_isFiniteLocallyFreeOfRank_one` of
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.LocallyTrivialInvertible.Basic` is the statement for
> `AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank`, the other rank predicate of
> [Stacks, Tag 01CS].
>
> The local generators of rank one give a covering family of the final object on which `L` becomes
> isomorphic to the structure sheaf; each such trivialization is a rank-one dual basis, and
> `isInvertible_of_dualBasisOne` turns a family of those on a covering family into invertibility
> by way of the evaluation pairing `L^∨ ⊗ L ⟶ 𝒪` and Tag 0B8K.

```lean
theorem isInvertible_of_isFiniteLocallyFreeOfRank_one
    (L : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
    [Invertible.IsFiniteLocallyFreeOfRank L 1] : IsInvertible 𝒪 h𝒪 L
```

**`Stacks.RingedSpace.isInvertible_of_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyTrivialInvertible/Basic.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyTrivialInvertible/Basic.lean#L229). The attribute's comment: “locally free of rank one implies invertible”.

> A sheaf of modules on a ringed space that is finite locally free of rank one is
> invertible.

```lean
theorem isInvertible_of_isFiniteLocallyFreeOfRank_one (X : RingedSpace.{u, u})
    (L : SheafOfModules.{u} (structureSheaf X.sheaf))
    [h : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank
      (C := Opens X) (J := Opens.grothendieckTopology X) L 1] :
    Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L
```

**`Stacks.RingedSpace.exists_isInvertible_not_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleCounterexample/Clause3.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertibleCounterexample/Clause3.lean#L49). The attribute's comment: “the converse fails for general ringed spaces”.

> **Clause 3 of Stacks Tag 0B8M.** On a general ringed space an invertible sheaf of modules
> need not be finite locally free of rank one: there is a ringed space `X` and a sheaf of
> `𝒪_X`-modules `L` with `L` invertible and `L` not finite locally free of rank one.
>
> The witness is the one-point ringed space whose ring of global sections is `ℤ[√-5]`, carrying
> the sheaf of modules attached to the non-principal invertible ideal `(2, 1 + √-5)`. Its single
> stalk is `ℤ[√-5]`, which is not a local ring; this is exactly what the local-stalk hypothesis of
> `Stacks.RingedSpace.isInvertible_iff_isFiniteLocallyFreeOfRank_one` rules out.

```lean
theorem exists_isInvertible_not_isFiniteLocallyFreeOfRank_one :
    ∃ (X : AlgebraicGeometry.RingedSpace.{u})
      (L : SheafOfModules.{u} (structureSheaf X.sheaf)),
      Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L ∧
        ¬AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank
          (C := Opens X) (J := Opens.grothendieckTopology X) L 1
```

**`Stacks.InvertibleLocallyFree.isInvertible_of_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleLocallyFree/DualBasis.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertibleLocallyFree/DualBasis.lean#L284). The attribute's comment: “(1)”.

> **Clause 1 of Stacks Tag 0B8M.** A sheaf of modules that is finite locally free of rank one
> is invertible, with invertibility read as
> `AlgebraicGeometry.SheafOfModules.IsInvertible` — the predicate every consumer in this
> repository uses.
>
> This is unconditional. It does **not** use
> `Stacks.InvertibleLocallyFree.InvertibleIsLocal` (which is itself proved, as
> `Stacks.SheafOfModules.invertibleIsLocal`): clause 1 does not need
> descent of the inverse object, because the inverse is the dual sheaf `L^∨ = SheafHom(L, 𝒪)` and
> the only local-to-global step is that a locally bijective pairing is inverted by sheafification.
> See the module documentation for the forced universe constraint `w = max u v`, inherited from
> the internal hom of Tag 03EM.

```lean
theorem isInvertible_of_isFiniteLocallyFreeOfRank_one
    (L : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank L 1] :
    AlgebraicGeometry.SheafOfModules.IsInvertible 𝒪 h𝒪 L
```

**`Stacks.InvertibleRankOneIff.isInvertible_of_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleRankOneIff/Basic.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertibleRankOneIff/Basic.lean#L137). The attribute's comment: “locally free of rank one implies invertible”.

> **Clause 1 of Stacks Tag 0B8M.** A finite locally free module of rank one on a ringed space
> is invertible. There is no hypothesis on the stalks of the structure sheaf, and none on the site.
>
> The content is `Stacks.SheafDescent.isInvertible_of_isFiniteLocallyFreeOfRank_one`; what is done
> here is to restate it over `structureSheaf X.sheaf`, which forces the carrier universe of the
> ringed space to agree with the universe of its rings and so makes the sheafification instances
> available.

```lean
theorem isInvertible_of_isFiniteLocallyFreeOfRank_one
    (X : RingedSpace.{u})
    (L : SheafOfModules.{u} (structureSheaf X.sheaf))
    [SheafOfModules.IsFiniteLocallyFreeOfRank (C := Opens X)
      (J := Opens.grothendieckTopology X) L 1] :
    SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L
```

**`Stacks.InvertibleRankOneIff.isInvertible_iff_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleRankOneIff/Basic.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertibleRankOneIff/Basic.lean#L157). The attribute's comment: “characterization for local stalks”.

> **Clause 2 of Stacks Tag 0B8M.** On a ringed space all of whose stalks `𝒪_{X, x}` are local
> rings, a sheaf of modules is invertible exactly when it is finite locally free of rank one.
>
> The forward implication is `Stacks.SheafRankOne.isFiniteLocallyFreeOfRank_one_of_isInvertible`
> and is where the local-stalk hypothesis is spent; the reverse implication is clause 1, which
> holds on every ringed space.

```lean
theorem isInvertible_iff_isFiniteLocallyFreeOfRank_one
    (X : RingedSpace.{u})
    (L : SheafOfModules.{u} (structureSheaf X.sheaf))
    [∀ x : X, IsLocalRing (X.presheaf.stalk x)] :
    SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L ↔
      SheafOfModules.IsFiniteLocallyFreeOfRank (C := Opens X)
        (J := Opens.grothendieckTopology X) L 1
```

**`Stacks.RingedSpace.isInvertible_iff_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleTrivialization/Sheaf.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InvertibleTrivialization/Sheaf.lean#L114). The attribute's comment: “characterization for local stalks”.

> On a ringed space all of whose structure-sheaf stalks are local rings, a sheaf of modules is
> invertible if and only if it is finite locally free of rank one.

```lean
theorem isInvertible_iff_isFiniteLocallyFreeOfRank_one (X : RingedSpace.{u, u})
    (L : SheafOfModules.{u} (structureSheaf X.sheaf))
    [∀ x : X, IsLocalRing (X.presheaf.stalk x)] :
    Stacks.SheafOfModules.IsInvertible X.sheaf.obj (structureSheaf X.sheaf).property L ↔
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank
        (C := Opens X) (J := Opens.grothendieckTopology X) L 1
```

**`AlgebraicGeometry.RingedSite.isInvertible_of_isFiniteLocallyFreeOfRank_one_of_essentiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOneEssentiallySmall.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOneEssentiallySmall.lean#L319). The attribute's comment: “locally free of rank one implies invertible, on an essentially small site”.

> **Stacks Project, Tag 0B8M**, clause 1, on an essentially small ringed site. A sheaf of
> modules which is locally free of rank one is invertible, with the universe of the sections of
> the structure sheaf independent of the universes of the site.

```lean
theorem isInvertible_of_isFiniteLocallyFreeOfRank_one_of_essentiallySmall
    (X : AlgebraicGeometry.RingedSite.{u₁, v₁, w}) [EssentiallySmall.{w} X.C]
    [HasWeakSheafify X.J AddCommGrpCat.{w}] [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hL : AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank X L 1) :
    Stacks.SheafOfModules.IsInvertible X.O.obj
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O).property L
```

## Tag 01CT, a lemma

[Tag 01CT](https://stacks.math.columbia.edu/tag/01CT) in the Stacks Project.

**`Stacks.SheafOfModules.Invertible.isIso_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L261). The attribute's comment: “evaluation”. References: EGA 0 (5.4.3), “more general”.

> **Stacks Project, Tag 040A (2), the evaluation clause.** For an invertible sheaf of
> `𝒪`-modules `L` on a ringed site the evaluation pairing `SheafHom(L, 𝒪) ⊗_𝒪 L ⟶ 𝒪` is an
> isomorphism.
>
> The dual is a left dual of `L` by `exactPairingDualSheafOfIsInvertible`, and the evaluation of an
> exact pairing is an isomorphism whenever tensoring on the right by the first object is an
> equivalence, which for an invertible sheaf of modules it is.
>
> A ringed space is a ringed site, so this is also the evaluation clause of Tag 01CT (2); see
> `Stacks.SheafOfModules.isIso_evaluation_of_isInvertible` for that reading.

```lean
theorem isIso_evaluation [IsInvertible 𝒪 h𝒪 L] : IsIso (evaluation 𝒪 h𝒪 L)
```

**`Stacks.SheafOfModules.Invertible.isIso_tensorSheafBraiding_hom_comp_evaluation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L277). The attribute's comment: “evaluation”. References: EGA 0 (5.4.3), “more general”.

> **Stacks Project, Tag 040A (2) and Tag 01CT (2), the evaluation clause in the order the tags
> write it.** The evaluation map `L ⊗_𝒪 SheafHom(L, 𝒪) ⟶ 𝒪` is an isomorphism. It is the canonical
> pairing of `Stacks.SheafOfModules.evaluation`, whose factors come in the order Tag 0FNV writes
> them, preceded by the braiding of the tensor product sheaf, which is what exchanges the two
> factors; in this order it is the trivializing pairing identifying `L^∨` as a tensor inverse of
> `L`.

```lean
theorem isIso_tensorSheafBraiding_hom_comp_evaluation [IsInvertible 𝒪 h𝒪 L] :
    IsIso ((tensorSheafBraiding 𝒪 h𝒪 L (dualSheaf 𝒪 h𝒪 L)).hom ≫ evaluation 𝒪 h𝒪 L)
```

**`Stacks.SheafOfModules.Invertible.isInvertible_dualSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleDualEvaluation.lean#L287). The attribute's comment: “dual_invertible”.

> **Stacks Project, Tag 040A (2) and Tag 01CT (2), the invertibility clause.** The dual
> `L^∨ = SheafHom(L, 𝒪)` of an invertible sheaf of `𝒪`-modules is again invertible: the evaluation
> pairing is an isomorphism `L^∨ ⊗_𝒪 L ≅ 𝒪`, which is Tag 0B8K (2) for `L^∨`.

```lean
theorem isInvertible_dualSheaf [IsInvertible 𝒪 h𝒪 L] :
    IsInvertible 𝒪 h𝒪 (dualSheaf 𝒪 h𝒪 L)
```

**`Stacks.SheafOfModules.tensorProduct_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorInvertible.lean#L474). The attribute's comment: “tensor_invertible”.

> **Stacks Project, Tag 01CT (1), Tag 040A (1).** The tensor product of two invertible sheaves
> of modules is invertible.

```lean
theorem tensorProduct_isInvertible
    (L N : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    [IsInvertible O hO L] [IsInvertible O hO N] :
    IsInvertible O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w}
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat) hO⟩).obj L)).obj N)
```

**`Stacks.SheafOfModules.Invertible.tensorProduct_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Ample/AmpleCriteria.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Ample/AmpleCriteria.lean#L70). The attribute's comment: “tensor_invertible”.

> **Stacks Project, Tag 01CT**, part (1). The tensor product of two invertible sheaves of
> modules is invertible: tensoring by it is the composite of the two tensor functors.

```lean
theorem tensorProduct_isInvertible
    (L N : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O
      hO))
    [IsInvertible O hO L] [IsInvertible O hO N] :
    IsInvertible O hO (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w}
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat) hO⟩).obj L).obj N)
```

## Tag 01CU, a definition

[Tag 01CU](https://stacks.math.columbia.edu/tag/01CU) in the Stacks Project.

**`Stacks.SheafOfModules.TensorPower.tensorPower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPower.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPower.lean#L213).

> The `n`th tensor power of an invertible sheaf of modules `L`, for `n : ℤ`: the image of the
> structure sheaf under the `n`th power of the autoequivalence given by tensoring by `L`.

```lean
noncomputable def tensorPower
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    [(((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w}
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ O (forget₂ CommRingCat RingCat)
        hO⟩).flip.obj L)).IsEquivalence] (n : ℤ) :
    SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)
```

**`Stacks.SheafOfModules.TensorPower.isInvertible_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCoherence.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCoherence.lean#L200). The attribute's comment: “tensor powers are invertible”.

> **Every integer tensor power of an invertible sheaf of modules is invertible.** For
> non-negative exponents this is Tag 01CT (1) and the successor comparison; for negative exponents
> it is the same two inputs read backwards, cancelling the invertible factor `L`.

```lean
theorem isInvertible_tensorPower [IsInvertible O hO L] (n : ℤ) :
    IsInvertible O hO (tensorPower O hO L n)
```

**`Stacks.SheafOfModules.TensorPower.mulIso_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCommutativity.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCommutativity.lean#L461). The attribute's comment: “commutativity of the canonical multiplication”.

> **The commutativity normalisation of Tag 01CU**: the canonical multiplication on the integer
> tensor powers of an invertible sheaf of modules agrees with itself after the symmetry constraint
> of the tensor product sheaf. This was the last of the four normalisations of Tag 01CU still
> outstanding.

```lean
theorem mulIso_comm (n m p : ℤ) (h : n + m = p) (h' : m + n = p) :
    mulIso O hO L n m p h =
      Stacks.SheafOfModules.tensorSheafBraiding O hO (pow L n) (pow L m) ≪≫
        mulIso O hO L m n p h'
```

**`Stacks.SheafOfModules.TensorPower.tensorPowerCoherence_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCommutativity.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCommutativity.lean#L595). The attribute's comment: “canonical multiplication and coherence”. References: EGA 0 (5.4.4), “partial”.

> **The canonical multiplication on the integer tensor powers of an invertible sheaf of modules
> exists and satisfies every normalisation asserted by Tag 01CU**: the two unit constraints, the
> degree-`(n, 1)` normalisation by the defining iteration, naturality of that comparison,
> associativity against the associativity constraint of the tensor product sheaf, and commutativity
> against its symmetry constraint.
>
> The multiplication is transported from `Stacks.MonoidalCategory.mul` by
> `Stacks.MonoidalCategory.nonempty_powCoherence`, which is what absorbs the fact that the tensor
> powers of Tag 01CU are built from `(Stacks.SheafOfModules.Tensor.sheafTensor _).flip.obj L` while
> the multiplication is built from `tensorRight`: the two functors are equal but their chosen
> quasi-inverses, used by the negative exponents, have no common normal form.

```lean
theorem tensorPowerCoherence_exists : Nonempty (TensorPowerCoherence O hO L)
```

**`Stacks.SheafOfModules.TensorPower.braidingScalar_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerConstraints.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerConstraints.lean#L344). The attribute's comment: “commutativity constraint”.

> The braiding scalar of the tensor powers of an invertible sheaf of modules is the identity,
> in every degree.

```lean
theorem braidingScalar_eq_id (n : ℤ) : braidingScalar O hO L n = 𝟙 _
```

**`Stacks.SheafOfModules.TensorPower.mulIso_zero_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerInteger.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerInteger.lean#L738). The attribute's comment: “left unit normalisation of the canonical multiplication”.

> **Multiplication by the zeroth tensor power on the left is the left unit constraint of the
> tensor product sheaf.**

```lean
theorem mulIso_zero_left (n : ℤ) (h : 0 + n = n) :
    mulIso O hO L 0 n n h = Stacks.SheafOfModules.tensorSheafLeftUnitor O hO (pow L n)
```

**`Stacks.SheafOfModules.TensorPower.mulIso_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerInteger.lean, line 767](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerInteger.lean#L767). The attribute's comment: “associativity of the canonical multiplication”.

> **Associativity of the canonical multiplication, against the associativity constraint of the
> tensor product sheaf.**

```lean
theorem mulIso_assoc (n m k p t s : ℤ) (h₁ : n + m = p) (h₂ : m + k = t) (h₃ : p + k = s) :
    tensorSheafMapIso O hO (mulIso O hO L n m p h₁) (Iso.refl (pow L k)) ≪≫
        mulIso O hO L p k s h₃ =
      Stacks.SheafOfModules.tensorSheafAssociator O hO (pow L n) (pow L m) (pow L k) ≪≫
        tensorSheafMapIso O hO (Iso.refl (pow L n)) (mulIso O hO L m k t h₂) ≪≫
          mulIso O hO L n t s (by omega)
```

**`Stacks.SheafOfModules.TensorPower.tensorPowerMulIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerMultiplication.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerMultiplication.lean#L339). The attribute's comment: “canonical multiplication”.

> The canonical multiplication isomorphism `L^{⊗ n} ⊗_O L^{⊗ m} ≅ L^{⊗ (n + m)}`, the addition
> law `CategoryTheory.Equivalence.powAdd` for the powers of `- ⊗ L` applied to the structure sheaf,
> read through `powFunctorIsoTensorRight`.

```lean
noncomputable def tensorPowerMulIso (n m : ℤ) :
    (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ (O) (forget₂
      CommRingCat RingCat) (hO)⟩).obj ((tensorPower O hO L n))).obj ((tensorPower
      O hO L m))) ≅
      tensorPower O hO L (n + m)
```

**`Stacks.SheafOfModules.Invertible.tensorPower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/TensorPower.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/TensorPower.lean#L156).

> **Stacks Project, Tag 01CU.** The `n`th tensor power `L^{⊗ n}` of an invertible sheaf `L`,
> for `n` an arbitrary integer: the image of the structure sheaf under the `n`th power of the
> right-tensor autoequivalence.

```lean
noncomputable def tensorPower
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    [IsInvertible O hO L] (n : ℤ) :
    SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)
```

**`Stacks.SelfBraidingInvertible.braidingScalar_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SelfBraidingInvertible/TensorPowerScalar.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SelfBraidingInvertible/TensorPowerScalar.lean#L87). The attribute's comment: “canonical multiplication and coherence”.

> **The braiding scalar of a tensor power of an invertible sheaf of modules is the identity**,
> in every degree. By `Stacks.SheafOfModules.TensorPower.tensorSheafBraiding_self_eq_refl_iff` this
> is the commutativity constraint of Stacks Tag 01CU in degrees `(n, n)`.

```lean
theorem braidingScalar_eq_id (n : ℤ) :
    Stacks.SheafOfModules.TensorPower.braidingScalar 𝒪 h𝒪 L n = 𝟙 _
```

**`AlgebraicGeometry.SheafOfModules.tensorPowAddIso_zero_right_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean#L107). The attribute's comment: “canonical multiplication and coherence”.

> The right unit constraint: multiplication by `L ^⊗ 0` on the right is the right unitor.

```lean
theorem tensorPowAddIso_zero_right_natCast (a : ℕ) :
    tensorPowAddIso 𝒪 h𝒪 L (a : ℤ) ((0 : ℕ) : ℤ) = ρ_ (tensorPow 𝒪 h𝒪 L (a : ℤ))
```

**`AlgebraicGeometry.SheafOfModules.tensorPowAddIso_zero_left_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean#L113). The attribute's comment: “canonical multiplication and coherence”.

> The left unit constraint: multiplication by `L ^⊗ 0` on the left is the left unitor.

```lean
theorem tensorPowAddIso_zero_left_natCast (b : ℕ) :
    tensorPowAddIso 𝒪 h𝒪 L ((0 : ℕ) : ℤ) (b : ℤ) ≪≫
        tensorPowNatCongrIso 𝒪 h𝒪 L (Nat.zero_add b) =
      λ_ (tensorPow 𝒪 h𝒪 L (b : ℤ))
```

**`AlgebraicGeometry.SheafOfModules.tensorPowAddIso_one_right_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean#L126). The attribute's comment: “canonical multiplication and coherence”.

> **The normalisation in degree one.** Multiplication by the first tensor power is
> `AlgebraicGeometry.SheafOfModules.tensorPowOneIso` whiskered into `L ^⊗ a`, followed by the
> successor step `L ^⊗ a ⊗ L = L ^⊗ (a + 1)` of the iteration which defines the powers; in
> nonnegative degree that step is the identity. This is what pins the canonical multiplication
> down: an associative family of multiplication isomorphisms is determined by its degree-`(a, 1)`
> value.

```lean
theorem tensorPowAddIso_one_right_natCast (a : ℕ) :
    tensorPowAddIso 𝒪 h𝒪 L (a : ℤ) ((1 : ℕ) : ℤ) =
      whiskerLeftIso (tensorPow 𝒪 h𝒪 L (a : ℤ)) (tensorPowOneIso 𝒪 h𝒪 L)
```

**`AlgebraicGeometry.SheafOfModules.tensorPowAddIso_assoc_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean#L135). The attribute's comment: “canonical multiplication and coherence”.

> **The associativity constraint on the multiplication of tensor powers**, which Stacks Tag
> 01CU asserts with the formulation omitted, in nonnegative degree and against the associator of
> the monoidal structure on sheaves of modules itself.

```lean
theorem tensorPowAddIso_assoc_natCast (a b c : ℕ) :
    whiskerRightIso (tensorPowAddIso 𝒪 h𝒪 L (a : ℤ) (b : ℤ)) (tensorPow 𝒪 h𝒪 L (c : ℤ)) ≪≫
        tensorPowAddIso 𝒪 h𝒪 L ((a + b : ℕ) : ℤ) (c : ℤ) =
      α_ (tensorPow 𝒪 h𝒪 L (a : ℤ)) (tensorPow 𝒪 h𝒪 L (b : ℤ)) (tensorPow 𝒪 h𝒪 L (c : ℤ)) ≪≫
        whiskerLeftIso (tensorPow 𝒪 h𝒪 L (a : ℤ)) (tensorPowAddIso 𝒪 h𝒪 L (b : ℤ) (c : ℤ)) ≪≫
          tensorPowAddIso 𝒪 h𝒪 L (a : ℤ) ((b + c : ℕ) : ℤ) ≪≫
            tensorPowNatCongrIso 𝒪 h𝒪 L (Nat.add_assoc a b c).symm
```

**`AlgebraicGeometry.SheafOfModules.tensorPowAddIso_comm_natCast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorPowerAssoc/SheafOfModules.lean#L150). The attribute's comment: “canonical multiplication and coherence”.

> **The commutativity constraint on the multiplication of tensor powers**, in nonnegative
> degree.
>
> At degrees `(1, 1)` the constraint *is* the triviality of the self-braiding of `L`, which holds
> for every invertible `L` by the instance `Stacks.SelfBraidingInvertible.hasTrivialSelfBraiding`.

```lean
theorem tensorPowAddIso_comm_natCast (a b : ℕ) :
    β_ (tensorPow 𝒪 h𝒪 L (a : ℤ)) (tensorPow 𝒪 h𝒪 L (b : ℤ)) ≪≫
        tensorPowAddIso 𝒪 h𝒪 L (b : ℤ) (a : ℤ) =
      tensorPowAddIso 𝒪 h𝒪 L (a : ℤ) (b : ℤ) ≪≫
        tensorPowNatCongrIso 𝒪 h𝒪 L (Nat.add_comm a b)
```

**`Stacks.SheafOfModules.Invertible.tensorPowerCoherence_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorPowerCoherence/Basic.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorPowerCoherence/Basic.lean#L225). The attribute's comment: “canonical multiplication and coherence”.

> **Existence of a coherent multiplication on the tensor powers.** The integer tensor powers of
> an invertible sheaf of modules `L` carry coherent multiplication data
> `Stacks.SheafOfModules.Invertible.TensorPowerCoherence O hO L`.

```lean
theorem tensorPowerCoherence_exists
    (L : SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    [_root_.AlgebraicGeometry.SheafOfModules.IsInvertible O hO L] :
    Nonempty (TensorPowerCoherence O hO L)
```

## Tag 01CV, a definition

[Tag 01CV](https://stacks.math.columbia.edu/tag/01CV) in the Stacks Project.

**`Stacks.SheafOfModules.sectionRingStructure_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TwistSectionRing.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TwistSectionRing.lean#L742). The attribute's comment: “graded ring multiplication”.

> There is a graded ring structure on the section ring whose homogeneous product is tensor
> multiplication.

```lean
theorem sectionRingStructure_exists
    (L : SheafOfModules.{w} (TensorSheafification.structureSheaf O hO))
    [IsInvertible O hO L] :
    Nonempty (SectionRingStructure O hO L)
```

**`Stacks.SheafOfModules.sectionModuleStructure_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TwistSectionRing.lean, line 1158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TwistSectionRing.lean#L1158). The attribute's comment: “graded module action”.

> There is a module structure of the section module over the section ring whose action on
> homogeneous terms is tensor multiplication.

```lean
theorem sectionModuleStructure_exists
    (L F : SheafOfModules.{w} (TensorSheafification.structureSheaf O hO))
    [IsInvertible O hO L] :
    Nonempty (SectionModuleStructure O hO L F)
```

**`Stacks.SheafOfModules.Invertible.sectionRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean#L168). The attribute's comment: “underlying graded ring”. References: EGA II (4.5.1), “S = ⊕Γ(X,L^⊗n)”; EGA III (2.1.1), “(2.1.1.1)”; EGA II (2.6.1), “Γ_•(O_X) definition”; EGA 0 (5.4.6), “Γ•(L) carrier”.

> **Stacks Project, Tag 01CV.** The *associated graded ring* `Γ_*(X, L)` of an invertible
> sheaf of modules: the direct sum of the global sections of its non-negative tensor powers. Its
> graded ring structure is `Stacks.SheafOfModules.Invertible.homGradedRing`.

```lean
abbrev sectionRing
```

**`Stacks.SheafOfModules.Invertible.twistedSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean#L181). The attribute's comment: “underlying graded module”. References: EGA 0 (5.4.6), “partial”; EGA II (2.6.1); EGA III (2.1.2), “partial”.

> **Stacks Project, Tag 01CV.** The graded module `Γ_*(X, L, F)` of a sheaf of modules `F`:
> the direct sum, over all integers `n`, of the global sections of the twists `F ⊗ L^{⊗ n}`. Its
> module structure over `Γ_*(X, L)` is
> `Stacks.SheafOfModules.Invertible.twistedSectionsModule`.

```lean
abbrev twistedSections
    (F : _root_.SheafOfModules.{w}
      (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
```

**`Stacks.SheafOfModules.Invertible.twistedSectionsGmodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean#L208). The attribute's comment: “graded module action”.

> **Stacks Project, Tag 01CV.** `Γ_*(X, L, F)` is a `ℤ`-graded module over the `ℕ`-graded
> ring `Γ_*(X, L)`, with the action `twistedSectionsSMul` on homogeneous sections. No
> commutativity of `Γ_*(X, L)` is used.

```lean
noncomputable def twistedSectionsGmodule
    (F : _root_.SheafOfModules.{w}
      (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO)) :
    letI : GradedMonoid.GMonoid (fun n : ℕ =>
        𝟙_ (_root_.SheafOfModules.{w}
          (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
            ⟶ tensorPower O hO L (n : ℤ)) := (tensorPowerSystem O hO L).gradedMonoid
    DirectSum.Gmodule
      (fun n : ℕ => 𝟙_ (_root_.SheafOfModules.{w}
        (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
          ⟶ tensorPower O hO L (n : ℤ))
      (fun n : ℤ => 𝟙_ (_root_.SheafOfModules.{w}
        (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
          ⟶ twist O hO L F n)
```

**`Stacks.SheafOfModules.Invertible.homGradedCommRingOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GradedSectionRing/Commutativity.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GradedSectionRing/Commutativity.lean#L313). The attribute's comment: “associated graded ring”. References: EGA II (4.5.1), “S = ⊕Γ(X,L^⊗n)”; EGA III (2.1.1), “(2.1.1.1)”; EGA II (2.6.1), “graded ring Γ_•(O_X)”; EGA 0 (5.4.6), “graded ring Γ•(L)”.

> **Stacks Project, Tag 01CV: the associated graded ring
> `Γ_*(X, L) = ⨁_{n ≥ 0} Γ(X, L^{⊗ n})` of an invertible sheaf of modules.** This is the
> commutative graded ring on the morphism groups `𝟙 ⟶ L^{⊗ n}`, with the commutativity constraint
> of Tag 01CU discharged by `tensorPowerMulIso_comm` above, so it is unconditional.
>
> The direct sum itself needs no declaration of ours: Mathlib's `DirectSum.commRing` turns a
> `DirectSum.GCommRing` on the family into a commutative ring on `⨁ n : ℕ, (𝟙 ⟶ L^{⊗ n})`, the
> tensor unit *is* the structure sheaf on the nose (`Stacks.SheafOfModules.tensorUnit_eq`) so the
> summands are the global sections the tag names, and
> `Stacks.SheafOfModules.Invertible.homToSection_sectionMul` identifies the multiplication with
> the one already defined on `PresheafOfModules.sections`. This declaration alone is therefore the
> covering set of the tag's first displayed object; the tag's second one, the `ℤ`-graded module
> `Γ_*(X, L, F)`, is not claimed — see the implementation notes.

```lean
noncomputable def homGradedCommRingOfInvertible :
    DirectSum.GCommRing (fun n : ℕ =>
      (𝟙_ (_root_.SheafOfModules.{w} (Stacks.SheafOfModules.TensorSheafification.structureSheaf O
        hO))
        ⟶ tensorPower O hO L (n : ℤ)))
```

**`Stacks.SectionRingProjTheta.sectionRingAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/SectionRingComparison.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/SectionRingComparison.lean#L147). The attribute's comment: “the repository's two realisations of the graded ring `Γ_*(X, L)` — the `Stacks.GradedSections.sectionRing` one on morphisms out of the monoidal unit and the `Stacks.SheafOfModules.sectionRing` one on honest global sections — have the same carrier, ADDITIVELY and degree by degree, and the grading corresponds (`map_summand_eq_sectionRingGrading`). The two MULTIPLICATIONS are not identified BY THIS DECLARATION, which is an `AddEquiv` and nothing more; they ARE identified, by `Stacks.SectionRingProjTheta.sectionRingEquiv` in `StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/SectionRingMultiplicative.lean`, which is this map with its multiplicativity supplied”.

> **The two section rings of an invertible sheaf of modules have the same carrier.**
>
> Degree by degree this is `powSectionsAddEquiv`: a morphism out of the monoidal unit into the
> `natTensorPow` spelling of `L^{⊗ n}` against an honest section over `⊤_ C` of the `tensorPower`
> spelling.

```lean
def sectionRingAddEquiv :
    Stacks.GradedSections.sectionRing L ≃+ Stacks.SheafOfModules.sectionRing 𝒪 h𝒪 L
```

**`Stacks.SectionRingProjTheta.sectionRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/SectionRingMultiplicative.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionRingProjTheta/SectionRingMultiplicative.lean#L260). The attribute's comment: “the repository's two realisations of the graded ring `Γ_*(X, L)` — the `Stacks.GradedSections.sectionRing` one on morphisms out of the monoidal unit and the `Stacks.SheafOfModules.sectionRing` one on honest global sections — are isomorphic as RINGS, and the isomorphism is graded (`sectionGradedRingHom`)”.

> **The two section rings of an invertible sheaf of modules are isomorphic as rings.** This is
> `Stacks.SectionRingProjTheta.sectionRingAddEquiv` with its multiplicativity supplied; the
> underlying function is unchanged, so every computation rule of that additive isomorphism applies
> verbatim.

```lean
def sectionRingEquiv :
    Stacks.GradedSections.sectionRing L ≃+* Stacks.SheafOfModules.sectionRing 𝒪 h𝒪 L
```

**`Stacks.SheafOfModules.sectionRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/SectionRing.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/SectionRing.lean#L113). The attribute's comment: “underlying graded ring”. References: EGA II (4.5.1), “partial”.

> **Stacks Project, Tag 01CV.** The section ring of an invertible sheaf `L`: the direct sum of
> the global sections of the nonnegative tensor powers of `L`.

```lean
abbrev sectionRing (L : SheafOfModules.{w} (TensorSheafification.structureSheaf O hO))
    [IsInvertible O hO L] : Type _
```

**`Stacks.SheafOfModules.sectionModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/SectionRing.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/InvertibleAndOperators/SectionRing.lean#L121). The attribute's comment: “underlying graded module”.

> **Stacks Project, Tag 01CV.** The section module of a sheaf of modules `F`: the direct sum of
> the global sections of all the twists of `F` by integer tensor powers of an invertible sheaf
> `L`.

```lean
abbrev sectionModule (L F : SheafOfModules.{w} (TensorSheafification.structureSheaf O hO))
    [IsInvertible O hO L] : Type _
```

Declarations registered for the tag:

- [`Stacks.SheafOfModules.Invertible.homGradedRing`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GradedSectionRing/Ring.lean#L240), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/InvertibleSections/TwistedSections.lean#L241) (StacksFrontier): “graded ring multiplication”.

## Tag 01CW, a lemma

[Tag 01CW](https://stacks.math.columbia.edu/tag/01CW) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.essentiallySmall_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRingedSpaceEssentiallySmall.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRingedSpaceEssentiallySmall.lean#L107).

> **Stacks Project, Tag 01CW.** The invertible sheaves of modules over the structure sheaf of
> a ringed space have only a set of isomorphism classes: there is a set of invertible modules, of
> size `max u w`, meeting every isomorphism class of invertible modules on the space.

```lean
theorem essentiallySmall_isInvertible (X : RingedSpace.{u, w}) :
    ObjectProperty.EssentiallySmall.{max u w}
      (AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
        (Presheaf.isSheaf_comp_of_isSheaf _ X.presheaf
          (forget₂ CommRingCat.{u} RingCat.{u}) X.IsSheaf))
```

**`AlgebraicGeometry.SheafOfModules.exists_unique_representative_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRingedSpaceEssentiallySmall.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleRingedSpaceEssentiallySmall.lean#L180). The attribute's comment: “exactly one representative”.

> **Stacks Project, Tag 01CW.** There is a family of invertible modules over the structure
> sheaf of a ringed space, indexed by a type of size `max u w`, whose members are pairwise
> non-isomorphic and such that every invertible module on the space is isomorphic to the member of
> exactly one index.

```lean
theorem exists_unique_representative_isInvertible (X : RingedSpace.{u, w}) :
    ∃ (I : Type (max u w)) (L : I → _root_.SheafOfModules.{u}
        (Stacks.SheafOfModules.TensorSheafification.structureSheaf X.presheaf
          (Presheaf.isSheaf_comp_of_isSheaf _ X.presheaf
            (forget₂ CommRingCat.{u} RingCat.{u}) X.IsSheaf))),
      (∀ i, AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
          (Presheaf.isSheaf_comp_of_isSheaf _ X.presheaf
            (forget₂ CommRingCat.{u} RingCat.{u}) X.IsSheaf) (L i)) ∧
      (∀ i j, Nonempty (L i ≅ L j) → i = j) ∧
      ∀ M, AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
          (Presheaf.isSheaf_comp_of_isSheaf _ X.presheaf
            (forget₂ CommRingCat.{u} RingCat.{u}) X.IsSheaf) M →
        ∃! i, Nonempty (M ≅ L i)
```

## Tag 01CX, a definition

[Tag 01CX](https://stacks.math.columbia.edu/tag/01CX) in the Stacks Project.

**`Stacks.SheafOfModules.Picard.PicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L170). The attribute's comment: “the Picard group”. References: EGA IV (21.3.2), “Pic(X) definition”; SGA 6 X (5.1), “Pic(X) definition”.

> The Picard group of `O`: the group of isomorphism classes of
> invertible sheaves of `O`-modules, as a small type.

```lean
noncomputable def PicardGroup : Type (max (max u v) w)
```

**`Stacks.SheafOfModules.Picard.instAddCommGroupPicardGroup`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L176). The attribute's comment: “abelian group structure”.

> The abelian group structure on the Picard group; its addition is the tensor product sheaf,
> by `classOf_tensor`.

```lean
noncomputable instance instAddCommGroupPicardGroup : AddCommGroup (PicardGroup O hO)
```

**`Stacks.SheafOfModules.Picard.classOf_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Picard.lean#L211). The attribute's comment: “addition is tensor product”.

> Addition in the Picard group is the tensor product sheaf.

```lean
theorem classOf_tensor (L N : SheafOfModules.{w}
  (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    (hL : IsInvertible O hO L) (hN : IsInvertible O hO N)
    (hLN : IsInvertible O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ (O) (forget₂ CommRingCat RingCat) (hO)⟩).obj
        (L)).obj (N)))) :
    classOf O hO L hL + classOf O hO N hN =
      classOf O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ (O) (forget₂ CommRingCat RingCat) (hO)⟩).obj
          (L)).obj (N))) hLN
```

**`Stacks.SheafOfModules.PicardGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardGroup/Basic.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardGroup/Basic.lean#L269). The attribute's comment: “the Picard group”. References: EGA IV (21.3.2), “Pic(X) definition”; SGA 6 X (5.1), “Pic(X) definition”.

> The *Picard group* of a sheaf of rings `O` on a site: the abelian group whose elements are
> the isomorphism classes of invertible sheaves of `O`-modules and whose addition is the tensor
> product.

```lean
noncomputable def PicardGroup : Type _
```

**`Stacks.SheafOfModules.instAddCommGroupPicardGroup`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardGroup/Basic.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardGroup/Basic.lean#L275). The attribute's comment: “abelian group structure”. References: EGA IV (21.3.2), “Pic(X) comm. group”.

> The addition of the Picard group, induced by the tensor product of invertible sheaves of
> modules.

```lean
noncomputable instance instAddCommGroupPicardGroup : AddCommGroup (PicardGroup O hO)
```

**`Stacks.SheafOfModules.picardClass_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardGroup/Basic.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardGroup/Basic.lean#L319). The attribute's comment: “addition is tensor product”. References: EGA IV (21.3.2), “cl(L)cl(L')=cl(L⊗L')”.

> Addition in the Picard group is the tensor product.

```lean
theorem picardClass_tensorSheaf (L N : SheafOfModules.{w}
  (Stacks.SheafOfModules.TensorSheafification.structureSheaf O hO))
    (hL : IsInvertible O hO L) (hN : IsInvertible O hO N)
    (hLN : IsInvertible O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ (O) (forget₂ CommRingCat RingCat) (hO)⟩).obj
        (L)).obj (N)))) :
    picardClass O hO L hL + picardClass O hO N hN =
      picardClass O hO ((((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨O, Presheaf.isSheaf_of_isSheaf_comp _ (O) (forget₂ CommRingCat RingCat) (hO)⟩).obj
          (L)).obj (N))) hLN
```

**`Stacks.SheafPicardGroup.PicardGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L182). The attribute's comment: “the Picard group”.

> **The Picard group of `𝒪`**, Stacks Tag 01CX: the isomorphism classes of *invertible*
> sheaves of `𝒪`-modules, with multiplication induced by tensor product. It is realised as the
> group of units of the monoid `ClassMonoid 𝒪 h𝒪` of all isomorphism classes; that these units
> are exactly the invertible sheaves is `isInvertible_iff_isUnit`, and that every one of them is
> the class of such a sheaf is `exists_classOf`.

```lean
abbrev PicardGroup : Type _
```

**`Stacks.SheafPicardGroup.commGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L190). The attribute's comment: “abelian group structure”.

> **The Picard group is an abelian group**, Stacks Tag 01CX. The structure is
> `Units.instCommGroup` over `instCommMonoid`: no coherence law is proved by hand, because the
> skeleton of a braided monoidal category is already a commutative monoid. The additive reading
> the source sometimes uses is `Additive (PicardGroup 𝒪 h𝒪)`, and
> `instAddCommGroupAdditivePicardGroup` records it.

```lean
noncomputable def commGroup : CommGroup (PicardGroup 𝒪 h𝒪)
```

**`Stacks.SheafPicardGroup.instAddCommGroupAdditivePicardGroup`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L195). The attribute's comment: “abelian group structure”.

> **The Picard group, written additively**, as Stacks Tag 01CX sometimes does.

```lean
noncomputable instance instAddCommGroupAdditivePicardGroup :
    AddCommGroup (Additive (PicardGroup 𝒪 h𝒪))
```

**`Stacks.SheafPicardGroup.exists_classOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L238). The attribute's comment: “the Picard group”.

> **Every element of the Picard group is the class of an invertible sheaf of modules**, so
> `classOf` is onto.

```lean
theorem exists_classOf (x : PicardGroup 𝒪 h𝒪) :
    ∃ (M : _root_.SheafOfModules.{w} (structureSheaf 𝒪 h𝒪)) (_ : IsInvertible 𝒪 h𝒪 M),
      classOf 𝒪 h𝒪 M = x
```

**`Stacks.SheafPicardGroup.classOf_eq_classOf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L250). The attribute's comment: “the Picard group”.

> **Two invertible sheaves have the same Picard class exactly when they are isomorphic.**

```lean
theorem classOf_eq_classOf_iff [IsInvertible 𝒪 h𝒪 L] [IsInvertible 𝒪 h𝒪 N] :
    classOf 𝒪 h𝒪 L = classOf 𝒪 h𝒪 N ↔ Nonempty (L ≅ N)
```

**`Stacks.SheafPicardGroup.classOf_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L257). The attribute's comment: “addition is tensor product”.

> **Multiplication in the Picard group is tensor product**, Stacks Tag 01CX.

```lean
theorem classOf_mul [IsInvertible 𝒪 h𝒪 L] [IsInvertible 𝒪 h𝒪 N] :
    classOf 𝒪 h𝒪 (L ⊗ N) = classOf 𝒪 h𝒪 L * classOf 𝒪 h𝒪 N
```

**`Stacks.SheafPicardGroup.classOf_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L264). The attribute's comment: “addition is tensor product”.

> **Multiplication in the Picard group is the tensor product sheaf**, Stacks Tag 01CX in the
> spelling whose statement mentions no monoidal structure.

```lean
theorem classOf_tensorSheaf [IsInvertible 𝒪 h𝒪 L] [IsInvertible 𝒪 h𝒪 N]
    [IsInvertible 𝒪 h𝒪 ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨𝒪, Presheaf.isSheaf_of_isSheaf_comp _ (𝒪) (forget₂ CommRingCat RingCat) (h𝒪)⟩).obj (L)).obj
      (N)))] :
    classOf 𝒪 h𝒪 ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨𝒪, Presheaf.isSheaf_of_isSheaf_comp _ (𝒪) (forget₂ CommRingCat RingCat) (h𝒪)⟩).obj (L)).obj
      (N))) = classOf 𝒪 h𝒪 L * classOf 𝒪 h𝒪 N
```

**`Stacks.SheafPicardGroup.classOf_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L276). The attribute's comment: “abelian group structure”.

> **The neutral element of the Picard group is the class of the structure sheaf**, Stacks
> Tag 01CX.

```lean
theorem classOf_unit :
    classOf 𝒪 h𝒪 (_root_.SheafOfModules.unit (structureSheaf 𝒪 h𝒪)) = 1
```

**`Stacks.SheafPicardGroup.classOf_tensorInv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L283). The attribute's comment: “abelian group structure”.

> **The inverse of a Picard class is the class of the inverse sheaf**, Stacks Tag 01CT (2)
> read in the Picard group of Stacks Tag 01CX.

```lean
theorem classOf_tensorInv [IsInvertible 𝒪 h𝒪 L] :
    classOf 𝒪 h𝒪 (tensorInv 𝒪 h𝒪 L) = (classOf 𝒪 h𝒪 L)⁻¹
```

**`Stacks.SheafPicardGroup.classOf_tensorPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Basic.lean#L316). The attribute's comment: “addition is tensor product”.

> **The class of the `n`-th tensor power is the `n`-th power of the class**, for every
> integer `n`. The powers are the integer tensor powers of Stacks Tag 01CU; this is the sense in
> which the Picard group records them.

```lean
theorem classOf_tensorPow [IsInvertible 𝒪 h𝒪 L] (n : ℤ) :
    classOf 𝒪 h𝒪 (tensorPow 𝒪 h𝒪 L n) = classOf 𝒪 h𝒪 L ^ n
```

**`Stacks.SheafPicardGroup.schemePicardGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Scheme.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Scheme.lean#L59). The attribute's comment: “the Picard group”. References: EGA 0 (5.4.7), “special case”; EGA IV (21.3.2); SGA 4 IX (3.3); SGA 4½ Arcata (2.2.3); SGA 6 X (5.1), “special case”.

> **The Picard group `Pic X` of a scheme**: the isomorphism classes of invertible
> `𝒪_X`-modules under tensor product.

```lean
noncomputable abbrev schemePicardGroup : Type (u + 1)
```

**`Stacks.SheafPicardGroup.schemeClassOf_eq_schemeClassOf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Scheme.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Scheme.lean#L71). The attribute's comment: “the Picard group”. References: EGA IV (21.3.2), “partial”.

> **Two invertible `𝒪_X`-modules have the same Picard class exactly when they are
> isomorphic.**

```lean
theorem schemeClassOf_eq_schemeClassOf_iff (L N : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] [Stacks.Ample.IsInvertibleModule X N] :
    schemeClassOf X L = schemeClassOf X N ↔ Nonempty (L ≅ N)
```

**`Stacks.SheafPicardGroup.schemeClassOf_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Scheme.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SheafPicardGroup/Scheme.lean#L78). The attribute's comment: “addition is tensor product”.

> **Multiplication in `Pic X` is tensor product.**

```lean
theorem schemeClassOf_tensorSheaf (L N : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] [Stacks.Ample.IsInvertibleModule X N]
    [Stacks.Ample.IsInvertibleModule X
      ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf,
        Presheaf.isSheaf_of_isSheaf_comp _ (X.presheaf) (forget₂ CommRingCat RingCat)
          ((Stacks.SheafInternalHom.isSheaf_structureRingPresheaf X))⟩).obj (L)).obj (N)))] :
    schemeClassOf X
        ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf,
          Presheaf.isSheaf_of_isSheaf_comp _ (X.presheaf) (forget₂ CommRingCat RingCat)
            ((Stacks.SheafInternalHom.isSheaf_structureRingPresheaf X))⟩).obj (L)).obj (N))) =
      schemeClassOf X L * schemeClassOf X N
```

**`Stacks.WeilCohomology.picardClassOf_tensorObjRingedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/InvertibleTensor.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/InvertibleTensor.lean#L68). The attribute's comment: “addition in `Pic(X)` is the tensor product, read at the spelling of the tensor product that the Grothendieck ring of Tag 0FDK multiplies with”.

> **Stacks Tag 01CX, addition in `Pic(X)` is the tensor product**, at the spelling of the
> tensor product that `K₀(Vect(X))` multiplies with.

```lean
theorem picardClassOf_tensorObjRingedSpace {X : Scheme.{u}} (L N : X.Modules)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L)
    (hN : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 N)
    (hLN : AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2
      (Scheme.Modules.tensorObjRingedSpace X L N)) :
    picardClassOf X (Scheme.Modules.tensorObjRingedSpace X L N) hLN =
      picardClassOf X L hL + picardClassOf X N hN
```

## Tag 01CY, a lemma

[Tag 01CY](https://stacks.math.columbia.edu/tag/01CY) in the Stacks Project.

**`Stacks.SheafOfModules.isOpen_nonvanishingLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FinitePresentationStalk.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FinitePresentationStalk.lean#L461). The attribute's comment: “openness”. References: EGA 0 (5.5.2).

> **Stacks Project, Tag 01CY** (openness). For an invertible sheaf of modules on a ringed
> space all of whose stalks are local rings, the nonvanishing locus of a global section is
> open.

```lean
theorem isOpen_nonvanishingLocus
    (L : SheafOfModules.{u} (structureSheafRing X))
    [IsInvertible X.presheaf (structureSheafRing X).property L] (s : L.sections) :
    IsOpen (nonvanishingLocus L s)
```

**`Stacks.SheafOfModules.exists_tensorPairing_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleTrivialization.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InvertibleTrivialization.lean#L298). The attribute's comment: “inverse section”.

> **Stacks Project, Tag 01CY** (inverse section). Let `L` be an invertible sheaf of modules on a
> ringed space with local stalks, let `N` be a sheaf of modules with a trivialization
> `ψ : L ⊗ N ≅ O_X`, and let `s` be a global section of `L`. Then over the nonvanishing open `X_s`
> there is a section `b` of `N` with `ψ (s ⊗ b) = 1`.
>
> Stacks states this for `N = L^{⊗ -1}`; see the implementation notes.

```lean
theorem exists_tensorPairing_eq_one
    [IsInvertible X.presheaf (structureSheafRing X).property L] (s : L.sections) :
    ∃ b : N.val.obj (op (nonvanishingOpen L s)),
      tensorPairing ψ (nonvanishingOpen L s) (s.eval (op (nonvanishingOpen L s))) b
        = unitSection X (nonvanishingOpen L s)
```

**`Stacks.InverseSection.exists_tensorInv_section_pairing_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InverseSection/Basic.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InverseSection/Basic.lean#L559). The attribute's comment: “inverse section”. References: EGA 0 (5.5.2), “(b) => (c)”.

> **Stacks Tag 01CY, the inverse-section clause**, in the shape of the tagged statement: on the
> nonvanishing open of a global section `s` of an invertible module, there is a section `t` of the
> `(-1)`-st tensor power whose canonical tensor-power pairing with `s` evaluates to `1`.
>
> The pairing is the one the tagged statement names: form the elementary tensor of `s`, read in the first
> tensor power, with `t`; push it into the sheafified tensor product; apply the addition
> isomorphism of Stacks Tag 01CU in degrees `1` and `-1`; reindex along `1 + (-1) = 0`. The tagged
> statement then compares the result with `1` directly, its zeroth tensor power being the unit of
> `SheafOfModules` on the nose; here the zeroth tensor power is the *sheafified* unit, so
> `AlgebraicGeometry.SheafOfModules.tensorPowZeroIso` is inserted, and only then is the comparison
> with `1 : 𝒪_X(X_s)` a statement.

```lean
theorem exists_tensorInv_section_pairing_eq_one (s : L.sections) :
    ∃ t : (tensorPow X.sheaf.obj (structureSheaf X.sheaf).property L (-1)).val.obj
        (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s)),
      (tensorPowZeroIso X.sheaf.obj (structureSheaf X.sheaf).property L).hom.val.app
        (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s))
        ((tensorPowReindexIso X.sheaf.obj (structureSheaf X.sheaf).property L
            (show (1 : ℤ) + -1 = 0 by omega)).hom.val.app
          (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s))
          ((tensorPowAddIsoSheaf X.sheaf.obj (structureSheaf X.sheaf).property L
              1 (-1)).hom.val.app
            (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s))
            ((toSheafify X.sheaf.obj (structureSheaf X.sheaf).property
                ((PresheafOfModules.tensorObj (O := X.sheaf.obj) ((powPre L 1))
                  ((powPre L (-1)))))).app
              (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s))
              ((tensorPowOneIso X.sheaf.obj (structureSheaf X.sheaf).property L).inv.val.app
                  (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s))
                  (s.eval (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s)))
                ⊗ₜ[X.presheaf.obj
                    (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s))] t)))) =
      (1 : X.presheaf.obj
        (op (Stacks.NonvanishingTrivialize.nonvanishingOpen X L s)))
```

**`Stacks.SheafOfModules.isIso_over_nonvanishingOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NonvanishingTrivialization/Basic.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NonvanishingTrivialization/Basic.lean#L221). The attribute's comment: “trivialization”.

> **Stacks Project, Tag 01CY** (trivialization). For an invertible sheaf of modules `L` on a
> ringed space all of whose stalks are local rings, and a global section `s` of `L`, the morphism
> `𝒪_X ⟶ L` given by multiplication by `s` restricts to an isomorphism over the nonvanishing
> locus `X_s`.

```lean
theorem isIso_over_nonvanishingOpen (L : SheafOfModules.{u} (structureSheafRing X))
    [IsInvertible X.presheaf (structureSheafRing X).property L] (s : L.sections) :
    IsIso ((L.unitHomEquiv.symm s).over (nonvanishingOpen L s))
```

## Tag 0H78, a remark

[Tag 0H78](https://stacks.math.columbia.edu/tag/0H78) in the Stacks Project.

**`Stacks.NonvanishingPullback.preimage_nonvanishingLocus_lrs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NonvanishingPullback/LocallyRingedSpace.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NonvanishingPullback/LocallyRingedSpace.lean#L97). References: EGA II (4.6.13.1), “more general”.

> **Stacks Tag 0H78.** For a morphism of locally ringed spaces, the inverse image of the
> nonvanishing locus of a global section of a module is the nonvanishing locus of the pulled-back
> section.

```lean
theorem preimage_nonvanishingLocus_lrs (s : L.sections) :
    f.base ⁻¹' Stacks.NonvanishingTrivialize.nonvanishingLocus X.toRingedSpace L s =
      Stacks.NonvanishingTrivialize.nonvanishingLocus Y.toRingedSpace
        ((modulePullback f.toShHom).obj L) (pullbackSections f L s)
```

**`Stacks.SheafOfModules.preimage_nonvanishingLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PullbackSections/Nonvanishing.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PullbackSections/Nonvanishing.lean#L165).

> **Stacks Project, Tag 0H78.** For a morphism `f : Y ⟶ X` of locally ringed spaces and a
> global section `s` of a sheaf of `𝒪_X`-modules `L`, the nonvanishing locus of the pullback of
> `s` is the preimage of the nonvanishing locus of `s`.

```lean
public theorem preimage_nonvanishingLocus (s : L.sections) :
    f.base ⁻¹' nonvanishingLocus (X := X.toRingedSpace) L s =
      nonvanishingLocus (X := Y.toRingedSpace)
        ((modulePullback f.toShHom).obj L) (modulePullbackSection f L s)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.25, Tag 01CR](https://stacks.math.columbia.edu/tag/01CR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
