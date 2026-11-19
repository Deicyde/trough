# Cayley coordinates

Angles make rotation matrices transcendental functions of the coordinates. Cayley coordinates make them rational, so that every quantity in the case analysis becomes a polynomial after clearing positive denominators.

- [cayley](def-cayley.md)

The numerator $N(r)$ is a polynomial with integer coefficients, defined over any commutative ring, and the denominator is positive.

Geometrically, if $a$ is a unit vector and $-\pi < \theta < \pi$, then $r = \tan(\theta/2)\,a$ gives the rotation through angle $\theta$ about $a$. In particular, $r = 0$ gives the identity, and small $r$ describes a small rotation. A single Cayley chart misses rotations through angle $\pi$; the chart bases in Definition [charts](../the-reduction/step-c-the-chart/def-charts.md) allow the reduction to cover all relative rotations using bounded Cayley coordinates.

- [cayley_so3](lem-cayley-so3.md)
- [Rodrigues form](lem-cayley-rodrigues.md)

The Rodrigues form is the source of the blow-up identity (Lemma [Blow-up identity](../boxes-and-leaf-certificates/the-blow-up/lem-blowup-identity.md)): the difference $\mathrm{Cay}(r) S - S$ is divisible by $r$.

- [cayley_trace](lem-cayley-trace.md)
- [cayley_surj](thm-cayley-surj.md)
- [Axis-angle form](lem-axis-angle.md)
- [Outer views](outer-views/README.md)
