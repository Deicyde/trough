---
declaration: section
origin: cited
lean: Flow.omegaLimit_singleton_subset_of_isClosed, Flow.exists_forall_eq_of_mem_omegaLimit, Flow.lasalle
statement: formalized
proof: formalized
---

# LaSalle's invariance principle

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/lasalle-s-invariance-principle/index.html).

## Omega-limit set lies in every closed set containing the orbit

The ω-limit set of a point under a semiflow is contained in every closed set that contains
the forward orbit.

Formalized by `Flow.omegaLimit_singleton_subset_of_isClosed`, a theorem declared in [MathlibExt/Dynamics/LaSalle.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/LaSalle.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/lasalle-s-invariance-principle/index.html#omega-limit-singleton-subset-of-is-close).

## `V` is constant on the ω-limit set

If the forward orbit of `x` lies in a compact set
`K` and the continuous function `V` is nonincreasing along it, then there is a constant `c`
(the limit of `V(ϕ t x)`) such that `V(ϕ t y) = c` for every `y ∈ ω⁺(x)` and every `t ≥ 0`.

Formalized by `Flow.exists_forall_eq_of_mem_omegaLimit`, a theorem declared in [MathlibExt/Dynamics/LaSalle.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/LaSalle.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/lasalle-s-invariance-principle/index.html#exists-forall-eq-of-mem-omega-limit).

## LaSalle's invariance principle

**LaSalle's invariance principle** (LaSalle 1960; Khalil 2002, Theorem 4.4). Let the forward
orbit of `x` under the semiflow `ϕ` lie in a compact set `K`, let `V` be continuous and
nonincreasing along that orbit, and let `E` contain every `y ∈ K` whose orbit keeps `V`
constant. Then the ω-limit set `ω⁺(x)` is nonempty and contained in the largest
forward-invariant subset `M = {y | ∀ t, ϕ t y ∈ E}` of `E`, and the orbit of `x` eventually
enters every open set containing `M`.

Formalized by `Flow.lasalle`, a theorem declared in [MathlibExt/Dynamics/LaSalle.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/LaSalle.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/lasalle-s-invariance-principle/index.html#lasalle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: LaSalle's invariance principle](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/lasalle-s-invariance-principle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/smooth-dynamics/lasalle-s-invariance-principle)
