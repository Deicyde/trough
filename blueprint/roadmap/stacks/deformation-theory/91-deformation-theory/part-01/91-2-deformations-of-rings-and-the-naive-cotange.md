---
declaration: section
origin: cited
lean: Stacks.Deformation.SquareZeroExtensionProblem.CompatibleExtension, Deformation.RingThickening.fittingMap_addTorsor_kaehlerDifferentialHom, Stacks.Deformation.obstructionClass, Stacks.Deformation.isomorphismClassesTorsor, Stacks.Deformation.isomorphismClasses_vsub_eq_obstructionClass, Stacks.Deformation.squareZeroAlgebraExtensionClassesEquivExtOne, Stacks.Deformation.squareZeroAlgebraExtensionClassesEquivExtOne_sub, Stacks.Deformation.squareZeroAlgebraExtensionClassesEquivExtOne_split_eq_zero
statement: formalized
proof: formalized
---

# 91.2 Deformations of rings and the naive cotangent complex

Section 91.2 of the Stacks Project, [Tag 08S3](https://stacks.math.columbia.edu/tag/08S3). 10 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08S4, an equation

[Tag 08S4](https://stacks.math.columbia.edu/tag/08S4) in the Stacks Project.

**`Stacks.Deformation.SquareZeroExtensionProblem.CompatibleExtension`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/Problem.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/Problem.lean#L107).

> A solution of a square-zero extension problem.
>
> The map `toB` and its kernel give the exact upper row
> `0 → N → B' → B → 0`; `kernelEquiv` supplies the displayed identification
> with `N`, and `map_I` says that the left square is the prescribed map `c`.

```lean
public structure CompatibleExtension (S : SquareZeroExtensionProblem)
```

## Tag 08S5, a lemma

[Tag 08S5](https://stacks.math.columbia.edu/tag/08S5) in the Stacks Project.

**`Deformation.RingThickening.fittingMap_addTorsor_kaehlerDifferentialHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/FittingMapTorsor.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/FittingMapTorsor.lean#L432). The attribute's comment: “torsor”. References: EGA IV (16.5.17), “special case”; SGA 1 III (5.3), “special case”; SGA 3 III (0.1.8), “(a), special case”.

> If a map filling a compatible square-zero deformation diagram exists, all such maps
> form a principal homogeneous space under `Hom_{B₁}(Ω_{B₁/A₁}, N₂)`. Subtracting
> two fitting maps gives the unique differential map whose value on `d b` is the
> difference of their values on any lift of `b`.

```lean
theorem fittingMap_addTorsor_kaehlerDifferentialHom
    (D : CompatibleSquareZeroDeformationDiagram.{u₁, u₂, u₃, u₄,
      v₁, v₂, v₃, v₄, w₁, w₂})
    (h : Nonempty D.FittingMap) :
    Nonempty
      {t : AddTorsor
          (KaehlerDifferential D.S₁.A D.S₁.B →ₗ[D.S₁.B] D.S₂.N)
          D.FittingMap //
        letI : AddTorsor
            (KaehlerDifferential D.S₁.A D.S₁.B →ₗ[D.S₁.B] D.S₂.N)
            D.FittingMap := t
        ∀ (φ ψ : D.FittingMap) (b' : D.X₁.B'),
          ((D.X₂.kernelEquiv
            ((φ -ᵥ ψ) (KaehlerDifferential.D D.S₁.A D.S₁.B (D.X₁.toB b'))) :
              RingHom.ker D.X₂.toB.toRingHom) : D.X₂.B') =
            φ.toRingHom b' - ψ.toRingHom b'}
```

**`Stacks.Deformation.obstructionClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/Obstruction/ObstructionClass.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/Obstruction/ObstructionClass.lean#L518). The attribute's comment: “obstruction”.

> The canonical obstruction to filling a compatible square-zero deformation diagram.
>
> Its value lies in `Ext¹_{B₁}(NL_{B₁/A₁}, N₂)`.  The subtype records the characteristic
> property of the obstruction: it is zero precisely when a fitting map `B'₁ → B'₂` exists.

```lean
public def obstructionClass
    (D : CompatibleSquareZeroDeformationDiagram.{u₁, u₂, u₃, u₄,
      v₁, v₂, v₃, v₄, w₁, w₂}) :
    let K := ((ModuleCat.uliftFunctor.{v₄} D.S₁.B).mapHomologicalComplex
      (ComplexShape.down ℕ)).obj (Algebra.naiveCotangentComplex D.S₁.A D.S₁.B)
    {o : DerivedCategory.Ext
        (DerivedCategory.Q.obj
          (HomologicalComplex.double (K.d 1 0)
            (show (ComplexShape.up ℤ).Rel (-1) 0 from rfl)))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₂ u₃ v₄} D.S₁.B) 0).obj
          ((ModuleCat.uliftFunctor.{max u₂ u₃} D.S₁.B).obj
            (ModuleCat.of D.S₁.B D.S₂.N))) 1 //
      o = 0 ↔ Nonempty D.FittingMap}
```

## Tag 08S7, a lemma

[Tag 08S7](https://stacks.math.columbia.edu/tag/08S7) in the Stacks Project.

**`Stacks.Deformation.isomorphismClassesTorsor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/Torsor/IsomorphismClasses.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/Torsor/IsomorphismClasses.lean#L440). References: SGA 7 VI (4.16), “(b), affine case”.

> If a square-zero extension problem has a solution, this is the canonical principal
> homogeneous-space structure on its isomorphism classes under `Ext¹_B(NL_{B/A}, N)`.

```lean
public noncomputable def isomorphismClassesTorsor
    (S : SquareZeroExtensionProblem.{u₁, u₂, u₃, u₄})
    (h : Nonempty (SquareZeroExtensionProblem.CompatibleExtension.{v} S)) :
    AddTorsor (naiveCotangentExtOne S.A S.B S.N)
      (SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{u₁, u₂, u₃, u₄, v}
        S)
```

**`Stacks.Deformation.isomorphismClasses_vsub_eq_obstructionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/Torsor/IsomorphismClasses.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/Torsor/IsomorphismClasses.lean#L455). The attribute's comment: “canonical difference”.

> In the canonical torsor of solutions, the difference `[Y] -ᵥ [X]` is the obstruction
> class `o(X, Y)` to a map from `X` to `Y`.

```lean
public theorem isomorphismClasses_vsub_eq_obstructionClass
    (S : SquareZeroExtensionProblem.{u₁, u₂, u₃, u₄})
    (h : Nonempty (SquareZeroExtensionProblem.CompatibleExtension.{v} S))
    (X Y : S.CompatibleExtension.{v}) :
    (@VSub.vsub
      (naiveCotangentExtOne S.A S.B S.N)
      (SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses S)
      (isomorphismClassesTorsor S h).toVSub
      (Quotient.mk
          (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid S) Y :
          SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses S)
      (Quotient.mk
          (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid S) X :
          SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses S) =
      (obstructionClass (comparisonDiagram X Y)).1)
```

## Tag 0GPT, a lemma

[Tag 0GPT](https://stacks.math.columbia.edu/tag/0GPT) in the Stacks Project.

**`Stacks.Deformation.squareZeroAlgebraExtensionClassesEquivExtOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/AlgebraExtensions.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/AlgebraExtensions.lean#L149).

> Isomorphism classes of square-zero extensions of an `A`-algebra `B` by a `B`-module `N`
> are canonically equivalent to `Ext¹_B(NL_{B/A}, N)`.

```lean
public noncomputable def squareZeroAlgebraExtensionClassesEquivExtOne
    (A : Type uA) (B : Type uB) [CommRing A] [CommRing B] [Algebra A B]
    (N : Type uN) [AddCommGroup N] [Module B N] :
    SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uA, uA, uB, uN,
        max uB uN}
        (algebraExtensionProblem A B N) ≃
      naiveCotangentExtOne A B N
```

**`Stacks.Deformation.squareZeroAlgebraExtensionClassesEquivExtOne_sub`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/AlgebraExtensions.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/AlgebraExtensions.lean#L196). The attribute's comment: “canonical difference”.

> The classification sends the difference between two square-zero extensions to the
> canonical obstruction class comparing them.

```lean
public theorem squareZeroAlgebraExtensionClassesEquivExtOne_sub
    (A : Type uA) (B : Type uB) [CommRing A] [CommRing B] [Algebra A B]
    (N : Type uN) [AddCommGroup N] [Module B N]
    (X Y : (algebraExtensionProblem A B N).CompatibleExtension.{max uB uN}) :
    squareZeroAlgebraExtensionClassesEquivExtOne A B N
        (Quotient.mk
          (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
            (algebraExtensionProblem A B N)) Y) -
      squareZeroAlgebraExtensionClassesEquivExtOne A B N
      (Quotient.mk
        (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
          (algebraExtensionProblem A B N)) X) =
      (obstructionClass (comparisonDiagram X Y)).1
```

**`Stacks.Deformation.squareZeroAlgebraExtensionClassesEquivExtOne_split_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/AlgebraExtensions.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/AlgebraExtensions.lean#L217). The attribute's comment: “split extension”.

> The canonical classification sends the split square-zero extension to zero.

```lean
public theorem squareZeroAlgebraExtensionClassesEquivExtOne_split_eq_zero
    (A : Type uA) (B : Type uB) [CommRing A] [CommRing B] [Algebra A B]
    (N : Type uN) [AddCommGroup N] [Module B N] :
    squareZeroAlgebraExtensionClassesEquivExtOne A B N
      (Quotient.mk
        (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
          (algebraExtensionProblem A B N)) (splitAlgebraExtension A B N)) = 0
```

## Tag 0GPU, a remark

[Tag 0GPU](https://stacks.math.columbia.edu/tag/0GPU) in the Stacks Project.

**`Algebra.Generators.exists_lift_and_cotangentMap_to_squareZeroKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/CotangentLift.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingThickening/CotangentLift.lean#L102). The attribute's comment: “lift\_and\_factor”.

> A polynomial presentation of an algebra lifts through every square-zero extension, and the
> restriction of the lift to the relation ideal factors `B`-linearly through `J / J²`.

```lean
theorem exists_lift_and_cotangentMap_to_squareZeroKernel
    {ι : Type w} (P : Algebra.Generators A B ι) (E : Algebra.Extension A B)
    (hE : E.ker ^ 2 = ⊥) :
    letI := Algebra.Extension.squareZeroKerModule E hE
    ∃ (f : P.toExtension.Hom E) (l : P.toExtension.Cotangent →ₗ[B] E.ker),
      ∀ x : P.toExtension.ker,
        (l (Algebra.Extension.Cotangent.mk x) : E.Ring) = f.toRingHom x
```

**`Stacks.Deformation.extensionClass_eq_conormalCokernelClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/PresentationExtensionClass.lean, line 673](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/PresentationExtensionClass.lean#L673). The attribute's comment: “extension\_class”.

> **Stacks 0GPU, the extension class.**  Let `α : P → B` be a presentation of the
> `A`-algebra `B` with relation ideal `J`, let `0 → N → B' → B → 0` be a square-zero extension
> of `A`-algebras, let `α' : P → B'` be an `A`-algebra lift of `α`, and let `δ : J/J² → N` be
> the `B`-linear factorisation of `α'|_J`.  Then the classification of Stacks 0GPT, carried to
> the cokernel `Coker(Hom_B(Ω_{P/A} ⊗_P B, N) → Hom_B(J/J², N))` which computes
> `Ext¹_B(NL(α), N)`, sends the extension to the class of `δ`.

```lean
public theorem extensionClass_eq_conormalCokernelClass
    {ι : Type uι} (P : Algebra.Generators A B ι)
    (X : (algebraExtensionProblem A B N).CompatibleExtension.{max uB uN})
    (lift : P.Ring →ₐ[A] X.B')
    (hlift : ∀ p, X.toB (lift p) = algebraMap P.Ring B p)
    (δ : P.toExtension.Cotangent →ₗ[B] N)
    (hδ : ∀ y : P.toExtension.ker,
      kernelVal X (δ (Algebra.Extension.Cotangent.mk y)) = lift (y : P.toExtension.Ring))
    (ψ : P.toExtension.Hom (Algebra.Generators.self A B).toExtension) :
    presentationComparison P ψ
        (extCokernelIso A B N (squareZeroAlgebraExtensionClassesEquivExtOne A B N
          (Quotient.mk (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
            (algebraExtensionProblem A B N)) X))) =
      Submodule.Quotient.mk δ
```

**`NaiveCotangent.extOne_naiveCotangentComplex_addEquiv_cokernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/ExtCokernel.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NaiveCotangent/ExtCokernel.lean#L120). The attribute's comment: “ext\_cokernel”.

> The comparison which computes the first Ext group of the naive cotangent complex of a
> polynomial presentation. On the right, the cokernel is represented as the quotient by the
> range of precomposition with the conormal differential.
>
> It is the underlying additive equivalence of
> `extOne_naiveCotangentComplex_linearEquiv_cokernel`, so the two cannot drift apart; use that
> one for anything involving scalars.

```lean
public noncomputable def extOne_naiveCotangentComplex_addEquiv_cokernel
    {A : Type uA} {B : Type uB} {ι : Type uι} {N : Type uN}
    [CommRing A] [CommRing B] [Algebra A B]
    (P : Algebra.Generators A B ι) [AddCommGroup N] [Module B N] :
    DerivedCategory.Ext
        ((DerivedCategory.Q :
            CochainComplex (ModuleCat.{max uA uB uι uN} B) ℤ ⥤ _).obj
          (CochainComplex.mappingCone
            ((CochainComplex.singleFunctor (ModuleCat.{max uA uB uι uN} B) 0).map
              (ModuleCat.ofHom
                (ULift.moduleEquiv.{uB, max (max uA uB) uι,
                  max uA uB uι uN}.symm.toLinearMap.comp
                  ((NaiveCotangent.NL P).d.comp
                    ULift.moduleEquiv.{uB, max uA uι,
                      max uA uB uι uN}.toLinearMap))))))
        ((DerivedCategory.singleFunctor (ModuleCat.{max uA uB uι uN} B) 0).obj
          (ModuleCat.of B (ULift.{max uA uB uι uN} N))) 1 ≃+
      ((P.toExtension.Cotangent →ₗ[B] N) ⧸ LinearMap.range
        ((LinearMap.lcomp B N (NaiveCotangent.NL P).d) :
          (P.toExtension.CotangentSpace →ₗ[B] N) →ₗ[B]
            (P.toExtension.Cotangent →ₗ[B] N)))
```

Declarations registered for the tag:

- [`Algebra.Extension.cotangentComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.Extension.cotangentComplex#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/NaiveCotangent/ExtCokernel.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NaiveCotangent/ExtCokernel.lean#L54) (StacksFrontier): “presentation\_complex”. References: EGA IV (17.15.9); SGA 1 II (5.9), “more general”; SGA 6 0 (4.4), “special case”; SGA 6 VIII (2.1), “affine case”.

## Tag 0GPV, a lemma

[Tag 0GPV](https://stacks.math.columbia.edu/tag/0GPV) in the Stacks Project.

**`Stacks.Deformation.exists_compatible_algebraMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/AlgebraExtensionMaps.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/AlgebraExtensionMaps.lean#L500).

> **Stacks 0GPV.**  Given ring maps `A → B → C`, a `B`-module `M`, a `C`-module `N`, a
> `B`-linear map `c : M → N`, a square-zero extension `0 → M → B' → B → 0` of `A`-algebras with
> class `ξ ∈ Ext¹_B(NL_{B/A}, M)` and a square-zero extension `0 → N → C' → C → 0` of
> `A`-algebras with class `ζ ∈ Ext¹_C(NL_{C/A}, N)`, there is an `A`-algebra map `B' → C'`
> compatible with `B → C` and with `c` if and only if `ξ` and `ζ` have the same image in
> `Ext¹_B(NL_{B/A}, N)`.

```lean
public theorem exists_compatible_algebraMap_iff :
    (∃ h : X.B' →ₐ[A] Y.B',
        (∀ z : X.B', Y.toB (h z) = algebraMap B C (X.toB z)) ∧
          ∀ m : M, h (kernelInclusion X m) = kernelInclusion Y (c m)) ↔
      naiveCotangentExtOneMap A B c (squareZeroAlgebraExtensionClassesEquivExtOne A B M
          (Quotient.mk (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
            (algebraExtensionProblem A B M)) X))
        = naiveCotangentExtOneTowerMap A B C
          (squareZeroAlgebraExtensionClassesEquivExtOne A C N
            (Quotient.mk (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
              (algebraExtensionProblem A C N)) Y))
```

## Tag 0GPW, a remark

[Tag 0GPW](https://stacks.math.columbia.edu/tag/0GPW) in the Stacks Project.

**`Stacks.Deformation.pullbackExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean#L305). The attribute's comment: “the pullback extension B'₂ = C' ×\_C B; all five rings and modules in one universe”.

> **The pullback extension `B'₂ = C' ×_C B`.**  Pulling the square-zero extension
> `0 → N → C' → C → 0` of `A`-algebras back along `B → C` gives a square-zero extension
> `0 → N → B'₂ → B → 0` of the `A`-algebra `B` by `N`.

```lean
public def pullbackExtension :
    (algebraExtensionProblem A B N).CompatibleExtension.{u}
```

**`Stacks.Deformation.pullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean#L360). The attribute's comment: “the map B'₂ → C' of the second displayed diagram”.

> **The map `B'₂ → C'`** of the remark's second displayed diagram: the first projection of the
> fibre product.

```lean
public def pullbackMap : ↥(pullbackSubalgebra A B C Y) →ₐ[A] Y.B'
```

**`Stacks.Deformation.pushoutExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean#L631). The attribute's comment: “the pushout extension B'₁ = (N × B')/M; all five rings and modules in one universe”. References: EGA 0 (19.5.6.1), “partial”.

> **The pushout extension `B'₁ = (N × B')/M`.**  Pushing the square-zero extension
> `0 → M → B' → B → 0` of `A`-algebras out along `c : M → N` gives a square-zero extension
> `0 → N → B'₁ → B → 0` of the `A`-algebra `B` by `N`.

```lean
public def pushoutExtension : (algebraExtensionProblem A B N).CompatibleExtension.{u}
```

**`Stacks.Deformation.pushoutMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean, line 696](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean#L696). The attribute's comment: “the map B' → B'₁ of the first displayed diagram”.

> **The map `B' → B'₁`** of the remark's first displayed diagram: `x ↦ [(0, x)]`.

```lean
public def pushoutMap : X.B' →ₐ[A] (pushoutExtension c X).B'
```

**`Stacks.Deformation.extClass_pushoutExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean#L739). The attribute's comment: “B'₁ corresponds to the image of ξ under Ext¹\_B(NL\_\{B/A}, M) → Ext¹\_B(NL\_\{B/A}, N)”.

> **Stacks 0GPW.**  The pushout extension `B'₁` corresponds, under the classification of
> **Stacks 0GPT**, to the image of the class of `B'` by the map
> `Ext¹_B(NL_{B/A}, M) → Ext¹_B(NL_{B/A}, N)` induced by `c : M → N`.
>
> This is **Stacks 0GPV** for the trivial tower `A → B → B`, applied to the map `B' → B'₁`
> produced by the construction, together with the fact that the restriction map for that tower
> is the identity.

```lean
public theorem extClass_pushoutExtension (c : M →ₗ[B] N)
    (X : (algebraExtensionProblem A B M).CompatibleExtension.{u}) :
    extClass (pushoutExtension c X) = naiveCotangentExtOneMap A B c (extClass X)
```

**`Stacks.Deformation.extClass_pullbackExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean, line 755](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean#L755). The attribute's comment: “B'₂ corresponds to the image of ζ under Ext¹\_C(NL\_\{C/A}, N) → Ext¹\_B(NL\_\{B/A}, N)”.

> **Stacks 0GPW.**  The pullback extension `B'₂` corresponds, under the classification of
> **Stacks 0GPT**, to the image of the class of `C'` by the map
> `Ext¹_C(NL_{C/A}, N) → Ext¹_B(NL_{B/A}, N)`.
>
> This is **Stacks 0GPV** applied to the projection `B'₂ → C'`, which is compatible with
> `B → C` and with the identity of `N`, together with the fact that the map on first Ext
> induced by the identity of `N` is the identity.

```lean
public theorem extClass_pullbackExtension
    (Y : (algebraExtensionProblem A C N).CompatibleExtension.{u}) :
    extClass (pullbackExtension A B C Y) = naiveCotangentExtOneTowerMap A B C (extClass Y)
```

**`Stacks.Deformation.isomorphic_pushoutExtension_pullbackExtension_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean, line 770](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtensionPushoutPullback.lean#L770). The attribute's comment: “a compatible A-algebra map B' → C' exists iff B'₁ and B'₂ are isomorphic”.

> **Stacks 0GPW**, the diagram chase.  There is an `A`-algebra map `B' → C'` compatible with
> `B → C` and with `c : M → N` if and only if the pushout `B'₁` is isomorphic to the pullback
> `B'₂` as `A`-algebra extensions of `B` by `N`.
>
> The two directions are obtained from **Stacks 0GPV** together with the two class
> identifications above and the injectivity of the classification of **Stacks 0GPT**.

```lean
public theorem isomorphic_pushoutExtension_pullbackExtension_iff (c : M →ₗ[B] N)
    (X : (algebraExtensionProblem A B M).CompatibleExtension.{u})
    (Y : (algebraExtensionProblem A C N).CompatibleExtension.{u}) :
    SquareZeroExtensionProblem.CompatibleExtension.Isomorphic
        (pushoutExtension c X) (pullbackExtension A B C Y) ↔
      ∃ h : X.B' →ₐ[A] Y.B',
        (∀ z : X.B', Y.toB (h z) = algebraMap B C (X.toB z)) ∧
          ∀ m : M, h (kernelInclusion X m) = kernelInclusion Y (c m)
```

## Tag 0GPX, a lemma

[Tag 0GPX](https://stacks.math.columbia.edu/tag/0GPX) in the Stacks Project.

**`Stacks.Deformation.baseExtClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean#L130). The attribute's comment: “the class ξ of the thickening A', via Lemma 0GPT”.

> The canonical class `ξ ∈ Ext¹_A(NL_{A/A'}, I)` of the square-zero thickening `A'`: the
> value of the classification of **Stacks 0GPT** on `baseExtension`.

```lean
public def baseExtClass : naiveCotangentExtOne S.A' S.A S.I
```

**`Stacks.Deformation.solutionsFibre`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean#L279). The attribute's comment: “the fibre over the image of the class of the thickening”.

> The fibre of `Ext¹_B(NL_{B/A'}, N) → Ext¹_A(NL_{A/A'}, N)` over the image of the canonical
> class `ξ` of the thickening `A'` under the map `Ext¹_A(NL_{A/A'}, I) → Ext¹_A(NL_{A/A'}, N)`
> induced by `c : I → N`.

```lean
public abbrev solutionsFibre
```

**`Stacks.Deformation.solutionsEquivFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean#L337). The attribute's comment: “solutions with middle ring in the universe max uB uN, as in Lemma 0GPT”.

> **Stacks 0GPX.**  Let `0 → I → A' → A → 0`, `A → B` and `c : I → N` be as in
> **Stacks 08S4**, and let `ξ ∈ Ext¹_A(NL_{A/A'}, I)` be the class of the extension `A'` of `A`
> by `I` under **Stacks 0GPT**.  The set of isomorphism classes of solutions of the extension
> problem is canonically bijective to the fibre of
> `Ext¹_B(NL_{B/A'}, N) → Ext¹_A(NL_{A/A'}, N)` over the image of `ξ`.
>
> The bijection is the canonical one: it sends the class of a solution to the class of its
> underlying square-zero extension of the `A'`-algebra `B` by `N`, as recorded by
> `solutionsEquivFibre_apply`.

```lean
public def solutionsEquivFibre :
    SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{u₁, u₂, u₃, u₄,
      max u₃ u₄} S ≃ solutionsFibre S
```

**`Stacks.Deformation.solutionsEquivFibre_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/SolutionsFibre.lean#L347). The attribute's comment: “the bijection sends a solution to the class of its underlying extension”.

> The bijection of **Stacks 0GPX** sends the class of a solution to the class in
> `Ext¹_B(NL_{B/A'}, N)` of its underlying square-zero extension of the `A'`-algebra `B` by
> `N`.

```lean
public lemma solutionsEquivFibre_apply (P : S.CompatibleExtension.{max u₃ u₄}) :
    (solutionsEquivFibre S (Quotient.mk
      (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid S) P)).1
      = solutionExtClass S P
```

## Tag 0GPY, a remark

[Tag 0GPY](https://stacks.math.columbia.edu/tag/0GPY) in the Stacks Project.

**`Stacks.Deformation.naiveCotangentExtOneDerivedBaseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean#L156). The attribute's comment: “Ext¹\_A(NL\_\{A/A'}, N) = Ext¹\_B(NL\_\{A/A'} ⊗^L\_A B, N), via Tag 0GMT”.

> **Stacks 0GPY**, first identification.  For `A' → A → B` and a `B`-module `M`, extension
> classes of the naive cotangent complex of `A` over `A'` with coefficients in `M` regarded as an
> `A`-module are the same as extension classes over `B` of its derived base change.  This is the
> adjunction of Stacks 0GMT.

```lean
public noncomputable def naiveCotangentExtOneDerivedBaseChangeEquiv
    (A' : Type u₁) (A : Type u₂) (B : Type u₃) [CommRing A'] [CommRing A] [CommRing B]
    [Algebra A' A] [Algebra A B] (M : ModuleCat.{max u₁ u₂ u₃ v} B) :
    DerivedCategory.Ext
        (DerivedCategory.Q.obj (naiveCotangentCochainComplex.{u₁, u₂, max u₃ v} A' A))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ u₂ u₃ v} A) 0).obj
          ((ModuleCat.restrictScalars (algebraMap A B)).obj M)) 1 ≃+
      DerivedCategory.Ext
        ((totalDerivedExtensionScalars.{u₂, u₃, max u₁ v} (algebraMap A B)).functor.obj
          (DerivedCategory.Q.obj (naiveCotangentCochainComplex.{u₁, u₂, max u₃ v} A' A)))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ u₂ u₃ v} B) 0).obj M) 1
```

**`Stacks.Deformation.naiveCotangentDerivedBaseChangeExtOneEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean#L175). The attribute's comment: “Ext¹\_B(NL\_\{A/A'} ⊗^L\_A B, N) = Ext¹\_B(NL\_\{A/A'} ⊗\_A B, N), via Tag 0FUY”.

> **Stacks 0GPY**, second identification.  Extension classes over `B` out of the derived base
> change of the naive cotangent complex are the same as extension classes out of its termwise base
> change.  The coefficient `M`, placed in degree `0` and shifted into degree `-1`, only sees the
> truncation `τ_{≥ -1}`, which the termwise base change computes by Stacks 0FUY.

```lean
public noncomputable def naiveCotangentDerivedBaseChangeExtOneEquiv
    (A' : Type u₁) (A : Type u₂) (B : Type u₃) [CommRing A'] [CommRing A] [CommRing B]
    [Algebra A' A] [Algebra A B] (M : ModuleCat.{max u₁ u₂ u₃ v} B) :
    letI : (ModuleCat.extendScalars.{u₂, u₃, max u₁ u₂ u₃ v} (algebraMap A B)).IsLeftAdjoint :=
      ModuleCat.instIsLeftAdjointExtendScalars.{u₂, u₃, max u₁ u₂ v} (algebraMap A B)
    DerivedCategory.Ext
        ((totalDerivedExtensionScalars.{u₂, u₃, max u₁ v} (algebraMap A B)).functor.obj
          (DerivedCategory.Q.obj (naiveCotangentCochainComplex.{u₁, u₂, max u₃ v} A' A)))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ u₂ u₃ v} B) 0).obj M) 1 ≃+
      DerivedCategory.Ext
        (DerivedCategory.Q.obj
          (((ModuleCat.extendScalars.{u₂, u₃, max u₁ u₂ u₃ v}
            (algebraMap A B)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
              (naiveCotangentCochainComplex.{u₁, u₂, max u₃ v} A' A)))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ u₂ u₃ v} B) 0).obj M) 1
```

**`Stacks.Deformation.naiveCotangentExtOneBaseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean#L215).

> **Stacks 0GPY**.  For `A' → A → B` and a `B`-module `M`, the first extension group of the
> naive cotangent complex of `A` over `A'` with coefficients in `M` regarded as an `A`-module is
> canonically the first extension group over `B` of the termwise base change `NL_{A/A'} ⊗_A B`
> with coefficients in `M`.

```lean
public noncomputable def naiveCotangentExtOneBaseChangeEquiv
    (A' : Type u₁) (A : Type u₂) (B : Type u₃) [CommRing A'] [CommRing A] [CommRing B]
    [Algebra A' A] [Algebra A B] (M : ModuleCat.{max u₁ u₂ u₃ v} B) :
    letI : (ModuleCat.extendScalars.{u₂, u₃, max u₁ u₂ u₃ v} (algebraMap A B)).IsLeftAdjoint :=
      ModuleCat.instIsLeftAdjointExtendScalars.{u₂, u₃, max u₁ u₂ v} (algebraMap A B)
    DerivedCategory.Ext
        (DerivedCategory.Q.obj (naiveCotangentCochainComplex.{u₁, u₂, max u₃ v} A' A))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ u₂ u₃ v} A) 0).obj
          ((ModuleCat.restrictScalars (algebraMap A B)).obj M)) 1 ≃+
      DerivedCategory.Ext
        (DerivedCategory.Q.obj
          (((ModuleCat.extendScalars.{u₂, u₃, max u₁ u₂ u₃ v}
            (algebraMap A B)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
              (naiveCotangentCochainComplex.{u₁, u₂, max u₃ v} A' A)))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ u₂ u₃ v} B) 0).obj M) 1
```

**`Stacks.Deformation.naiveCotangentExtOneBaseChangeModuleEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/ExtBaseChange.lean#L238). The attribute's comment: “for a module `N` and the Ext group `naiveCotangentExtOne`”.

> **Stacks 0GPY**, stated for a `B`-module `N` and the Ext group
> `Stacks.Deformation.naiveCotangentExtOne`: the first extension group over `A` of the naive
> cotangent complex of `A` over `A'` with coefficients in `N`, which is an `A`-module by
> restriction of scalars, is the first extension group over `B` of `NL_{A/A'} ⊗_A B`.

```lean
public noncomputable def naiveCotangentExtOneBaseChangeModuleEquiv
    (A' : Type u₁) (A : Type u₂) (B : Type u₃) [CommRing A'] [CommRing A] [CommRing B]
    [Algebra A' A] [Algebra A B] (N : Type u₄) [AddCommGroup N] [Module B N] :
    letI : (ModuleCat.extendScalars.{u₂, u₃, max u₁ u₂ u₃ u₄} (algebraMap A B)).IsLeftAdjoint :=
      ModuleCat.instIsLeftAdjointExtendScalars.{u₂, u₃, max u₁ u₂ u₄} (algebraMap A B)
    letI : Module A (ULift.{u₃} N) := Module.compHom _ (algebraMap A B)
    naiveCotangentExtOne A' A (ULift.{u₃} N) ≃+
      DerivedCategory.Ext
        (DerivedCategory.Q.obj
          (((ModuleCat.extendScalars.{u₂, u₃, max u₁ u₂ u₃ u₄}
            (algebraMap A B)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
              (naiveCotangentCochainComplex.{u₁, u₂, max u₃ u₄} A' A)))
        ((DerivedCategory.singleFunctor (ModuleCat.{max u₁ u₂ u₃ u₄} B) 0).obj
          ((ModuleCat.uliftFunctor.{max u₁ u₂} B).obj
            (ModuleCat.of B (ULift.{u₃} N)))) 1
```

## Tag 08S6, a lemma

[Tag 08S6](https://stacks.math.columbia.edu/tag/08S6) in the Stacks Project.

**`Stacks.Deformation.nonempty_compatibleExtension_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/LocalCompleteIntersection.lean, line 674](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SquareZero/LocalCompleteIntersection.lean#L674).

> **Stacks 08S6.**  If `A → B` is a local complete intersection ring map, then every
> square-zero extension problem over `A' → A` with target `B` and prescribed kernel map
> `c : I → N` has a solution.

```lean
public theorem nonempty_compatibleExtension_of_isLocalCompleteIntersection
    (S : SquareZeroExtensionProblem.{u₁, u₂, u₃, u₄})
    (h : (algebraMap S.A S.B).IsLocalCompleteIntersection) :
    Nonempty (S.CompatibleExtension.{max u₁ (max u₂ (max u₃ u₄))})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.2, Tag 08S3](https://stacks.math.columbia.edu/tag/08S3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
