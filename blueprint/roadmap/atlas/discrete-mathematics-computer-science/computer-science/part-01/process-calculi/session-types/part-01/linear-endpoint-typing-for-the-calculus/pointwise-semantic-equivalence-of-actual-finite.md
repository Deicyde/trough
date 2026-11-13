---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.ContextEquivalent, Cslib.SessionTypes.Endpoint.ContextEquivalent.refl, Cslib.SessionTypes.Endpoint.ContextEquivalent.lookup, Cslib.SessionTypes.Endpoint.ContextEquivalent.symm, Cslib.SessionTypes.Endpoint.ContextEquivalent.trans, Cslib.SessionTypes.Endpoint.ContextEquivalent.mem_iff, Cslib.SessionTypes.Endpoint.ContextEquivalent.completed, Cslib.SessionTypes.Endpoint.ContextEquivalent.scope
statement: formalized
proof: formalized
---

# Pointwise semantic equivalence of actual finite ownership maps

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html).

## Endpoint

## Pointwise equivalence of ownership maps

Same lookup domain, identical enclosing capability ranks, and equivalent
protocol trees. No matching split or retyping result is stored.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#context-equivalent).

## Reflexivity of ownership-map equivalence

Reflexivity of actual matching lookups.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.refl`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#refl).

## Lookups transfer along ownership-map equivalence

Matching source lookup yields an actual target binding and rank/tree relation.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.lookup`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#lookup).

## Symmetry of ownership-map equivalence

Symmetry includes both absent and present endpoints.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.symm`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#symm).

## Transitivity of ownership-map equivalence

Transitivity requires the same intermediate lookup, not a chosen representative.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.trans`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#trans).

## Equivalent ownership maps have the same keys

Exact key-domain invariance.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.mem_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#mem-iff).

## Ownership-map equivalence preserves completion

Completion invariance uses actual unfolded done, not just empty ownership.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#completed).

## Ownership-map equivalence preserves key scoping

Scope of every actual owned key is unchanged with the exact domain.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.scope`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#scope).

## Equivalent insertions preserve ownership-map equivalence

Corresponding insertions preserve literal rank and semantic type equivalence.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#insert).

## Erasure preserves ownership-map equivalence

Both sides erase precisely the same key.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#erase).

## Ownership-map equivalence from two-way lookup correspondence

Bidirectional actual lookup correspondence suffices for Option.Rel.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.of_lookups`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#of-lookups).

## Union preserves ownership-map equivalence

Left-biased unions respect equivalent key domains on BOTH sides.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#union).

## Lifting preserves ownership-map equivalence

Canonical binder lift preserves corresponding values and exact domains.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#lift).

## Binding equivalent fresh pairs preserves ownership-map equivalence

A chosen exact dual private pair can be preserved or equivalently changed.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#bind).

## Ownership-map equivalence preserves semantic compatibility

Semantic compatibility is invariant, including explicit enclosing ranks.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.compatible`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#compatible).

## Projection of an ownership map onto another map's keys

Restrict actual target bindings to the exact key domain of a source map.
The implementation is canonical multiset filtering, not a new finite map.

Formalized by `Cslib.SessionTypes.Endpoint.Context.projectKeys`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#project-keys).

## Lookups in a key projection

Projection retains precisely the actual target binding at a source key.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_projectKeys`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#lookup-project-keys).

## Keys of a projection are the intersection of domains

The projected domain is the exact intersection of actual owned domains.

Formalized by `Cslib.SessionTypes.Endpoint.Context.mem_projectKeys`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#mem-project-keys).

## Key projection is absent outside the source domain

Outside a source domain the projection is literally absent.

Formalized by `Cslib.SessionTypes.Endpoint.Context.projectKeys_none`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#project-keys-none).

## Key projection agrees with the target inside the source domain

Inside a source domain the actual target value is retained verbatim.

Formalized by `Cslib.SessionTypes.Endpoint.Context.projectKeys_lookup`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#project-keys-lookup).

## Equivalence of a union restricts to its left part

An equivalent whole map induces an equivalent child with the exact source
key domain; no matching target split is supplied by a caller.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.project_left`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#project-left).

## Equivalence of a disjoint union splits into equivalent parts

GENERAL split derivation from source disjointness and whole-map equivalence.
It preserves each child domain and the exact target finite-map union.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.split`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#split).

## Equivalent capabilities give equivalent singleton maps

Equivalent singleton capabilities preserve their exact polarized key.

Formalized by `Cslib.SessionTypes.Endpoint.ContextEquivalent.singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextEquivalence.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html#singleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pointwise semantic equivalence of actual finite ownership maps](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/pointwise-semantic-equivalence-of-actual-finite)
