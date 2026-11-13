---
declaration: theorem
origin: cited
lean: MoserWorm.disc_mem_worm_covers, MoserWorm.mosers_worm_problem, MoserWorm.mosers_worm_problem_upper_bound, MoserWorm.convex_mosers_worm_problem, MoserWorm.convex_mosers_worm_problem_bound_attained, MoserWorm.convex_mosers_worm_problem_upper_bound, MoserWorm.convex_mosers_worm_problem_lower_bound
statement: formalized
---

# Moser's Worm

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Moser%27s_worm_problem)
> - [Tao's optimization constant 13a](https://teorth.github.io/optimizationproblems/constants/13a.html)

*Quoted from [FormalConjectures/Wikipedia/MoserWorm.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 2 open, 4 solved and 1 textbook result.

## `MoserWorm.disc_mem_worm_covers`

Textbook result, proved here.

> A disc of radius 1 / 2 is a worm cover.
>
> This follows by translating the center of the disc to the midpoint of the worm.

```lean
theorem disc_mem_worm_covers : Metric.closedBall 0 0.5 ∈ WormCovers
```

Category `textbook`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/MoserWorm.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean#L55).

## `MoserWorm.mosers_worm_problem`

Open: stated without proof.

> **Moser's Worm Problem**
> What is the minimal area (or greatest lower bound on the area)
> of a shape that can cover every unit-length curve?

```lean
theorem mosers_worm_problem :
    IsGLB {v | ∃ X ∈ WormCovers, volume X = v} mosers_worm_problem.answer
```

Category `research open`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/MoserWorm.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean#L80).

## `MoserWorm.mosers_worm_problem_upper_bound`

Solved: stated here without proof.

> There is a set of area 0.260437 that covers all worms.
>
> *Reference:*
> Norwood, Rick; Poole, George (2003), "An improved upper bound for Leo Moser's worm problem",
> Discrete and Computational Geometry, 29 (3): 409–417, doi:10.1007/s00454-002-0774-3, MR 1961007.

```lean
theorem mosers_worm_problem_upper_bound :
    ∃ X ∈ WormCovers, volume X = 0.260437
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/MoserWorm.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean#L92).

## `MoserWorm.convex_mosers_worm_problem`

Open: stated without proof.

> **Convex Moser's Worm Problem**
> What is the minimal area (or greatest lower bound on the area)
> of a *convex* shape that can cover every unit-length curve?

```lean
theorem convex_mosers_worm_problem :
    convexWormCoverConstant = convex_mosers_worm_problem.answer
```

Category `research open`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/MoserWorm.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean#L110).

## `MoserWorm.convex_mosers_worm_problem_bound_attained`

Solved: stated here without proof.

> The minimal area of a convex shape that can cover every unit-length curve is attained.
> This follows from the Blaschke selection theorem.

```lean
theorem convex_mosers_worm_problem_bound_attained :
    ∃ X ∈ WormCovers, Convex ℝ X ∧ volume X = convexWormCoverConstant
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/MoserWorm.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean#L119).

## `MoserWorm.convex_mosers_worm_problem_upper_bound`

Solved: stated here without proof.

> There is a convex set of area 0.270911861 that covers all worms.
>
> *Reference:*
> Wang, Wei (2006), "An improved upper bound for the worm problem",
> Acta Mathematica Sinica, 49 (4): 835–846, MR 2264090.

```lean
theorem convex_mosers_worm_problem_upper_bound :
    ∃ X ∈ WormCovers, Convex ℝ X ∧ volume X = 0.270911861
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/MoserWorm.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean#L131).

## `MoserWorm.convex_mosers_worm_problem_lower_bound`

Solved: stated here without proof.

> 0.232239 is a lower bound on the area of a convex set that covers all worms.
>
> *Reference:*
> Khandhawit, Tirasan; Pagonakis, Dimitrios; Sriswasdi, Sira (2013),
> "Lower Bound for Convex Hull Area and Universal Cover Problems",
> International Journal of Computational Geometry & Applications,
> 23 (3): 197–212, arXiv:1101.5638, doi:10.1142/S0218195913500076, MR 3158583, S2CID 207132316.

```lean
theorem convex_mosers_worm_problem_lower_bound :
    0.232239 ≤ convexWormCoverConstant
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/MoserWorm.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean#L145).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MoserWorm.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MoserWorm.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Moser%27s_worm_problem)
