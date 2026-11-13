---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.HasUnguardedInput, Cslib.SessionTypes.Endpoint.input_cong, Cslib.SessionTypes.Endpoint.input_select, Cslib.SessionTypes.Endpoint.Step.source_hasUnguardedInput, Cslib.SessionTypes.Endpoint.NameAbsent, Cslib.SessionTypes.Endpoint.NameAbsent.out_payload, Cslib.SessionTypes.Endpoint.nameAbsent_fresh_lift, Cslib.SessionTypes.Endpoint.substName_liftName
statement: formalized
proof: formalized
---

# Subject reduction for endpoint typing

143 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/index.html).

## Unguarded input in a process

An input is exposed outside every communication guard.

Formalized by `Cslib.SessionTypes.Endpoint.HasUnguardedInput`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#has-unguarded-input).

## Structural congruence preserves unguarded inputs

Every existing structural congruence preserves exposed input presence.

Formalized by `Cslib.SessionTypes.Endpoint.input_cong`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#input-cong).

## Selection reflects unguarded inputs

Selection cannot hide an input that is present in its selected term.

Formalized by `Cslib.SessionTypes.Endpoint.input_select`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#input-select).

## Every π step source has an unguarded input

Every existing π step requires an exposed input in its source,
including pre-congruence, selection, context closure and replication folding.

Formalized by `Cslib.SessionTypes.Endpoint.Step.source_hasUnguardedInput`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/InputInvariant.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#source-has-unguarded-input).

## Absence of a physical name from a process

The given physical name occurs in no subject, payload or continuation
position. Existing binders shift the tracked outer name with canonical lift.

Formalized by `Cslib.SessionTypes.Endpoint.NameAbsent`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameAbsence.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameAbsence.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#name-absent).

## An output payload name is not absent

A transmitted endpoint payload is an occurrence, even when completed.

Formalized by `Cslib.SessionTypes.Endpoint.NameAbsent.out_payload`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameAbsence.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameAbsence.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#out-payload).

## The inserted name is absent from a lifted process

The inserted name is absent from every position of the actual lifted
π term, including payloads and all nested input/restriction binders.

Formalized by `Cslib.SessionTypes.Endpoint.nameAbsent_fresh_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameAbsence.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameAbsence.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#name-absent-fresh-lift).

## Substitution cancels name lifting

Substitution removes an inserted binder without changing its shifted
outer names. The inserted binder's replacement is arbitrary.

Formalized by `Cslib.SessionTypes.Endpoint.substName_liftName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#subst-name-lift-name).

## Substitution cancels process lifting

Removing an inserted binder cancels lifting throughout the unchanged
π syntax, including nested inputs, restrictions, choice and replication.

Formalized by `Cslib.SessionTypes.Endpoint.substProc_liftProc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#subst-proc-lift-proc).

## Injectivity of name lifting

Binder lifting cannot identify two physical names.

Formalized by `Cslib.SessionTypes.Endpoint.liftName_injective`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#lift-name-injective).

## Name swap is an involution

Swapping the same two existing binders twice restores a name.

Formalized by `Cslib.SessionTypes.Endpoint.swapNameAt_swapNameAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#swap-name-at-swap-name-at).

## Process swap is an involution

Existing process swapping is likewise involutive under every binder.

Formalized by `Cslib.SessionTypes.Endpoint.swapProc_swapProc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#swap-proc-swap-proc).

## A lifted name is never the innermost binder

Existing outer names cannot become the fresh innermost binder.

Formalized by `Cslib.SessionTypes.Endpoint.liftName_zero_ne_var_zero`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#lift-name-zero-ne-var-zero).

## Commuting a name lift past a lift at cutoff zero

Lifting commutes with entering the innermost name binder.

Formalized by `Cslib.SessionTypes.Endpoint.liftName_liftName_zero`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#lift-name-lift-name-zero).

## Commutation of name lifts at ordered cutoffs

Arbitrary-cutoff lift fusion, including the cutoffs reached under input
and restriction binders.

Formalized by `Cslib.SessionTypes.Endpoint.liftName_liftName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#lift-name-lift-name).

## Commutation of process lifts at ordered cutoffs

Lift fusion throughout existing π syntax, at arbitrary ordered cutoffs.

Formalized by `Cslib.SessionTypes.Endpoint.liftProc_liftProc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#lift-proc-lift-proc).

## Lifting preserves and reflects name scoping

At an actual ambient cutoff, lifting reflects as well as preserves
canonical name scoping. It is not a second scope definition.

Formalized by `Cslib.SessionTypes.Endpoint.closedAt_liftName_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#closed-at-lift-name-iff).

## Injectivity of name swapping

Swapping existing binders cannot identify physical names.

Formalized by `Cslib.SessionTypes.Endpoint.swapNameAt_injective`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#swap-name-at-injective).

## A lifted key is never a freshly bound key

A lifted outer key can never be either freshly bound role at var zero.

Formalized by `Cslib.SessionTypes.Endpoint.Key.lift_ne_bound`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/NameTransport.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#lift-ne-bound).

## Weakening by an unused completed endpoint

An unused completed endpoint may be added through every current typing
constructor. Scope and freshness are explicit; active weakening is not admitted.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.weaken_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/EndWeakening.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/EndWeakening.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-01/index.html#weaken-completed).

## Weakening by a disjoint completed context

A disjoint completed context can be reattached to any typed process,
with the exact finite-map union required by parallel-nil congruence.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.weaken_completed_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/EndWeakening.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/EndWeakening.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#weaken-completed-union).

## Removing a parallel nil preserves endpoint typing

Removing a parallel nil reattaches exactly its completed ownership;
no active capability is silently dropped.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.par_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/EndWeakening.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/EndWeakening.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#par-nil-elim).

## Extension of a name map under a binder

Extend a name transformation under one existing input/ν binder.

Formalized by `Cslib.SessionTypes.Endpoint.under`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#under).

## Extended name map commutes with lifting outer names

The new binder is fixed and outer names are transformed capture-safely.

Formalized by `Cslib.SessionTypes.Endpoint.under_lift_zero`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#under-lift-zero).

## Capture-safe renaming of processes

Capture-safe name transformation of existing processes. Binder bodies
use `under`; this introduces no new syntax or transition relation.

Formalized by `Cslib.SessionTypes.Endpoint.mapProc`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#map-proc).

## Extending a scoped name map under a binder keeps it scoped

Extending a scoped transformation under a binder preserves the
canonical scope relation at the incremented source and target depths.

Formalized by `Cslib.SessionTypes.Endpoint.under_scoped`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#under-scoped).

## Extending a lift under a binder raises its cutoff

Under a binder, canonical lifting increases its cutoff by one.

Formalized by `Cslib.SessionTypes.Endpoint.under_liftName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#under-lift-name).

## Process renaming by a lift is process lifting

The generic syntax transformation specializes to the existing π lift.

Formalized by `Cslib.SessionTypes.Endpoint.mapProc_liftName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#map-proc-lift-name).

## Extending a substitution under a binder raises its cutoff

Under an existing binder, substitution lifts its replacement and
increments its cutoff, exactly as PiCalculus.substProc does.

Formalized by `Cslib.SessionTypes.Endpoint.under_substName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#under-subst-name).

## Process renaming by a substitution is process substitution

Subject and payload substitution are exactly the canonical π operation,
including through all input and restriction binders.

Formalized by `Cslib.SessionTypes.Endpoint.mapProc_substName`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#map-proc-subst-name).

## Capture-safe renaming preserves process scope

Capture-safe syntax transport preserves the canonical process scope.

Formalized by `Cslib.SessionTypes.Endpoint.mapProc_closedAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#map-proc-closed-at).

## Extending a swap under a binder shifts both indices

Extending a restriction swap under a binder shifts both swapped indices.

Formalized by `Cslib.SessionTypes.Endpoint.under_swapNameAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#under-swap-name-at).

## Process renaming by a swap is the restriction swap

The generic capture-safe map specializes to the existing π restriction swap.

Formalized by `Cslib.SessionTypes.Endpoint.mapProc_swapNameAt`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Renaming.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#map-proc-swap-name-at).

## Collision-free renaming preserves endpoint typing

Capture-safe rekeying transports all finite-process endpoint typing,
including linear payloads and actual input/ν binders. Collision freedom is
required only on owned keys and can be derived from a delegation split.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.rename`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RenameTyping.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RenameTyping.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#rename).

## Binder lifting preserves endpoint typing

Any ambient binder lift transports full endpoint typing without
changing protocols, roles or resource multiplicity.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/RenameTyping.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/RenameTyping.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#lift).

## Lifting preserves and reflects process scoping

Lifting reflects canonical process scoping at an ambient cutoff.

Formalized by `Cslib.SessionTypes.Endpoint.closedAt_liftProc_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#closed-at-lift-proc-iff).

## Swapping binders in scope preserves name scoping

Swapping two binders inside the ambient scope preserves the canonical
name predicate in both directions.

Formalized by `Cslib.SessionTypes.Endpoint.closedAt_swapName_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#closed-at-swap-name-iff).

## Swapping binders in scope preserves process scoping

Scope preservation by swapping extends through every existing binder.

Formalized by `Cslib.SessionTypes.Endpoint.closedAt_swapProc_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#closed-at-swap-proc-iff).

## Structural congruence preserves process scoping

Every existing structural congruence transports canonical π scoping,
including scope extrusion, restriction swapping and replication folding.

Formalized by `Cslib.SessionTypes.Endpoint.closedAt_cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#closed-at-cong-iff).

## Choice selection preserves process scoping

Selection preserves canonical scope even when actual guarded choices
are present in the existing π syntax.

Formalized by `Cslib.SessionTypes.Endpoint.closedAt_select`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-02/index.html#closed-at-select).

## Reduction steps preserve process scoping

Every existing π step preserves canonical scope, not just direct
head communication. Substitution is the existing capture-avoiding one.

Formalized by `Cslib.SessionTypes.Endpoint.closedAt_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTransport.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#closed-at-step).

## Endpoint typing drops a role whose name does not occur

A role can be erased when its physical name is absent from every
subject, payload and binder-adjusted continuation position of the typed term.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.erase_nameAbsent`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Strengthening.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Strengthening.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#erase-name-absent).

## Owned capability with an absent name is completed

An owned capability with no physical-name occurrence must already be
completed. This is derived from typing, including endpoint payload positions.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.absent_lookup_completed`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Strengthening.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Strengthening.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#absent-lookup-completed).

## Substitution cancels lifting on endpoint keys

Substitution cancels binder lift on an entire polarized endpoint key.

Formalized by `Cslib.SessionTypes.Endpoint.Key.subst_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#subst-lift).

## Received-endpoint substitution is injective when the role is fresh

Linear input substitution is collision-free when the transmitted role
was absent from the receiver. Its opposite physical-name role is allowed.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_received_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#inj-on-received-subst).

## Received-endpoint substitution moves the bound role to the sent key

Subject substitution consumes the bound role and inserts exactly the
sent key, preserving every other capability and permitting its peer role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_received_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#rekey-received-subst).

## Endpoint typing under substitution of a transmitted endpoint

Receiving a linear endpoint substitutes its physical name in ALL
subject and payload positions, removes the bound role and inserts the sent
role exactly once. Capture under input and ν is the canonical π substitution.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.subst_endpoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#subst-endpoint).

## Linear subject substitution with freshness from disjoint ownership

Linear subject substitution with non-aliasing DERIVED from disjoint
sender/receiver ownership and the receiver's already-owned carrier.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.subst_endpoint_from_split`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#subst-endpoint-from-split).

## Passive substitution leaves the linear context unchanged

Passive input substitution changes no linear context: every owned
key is a lifted outer key, so the input binder owns no endpoint role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_passive_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#rekey-passive-subst).

## Passive substitution is injective on lifted outer keys

Passive substitution is collision-free on all lifted outer endpoint keys.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_passive_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#inj-on-passive-subst).

## Endpoint typing under passive name substitution

Passive payload substitution preserves every linear obligation and
cannot introduce an endpoint subject capability.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.subst_passive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Substitution.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#subst-passive).

## Communicating subjects in a compatible split have dual capabilities

Disjoint complementary subjects in a compatible interface have exactly
dual protocol capabilities, including their ranks and endpoint payload sorts.

Formalized by `Cslib.SessionTypes.Endpoint.communicating_capabilities_dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#communicating-capabilities-dual).

## Dual of a passive send head is a passive receive head

Actual endpoint protocols and rank equality force matching passive
receive guards at a complementary owned role.

Formalized by `Cslib.SessionTypes.Endpoint.passive_dual_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#passive-dual-head).

## Passive-payload communication preserves endpoint typing

At a compatible combined interface with the stated disjoint typed split
and scoped passive payload, head communication advances the two complementary
roles and no other capability in the exact residual context.

Formalized by `Cslib.SessionTypes.Endpoint.passive_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#passive-head-preservation).

## Dual of an endpoint send head is an endpoint receive head

Duality preserves a delegated payload's role/rank/protocol while
reversing only the subject continuation.

Formalized by `Cslib.SessionTypes.Endpoint.endpoint_dual_head`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#endpoint-dual-head).

## Communicating subjects in a compatible split have equal ranks

For disjoint owned same-name roles in a compatible combined interface,
their capability ranks agree, as required by exact capability duality.

Formalized by `Cslib.SessionTypes.Endpoint.communicating_ranks_equal`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#communicating-ranks-equal).

## Endpoint-delegating communication preserves typing

At a compatible combined interface with the stated disjoint typed split,
owned payload distinct from the carrier and scoped payload name, endpoint
communication transfers the payload role once and advances only the carrier.

Formalized by `Cslib.SessionTypes.Endpoint.endpoint_head_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#endpoint-head-preservation).

## Head communication preserves endpoint typing

For a typed opposite-head pair at an initially compatible interface,
direct communication in the existing π syntax yields an exact typed residual
ownership context, including endpoint delegation.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.head_comm_preservation`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/Communication.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#head-comm-preservation).

## Matched output head of a capability

The actual payload kind and continuation of a matched output head.

Formalized by `Cslib.SessionTypes.Endpoint.MatchedOutput`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#matched-output).

## Capability whose head is a send with a given continuation

The old subject's actual head determines its literal continuation,
independently of whether the transmitted endpoint is external or ν-bound.

Formalized by `Cslib.SessionTypes.Endpoint.SendsTo`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-03/index.html#sends-to).

## A matched output head is a send with the same continuation

The detailed matched output determines the same literal continuation.

Formalized by `Cslib.SessionTypes.Endpoint.MatchedOutput.sendsTo`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#sends-to).

## Advancement of a matched dual subject pair

Only two actually matched dual subject capabilities advance. Payload
ownership transfer is invisible in the combined map; all other entries remain.
The payload can be private to a ν binder, so external advancement records its
protocol head rather than demanding external ownership of that payload.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#dual-advance).

## Head communication preserves typing and records the matched output

For a typed opposite-head pair at an initially compatible interface,
the packed result retains the literal send head, payload kind and continuation
correspondence instead of hiding an unconstrained protocol.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.head_comm_faithful`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#head-comm-faithful).

## Dual-continuation update leaves other lookups unchanged

Outside the two matched subjects, the entire capability is unchanged.

Formalized by `Cslib.SessionTypes.Endpoint.dual_update_lookup_other`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#dual-update-lookup-other).

## Subject lookup after a dual-continuation update

The matched subject's rank is retained at its exact continuation.

Formalized by `Cslib.SessionTypes.Endpoint.dual_update_lookup_subject`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#dual-update-lookup-subject).

## Dual advancement preserves the owned keys

Both matched old keys remain owned; the update creates no new key.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.mem_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#mem-iff).

## Dual-continuation update preserves compatibility

From a compatible initial interface, updating both subjects to dual
continuations preserves compatibility independently of process typing.

Formalized by `Cslib.SessionTypes.Endpoint.dual_update_compatible`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#dual-update-compatible).

## Dual advancement preserves compatibility

A faithful matched update retains compatibility if the initial
interface is compatible.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.compatible`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#compatible).

## Dual-continuation update preserves balance

Advancing a matched dual pair preserves full balance when the original
interface is balanced, including every untouched opposite-role obligation.

Formalized by `Cslib.SessionTypes.Endpoint.dual_update_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#dual-update-balanced).

## Dual advancement preserves balance

Faithful subject advancement retains balance if the initial external
interface is balanced.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#balanced).

## Head communication yields a dual advancement

A typed opposite-head pair at an initially compatible interface yields
a faithful matched update and a compatible typed residual via the packed result.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.head_comm_advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#head-comm-advance).

## Dual advancement preserves disjointness from a frame

A matched update leaves a disjoint ownership frame disjoint.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.disjoint_frame`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#disjoint-frame).

## Dual advancement in the left part of a union

A left parallel frame retains all its capabilities and the exact
subject head/rank/continuation correspondence of the actual update.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.frame_left`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#frame-left).

## Dual advancement in the right part of a disjoint union

A right parallel frame requires the actual disjoint ownership split,
so its matched entries cannot be shadowed by the left-biased union.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.frame_right`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAdvance.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#frame-right).

## Swapping two ambient binders in an ownership context

Swap ownership of two existing ambient binders without altering any role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.swap`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#swap).

## Binder swapping preserves endpoint typing

Canonical swapping preserves full finite-process endpoint typing.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#swap-2).

## Context swapping commutes with insertion

Swapping maps an inserted capability to the swapped role key verbatim.

Formalized by `Cslib.SessionTypes.Endpoint.Context.swap_insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#swap-insert).

## Swapping the two innermost binders fixes a twice-lifted context

Two lifts put all outer names above both swapped binder indices.

Formalized by `Cslib.SessionTypes.Endpoint.Context.swap_double_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#swap-double-lift).

## Swapping nested restrictions exchanges their bound pairs

Swapping nested restrictions exchanges their complete dual pairs and
fixes all lifted outer ownership, rather than forgetting any bound capability.

Formalized by `Cslib.SessionTypes.Endpoint.Context.swap_bind_bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SwapTyping.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#swap-bind-bind).

## Matching send and receive heads of two capabilities

Both literal communication heads, with separate payload equivalence.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.CommunicationHeads`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-04/index.html#communication-heads).

## Semantic advancement of a communicating endpoint pair

Actual old sender/peer values and literal continuations, not raw dual-code
identity. Target is EXACTLY the two actual subject insertions.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance`, an inductive type declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#semantic-advance).

## Semantic balance of a linear context

Every actual owned key has a semantic dual peer at equal capability rank.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Balanced`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#balanced).

## Semantic balance implies semantic compatibility

Semantic balance supplies semantic compatibility by actual lookup uniqueness.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Balanced.compatible`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#compatible).

## The empty context is semantically balanced

Empty interface balance is not a completion assertion about private work.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.balanced_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#balanced-empty).

## Raw balance implies semantic balance

Literal raw balance is a special case, not the semantic definition.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.balanced_of_raw`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#balanced-of-raw).

## Semantic advancement preserves the context's domain

Exact domain preservation includes completed capabilities.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.mem_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#mem-iff).

## Semantic advancement preserves disjointness from a frame

No new key can conflict with a parallel ownership frame.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.disjoint_frame`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#disjoint-frame).

## Semantic advancement preserves scoping of owned keys

Canonical scope of the whole owned domain is preserved.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.scope`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#scope).

## Semantic advancement preserves compatibility

Actual compatible source retains semantic duality after the exact update.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.compatible`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#compatible-2).

## Semantic advancement preserves balance

From a semantically balanced initial interface, actual advancement retains
balance with exact old keys and actual new codes.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#balanced-2).

## Semantic advancement extends from the left part to the whole union

Left frame preserves actual old lookups and all literal head evidence.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.frame_left`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#frame-left).

## Semantic advancement extends from the right part to a disjoint union

Right frame uses actual disjointness so neither old subject is shadowed.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.frame_right`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#frame-right).

## Literally dual capabilities have literally dual continuations

Literal duality of the ORIGINAL codes forces literal tail equality.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.CommunicationHeads.literal_dual_tail`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#literal-dual-tail).

## Communication heads give a send-head observation

The existing raw send-head observation is reused only as a pure head fact.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.CommunicationHeads.sendsTo`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#sends-to).

## Raw dual advancement is a semantic advancement

Raw actual dual-code advancement embeds into the semantic relation.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.of_raw`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#of-raw).

## Semantic advancement is raw under literal compatibility

Reverse bridge requires literal ORIGINAL peer compatibility, not merely
semantic compatibility or residual retyping.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.to_raw`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#to-raw).

## Lifting preserves semantic advancement

Canonical lifting preserves actual heads, ranks and code-valued payloads.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#lift).

## Binder swapping preserves semantic advancement

Canonical swapping permutes only subject keys, never the protocol codes.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#swap).

## Typed head communication yields a semantic advancement

A typed opposite-head pair at an initially semantically compatible interface
yields a faithful semantic advance and a compatible typed residual.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.HasType.head_advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#head-advance).

## Semantic advancement preserves capability ranks

Every actual capability retains its enclosing rank at the same key.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.rank_lookup`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticAdvance.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-05/index.html#rank-lookup).

## Lowering then lifting an outer key returns it

Canonical lowering and lifting cancel for a polarized outer key,
provided it is not either role of the freshly inserted physical name.

Formalized by `Cslib.SessionTypes.Endpoint.Key.lift_subst_outer_name`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#lift-subst-outer-name).

## Lowering is injective on contexts without fresh-name keys

Canonical lowering is injective on an outer context with no fresh-name
role. The inverse is canonical lift, not a guessed fresh constant identity.

Formalized by `Cslib.SessionTypes.Endpoint.Context.injOn_lower`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#inj-on-lower).

## Lowering of an outer context past a fresh binder

Remove a fresh ambient binder from a finite outer ownership context.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lower`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#lower).

## Lifting a lowered context recovers it

Lifting the recovered outer context restores every key and capability.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_lower`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#lift-lower).

## Endpoint typing reflects through binder lifting

Typing an actually lifted term under outer-only ownership reflects
back to its exact recovered context; no closed-hole premise is required.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.unlift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#unlift).

## Erasing both roles of the fresh name leaves outer keys

Removing both roles of var zero leaves only genuine outer-name keys.

Formalized by `Cslib.SessionTypes.Endpoint.Context.erased_pair_outer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#erased-pair-outer).

## Context lifting is injective

Canonical context lifting is injective, including recorded completed slots.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_zero_injective`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#lift-zero-injective).

## Lowering preserves disjointness of outer contexts

Lowering disjoint outer-only contexts preserves their exact key split.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_lower`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/UnliftContext.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#disjoint-lower).

## Outer insertion commutes with binding a fresh pair

Installing an outer capability commutes with the entire fresh bound pair.

Formalized by `Cslib.SessionTypes.Endpoint.Context.bind_insert_outer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#bind-insert-outer).

## Updating both bound roles, positive first, rebinds the pair

Two updates at the fresh positive/negative roles replace only the
bound capability pair and retain the entire lifted external context.

Formalized by `Cslib.SessionTypes.Endpoint.Context.update_bound_positive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#update-bound-positive).

## Updating both bound roles, negative first, rebinds the pair

A negative sender installs the dual continuation on the positive role;
reordering the distinct insertions retains the same complete bound pair.

Formalized by `Cslib.SessionTypes.Endpoint.Context.update_bound_negative`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#update-bound-negative).

## Outer lookups pass through a freshly bound pair

An outer lifted role lookup passes through both fresh bound entries
and reflects to the exact old external capability.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_bind_outer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#lookup-bind-outer).

## Dual advancement under restriction splits into inner and outer cases

Exact pure restriction projection. An internal matched pair changes
only the bound pair at the same rank; an outer matched pair changes only the
external context and retains the entire old bound pair.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.project_bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#project-bind).

## Outer dual advancement lifts through restriction

An actual external matched update lifts through restriction without
altering its private pair, even when the payload protocol refers to private data.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.bind_outer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#bind-outer).

## Dual advancement under restriction splits, keeping the private step

Projection additionally retains an actual private old-head/continuation
transition when the communication is hidden by ν. It does not reduce private
advancement to an arbitrary capability with the same rank.

Formalized by `Cslib.SessionTypes.Endpoint.DualAdvance.project_bind_faithful`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/AdvanceProjection.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#project-bind-faithful).

## Inversion of endpoint typing for restriction

Restriction inversion exposes the actual bound dual pair.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nu_inv`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#nu-inv).

## Endpoint typing is preserved by forward scope extrusion

The forward canonical scope rule preserves the exact external context
and ambient depth, with the dual pair derived from restriction typing.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.scope_forward`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#scope-forward).

## Endpoint typing absorbs a role absent from its parallel partner

A role missing from one component can be reattached only after actual
absence in its typed partner derives completion of the advertised capability.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.insert_from_absent_partner`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#insert-from-absent-partner).

## Endpoint typing restores both bound roles to the restricted side

In the actual scope split, either freshly bound role can be moved
back to the restricted component only when partner absence proves it completed.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.restore_scope_pair`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#restore-scope-pair).

## Endpoint typing is preserved by reverse scope extrusion

Reverse scope transport recovers the exact external ownership split
from the actual restriction/parallel typing, with no closed-hole premise.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.scope_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-06/index.html#scope-reverse).

## Endpoint typing is invariant under scope extrusion

Both directions of the canonical scope congruence preserve exact
external polarized ownership and the unchanged ambient binder depth.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.scope_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ScopeTyping.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#scope-iff).

## Parallel commutation preserves endpoint typing

Parallel commutation swaps a derived disjoint split, not its capabilities.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.par_comm`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#par-comm).

## Parallel reassociation preserves endpoint typing

Parallel reassociation preserves the actual three-way disjoint split.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.par_assoc`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#par-assoc).

## Reverse parallel reassociation preserves endpoint typing

Reverse reassociation recovers both sub-splits from the supplied typing.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.par_assoc_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#par-assoc-reverse).

## Adding a parallel nil preserves endpoint typing

Adding a parallel nil allocates it no ownership; no active slot is dropped.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.par_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#par-nil-intro).

## Removing a restriction around nil preserves endpoint typing

Restriction of nil has exactly the completed external ownership of nil.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nu_nil_elim`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#nu-nil-elim).

## Adding a restriction around nil preserves endpoint typing

A completed fresh pair may be introduced around nil while retaining
all original external capabilities and scope.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nu_nil_intro`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#nu-nil-intro).

## Swapping nested restrictions preserves endpoint typing

Nested restriction commutation swaps their derived complete dual pairs.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nu_swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#nu-swap).

## Reverse restriction swap preserves endpoint typing

Reverse nested restriction commutation uses the canonical involution.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.nu_swap_reverse`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#nu-swap-reverse).

## Structural congruence preserves endpoint typing

Every existing canonical structural congruence preserves endpoint typing
in both directions with exactly the same depth and ownership. Unsupported
choice/replication shapes are rejected by the typing-derived finite invariant.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.cong_iff`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/CongTyping.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#cong-iff).

## Compatibility restricts to the left part of a union

Left children inherit actual peer compatibility.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Compatible.union_left`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#union-left).

## Compatibility restricts to the right part of a disjoint union

A disjoint right child inherits actual peer compatibility without shadowing.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Compatible.union_right`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#union-right).

## Binding a dual private pair preserves compatibility

A chosen exact dual private pair extends a semantically compatible interface.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Compatible.bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#bind).

## Binding a dual private pair preserves balance

At a semantically balanced outer interface, binding an exact dual private
pair retains balance for the pair and every actual outer peer.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Balanced.bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#bind-2).

## Semantic advance under a private binding is private or outer

Faithful projection retains an actual private-pair advance OR the actual
outer advance and unchanged bound pair. It never chooses an arbitrary Xi.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.project_bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#project-bind).

## Outer semantic advances lift past a private binding

An actual outer semantic advance lifts without changing its private pair.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.SemanticAdvance.bind_outer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#bind-outer).

## Equivalent retyping preserves semantic balance

Pointwise semantic recoding retains actual paired domain and cap ranks.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Balanced.retype`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#retype).

## Union of disjoint balanced contexts is balanced

Disjoint balanced components form a balanced ownership frame union.

Formalized by `Cslib.SessionTypes.Endpoint.Conversion.Balanced.union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SemanticProjection.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#union).

## Injective rekeying preserves dual compatibility

Injective physical-name rekeying retains partial dual compatibility.

Formalized by `Cslib.SessionTypes.Endpoint.Compatible.rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#rekey).

## Binding a fresh dual pair preserves dual compatibility

A fresh complete bound pair extends any ordinary compatible interface.

Formalized by `Cslib.SessionTypes.Endpoint.Compatible.bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-07/index.html#bind-3).

## Subject reduction for endpoint typing at compatible interfaces

From a typed source at an initially compatible interface, all five
canonical reduction constructors preserve typing and compatibility, with one
matched external subject-pair advancement or an unchanged interface when
communication is private. No fragment or enabled-edge premise is required.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.subject_reduction`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-08/index.html#subject-reduction).

## Subject reduction for endpoint typing at balanced interfaces

A typed source with a balanced initial interface retains typing and balance
after any canonical step. Balance supplies the required compatibility; the
exact zero-or-one external advancement evidence is retained.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.subject_reduction_balanced`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-08/index.html#subject-reduction-balanced).

## Subject reduction for endpoint typing at the empty interface

An empty-interface typed network retains empty-interface typing through
any canonical step. The empty context is balanced, hence compatible, including
communication behind restrictions and pre/post congruence.

Formalized by `Cslib.SessionTypes.Endpoint.HasType.subject_reduction_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/SubjectReduction.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/part-08/index.html#subject-reduction-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subject reduction for endpoint typing](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/subject-reduction-for-endpoint-typing)
