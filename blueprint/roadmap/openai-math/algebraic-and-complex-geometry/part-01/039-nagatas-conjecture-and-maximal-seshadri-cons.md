---
declaration: section
origin: cited
lean: OAI.Nagata.nagata_conjecture, OAI.Nagata.nagata_conjecture_coordinates, OAI.MaximalSeshadri.Geometry.maximalSeshadriConstants
statement: formalized
---

# 039. Nagata’s conjecture and maximal Seshadri constants

4 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Nagata's strict inequality $\sum_i m_i\lt d\sqrt r$ for every nonzero effective plane curve of degree *d* through *r* ≥ 10 very general complex points, with arbitrary multiplicities $m_{i}$. It also proves maximal multipoint Seshadri constants $(L^n/r)^{1/n}$ for every smooth polarized projective variety of dimension *n* ≥ 2 and all sufficiently large *r*: at very general points over ℂ, and at the geometric generic tuple over any algebraically closed field of positive characteristic.

## Nagata's conjecture for plane curves

We prove that a nonzero effective plane curve of degree *d* at *r* ≥ 10 very general complex points has total multiplicity strictly less than $d\sqrt r$. The inequality holds simultaneously for all curves, including reducible and nonreduced curves, and establishes Nagata's conjecture in its strict, nonhomogeneous form.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nagatas-Conjecture-for-Plane-Curves-September-23-2026/main.pdf); the Lean below formalizes results from it.

## Maximal Seshadri constants on arbitrary polarized surfaces

We prove that, for every smooth integral complex projective surface *S* and every ample line bundle *L*, the multipoint Seshadri constant at *r* very general points equals $\sqrt{L^2/r}$ for every sufficiently large integer *r*. This resolves positively the qualitative Nagata–Biran conjecture for surfaces.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Maximal-Seshadri-Constants-on-Arbitrary-Polarized-Surfaces-September-23-2026/main.pdf); the Lean below formalizes results from it.

## Maximal Multipoint Seshadri Constants in Higher Dimensions

Let *L* be an ample line bundle on a smooth integral complex projective variety *X* of dimension *n* ≥ 3. We prove that there is a threshold $r_0=r_0(X,L)$ such that for every integer $r\ge r_0$, the ordinary multipoint Seshadri constant at *r* very general points equals the volume bound $(L^n/r)^{1/n}$. This establishes the qualitative Nagata–Biran–Szemberg assertion in these dimensions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Maximal-Multipoint-Seshadri-Constants-in-Higher-Dimensions-October-5-2026/main.pdf).

## Maximal multipoint Seshadri constants in positive characteristic

Let *L* be an ample line bundle on a smooth integral projective variety *X* over an algebraically closed field of positive characteristic, with $\dim X=n\ge3$. We prove that there is a threshold $r_0=r_0(X,L)$ such that for every integer $r\ge r_0$, the ordinary multipoint Seshadri constant at the geometric generic tuple of *r* points equals the volume bound $(L^n/r)^{1/n}$. The same conclusion holds in dimension two. This establishes the positive-characteristic form of the qualitative Nagata–Biran–Szemberg assertion at geometric generic tuples.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Maximal-multipoint-Seshadri-constants-in-positive-characteristic-October-5-2026/seshadri-positive-characteristic.pdf).

## The Lean formalization

Nagata's conjecture asserts that a nonzero effective plane curve of degree $d$, with multiplicities at least $m_i$ at $r\ge10$ very general points, satisfies $\sum_i m_i<d\sqrt r$.

The formalization establishes this inequality simultaneously for all curves and multiplicity vectors outside one countable union of proper Zariski-closed exceptional sets with nonempty complement. Reducible curves, repeated components, and unequal multiplicities are included, in both effective-curve and homogeneous-polynomial formulations. The formalization also includes the passage from homogeneous effective cycles to equations.

The maximality question asks whether the multipoint Seshadri constant reaches the upper bound $\sqrt{L^2/r}$ at very general points once $r$ is sufficiently large. The formalized result establishes this for every smooth integral complex projective surface $S$ and ample line bundle $L$.

For every $r$ above a threshold depending on $(S,L)$, it gives a countable union of proper closed exceptional sets with nonempty complement. Outside it, the constant is $\sqrt{L^2/r}$ and the boundary class defining this Seshadri constant on the point blowup is nef. The threshold is not explicit or uniform over all surfaces.

## Lean: Nagata's conjecture

Stated in [Nagata.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Nagata.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem exists_positive_degree_equation_of_homogeneous_cycle
    (cycle : Ideal TernaryPolynomial →₀ ℕ) (nonzero : cycle ≠ 0)
    (homogeneous : ∀ ideal ∈ cycle.support,
      ideal.IsPrime ∧ ideal ≠ ⊥ ∧ ideal.IsPrincipal ∧
        ideal.IsHomogeneous (MvPolynomial.homogeneousSubmodule (Fin 3) ℂ)) :
    ∃ polynomial : TernaryPolynomial,
      polynomial ≠ 0 ∧ polynomial.IsHomogeneous polynomial.totalDegree ∧
        0 < polynomial.totalDegree ∧ equationIdealCycle polynomial = cycle
```

Its proof is in [lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean) or a file it imports further down, which this chapter does not read.

```lean
theorem nagata_conjecture :
    ∀ count : ℕ, 10 ≤ count →
      ∃ exceptional : ℕ → Set (OrderedDistinctPoints count),
        (∀ index, IsConfigurationZariskiClosed (exceptional index) ∧
          exceptional index ≠ Set.univ) ∧
        (∃ points : OrderedDistinctPoints count, ∀ index, points ∉ exceptional index) ∧
        ∀ points : OrderedDistinctPoints count, (∀ index, points ∉ exceptional index) →
          ∀ curve : Workers.W10.EffectivePlaneCurve, ∀ multiplicities : Fin count → ℕ,
            (∀ index, multiplicities index ≤ W15.curveOrdinaryMultiplicity curve (points.val index)) →
            (∑ index, (multiplicities index : ℝ)) <
              (Workers.W10.curveDegree curve : ℝ) * Real.sqrt (count : ℝ)
```

Proved in [lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean, line 148](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean#L148).

```lean
theorem nagata_conjecture_coordinates : FullNagata
```

Proved in [lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean, line 162](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/AlgebraicGeometry/PlaneCurves/Nagata.lean#L162).

## Lean: Eventual maximal Seshadri constants

Stated in [MaximalSeshadriConstants.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MaximalSeshadriConstants.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem maximalSeshadriConstants (S : Surface) (L : LineBundle S.scheme)
    (hL : LineBundle.IsAmple S.scheme L) : EventualMaximalSeshadri S L
```

Proved in [lean/OAI/AlgebraicGeometry/Seshadri/Main.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/AlgebraicGeometry/Seshadri/Main.lean#L25).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/039.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/039.md)
