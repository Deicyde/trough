---
declaration: section
origin: cited
lean: LinearMap.trace_eq_trace_restrict_add_trace_mapQ, LinearMap.trace_eq_trace_restrict_ker_add_of_surjective
statement: formalized
proof: formalized
---

# Trace on invariant subspaces

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/trace-on-invariant-subspaces/index.html).

## Trace is additive over an invariant subspace

Let $V$ be a finite-dimensional vector space
over a field $K$, let $e$ be a linear endomorphism of $V$, and let $W$ be a subspace of $V$ with
$e(W) \subseteq W$. Then the trace of $e$ equals the trace of the restriction $e|_W$ of $e$ to $W$
plus the trace of the endomorphism $\bar e$ of the quotient $V/W$ induced by $e$:
$\operatorname{tr}(e) = \operatorname{tr}(e|_W) + \operatorname{tr}(\bar e)$.

Formalized by `LinearMap.trace_eq_trace_restrict_add_trace_mapQ`, a theorem declared in [MathlibExt/LinearAlgebra/Trace/InvariantSubmodule.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Trace/InvariantSubmodule.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/trace-on-invariant-subspaces/index.html#trace-eq-trace-restrict-add-trace-map-q).

## Trace splits along a surjective intertwining map

Let $V$ be a finite-dimensional vector
space over a field $K$, let $W$ be a vector space over $K$, and let $q : V \to W$ be a surjective
linear map. If $f$ is a linear endomorphism of $V$ and $g$ a linear endomorphism of $W$ with
$q \circ f = g \circ q$, then $f$ maps $\ker q$ into itself, and the trace of $f$ equals the
trace of the restriction $f|_{\ker q}$ of $f$ to $\ker q$ plus the trace of $g$.

Formalized by `LinearMap.trace_eq_trace_restrict_ker_add_of_surjective`, a theorem declared in [MathlibExt/LinearAlgebra/Trace/InvariantSubmodule.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Trace/InvariantSubmodule.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/trace-on-invariant-subspaces/index.html#trace-eq-trace-restrict-ker-add-of-surje).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trace on invariant subspaces](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/trace-on-invariant-subspaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/linear-maps-and-duality/trace-on-invariant-subspaces)
