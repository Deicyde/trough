---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isProper_and_isLocallyQuasiFinite_iff_isProper_and_discreteFibres, AlgebraicGeometry.Space.isProper_iff_universallyClosed_isSeparated_isLocallyOfFiniteType, AlgebraicGeometry.Space.isFinite_of_isProper_of_isLocallyQuasiFinite, AlgebraicGeometry.Space.isProper_and_isLocallyQuasiFinite_of_isFinite, AlgebraicGeometry.Space.isProper_and_discreteFibres_of_isFinite, AlgebraicGeometry.Space.universallyClosed_isSeparated_isLocallyOfFiniteType_and_discreteFibres_of_isFinite, AlgebraicGeometry.Space.isFinite_tfae, AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_isProper
statement: formalized
proof: formalized
---

# 76.35 Applications of Zariski's Main Theorem, I

Section 76.35 of the Stacks Project, [Tag 0F43](https://stacks.math.columbia.edu/tag/0F43). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A4X, a lemma

[Tag 0A4X](https://stacks.math.columbia.edu/tag/0A4X) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_and_isLocallyQuasiFinite_iff_isProper_and_discreteFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean#L253). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 0A4X, conditions (2) and (3).** A proper morphism of algebraic spaces over `S` is
> locally quasi-finite exactly when the point space of its fibre over every field-valued point of
> its target is discrete.
>
> A proper morphism is locally of finite type, and for a morphism locally of finite type the two
> conditions are compared by Stacks 06RW.

```lean
theorem isProper_and_isLocallyQuasiFinite_iff_isProper_and_discreteFibres
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (IsProper B S hS f ∧ IsLocallyQuasiFinite B S hS f) ↔
      (IsProper B S hS f ∧ ∀ p : FieldValuedPoint B S hS Y,
        DiscreteTopology (points B S hS (pullback (yonedaEquiv.symm p.value) f)))
```

**`AlgebraicGeometry.Space.isProper_iff_universallyClosed_isSeparated_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean#L272). The attribute's comment: “conditions (3) and (4)”.

> **Stacks 0A4X, conditions (3) and (4).** A morphism of algebraic spaces over `S` is proper
> exactly when it is universally closed, separated and locally of finite type.
>
> Properness of Stacks 03ZM is separatedness together with being of finite type and universally
> closed, and being of finite type is being locally of finite type together with quasi-compactness;
> quasi-compactness is implied by universal closedness alone, by Stacks 04XW, so it is not an extra
> condition. Conditions (3) and (4) of Stacks 0A4X share their discreteness clause and differ only
> by this comparison.

```lean
theorem isProper_iff_universallyClosed_isSeparated_isLocallyOfFiniteType
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsProper B S hS f ↔
      UniversallyClosed B S hS f ∧ IsSeparated B S hS f ∧ IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.Space.isFinite_of_isProper_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean#L425). The attribute's comment: “condition (2) implies condition (1)”. References: EGA III (4.4.11), “proper q-finite ⇒ finite”; EGA IV (18.12.4), “proper q-finite⇒finite”; EGA III (4.4.2), “c) => a)”.

> **Stacks 0A4X, condition (2) implies condition (1).** A proper, locally quasi-finite
> morphism of algebraic spaces over `S` is finite.
>
> Every point of `|Y|` has an étale neighbourhood over which `f` becomes finite,
> by `AlgebraicGeometry.Space.exists_etale_isFinite_pullback_snd_of_isProper`. Replacing such a
> neighbourhood by the open subspace of `Y` it sweeps out, which receives a surjective étale chart
> from it by Stacks 06NF, finiteness descends along that chart by Stacks 03ZQ; the resulting open
> subspaces cover `|Y|`, indexed by the points of the underlying scheme of an étale atlas of `Y` so
> that the index type has the right size, and finiteness is Zariski-local on the target, again by
> Stacks 03ZQ.

```lean
theorem isFinite_of_isProper_of_isLocallyQuasiFinite
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hp : IsProper B S hS f) (hqf : IsLocallyQuasiFinite B S hS f) :
    IsFinite B S hS f
```

**`AlgebraicGeometry.Space.isProper_and_isLocallyQuasiFinite_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean#L477). The attribute's comment: “condition (1) implies condition (2)”.

> **Stacks 0A4X, condition (1) implies condition (2).** A finite morphism of algebraic spaces
> over `S` is proper and locally quasi-finite.
>
> Properness is the second half of the characterization of finiteness as affineness together with
> properness, Stacks 04NZ, and local quasi-finiteness is the first half of quasi-finiteness of a
> finite morphism, Stacks 04NY.

```lean
theorem isProper_and_isLocallyQuasiFinite_of_isFinite
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsFinite B S hS f) :
    IsProper B S hS f ∧ IsLocallyQuasiFinite B S hS f
```

**`AlgebraicGeometry.Space.isProper_and_discreteFibres_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean#L490). The attribute's comment: “condition (1) implies condition (3)”. References: EGA IV (18.12.4), “finite⇒proper+discrete”; EGA II (6.1.7), “discrete fibres”; EGA III (4.4.2), “a) => c)”.

> **Stacks 0A4X, condition (1) implies condition (3).** A finite morphism of algebraic spaces
> over `S` is proper and the point space of its fibre over every field-valued point of its target
> is discrete.

```lean
theorem isProper_and_discreteFibres_of_isFinite
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsFinite B S hS f) :
    IsProper B S hS f ∧ ∀ p : FieldValuedPoint B S hS Y,
      DiscreteTopology (points B S hS (pullback (yonedaEquiv.symm p.value) f))
```

**`AlgebraicGeometry.Space.universallyClosed_isSeparated_isLocallyOfFiniteType_and_discreteFibres_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean#L502). The attribute's comment: “condition (1) implies condition (4)”.

> **Stacks 0A4X, condition (1) implies condition (4).** A finite morphism of algebraic spaces
> over `S` is universally closed, separated and locally of finite type, and the point space of its
> fibre over every field-valued point of its target is discrete.

```lean
theorem universallyClosed_isSeparated_isLocallyOfFiniteType_and_discreteFibres_of_isFinite
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsFinite B S hS f) :
    UniversallyClosed B S hS f ∧ IsSeparated B S hS f ∧ IsLocallyOfFiniteType B S hS f ∧
      ∀ p : FieldValuedPoint B S hS Y,
        DiscreteTopology (points B S hS (pullback (yonedaEquiv.symm p.value) f))
```

**`AlgebraicGeometry.Space.isFinite_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFiniteTfae.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFiniteTfae.lean#L89). The attribute's comment: “the four conditions collected as a TFAE”. References: EGA IV (18.12.4); EGA III (4.4.11), “proper q-finite ⇒ finite”; EGA III (4.4.2), “a) <=> c)”.

> **Stacks 0A4X**, the four conditions collected as a `List.TFAE`. For a morphism
> `f : X ⟶ Y` of algebraic spaces over `S` the following are equivalent: `f` is finite; `f` is
> proper and locally quasi-finite; `f` is proper and the point space of its fibre over every
> field-valued point of `Y` is discrete; `f` is universally closed, separated and locally of
> finite type, and the point space of its fibre over every field-valued point of `Y` is
> discrete.
>
> The entries are listed in the source's numbering, and each is the proposition the
> corresponding pairwise comparison in
> `StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean` speaks about, from which
> this equivalence is assembled.

```lean
theorem isFinite_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [IsFinite B S hS f,
        IsProper B S hS f ∧ IsLocallyQuasiFinite B S hS f,
        IsProper B S hS f ∧ ∀ p : FieldValuedPoint B S hS Y,
          DiscreteTopology (points B S hS (pullback (yonedaEquiv.symm p.value) f)),
        UniversallyClosed B S hS f ∧ IsSeparated B S hS f ∧ IsLocallyOfFiniteType B S hS f ∧
          ∀ p : FieldValuedPoint B S hS Y,
            DiscreteTopology (points B S hS (pullback (yonedaEquiv.symm p.value) f))]
```

## Tag 0A4Y, a lemma

[Tag 0A4Y](https://stacks.math.columbia.edu/tag/0A4Y) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperQuasiFinite.lean#L530).

> **Stacks 0A4Y.** Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S` and let
> `y` be a point of `|Y|` such that `f` is quasi-finite at every point of `|X|` lying over `y`.
> Then `y` has an open neighbourhood `V ⊆ Y` over which `f` becomes finite, in the sense that the
> base change `f^{-1}(V) ⟶ V` is finite.
>
> The locus in `|X|` where `f` is quasi-finite is open — that is Stacks 04NW, in the point-set
> form of part (1) of Stacks 0ABM — so its
> complement `Z` is closed; `f` is universally closed, hence closed, so the image of `Z` is closed
> in `|Y|`, and the hypothesis at `y` says exactly that `y` is not in that image. Take for `V` the
> open subspace of `Y` with point set the complement of the image of `Z`, which exists by part (1)
> of Stacks 03BZ. The base change `f^{-1}(V) ⟶ V` is proper, and it is locally quasi-finite
> because each of its points maps to a point of `|X|` whose image in `|Y|` avoids the image of
> `Z`, hence lies outside `Z`, and quasi-finiteness at a point transfers to a base change by part
> (2) of Stacks 0ABM. It is therefore finite by Stacks 0A4X.

```lean
theorem exists_isOpenSubspace_isFinite_pullback_snd_of_isProper
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hp : IsProper B S hS f) (y : points B S hS Y)
    (hqf : ∀ x : points B S hS X, pointsMap B S hS X f x = y → IsQuasiFiniteAt B S hS f x) :
    ∃ V : Subfunctor Y, IsOpenSubspace B S hS V ∧
      y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι) ∧
      IsFinite B S hS (pullback.snd f V.ι)
```

## Tag 0AEJ, a lemma

[Tag 0AEJ](https://stacks.math.columbia.edu/tag/0AEJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isClosedSubspace_isFinite_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFiniteImageNearFibre.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFiniteImageNearFibre.lean#L318).

> **Stacks 0AEJ.** Let `h : X ⟶ Y`, `f : X ⟶ T` and `g : Y ⟶ T` be morphisms of algebraic
> spaces over `S` with `h ≫ g = f`, with `f` proper and `g` separated and locally of finite type,
> and let `b ∈ |T|` be represented by a field-valued point `p` with field of definition `k`. If
> the image of `|X_k|` in `|Y_k|` is finite, or if `T` is decent and the image in `|Y|` of the
> set-theoretic fibre of `f` over `b` is finite, then `b` has an open neighbourhood `U ⊆ T` and
> `X ×_T U ⟶ Y ×_T U` factors through a closed subspace of `Y ×_T U` which is finite over `U`.

```lean
theorem exists_isOpenSubspace_isClosedSubspace_isFinite_of_isProper
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hT : IsAlgebraicSpace B S hS T) (h : X ⟶ Y) (f : X ⟶ T) (g : Y ⟶ T)
    (comm : h ≫ g = f) (b : points B S hS T) (p : FieldValuedPoint B S hS T)
    (hp : p.class B S hS T = b) (hf : IsProper B S hS f)
    (hg_sep : IsSeparated B S hS g) (hg_lft : IsLocallyOfFiniteType B S hS g)
    (hfinite :
      Set.Finite (Set.range (pointsMap B S hS (pullback f (fieldMorphism B S hS T p))
        (pullback.map f (fieldMorphism B S hS T p) g (fieldMorphism B S hS T p) h
          (𝟙 _) (𝟙 _) (by simp [comm]) (by simp)))) ∨
      (Set.Finite (pointsMap B S hS X h ''
          {x : points B S hS X | pointsMap B S hS X f x = b}) ∧
        IsDecentSpace B S hS T)) :
    ∃ U : Subfunctor T,
      IsOpenSubspace B S hS U ∧
      b ∈ Set.range (pointsMap B S hS U.toFunctor U.ι) ∧
      ∃ Z : Subfunctor (pullback g U.ι),
        IsClosedSubspace B S hS Z ∧
        (∃ m : pullback f U.ι ⟶ Z.toFunctor, m ≫ Z.ι =
          pullback.map f U.ι g U.ι h (𝟙 _) (𝟙 _) (by simp [comm]) (by simp)) ∧
        IsFinite B S hS (Z.ι ≫ pullback.snd g U.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.35, Tag 0F43](https://stacks.math.columbia.edu/tag/0F43)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
