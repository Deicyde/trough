---
declaration: section
origin: cited
lean: OAI.CylinderCovering.fourPaperMain, OAI.TriangularCovering.main, OAI.RuledApproximation.fullMain
statement: formalized
proof: formalized
---

# 100. Cylinder coverings below the half-area bound

4 manuscripts and 6 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Covers the entire closed regular tetrahedron by finitely many cylinders with compact triangular perpendicular bases whose total area is less than half its smallest orthogonal projection area. This disproves Bang's half-area cylinder-covering bound and the stronger directionwise normalized conjecture in dimension three.

## Finite angular cylinder covers below the half-area bound

A regular tetrahedron admits a finite cylinder covering with compact triangular perpendicular bases whose total area is less than half its minimum orthogonal projection area. This disproves the half-area cylinder-covering conjecture. By affine invariance, the same construction gives a counterexample to the directionwise normalized half-bound for every nondegenerate tetrahedron.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-angular-cylinder-covers-below-the-half-area-bound-September-27-2026/main.pdf); the Lean below formalizes results from it.

## Finite cylinder approximation of ruled sets

We approximate compact ruled families of segments by finitely many cylinders with square intercept tiles and perpendicular-base area at most their integral projection cost plus any positive error. The velocity field is $C^{1}$, and its differential has opposite real eigenvalues whose magnitudes are strictly below the inverse segment half-length; both eigenvalues may vanish. The result includes square-zero differentials with unrestricted shear and fields that pass between the two regimes. It holds for arbitrary compact label sets.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-cylinder-approximation-of-ruled-sets-September-27-2026/main.pdf); the Lean below formalizes results from it.

## Slope-field perturbations of the two-cylinder covering

The two-cylinder covering of a regular tetrahedron can be perturbed to give finite covers with total perpendicular base area strictly below half its minimum projection area. These covers give negative answers to both the half-area question and the directionwise normalized half-bound conjecture. By affine invariance, the directionwise conclusion holds for every nondegenerate tetrahedron.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Slope-field-perturbations-of-the-two-cylinder-covering-September-27-2026/main.pdf); the Lean below formalizes results from it.

## Finite triangular approximation of radial sweeps

We prove that radially aligned segment sweeps admit finite cylinder covers with one triangular base for each interval of any tagged partition. As the mesh tends to zero, the total perpendicular base area converges to a weighted parameter area. An explicit application covers every regular tetrahedron with total base area below half its minimum projection area, giving negative answers to the half-area question and the directionwise normalized 1-Codimensional Cylinder Covering Conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Finite-triangular-approximation-of-radial-sweeps-September-27-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The half-area cylinder-covering conjecture predicts that a cylinder cover of a convex body has total perpendicular-base area at least half its smallest projection area. The formalization constructs finite covers of a regular tetrahedron by cylinders with compact triangular bases whose total area is strictly below that bound. For the explicit small parameter $\varepsilon$, the normalized area is $1/2-(13/6000)\varepsilon^2+O(\varepsilon^4)$, giving the strict saving.

It also gives a counterexample to the directionwise normalized half-bound. The broader Comparator file includes the companion ruled-set and radial-sweep approximation results.

The formalization approximates compact ruled families of line segments by finite cylinder covers with perpendicular-base area at most the integral projection cost plus any prescribed positive error. The selected results cover the stated $C^1$ hyperbolic differential condition, square-zero and nilpotent cases, physical rescalings, logarithmic and product-cell estimates, and singular cases. Compact label sets need not have regular boundary.

The differential and segment-length hypotheses remain part of each result. The aggregate Comparator file also contains the companion tetrahedron counterexamples and radial-sweep estimates.

The formalization proves that every regular tetrahedron has a finite cylinder cover whose total perpendicular-base area is strictly less than half its minimum projection area. It supplies covers with parallelogram bases and also proves the directionwise normalized cost is below one half. These are counterexamples to the two cylinder-covering bounds studied in the paper.

The linked aggregate includes the accompanying explicit angular covers and finite approximation theorems for ruled sets and radial sweeps. The affine extension of the directionwise conclusion to every nondegenerate tetrahedron is outside the selected regular-tetrahedron statements.

The formalization proves finite triangular-cylinder approximation for radially aligned segment sweeps. For every tagged partition of the parameter interval, it constructs one cylinder per interval with the prescribed radial direction, and the total perpendicular-base area converges to the weighted parameter area as the mesh tends to zero. It also covers the corresponding actual swept set under the stated geometric hypotheses.

The same aggregate includes finite cylinder covers of regular tetrahedra below half the minimum projection area. These are the radial approximation and covering consequences relevant to the paper.

## Lean: Cylinder-covering counterexamples and companion approximations

Stated in [CylinderCovering.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CylinderCovering.lean).

```lean
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement
```

Proved in [lean/OAI/Geometry/CylinderCovering/Main.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/CylinderCovering/Main.lean#L44).

## Lean: Explicit triangular-cylinder cover below half area

Stated in [TriangularCovering.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TriangularCovering.lean).

```lean
theorem main : A_min = H ∧ MainAsymptotic ∧ NormalizedCounterexample
```

Proved in [lean/OAI/Geometry/TriangularCovering/Main.lean, line 61](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/TriangularCovering/Main.lean#L61).

## Lean: Ruled-set approximation within the cylinder-covering aggregate

Stated in [CylinderCovering.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CylinderCovering.lean).

```lean
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement
```

Proved in [lean/OAI/Geometry/CylinderCovering/Main.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/CylinderCovering/Main.lean#L44).

## Lean: Finite cylinder approximation for the selected ruled families

Stated in [RuledCovering.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RuledCovering.lean).

```lean
theorem fullMain : FullMain
```

Proved in [lean/OAI/Geometry/RuledCovering/Main.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/RuledCovering/Main.lean#L13).

## Lean: Cylinder-covering counterexamples and approximation results

Stated in [CylinderCovering.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CylinderCovering.lean).

```lean
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement
```

Proved in [lean/OAI/Geometry/CylinderCovering/Main.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/CylinderCovering/Main.lean#L44).

## Lean: Finite triangular approximation of radial sweeps

Stated in [CylinderCovering.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CylinderCovering.lean).

```lean
theorem fourPaperMain :
    AngularExplicitStatement ∧
    RuledApproximation.HyperbolicStatement ∧
    RuledApproximation.NilpotentC1Statement ∧
    RegularParallelogramCounterexampleStatement ∧
    RegularOpenCounterexampleStatement ∧
    RadialSweep.AlignedStatement ∧
    RadialSweep.ActualSweepStatement
```

Proved in [lean/OAI/Geometry/CylinderCovering/Main.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/CylinderCovering/Main.lean#L44).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/100.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/100.md)
