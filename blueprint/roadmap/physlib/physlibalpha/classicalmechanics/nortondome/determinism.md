---
declaration: module
origin: cited
lean: ClassicalMechanics.NortonDome.toNewtonianSystem, ClassicalMechanics.NortonDome.toNewtonianSystem_force, ClassicalMechanics.NortonDome.toNewtonianSystem_equationOfMotion_iff, ClassicalMechanics.NortonDome.toNewtonianSystem_isSolution_iff, ClassicalMechanics.NortonDome.not_isDeterministic, ClassicalMechanics.NortonDome.not_satisfiesFirstLaw, ClassicalMechanics.NortonDome.not_hasLocallyLipschitzForce, ClassicalMechanics.NortonDome.not_hasLipschitzForce
statement: formalized
proof: formalized
---

# The Norton dome and the determinism of Newtonian mechanics

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.Determinism`, [PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean): 10 declarations, 10 with a docstring.

> The Norton dome is a Newtonian system with continuous force that is not deterministic.

## i. Overview

> A particle at rest on the apex of the Norton dome may stay there forever or slide off at any
> instant, in obedience to Newton's second law with a continuous force. This file states what
> that does and does not show, in the terms of `NortonDome.NewtonianSystem`.
>
> The dome is such a system (`toNewtonianSystem`). It is not deterministic
> (`not_isDeterministic`) and it violates the first law (`not_satisfiesFirstLaw`). Since a locally
> Lipschitz force gives determinism, the dome must fail that hypothesis and everything implying
> it, and it does (`not_hasLocallyLipschitzForce`, `not_hasLipschitzForce`, `not_hasC2Potential`).
> Its force `m √r` is continuous but has infinite slope at the apex, and its potential is `C¹`
> but not `C²`.
>
> Put together, this is `exists_continuous_force_not_isDeterministic`: a continuous force does
> not make a Newtonian system deterministic, while a locally Lipschitz force, or a `C²`
> potential, does. Newton's laws do not say which requirement, if any, belongs in the definition
> of a Newtonian system. The theorems say what each requirement buys and that the dome is what
> each excludes, and leave the choice open. Malament's proposal, a regularity condition on the
> constraint surface in physical space rather than on the potential, is not formulated here. With
> Peano's theorem, whose proof is pending in Mathlib, the dome has solutions from every initial
> datum (`hasLocalSolutions`), so its failure is one of uniqueness alone.

## ii. Key results

> - `NortonDome.not_isDeterministic`: the dome is not deterministic.
> - `NortonDome.not_satisfiesFirstLaw`: the dome violates the first law.
> - `NortonDome.exists_continuous_force_not_isDeterministic`: Norton's claim, a Newtonian
>   system with a continuous force that is not deterministic.
> - `NortonDome.not_hasLocallyLipschitzForce`, `NortonDome.not_hasLipschitzForce` and
>   `NortonDome.not_hasC2Potential`: the dome satisfies none of the regularity conditions.
> - `NortonDome.toNewtonianSystem` is the dome as a Newtonian system, with
>   `toNewtonianSystem_force`, `toNewtonianSystem_equationOfMotion_iff` and
>   `toNewtonianSystem_isSolution_iff` identifying its force, equation of motion and solutions
>   with those of `NortonDome.Basic`.
> - `NortonDome.hasLocalSolutions` and `NortonDome.exists_hasLocalSolutions_not_isDeterministic`:
>   the dome has local solutions from every initial datum, by Peano's theorem, so its failure of
>   determinism is a failure of uniqueness alone (pending the upstream proof).

## iv. References

> - Norton, J. D., *The dome: an unexpectedly simple failure of determinism*, Philosophy of
>   Science 75 (2008), 786–798.
> - Malament, D. B., *Norton's slippery slope*, Philosophy of Science 75 (2008), 799–816.

## A. The dome as a Newtonian system

> The dome has a differentiable potential, so it is a Newtonian system whose force, equation of
> motion and solutions are by definition those of `NortonDome.Basic`.

**`ClassicalMechanics.NortonDome.toNewtonianSystem`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L89).

> The Norton dome as a conservative Newtonian system on the Euclidean lift of the arc
> length.

```lean
noncomputable def toNewtonianSystem : NewtonianSystem (EuclideanSpace ℝ (Fin 1))
```

**`ClassicalMechanics.NortonDome.toNewtonianSystem_force`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L96).

> The force of the dome as a Newtonian system is its force.

```lean
lemma toNewtonianSystem_force : S.toNewtonianSystem.force = S.force
```

**`ClassicalMechanics.NortonDome.toNewtonianSystem_equationOfMotion_iff`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L99).

> The equation of motion of the dome as a Newtonian system is its equation of motion.

```lean
lemma toNewtonianSystem_equationOfMotion_iff (r : Time → EuclideanSpace ℝ (Fin 1)) :
    S.toNewtonianSystem.EquationOfMotion r ↔ S.EquationOfMotion r
```

**`ClassicalMechanics.NortonDome.toNewtonianSystem_isSolution_iff`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L103).

> The solutions of the dome as a Newtonian system are its solutions.

```lean
lemma toNewtonianSystem_isSolution_iff (r : Time → EuclideanSpace ℝ (Fin 1)) :
    S.toNewtonianSystem.IsSolution r ↔ S.IsSolution r
```

## B. The properties the dome fails

### B.1. Determinism and the first law

> Determinism fails by the non-uniqueness proved in `NortonDome.Solution`. The first law fails
> along the motion leaving the apex at the instant `1`: at the instant `0` it is at rest at the
> apex, where the force vanishes, and at the instant `2` it is off the apex.

**`ClassicalMechanics.NortonDome.not_isDeterministic`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L123).

> The Norton dome is not deterministic.

```lean
lemma not_isDeterministic : ¬ S.toNewtonianSystem.IsDeterministic
```

**`ClassicalMechanics.NortonDome.not_satisfiesFirstLaw`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L130).

> The Norton dome violates Newton's first law, read as a statement about intervals of time:
> a particle at rest at the apex, where the force vanishes, need not stay there.

```lean
lemma not_satisfiesFirstLaw : ¬ S.toNewtonianSystem.SatisfiesFirstLaw
```

### B.2. The regularity conditions

> The force is not Lipschitz on any closed ball about the apex, `not_lipschitzOnWith_force`,
> hence not locally Lipschitz; the two stronger conditions imply a locally Lipschitz force, so
> they fail too.

**`ClassicalMechanics.NortonDome.not_hasLocallyLipschitzForce`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L151).

> The force of the Norton dome is not locally Lipschitz: it is not Lipschitz on any
> neighbourhood of the apex.

```lean
lemma not_hasLocallyLipschitzForce : ¬ S.toNewtonianSystem.HasLocallyLipschitzForce
```

**`ClassicalMechanics.NortonDome.not_hasLipschitzForce`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L159).

> The force of the Norton dome is not Lipschitz.

```lean
lemma not_hasLipschitzForce : ¬ S.toNewtonianSystem.HasLipschitzForce
```

**`ClassicalMechanics.NortonDome.not_hasC2Potential`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L163).

> The potential of the Norton dome is not `C²`.

```lean
lemma not_hasC2Potential : ¬ S.toNewtonianSystem.HasC2Potential
```

## C. Norton's claim

**`ClassicalMechanics.NortonDome.exists_continuous_force_not_isDeterministic`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean#L175).

> Norton's claim: there is a conservative Newtonian system, with a continuous force,
> which is not deterministic. The witness is the dome with unit mass and unit gravitational
> acceleration.

```lean
lemma exists_continuous_force_not_isDeterministic :
    ∃ N : NewtonianSystem (EuclideanSpace ℝ (Fin 1)), Continuous N.force ∧ ¬ N.IsDeterministic
```

## D. Existence without uniqueness

> The force is continuous and the configuration space is finite-dimensional, so by Peano's
> theorem, `NewtonianSystem.hasLocalSolutions_of_continuous_force`, every initial datum has a
> local solution: the failure of determinism is purely one of uniqueness. Pending the proof of
> Peano's theorem in Mathlib, these results are informal lemmas.

## Depends on

- [The Norton dome](basic.md)
- [Conservative Newtonian systems and determinism](newtoniansystem.md)

## Proof depends on

- [The motions of the Norton dome and the failure of uniqueness](solution.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Determinism.lean)
