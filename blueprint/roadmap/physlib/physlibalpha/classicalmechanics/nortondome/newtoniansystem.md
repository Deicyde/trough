---
declaration: module
origin: cited
lean: ClassicalMechanics.NewtonianSystem, ClassicalMechanics.NewtonianSystem.m_ne_zero, ClassicalMechanics.NewtonianSystem.force, ClassicalMechanics.NewtonianSystem.EquationOfMotion, ClassicalMechanics.NewtonianSystem.IsSolution, ClassicalMechanics.NewtonianSystem.IsSolution.differentiable, ClassicalMechanics.NewtonianSystem.IsSolution.deriv_differentiable, ClassicalMechanics.NewtonianSystem.IsSolution.equationOfMotion
statement: formalized
proof: formalized
---

# Conservative Newtonian systems and determinism

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.NewtonianSystem`, [PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean): 30 declarations, 30 with a docstring.

> Conservative Newtonian systems: a locally Lipschitz force gives determinism.

## i. Overview

> A conservative Newtonian system is a point mass `m` in a configuration space `X` under a
> potential `V`, with equation of motion `m r̈ = -∇V(r)`. Physics takes for granted that position
> and velocity at one instant fix the motion at all instants. This file makes that a theorem and
> states what it costs.
>
> The main result is `NewtonianSystem.isDeterministic_of_hasLocallyLipschitzForce`: if the force
> is locally Lipschitz, two solutions with the same position and velocity at one instant coincide
> at every instant; in the form usually quoted,
> `NewtonianSystem.isDeterministic_of_hasC2Potential`, a `C²` potential suffices. Continuity of
> the force is not enough: the Norton dome has a continuous force and a `C¹` potential, and a
> particle at rest on its apex may stay or leave at any time (see `NortonDome.Determinism`).
>
> The `NewtonianSystem` defined here asks only for a differentiable potential, the least under
> which the equation of motion makes sense. Newton's laws, as stated, are silent on how regular
> the force must be, and the dome shows that without some regularity the equation does not
> determine the motion. A definition that is to be deterministic must add something the laws do
> not state, a regularity condition on the force or a restriction on the admissible motions;
> whether that is part of the theory or a choice about it is debated. Each candidate condition is
> a separate predicate, so that what it buys is a theorem, and the file takes no side. The
> predicates are:
>
> - `IsDeterministic`: position and velocity at one instant fix the solution.
> - `SatisfiesFirstLaw`: a body at rest where the force vanishes stays at rest. It follows from
>   determinism and is the form of the first law the dome violates. The interval reading follows
>   from the second law for every system (`IsSolution.deriv_eq_of_force_eq_zero_on`, section B.3).
> - `HasLocallyLipschitzForce`: the hypothesis of the ODE uniqueness theorem. `HasLipschitzForce`
>   and `HasC2Potential` are the stronger conditions usually assumed; each implies it and neither
>   implies the other.
> - `HasLocalSolutions`: existence, kept separate. For a continuous force on a finite-dimensional
>   configuration space it follows from Peano's theorem, whose proof is pending in Mathlib;
>   section E derives it from the statement in `NortonDome.PeanoExistence`, informally.
>
> The proof of determinism turns the equation of motion into the first-order system
> `(r, v)' = (v, F(r)/m)` on `X × X`, applies Mathlib's local uniqueness theorem for integral
> curves, and extends to all time by connectedness of the real line. So continuity buys
> existence and local Lipschitz continuity buys uniqueness; the file records what each condition
> does, not which one is right.

## ii. Key results

> - `NewtonianSystem.isDeterministic_of_hasLocallyLipschitzForce`: a locally Lipschitz force
>   gives determinism, hence `NewtonianSystem.satisfiesFirstLaw_of_hasLocallyLipschitzForce`
>   the first law. `NewtonianSystem.isDeterministic_of_hasC2Potential` and
>   `NewtonianSystem.isDeterministic_of_hasLipschitzForce` are the forms usually quoted; the
>   chain of implications is drawn in section D.3.
> - `NewtonianSystem.ODE_solution_unique_of_locallyLipschitz`: integral curves of a locally
>   Lipschitz vector field through a common point coincide for all time.
> - `NewtonianSystem`, `NewtonianSystem.force`, `NewtonianSystem.EquationOfMotion` and
>   `NewtonianSystem.IsSolution`: the system, the force `-∇V`, Newton's second law, and its
>   twice differentiable solutions; `NewtonianSystem.isSolution_const` is rest at an
>   equilibrium.
> - `NewtonianSystem.IsSolution.deriv_eq_of_force_eq_zero_on`: the first law read on an
>   interval, a consequence of the second law for every system.
> - `NewtonianSystem.IsDeterministic`, `NewtonianSystem.SatisfiesFirstLaw`,
>   `NewtonianSystem.HasLocallyLipschitzForce`, `NewtonianSystem.HasLipschitzForce` and
>   `NewtonianSystem.HasC2Potential`: the predicates, with
>   `NewtonianSystem.HasLipschitzForce.hasLocallyLipschitzForce` and
>   `NewtonianSystem.HasC2Potential.hasLocallyLipschitzForce`.
> - `NewtonianSystem.HasLocalSolutions` and `NewtonianSystem.hasLocalSolutions_of_continuous_force`:
>   Peano's theorem for Newtonian systems, a continuous force on a finite-dimensional
>   configuration space gives local solutions (pending the upstream proof).

## iv. References

> - Earman, J., *A Primer on Determinism*, Reidel (1986).
> - Laplace, P.-S., *Essai philosophique sur les probabilités* (1814).
> - Montague, R., *Deterministic theories*, in *Formal Philosophy*, Yale University Press (1974).
> - Norton, J. D., *The dome: an unexpectedly simple failure of determinism*, Philosophy of
>   Science 75 (2008), 786–798.
> - `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Solution` (the same uniqueness argument
>   for the pendulum).

## A. Conservative Newtonian systems

### A.1. The structure

> The potential is asked to be differentiable and no more, so that the force `-∇V` exists and the
> equation of motion can be written pointwise; further regularity is added in section C. Physlib's
> general notion is `ClassicalMechanics.PointParticle.NewtonianSystem`, finitely many particles
> with explicit forces in a reference frame. The structure here is a single mass in a potential,
> which is all the dome needs; the two live in different namespaces and no file opens both.

**`ClassicalMechanics.NewtonianSystem`**, a structure, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L141).

> A conservative Newtonian system on the configuration space `X`: a point mass `m` in a
> differentiable potential `V`. Its equation of motion is Newton's second law `m r̈ = -∇V(r)`.

```lean
structure NewtonianSystem (X : Type) [NormedAddCommGroup X] [InnerProductSpace ℝ X]
    [CompleteSpace X] where
  /-- The mass. -/
  m : ℝ
  /-- The potential. -/
  potential : X → ℝ
  m_pos : 0 < m
  potential_differentiable : Differentiable ℝ potential
```

**`ClassicalMechanics.NewtonianSystem.m_ne_zero`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L156).

> The mass of a Newtonian system is not equal to zero.

```lean
lemma m_ne_zero : S.m ≠ 0
```

### A.2. The force and the equation of motion

**`ClassicalMechanics.NewtonianSystem.force`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L165).

> The force of a Newtonian system, minus the gradient of the potential.

```lean
noncomputable def force (x : X) : X
```

**`ClassicalMechanics.NewtonianSystem.EquationOfMotion`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L169).

> Newton's second law for a Newtonian system: at every instant `m r̈` equals the force at
> the position.

```lean
def EquationOfMotion (r : Time → X) : Prop
```

### A.3. Solutions

> A solution is a twice differentiable curve, position and velocity both differentiable, satisfying
> the equation of motion: the regularity of `ClassicalMechanics.ReferenceFrame.Particle` and the
> least under which the acceleration exists. It is demanded because the pointwise equation, whose
> derivatives are zero wherever they do not exist, admits rough accidental solutions. Continuity of
> the acceleration is not demanded; for a continuous force it is automatic.

**`ClassicalMechanics.NewtonianSystem.IsSolution`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L186).

> A solution of a Newtonian system is a twice differentiable curve, its position and velocity
> both differentiable, satisfying the equation of motion.

```lean
def IsSolution (r : Time → X) : Prop
```

**`ClassicalMechanics.NewtonianSystem.IsSolution.differentiable`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L190).

> The position along a solution is differentiable.

```lean
lemma IsSolution.differentiable {S : NewtonianSystem X} {r : Time → X} (h : S.IsSolution r) :
    Differentiable ℝ r
```

**`ClassicalMechanics.NewtonianSystem.IsSolution.deriv_differentiable`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L194).

> The velocity along a solution is differentiable.

```lean
lemma IsSolution.deriv_differentiable {S : NewtonianSystem X} {r : Time → X}
    (h : S.IsSolution r) : Differentiable ℝ (∂ₜ r)
```

**`ClassicalMechanics.NewtonianSystem.IsSolution.equationOfMotion`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L198).

> A solution satisfies the equation of motion.

```lean
lemma IsSolution.equationOfMotion {S : NewtonianSystem X} {r : Time → X}
    (h : S.IsSolution r) : S.EquationOfMotion r
```

**`ClassicalMechanics.NewtonianSystem.isSolution_const`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L202).

> The curve at rest at a point where the force vanishes is a solution.

```lean
lemma isSolution_const {x : X} (hx : S.force x = 0) : S.IsSolution (fun _ => x)
```

## B. Determinism and the first law

### B.1. The properties

> Determinism is the statement that position and velocity at one instant fix the motion at all
> instants. The first law, in the reading that says more than the second law, is the statement
> that a body at rest where no force acts stays at rest; section B.3 compares the readings. Both
> are properties of the system, not of a motion.
>
> The definition of determinism is the naive one. Laplace's formulation is about knowledge; the
> notion used since Montague and Earman is about models, a theory being deterministic if any two
> models agreeing at one instant agree at every instant. `IsDeterministic` is that notion, with
> the models taken to be the twice differentiable solutions of one system, defined for all time,
> and the state taken to be position and velocity. Four things follow.
>
> - It is a property of one system. That Newtonian mechanics is deterministic is a claim about
>   every system in some class, and which class is what this folder is about.
> - It is uniqueness only. A system with no solution from some initial datum, or with solutions
>   not defined for all time, counts as deterministic here, whereas on Earman's account such
>   failures of existence count against determinism. Existence is kept separate, as
>   `HasLocalSolutions`.
> - It is relative to the class of solutions. Demanding smooth or analytic solutions would
>   exclude the departing motions of the dome, which vanish on a half-line and are not `C⁴`, and
>   so restore uniqueness by fiat.
> - It does not distinguish future from past. The time-reversed motions of the dome arrive at
>   rest on the apex and stay, so the state there fixes neither past nor future; Earman's
>   futuristic and historical determinism both fail.

**`ClassicalMechanics.NewtonianSystem.IsDeterministic`**, a def, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L246).

> A Newtonian system is deterministic if any two solutions with the same position and
> velocity at some instant coincide. This is uniqueness of twice differentiable solutions
> defined for all time, in both directions of time and without existence; see section B.1.

```lean
def IsDeterministic : Prop
```

**`ClassicalMechanics.NewtonianSystem.SatisfiesFirstLaw`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L252).

> A Newtonian system satisfies the first law if a solution at rest, at some instant, at a
> point where the force vanishes stays at that point at all instants.

```lean
def SatisfiesFirstLaw : Prop
```

### B.2. Determinism implies the first law

> The curve staying at the equilibrium is a solution with the same position and velocity as the
> given one at the given instant, so by determinism it is the given one.

**`ClassicalMechanics.NewtonianSystem.IsDeterministic.satisfiesFirstLaw`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L265).

> A deterministic Newtonian system satisfies the first law.

```lean
lemma IsDeterministic.satisfiesFirstLaw {S : NewtonianSystem X} (h : S.IsDeterministic) :
    S.SatisfiesFirstLaw
```

### B.3. The interval reading of the first law

> The first law can be read instantaneously (no force at an instant, no acceleration then), with
> an interval in the hypothesis (no force on an interval, constant velocity on it), or with an
> interval in the conclusion (at rest at an instant where no force acts, at rest forever). The
> first two follow from the second law for every system, the second being the lemma below, and
> both hold for the dome. The third, `SatisfiesFirstLaw`, is determinism at an equilibrium; it is
> what the dome violates and what Norton's argument is about, so it is the reading taken here.

**`ClassicalMechanics.NewtonianSystem.IsSolution.deriv_eq_of_force_eq_zero_on`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L288).

> The first law read on an interval: if the force vanishes along a solution throughout the
> interval `[a, b]`, the velocity is constant on it. This is a consequence of the second law
> alone, and holds for every system.

```lean
lemma IsSolution.deriv_eq_of_force_eq_zero_on {S : NewtonianSystem X} {r : Time → X}
    (hr : S.IsSolution r) {a b : Time} (hF : ∀ t ∈ Set.Icc a b, S.force (r t) = 0) :
    ∀ t ∈ Set.Icc a b, ∂ₜ r t = ∂ₜ r a
```

## C. Regularity conditions

> The hypothesis of the ODE uniqueness theorem is a locally Lipschitz force,
> `HasLocallyLipschitzForce`. The two stronger conditions usually stated are a globally Lipschitz
> force, `HasLipschitzForce`, and a `C²` potential, `HasC2Potential`, whose force is `C¹`.
> Neither implies the other: for example, `x ^ 4` has a `C¹` force of unbounded slope, and
> `x * |x| / 2` has the Lipschitz force `-|x|` but is not `C²`. The structure `NewtonianSystem`
> of section A assumes none of these conditions; they are separate predicates on it.

**`ClassicalMechanics.NewtonianSystem.HasLocallyLipschitzForce`**, a def, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L325).

> A Newtonian system has a locally Lipschitz force if its force is Lipschitz on a
> neighbourhood of every point. This is the hypothesis of the uniqueness theorem for ordinary
> differential equations.

```lean
def HasLocallyLipschitzForce : Prop
```

**`ClassicalMechanics.NewtonianSystem.HasLipschitzForce`**, a def, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L328).

> A Newtonian system has a Lipschitz force if its force is globally Lipschitz.

```lean
def HasLipschitzForce : Prop
```

**`ClassicalMechanics.NewtonianSystem.HasC2Potential`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L333).

> A Newtonian system has a `C²` potential if its potential is twice continuously
> differentiable; two derivatives are what the uniqueness theory of ordinary differential
> equations uses.

```lean
def HasC2Potential : Prop
```

**`ClassicalMechanics.NewtonianSystem.HasLipschitzForce.hasLocallyLipschitzForce`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L336).

> A Lipschitz force is locally Lipschitz.

```lean
lemma HasLipschitzForce.hasLocallyLipschitzForce (h : S.HasLipschitzForce) :
    S.HasLocallyLipschitzForce
```

**`ClassicalMechanics.NewtonianSystem.HasC2Potential.contDiff_gradient`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L342).

> The gradient of a `C²` potential is `C¹`.

```lean
lemma HasC2Potential.contDiff_gradient (h : S.HasC2Potential) :
    ContDiff ℝ 1 (gradient S.potential)
```

**`ClassicalMechanics.NewtonianSystem.HasC2Potential.hasLocallyLipschitzForce`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L348).

> The force of a system with a `C²` potential is locally Lipschitz.

```lean
lemma HasC2Potential.hasLocallyLipschitzForce (h : S.HasC2Potential) :
    S.HasLocallyLipschitzForce
```

## D. A locally Lipschitz force gives determinism

> The equation of motion becomes the first-order system `(r, v)' = (v, F(r)/m)` on `X × X`. If
> the force is locally Lipschitz so is this vector field, and the local uniqueness theorem
> `ODE_solution_unique_of_eventually` of Mathlib, with the connectedness of the real line, gives
> determinism, as in `SimplePendulum.equationOfMotion_unique`.

### D.1. The phase-space vector field

**`ClassicalMechanics.NewtonianSystem.phaseVectorField`**, a def, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L370).

> The phase-space vector field of a Newtonian system, sending `(r, v)` to `(v, F(r)/m)`.

```lean
noncomputable def phaseVectorField (p : X × X) : X × X
```

**`ClassicalMechanics.NewtonianSystem.phaseVectorField_locallyLipschitz`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L375).

> If the force of a Newtonian system is locally Lipschitz, so is its phase-space vector
> field.

```lean
lemma phaseVectorField_locallyLipschitz (h : LocallyLipschitz S.force) :
    LocallyLipschitz S.phaseVectorField
```

### D.2. The phase curve of a solution

**`ClassicalMechanics.NewtonianSystem.phaseCurve_hasDerivAt`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L390).

> The phase curve `τ ↦ (r t, ṙ t)` (with `t = toRealCLE.symm τ`) of a solution is an
> integral curve of the phase-space vector field.

```lean
lemma phaseCurve_hasDerivAt {r : Time → X} (hr : Differentiable ℝ r)
    (hr' : Differentiable ℝ (∂ₜ r)) (h : S.EquationOfMotion r) (τ : ℝ) :
    HasDerivAt (fun τ : ℝ => (r (toRealCLE.symm τ), ∂ₜ r (toRealCLE.symm τ)))
      (S.phaseVectorField (r (toRealCLE.symm τ), ∂ₜ r (toRealCLE.symm τ))) τ
```

### D.3. The uniqueness theorem

> Local uniqueness makes the set of instants at which two integral curves through a common point
> agree open, continuity makes it closed, and the real line is connected. Applied to the
> phase-space vector field this gives the theorem of the file, and sections B, C and D form one
> chain, each arrow a theorem:
>
> ```
> HasC2Potential ────┐
>                    ├──▶ HasLocallyLipschitzForce ──▶ IsDeterministic ──▶ SatisfiesFirstLaw
> HasLipschitzForce ─┘
> ```
>
> Naming follows Mathlib: `isDeterministic_of_hasC2Potential` is the arrow from
> `HasC2Potential` to `IsDeterministic`.

**`ClassicalMechanics.NewtonianSystem.ODE_solution_unique_of_locallyLipschitz`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L422).

> Integral curves of a locally Lipschitz vector field, defined at all times, which pass
> through the same point at the same instant coincide.

```lean
lemma ODE_solution_unique_of_locallyLipschitz {E : Type} [NormedAddCommGroup E]
    [NormedSpace ℝ E] {v : E → E} (hv : LocallyLipschitz v) {f g : ℝ → E}
    (hf : ∀ τ, HasDerivAt f (v (f τ)) τ) (hg : ∀ τ, HasDerivAt g (v (g τ)) τ)
    {τ₀ : ℝ} (h0 : f τ₀ = g τ₀) : f = g
```

**`ClassicalMechanics.NewtonianSystem.isDeterministic_of_hasLocallyLipschitzForce`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L449).

> The uniqueness theorem for Newtonian systems: a Newtonian system with a locally Lipschitz
> force is deterministic.

```lean
lemma isDeterministic_of_hasLocallyLipschitzForce (h : S.HasLocallyLipschitzForce) :
    S.IsDeterministic
```

**`ClassicalMechanics.NewtonianSystem.isDeterministic_of_hasLipschitzForce`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L464).

> Picard–Lindelöf for Newtonian systems: a Newtonian system with a Lipschitz force is
> deterministic.

```lean
lemma isDeterministic_of_hasLipschitzForce (h : S.HasLipschitzForce) : S.IsDeterministic
```

**`ClassicalMechanics.NewtonianSystem.isDeterministic_of_hasC2Potential`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L468).

> A Newtonian system with a `C²` potential is deterministic.

```lean
lemma isDeterministic_of_hasC2Potential (h : S.HasC2Potential) : S.IsDeterministic
```

**`ClassicalMechanics.NewtonianSystem.satisfiesFirstLaw_of_hasLocallyLipschitzForce`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L472).

> A Newtonian system with a locally Lipschitz force satisfies the first law.

```lean
lemma satisfiesFirstLaw_of_hasLocallyLipschitzForce (h : S.HasLocallyLipschitzForce) :
    S.SatisfiesFirstLaw
```

## E. A continuous force gives local solutions

> Determinism is uniqueness; the complementary existence property is that every initial position
> and velocity is the initial datum of some solution for a short time. For a continuous force on
> a finite-dimensional configuration space this is Peano's theorem applied to the phase-space
> vector field, as Picard–Lindelöf gives it for the pendulum in
> `SimplePendulum.exists_local_solution`. The statement of Peano's theorem is that of
> `NortonDome.PeanoExistence`, pending in Mathlib, so the result here is an informal lemma.

### E.1. Local existence

**`ClassicalMechanics.NewtonianSystem.HasLocalSolutions`**, a def, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L499).

> A Newtonian system has local solutions if for every initial position `x₀` and velocity
> `v₀` there are `ε > 0` and a curve `r` with `r 0 = x₀` and `ṙ 0 = v₀` which, at every time
> within `ε` of the initial instant, is differentiable together with its velocity and satisfies
> the equation of motion.

```lean
def HasLocalSolutions : Prop
```

### E.2. The hypotheses of Peano's theorem

> The phase-space vector field is continuous if the force is, and is bounded on the closed unit
> ball about the initial datum by compactness; a short enough time interval then gives the
> hypotheses of Peano's theorem.

**`ClassicalMechanics.NewtonianSystem.phaseVectorField_continuous`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L516).

> If the force of a Newtonian system is continuous, so is its phase-space vector field.

```lean
lemma phaseVectorField_continuous (hF : Continuous S.force) :
    Continuous S.phaseVectorField
```

**`ClassicalMechanics.NewtonianSystem.exists_isPeano_phaseVectorField`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean#L524).

> For a continuous force on a finite-dimensional configuration space, the time-independent
> phase-space vector field satisfies the hypotheses of Peano's theorem about any initial datum,
> on a short enough symmetric time interval and the closed unit ball.

```lean
lemma exists_isPeano_phaseVectorField [FiniteDimensional ℝ X] (hF : Continuous S.force)
    (p₀ : X × X) :
    ∃ δ > (0 : ℝ), ∃ L : NNReal,
      IsPeano (fun q : ℝ × (X × X) => S.phaseVectorField q.2) (-δ) δ 0 p₀ 1 L
```

### E.3. The existence theorem

> Peano's theorem gives an integral curve through the initial datum, differentiable in the sense
> of `HasDerivWithinAt` on the closed interval, hence with an honest derivative on the open one.
> Its first component, pulled back to `Time` through `Time.toRealCLE`, is the required curve; its
> derivatives are read off with `Time.deriv_comp_toRealCLE_of_hasDerivAt`.

## Depends on

- [Time Derivatives](../../../physlib/spaceandtime/time/derivatives.md)
- [Peano's existence theorem (statements)](peanoexistence.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/NewtonianSystem.lean)
