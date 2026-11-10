---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.BrauerScheme.IsSimilar, Stacks.EtaleCohomology.BrauerScheme.IsAzumaya, Stacks.EtaleCohomology.BrauerScheme.BrauerGroup, Stacks.EtaleCohomology.BrauerScheme.BrauerGroup.mul, Stacks.EtaleCohomology.exists_invertible_tensor_iso_of_endomorphism_algebra_iso, Stacks.EtaleCohomology.BrauerScheme.brauerClass_pow_eq_one_of_rank
statement: formalized
proof: formalized
---

# 59.62 The Brauer group of a scheme

Section 59.62 of the Stacks Project, [Tag 0A2J](https://stacks.math.columbia.edu/tag/0A2J). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A2J, the section

[Tag 0A2J](https://stacks.math.columbia.edu/tag/0A2J) in the Stacks Project.

**`Stacks.EtaleCohomology.BrauerScheme.IsSimilar`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean#L362). The attribute's comment: “the equivalence of Azumaya algebras”.

> **The equivalence of Tag 0A2J.** Two sheaves of `𝒪_S`-algebras `A` and `B` are similar if
> there are finite locally free sheaves of `𝒪_S`-modules `F` and `G` of positive rank at every
> point of `S` with `A ⊗_{𝒪_S} 𝓗om(F,F) ≅ B ⊗_{𝒪_S} 𝓗om(G,G)` as `𝒪_S`-algebras. The Brauer
> group of `S` is the set of equivalence classes of *Azumaya* `𝒪_S`-algebras for this relation,
> with the operation induced by the tensor product.

```lean
def IsSimilar (A B : AlgebraSheaf S) : Prop
```

**`Stacks.EtaleCohomology.BrauerScheme.IsAzumaya`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean#L672). The attribute's comment: “the Azumaya condition”.

> **The Azumaya condition of Tag 0A2J.** A sheaf of `𝒪_S`-algebras is Azumaya if it is étale
> locally a matrix algebra: there is an étale covering `{φ_i : U_i → S}` of `S` and integers
> `d_i ≥ 1` with `φ_i^* A ≅ Mat_{d_i}(𝒪_{U_i})` as `𝒪_{U_i}`-algebras. An
> `AlgebraicGeometry.Scheme.Cover` at `AlgebraicGeometry.Scheme.etalePrecoverage` packages both
> halves of "étale covering": every `𝒰.f i` is étale, and the family is jointly surjective.
>
> The pullback `φ_i^*` of the sheaf of algebras is `algebraPullback`, which transports the
> multiplication along the tensor comparison of Tag 01CD — the map
> `φ^*(A ⊗ B) ⟶ φ^*A ⊗ φ^*B` of `Stacks.RingedSpace.comparison`, see `monoidalModulePullback`.

```lean
def IsAzumaya {S : Scheme.{u}} (A : AlgebraSheaf S) : Prop
```

**`Stacks.EtaleCohomology.BrauerScheme.BrauerGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean#L689). The attribute's comment: “the Brauer group”.

> **The Brauer group of a scheme**, Tag 0A2J: the set of equivalence classes of Azumaya
> `𝒪_S`-algebras for the equivalence of `IsSimilar`. The operation induced by the tensor product
> is `BrauerGroup.mul`.

```lean
def BrauerGroup (S : Scheme.{u}) : Type (u + 1)
```

**`Stacks.EtaleCohomology.BrauerScheme.BrauerGroup.mul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/AlgebraSheaf.lean#L738). The attribute's comment: “the operation of the Brauer group”.

> **The operation of the Brauer group of Tag 0A2J**: the one induced by the tensor product of
> sheaves of algebras. It is well defined because a tensor product of Azumaya algebra sheaves is
> Azumaya (`IsAzumaya.tensor`) and because similarity is compatible with the tensor product
> (`IsSimilar.tensor`).

```lean
def BrauerGroup.mul {S : Scheme.{u}} : BrauerGroup S → BrauerGroup S → BrauerGroup S
```

## Tag 0A2K, a lemma

[Tag 0A2K](https://stacks.math.columbia.edu/tag/0A2K) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_invertible_tensor_iso_of_endomorphism_algebra_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/EndomorphismAlgebra/InvertibleTwist.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/EndomorphismAlgebra/InvertibleTwist.lean#L355).

> An isomorphism of the endomorphism algebra sheaves of two positive-rank vector
> bundles is conjugation by an isomorphism after an invertible twist.

```lean
public theorem exists_invertible_tensor_iso_of_endomorphism_algebra_iso
    (S : Scheme.{u})
    (F G : SheafOfModules.{u} (structureSheaf S.sheaf))
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree (C := Opens S)
      (J := Opens.grothendieckTopology S) F]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree (C := Opens S)
      (J := Opens.grothendieckTopology S) G]
    (hF : ∃ q : SheafOfModules.LocalGeneratorsData F,
      q.IsLocallyFreeData ∧ ∀ i, Nonempty (q.generators i).I)
    (hG : ∃ q : SheafOfModules.LocalGeneratorsData G,
      q.IsLocallyFreeData ∧ ∀ i, Nonempty (q.generators i).I)
    (HFF : SheafHom S.sheaf F F) (HGG : SheafHom S.sheaf G G)
    (α : HFF.obj ≅ HGG.obj)
    (hα_one : ∀ U : Opens S, HGG.sectionsEquiv U
      (α.hom.val.app (op U) ((HFF.sectionsEquiv U).symm (𝟙 (F.over U)))) =
        𝟙 (G.over U))
    (hα_comp : ∀ (U : Opens S) (f g : F.over U ⟶ F.over U),
      HGG.sectionsEquiv U
        (α.hom.val.app (op U) ((HFF.sectionsEquiv U).symm (f ≫ g))) =
      (HGG.sectionsEquiv U
        (α.hom.val.app (op U) ((HFF.sectionsEquiv U).symm f))) ≫
      (HGG.sectionsEquiv U
        (α.hom.val.app (op U) ((HFF.sectionsEquiv U).symm g)))) :
    ∃ L : SheafOfModules.{u} (structureSheaf S.sheaf),
      Stacks.SheafOfModules.IsInvertible S.sheaf.obj (structureSheaf S.sheaf).property L ∧
      ∃ e : (((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨((S.toLocallyRingedSpace.toRingedSpace)).presheaf,
            ((S.toLocallyRingedSpace.toRingedSpace)).IsSheaf⟩).obj (F)).obj (L)) ≅ G,
        ∀ (U : Opens S) (s : HFF.obj.val.obj (op U))
          (f : F.val.obj (op U)) (l : L.val.obj (op U)),
          ((HGG.sectionsEquiv U (α.hom.val.app (op U) s)).val.app
            (op (Over.mk (𝟙 U)))).hom
              ((e.hom.val.app (op U)).hom
                (toTensorSheafSection S.toLocallyRingedSpace.toRingedSpace F L (op U)
                  (f ⊗ₜ[(O S.toLocallyRingedSpace.toRingedSpace).obj (op U)] l))) =
            (e.hom.val.app (op U)).hom
              (toTensorSheafSection S.toLocallyRingedSpace.toRingedSpace F L (op U)
                ((((HFF.sectionsEquiv U s).val.app (op (Over.mk (𝟙 U)))).hom f) ⊗ₜ[
                  (O S.toLocallyRingedSpace.toRingedSpace).obj (op U)] l))
```

## Tag 0A2L, a lemma

[Tag 0A2L](https://stacks.math.columbia.edu/tag/0A2L) in the Stacks Project.

**`Stacks.EtaleCohomology.BrauerScheme.brauerClass_pow_eq_one_of_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/BrauerClassAnnihilated.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BrauerGroupScheme/BrauerClassAnnihilated.lean#L212).

> **The class in `Br(S)` of an Azumaya `𝒪_S`-algebra whose underlying sheaf of modules is
> finite locally free of rank `d ^ 2` is annihilated by `d`.**
>
> This is [Stacks, Tag 0A2L]. The case `d = 0` is `pow_zero`; for `d ≥ 1` the reduction
> `Stacks.EtaleCohomology.BrauerScheme.brauerClass_pow_eq_one_of_isTrivialClass_natTensorPow`
> leaves exactly Saltman's construction,
> `Stacks.EtaleCohomology.BrauerScheme.isTrivialClass_natTensorPow_of_rank`.

```lean
theorem brauerClass_pow_eq_one_of_rank (A : Azumaya S) {d : ℕ}
    (hrank : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank (C := Opens S)
      (J := Opens.grothendieckTopology S) A.1.X (d ^ 2)) :
    brauerClass A ^ d = 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.62, Tag 0A2J](https://stacks.math.columbia.edu/tag/0A2J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
