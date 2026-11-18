---
declaration: section
origin: cited
lean: OAI.Solenoidal.sheet_theorem, OAI.AlternatingNS.alternating, OAI.VelocityDetection.main_result, OAI.BoxTransport.Routing.balanced_box_routing, OAI.BalancedTransport.balanced_three_stack_realization
statement: formalized
proof: formalized
---

# 376. Universal computation in forced Navier–Stokes flows

9 manuscripts and 6 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs viscous incompressible flows starting from rest on a fixed flat three-dimensional domain that perform universal computation under smooth external forcing. A terminating compiler turns a Turing machine and input into a finite program for the force, so a designated particle reaches a fixed region exactly when the machine halts. The viscosity is fixed, positive and computable.

## Finite Instructions and Solenoidal Shear Flows

We realize finite reciprocal affine instruction maps by smooth incompressible shear flows on a flat three-torus. Applied to a reversible one-head recorder with a finite transition table, this gives a complete machine-to-fluid construction: a fixed particle enters a fixed open strip exactly when a given machine halts, with zero initial velocity, zero pressure, and a solenoidal mean-zero force that is periodic after initialization. The construction acts on full closed rectangles and controls every intermediate trajectory. Separate heights resolve overlap between sources and targets, and an endpoint-size estimate controls all excursions independently of the reciprocal scaling factor.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/manuscript.pdf).

## A Fixed Particle Test for Computation in a Forced Viscous Flow

We construct smooth external forces for incompressible Navier–Stokes flow on a fixed flat three-torus at any fixed positive computable viscosity, from zero initial velocity, such that a fixed particle enters a fixed open set exactly when a prescribed Turing machine halts. Every mixed derivative of the force and velocity is bounded and square-integrable in time in spatial supremum norm. The construction uses the machine's ordinary instructions, records their history in a third coordinate, and compensates for finer spatial gates by longer time steps.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/manuscript.pdf).

## Universal Computation with Eventually Stationary Navier–Stokes Forcing

At every fixed positive computable viscosity, we construct smooth mean-zero forces on the flat three-torus that become stationary after time one and make a fixed particle, initially in a fluid at rest, enter a fixed open set exactly when a prescribed Turing machine halts. The force has bounded derivatives of every order and a finite effective description. A reversible recording table is realized on whole planar rectangles by Hamiltonian motions, then driven by a mean-zero spatial clock. Separate choices give periodic forcing from time zero or a force whose derivatives are square-integrable in time.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf).

## Geometric Programs for Solenoidal Forcing

We construct smooth solenoidal mean-zero forces, periodic from time zero, for which a fixed particle on a flat three-torus reaches a fixed open strip exactly when a given machine halts. The initial fluid velocity and the pressure are zero. We also realize positive diagonal maps on coding sheets by incompressible shears, with explicit normal compensation for changes of planar area, and reciprocal maps on whole boxes of positive thickness. Complete local inverses, initialization rules, and intermediate trajectory bounds connect these geometric constructions to finite computations.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Prefix Instructions and Incompressible Flows

Finite prefix instructions may change area and erase information. We give explicit history processors and smooth incompressible motions that retain that information and realize every instruction on its full domain. A first application assigns each machine and finite input a smooth mean-zero force on the flat unit three-torus, at any fixed positive computable viscosity. The solution starts from rest; a fixed particle enters a fixed open strip exactly when the machine halts. The force repeats with period one after an initial loading interval. We then prove alternative realizations using full boxes, normal compensation, invariant planes, and a spatial clock. The constructions specify their initialization, comparison class, derivative bounds, and continuous-time observation. Exact formulas and effective cutoffs provide finite descriptions of the fields and all their derivatives.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/manuscript.pdf).

## Computation under Rapidly Vanishing Navier–Stokes Forcing

At any fixed positive computable viscosity, smooth forces can make a fixed fluid particle detect the halting of an arbitrary machine, starting from rest, while every mixed derivative of the force and velocity decreases faster than every inverse power of time. We give three complete memory constructions: compact moving curls, alternating fractional coordinates, and a periodic lattice on the flat three-torus. Each machine step takes one unit of physical time. The constructions retain earlier records at separated spatial scales and use an exact open detector with a shrinking signal.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Velocity-Field Detection of Computation in Forced Navier–Stokes Flows

We construct smooth forces for three-dimensional incompressible Navier–Stokes flow, from rest at any fixed positive computable viscosity, whose velocity field detects whether a prescribed machine halts. On the unit flat torus, a pointwise test of the third velocity component uses successively shorter stirring intervals in a fixed spatial region. On $\mathbb R^2\times\mathbb T$, an integral test uses an expanding array of translation regions and a force with globally bounded mixed derivatives. The vertical velocity solves an advection–diffusion equation: short bursts control its pointwise error in the first construction, and a moving cutoff controls the total escaped mass in the second.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Scalar Potentials and Slow Clocks for Forced Fluid Computation

We construct smooth forces of fixed compact spatial support for three-dimensional incompressible Navier–Stokes flow from rest whose particle at the origin detects halting by entering a fixed half-space. Every mixed derivative of the force and velocity decays at rate $O((1+t)^{-1-j})$ for time order *j*. Three scalar potentials lift a coded rectangle, perform its instruction, and lower its image; an unbounded logarithmic clock supplies the decay. We also realize area-changing prefix instructions on an invariant torus plane, and construct a planar Hamiltonian processor admitting periodic forcing, stationary forcing after startup, and a velocity-field detector through a companion diffusion theorem.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/manuscript.pdf).

## Incompressible Box Transport and Finite Computation

We realize finite positive diagonal affine maps of determinant one by effective smooth incompressible flows on neighborhoods of entire closed rational solid boxes. The source and target families are each disjoint, but may overlap each other. The construction uses localized curls, evacuation to storage and obstacle detours. A balanced three-stack recorder then assigns every machine and finite input a smooth Navier–Stokes force with one compact spatial support, periodic after a loading interval, at any fixed positive computable viscosity. The fluid starts at rest, and one fixed particle enters one fixed open cube exactly when the machine halts. Further constructions give fixed torus charts, periodicity from time zero, alternative history guards and bounded or slab observers. Onto slow clocks yield separate decaying forces. Each construction includes an all-time observation proof, effective derivative bounds and a stated pressure comparison class.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Incompressible-Box-Transport-and-Finite-Computation-October-6-2026/manuscript.pdf).

## The Lean formalization

The formalization realizes finite families of prescribed positive diagonal maps on coding sheets by smooth incompressible flows on a flat three-torus. At every positive computable viscosity, it supplies a solution starting from rest with zero pressure and a force that is divergence free, has spatial mean zero, and is one-periodic from time zero. Each map acts on every point of its source sheet, and the construction provides effective bounds for all mixed derivatives.

This selected statement covers the sheet programs. The paper's fixed-particle halting detector and its reciprocal maps on solid boxes are outside its scope.

The formalization proves that a fluid particle can detect arbitrary finite-machine halting using alternating-coordinate memory in smooth incompressible Navier–Stokes flows whose velocity and force decay faster than every inverse power of time, including every mixed derivative. For each fixed positive computable viscosity, the construction starts from rest and provides effective forces, unique material trajectories, and an exact equivalence between entering a fixed open detector and halting.

The velocity and force share one compact support for every machine and input. The solution-uniqueness assertion uses the stated energy comparison class.

The formalization constructs smooth forced three-dimensional Navier–Stokes flows from rest whose velocity fields detect whether a prescribed machine halts, at any positive computable viscosity. On the unit flat torus, halting is equivalent to the vertical velocity exceeding $1/2$ somewhere in a fixed observation strip. On $\mathbb R^2\times\mathbb T$, it is equivalent to the integral of the nonnegative vertical velocity over the observation half-plane times the circle exceeding $1/2$.

The torus force is confined to a fixed horizontal region. The cylindrical force has globally bounded mixed derivatives and compact horizontal support on every finite time interval. Both constructions have effective descriptions and uniqueness within their respective smooth solution-comparison classes.

The formalization realizes finitely many positive diagonal affine maps of determinant one between rational solid boxes by a smooth compactly supported divergence-free flow. Source boxes are pairwise disjoint and target boxes are pairwise disjoint, while overlap between the two families is allowed. Each map holds on a neighborhood of the entire source box, and the velocity is supported in the middle half of the time interval.

It also encodes every finite machine and input in a smooth, compactly supported incompressible Navier–Stokes flow on $\mathbb R^3$ starting from rest: the particle initially at $(4,0,0)$ enters the fixed open box $(-1,2)^3$ exactly when the machine halts. One velocity works for every viscosity $\nu>0$, with zero pressure and force $f_0+\nu f_1$. Velocity and force have bounded mixed derivatives and are one-periodic after time one; the repeated velocity depends only on the machine. The force is computable for computable $\nu$. Velocity is unique among smooth zero-data solutions with $u\in C_tH_x^2\cap C_t^1L_x^2$, bounded $u$ and $\nabla u$ on finite time intervals, and pressure modulo a function of time in $C_tH_x^1$.

## Lean: Positive diagonal programs on incompressible coding sheets

```lean
theorem sheet_theorem {N : ℕ} (D : SheetData N) (ν : ℝ)
    (hν : 0 < ν) (hνcomp : ComputableReal ν) :
    ∃ f u : Field, ∃ X : ℝ → Space → Space,
      SpatiallyPeriodic f ∧ SpatiallyPeriodic u ∧
      Smooth f ∧ Smooth u ∧ Effective f ∧
      MeanZero f ∧ DivergenceFree f ∧ OnePeriodic f ∧
      ClassicalSolution ν f u (fun _ _ => 0) ∧
      (∀ v : Field, ∀ p : Pressure, ClassicalSolution ν f v p →
        ∀ t, 0 ≤ t → ∀ x, v t x = u t x ∧ p t x = 0) ∧
      MaterialFlow u X ∧
      (∀ i : Fin N, ∀ y ∈ (D.source i).carrier,
        toTorus (X 1 (sheet y)) =
          toTorus (sheet (diagonalMap (D.source i) (D.target i) (D.ratio i) y))) ∧
      IntegerCollars u ∧ (∀ t x, advection u t x = 0) ∧
      EffectiveBounds f ∧ EffectiveBounds u ∧
      (N = 0 → f = 0 ∧ u = 0)
```

Stated in [SolenoidalSheetPrograms.lean, line 175](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SolenoidalSheetPrograms.lean#L175). Proved in [lean/OAI/MathematicalPhysics/SheetFlows/SheetProgram.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/SheetFlows/SheetProgram.lean#L15).

## Lean: Rapidly decaying alternating-coordinate memory

```lean
theorem alternating (ν : ℝ) (hν : 0 < ν) (hc : ComputableReal ν) :
    AlternatingConclusion ν
```

Stated in [NavierStokesAlternating.lean, line 239](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/NavierStokesAlternating.lean#L239). Proved in [lean/OAI/MathematicalPhysics/AlternatingFlow/Main.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/AlternatingFlow/Main.lean#L11).

## Lean: Pointwise and integral velocity-field detection of halting

```lean
theorem main_result :
    ∃ B : ℕ, 0 < B ∧
      (∀ s : ℝ, |deriv (deriv SmoothBump.profile) s| ≤ (B:ℝ)) ∧
    ∀ (ν : ℝ), 0 < ν → ComputableReal ν →
    ∀ (b N : ℕ) [NeZero b] [NeZero N]
      (M : TM0.Machine (Fin b) (Fin N)) (w : List (Fin b)),
    ∃ (Ftor Fcyl : ℝ → VectorField 3),
      (compile B M w).Represents .torus Ftor ∧
      (compile B M w).Represents .cylinder Fcyl ∧
      (ContDiff ℝ ∞ (uncurry (Ftor ν)) ∧
        (∀ t, FactorsThrough (Ftor ν t) PeriodicSpace.cover) ∧
        (∃ K : Set (Coord 2), IsCompact K ∧ (∀ X ∈ K, ∀ i, X i ∈ Ioo (0:ℝ) 1) ∧
          ∀ t X, PeriodicSpace.cover (horizontal X) ∉ PeriodicSpace.cover '' K → Ftor ν t X = 0) ∧
        (∀ T d, ∃ C : ℝ, 0 ≤ C ∧ ∀ t ∈ Icc (0:ℝ) T, ∀ X,
          ‖iteratedFDeriv ℝ d (uncurry (Ftor ν)) (t,X)‖ ≤ C) ∧
        ∃ u : VectorField 3,
          ContDiff ℝ ∞ (uncurry u) ∧ TorusClass.ComparisonClass u (fun _ _ => 0) ∧
          NavierStokes ν u (fun _ _ => 0) (Ftor ν) ∧
          (Observation.torusEvent u ↔ (TM0.eval M w).Dom) ∧
          ∀ (v : VectorField 3) (p : ScalarField 3), TorusClass.ComparisonClass v p →
            NavierStokes ν v p (Ftor ν) →
            ∀ t ≥ 0, (∀ X, v t X = u t X) ∧ (∀ X, p t X = 0)) ∧
      (ContDiff ℝ ∞ (uncurry (Fcyl ν)) ∧
        UniformDerivatives.Bounded (fun _ : Unit => uncurry (Fcyl ν)) ∧
        (∀ t X z, Fcyl ν t (update X 2 z) = Fcyl ν t X) ∧
        (∀ T : ℝ, ∃ K : Set (Coord 2), IsCompact K ∧ ∀ t ∈ Icc (0:ℝ) T,
          ∀ X : Coord 3, horizontal X ∉ K → Fcyl ν t X = 0) ∧
        ∃ u : VectorField 3,
          ContDiff ℝ ∞ (uncurry u) ∧
          Cylinder.ComparisonClass (fun t x => u t (Cylinder.join x)) (fun _ _ => 0) ∧
          NavierStokes ν u (fun _ _ => 0) (Fcyl ν) ∧
          (∀ t ≥ 0, (∀ x, 0 ≤ u t (Cylinder.join x) 2) ∧
            Integrable (fun x => u t (Cylinder.join x) 2) Cylinder.measure) ∧
          (Observation.planeEvent u ↔ (TM0.eval M w).Dom) ∧
          ∀ (v : VectorField 3) (p : ScalarField 3),
            Cylinder.ComparisonClass (fun t x => v t (Cylinder.join x))
              (fun t x => p t (Cylinder.join x)) →
            NavierStokes ν v p (Fcyl ν) →
            ∀ t ≥ 0, (∀ X, v t X = u t X) ∧ (∀ X, p t X = 0))
```

Stated in [NavierStokesVelocity.lean, line 1232](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/NavierStokesVelocity.lean#L1232). Proved in [lean/OAI/MathematicalPhysics/NavierStokes/VelocityDetection/MainResult.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/NavierStokes/VelocityDetection/MainResult.lean#L11).

## Lean: Incompressible transport of solid boxes

```lean
theorem balanced_box_routing
    (n : ℕ) (a b h k : Fin n → RationalSpace)
    (hh : ∀ i j, 0 < h i j) (hk : ∀ i j, 0 < k i j)
    (ha : Pairwise fun i j => Disjoint (solidBox (a i) (h i)) (solidBox (a j) (h j)))
    (hb : Pairwise fun i j => Disjoint (solidBox (b i) (k i)) (solidBox (b j) (k j)))
    (hvol : ∀ i, ∏ j : Fin 3, k i j / h i j = 1) :
    ∃ U : Field, ∃ Φ : ℝ → Space → Space,
      AdmissibleField U ∧ IsGlobalFlow U Φ ∧ Delivers a b h k Φ
```

Stated in [BalancedBoxRouting.lean, line 84](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BalancedBoxRouting.lean#L84). Proved in [lean/OAI/Analysis/BoxTransport/Routing.lean, line 172](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/BoxTransport/Routing.lean#L172).

## Lean: Finite computation in a balanced zero-data fluid flow

```lean
theorem balanced_three_stack_realization :
    ∃ U f₀ f₁ : Family Velocity,
    ∃ X : Family MaterialFlow,
    ∃ repeated : FiniteMachine → Velocity,
      EffectiveFamily U ∧ EffectiveFamily f₀ ∧ EffectiveFamily f₁ ∧
      (∀ M, Function.Periodic (repeated M) 1) ∧
      ∀ (M : FiniteMachine) (w : Input M),
        Smooth (U M w) ∧ Smooth (f₀ M w) ∧ Smooth (f₁ M w) ∧
        f₀ M w = inertialCoefficient (U M w) ∧
        f₁ M w = viscousCoefficient (U M w) ∧
        CommonCompactSupport (U M w) (f₀ M w) (f₁ M w) ∧
        BoundedMixed (U M w) ∧
        PeriodicAfterOne (U M w) ∧
        (∀ t, 1 ≤ t → ∀ x, U M w t x = repeated M t x) ∧
        ComparisonClass (U M w) (fun _ _ => 0) ∧
        IsMaterialFlow (U M w) (X M w) ∧
        ((∃ t : ℝ, 0 ≤ t ∧ X M w t fixedLabel ∈ observer) ↔ Halts M w) ∧
        ∀ ν : ℝ, 0 < ν →
          let f := affineForce (f₀ M w) (f₁ M w) ν
          ZeroDataSolution ν f (U M w) (fun _ _ => 0) ∧
          Smooth f ∧ BoundedMixed f ∧ PeriodicAfterOne f ∧
          UniqueInComparison ν f (U M w) ∧
          (ComputableReal ν → EffectiveFieldIn ∅ f) ∧
          (∀ name : ℕ → ℚ, RealName name ν → EffectiveFieldIn {nameOracle name} f)
```

Stated in [BalancedThreeStack.lean, line 211](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BalancedThreeStack.lean#L211). Proved in [lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/MainResult.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/MainResult.lean#L12).

## Lean: Effective finite computation detected by a fixed particle

```lean
theorem balanced_three_stack_realization :
    ∃ U f₀ f₁ : Family Velocity,
    ∃ X : Family MaterialFlow,
    ∃ repeated : FiniteMachine → Velocity,
      EffectiveFamily U ∧ EffectiveFamily f₀ ∧ EffectiveFamily f₁ ∧
      (∀ M, Function.Periodic (repeated M) 1) ∧
      ∀ (M : FiniteMachine) (w : Input M),
        Smooth (U M w) ∧ Smooth (f₀ M w) ∧ Smooth (f₁ M w) ∧
        f₀ M w = inertialCoefficient (U M w) ∧
        f₁ M w = viscousCoefficient (U M w) ∧
        CommonCompactSupport (U M w) (f₀ M w) (f₁ M w) ∧
        BoundedMixed (U M w) ∧
        PeriodicAfterOne (U M w) ∧
        (∀ t, 1 ≤ t → ∀ x, U M w t x = repeated M t x) ∧
        ComparisonClass (U M w) (fun _ _ => 0) ∧
        IsMaterialFlow (U M w) (X M w) ∧
        ((∃ t : ℝ, 0 ≤ t ∧ X M w t fixedLabel ∈ observer) ↔ Halts M w) ∧
        ∀ ν : ℝ, 0 < ν →
          let f := affineForce (f₀ M w) (f₁ M w) ν
          ZeroDataSolution ν f (U M w) (fun _ _ => 0) ∧
          Smooth f ∧ BoundedMixed f ∧ PeriodicAfterOne f ∧
          UniqueInComparison ν f (U M w) ∧
          (ComputableReal ν → EffectiveFieldIn ∅ f) ∧
          (∀ name : ℕ → ℚ, RealName name ν → EffectiveFieldIn {nameOracle name} f)
```

Stated in [ForcedNavierStokesComputation.lean, line 206](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ForcedNavierStokesComputation.lean#L206). Proved in [lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/MainResult.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/NavierStokes/BalancedTransport/MainResult.lean#L12).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/376.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/376.md)
