---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.RelativeMorphism, AlgebraicGeometry.Space.RelativeMorphismDiagram, AlgebraicGeometry.Space.relativeHomData, AlgebraicGeometry.Space.relativeHomEquiv, AlgebraicGeometry.Space.isSheaf_relativeHom, AlgebraicGeometry.Space.isPullback_sheaf_relativeHomOfBaseChange, AlgebraicGeometry.Space.isPullback_sheaf_relativeHomOfBaseChange_relativeHomData, AlgebraicGeometry.Space.isPullback_sheaf_relativeHomOfBaseChange_of_isAlgebraicSpace
statement: formalized
proof: formalized
---

# 97.10 Relative morphisms

Section 97.10 of the Stacks Project, [Tag 05Y0](https://stacks.math.columbia.edu/tag/05Y0). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05Y1, an equation

[Tag 05Y1](https://stacks.math.columbia.edu/tag/05Y1) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphism.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphism.lean#L231). The attribute's comment: “the pair `(a, b)` of the diagram”.

> **Stacks 05Y1.** A pair `(a, b)` for the relative morphism functor of `z : Z ⟶ Q` and
> `x : X ⟶ Q` at a test presheaf `T`: a morphism `a : T ⟶ Q` together with a morphism
> `b : T ×_{a, Q} Z ⟶ X` lying over `Q`. The source's other description of `b`, as a morphism
> `T ×_{a, Q} Z ⟶ T ×_{a, Q} X` over `T`, is equivalent to this one.

```lean
structure RelativeMorphism (Z X Q : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (z : Z ⟶ Q) (x : X ⟶ Q)
    (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
```

**`AlgebraicGeometry.Space.RelativeMorphismDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphism.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphism.lean#L347). The attribute's comment: “the displayed diagram: `b : T ×_{a, B} Z ⟶ T ×_{a, B} X` over `T`”.

> **Stacks 05Y1.** The diagram of a pair at a test presheaf `T`, in the shape the source
> displays it: a morphism `a : T ⟶ Q` together with a morphism
> `b : T ×_{a, Q} Z ⟶ T ×_{a, Q} X` *over `T`*, that is, commuting with the two projections to
> `T`.
>
> This is the first of the source's two descriptions of a pair; the second,
> `AlgebraicGeometry.Space.RelativeMorphism`, reads `b` instead as a morphism
> `T ×_{a, Q} Z ⟶ X` lying over `Q`. The two are the same data —
> `AlgebraicGeometry.Space.relativeMorphismEquivDiagram`.

```lean
structure RelativeMorphismDiagram (Z X Q : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (z : Z ⟶ Q)
    (x : X ⟶ Q) (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
```

## Tag 05Y2, an equation

[Tag 05Y2](https://stacks.math.columbia.edu/tag/05Y2) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeHomData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphism.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphism.lean#L513).

> **Stacks 05Y2.** The relative morphism functor `Mor_Q(Z, X)` of two morphisms `z : Z ⟶ Q` and
> `x : X ⟶ Q` of algebraic spaces over `S`: a small-valued presheaf on the big fppf site of `S`
> whose sections over a scheme `T` are the pairs `(a, b)` of Stacks 05Y1, with its projection to `Q`
> and with restriction given by base change.
>
> The three algebraicity hypotheses are kept because the source states the functor for algebraic
> spaces, but they are not used: smallness of the values comes from essential smallness of the
> site (`AlgebraicGeometry.locallySmall_presheaf_bigFppfOver`), not from the existence of an étale
> atlas.

```lean
noncomputable def relativeHomData (Z X Q : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (z : Z ⟶ Q)
    (x : X ⟶ Q) (_hZ : IsAlgebraicSpace B S hS Z) (_hX : IsAlgebraicSpace B S hS X)
    (_hQ : IsAlgebraicSpace B S hS Q) : RelativeHomConstruction B S hS Z X Q z x
```

## Tag 05Y3, a lemma

[Tag 05Y3](https://stacks.math.columbia.edu/tag/05Y3) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphismHom.lean, line 669](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphismHom.lean#L669). The attribute's comment: “part (2): the canonical bijection between the morphisms from an algebraic space `T` into `Mor_B(Z, X)` and the pairs `(a, b)` of Stacks 05Y1 at `T`”.

> **Stacks 05Y3**, part (2). For a test object `T` — in the source an algebraic space over
> `S` — the morphisms `T ⟶ Mor_Q(Z, X)` are canonically the pairs `(a, b)` of Stacks 05Y1 at `T`:
> a morphism `a : T ⟶ Q` together with a morphism `b : T ×_{a, Q} Z ⟶ X` over `Q`.
>
> The bijection extends the identification of the sections over a scheme with pairs
> (`AlgebraicGeometry.Space.relativeHomEquiv_yoneda`) and is natural in `T`
> (`AlgebraicGeometry.Space.relativeHomEquiv_naturality`); the algebraicity of `T` is recorded
> because the source states the bijection for algebraic spaces, but it is not used.

```lean
noncomputable def relativeHomEquiv (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hT : IsAlgebraicSpace B S hS T) :
    (T ⟶ relativeHom B S hS Z X Q z x hZ hX hQ) ≃ RelativeMorphism B S hS Z X Q z x T
```

**`AlgebraicGeometry.Space.isSheaf_relativeHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphismSheaf.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeMorphismSheaf.lean#L269). The attribute's comment: “part (1): the relative morphism functor `Mor_B(Z, X)` is a sheaf on the big fppf site of `S`”.

> **Stacks 05Y3**, part (1). For morphisms `z : Z ⟶ Q` and `x : X ⟶ Q` of algebraic spaces
> over `S`, the relative morphism functor `Mor_Q(Z, X)` of Stacks 05Y2 is a sheaf on the big fppf
> site of `S`.

```lean
theorem isSheaf_relativeHom (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (Z X Q : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (z : Z ⟶ Q) (x : X ⟶ Q)
    (hZ : IsAlgebraicSpace B S hS Z) (hX : IsAlgebraicSpace B S hS X)
    (hQ : IsAlgebraicSpace B S hS Q) :
    Presheaf.IsSheaf (BigFppfOver.topology B S hS)
      (relativeHom B S hS Z X Q z x hZ hX hQ)
```

## Tag 05Y4, a lemma

[Tag 05Y4](https://stacks.math.columbia.edu/tag/05Y4) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_sheaf_relativeHomOfBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean#L581). The attribute's comment: “the identification in `Sh((Sch/S)_fppf)`, with the sheaf property of the two relative morphism functors — part (1) of the cited Stacks 05Y3 — carried as a hypothesis”.

> **Stacks 05Y4.** The identification
>
> ```text
> Mor_{Q'}(Z', X') = Q' ×_Q Mor_Q(Z, X)
> ```
>
> **in `Sh((Sch/S)_fppf)`**: the square of fppf sheaves formed by the two projections reading off
> the first component of a pair of Stacks 05Y1, the morphism `q` and the morphism forgetting the
> base change is cartesian.
>
> This is the source's statement. Its proof is the source's: the square of presheaves is
> cartesian, which is `AlgebraicGeometry.Space.isPullback_relativeHomOfBaseChange`, and the
> inclusion of fppf sheaves into presheaves creates limits, so a square of sheaves is cartesian as
> soon as the underlying square of presheaves is. The sheaf property of the two relative morphism
> functors is part (1) of Stacks 05Y3, which this library does not carry; it is taken as the
> hypotheses `hH` and `hH'`, and nothing else about the two functors is assumed. The sheaf
> property of `Q` and of `Q'` is automatic for algebraic spaces.

```lean
theorem isPullback_sheaf_relativeHomOfBaseChange (q : Q' ⟶ Q)
    (H : RelativeHomConstruction B S hS Z X Q z x)
    (H' : RelativeHomConstruction B S hS (pullback q z) (pullback q x) Q'
      (pullback.fst q z) (pullback.fst q x))
    (hQ : Presheaf.IsSheaf (BigFppfOver.topology B S hS) Q)
    (hQ' : Presheaf.IsSheaf (BigFppfOver.topology B S hS) Q')
    (hH : Presheaf.IsSheaf (BigFppfOver.topology B S hS) H.functor)
    (hH' : Presheaf.IsSheaf (BigFppfOver.topology B S hS) H'.functor) :
    IsPullback
      (ObjectProperty.homMk H'.projection :
        (⟨H'.functor, hH'⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨Q', hQ'⟩)
      (ObjectProperty.homMk (relativeHomOfBaseChange q H H') :
        (⟨H'.functor, hH'⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨H.functor, hH⟩)
      (ObjectProperty.homMk q :
        (⟨Q', hQ'⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨Q, hQ⟩)
      (ObjectProperty.homMk H.projection :
        (⟨H.functor, hH⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨Q, hQ⟩)
```

**`AlgebraicGeometry.Space.isPullback_sheaf_relativeHomOfBaseChange_relativeHomData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean, line 667](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean#L667). The attribute's comment: “the identification in `Sh((Sch/S)_fppf)` for the functor of Stacks 05Y2 and the fibre products of Stacks 02X2, with the sheaf property of the two relative morphism functors — part (1) of the cited Stacks 05Y3 — carried as a hypothesis”.

> **Stacks 05Y4** for the relative morphism functor of Stacks 05Y2 and the fibre products of
> algebraic spaces of Stacks 02X2: for morphisms `z : Z ⟶ Q`, `x : X ⟶ Q` and `q : Q' ⟶ Q` of
> algebraic spaces over `S`,
>
> ```text
> Mor_{Q'}(Q' ×_Q Z, Q' ×_Q X) = Q' ×_Q Mor_Q(Z, X)
> ```
>
> **in `Sh((Sch/S)_fppf)`**. The sheaf property of the two relative morphism functors is part (1)
> of Stacks 05Y3, which this library does not carry; it is taken as the hypotheses `hH` and `hH'`.
> That `Q` and `Q'` are sheaves is part of being an algebraic space, so nothing else is assumed.

```lean
theorem isPullback_sheaf_relativeHomOfBaseChange_relativeHomData
    {Z X Q Q' : AlgebraicSpaces B S hS} (z : Z ⟶ Q) (x : X ⟶ Q) (q : Q' ⟶ Q)
    (hH : Presheaf.IsSheaf (BigFppfOver.topology B S hS)
      (relativeHomData B S hS Z.obj X.obj Q.obj z.hom x.hom Z.property X.property
        Q.property).functor)
    (hH' : Presheaf.IsSheaf (BigFppfOver.topology B S hS)
      (relativeHomData B S hS (AlgebraicSpaces.fiberProduct B S hS q z).obj
        (AlgebraicSpaces.fiberProduct B S hS q x).obj Q'.obj
        (pullback.fst q.hom z.hom) (pullback.fst q.hom x.hom)
        (AlgebraicSpaces.fiberProduct B S hS q z).property
        (AlgebraicSpaces.fiberProduct B S hS q x).property Q'.property).functor) :
    IsPullback
      (ObjectProperty.homMk
        (relativeHomData B S hS (AlgebraicSpaces.fiberProduct B S hS q z).obj
          (AlgebraicSpaces.fiberProduct B S hS q x).obj Q'.obj
          (pullback.fst q.hom z.hom) (pullback.fst q.hom x.hom)
          (AlgebraicSpaces.fiberProduct B S hS q z).property
          (AlgebraicSpaces.fiberProduct B S hS q x).property Q'.property).projection :
        (⟨_, hH'⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶
          ⟨Q'.obj, Q'.property.isSheaf⟩)
      (ObjectProperty.homMk
        (relativeHomOfBaseChange q.hom
          (relativeHomData B S hS Z.obj X.obj Q.obj z.hom x.hom Z.property X.property Q.property)
          (relativeHomData B S hS (AlgebraicSpaces.fiberProduct B S hS q z).obj
            (AlgebraicSpaces.fiberProduct B S hS q x).obj Q'.obj
            (pullback.fst q.hom z.hom) (pullback.fst q.hom x.hom)
            (AlgebraicSpaces.fiberProduct B S hS q z).property
            (AlgebraicSpaces.fiberProduct B S hS q x).property Q'.property)) :
        (⟨_, hH'⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨_, hH⟩)
      (ObjectProperty.homMk q.hom :
        (⟨Q'.obj, Q'.property.isSheaf⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶
          ⟨Q.obj, Q.property.isSheaf⟩)
      (ObjectProperty.homMk
        (relativeHomData B S hS Z.obj X.obj Q.obj z.hom x.hom Z.property X.property
          Q.property).projection :
        (⟨_, hH⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶
          ⟨Q.obj, Q.property.isSheaf⟩)
```

**`AlgebraicGeometry.Space.isPullback_sheaf_relativeHomOfBaseChange_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean#L764). The attribute's comment: “the identification in `Sh((Sch/S)_fppf)`”.

> **Stacks 05Y4**, unconditionally. The identification
>
> ```text
> Mor_{Q'}(Z', X') = Q' ×_Q Mor_Q(Z, X)
> ```
>
> **in `Sh((Sch/S)_fppf)`**, for arbitrary realizations of the two relative morphism functors.
> This is `AlgebraicGeometry.Space.isPullback_sheaf_relativeHomOfBaseChange` with its two sheaf
> hypotheses discharged by part (1) of Stacks 05Y3, in the form
> `AlgebraicGeometry.Space.RelativeHomConstruction.isSheaf_functor`; the algebraicity of the
> sources and of the two bases is all that remains.

```lean
theorem isPullback_sheaf_relativeHomOfBaseChange_of_isAlgebraicSpace (q : Q' ⟶ Q)
    (H : RelativeHomConstruction B S hS Z X Q z x)
    (H' : RelativeHomConstruction B S hS (pullback q z) (pullback q x) Q'
      (pullback.fst q z) (pullback.fst q x))
    (hZ : IsAlgebraicSpace B S hS Z) (hX : IsAlgebraicSpace B S hS X)
    (hQ : IsAlgebraicSpace B S hS Q) (hQ' : IsAlgebraicSpace B S hS Q')
    (hZ' : IsAlgebraicSpace B S hS (pullback q z))
    (hX' : IsAlgebraicSpace B S hS (pullback q x)) :
    IsPullback
      (ObjectProperty.homMk H'.projection :
        (⟨H'.functor, H'.isSheaf_functor hZ' hX' hQ'⟩ :
          Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨Q', hQ'.isSheaf⟩)
      (ObjectProperty.homMk (relativeHomOfBaseChange q H H') :
        (⟨H'.functor, H'.isSheaf_functor hZ' hX' hQ'⟩ :
            Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶
          ⟨H.functor, H.isSheaf_functor hZ hX hQ⟩)
      (ObjectProperty.homMk q :
        (⟨Q', hQ'.isSheaf⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨Q, hQ.isSheaf⟩)
      (ObjectProperty.homMk H.projection :
        (⟨H.functor, H.isSheaf_functor hZ hX hQ⟩ :
          Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ ⟨Q, hQ.isSheaf⟩)
```

**`AlgebraicGeometry.Space.isPullback_relativeHomSheafOfBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean, line 804](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/RelativeMorphismBaseChange.lean#L804). The attribute's comment: “the identification in `Sh((Sch/S)_fppf)` for the functor of Stacks 05Y2 and the fibre products of Stacks 02X2”.

> **Stacks 05Y4**, unconditionally, for the relative morphism functor of Stacks 05Y2 and the
> fibre products of algebraic spaces of Stacks 02X2: for morphisms `z : Z ⟶ Q`, `x : X ⟶ Q` and
> `q : Q' ⟶ Q` of algebraic spaces over `S`,
>
> ```text
> Mor_{Q'}(Q' ×_Q Z, Q' ×_Q X) = Q' ×_Q Mor_Q(Z, X)
> ```
>
> **in `Sh((Sch/S)_fppf)`**. This is the source's statement with nothing assumed: the sheaf
> property of the two relative morphism functors is part (1) of Stacks 05Y3,
> `AlgebraicGeometry.Space.isSheaf_relativeHom`.

```lean
theorem isPullback_relativeHomSheafOfBaseChange {Z X Q Q' : AlgebraicSpaces B S hS}
    (z : Z ⟶ Q) (x : X ⟶ Q) (q : Q' ⟶ Q) :
    IsPullback
      (ObjectProperty.homMk
        (relativeHomProjection B S hS (AlgebraicSpaces.fiberProduct B S hS q z).obj
          (AlgebraicSpaces.fiberProduct B S hS q x).obj Q'.obj
          (pullback.fst q.hom z.hom) (pullback.fst q.hom x.hom)
          (AlgebraicSpaces.fiberProduct B S hS q z).property
          (AlgebraicSpaces.fiberProduct B S hS q x).property Q'.property) :
        relativeHomSheaf B S hS (AlgebraicSpaces.fiberProduct B S hS q z).obj
            (AlgebraicSpaces.fiberProduct B S hS q x).obj Q'.obj
            (pullback.fst q.hom z.hom) (pullback.fst q.hom x.hom)
            (AlgebraicSpaces.fiberProduct B S hS q z).property
            (AlgebraicSpaces.fiberProduct B S hS q x).property Q'.property ⟶
          ⟨Q'.obj, Q'.property.isSheaf⟩)
      (ObjectProperty.homMk
        (relativeHomOfBaseChange q.hom
          (relativeHomData B S hS Z.obj X.obj Q.obj z.hom x.hom Z.property X.property Q.property)
          (relativeHomData B S hS (AlgebraicSpaces.fiberProduct B S hS q z).obj
            (AlgebraicSpaces.fiberProduct B S hS q x).obj Q'.obj
            (pullback.fst q.hom z.hom) (pullback.fst q.hom x.hom)
            (AlgebraicSpaces.fiberProduct B S hS q z).property
            (AlgebraicSpaces.fiberProduct B S hS q x).property Q'.property)) :
        relativeHomSheaf B S hS (AlgebraicSpaces.fiberProduct B S hS q z).obj
            (AlgebraicSpaces.fiberProduct B S hS q x).obj Q'.obj
            (pullback.fst q.hom z.hom) (pullback.fst q.hom x.hom)
            (AlgebraicSpaces.fiberProduct B S hS q z).property
            (AlgebraicSpaces.fiberProduct B S hS q x).property Q'.property ⟶
          relativeHomSheaf B S hS Z.obj X.obj Q.obj z.hom x.hom Z.property X.property Q.property)
      (ObjectProperty.homMk q.hom :
        (⟨Q'.obj, Q'.property.isSheaf⟩ : Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶
          ⟨Q.obj, Q.property.isSheaf⟩)
      (ObjectProperty.homMk
        (relativeHomProjection B S hS Z.obj X.obj Q.obj z.hom x.hom Z.property X.property
          Q.property) :
        relativeHomSheaf B S hS Z.obj X.obj Q.obj z.hom x.hom Z.property X.property Q.property ⟶
          ⟨Q.obj, Q.property.isSheaf⟩)
```

## Tag 05Y5, a lemma

[Tag 05Y5](https://stacks.math.columbia.edu/tag/05Y5) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_relativeHomPostcompose_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean#L445). The attribute's comment: “surjective, given `X' ⟶ X` surjective: at the hypotheses of the source, with nothing carried”.

> **Stacks 05Y5, third conclusion, at the hypotheses of the source.**  Let `z : Z ⟶ Q` and
> `x' : X' ⟶ X ⟶ Q` be morphisms of algebraic spaces over `S` with `X' ⟶ X` étale and surjective
> and `z` finite locally free.  Then `Mor_Q(Z, X') ⟶ Mor_Q(Z, X)` is surjective.
>
> This is `AlgebraicGeometry.Space.isSurjective_relativeHomPostcompose` with its hypothesis
> `h05XQ` discharged by `AlgebraicGeometry.Space.isFibreSectionsSurjective`; it is stated here for
> the reason recorded on
> `AlgebraicGeometry.Space.isSurjective_restrictionOfScalarsMap_of_isFiniteLocallyFree`.

```lean
theorem isSurjective_relativeHomPostcompose_of_isFiniteLocallyFree
    {X' X Z Q : AlgebraicSpaces B S hS} {x' : X' ⟶ Q} {x : X ⟶ Q} {z : Z ⟶ Q}
    (HX' : RelativeHomConstruction B S hS Z.obj X'.obj Q.obj z.hom x'.hom)
    (HX : RelativeHomConstruction B S hS Z.obj X.obj Q.obj z.hom x.hom)
    (g : X' ⟶ X) (hg : g.hom ≫ x.hom = x'.hom)
    (hg_etale : IsEtale B S hS g.hom) (hg_surjective : IsSurjective B S hS g.hom)
    (hz : IsFiniteLocallyFree B S hS z) :
    IsSurjective B S hS (relativeHomPostcompose HX' HX g.hom hg)
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_relativeHomPostcompose_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean#L385). The attribute's comment: “representable by algebraic spaces: at the hypotheses of the source, with nothing carried”.

> **Stacks 05Y5, first conclusion, at the hypotheses of the source.** Let `Z → Q` and
> `X' → X → Q` be morphisms of algebraic spaces over `S` with `X' → X` étale and `Z → Q` finite
> locally free. Then `Mor_Q(Z, X') → Mor_Q(Z, X)` is representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_relativeHomPostcompose_of_isFiniteLocallyFree
    {X' X Z Q : AlgebraicSpaces B S hS} {x' : X' ⟶ Q} {x : X ⟶ Q} {z : Z ⟶ Q}
    (HX' : RelativeHomConstruction B S hS Z.obj X'.obj Q.obj z.hom x'.hom)
    (HX : RelativeHomConstruction B S hS Z.obj X.obj Q.obj z.hom x.hom)
    (g : X' ⟶ X) (hg : g.hom ≫ x.hom = x'.hom) (hg_etale : IsEtale B S hS g.hom)
    (hz : IsFiniteLocallyFree B S hS z) :
    IsRepresentableByAlgebraicSpaces B S hS (relativeHomPostcompose HX' HX g.hom hg)
```

**`AlgebraicGeometry.Space.hasProperty_isEtale_relativeHomPostcompose_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean#L399). The attribute's comment: “étale: at the hypotheses of the source, with nothing carried”.

> **Stacks 05Y5, second conclusion, at the hypotheses of the source.** In the situation of
> `isRepresentableByAlgebraicSpaces_relativeHomPostcompose_of_isFiniteLocallyFree`,
> the morphism `Mor_Q(Z, X') → Mor_Q(Z, X)` is étale.

```lean
theorem hasProperty_isEtale_relativeHomPostcompose_of_isFiniteLocallyFree
    {X' X Z Q : AlgebraicSpaces B S hS} {x' : X' ⟶ Q} {x : X ⟶ Q} {z : Z ⟶ Q}
    (HX' : RelativeHomConstruction B S hS Z.obj X'.obj Q.obj z.hom x'.hom)
    (HX : RelativeHomConstruction B S hS Z.obj X.obj Q.obj z.hom x.hom)
    (g : X' ⟶ X) (hg : g.hom ≫ x.hom = x'.hom) (hg_etale : IsEtale B S hS g.hom)
    (hz : IsFiniteLocallyFree B S hS z) :
    HasProperty B S hS (fun _ _ f => IsEtale B S hS f.hom)
      (relativeHomPostcompose HX' HX g.hom hg)
      (isRepresentableByAlgebraicSpaces_relativeHomPostcompose_of_isFiniteLocallyFree B S hS HX'
        HX g hg hg_etale hz)
```

## Tag 05Y7, a proposition

[Tag 05Y7](https://stacks.math.columbia.edu/tag/05Y7) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_relativeHom_of_isFiniteLocallyFree_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean#L472). The attribute's comment: “at the hypotheses of the source, with nothing carried”.

> **Stacks 05Y7, at the hypotheses of the source.** Let `S` be a scheme contained in a big fppf
> site, and let `z : Z ⟶ Q` and `x : X ⟶ Q` be morphisms of algebraic spaces over `S`. If `z` is
> finite locally free then the relative morphism functor `Mor_Q(Z, X)` of Stacks 05Y2 is an
> algebraic space over `S`.

```lean
theorem isAlgebraicSpace_relativeHom_of_isFiniteLocallyFree_source
    (Z X Q : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (z : Z ⟶ Q) (x : X ⟶ Q)
    (hZ : IsAlgebraicSpace B S hS Z) (hX : IsAlgebraicSpace B S hS X)
    (hQ : IsAlgebraicSpace B S hS Q)
    (hz : IsFiniteLocallyFree B S hS
      (ObjectProperty.homMk z :
        (⟨Z, hZ⟩ : AlgebraicSpaces B S hS) ⟶ (⟨Q, hQ⟩ : AlgebraicSpaces B S hS))) :
    IsAlgebraicSpace B S hS (relativeHom B S hS Z X Q z x hZ hX hQ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.10, Tag 05Y0](https://stacks.math.columbia.edu/tag/05Y0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
