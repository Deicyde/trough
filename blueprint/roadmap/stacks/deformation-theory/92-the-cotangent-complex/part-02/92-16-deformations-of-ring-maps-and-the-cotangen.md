---
declaration: section
origin: cited
lean: Stacks.Deformation.SquareZeroExtensionProblem.CompatibleExtension, Stacks.Deformation.SquareZeroExtensionProblem.isoFittingMapEquiv, Stacks.Deformation.SquareZeroExtensionProblem.automorphismsExtEquiv, Stacks.Deformation.SquareZeroExtensionProblem.cotangentObstructionClass_eq_zero_iff, Stacks.Deformation.SquareZeroExtensionProblem.isomorphismClassesCotangentTorsor
statement: formalized
proof: formalized
---

# 92.16 Deformations of ring maps and the cotangent complex

Section 92.16 of the Stacks Project, [Tag 08SM](https://stacks.math.columbia.edu/tag/08SM). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08SN, an equation

[Tag 08SN](https://stacks.math.columbia.edu/tag/08SN) in the Stacks Project.

**`Stacks.Deformation.SquareZeroExtensionProblem.CompatibleExtension`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SquareZero/Problem.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/SquareZero/Problem.lean#L107). The attribute's comment: “the same extension problem diagram”.

> A solution of a square-zero extension problem.
>
> The map `toB` and its kernel give the exact upper row
> `0 → N → B' → B → 0`; `kernelEquiv` supplies the displayed identification
> with `N`, and `map_I` says that the left square is the prescribed map `c`.

```lean
public structure CompatibleExtension (S : SquareZeroExtensionProblem)
```

## Tag 08SP, a lemma

[Tag 08SP](https://stacks.math.columbia.edu/tag/08SP) in the Stacks Project.

**`Stacks.Deformation.SquareZeroExtensionProblem.isoFittingMapEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/CotangentAutomorphisms.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingThickening/CotangentAutomorphisms.lean#L285). The attribute's comment: “automorphisms are the fitting maps of the self-comparison diagram”.

> The automorphisms of a solution of a square-zero extension problem which induce the identity
> on `B` and on `N` are exactly the maps filling the diagram comparing the problem with itself.

```lean
noncomputable def isoFittingMapEquiv (X : S.CompatibleExtension.{w}) :
    CompatibleExtension.Iso X X ≃ (comparisonDiagram X X).FittingMap
```

**`Stacks.Deformation.SquareZeroExtensionProblem.automorphismsExtEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/CotangentAutomorphisms.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingThickening/CotangentAutomorphisms.lean#L304). The attribute's comment: “automorphisms”. References: EGA 0 (20.1.4), “Commutative case”; SGA 7 VI (4.16), “(a), affine case”.

> **Stacks 08SP**, part (3). For a solution `B'` of a square-zero extension problem, the
> automorphisms of `B'` inducing the identity on `B` and on `N` are canonically
> `Ext⁰_B(L_{B/A}, N)`.
>
> The equivalence carries the identity automorphism to `0` and composition to addition, so it is
> an isomorphism of groups, and the class attached to `f` is the one whose associated differential
> map sends `d (b' mod N)` to `f(b') - b'`.

```lean
noncomputable def automorphismsExtEquiv (X : S.CompatibleExtension.{w}) :
    {e : CompatibleExtension.Iso X X ≃ S.cotangentExt 0 //
      e (CompatibleExtension.Iso.refl X) = 0 ∧
      (∀ f g : CompatibleExtension.Iso X X, e (f.trans g) = e f + e g) ∧
      ∀ (f : CompatibleExtension.Iso X X) (b' : X.B'),
        ((X.kernelEquiv (S.cotangentExtZeroToHom (e f)
            (KaehlerDifferential.D S.A S.B (X.toB b'))) :
          RingHom.ker X.toB.toRingHom) : X.B') = f.toAlgEquiv b' - b'}
```

**`Stacks.Deformation.SquareZeroExtensionProblem.cotangentObstructionClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/CotangentObstruction.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingThickening/CotangentObstruction.lean#L111). The attribute's comment: “(1): there is a class in Ext²\_B(L\_\{B/A}, N) whose vanishing is necessary and sufficient for the existence of a solution”.

> **Stacks 08SP**, part (1). The class `ξ ∈ Ext²_B(L_{B/A}, N)` vanishes if and only if the
> square-zero extension problem has a solution.

```lean
theorem cotangentObstructionClass_eq_zero_iff :
    S.cotangentObstructionClass = 0 ↔ Nonempty (S.CompatibleExtension.{u})
```

**`Stacks.Deformation.SquareZeroExtensionProblem.isomorphismClassesCotangentTorsor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingThickening/CotangentTorsor.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingThickening/CotangentTorsor.lean#L50). The attribute's comment: “(2): if a solution exists, the isomorphism classes of solutions form a principal homogeneous space under Ext¹\_B(L\_\{B/A}, N)”.

> **Stacks 08SP**, part (2). If the square-zero extension problem has a solution, its set of
> isomorphism classes of solutions is a principal homogeneous space under `Ext¹_B(L_{B/A}, N)`.
>
> The action is that of Tag 08S7 under `Ext¹_B(NL_{B/A}, N)`, read through the identification
> `Ext¹_B(NL_{B/A}, N) = Ext¹_B(L_{B/A}, N)` of `cotangentExtOneEquiv`.

```lean
noncomputable def isomorphismClassesCotangentTorsor
    (h : Nonempty (S.CompatibleExtension.{w})) :
    AddTorsor (S.cotangentExt 1)
      (CompatibleExtension.IsomorphismClasses.{u₁, u₂, max u₂ v, u₄, w} S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.16, Tag 08SM](https://stacks.math.columbia.edu/tag/08SM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
