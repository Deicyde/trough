---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.finite_fieldFiber_iff_quasiFiniteAt_fiber, AlgebraicGeometry.Space.finite_fieldFiber_iff_finite_setFiber_of_decent, AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_finite_fieldFiber, AlgebraicGeometry.Space.isQuasiFiniteAt_of_isFinite_pullback_snd, AlgebraicGeometry.Space.finite_fieldFiber_iff_exists_isOpenSubspace_isFinite_pullback_snd, AlgebraicGeometry.Space.finite_setFibre_iff_finite_fieldFibre_of_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Space.finite_setFibre_of_isFinite_openRestriction, AlgebraicGeometry.Space.finite_fieldFibre_of_isFinite_openRestriction
statement: formalized
proof: formalized
---

# 68.21 Generically finite morphisms

Section 68.21 of the Stacks Project, [Tag 0BBA](https://stacks.math.columbia.edu/tag/0BBA). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ACZ, a lemma

[Tag 0ACZ](https://stacks.math.columbia.edu/tag/0ACZ) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_fieldFiber_iff_quasiFiniteAt_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean#L493). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0ACZ, conditions (1) and (2).** Let `f : X ⟶ Y` be a quasi-separated morphism of
> algebraic spaces over `S` of finite type and let `p` be a field-valued representative of a
> point `y` of `|Y|`. The field fibre `X_k` has finitely many points exactly when `f` is
> quasi-finite at every point of `|X|` above `y`.

```lean
theorem finite_fieldFiber_iff_quasiFiniteAt_fiber (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hqs : IsQuasiSeparated B S hS f)
    (hft : IsFiniteType B S hS f) (y : points B S hS Y)
    (p : FieldValuedPoint B S hS Y) (hp : p.class B S hS Y = y) :
    Set.Finite (Set.univ : Set (points B S hS
        (pullback f (yonedaEquiv.symm p.value)))) ↔
      ∀ x : points B S hS X, pointsMap B S hS X f x = y →
        IsQuasiFiniteAt B S hS f x
```

**`AlgebraicGeometry.Space.finite_fieldFiber_iff_finite_setFiber_of_decent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean#L515). The attribute's comment: “condition (4) for a decent target”.

> **Stacks 0ACZ, condition (4) for a decent target.** Let `f : X ⟶ Y` be a quasi-separated
> morphism of algebraic spaces over `S` of finite type with `Y` a decent algebraic space, and
> let `p` be a field-valued representative of a point `y` of `|Y|`. The field fibre `X_k` has
> finitely many points exactly when the set-theoretic fibre `f^{-1}({y}) ⊂ |X|` is finite.

```lean
theorem finite_fieldFiber_iff_finite_setFiber_of_decent (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hqs : IsQuasiSeparated B S hS f)
    (hft : IsFiniteType B S hS f) (hdecent : IsDecentSpace B S hS Y)
    (y : points B S hS Y) (p : FieldValuedPoint B S hS Y)
    (hp : p.class B S hS Y = y) :
    Set.Finite (Set.univ : Set (points B S hS
        (pullback f (yonedaEquiv.symm p.value)))) ↔
      Set.Finite {x : points B S hS X | pointsMap B S hS X f x = y}
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_finite_fieldFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean, line 1360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean#L1360). The attribute's comment: “conditions (1) and (2) imply condition (3)”.

> **Stacks 0ACZ, conditions (1) and (2) imply condition (3).** Let `f : X ⟶ Y` be a
> quasi-separated morphism of algebraic spaces over `S` of finite type, let `y` be a point of
> `|Y|` whose local ring has dimension zero and let `p` be a field-valued representative of `y`
> with field of definition `k`. If the field fibre `X_k = X ×_Y Spec(k)` has finitely many
> points then there is an open subspace `V ⊂ Y` with `y ∈ |V|` whose base change
> `V ×_Y X ⟶ V` is finite.
>
> An affine étale chart `V ⟶ Y` at `y` may be chosen so that `y` comes from a generic point `v`
> of `V` (Stacks 0BAQ). Over an affine étale atlas `U` of `V ×_Y X` the two morphisms
> `U ⟶ V` and `U ×_{V ×_Y X} U ⟶ V` are quasi-finite above `v` (Stacks 0BBB), so both become
> finite after shrinking `V` to an affine open neighbourhood of `v` (Stacks 02NW). The relation
> being finite over the atlas makes the atlas finite over the shrunk chart, and the chart being
> affine with a finite surjective atlas makes `V ×_Y X` an affine scheme (Stacks 01ZT), over
> which finiteness is properness together with affineness. Descending along the étale chart
> produces the open subspace of `Y`.

```lean
theorem exists_isOpenSubspace_isFinite_pullback_snd_of_finite_fieldFiber
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f)
    (hft : IsFiniteType B S hS f)
    (y : points B S hS Y)
    (p : FieldValuedPoint B S hS Y)
    (hp : p.class B S hS Y = y)
    (hy : localRingDimension B S hS y = 0) :
    Set.Finite (Set.univ : Set (points B S hS
      (pullback f (yonedaEquiv.symm p.value)))) →
    ∃ V : Subfunctor Y,
        IsOpenSubspace B S hS V ∧
        y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι) ∧
        IsFinite B S hS (pullback.snd f V.ι)
```

**`AlgebraicGeometry.Space.isQuasiFiniteAt_of_isFinite_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean, line 1401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean#L1401). The attribute's comment: “condition (3) implies condition (2)”.

> **Stacks 0ACZ, condition (3) implies condition (2).** Let `f : X ⟶ Y` be a morphism of
> algebraic spaces over `S` which is locally of finite type and let `V ⊂ Y` be an open subspace
> containing a point `y` of `|Y|` in its point set. If the base change `V ×_Y X ⟶ V` is finite
> then `f` is quasi-finite at every point of `|X|` above `y`.
>
> A finite morphism is quasi-finite (Stacks 04NY), so `V ×_Y X ⟶ V` is quasi-finite at every
> point of its source; a point of `|X|` above `y` lifts to `|V ×_Y X|` (Stacks 03H4), and
> quasi-finiteness at a point passes to and from a base change (Stacks 0ABM).

```lean
theorem isQuasiFiniteAt_of_isFinite_pullback_snd
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hlft : IsLocallyOfFiniteType B S hS f)
    (y : points B S hS Y)
    (V : Subfunctor Y)
    (hV : IsOpenSubspace B S hS V)
    (hyV : y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι))
    (hfin : IsFinite B S hS (pullback.snd f V.ι))
    (x : points B S hS X)
    (hxy : pointsMap B S hS X f x = y) :
    IsQuasiFiniteAt B S hS f x
```

**`AlgebraicGeometry.Space.finite_fieldFiber_iff_exists_isOpenSubspace_isFinite_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean, line 1439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean#L1439). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 0ACZ, conditions (1) and (3).** Let `f : X ⟶ Y` be a quasi-separated morphism of
> algebraic spaces over `S` of finite type, let `y` be a point of `|Y|` whose local ring has
> dimension zero and let `p` be a field-valued representative of `y`. The field fibre `X_k` has
> finitely many points exactly when there is an open subspace `V ⊂ Y` with `y ∈ |V|` whose base
> change `V ×_Y X ⟶ V` is finite.
>
> Together with `AlgebraicGeometry.Space.finite_fieldFiber_iff_quasiFiniteAt_fiber` this closes
> the equivalence of the source's conditions (1), (2) and (3).

```lean
theorem finite_fieldFiber_iff_exists_isOpenSubspace_isFinite_pullback_snd
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f)
    (hft : IsFiniteType B S hS f)
    (y : points B S hS Y)
    (p : FieldValuedPoint B S hS Y)
    (hp : p.class B S hS Y = y)
    (hy : localRingDimension B S hS y = 0) :
    Set.Finite (Set.univ : Set (points B S hS
        (pullback f (yonedaEquiv.symm p.value)))) ↔
      ∃ V : Subfunctor Y,
        IsOpenSubspace B S hS V ∧
        y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι) ∧
        IsFinite B S hS (pullback.snd f V.ι)
```

## Tag 0AD0, a lemma

[Tag 0AD0](https://stacks.math.columbia.edu/tag/0AD0) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_setFibre_iff_finite_fieldFibre_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean#L161). The attribute's comment: “the equivalence of conditions (1) and (2)”.

> **Stacks 0AD0, the equivalence of conditions (1) and (2).** Let `f : X ⟶ Y` be a
> quasi-separated morphism of algebraic spaces over `S` which is locally of finite type, let `Y`
> be a quasi-separated algebraic space, let `y` be a point of `|Y|` of codimension zero and let
> `p` be a field-valued representative of `y`, with field of definition `k`. Then the
> set-theoretic fibre `f^{-1}({y}) ⊂ |X|` is finite exactly when the point set of the field
> fibre `X_k = X ×_Y Spec(k)` is finite.
>
> Quasi-separatedness of `Y` makes `Y` decent (Stacks 03JX) and quasi-separatedness of `f` then
> makes `X` decent (Stacks 03M5 and Stacks 0ABY), so both implications are instances of the
> comparison of conditions (1) and (4) of Stacks 0ACK for decent source and target: condition (4)
> implies condition (1) because the comparison map `|X_k| → |X|` has image the set-theoretic
> fibre, and the converse is
> `AlgebraicGeometry.Space.finite_univ_points_fieldFibre_of_finite_setFibre_of_isDecent` once the
> fibre is nonempty, an empty fibre leaving `|X_k|` without points by the same surjectivity.
>
> The codimension-zero hypothesis on `y` is the source's; this implication does not use it.

```lean
theorem finite_setFibre_iff_finite_fieldFibre_of_isAbsolutelyQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f) (hft : IsLocallyOfFiniteType B S hS f)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (y : points B S hS Y) (_hy : localRingDimension B S hS y = 0)
    (p : FieldValuedPoint B S hS Y) (hp : p.class B S hS Y = y) :
    {x : points B S hS X | pointsMap B S hS X f x = y}.Finite ↔
      (Set.univ : Set (points B S hS (fieldFibre B S hS f p))).Finite
```

**`AlgebraicGeometry.Space.finite_setFibre_of_isFinite_openRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean#L193). The attribute's comment: “condition (3) implies condition (1)”.

> **Stacks 0AD0, condition (3) implies condition (1).** Let `f : X ⟶ Y` be a morphism of
> presheaves on the big fppf site of `S`, let `y` be a point of `|Y|`, let `U ⊂ X` and `V ⊂ Y`
> be open subspaces and let `g : U ⟶ V` be a morphism whose square with the two inclusions and
> `f` commutes, so that `f` carries `U` into `V` and `g` restricts `f`. If `y` lies in `|V|`, if
> the set-theoretic fibre `f^{-1}({y}) ⊂ |X|` is contained in `|U|` and if `g` is finite, then
> `f^{-1}({y})` is finite.
>
> A finite morphism of algebraic spaces is universally closed with discrete fibres (Stacks 0A4X),
> so each of its set-theoretic fibres is finite. The inclusion `|V| → |Y|` is injective because
> the inclusion of an open subspace is a monomorphism, so the point `v` of `|V|` above `y` is the
> only one, and a point of `|U|` lands on `y` under `f` exactly when it lands on `v` under `g`.
> The fibre `f^{-1}({y})` is therefore the image under `|U| → |X|` of a fibre of `g`.
>
> No hypothesis on `f`, on `Y` or on `y` is needed: the quasi-separatedness, finite type and
> codimension-zero hypotheses of the tag are used only for the other implications.

```lean
theorem finite_setFibre_of_isFinite_openRestriction (f : X ⟶ Y) (y : points B S hS Y)
    (U : Subfunctor X) (V : Subfunctor Y) (g : U.toFunctor ⟶ V.toFunctor)
    (hU : IsOpenSubspace B S hS U) (hV : IsOpenSubspace B S hS V)
    (hcomm : g ≫ V.ι = U.ι ≫ f)
    (hy : y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι))
    (hfib : {x : points B S hS X | pointsMap B S hS X f x = y} ⊆
      Set.range (pointsMap B S hS U.toFunctor U.ι))
    (hg : IsFinite B S hS g) :
    {x : points B S hS X | pointsMap B S hS X f x = y}.Finite
```

**`AlgebraicGeometry.Space.finite_fieldFibre_of_isFinite_openRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean#L231). The attribute's comment: “condition (3) implies condition (2)”.

> **Stacks 0AD0, condition (3) implies condition (2).** In the situation of condition (3) of
> the tag, with `f` in addition quasi-separated and locally of finite type and `Y` a
> quasi-separated algebraic space, the point set of the field fibre `X_k` over a field-valued
> representative `p` of `y` is finite.
>
> The source omits the proof of this implication. It is obtained here by composing
> `AlgebraicGeometry.Space.finite_setFibre_of_isFinite_openRestriction` with the equivalence of
> conditions (1) and (2).

```lean
theorem finite_fieldFibre_of_isFinite_openRestriction (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f) (hft : IsLocallyOfFiniteType B S hS f)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (y : points B S hS Y) (hy0 : localRingDimension B S hS y = 0)
    (p : FieldValuedPoint B S hS Y) (hp : p.class B S hS Y = y)
    (U : Subfunctor X) (V : Subfunctor Y) (g : U.toFunctor ⟶ V.toFunctor)
    (hU : IsOpenSubspace B S hS U) (hV : IsOpenSubspace B S hS V)
    (hcomm : g ≫ V.ι = U.ι ≫ f)
    (hy : y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι))
    (hfib : {x : points B S hS X | pointsMap B S hS X f x = y} ⊆
      Set.range (pointsMap B S hS U.toFunctor U.ι))
    (hg : IsFinite B S hS g) :
    (Set.univ : Set (points B S hS (fieldFibre B S hS f p))).Finite
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_openRestriction_of_finite_setFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteQuasiSeparated.lean#L447). The attribute's comment: “conditions (1) and (2) imply condition (3)”.

> **Stacks 0AD0, conditions (1) and (2) imply condition (3).** Let `f : X ⟶ Y` be a
> quasi-separated morphism of algebraic spaces over `S` which is locally of finite type, let `Y`
> be a quasi-separated algebraic space and let `y` be a point of `|Y|` whose local ring has
> dimension zero. If the set-theoretic fibre `f^{-1}({y}) ⊂ |X|` is finite then there are open
> subspaces `U ⊂ X` and `V ⊂ Y` and a morphism `g : U ⟶ V` restricting `f`, with `y ∈ |V|`,
> with `f^{-1}({y}) ⊂ |U|`, and with `g` finite.
>
> A finite set of points of an algebraic space is covered by a quasi-compact open subspace, so
> `X` may be shrunk to a quasi-compact open `U₀` containing the fibre. Quasi-separatedness of
> `Y` makes the restriction `U₀ ⟶ Y` quasi-compact (Stacks 073B) and hence of finite type, and
> its fibre over `y` is still finite, so the field fibre is finite as well. Condition (3) of
> Stacks 0ACZ then supplies an open `V ⊂ Y` containing `y` over which `U₀` becomes finite, and
> the base change `U₀ ×_Y V` is an open subspace of `X` because `U₀` is.

```lean
theorem exists_isOpenSubspace_isFinite_openRestriction_of_finite_setFibre
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (y : points B S hS Y)
    (hy : localRingDimension B S hS y = 0) :
    Set.Finite {x : points B S hS X |
      pointsMap B S hS X f x = y} →
      ∃ (U : Subfunctor X) (V : Subfunctor Y)
        (g : U.toFunctor ⟶ V.toFunctor),
        IsOpenSubspace B S hS U ∧
        IsOpenSubspace B S hS V ∧
        g ≫ V.ι = U.ι ≫ f ∧
        y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι) ∧
        {x : points B S hS X |
          pointsMap B S hS X f x = y} ⊆
          Set.range (pointsMap B S hS U.toFunctor U.ι) ∧
        IsFinite B S hS g
```

## Tag 0BBB, a lemma

[Tag 0BBB](https://stacks.math.columbia.edu/tag/0BBB) in the Stacks Project.

**`AlgebraicGeometry.Space.quasiFiniteAt_over_codimensionZeroPoint_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFinite.lean#L293).

> **Stacks 0BBB.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` locally of
> finite type and let `y` be a point of `Y` whose local ring has dimension zero. The following
> are equivalent: every point of `X` above `y` has local ring of dimension zero; `f` is
> quasi-finite at every point above `y`; and `f` is quasi-finite at every point above `y` whose
> local ring has dimension zero.

```lean
theorem quasiFiniteAt_over_codimensionZeroPoint_tfae
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (y : points B S hS Y) (hy : localRingDimension B S hS y = 0) :
    List.TFAE [
      ∀ x : points B S hS X, pointsMap B S hS X f x = y →
        localRingDimension B S hS x = 0,
      ∀ x : points B S hS X, pointsMap B S hS X f x = y → IsQuasiFiniteAt B S hS f x,
      ∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        pointsMap B S hS X f x = y → IsQuasiFiniteAt B S hS f x]
```

## Tag 0BBC, a lemma

[Tag 0BBC](https://stacks.math.columbia.edu/tag/0BBC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isDenseOpenSubspace_isFinite_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteOverDenseOpenSubspace.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteOverDenseOpenSubspace.lean#L233).

> **Stacks 0BBC.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, and write `X⁰` and `Y⁰` for the sets of points of `|X|` and `|Y|`
> whose local rings have dimension zero. Assume that `Y` is decent, that `X⁰` and `Y⁰` are
> finite with `f^{-1}(Y⁰) = X⁰`, and that `f` is either quasi-compact or separated. Then there
> is an open subspace `V ⊂ Y` whose set of points is dense in `|Y|` and over which `f` becomes
> finite.
>
> The hypothesis `f^{-1}(Y⁰) = X⁰` makes the fibre of `f` over a point of codimension zero of
> `Y` finite, so over a suitable neighbourhood of such a point `f` is finite: if `f` is
> quasi-compact this is condition (3) of Stacks 0ACZ, and if `f` is separated it is condition
> (3) of Stacks 0AD0 together with the vanishing of the complementary open, which carries no
> point of codimension zero and is therefore empty by Stacks 0BAR. Since `Y⁰` is finite, finitely
> many such neighbourhoods are glued, and the result is dense because it contains `Y⁰`.

```lean
theorem exists_isDenseOpenSubspace_isFinite_pullback_snd
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y)
    (hlft : IsLocallyOfFiniteType B S hS f)
    (hYdecent : IsDecentSpace B S hS Y)
    (hXzero : Set.Finite {x : points B S hS X |
      localRingDimension B S hS x = 0})
    (hYzero : Set.Finite {y : points B S hS Y |
      localRingDimension B S hS y = 0})
    (hpreimage :
      (pointsMap B S hS X f) ⁻¹'
        {y : points B S hS Y |
          localRingDimension B S hS y = 0} =
        {x : points B S hS X |
          localRingDimension B S hS x = 0})
    (hqc_or_sep : IsQuasiCompact B S hS f ∨
      IsSeparated B S hS f) :
    letI : TopologicalSpace (points B S hS Y) :=
      pointTopology B S hS Y
    ∃ V : Subfunctor Y,
      IsOpenSubspace B S hS V ∧
        Dense (Set.range (pointsMap B S hS V.toFunctor V.ι)) ∧
          IsFinite B S hS (pullback.snd f V.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.21, Tag 0BBA](https://stacks.math.columbia.edu/tag/0BBA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
