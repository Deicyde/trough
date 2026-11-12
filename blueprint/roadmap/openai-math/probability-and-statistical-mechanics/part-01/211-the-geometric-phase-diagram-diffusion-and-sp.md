---
declaration: section
origin: cited
lean: OAI.FKCRT.finite_fk_maps_converge_to_brownian_crt
statement: formalized
proof: formalized
---

# 211. The geometric phase diagram, diffusion, and spectra of random planar maps

7 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Critical Fortuin–Kasteleyn planar maps converge to Liouville quantum gravity spheres for $0\lt q\le4$ and to the Brownian continuum random tree for *q* > 4, establishing the surface-to-tree geometric transition. For FK–Ising and spanning-tree-weighted maps, stationary random walks converge to Liouville Brownian motion on the limiting sphere. The FK–Ising spectral result also gives convergence of eigenvalues and heat traces, using the stated Brownian/LQG inputs.

## Random Walks on Critical FK–Ising Maps and Liouville Brownian Motion

We prove that stationary random walks on critical spherical FK–Ising planar maps converge to Liouville Brownian motion on the ordinary unit-area $\sqrt3$-quantum sphere, using the geometric and electrical results of the spectral companion. The walk chooses uniformly among all incident half-edges, retaining loops and multiple edges. With the corner measure as the stationary law, the deterministic time acceleration is exactly the number of map edges. For any deterministic metric scale giving the metric-measure limit, convergence retains that same surface and any fixed finite number of conditionally independent walks with their time parameters.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Random-Walks-on-Critical-FK-Ising-Maps-and-Liouville-Brownian-Motion-October-5-2026/fk-ising-walk-limit.pdf).

## Spectral convergence for critical FK–Ising planar maps

Using the conformal and metric-measure companion results and the stated Brownian/Liouville quantum gravity inputs, we prove spectral convergence for critical spherical FK–Ising maps to Liouville Brownian motion on the ordinary unit-area $\sqrt3$-quantum sphere. The discrete walk has total attempt rate one, uses every map edge including loops and multiplicities, and has the corner measure as its stationary law. Accelerating time by the number of map edges gives joint convergence of the metric-measure space, all ordered eigenvalues with multiplicities and padding, and the heat trace locally uniformly at strictly positive times. The conductivity and clock constant are one in these conventions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Spectral-convergence-for-critical-FK-Ising-planar-maps-October-5-2026/spectral-convergence-critical-fk-ising-planar-maps.pdf).

## A Linear Clock for Random Walk on Tree-Weighted Planar Maps

We prove that stationary random walk on a planar map sampled with weight equal to its number of spanning trees converges to Liouville Brownian motion on the unit-area $\sqrt2$-Liouville quantum sphere. The convergence retains the conditional path law jointly with the measured metric space. The walk chooses uniformly among all incident half-edges and starts from the stationary degree measure. For total attempt rate one and the continuum Dirichlet form with factor 1/2, the time acceleration is exactly the number of map edges. The result uses the companion contour and metric limits for this same ensemble.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Linear-Clock-for-Random-Walk-on-Tree-Weighted-Planar-Maps-October-5-2026/linear-clock-random-walk-tree-weighted-planar-maps.pdf).

## Canonical conformal limits of subcritical FK planar maps

For every fixed $0\lt q\lt 4$, we prove joint convergence of spherical Fortuin–Kasteleyn planar maps in their flag-triangle uniformization to the corresponding unit-area Liouville quantum gravity sphere decorated by an independent conformal loop ensemble. The convergence includes the area measure, deterministically rescaled graph distances between all vertex pairs, and the full nested interface collection, with interfaces converging uniformly up to reparameterization.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Canonical-conformal-limits-of-subcritical-FK-planar-maps-September-24-2026/main.pdf).

## The critical Liouville quantum sphere and geometric limits of FK maps at q=4

We construct the field and area law of the unit-area critical Liouville quantum sphere as a limit of ordinary subcritical quantum spheres, and equip it with its critical intrinsic metric. We then prove that spherical Fortuin–Kasteleyn planar maps at *q* = 4, embedded by their equilateral flag uniformizations, converge jointly to this sphere decorated by an independent nested conformal loop ensemble CLE$_{4}$. With deterministic distance normalization, the convergence includes the area measure, the full embedded distance function, and every macroscopic interface through all positive integer edge counts.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-critical-Liouville-quantum-sphere-and-geometric-limits-of-FK-maps-at-q-equals-4-September-24-2026/main.pdf).

## Metric-measure limits of subcritical FK and spanning-tree planar maps

We resolve the finite spherical cases of Gwynne and Miller's graph-metric conjecture for critical Fortuin–Kasteleyn maps at each fixed $q\in(0,4)$ and for uniform spanning-tree-decorated maps. After deterministic rescaling of graph distances, these maps, equipped with the vertex probability measure proportional to degree, converge in Gromov–Hausdorff–Prokhorov law to their ordinary unit-area Liouville quantum gravity spheres. Distances use every primal edge, and convergence holds through all positive integer edge counts.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Metric-measure-limits-of-subcritical-FK-and-spanning-tree-planar-maps-September-24-2026/main.pdf).

## Brownian continuum random tree limits of finite Fortuin–Kasteleyn maps above four

We prove the finite-volume continuum-random-tree prediction for critical Fortuin–Kasteleyn planar maps at every fixed *q* > 4. After rescaling graph distances by a constant times $n^{−1/2}$, an *n*-edge map with normalized degree measure converges to the Brownian continuum random tree in the Gromov–Hausdorff–Prokhorov topology. The convergence holds through all positive integer sizes.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Brownian-continuum-random-tree-limits-of-finite-Fortuin-Kasteleyn-maps-above-four-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

For every fixed $q>4$, the formalization proves the Brownian continuum-random-tree limit for critical finite Fortuin–Kasteleyn planar maps. After rescaling graph distances in an $n$-edge map by a constant depending on $q$ times $n^{-1/2}$ and using normalized degree measure, the metric-measure space converges in distribution to the Brownian continuum random tree in the Gromov–Hausdorff–Prokhorov topology. The convergence holds through all positive integer sizes.

## Lean: Brownian continuum-random-tree limit for finite FK maps

Stated in [FKCRT.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FKCRT.lean).

```lean
theorem finite_fk_maps_converge_to_brownian_crt : MainStatement
```

Proved in [lean/OAI/Probability/FKMaps/Convergence.lean, line 68](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/FKMaps/Convergence.lean#L68).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/211.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/211.md)
