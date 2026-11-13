---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Convex.ExtremePointsContinuousMapBall.extremePoints_closedBall_continuousMap, MathlibExt.Analysis.Convex.ExtremePointsContinuousMapBall.mem_extremePoints_closedBall_continuousMap, MathlibExt.Analysis.Convex.ExtremePointsLpBalls.extremePoints_closedBall_piLp_top, MathlibExt.Analysis.Convex.ExtremePointsLpBalls.extremePoints_closedBall_piLp_one
statement: formalized
proof: formalized
---

# Extreme points of unit balls

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/extreme-points-of-unit-balls/index.html).

## Extreme points of the unit ball of continuous real functions

The extreme points of the closed unit ball of `C(X, ℝ)`, for `X`
compact Hausdorff, are exactly the functions with `|f x| = 1` for every
`x`.

Formalized by `MathlibExt.Analysis.Convex.ExtremePointsContinuousMapBall.extremePoints_closedBall_continuousMap`, a theorem declared in [MathlibExt/Analysis/Convex/ExtremePointsContinuousMapBall.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/ExtremePointsContinuousMapBall.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/extreme-points-of-unit-balls/index.html#extreme-points-closed-ball-continuous-ma).

## Membership criterion for extreme points of the unit ball of $C(X)$

Membership form of `extremePoints_closedBall_continuousMap`.

Formalized by `MathlibExt.Analysis.Convex.ExtremePointsContinuousMapBall.mem_extremePoints_closedBall_continuousMap`, a theorem declared in [MathlibExt/Analysis/Convex/ExtremePointsContinuousMapBall.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/ExtremePointsContinuousMapBall.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/extreme-points-of-unit-balls/index.html#mem-extreme-points-closed-ball-continuou).

## Extreme points of the unit ball of finite $\ell^\infty$

The extreme points of the closed unit ball of `PiLp ∞ (fun _ : ι => 𝕜)`
are exactly the vectors all of whose coordinates have norm `1`. If some
coordinate has norm `< 1`, a small perturbation of that coordinate stays
in the ball and exhibits the point as a midpoint; conversely, a vector
with all coordinates of norm `1` that is a convex combination of two ball
points must agree with both of them coordinatewise, by strict convexity
of the scalar field.

Formalized by `MathlibExt.Analysis.Convex.ExtremePointsLpBalls.extremePoints_closedBall_piLp_top`, a theorem declared in [MathlibExt/Analysis/Convex/ExtremePointsLpBalls.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/ExtremePointsLpBalls.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/extreme-points-of-unit-balls/index.html#extreme-points-closed-ball-pi-lp-top).

## Extreme points of the unit ball of finite $\ell^1$

The extreme points of the closed unit ball of `PiLp 1 (fun _ : ι => 𝕜)`
are exactly the unit multiples of the coordinate vectors. The proof: an
extreme point must have norm `1` (otherwise a one-coordinate perturbation
stays in the ball and exhibits it as a midpoint), and it cannot have two
nonzero coordinates (otherwise mass can be transferred between them, in
the direction of the phases of the two coordinates, staying at norm `1`
on both sides). Conversely, a unit multiple of a coordinate vector is
extreme: a convex combination equalling it must have total norm `1`,
hence coordinatewise triangle equality, hence vanishing off the
coordinate, and strict convexity of the scalar field at the coordinate.

Formalized by `MathlibExt.Analysis.Convex.ExtremePointsLpBalls.extremePoints_closedBall_piLp_one`, a theorem declared in [MathlibExt/Analysis/Convex/ExtremePointsLpBalls.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/ExtremePointsLpBalls.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/extreme-points-of-unit-balls/index.html#extreme-points-closed-ball-pi-lp-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extreme points of unit balls](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/extreme-points-of-unit-balls/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/extreme-points-of-unit-balls)
