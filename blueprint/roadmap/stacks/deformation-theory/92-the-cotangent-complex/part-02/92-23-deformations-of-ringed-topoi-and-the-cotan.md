---
declaration: section
origin: cited
lean: Deformation.ToposThickening.ArbitrarySiteExtensionProblem.CompatibleFirstOrderThickening, Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening, Deformation.ToposThickening.RingedToposExtensionProblem.nonempty_iff_obstructionClass_eq_zero, Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.autEquivDerivation, Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.autEquivDerivation_mul, Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.autMulEquivExtZero, Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphismClassesAddTorsor
statement: formalized
proof: formalized
---

# 92.23 Deformations of ringed topoi and the cotangent complex

Section 92.23 of the Stacks Project, [Tag 08V3](https://stacks.math.columbia.edu/tag/08V3). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08V4, an equation

[Tag 08V4](https://stacks.math.columbia.edu/tag/08V4) in the Stacks Project.

**`Deformation.ToposThickening.ArbitrarySiteExtensionProblem.CompatibleFirstOrderThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean#L167). The attribute's comment: “the same square-zero extension problem, as stated in the Cotangent chapter”.

> **Stacks 08UF on arbitrary equivalent sites.** A solution of the extension problem on a given
> thickened source ringed topos `X'`. The displayed diagram of sheaves is pulled back along the
> equivalence underlying `i`, and the invertible 2-morphism records the morphism of thickenings.

```lean
public structure CompatibleFirstOrderThickening
    (S : ArbitrarySiteExtensionProblem X B B')
    (X' : RingedTopos.{v''', u''', w'''})
    [X'.J.HasSheafCompose (forget RingCat.{w'''})]
    [X'.J.HasSheafCompose (forget₂ CommRingCat.{w'''} RingCat.{w'''})]
```

Declarations registered for the tag:

- [`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionProblem.lean#L127), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/UniversalFirstOrder/ArbitrarySite.lean#L90) (StacksFrontier): “the displayed diagram, same-site presentation”.

## Tag 08V5, a lemma

[Tag 08V5](https://stacks.math.columbia.edu/tag/08V5) in the Stacks Project.

**`Deformation.ToposThickening.RingedToposExtensionProblem.nonempty_iff_obstructionClass_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CotangentObstructionExistence.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CotangentObstructionExistence.lean#L326). The attribute's comment: “(1): the element `obstructionClass` of `Ext²_O(L_f, G)`, the image of the class of `c` under the connecting morphism of the fundamental triangle of `f⁻¹O_{B'} → f⁻¹O_B → O`, vanishes exactly when a solution exists”.

> **Stacks 08V5 (1)**: a solution of the square-zero extension problem exists if and only if
> the obstruction class in `Ext²_O(L_f, G)` vanishes.

```lean
theorem nonempty_iff_obstructionClass_eq_zero :
    Nonempty S.CompatibleFirstOrderThickening ↔ S.obstructionClass = 0
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.autEquivDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionAutomorphisms.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionAutomorphisms.lean#L419). The attribute's comment: “clause (3), the automorphism group of a solution, computed for the concrete group of section-wise derivations of the solution rather than Ext⁰_O(L_f, G); that identification is not proved, as in the library's Stacks 08UG and Stacks 08UK”.

> **Stacks Project, Tag 08V5, clause (3).** The automorphisms of a solution of the square-zero
> extension problem of [Stacks Project, Tag 08V4] fitting into that diagram are canonically
> bijective to the derivations of that solution — section-wise maps from its thickened structure
> sheaf to the prescribed module `G` satisfying the Leibniz rule and vanishing on `G` and on the
> image of `f⁻¹O_{B'}`. With `autEquivDerivation_mul` this is an isomorphism of groups.
>
> The source writes the group as `Ext⁰_O(L_f, G)`; that identification is **not** proved here, and
> the three steps separating the two readings are recorded in the implementation notes of this
> file.

```lean
public noncomputable def autEquivDerivation (P : S.CompatibleFirstOrderThickening) :
    P.AutomorphismGroup ≃ Derivation P
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.autEquivDerivation_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionAutomorphisms.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionAutomorphisms.lean#L445). The attribute's comment: “clause (3), that the canonical bijection of `autEquivDerivation` between the automorphisms of a solution and its section-wise derivations is a group isomorphism; the group is not identified with Ext⁰_O(L_f, G), as in the library's Stacks 08UG and Stacks 08UK”.

> **Stacks Project, Tag 08V5, clause (3).** The canonical bijection between the automorphisms
> of a solution and the derivations of that solution is an isomorphism of groups: composition of
> automorphisms is addition of derivations.

```lean
public theorem autEquivDerivation_mul (P : S.CompatibleFirstOrderThickening)
    (a b : P.AutomorphismGroup) :
    autEquivDerivation P (a * b) = autEquivDerivation P a + autEquivDerivation P b
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.autMulEquivExtZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionAutomorphismsExt.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionAutomorphismsExt.lean#L483). The attribute's comment: “clause (3): given a solution, its automorphisms fitting into the diagram of 08V4 form a group canonically isomorphic to Ext⁰_O(L_f, G)”.

> Given a solution `P` of a square-zero extension problem of ringed topoi, the group of
> automorphisms of `P` fitting into the diagram of the problem is canonically isomorphic to
> `Ext⁰_O(L_f, G)`: an automorphism `a` goes to the class whose degree-zero homology
> `Ω_f = H⁰(L_f) ⟶ G` sends `d(x mod G)` to the section of `G` by which `a(x)` differs from `x`;
> composition of automorphisms goes to addition of classes.

```lean
noncomputable def autMulEquivExtZero :
    P.AutomorphismGroup ≃* Multiplicative (S.f.cotangentExt (targetG S) 0)
```

**`Deformation.ToposThickening.RingedToposExtensionProblem.CompatibleFirstOrderThickening.isomorphismClassesAddTorsor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/SolutionIsomorphismClassesExt.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/SolutionIsomorphismClassesExt.lean#L106). The attribute's comment: “clause (2): if a solution exists, the set of isomorphism classes of solutions is principal homogeneous under Ext¹(L_f, G); the element separating two classes is the image of their obstruction class under Ext¹(NL_f, G) = Ext¹(L_f, G)”.

> **Stacks 08V5**, clause (2): if the square-zero extension problem has a solution, the
> isomorphism classes of solutions are a principal homogeneous space under `Ext¹_O(L_f, G)`.

```lean
noncomputable def isomorphismClassesAddTorsor [Nonempty S.CompatibleFirstOrderThickening] :
    AddTorsor (S.f.cotangentExt (targetG S) 1) (IsomorphismClasses S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.23, Tag 08V3](https://stacks.math.columbia.edu/tag/08V3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
