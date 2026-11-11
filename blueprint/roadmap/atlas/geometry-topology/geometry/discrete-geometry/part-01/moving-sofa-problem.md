---
declaration: section
origin: cited
lean: MovingSofa.corridor, MovingSofa.entrance, MovingSofa.exit, MovingSofa.Motion, MovingSofa.Motion.position, MovingSofa.CanPass, MovingSofa.IsSofa, MovingSofa.optimalArea
statement: formalized
---

# Moving sofa problem

46 results, 38 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html).

## Corridor

The corridor is the L-shaped set of points $z \in \mathbb{C}$ with
$\operatorname{Re} z \le 1$ and $0 \le \operatorname{Im} z \le 1$ (the horizontal arm, extending
to the left) together with the points $z$ with $0 \le \operatorname{Re} z \le 1$ and
$\operatorname{Im} z \ge 0$ (the vertical arm, extending upward): two perpendicular
semi-infinite arms of width one.

Formalized by `MovingSofa.corridor`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#corridor).

## Entrance of the corridor

The entrance region of the unit right-angle corridor is
the closed half-strip
$\{z \in \mathbb{C} : \operatorname{Re} z \le 0,\ 0 \le \operatorname{Im} z \le 1\}$,
the part of its horizontal arm to the left of the corner square.

Formalized by `MovingSofa.entrance`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#entrance).

## Exit of the corridor

The exit region of the unit right-angle corridor is the closed
half-strip $\{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ \operatorname{Im} z \ge 1\}$,
the part of its vertical arm above the corner square.

Formalized by `MovingSofa.exit`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#exit).

## Planar rigid motion

A motion consists of a continuous map $t \mapsto u_t$ from $[0, 1]$
to the unit circle $\{u \in \mathbb{C} : |u| = 1\}$ (the rotation) and a continuous map
$t \mapsto c_t$ from $[0, 1]$ to $\mathbb{C}$ (the translation).

Formalized by `MovingSofa.Motion`, a structure declared in [MathlibExt/Geometry/MovingSofa.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#motion).

## Position under a rigid motion

Let $m$ be a motion with rotation $u(t)$ in the unit circle
and translation $c(t) \in \mathbb{C}$ at each time $t \in [0, 1]$. The position at time $t$ of a
point $z \in \mathbb{C}$ is $u(t)\,z + c(t)$.

Formalized by `MovingSofa.Motion.position`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#position).

## Passing the corridor

A set $K \subseteq \mathbb{C}$ can pass the corridor if there are
continuous maps $u$ from $[0, 1]$ to the unit circle $\{w \in \mathbb{C} : |w| = 1\}$ and $c$
from $[0, 1]$ to $\mathbb{C}$ such that, writing $K_t = \{u(t) z + c(t) : z \in K\}$ for the
position of $K$ at time $t$, $K_0$ lies in the entrance arm, $K_1$ lies in the exit arm, and
$K_t$ lies in the corridor for every $t \in [0, 1]$.

Formalized by `MovingSofa.CanPass`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#can-pass).

## Sofa shapes

A set $K \subseteq \mathbb{C}$ is a sofa when it is Lebesgue measurable,
nonempty and connected, and can be moved through the unit right-angle corridor: there is a motion
(a rotation by a unit complex number and a translation, both varying continuously with time
$t \in [0, 1]$) that places $K$ inside the corridor's entrance region at time $0$, inside its exit
region at time $1$, and inside the corridor at every time $t$.

Formalized by `MovingSofa.IsSofa`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#is-sofa).

## Optimal sofa area

Let the corridor be
$L = \{z \in \mathbb{C} : \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z \le 1\} \cup
\{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z\}$, with entrance
$E = \{z \in \mathbb{C} : \operatorname{Re} z \le 0,\ 0 \le \operatorname{Im} z \le 1\}$ and exit
$X = \{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 1 \le \operatorname{Im} z\}$. A sofa
is a nonempty connected Lebesgue-measurable set $K \subseteq \mathbb{C}$ for which there are
continuous maps $u : [0, 1] \to \{w \in \mathbb{C} : |w| = 1\}$ and $c : [0, 1] \to \mathbb{C}$
such that, writing $K_t = \{u(t)\,z + c(t) : z \in K\}$, we have $K_0 \subseteq E$,
$K_1 \subseteq X$ and $K_t \subseteq L$ for every $t \in [0, 1]$. The optimal sofa area is the
supremum, taken in $[0, \infty]$, of the Lebesgue measures of all sofas.

Because the supremum is taken in $[0, \infty]$, neither its finiteness nor its attainment is
assumed.

Formalized by `MovingSofa.optimalArea`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#optimal-area).

## Unit square

The unit square is the set of complex numbers $z$ with
$0 \le \operatorname{Re} z \le 1$ and $0 \le \operatorname{Im} z \le 1$, that is, the square
$[0,1] \times [0,1]$ in the complex plane.

Formalized by `MovingSofa.unitSquare`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#unit-square).

## The square's translation through the corner

The motion with no rotation that sends a
point $z$ at time $t \in [0,1]$ to $z + \tau(t)$, where $\tau(t) = 2t - 1$ for $t \le 1/2$ and
$\tau(t) = (2t - 1)i$ for $t \ge 1/2$: it moves a shape one unit to the right during the first
half of the time interval and then one unit upward.

Formalized by `MovingSofa.squareMotion`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-motion).

## Motions preserve distance

Let $m$ be a motion, $t \in [0, 1]$ a time, and write $m_t(z)$
for the position of a point $z \in \mathbb{C}$ under $m$ at time $t$. Then
$|m_t(z) - m_t(w)| = |z - w|$ for all $z, w \in \mathbb{C}$.

Formalized by `MovingSofa.motion_preserves_distance`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#motion-preserves-distance).

## The unit square is Borel measurable

The unit square $[0,1] \times [0,1]$ is a measurable
set for the Borel $\sigma$-algebra of the complex plane.

Formalized by `MovingSofa.square_measurable`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-measurable).

## The unit square is connected

The unit square
$\{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z \le 1\}$ is a
nonempty connected subset of $\mathbb{C}$.

Formalized by `MovingSofa.square_connected`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-connected).

## The unit square has area one

The unit square
$\{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z \le 1\}$ has
Lebesgue measure $1$.

Formalized by `MovingSofa.square_area`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-area).

## The unit square passes the corridor

Let the corridor be
$L = \{z \in \mathbb{C} : \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z \le 1\} \cup
\{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z\}$, with entrance
$E = \{z \in \mathbb{C} : \operatorname{Re} z \le 0,\ 0 \le \operatorname{Im} z \le 1\}$ and exit
$X = \{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 1 \le \operatorname{Im} z\}$. For the
unit square
$Q = \{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z \le 1\}$
there are continuous maps $u : [0, 1] \to \{w \in \mathbb{C} : |w| = 1\}$ and
$c : [0, 1] \to \mathbb{C}$ such that, writing $Q_t = \{u(t)\,z + c(t) : z \in Q\}$, we have
$Q_0 \subseteq E$, $Q_1 \subseteq X$ and $Q_t \subseteq L$ for every $t \in [0, 1]$.

A pure translation, first to the right and then upward, suffices.

Formalized by `MovingSofa.square_canPass`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-can-pass).

## The unit square is a sofa

The unit square $[0,1] \times [0,1]$ in the complex plane is a
sofa: it is null-measurable for Lebesgue measure, connected, and there are continuous maps
$u \colon [0,1] \to \{w \in \mathbb{C} : |w| = 1\}$ and $v \colon [0,1] \to \mathbb{C}$ such that
the motion $z \mapsto u(t) z + v(t)$ carries the square into the entrance
$\{z : \operatorname{Re} z \le 0,\ 0 \le \operatorname{Im} z \le 1\}$ at $t = 0$, into the exit
$\{z : 0 \le \operatorname{Re} z \le 1,\ 1 \le \operatorname{Im} z\}$ at $t = 1$, and into the
unit right-angle corridor
$\{z : \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z \le 1\} \cup
\{z : 0 \le \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z\}$ at every time $t \in [0,1]$.

Formalized by `MovingSofa.square_isSofa`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-is-sofa).

## The optimal sofa area is at least one

The optimal sofa area, that is, the supremum
in $[0, \infty]$ of the Lebesgue areas of all sofas, is at least $1$.

The unit square, a sofa of area $1$, witnesses the bound.

Formalized by `MovingSofa.one_le_optimalArea`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#one-le-optimal-area).

## Mirrored corridor

The mirrored corridor is the set of points $z \in \mathbb{C}$ with
$\operatorname{Re} z \ge -1$ and $0 \le \operatorname{Im} z \le 1$ (the horizontal arm,
extending to the right) together with the points $z$ with $-1 \le \operatorname{Re} z \le 0$
and $\operatorname{Im} z \ge 0$ (the vertical arm, extending upward). It is the reflection of
the corridor in the imaginary axis, so passing it requires the opposite turn.

Formalized by `MovingSofa.corridorOther`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#corridor-other).

## Entrance arm of the mirrored corridor

The entrance arm of the mirrored corridor is the
set of points $z \in \mathbb{C}$ with $\operatorname{Re} z \ge 0$ and
$0 \le \operatorname{Im} z \le 1$: the part of its horizontal arm beyond the corner square
$-1 \le \operatorname{Re} z \le 0$, $0 \le \operatorname{Im} z \le 1$.

Formalized by `MovingSofa.entranceOther`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#entrance-other).

## Exit of the mirrored corridor

The exit region of the mirrored unit corridor is the
closed half-strip
$\{z \in \mathbb{C} : -1 \le \operatorname{Re} z \le 0,\ \operatorname{Im} z \ge 1\}$,
the part of its vertical arm above its corner square.

Formalized by `MovingSofa.exitOther`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#exit-other).

## Passing the mirrored corridor

A set $K \subseteq \mathbb{C}$ can pass the mirrored
corridor if there are continuous maps $u$ from $[0, 1]$ to the unit circle
$\{w \in \mathbb{C} : |w| = 1\}$ and $c$ from $[0, 1]$ to $\mathbb{C}$ such that, writing
$K_t = \{u(t) z + c(t) : z \in K\}$ for the position of $K$ at time $t$, $K_0$ lies in the
entrance arm of the mirrored corridor, $K_1$ lies in the exit arm of the mirrored corridor, and
$K_t$ lies in the mirrored corridor for every $t \in [0, 1]$.

Formalized by `MovingSofa.CanPassOther`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#can-pass-other).

## Z-shaped corridor

For a real number $d$, the Z-shaped corridor with corner separation
$d$ is the set of points $z \in \mathbb{C}$ lying in at least one of three pieces: the lower
horizontal arm, where $\operatorname{Re} z \le 1$ and $0 \le \operatorname{Im} z \le 1$; the
middle channel, where $0 \le \operatorname{Re} z \le 1$ and $0 \le \operatorname{Im} z \le 2 + d$;
and the upper horizontal arm, where $\operatorname{Re} z \ge 0$ and
$1 + d \le \operatorname{Im} z \le 2 + d$.

The middle channel is bounded: it does not contain the upward ray above the upper arm. For
$d = 1$ the two corner squares are separated by one full corridor width. Passing the corridor
requires one turn in each direction inside a single passage.

Formalized by `MovingSofa.corridorZ`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#corridor-z).

## Entrance arm of the Z corridor

The entrance region of the Z corridor is the closed
half-strip $\{z \in \mathbb{C} : \operatorname{Re} z \le 0,\ 0 \le \operatorname{Im} z \le 1\}$,
the part of its horizontal entrance arm to the left of the middle channel.

Formalized by `MovingSofa.entranceZ`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#entrance-z).

## Exit arm of the Z corridor

For a real number $d$ (the corner separation), the exit region
of the Z corridor with separation $d$ is the closed half-strip
$\{z \in \mathbb{C} : \operatorname{Re} z \ge 1,\ 1 + d \le \operatorname{Im} z \le 2 + d\}$,
the part of its horizontal exit arm to the right of the middle channel.

Formalized by `MovingSofa.exitZ`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#exit-z).

## Passing the Z corridor at a given separation

For a real number $d$, a set
$K \subseteq \mathbb{C}$ can pass the Z corridor with corner separation $d$ if there are
continuous maps $u$ from $[0, 1]$ to the unit circle $\{w \in \mathbb{C} : |w| = 1\}$ and $c$
from $[0, 1]$ to $\mathbb{C}$ such that, writing $K_t = \{u(t) z + c(t) : z \in K\}$ for the
position of $K$ at time $t$, $K_0$ lies in the entrance arm of the Z corridor, $K_1$ lies in the
exit arm of the Z corridor with corner separation $d$, and $K_t$ lies in the Z corridor with
corner separation $d$ for every $t \in [0, 1]$.

Such a passage is a single motion that turns once in each direction.

Formalized by `MovingSofa.CanPassZAt`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#can-pass-zat).

## Passing the Z corridor for all large separations

A set $K \subseteq \mathbb{C}$ can pass
the Z corridor if there is a real number $D$ such that, for every real $d \ge D$, $K$ can pass
the Z corridor with corner separation $d$; that is, $K$ passes whenever the corners are
sufficiently separated.

Unlike the mirrored corridor, this is not implied by an ordinary passage: time reversal plus a
rigid motion transports an ordinary passage to the mirrored corridor, but a Z passage couples
both turns in one motion.

Formalized by `MovingSofa.CanPassZ`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#can-pass-z).

## The square's translation through the Z corridor

For a real number $d$, the motion with no
rotation that sends a point $z$ at time $t \in [0,1]$ to $z + \tau(t)$, where $\tau(t) = 3t - 1$ for
$t \le 1/3$, $\tau(t) = (1 + d)(3t - 1)i$ for $1/3 \le t \le 2/3$, and
$\tau(t) = (3t - 2) + (1 + d)i$ for $t \ge 2/3$: it translates a shape by $1$, then by $(1 + d)i$,
then by $1$, each segment taking a third of the time interval.

Formalized by `MovingSofa.squareMotionZAt`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-motion-zat).

## Z-corridor passage of the unit square

For every real $d \ge 0$, the unit square passes
the Z corridor with corner separation $d$.

Formalized by `MovingSofa.square_canPassZAt`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-can-pass-zat).

## The square's translation through the Z corridor at separation one

The square's
translation through the Z corridor at separation $d = 1$: the motion with no rotation that sends a
point $z$ at time $t \in [0,1]$ to $z + \tau(t)$, where $\tau(t) = 3t - 1$ for $t \le 1/3$,
$\tau(t) = 2(3t - 1)i$ for $1/3 \le t \le 2/3$, and $\tau(t) = (3t - 2) + 2i$ for $t \ge 2/3$.

Formalized by `MovingSofa.squareMotionZ`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-motion-z).

## Z-corridor passage of the unit square at separation one

The unit square passes the Z
corridor with corner separation $1$.

Formalized by `MovingSofa.square_canPassZAt_one`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-can-pass-zat-one).

## Z-corridor passage of the unit square for large separations

There is a real $D$ such
that for every $d \ge D$ the unit square passes the Z corridor with corner separation $d$.

Formalized by `MovingSofa.square_canPassZ`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-can-pass-z).

## Ambidextrous sofa shapes

A set $K \subseteq \mathbb{C}$ is an ambidextrous sofa when it is
a sofa and there is a real number $D$ such that, for every corner separation $d \ge D$, a single
motion places $K$ inside the entrance arm of the Z corridor with separation $d$ at time $0$, inside
its exit arm at time $1$, and inside that corridor at every time; such a passage turns once in
each direction.

(Two independent passages, one through each mirrored L corridor, would not suffice: an ordinary
passage transports to the mirrored corridor by time reversal plus a rigid motion, so that
formulation would collapse to the ordinary sofa condition.)

Formalized by `MovingSofa.IsAmbidextrousSofa`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#is-ambidextrous-sofa).

## Optimal area of ambidextrous sofas

The ambidextrous optimal area is the supremum, taken
in $[0, \infty]$, of the Lebesgue areas of all ambidextrous sofas $K \subseteq \mathbb{C}$.

Formalized by `MovingSofa.ambidextrousOptimalArea`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#ambidextrous-optimal-area).

## The ambidextrous optimal area is at most the optimal area

The supremum, in $[0, \infty]$,
of the Lebesgue areas of all ambidextrous sofas is at most the supremum of the Lebesgue areas of
all sofas. This holds because every ambidextrous sofa is a sofa.

Formalized by `MovingSofa.ambidextrousOptimalArea_le_optimalArea`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#ambidextrous-optimal-area-le-optimal-are).

## The square's translation through the mirrored corner

The motion with no rotation that
sends a point $z$ at time $t \in [0,1]$ to $z + \tau(t)$, where $\tau(t) = -2t$ for $t \le 1/2$ and
$\tau(t) = -1 + (2t - 1)i$ for $t \ge 1/2$: it moves a shape one unit to the left during the first
half of the time interval and then one unit upward.

Formalized by `MovingSofa.squareMotionOther`, a definition declared in [MathlibExt/Geometry/MovingSofa.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-motion-other).

## The unit square passes the mirrored corridor

Let the mirrored corridor be
$L' = \{z \in \mathbb{C} : -1 \le \operatorname{Re} z,\ 0 \le \operatorname{Im} z \le 1\} \cup
\{z \in \mathbb{C} : -1 \le \operatorname{Re} z \le 0,\ 0 \le \operatorname{Im} z\}$, with entrance
$E' = \{z \in \mathbb{C} : 0 \le \operatorname{Re} z,\ 0 \le \operatorname{Im} z \le 1\}$ and exit
$X' = \{z \in \mathbb{C} : -1 \le \operatorname{Re} z \le 0,\ 1 \le \operatorname{Im} z\}$. For the
unit square
$Q = \{z \in \mathbb{C} : 0 \le \operatorname{Re} z \le 1,\ 0 \le \operatorname{Im} z \le 1\}$
there are continuous maps $u : [0, 1] \to \{w \in \mathbb{C} : |w| = 1\}$ and
$c : [0, 1] \to \mathbb{C}$ such that, writing $Q_t = \{u(t)\,z + c(t) : z \in Q\}$, we have
$Q_0 \subseteq E'$, $Q_1 \subseteq X'$ and $Q_t \subseteq L'$ for every $t \in [0, 1]$.

Formalized by `MovingSofa.square_canPassOther`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-can-pass-other).

## The unit square is an ambidextrous sofa

The unit square $[0,1] \times [0,1]$ in the
complex plane is an ambidextrous sofa.

Formalized by `MovingSofa.square_isAmbidextrousSofa`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#square-is-ambidextrous-sofa).

## The ambidextrous sofa constant is at least one

The supremum of the Lebesgue areas of all
ambidextrous sofas, taken in $[0, \infty]$, is at least $1$.

The unit square $[0, 1] \times [0, 1]$ is an ambidextrous sofa of area $1$.

Formalized by `MovingSofa.one_le_ambidextrousOptimalArea`, a theorem declared in [MathlibExt/Geometry/MovingSofa.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/MovingSofa.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#one-le-ambidextrous-optimal-area).

## Hammersley upper bound for the ambidextrous sofa

The supremum of the areas of
ambidextrous sofas, taken in $[0, \infty]$, is at most $2\sqrt{2}$.

## Sources

- catalogue upper row, Hammersley (1968), adapted from C41a.

Stated but not proved: `AmbidextrousSofaWanted.hammersley_upper` is written with `theorem_wanted` in [WantedExt/Geometry/AmbidextrousSofaWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/AmbidextrousSofaWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#hammersley-upper).

## Baek upper bound for the ambidextrous sofa

The supremum of the areas of
ambidextrous sofas, taken in $[0, \infty]$, is at most $22195/10000 = 2.2195$.

## Sources

- catalogue upper row, Baek (2024) naive bound from C41a, exact decimal endpoint `22195 / 10000`.

Stated but not proved: `AmbidextrousSofaWanted.baek_upper` is written with `theorem_wanted` in [WantedExt/Geometry/AmbidextrousSofaWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/AmbidextrousSofaWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#baek-upper).

## Gibbs lower bound for the ambidextrous sofa

The supremum of the areas of
ambidextrous sofas, taken in $[0, \infty]$, is at least $164495/100000 = 1.64495$.

## Sources

- catalogue lower row, Gibbs (2014) numerical construction, exact decimal endpoint `164495 / 100000`.

Stated but not proved: `AmbidextrousSofaWanted.gibbs_lower` is written with `theorem_wanted` in [WantedExt/Geometry/AmbidextrousSofaWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/AmbidextrousSofaWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#gibbs-lower).

## Romik lower bound for the ambidextrous sofa

The supremum of the areas of
ambidextrous sofas, taken in $[0, \infty]$, is at least
$164495521/100000000 = 1.64495521$.

## Sources

- catalogue lower row, Romik (2016), exact decimal endpoint `164495521 / 100000000`.

Stated but not proved: `AmbidextrousSofaWanted.romik_lower` is written with `theorem_wanted` in [WantedExt/Geometry/AmbidextrousSofaWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/AmbidextrousSofaWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#romik-lower).

## Hammersley's upper bound for the moving sofa constant

The moving sofa constant, the
supremum of the areas of connected Lebesgue-measurable planar shapes that a continuous rigid motion
can carry through the right-angled corridor of width $1$, is at most $2\sqrt{2}$.

## Sources

- catalogue line 13, attributed to Hammersley (1968). Primary not retained.

Stated but not proved: `MovingSofaWanted.hammersley_upper` is written with `theorem_wanted` in [WantedExt/Geometry/MovingSofaWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MovingSofaWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#hammersley-upper-2).

## Kallus–Romik upper bound for the moving sofa constant

The moving sofa constant, the
supremum of the areas of connected Lebesgue-measurable planar shapes that a continuous rigid motion
can carry through the right-angled corridor of width $1$, is at most $2.37$.

## Sources

- catalogue line 14, Kallus-Romik (2018). Numerical certificate not retained.

Stated but not proved: `MovingSofaWanted.kallus_romik_upper` is written with `theorem_wanted` in [WantedExt/Geometry/MovingSofaWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MovingSofaWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#kallus-romik-upper).

## Hammersley's lower bound for the moving sofa constant

The moving sofa constant, the
supremum of the areas of connected Lebesgue-measurable planar shapes that a continuous rigid motion
can carry through the right-angled corridor of width $1$, is at least $\pi/2 + 2/\pi$.

## Sources

- catalogue line 21, Hammersley (1968). Construction not retained.

Stated but not proved: `MovingSofaWanted.hammersley_lower` is written with `theorem_wanted` in [WantedExt/Geometry/MovingSofaWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MovingSofaWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#hammersley-lower).

## Gerver's lower bound for the moving sofa constant

The moving sofa constant, the
supremum of the areas of connected Lebesgue-measurable planar shapes that a continuous rigid motion
can carry through the right-angled corridor of width $1$, is at least $2.2195$.

## Sources

- catalogue line 22, printed Gerver lower target, not an exact area formula.

Stated but not proved: `MovingSofaWanted.gerver_printed_lower` is written with `theorem_wanted` in [WantedExt/Geometry/MovingSofaWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MovingSofaWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html#gerver-printed-lower).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moving sofa problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/moving-sofa-problem)
