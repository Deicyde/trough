---
declaration: section
origin: cited
lean: OAI.PolynomialVacuumBridge.Corridor.finite_bridge_sums, OAI.HoneycombForce.logPartition_tendsto, OAI.CriticalStrip.critical_strip_mass, OAI.CriticalHoneycomb.finiteBridgeMassEstimate
statement: formalized
proof: formalized
---

# 237. The three-quarter exponent for honeycomb self-avoiding walk

13 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the diameter form of Nienhuis's predicted three-quarter exponent: a uniformly chosen *n*-step self-avoiding walk on the honeycomb lattice has diameter $n^{3/4+o(1)}$. Its local mass and covering numbers have exponent 4/3. These estimates hold at every sufficiently large fixed length, simultaneously across scales, with arbitrarily high polynomial probability.

## Radial transfer estimates and polygon length laws for honeycomb walks

We prove critical diameter-tail exponents −2 for unrooted honeycomb polygons and −2/3 for length-weighted polygons, together with a truncated second-length-moment bound of exponent 2/3. Consequently, polygons conditioned to have length at least *n* have diameter $n^{3/4+o(1)}$ in probability under either weight.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Radial-transfer-estimates-and-polygon-length-laws-for-honeycomb-walks-September-26-2026/main.pdf).

## Critical honeycomb chords with prescribed boundary endpoints

Critical self-avoiding walks between prescribed, macroscopically separated boundary ports of a regular honeycomb hexagon have length $R^{4/3+o(1)}$ in probability, where *R* is the scale of the hexagon. We prove the corresponding statements for half-plane arches, parallel cuts and nonparallel pure cuts. The half-plane law also has mean length $R^{4/3+o(1)}$. A separate strip argument gives endpoint mean laws on one density-one set of heights and in an aligned, critically weighted mixture of all even heights in a macroscopic interval.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/main.pdf); the Lean below formalizes results from it.

## Cylinder loop weights and planar nesting

We determine the growth exponent, at every fixed positive loop fugacity, of the critical honeycomb partition function for disjoint polygons separating two prescribed markers on a balanced cylinder. At fugacity two the cylinder exponent is 1/6; the corresponding planar nesting exponent and middle-strip nesting exponent are 1/12.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Cylinder-loop-weights-and-planar-nesting-September-26-2026/main.pdf).

## Mass and covering exponents for fixed-length honeycomb walks

For uniform self-avoiding walks of every sufficiently large integer length on the honeycomb lattice, we prove diameter exponent 3/4 and simultaneous local-mass and covering exponent 4/3, with arbitrary positive exponent slack and arbitrary polynomial failure probability.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026/main.pdf).

## Signed cylinder propagation and marked polygons on the honeycomb lattice

At the critical activity and loop fugacity two, we prove a 1/6 partition exponent for disjoint honeycomb polygons separating opposite marks on a balanced infinite cylinder, and a 1/12 planar nesting exponent. For ordered first-exit chords in a regular hexagon of side *R*, with both boundary ports summed and diameter at least $R/10$, the finite critical partition is $R^{3/4+o(1)}$ and the normalized mean length is $R^{4/3+o(1)}$. A separate two-bond estimate on tilted cylinders with controlled site proportions bounds the length-square mass of planar polygons of diameter at most *H*, modulo translations, by $H^{2/3+o(1)}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Signed-cylinder-propagation-and-marked-polygons-on-the-honeycomb-lattice-September-26-2026/main.pdf).

## Cylinder amplitudes and logarithmic bridge-length windows on the honeycomb lattice

We prove a logarithmic window of critical honeycomb bridge lengths: summed through height $2h(\log h)^{1/64}$, bridges of lengths between $h^{4/3}(\log h)^{-1/8}$ and $2h^{4/3}(\log h)^{1/2}$ have mass at least $h^{3/4}(\log h)^{-C}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Cylinder-amplitudes-and-logarithmic-bridge-length-windows-on-the-honeycomb-lattice-September-26-2026/main.pdf).

## Marked polygon correlations and one-arc bounds

At the critical honeycomb vertex activity, the squared-length mass of simple polygons of diameter at most *H*, counted modulo translations, is at most $H^{2/3+o(1)}$. We also prove a quantitative two-mark cylinder estimate and a polynomial one-arc bound uniform even for arbitrarily unequal marked intervals.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Marked-polygon-correlations-and-one-arc-bounds-September-26-2026/main.pdf).

## Disk transfer representations and confined bridge mass

We prove that critical honeycomb bridges crossing a strip of width *R* have mean length $R^{4/3+o(1)}$, with the same exponent after confinement to a fixed multiple of the strip width. The initial boundary port is fixed, the terminal port is summed, and all finite lengths receive their critical weights. The bridge mass is comparable to $R^{−1/4}$; the half-plane arch kernel at endpoint separation *m* is comparable to $m^{−5/4}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Disk-transfer-representations-and-confined-bridge-mass-September-26-2026/main.pdf).

## Polynomial vacuum representations and bridge mass for honeycomb walks

We prove that, under the all-length critical measure, a honeycomb bridge crossing a strip of *h* layers, with its initial port fixed and its terminal port free, has mean length $h^{4/3+o(1)}$. We also obtain central visit probability $R^{-2/3+o(1)}$ and mean length $R^{4/3+o(1)}$ for macroscopic free-boundary chords in a regular hexagon.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Polynomial-vacuum-representations-and-bridge-mass-for-honeycomb-walks-September-26-2026/main.pdf); the Lean below formalizes results from it.

## Renewal and changes of law for critical honeycomb walks

For critical honeycomb self-avoiding walk, we prove spatial exponent 3/4 for the infinite irreducible-bridge law and for bridges of every sufficiently large compatible even length. We establish the corresponding thermal laws at every large discount scale, including all positive length and spatial moments. For unrestricted uniform walks, the endpoint lower law holds on a common set of lengths of natural density one. We also determine the near-critical exponential correlation scale and small-force free-energy exponent, and prove spatial local lower bounds that permit conditioning on a prescribed terminal vertex.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/main.pdf); the Lean below formalizes results from it.

## Critical strip-crossing mass on the honeycomb lattice

At the critical weight of the regular honeycomb lattice, the total weight of self-avoiding paths crossing a strip of height *N* is comparable to $N^{−1/4}$. The first horizontal-displacement moment of return paths is comparable to $N^{3/4}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Critical-strip-crossing-mass-on-the-honeycomb-lattice-September-26-2026/main.pdf); the Lean below formalizes results from it.

## Uniform marked-polygon estimates and sharp finite bridge moments

We prove a uniform bound for critical honeycomb polygons through two axial marks on a periodic staircase. The bound retains an explicit power of the ratio between the period and the marked separation. We also prove sharp finite strip estimates: bridge mass of order $h^{−1/4}$, first-length mass at most $Ch^{13/12}$, and mass at least $ch^{-1/4}$ on bridges with length at least $ch^{4/3}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-marked-polygon-estimates-and-sharp-finite-bridge-moments-September-26-2026/main.pdf).

## Cap-selected amplitudes and triangle chords for honeycomb walks

At the critical honeycomb fugacity, self-avoiding port-to-port chords in an equilateral lattice triangle of side *R*, summed over both boundary endpoints and restricted to diameter at least $R/100$, have partition sum comparable to $R^{3/4}$ and mean length $R^{4/3+o(1)}$. We also determine the amplitude selected by two vacuum caps on a cylinder of circumference *N* and prove that it grows as $N^{1/6+o(1)}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Cap-selected-amplitudes-and-triangle-chords-for-honeycomb-walks-September-26-2026/main.pdf).

## The Lean formalization

The linked formalization establishes finiteness of the critical bridge measures used in the paper. For every strip height $h\ge1$, the total weight and first length moment of self-avoiding honeycomb bridges from a fixed initial port to a free terminal port are finite. The corresponding sums are also finite when the bridge is confined to the corridor of horizontal width $h(\log h)^2$, including the normalized first-moment sums.

These are supporting summability statements. The paper's $h^{4/3+o(1)}$ mean-length law and its central-visit and hexagonal-chord exponents are outside them.

The linked formalization proves existence of the infinite-length free energy for the critical honeycomb self-avoiding-walk partition function. For every starting vertex, force direction, and real force parameter, the logarithm of the length-$n$ partition function divided by $n$ converges to its stated free-energy limit.

This selected result supplies the limiting free energy. It does not state the paper's small-force exponent, near-critical correlation scale, or the $3/4$ spatial and moment laws.

For critical self-avoiding walks on the honeycomb lattice, the formalization proves that the total weight of paths crossing a strip of height $N$ is comparable to $N^{-1/4}$, while the first horizontal-displacement moment of return paths is comparable to $N^{3/4}$. It also proves finiteness of the strip sums, the exact arch–bridge balance identity, comparison of successive moment increments with bridge mass, and monotonicity of bridge mass. The comparison constants are uniform in the strip height.

For the prescribed-boundary-endpoint companion, let $B_h$ be the total critical weight of strict bridges crossing a strip of integral height $h$, from one fixed bottom port to all compatible top ports, with $B_0=1$. The formalization proves
$c(1+h)^{-1/4}\le B_h\le C(1+h)^{-1/4}$
for all $h\ge0$ and fixed positive constants $c,C$. This includes finiteness of the path sum.

This establishes the bridge-mass estimate in the companion's finite boundary and length inputs, with the terminal port summed over. The companion's main prescribed-endpoint theorem asserts that, for every $\varepsilon>0$, the probability that a chord between two specified ports has length between $R^{4/3-\varepsilon}$ and $R^{4/3+\varepsilon}$ tends to one as $R\to\infty$ in the stated geometries. That length law, its lower bound for the normalizing mass, the arch and strip mean laws, and the remaining moment and renewal conclusions are outside this supporting comparison. The separate strip-mass and displacement-moment results above concern the strip-crossing paper.

## Lean: Finiteness of critical bridge mass and first length moments

```lean
theorem finite_bridge_sums : FiniteBridgeSums
```

Stated in [HoneycombBridgeFiniteness.lean, line 60](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HoneycombBridgeFiniteness.lean#L60). Proved in [lean/OAI/Combinatorics/HoneycombCorridor/BridgeFiniteness.lean, line 91](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/HoneycombCorridor/BridgeFiniteness.lean#L91).

## Lean: Existence of the honeycomb free-energy limit

```lean
theorem logPartition_tendsto (o : Vertex) (e : ℂ) (s : ℝ) :
    Tendsto (logPartition o e s) atTop (𝓝 (freeEnergy o e s))
```

Stated in [HoneycombFreeEnergy.lean, line 64](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HoneycombFreeEnergy.lean#L64). Proved in [lean/OAI/Probability/Honeycomb/FreeEnergy.lean, line 716](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/Honeycomb/FreeEnergy.lean#L716).

## Lean: Critical honeycomb strip mass and displacement moment

```lean
theorem critical_strip_mass : CriticalStripMass
```

Stated in [CriticalStripMass.lean, line 76](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CriticalStripMass.lean#L76). Proved in [lean/OAI/Combinatorics/StripMass/PhysicalPorts.lean, line 552](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/StripMass/PhysicalPorts.lean#L552).

## Lean: Strict honeycomb bridge mass of order $(1+h)^{-1/4}$

```lean
theorem finiteBridgeMassEstimate : FiniteBridgeMassEstimate
```

Stated in [HoneycombBridgeMassSupport.lean, line 72](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HoneycombBridgeMassSupport.lean#L72). Proved in [lean/OAI/Combinatorics/HoneycombChords/BridgeMass.lean, line 114](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/HoneycombChords/BridgeMass.lean#L114). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/237.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/237.md)
