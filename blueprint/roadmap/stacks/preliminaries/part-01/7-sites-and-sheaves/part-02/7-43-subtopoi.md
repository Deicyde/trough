---
declaration: section
origin: cited
lean: MorphismOfTopoi.IsEmbedding, IsSubtopos, CategoryTheory.Sites.Subtopos.MorphismOfTopoi.isEmbedding_overLocalization_iff_isSubterminal, OpenSubtopos.IsOpenSubtopos, CategoryTheory.Sites.Subtopos.isSubtopos_closedComplement, IsClosedSubtopos, MorphismOfTopoi.IsOpenImmersion, MorphismOfTopoi.IsClosedImmersion
statement: formalized
proof: formalized
---

# 7.43 Subtopoi

Section 7.43 of the Stacks Project, [Tag 08LT](https://stacks.math.columbia.edu/tag/08LT). 8 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08LU, a definition

[Tag 08LU](https://stacks.math.columbia.edu/tag/08LU) in the Stacks Project.

**`MorphismOfTopoi.IsEmbedding`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Embedding.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Embedding.lean#L37). References: SGA 4 IV (9.1.1), “a)”; SGA 4 IV (9.1), “embedding def”.

> **Stacks Project, Definition 7.43.1 (tag 08LU).**
>
> A morphism of topoi `f : E → F` is an *embedding* if its pushforward `f_*` is fully faithful.

```lean
def IsEmbedding (f : MorphismOfTopoi E F) : Prop
```

## Tag 08LV, a definition

[Tag 08LV](https://stacks.math.columbia.edu/tag/08LV) in the Stacks Project.

**`IsSubtopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Defs.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Defs.lean#L50). References: SGA 4 IV (9.1), “subtopos def”; SGA 4 IV (9.1.1), “b)”.

> **Stacks Project, Definition 7.43.2 (tag 08LV).**
>
> A strictly full subcategory `E ⊆ Sh(C, J)`, given by the property `P` of its objects, is a
> *subtopos* if there is an embedding of topoi `f : Sh(D, K) → Sh(C, J)`, for some site
> `(D, K)`, whose pushforward has `E` as its essential image.
>
> Since a subcategory of `Sh(C, J)` cut out by a property of objects is automatically strictly
> full and closed under isomorphisms, no further condition on `P` is imposed; the equality
> `f_*.essImage = P` already forces it.
>
> The site `(D, K)` is quantified over the same universes as `(C, J)`. This is the case that
> occurs in practice — in Stacks 08LY, for instance, `D` is `C` itself carrying a finer
> topology — and it keeps the universe parameters of `IsSubtopos` determined by its
> arguments.

```lean
def IsSubtopos (J : GrothendieckTopology C) (P : ObjectProperty (Sheaf J (Type w))) : Prop
```

## Tag 08LW, a lemma

[Tag 08LW](https://stacks.math.columbia.edu/tag/08LW) in the Stacks Project.

**`CategoryTheory.Sites.Subtopos.MorphismOfTopoi.isEmbedding_overLocalization_iff_isSubterminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Subtopoi.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Subtopoi.lean#L183). The attribute's comment: “The localization j_F : E/F ⟶ E is an embedding of topoi, i.e. E/F is a subtopos of E, if and only if F is a subobject of the final object.”. References: SGA 4 IV (9.2.1), “(9.2.2) is an embedding”; SGA 4 VI (4.1), “open inclusion j”.

> **Stacks 08LW.** Let `E` be a topos and `F` an object of `E` (in the source, a sheaf on a
> site `C`), and let `j_F : E/F ⟶ E` be the localization morphism of Stacks 04GZ, given by a right
> adjoint `p` of `j_F⁻¹ = toOver F`. Then `j_F` is an embedding of topoi — so that `E/F` is the
> subtopos `j_{F,*}(E/F)` of `E` — if and only if `F` is a subobject of the final object of `E`.

```lean
public theorem MorphismOfTopoi.isEmbedding_overLocalization_iff_isSubterminal {E : Type u}
    [Category.{v} E] [CartesianMonoidalCategory E] (F : E) {p : Over F ⥤ E}
    (adj : toOver F ⊣ p) :
    (MorphismOfTopoi.overLocalization F adj).IsEmbedding ↔ IsSubterminal F
```

## Tag 08LX, a definition

[Tag 08LX](https://stacks.math.columbia.edu/tag/08LX) in the Stacks Project.

**`OpenSubtopos.IsOpenSubtopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Open.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Open.lean#L97).

> **Open subtopos.**
>
> A strictly full subcategory `E ⊂ Sh(C)`, modelled as an
> `ObjectProperty (Sheaf J (Type w))` closed under isomorphisms, is an
> *open subtopos* of `Sh(C)` if there exists a subsheaf `F` of the terminal
> sheaf such that `E` is the subtopos `Sh(C)/F`. We capture "`E` is the
> subtopos `Sh(C)/F`" by an equivalence of categories
> `P.FullSubcategory ≌ Over F` compatible with the inclusion `P.ι` into
> `Sh(C)` and the canonical forgetful functor `Over.forget F`.

```lean
def IsOpenSubtopos [Limits.HasTerminal (Sheaf J (Type w))]
    (P : ObjectProperty (Sheaf J (Type w))) : Prop
```

## Tag 08LY, a lemma

[Tag 08LY](https://stacks.math.columbia.edu/tag/08LY) in the Stacks Project.

**`CategoryTheory.Sites.Subtopos.isSubtopos_closedComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Subtopoi.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Subtopoi.lean#L585). The attribute's comment: “The full subcategory of sheaves G with F ⨯ G ⟶ F an isomorphism is a subtopos of Sh(C). Stated for an arbitrary sheaf F, the source's hypothesis that F be a subsheaf of the final object being unused in its proof.”. References: SGA 4 IV (9.3.1), “for any topos and open U”; SGA 4 IV (9.3.4), “partial”; SGA 4 VI (4.1), “partial”.

> **Stacks Project, Lemma 7.43.5 (tag 08LY).** Let `(C, J)` be a site and let `F` be a sheaf
> of sets on it. The strictly full subcategory `closedComplement F` of `Sh(C, J)`, consisting of
> the sheaves `G` for which the projection `F ⨯ G ⟶ F` is an isomorphism, is a subtopos of
> `Sh(C, J)`: it is the essential image of the pushforward of an embedding of topoi.
>
> The source assumes `F` to be a subsheaf of the final object, in which case this closed subtopos
> is complementary to the open subtopos `Sh(C, J)/F` of Stacks 08LW; the hypothesis is not needed,
> as `closedComplement F` depends on `F` only through the objects on which `F` has a section.

```lean
public theorem isSubtopos_closedComplement {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} (F : Sheaf J (Type (max u v))) :
    IsSubtopos J (closedComplement F)
```

## Tag 08LZ, a definition

[Tag 08LZ](https://stacks.math.columbia.edu/tag/08LZ) in the Stacks Project.

**`IsClosedSubtopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Closed.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Closed.lean#L46). References: SGA 4 IV (9.3.1), “closed subtopos defn”; SGA 4 IV (9.3.5), “closed subtopos”.

> **Stacks Project, Definition 7.43.6 (tag 08LZ).**
>
> A strictly full subcategory `E ⊆ Sh(C, J)`, given by the property `P` of its objects, is a
> *closed subtopos* if there is a subsheaf `F` of the final object of `Sh(C, J)` — that is, a
> sheaf `F` whose map to the terminal object is a monomorphism — such that `E` is the subtopos
> `closedComplement F` described in Stacks 08LY.

```lean
def IsClosedSubtopos (J : GrothendieckTopology C) (P : ObjectProperty (Sheaf J (Type w))) :
    Prop
```

## Tag 08M0, a definition

[Tag 08M0](https://stacks.math.columbia.edu/tag/08M0) in the Stacks Project.

**`MorphismOfTopoi.IsOpenImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Immersions.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Immersions.lean#L36). References: SGA 4 IV (9.2.1), “open embedding def”.

> **Stacks Project, Definition 7.43.7(1) (tag 08M0).**
>
> A morphism of topoi `f : Sh(D, K) → Sh(C, J)` is an *open immersion* if it is an embedding and
> the essential image of `f_*` is an open subtopos of `Sh(C, J)`.

```lean
def IsOpenImmersion (f : MorphismOfTopoi (Sheaf K (Type w)) (Sheaf J (Type w))) : Prop
```

**`MorphismOfTopoi.IsClosedImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/Immersions.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/Immersions.lean#L44). References: SGA 4 IV (9.3.5), “closed embedding”.

> **Stacks Project, Definition 7.43.7(2) (tag 08M0).**
>
> A morphism of topoi `f : Sh(D, K) → Sh(C, J)` is a *closed immersion* if it is an embedding and
> the essential image of `f_*` is a closed subtopos of `Sh(C, J)`.

```lean
def IsClosedImmersion (f : MorphismOfTopoi (Sheaf K (Type w)) (Sheaf J (Type w))) : Prop
```

## Tag 08M1, a lemma

[Tag 08M1](https://stacks.math.columbia.edu/tag/08M1) in the Stacks Project.

**`MorphismOfTopoi.IsClosedImmersion.fullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean#L174).

> The pushforward of a closed immersion of topoi is fully faithful. This is the first
> assertion of Stacks 08M1; it already holds for an embedding.

```lean
noncomputable def fullyFaithful (hi : i.IsClosedImmersion) : i.pushforward.FullyFaithful
```

**`MorphismOfTopoi.IsClosedImmersion.preservesColimitsOfShape_walkingParallelPair`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean#L197).

> **Stacks Project, Lemma 7.43.8 (tag 08M1).** The pushforward of a closed immersion of
> topoi commutes with coequalizers.

```lean
lemma preservesColimitsOfShape_walkingParallelPair (hi : i.IsClosedImmersion) :
    PreservesColimitsOfShape WalkingParallelPair i.pushforward
```

**`MorphismOfTopoi.IsClosedImmersion.preservesColimitsOfShape_walkingSpan`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean#L204).

> **Stacks Project, Lemma 7.43.8 (tag 08M1).** The pushforward of a closed immersion of
> topoi commutes with pushouts.

```lean
lemma preservesColimitsOfShape_walkingSpan (hi : i.IsClosedImmersion) :
    PreservesColimitsOfShape WalkingSpan i.pushforward
```

**`MorphismOfTopoi.IsClosedImmersion.preservesEpimorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean#L211).

> **Stacks Project, Lemma 7.43.8 (tag 08M1).** The pushforward of a closed immersion of
> topoi transforms surjections into surjections.

```lean
lemma preservesEpimorphisms (hi : i.IsClosedImmersion) :
    i.pushforward.PreservesEpimorphisms
```

**`MorphismOfTopoi.IsClosedImmersion.reflectsMonomorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean#L221).

> **Stacks Project, Lemma 7.43.8 (tag 08M1).** The pushforward of a closed immersion of
> topoi reflects injections.

```lean
lemma reflectsMonomorphisms (hi : i.IsClosedImmersion) :
    i.pushforward.ReflectsMonomorphisms
```

**`MorphismOfTopoi.IsClosedImmersion.reflectsEpimorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean#L229).

> **Stacks Project, Lemma 7.43.8 (tag 08M1).** The pushforward of a closed immersion of
> topoi reflects surjections.

```lean
lemma reflectsEpimorphisms (hi : i.IsClosedImmersion) :
    i.pushforward.ReflectsEpimorphisms
```

**`MorphismOfTopoi.IsClosedImmersion.reflectsIsomorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Subtopos/ClosedImmersion.lean#L237).

> **Stacks Project, Lemma 7.43.8 (tag 08M1).** The pushforward of a closed immersion of
> topoi reflects bijections.

```lean
lemma reflectsIsomorphisms (hi : i.IsClosedImmersion) :
    i.pushforward.ReflectsIsomorphisms
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.43, Tag 08LT](https://stacks.math.columbia.edu/tag/08LT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
